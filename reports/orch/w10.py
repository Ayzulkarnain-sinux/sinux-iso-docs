#!/usr/bin/env python3
"""Perkakas orkestrator ISO-W10 (WORKER-ISO-03, LEAD G-4). Bukan perkakas dokumen; jalankan dari root repo.

  python3 -I reports/orch/w10.py terms [KEY..]   peta istilah STYLE §1.5 + diksi §2.5 (mekanis) -> reports/w10/terms/KEY.diff
  python3 -I reports/orch/w10.py td              meta.table_defaults di semua spec docx (G-4 butir 6)
  python3 -I reports/orch/w10.py xlsxinit        reports/w10/xlsx_sheets.json + op format di specs/KEY.w10.patch.json
  python3 -I reports/orch/w10.py build KEY..     render ke out/ + gerbang mesin -> reports/w10/gates/KEY.json
  python3 -I reports/orch/w10.py revert KEY..    kembalikan spec + out/ ke bed1bb6 (residu jam potong)
  python3 -I reports/orch/w10.py status
Basis substansi: bed1bb6. Xlsx dibangun dari out/ bed1bb6 + specs/KEY.w10.patch.json (sumber Drive tidak diunduh).
"""
import difflib, glob, json, os, re, shutil, subprocess, sys, tempfile

BASE = 'bed1bb6'
W = '/tmp/claude-0/w10'
LED = json.load(open('ledger.json', encoding='utf-8'))
DOCS = {d['key']: d for d in LED['docs'] if d['state'] == 'DONE'}
VALIDATOR = '/mnt/skills/public/docx/scripts/office/validate.py'
TD = {'align_left': True, 'repeat_header': True, 'cant_split': True}
STEPS_W = [7.6, 3.4, 5.0]
INSTR_H = ('petunjuk pengisian', 'cara mengisi', 'ketentuan pengisian')
TXT = ("import docx,sys;d=docx.Document(sys.argv[1]);print('\\n'.join(p.text for p in d.paragraphs));"
       "[print(' | '.join(c.text for c in r.cells)) for t in d.tables for r in t.rows]")
TXX = ("import openpyxl,sys;wb=openpyxl.load_workbook(sys.argv[1]);"
       "[print(ws.title, c.coordinate, c.value) for ws in wb.worksheets for r in ws.iter_rows() for c in r if c.value is not None]")

# Peta istilah STYLE §1.5 dan diksi §2.5. Urutan penting: frasa dua kata dulu.
RULES = [(r'tindakan korektif', 'corrective action'), (r'akar masalah', 'root cause'), (r'rekaman', 'record'),
         (r'tiket', 'ticket'), (r'formulir', 'form'), (r'peninjauan|tinjauan', 'review'), (r'lewat', 'melalui'),
         (r'sesudah', 'setelah')]
ENG = {'corrective action', 'root cause', 'record', 'ticket', 'form', 'review'}


def run(*a, **k):
    r = subprocess.run(a, capture_output=True, text=True, **k)
    return r.returncode, r.stdout, r.stderr


def ext(k):
    return 'xlsx' if DOCS[k]['mode'] == 'xlsx' else 'docx'


def base_file(k):
    p = f'{W}/base/{k}.{ext(k)}'
    if not os.path.exists(p):
        os.makedirs(f'{W}/base', exist_ok=True)
        open(p, 'wb').write(subprocess.run(['git', 'show', f'{BASE}:{DOCS[k]["out_path"]}'], capture_output=True).stdout)
    return p


def recase(src, eng):
    if src.isupper():
        return eng.upper()
    ws = src.split()
    if len(ws) > 1 and all(w[0].isupper() for w in ws):
        return ' '.join(w[0].upper() + w[1:] for w in eng.split())
    return eng[0].upper() + eng[1:] if src[0].isupper() else eng


def map_text(t):
    for pat, eng in RULES:
        def sub(m, eng=eng):
            w = recase(m.group(1), eng)
            return w + (('-nya' if eng in ENG else 'nya') if m.group(2) else '')
        t = re.sub(r'\b(' + pat + r')(nya)?\b', sub, t, flags=re.I)
    return t


