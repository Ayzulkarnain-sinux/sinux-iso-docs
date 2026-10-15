#!/usr/bin/env python3
"""ISO-W10 gerbang akhir (LEAD G-4 gerbang 6) atas SEMUA berkas out/ dokumen DONE, apa adanya di working tree:
docx: lint_doc, validator OOXML, blankscan; xlsx: fitur (sheet, gambar, validasi, conditional formatting, rumus)
tidak berkurang dibanding bed1bb6 dan nol teks CONTOH. Plus langscan scan per berkas.
Pakai (root repo): python3 -I reports/orch/w10_final.py > reports/w10/close/gate_final.txt
  -> reports/w10/close/gate_final.jsonl; keluar 1 bila ada berkas gagal."""
import hashlib, io, json, os, subprocess, sys
sys.path.insert(0, 'tools')
from xlsx_patch import features  # noqa: E402

VALIDATOR = '/mnt/skills/public/docx/scripts/office/validate.py'
L = json.load(open('ledger.json'))
docs = sorted((d for d in L['docs'] if d['state'] == 'DONE'), key=lambda d: d['key'])


def run(*a):
    p = subprocess.run(a, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


rows, bad = [], []
docx_paths = [d['out_path'] for d in docs if d['out_path'].endswith('.docx')]
blank = {}
for line in run('python3', '-I', 'reports/orch/blankscan.py', *docx_paths)[1].splitlines():
    st, n, name, detail = line.split('\t', 3)
    blank[name] = (st, int(n), detail)
scan = json.loads(run('python3', '-I', 'tools/w10_langscan.py', 'scan', *[d['out_path'] for d in docs])[1])
for d in docs:
    p = d['out_path']
    r = {'key': d['key'], 'out': p, 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()}
    if p.endswith('.docx'):
        mode = 'sop' if '-SOP-' in p or '-PLN-' in p or '-PRC-' in p or '-PRO-' in p else 'generic'
        g = json.load(open(f"reports/w10/gates/{d['key']}.json")) if os.path.exists(f"reports/w10/gates/{d['key']}.json") else {}
        mode = g.get('mode', mode)
        r['lint'] = 'pass' if run('python3', '-I', 'tools/lint_doc.py', p, mode)[0] == 0 else 'GAGAL'
        r['ooxml'] = 'PASSED' if run('python3', VALIDATOR, p)[0] == 0 else 'GAGAL'
        st, n, detail = blank.get(os.path.basename(p), ('TIDAK_DIUKUR', 0, ''))
        r['pages'], r['blank'] = n, (st if st != 'ok' else 0)
        ok = r['lint'] == 'pass' and r['ooxml'] == 'PASSED' and st == 'ok'
    else:
        base = '/tmp/claude-0/w10/pc/base.xlsx'
        open(base, 'wb').write(subprocess.run(['git', 'show', f'bed1bb6:{p}'], capture_output=True).stdout)
        fb, mb, _ = features(base)
        fa, ma, _ = features(p)
        less = [k for k, v in fb.items() if k not in fa or any(x < y for x, y in zip(fa[k], v))]
        import openpyxl
        wb = openpyxl.load_workbook(p)
        contoh = [f'{ws.title}!{c.coordinate}' for ws in wb.worksheets if ws.title != 'Kontrol Dokumen'
                  for row in ws.iter_rows() for c in row if isinstance(c.value, str) and 'CONTOH' in c.value]
        r['fitur_berkurang'], r['media'], r['contoh'] = less, f'{mb}->{ma}', contoh
        ok = not less and ma >= mb and not contoh
    s = scan.get(p, {})
    r['scan'] = {x: (len(s[x]) if isinstance(s.get(x), list) else s.get(x)) for x in
                 ('calque', 'lewat', 'justified_cells', 'tables_ge3_no_header', 'instr_items', 'instr_role_start', 'usulan', 'pointer')}
    r['ok'] = ok
    rows.append(r)
    if not ok:
        bad.append(d['key'])
with open('reports/w10/close/gate_final.jsonl', 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
nd = sum(1 for r in rows if r['out'].endswith('.docx'))
print(f'{len(rows)} berkas (docx {nd}, xlsx {len(rows) - nd})')
print(f"lint pass {sum(r.get('lint') == 'pass' for r in rows)}/{nd}; OOXML PASSED {sum(r.get('ooxml') == 'PASSED' for r in rows)}/{nd}; "
      f"halaman kosong {sum(1 for r in rows if r.get('blank') not in (0, None))}")
print(f"xlsx fitur berkurang {sum(1 for r in rows if r.get('fitur_berkurang'))}; CONTOH {sum(1 for r in rows if r.get('contoh'))}")
print('GAGAL: ' + (', '.join(bad) if bad else 'nihil'))
sys.exit(1 if bad else 0)