def selftest_terms():
    cases = {'Rekaman disimpan lewat Zammad sesudah tiket ditutup.': 'Record disimpan melalui Zammad setelah ticket ditutup.',
             'Tindakan Korektif dan akar masalahnya': 'Corrective Action dan root cause-nya',
             'Tindakan korektif; peninjauan berkala; Formulir ini': 'Corrective action; review berkala; Form ini',
             'perekaman ditinjau meninjau melewati terlewat': 'perekaman ditinjau meninjau melewati terlewat',
             'REKAMAN': 'RECORD', 'sesudahnya': 'setelahnya'}
    for a, b in cases.items():
        assert map_text(a) == b, (a, map_text(a), b)


def walk_docx_spec(s):
    """Hasilkan (jalur, getter/setter) untuk string yang boleh dipetakan; heading, meta, nama peran, PIC, id flow dilewati."""
    out = []

    def add(obj, key, path):
        if isinstance(obj[key], str):
            out.append((path, obj, key))

    def rec(o, path, skip=()):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in skip:
                    continue
                if isinstance(v, str):
                    add(o, k, f'{path}.{k}')
                else:
                    rec(v, f'{path}.{k}')
        elif isinstance(o, list):
            for i, v in enumerate(o):
                if isinstance(v, str):
                    add(o, i, f'{path}[{i}]')
                else:
                    rec(v, f'{path}[{i}]')

    def flow(f, path):
        for n in f.get('nodes', {}):
            add(f['nodes'], n, f'{path}.nodes.{n}')
        for i, e in enumerate(f.get('edges', [])):
            if len(e) > 2:
                add(e, 2, f'{path}.edges[{i}][2]')
        if 'caption' in f:
            add(f, 'caption', f'{path}.caption')

    for k, v in s.items():
        if k == 'meta':
            continue
        if k == 'flow':
            flow(v, '.flow')
        elif k == 'roles':
            for i, r in enumerate(v):
                for j in range(1, len(r)):
                    add(r, j, f'.roles[{i}][{j}]')
        elif k == 'procedures':
            for i, p in enumerate(v):
                for j, x in enumerate(p.get('intro', [])):
                    add(p['intro'], j, f'.procedures[{i}].intro[{j}]')
                for j, st in enumerate(p['steps']):
                    for c in (0, 2):
                        add(st, c, f'.procedures[{i}].steps[{j}][{c}]')
        elif k == 'sla':
            for i, r in enumerate(v):
                for c in range(len(r)):
                    if c != 1:
                        add(r, c, f'.sla[{i}][{c}]')
        elif k == 'sections':
            for i, sec in enumerate(v):
                for j, b in enumerate(sec.get('blocks', [])):
                    p = f'.sections[{i}].blocks[{j}]'
                    if 'p' in b:
                        add(b, 'p', p + '.p')
                    elif 'table' in b:
                        rec(b['table'], p + '.table', skip=('widths_cm',))
                    elif 'flow' in b:
                        flow(b['flow'], p + '.flow')
        else:
            rec(v, '.' + k)
    return out


def dump(s, path):
    open(path, 'w', encoding='utf-8').write(json.dumps(s, ensure_ascii=False, indent=1) + '\n')


def xlsx_text_cells(k):
    """Sel teks xlsx yang boleh dipetakan: Kontrol Dokumen (nilai, bukan label/judul) dan baris di atas header sheet data."""
    import openpyxl
    S = json.load(open('reports/w10/xlsx_sheets.json'))[k]
    wb = openpyxl.load_workbook(base_file(k))
    cells = []
    for ws in wb:
        if ws.title == 'Kontrol Dokumen':
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str) and c.column > 1 and ws.cell(c.row, 1).value not in ('Judul', 'Nomor dokumen') and not c.value.startswith('='):
                        cells.append((f'{ws.title}!{c.coordinate}', c.value))
        else:
            hdr = next((d['header_row'] for d in S['data'] if d['sheet'] == ws.title), None)
            if hdr is None or ws.title.startswith('Daftar'):
                continue
            for row in ws.iter_rows(max_row=hdr - 1):
                for c in row:
                    if isinstance(c.value, str) and not c.value.startswith('='):
                        cells.append((f'{ws.title}!{c.coordinate}', c.value))
    return cells


def terms(keys):
    selftest_terms()
    os.makedirs('reports/w10/terms', exist_ok=True)
    summ = {}
    for k in keys:
        d = DOCS[k]
        lines_a, lines_b = [], []
        if d['mode'] == 'xlsx':
            pp = f'specs/{k}.w10.patch.json'
            P = json.load(open(pp, encoding='utf-8'))
            for ref, v in xlsx_text_cells(k):
                nv = map_text(v)
                if nv != v:
                    P.setdefault('set', {})[ref] = nv
                    lines_a.append(f'{ref}: {v}')
                    lines_b.append(f'{ref}: {nv}')
            dump(P, pp)
        else:
            sp = f'specs/{k}.json'
            s = json.load(open(sp, encoding='utf-8'))
            for path, obj, key in walk_docx_spec(s):
                v = obj[key]
                nv = map_text(v)
                if nv != v:
                    obj[key] = nv
                    lines_a.append(f'{path}: {v}')
                    lines_b.append(f'{path}: {nv}')
            dump(s, sp)
        diff = '\n'.join(difflib.unified_diff(lines_a, lines_b, f'{k} sebelum skrip', f'{k} sesudah skrip', lineterm='', n=0))
        open(f'reports/w10/terms/{k}.diff', 'w', encoding='utf-8').write(diff + '\n')
        summ[k] = len(lines_a)
    old = json.load(open('reports/w10/terms_summary.json')) if os.path.exists('reports/w10/terms_summary.json') else {}
    old.update(summ)
    json.dump(old, open('reports/w10/terms_summary.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(summ))


def termsdiff(keys):
    """Diff berpasangan efek skrip istilah, dihitung ulang dari spec/out bed1bb6 (skrip deterministik)."""
    for k in keys:
        d = DOCS[k]
        pairs = []
        if d['mode'] == 'xlsx':
            pairs = [(ref, v, map_text(v)) for ref, v in xlsx_text_cells(k) if map_text(v) != v]
        else:
            s = json.loads(run('git', 'show', f'{BASE}:specs/{k}.json')[1])
            pairs = [(path, obj[key], map_text(obj[key])) for path, obj, key in walk_docx_spec(s) if map_text(obj[key]) != obj[key]]
        txt = [f'# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), {k}: {len(pairs)} teks berubah. Basis bed1bb6.', '']
        for path, a, b in pairs:
            txt += [f'@@ {path}', '- ' + a.replace(chr(10), ' / '), '+ ' + b.replace(chr(10), ' / '), '']
        open(f'reports/w10/terms/{k}.diff', 'w', encoding='utf-8').write('\n'.join(txt))


def td():
    n = 0
    for k, d in DOCS.items():
        if d['mode'] == 'xlsx':
            continue
        sp = f'specs/{k}.json'
        s = json.load(open(sp, encoding='utf-8'))
        s['meta']['table_defaults'] = dict(TD, **({'steps_widths_cm': STEPS_W} if d['mode'] == 'sop' else {}))
        dump(s, sp)
        n += 1
    print('table_defaults diset di', n, 'spec')


def xlsxinit():
    import openpyxl
    res = {}
    for k, d in sorted(DOCS.items()):
        if d['mode'] != 'xlsx':
            continue
        wb = openpyxl.load_workbook(base_file(k))
        r = {'file': d['out_path'], 'data': [], 'kontrol': None, 'gambar': [], 'lain': []}
        for ws in wb:
            if getattr(ws, '_images', []):
                r['gambar'].append(ws.title)
                continue
            if ws.title == 'Kontrol Dokumen':
                r['kontrol'] = {'sheet': ws.title, 'rows': [1, ws.max_row]}
                continue
            hdr = None
            if not ws.title.startswith('Matriks'):
                for i in range(1, min(ws.max_row, 40) + 1):
                    cells = [c for c in ws[i] if c.value not in (None, '')]
                    if len(cells) >= 2 and all(c.font and c.font.b for c in cells) and not any(
                            isinstance(c.value, str) and c.value.startswith('=') for c in cells):
                        hdr = i
                        break
            if hdr and ws.title != 'Ringkasan dan Persetujuan':
                r['data'].append({'sheet': ws.title, 'header_row': hdr, 'max_row': ws.max_row, 'freeze_bed1bb6': ws.freeze_panes,
                                  'header': [str(c.value) for c in ws[hdr] if c.value not in (None, '')]})
            else:
                r['lain'].append({'sheet': ws.title, 'max_row': ws.max_row, 'orientation': ws.page_setup.orientation or 'portrait'})
        res[k] = r
        P = {'freeze': {}, 'wrap_cols': {}, 'page_setup': {}}
        for x in r['data']:
            P['freeze'][x['sheet']] = x['freeze_bed1bb6'] or f"A{x['header_row'] + 1}"
            P['wrap_cols'][x['sheet']] = {'rows': [x['header_row'], x['max_row']]}
            P['page_setup'][x['sheet']] = {'orientation': 'landscape', 'fitToWidth': 1, 'fitToHeight': 0,
                                           'print_title_rows': f"{x['header_row']}:{x['header_row']}"}
        if r['kontrol']:
            P['wrap_cols']['Kontrol Dokumen'] = {'rows': r['kontrol']['rows']}
            P['page_setup']['Kontrol Dokumen'] = {'orientation': 'portrait', 'fitToWidth': 1, 'fitToHeight': 0}
        for x in r['lain']:
            P['page_setup'][x['sheet']] = {'orientation': x['orientation'], 'fitToWidth': 1, 'fitToHeight': 0}
        pp = f'specs/{k}.w10.patch.json'
        if os.path.exists(pp):
            P['set'] = json.load(open(pp)).get('set', {})
        dump(P, pp)
    json.dump(res, open('reports/w10/xlsx_sheets.json', 'w'), ensure_ascii=False, indent=1)
    print('xlsx_sheets.json:', {k: len(v['data']) for k, v in res.items()})


def fmt_ops(k):
    """Op format W10 dari reports/w10/xlsx_sheets.json (milik worker; penyusun hanya memegang set dan col_widths)."""
    r = json.load(open('reports/w10/xlsx_sheets.json'))[k]
    P = {'freeze': {}, 'wrap_cols': {}, 'page_setup': {}, 'fit_rows': {}, 'col_widths': {}}
    for x in r['data']:
        P['freeze'][x['sheet']] = x['freeze_bed1bb6'] or f"A{x['header_row'] + 1}"
        P['wrap_cols'][x['sheet']] = {'rows': [x['header_row'], x['max_row']]}
        P['page_setup'][x['sheet']] = {'orientation': 'landscape', 'fitToWidth': 1, 'fitToHeight': 0,
                                       'print_title_rows': f"{x['header_row']}:{x['header_row']}"}
    if r['kontrol']:
        rows = [3, r['kontrol']['rows'][1]]  # baris 1-2 judul dibiarkan melebar ke kanan, tidak di-wrap
        P['wrap_cols']['Kontrol Dokumen'] = {'rows': rows, 'valign': 'top'}
        P['fit_rows']['Kontrol Dokumen'] = {'rows': rows}
        P['page_setup']['Kontrol Dokumen'] = {'orientation': 'portrait', 'fitToWidth': 1, 'fitToHeight': 0}
    for x in r['lain']:
        if x['sheet'].startswith('Matriks'):
            # matriks 5x5 seimbang: kolom Impact 1 sampai 5 sama lebar; legenda di kolom C ikut wrap
            P['col_widths'][x['sheet']] = {c: 24 for c in 'CDEFG'}
            P['fit_rows'][x['sheet']] = {'rows': [12, x['max_row']]}
            P['page_setup'][x['sheet']] = {'orientation': 'landscape', 'fitToWidth': 1, 'fitToHeight': 0}
        else:
            P['page_setup'][x['sheet']] = {'orientation': x['orientation'], 'fitToWidth': 1, 'fitToHeight': 0}
    return P


def effective_patch(k):
    """Gabungan op format worker + set/col_widths penyusun; ditulis untuk audit, dipakai build."""
    P = fmt_ops(k)
    U = json.load(open(f'specs/{k}.w10.patch.json', encoding='utf-8'))
    P['set'] = U.get('set', {})
    for sh, w in U.get('col_widths', {}).items():
        P['col_widths'].setdefault(sh, {}).update(w)
    P = {a: b for a, b in P.items() if b}
    os.makedirs('reports/w10/xlsx_effective', exist_ok=True)
    pth = f'reports/w10/xlsx_effective/{k}.json'
    dump(P, pth)
    return pth


def text_of(p):
    return run('python3', '-I', '-c', TXX if p.endswith('.xlsx') else TXT, p)[1]


def to_pdf(src, outdir):
    """soffice dengan profil terpisah per proses (aman paralel)."""
    os.makedirs(outdir, exist_ok=True)
    prof = tempfile.mkdtemp(prefix='lo-', dir='/tmp/claude-0')
    run('soffice', f'-env:UserInstallation=file://{prof}', '--headless', '--convert-to', 'pdf', '--outdir', outdir, src)
    shutil.rmtree(prof, ignore_errors=True)
    return os.path.join(outdir, os.path.splitext(os.path.basename(src))[0] + '.pdf')


def pdf_pages(pdf):
    m = re.search(r'Pages:\s+(\d+)', run('pdfinfo', pdf)[1])
    return int(m.group(1)) if m else None


def page_text(pdf, i):
    return run('pdftotext', '-layout', '-f', str(i), '-l', str(i), pdf, '-')[1]


def blank_pages(pdf, n):
    bad = []
    for i in range(1, n + 1):
        words = [w for w in page_text(pdf, i).split() if not re.fullmatch(r'Page/?|Halaman|-|\d+', w)]
        if len(words) < 8:
            bad.append(i)
    return bad


def isi_heading(spec):
    hs = [s['h'] for s in spec.get('sections', [])]
    idx = [i for i, h in enumerate(hs) if h.lower() in INSTR_H]
    if not idx:
        return None
    for h in hs[idx[-1] + 1:]:
        if not h.lower().startswith('alur') and h.lower() != 'peran':
            return h
    return None


def isi_page(pdf, n, head):
    for i in range(1, n + 1):
        if any(line.strip().endswith(head.upper()) for line in page_text(pdf, i).splitlines()):
            return i
    return None


def skeleton(o):
    if isinstance(o, dict):
        return {k: skeleton(v) for k, v in o.items() if k != 'table_defaults'}
    if isinstance(o, list):
        return [skeleton(v) for v in o]
    return '' if isinstance(o, str) else o


def frozen(s):
    """Nilai yang tidak boleh berubah di W10: meta (selain table_defaults), heading, nama peran, PIC, id flow."""
    m = {k: v for k, v in s.get('meta', {}).items() if k != 'table_defaults'}
    f = {'meta': m}
    f['h'] = [sec['h'] for sec in s.get('sections', [])] + [b['h2'] for sec in s.get('sections', []) for b in sec.get('blocks', []) if 'h2' in b]
    f['proc'] = [p['title'] for p in s.get('procedures', [])]
    f['roles'] = [r[0] for r in s.get('roles', [])]
    f['pic'] = [st[1] for p in s.get('procedures', []) for st in p['steps']] + [r[1] for r in s.get('sla', [])]
    fl = [s['flow']] if 'flow' in s else [b['flow'] for sec in s.get('sections', []) for b in sec.get('blocks', []) if 'flow' in b]
    f['flow_ids'] = [(sorted(x.get('nodes', {})), x.get('lanes'), [e[:2] for e in x.get('edges', [])], x.get('shapes')) for x in fl]
    return f


def notes_w10(k):
    p = f'notes/{k}.md'
    if not os.path.exists(p):
        return ''
    md = open(p, encoding='utf-8').read()
    i = md.find('## W10')
    return md[i:] if i >= 0 else ''


def build(k):
    d = DOCS[k]
    out = d['out_path']
    g = {'key': k, 'mode': d['mode'], 'out': out, 'fails': []}
    base = base_file(k)
    os.makedirs(f'{W}/diff', exist_ok=True)
    os.makedirs(f'{W}/pdf', exist_ok=True)
    if d['mode'] == 'xlsx':
        eff = effective_patch(k)
        rc, o, e = run('python3', '-I', 'tools/xlsx_patch.py', base, eff, out)
        g['xlsx_patch'] = 'pass' if rc == 0 else (o + e)[-400:]
        if rc:
            g['fails'].append('xlsx_patch gagal')
    else:
        rc, o, e = run('python3', '-I', 'tools/render_sop.py', 'template/SOP_TEMPLATE.docx', f'specs/{k}.json', out)
        if rc:
            g['fails'].append('render gagal: ' + (o + e)[-300:])
            return finish(k, g)
        old = json.loads(run('git', 'show', f'{BASE}:specs/{k}.json')[1])
        new = json.load(open(f'specs/{k}.json', encoding='utf-8'))
        if skeleton(old) != skeleton(new):
            g['fails'].append('struktur spec berubah (jumlah butir, baris, atau medan)')
        fo, fn = frozen(old), frozen(new)
        for part in fo:
            if fo[part] != fn[part]:
                g['fails'].append(f'nilai beku berubah: {part}')
        if new['meta'].get('table_defaults', {}).get('align_left') is not True:
            g['fails'].append('meta.table_defaults belum diset')
        rc, o, e = run('python3', '-I', 'tools/lint_doc.py', out, 'generic' if d['mode'] == 'generic' else 'sop')
        g['lint'] = 'pass' if rc == 0 else json.loads(o).get('fails') if o.startswith('{') else (o + e)[-300:]
        if rc:
            g['fails'].append('lint gagal')
        rc, o, e = run('python3', VALIDATOR, out)
        g['ooxml'] = 'PASSED' if rc == 0 else (o + e)[-300:]
        if rc:
            g['fails'].append('OOXML gagal')
    sc = json.loads(run('python3', '-I', 'tools/w10_langscan.py', 'scan', out)[1])[out]
    sb = json.loads(open('reports/w10/baseline.json').read())[out]
    g['scan'] = {x: sc[x] for x in sc if x != 'sheets'}
    g['scan_bed1bb6'] = {x: sb[x] for x in sb if x != 'sheets'}
    if sc['calque']:
        g['fails'].append(f"calque {len(sc['calque'])}")
    if sc['lewat']:
        g['fails'].append(f"lewat {sc['lewat']}")
    if sc['justified_cells']:
        g['fails'].append(f"justified_cells {sc['justified_cells']}")
    if sc.get('tables_ge3_no_header'):
        g['fails'].append(f"tables_ge3_no_header {sc['tables_ge3_no_header']}")
    if sc['instr_items'] and sc['instr_role_start'] > 0.25 * sc['instr_items']:
        g['fails'].append(f"instr_role_start {sc['instr_role_start']}/{sc['instr_items']} > 25%")
    df = json.loads(run('python3', '-I', 'tools/w10_langscan.py', 'diff', base, out)[1])
    g['subst_diff'] = df
    for bad in ('butir', 'headings', 'persons', 'snx'):
        if bad in df:
            g['fails'].append(f'substansi: {bad} berubah')
    nw = notes_w10(k)
    for kk in ('numbers', 'usul_butir'):
        for tok in (df.get(kk, {}).get('hilang', []) + df.get(kk, {}).get('baru', [])):
            if tok not in nw:
                g['fails'].append(f'selisih {kk} "{tok}" tidak tercatat di notes/{k}.md bagian ## W10')
    if not nw:
        g['fails'].append(f'notes/{k}.md belum punya bagian ## W10')
    if d['mode'] == 'xlsx':
        S = json.load(open('reports/w10/xlsx_sheets.json'))[k]
        sh = {x['sheet']: x for x in sc['sheets']}
        for x in S['data']:
            s = sh[x['sheet']]
            if not (s['freeze'] and s['fit_w'] and s['fitToWidth'] == 1 and s['orientation'] == 'landscape' and s['print_title_rows']):
                g['fails'].append(f"sheet {x['sheet']} belum freeze/fit/landscape/print titles")
        import openpyxl
        ws = openpyxl.load_workbook(out)['Kontrol Dokumen']
        nowrap = [c.coordinate for r in ws.iter_rows(min_row=3) for c in r if isinstance(c.value, str) and len(c.value) > 20 and not c.alignment.wrap_text]
        if nowrap:
            g['fails'].append(f'Kontrol Dokumen tanpa wrap: {nowrap[:5]}')
    # Diff teks untuk pemeriksa buta, PDF untuk rubrik (d), halaman form.
    a, b = text_of(base).splitlines(), text_of(out).splitlines()
    open(f'{W}/diff/{k}.diff', 'w', encoding='utf-8').write('\n'.join(difflib.unified_diff(a, b, f'{k} bed1bb6', f'{k} W10', lineterm='', n=1)) + '\n')
    pdf = to_pdf(out, f'{W}/pdf/new')
    n = pdf_pages(pdf)
    g['pdf'] = pdf
    g['pages'] = n
    if d['mode'] != 'xlsx' and n:
        bl = blank_pages(pdf, n)
        g['blank'] = bl
        if bl:
            g['fails'].append(f'halaman kosong {bl}')
        spec = json.load(open(f'specs/{k}.json', encoding='utf-8'))
        head = isi_heading(spec)
        if head:
            bpdf = to_pdf(base, f'{W}/pdf/base')
            bn = pdf_pages(bpdf)
            g['form'] = {'isi_heading': head, 'pages_bed1bb6': bn, 'pages_w10': n,
                         'isi_page_bed1bb6': isi_page(bpdf, bn, head), 'isi_page_w10': isi_page(pdf, n, head)}
            f = g['form']
            if f['pages_w10'] > f['pages_bed1bb6'] or (f['isi_page_w10'] or 0) > (f['isi_page_bed1bb6'] or 0):
                g['fails'].append(f"halaman form naik: {f}")
    return finish(k, g)


def finish(k, g):
    g['pass'] = not g['fails']
    os.makedirs('reports/w10/gates', exist_ok=True)
    json.dump(g, open(f'reports/w10/gates/{k}.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({'key': k, 'pass': g['pass'], 'fails': g['fails'], 'pages': g.get('pages'), 'form': g.get('form')}, ensure_ascii=False))
    return g


def revert(k):
    d = DOCS[k]
    files = [d['out_path']] + ([f'specs/{k}.json'] if d['mode'] != 'xlsx' else [])
    run('git', 'checkout', BASE, '--', *files)
    if d['mode'] == 'xlsx' and os.path.exists(f'specs/{k}.w10.patch.json'):
        os.remove(f'specs/{k}.w10.patch.json')
    print(k, 'dikembalikan ke', BASE)


def status():
    for k in sorted(DOCS):
        p = f'reports/w10/gates/{k}.json'
        q = f'qa/{k}.w10.json'
        g = json.load(open(p)) if os.path.exists(p) else {}
        v = json.load(open(q)).get('verdict') if os.path.exists(q) else '-'
        print(f"{k:12} {DOCS[k]['mode']:8} gate={g.get('pass', '-')!s:5} qa={v:5} fails={len(g.get('fails', []))}")


if __name__ == '__main__':
    cmd, args = sys.argv[1], sys.argv[2:]
    keys = args or sorted(DOCS)
    if cmd == 'terms':
        terms(keys)
    elif cmd == 'termsdiff':
        termsdiff(keys)
    elif cmd == 'td':
        td()
    elif cmd == 'xlsxinit':
        xlsxinit()
    elif cmd == 'build':
        for k in args:
            build(k)
    elif cmd == 'revert':
        for k in args:
            revert(k)
    elif cmd == 'status':
        status()
    elif cmd == 'selftest':
        selftest_terms()
        print('OK selftest w10 terms')
