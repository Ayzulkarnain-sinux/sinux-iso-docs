#!/usr/bin/env python3
"""Render satu SOP SINUX dari spec JSON ke docx, memakai SOP TEMPLATE.docx apa adanya.

Pakai: python3 -I render_sop.py <template.docx> <spec.json> <out.docx> [--flow-dir DIR]
Template tidak diubah; salinan diisi. Struktur 11 bagian, header, footer, gaya tetap.
"""
import copy, json, re, subprocess, sys, os
import docx
from docx.oxml.ns import qn
from docx.shared import Cm

HEADINGS = ["PURPOSE", "SCOPE", "DEFINITION & ABBREVIATIONS", "POLICY & GENERAL PRINCIPLES",
            "ROLES, RESPONSIBILITIES & AUTHORITIES", "STANDARD OPERATING PROCEDURE", "PROCESS FLOW",
            "SERVICE LEVEL AGREEMENT (SLA)", "EXCEPTION MANAGEMENT", "CONCLUSION",
            "RELATED DOCUMENTS & ATTACHMENTS"]
TOC_TITLES = ["Purpose", "Scope", "Definition & Abbreviations", "Policy & General Principles",
              "Roles, Responsibilities & Authorities", "Standard Operating Procedure", "Process Flow",
              "Service Level Agreement (SLA)", "Exception Management", "Conclusion",
              "Related Documents & Attachments"]


def replace_span(p_el, old, new):
    """Ganti teks yang mungkin terpecah lintas run, format run pertama dipertahankan."""
    ts = list(p_el.iter(qn('w:t')))
    full = ''.join(t.text or '' for t in ts)
    while old in full:
        start = full.index(old)
        end = start + len(old)
        pos = 0
        first = True
        for t in ts:
            txt = t.text or ''
            a, b = pos, pos + len(txt)
            pos = b
            if b <= start or a >= end:
                continue
            ls, le = max(start, a) - a, min(end, b) - a
            if first:
                t.text = txt[:ls] + new + txt[le:]
                first = False
            else:
                t.text = txt[:ls] + txt[le:]
            t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        full = ''.join(t.text or '' for t in ts)


def set_cell(cell, text, bold=None):
    """Isi sel: run pertama yang ada dipakai sebagai format, sisanya dibuang."""
    paras = cell.paragraphs
    p = paras[0]
    for extra in paras[1:]:
        extra._p.getparent().remove(extra._p)
    runs = p.runs
    if runs:
        runs[0].text = text
        for r in runs[1:]:
            r._r.getparent().remove(r._r)
        run = runs[0]
    else:
        run = p.add_run(text)
        prr = p._p.find(qn('w:pPr'))
        if prr is not None and prr.find(qn('w:rPr')) is not None:
            run._r.insert(0, copy.deepcopy(prr.find(qn('w:rPr'))))
    for br in run._r.findall(qn('w:br')):
        run._r.remove(br)
    if bold is not None:
        run.bold = bold
    return run


def fill_table(tbl, rows, header=None, body_bold=False):
    """rows = list baris (list teks). Baris template dikloning dari baris data pertama."""
    tr_tmpl = copy.deepcopy(tbl.rows[1]._tr if len(tbl.rows) > 1 else tbl.rows[0]._tr)
    if header is not None:
        for c, h in zip(tbl.rows[0].cells, header):
            set_cell(c, h, bold=True)
    # buang semua baris data lama
    for r in list(tbl.rows)[1:]:
        tbl._tbl.remove(r._tr)
    for row in rows:
        tr = copy.deepcopy(tr_tmpl)
        tbl._tbl.append(tr)
        new = tbl.rows[-1]
        for c, v in zip(new.cells, row):
            set_cell(c, str(v), bold=body_bold if body_bold else False)
    return tbl


def body_paragraph_template(doc_body, idx):
    return copy.deepcopy(doc_body[idx])


def make_para(tmpl_p, text, bold=False):
    p = copy.deepcopy(tmpl_p)
    for child in list(p):
        if child.tag != qn('w:pPr'):
            p.remove(child)
    ppr = p.find(qn('w:pPr'))
    r = p.makeelement(qn('w:r'), {})
    if ppr is not None and ppr.find(qn('w:rPr')) is not None:
        r.append(copy.deepcopy(ppr.find(qn('w:rPr'))))
    if bold:
        rpr = r.find(qn('w:rPr'))
        if rpr is None:
            rpr = r.makeelement(qn('w:rPr'), {})
            r.insert(0, rpr)
        rpr.append(rpr.makeelement(qn('w:b'), {}))
    t = r.makeelement(qn('w:t'), {})
    t.text = text
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    r.append(t)
    p.append(r)
    return p


def heading_index(body, title):
    for i, el in enumerate(body):
        if el.tag == qn('w:p'):
            txt = ''.join(t.text or '' for t in el.iter(qn('w:t'))).strip()
            if txt == title:
                return i
    raise KeyError(title)


def strip_page_break(p_el):
    for br in p_el.iter(qn('w:br')):
        if br.get(qn('w:type')) == 'page':
            br.getparent().remove(br)


def add_picture_capped(para, png, max_w=15.5, max_h=19.0):
    from PIL import Image
    w, h = Image.open(png).size
    if h / w * max_w > max_h:
        para.add_run().add_picture(png, height=Cm(max_h))
    else:
        para.add_run().add_picture(png, width=Cm(max_w))


def label_footer(d, classification):
    """PRO-01: dokumen RESTRICTED/SECRET wajib berlabel di header/footer tiap halaman."""
    if classification.upper().startswith(('RESTRICTED', 'SECRET')):
        for sec in d.sections:
            ps = sec.footer._element.findall(qn('w:p'))
            for p in ps:
                ts = list(p.iter(qn('w:t')))
                if ts and 'Page' in ''.join(t.text or '' for t in ts):
                    ts[0].text = f"{classification}   |   " + (ts[0].text or '')
                    ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                    break


def dedupe_bookmarks(d):
    """Hapus bookmark ber-id ganda hasil klon paragraf (Word menganggap id ganda tidak valid)."""
    for tag in (qn('w:bookmarkStart'), qn('w:bookmarkEnd')):
        seen = set()
        for el in list(d.element.body.iter(tag)):
            i = el.get(qn('w:id'))
            if i in seen:
                el.getparent().remove(el)
            else:
                seen.add(i)


def render_flow(spec, out_png):
    f = spec['flow']
    lines = ['digraph G {', f"rankdir={f.get('rankdir', 'LR')}; compound=true; newrank=true;",
             'graph [fontname="Arial", fontsize=11, nodesep=0.35, ranksep=0.4];',
             'node [fontname="Arial", fontsize=10, shape=box, style="rounded", width=2.0];',
             'edge [fontname="Arial", fontsize=9];']
    shapes = f.get('shapes', {})

    def node_line(n):
        label = f['nodes'][n].replace('"', "'").replace('\n', '\\n')
        shape = shapes.get(n, 'box')
        extra = ', style="filled", fillcolor="#EEF3FB"' if shape == 'diamond' else ''
        return f'"{n}" [label="{label}", shape={shape}{extra}];'

    placed = set()
    for li, (lane, nodes) in enumerate(f.get('lanes', {}).items()):
        lines.append(f'subgraph cluster_{li} {{ label="{lane}"; style="rounded"; color="#9AA5B1";')
        for n in nodes:
            lines.append(node_line(n))
            placed.add(n)
        lines.append('}')
    for n in f['nodes']:
        if n not in placed:
            lines.append(node_line(n))
    for e in f['edges']:
        lab = f'label="{e[2]}"' if len(e) > 2 and e[2] else ''
        # Garis lapor/alur yang belum terkonfirmasi digambar putus-putus (data_conflicts: "garis putus-putus ... menunggu konfirmasi").
        if (len(e) > 3 and e[3] == 'dashed') or (len(e) > 2 and str(e[2]).lower().startswith('menunggu konfirmasi')):
            lab += ', style=dashed' if lab else 'style=dashed'
        lines.append(f'"{e[0]}" -> "{e[1]}" [{lab}];')
    lines.append('}')
    with open(out_png + '.dot', 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))
    subprocess.run(['dot', '-Tpng', '-Gdpi=180', '-o', out_png, out_png + '.dot'], check=True)


def main():
    tpl, spec_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
    flow_dir = os.path.dirname(out)
    spec = json.load(open(spec_path, encoding='utf-8'))
    cfg = spec['meta']
    if cfg.get('mode', 'sop') == 'generic':
        return render_generic(tpl, spec, out)
    d = docx.Document(tpl)
    body = d.element.body
    T = list(d.tables)  # tangkap sebelum klon agar indeks tidak bergeser
    t_ident, t_rev, t_appr, t_def, t_roles, t_sla, t_exc = T[:7]
    def_tbl = copy.deepcopy(t_def._tbl)
    sla_tbl_el = copy.deepcopy(t_sla._tbl)

    # 1. Sampul
    replace_span(body[0], '[NAMA SOP]', cfg['title'])
    replace_span(body[0], '[NAMA]', cfg['department'].upper())
    replace_span(body[1], '[NOMOR SURAT]', cfg['number'])

    # 2. Identity
    ident = t_ident
    vals = {
        'Document Title': f"{cfg['department']} - SOP {cfg['title']}",
        'Document Number': cfg['number'],
        'Department': cfg['department'],
        'Effective Date': cfg.get('effective_date', ''),
        'Revision Number': f"Rev. {cfg.get('revision', '00')}",
        'Document Status': cfg.get('status', 'Draft'),
        'Classification': cfg.get('classification', 'Internal'),
        'Process Owner': cfg['process_owner'],
        'Review Period': cfg.get('review_period', 'YEARLY'),
    }
    for row in ident.rows:
        label = row.cells[0].text.strip()
        if label in vals:
            set_cell(row.cells[1], vals[label])

    # 3. Revision History baris 00
    rev = t_rev
    set_cell(rev.rows[1].cells[0], cfg.get('revision', '00'))
    set_cell(rev.rows[1].cells[1], cfg.get('effective_date', ''))
    set_cell(rev.rows[1].cells[2], cfg.get('revision_desc', 'Penerbitan awal'))

    # 4. Approval: nama/jabatan; tanda tangan TIDAK diisi
    appr = t_appr
    a = cfg['approval']
    set_cell(appr.rows[1].cells[2], a['prepared'])
    set_cell(appr.rows[2].cells[2], a['reviewed'])
    set_cell(appr.rows[3].cells[2], a['approved'])

    # 5. TOC statis: buang teks instruksi, sub-bagian 6.x sesuai isi
    sdt = [e for e in body if e.tag == qn('w:sdt')][0]
    tps = list(sdt.iter(qn('w:p')))
    for tp in tps:
        txt = ''.join(t.text or '' for t in tp.iter(qn('w:t')))
        if txt.startswith('1. Purpose') or txt.startswith('7. Process Flow'):
            ts = list(tp.iter(qn('w:t')))
            keep_r = ts[0].getparent()
            for r in list(tp.iter(qn('w:r'))):
                if r is not keep_r:
                    r.getparent().remove(r)
            for c in list(keep_r):
                if c.tag != qn('w:rPr'):
                    keep_r.remove(c)
            if txt.startswith('1. Purpose'):
                items = [f"{i+1}. {TOC_TITLES[i]}" for i in range(6)]
                items += [f"6.{j+1} {p['title']}" for j, p in enumerate(spec['procedures'])]
            else:
                items = [f"{i+1}. {TOC_TITLES[i]}" for i in range(6, 11)]
            for k, it in enumerate(items):
                if k:
                    keep_r.append(keep_r.makeelement(qn('w:br'), {}))
                t = keep_r.makeelement(qn('w:t'), {})
                t.text = it
                t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                keep_r.append(t)

    # format paragraf badan = paragraf kosong pertama sesudah PURPOSE
    i_purpose = heading_index(body, 'PURPOSE')
    ptmpl = copy.deepcopy(body[i_purpose + 1])

    def put_paras(title, paras):
        i = heading_index(body, title)
        # buang paragraf kosong placeholder sesudah heading
        j = i + 1
        while j < len(body) and body[j].tag == qn('w:p') and not ''.join(
                t.text or '' for t in body[j].iter(qn('w:t'))).strip() and not body[j].findall('.//' + qn('w:br')):
            body.remove(body[j])
        anchor = body[i]
        for txt in reversed(paras):
            bold = txt.startswith('**') and txt.endswith('**')
            anchor.addnext(make_para(ptmpl, txt.strip('*') if bold else txt, bold=bold))

    put_paras('PURPOSE', spec['purpose'])
    put_paras('SCOPE', spec['scope'])
    fill_table(t_def, spec['definitions'])
    put_paras('POLICY & GENERAL PRINCIPLES', spec['policy'])
    fill_table(t_roles, spec['roles'])

    # 6. Prosedur: Heading 2 per sub-proses + tabel langkah (klon tabel SLA, 3 kolom)
    h2 = body[heading_index(body, 'Process Detail')]
    strip_page_break(h2)
    anchor = h2
    first = True
    for proc in spec['procedures']:
        if first:
            replace_span(h2, 'Process Detail', proc['title'])
            hp = h2
            first = False
        else:
            hp = copy.deepcopy(h2)
            ts = list(hp.iter(qn('w:t')))
            ts[0].text = proc['title']
            for t in ts[1:]:
                t.text = ''
            anchor.addnext(hp)
        anchor = hp
        for note in proc.get('intro', []):
            np_ = make_para(ptmpl, note)
            anchor.addnext(np_)
            anchor = np_
        tbl_el = copy.deepcopy(sla_tbl_el)
        anchor.addnext(tbl_el)
        tbl = docx.table.Table(tbl_el, d._body)
        rows = [[f"{k+1}. {s[0]}", s[1], s[2]] for k, s in enumerate(proc['steps'])]
        fill_table(tbl, rows, header=['Aktivitas', 'PIC', 'Output / Rekaman'])
        sw = (cfg.get('table_defaults') or {}).get('steps_widths_cm')  # ISO-W10: kolom Aktivitas paling lebar
        if sw:
            adjust_cols(tbl_el, 3, [int(w * 567) for w in sw])
        anchor = tbl_el
        sp = make_para(ptmpl, '')
        anchor.addnext(sp)
        anchor = sp
    # buang paragraf kosong lama sesudah Process Detail bila tersisa
    # 7. Diagram alir
    png = os.path.join(flow_dir, cfg['doc_key'] + '_flow.png')
    render_flow(spec, png)
    i_flow = heading_index(body, 'PROCESS FLOW')
    fp = body[i_flow + 1]
    for c in list(fp):
        if c.tag != qn('w:pPr'):
            fp.remove(c)
    para = docx.text.paragraph.Paragraph(fp, d._body)
    add_picture_capped(para, png)
    if spec['flow'].get('caption'):
        fp.addnext(make_para(ptmpl, spec['flow']['caption']))

    # 8. SLA, 9. Exception, 10. Conclusion
    fill_table(t_sla, spec['sla'])
    exc = t_exc
    fill_table(exc, spec['exceptions'], header=spec.get('exceptions_header', ['Kondisi', 'Penanganan']))
    put_paras('CONCLUSION', spec['conclusion'])

    # 11. Related documents: daftar dokumen, rekaman, acuan klausul
    i11 = heading_index(body, 'RELATED DOCUMENTS & ATTACHMENTS')
    anchor = body[i11]
    blocks = []
    blocks.append(('p', '**Dokumen terkait**'))
    blocks.append(('t2', spec['related_documents'], ['Kode / Dokumen', 'Keterangan']))
    blocks.append(('p', '**Rekaman (records)**'))
    blocks.append(('t3', spec['records'], ['Rekaman', 'Lokasi simpan dan pemilik', 'Retensi']))
    if spec.get('iso_refs'):
        blocks.append(('p', '**Acuan standar**'))
        for k, v in spec['iso_refs'].items():
            blocks.append(('p', f"{k}: {v}"))
    for kind, *rest in blocks:
        if kind == 'p':
            txt = rest[0]
            bold = txt.startswith('**')
            el = make_para(ptmpl, txt.strip('*'), bold=bold)
        elif kind == 't2':
            el = copy.deepcopy(def_tbl)
            fill_table(docx.table.Table(el, d._body), rest[0], header=rest[1])
        else:
            el = copy.deepcopy(sla_tbl_el)
            fill_table(docx.table.Table(el, d._body), rest[0], header=rest[1])
        anchor.addnext(el)
        anchor = el
    apply_table_defaults(d, cfg.get('table_defaults'))
    dedupe_bookmarks(d)
    label_footer(d, cfg.get('classification', 'INTERNAL'))
    d.save(out)


def adjust_cols(tbl_el, n, widths=None, total=9072):
    """Ubah jumlah kolom tabel klon (format sel dipertahankan dari sel terakhir)."""
    grid = tbl_el.find(qn('w:tblGrid'))
    for c in grid.findall(qn('w:gridCol')):
        grid.remove(c)
    ws = widths or [total // n] * n
    for w in ws:
        grid.append(grid.makeelement(qn('w:gridCol'), {qn('w:w'): str(w)}))
    for tr in tbl_el.findall(qn('w:tr')):
        tcs = tr.findall(qn('w:tc'))
        while len(tcs) < n:
            nc = copy.deepcopy(tcs[-1])
            tcs[-1].addnext(nc)
            tcs.append(nc)
        while len(tcs) > n:
            tr.remove(tcs[-1])
            tcs.pop()
        for tc, w in zip(tcs, ws):
            tcpr = tc.find(qn('w:tcPr'))
            if tcpr is not None and tcpr.find(qn('w:tcW')) is not None:
                tcpr.find(qn('w:tcW')).set(qn('w:w'), str(w))
                tcpr.find(qn('w:tcW')).set(qn('w:type'), 'dxa')


def table_row_flags(tbl_el, tb):
    """tech_fix ISO-W9 (LEAD G-3 B4): opt-in per tabel. "repeat_header": baris judul diulang di tiap halaman;
    "cant_split": baris tidak terbelah antarhalaman. Tanpa flag, tabel tidak berubah (format acuan tetap)."""
    rows = tbl_el.findall(qn('w:tr'))
    for i, tr in enumerate(rows):
        want = (['tblHeader'] if tb.get('repeat_header') and i == 0 else []) + (['cantSplit'] if tb.get('cant_split') else [])
        if not want:
            continue
        trpr = tr.find(qn('w:trPr'))
        if trpr is None:
            trpr = tr.makeelement(qn('w:trPr'), {})
            tcs = tr.findall(qn('w:tc'))
            (tcs[0].addprevious(trpr) if tcs else tr.append(trpr))
        for tag in want:  # urutan skema CT_TrPr: cantSplit sebelum tblHeader, keduanya sebelum jc
            if trpr.find(qn('w:' + tag)) is None:
                trpr.insert(0 if tag == 'cantSplit' else (1 if trpr.find(qn('w:cantSplit')) is not None else 0), trpr.makeelement(qn('w:' + tag), {}))


def apply_table_defaults(d, td):
    """tech_fix ISO-W10 (LEAD G-4 butir 6): meta.table_defaults berlaku untuk semua tabel dokumen.
    align_left: sel rata kiri-kanan (jc both) menjadi rata kiri; repeat_header dan cant_split lewat table_row_flags.
    Spec tanpa table_defaults (termasuk UJI-RENDER dan UJI-GENERIC) tidak berubah."""
    if not td:
        return
    body = d.element.body
    if td.get('align_left'):
        for tc in body.iter(qn('w:tc')):
            for jc in tc.iter(qn('w:jc')):
                if jc.get(qn('w:val')) == 'both':
                    jc.set(qn('w:val'), 'left')
    for tbl in body.iter(qn('w:tbl')):
        table_row_flags(tbl, td)
    if td.get('keep_with_table'):
        # Label atau paragraf tepat sebelum tabel tidak terpisah dari tabelnya; baris judul tidak tertinggal sendiri
        # di dasar halaman; tabel pendek (<= keep_small_rows baris) tidak terbelah antarhalaman.
        small = td.get('keep_small_rows', 0)
        for tbl in list(body.iter(qn('w:tbl'))):
            prev = tbl.getprevious()
            if prev is not None and prev.tag == qn('w:p') and ''.join(t.text or '' for t in prev.iter(qn('w:t'))).strip():
                _keep_next(prev)
            rows = tbl.findall(qn('w:tr'))
            keep = rows[:-1] if len(rows) <= small else rows[:1]
            for tr in keep:
                for pe in tr.iter(qn('w:p')):
                    _keep_next(pe)


def _keep_next(p_el):
    ppr = p_el.find(qn('w:pPr'))
    if ppr is None:
        ppr = p_el.makeelement(qn('w:pPr'), {})
        p_el.insert(0, ppr)
    if ppr.find(qn('w:keepNext')) is None:
        kn = ppr.makeelement(qn('w:keepNext'), {})
        anchor = ppr.find(qn('w:pStyle'))  # urutan skema CT_PPr: pStyle lalu keepNext
        (anchor.addnext(kn) if anchor is not None else ppr.insert(0, kn))


def render_generic(tpl, spec, out):
    """Dokumen non-SOP (struktur, jobdesc, form, register): halaman depan template + badan bebas."""
    cfg = spec['meta']
    d = docx.Document(tpl)
    body = d.element.body
    T = list(d.tables)
    t_ident, t_rev, t_appr = T[:3]
    sla_tbl = copy.deepcopy(T[5]._tbl)
    i_p = heading_index(body, 'PURPOSE')
    ptmpl = copy.deepcopy(body[i_p + 1])
    h1t = copy.deepcopy(body[i_p])
    h2t = copy.deepcopy(body[heading_index(body, 'Process Detail')])
    strip_page_break(h2t)
    label = cfg.get('doc_type_label', cfg['doc_type_cover'].title())
    replace_span(body[0], 'STANDARD OPERATIONAL PROCEDURE', cfg['doc_type_cover'])
    replace_span(body[0], 'DEPARTMENT [NAMA]', 'DEPARTMENT ' + cfg['department'].upper())
    replace_span(body[0], '[NAMA SOP]', cfg['title'])
    replace_span(body[1], '[NOMOR SURAT]', cfg['number'])
    replace_span(body[6], 'Standard Operating Procedure', label)
    vals = {'Document Title': f"{cfg['department']} - {cfg['title']}", 'Document Number': cfg['number'],
            'Department': cfg['department'], 'Effective Date': cfg.get('effective_date', ''),
            'Revision Number': f"Rev. {cfg.get('revision', '00')}", 'Document Status': cfg.get('status', 'Draft'),
            'Classification': cfg.get('classification', 'Internal'), 'Process Owner': cfg['process_owner'],
            'Review Period': cfg.get('review_period', 'YEARLY')}
    for row in t_ident.rows:
        if row.cells[0].text.strip() in vals:
            set_cell(row.cells[1], vals[row.cells[0].text.strip()])
    set_cell(t_rev.rows[1].cells[0], cfg.get('revision', '00'))
    set_cell(t_rev.rows[1].cells[1], cfg.get('effective_date', ''))
    set_cell(t_rev.rows[1].cells[2], cfg.get('revision_desc', 'Penerbitan awal'))
    a = cfg['approval']
    set_cell(t_appr.rows[1].cells[2], a['prepared'])
    set_cell(t_appr.rows[2].cells[2], a['reviewed'])
    set_cell(t_appr.rows[3].cells[2], a['approved'])
    # TOC
    sdt = [e for e in body if e.tag == qn('w:sdt')][0]
    tps = list(sdt.iter(qn('w:p')))
    replace_span(tps[0], 'Standard Operating Procedure', label)
    titles = [sec['h'] for sec in spec['sections']]
    done = False
    for tp in tps:
        txt = ''.join(t.text or '' for t in tp.iter(qn('w:t')))
        if txt.startswith('1. Purpose') or txt.startswith('7. Process Flow'):
            if done:
                tp.getparent().remove(tp)
                continue
            ts = list(tp.iter(qn('w:t')))
            keep_r = ts[0].getparent()
            for r in list(tp.iter(qn('w:r'))):
                if r is not keep_r:
                    r.getparent().remove(r)
            for c in list(keep_r):
                if c.tag != qn('w:rPr'):
                    keep_r.remove(c)
            for k, it in enumerate(f"{i+1}. {t}" for i, t in enumerate(titles)):
                if k:
                    keep_r.append(keep_r.makeelement(qn('w:br'), {}))
                t = keep_r.makeelement(qn('w:t'), {})
                t.text = it
                t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
                keep_r.append(t)
            done = True
    # badan: buang semua dari heading hantu sampai sebelum sectPr
    i_sdt = list(body).index(sdt)
    start = None
    for i in range(i_sdt + 1, len(body)):
        el = body[i]
        if el.tag == qn('w:p') and el.find('.//' + qn('w:pStyle')) is not None and \
                el.find('.//' + qn('w:pStyle')).get(qn('w:val')) in ('Heading1', '1'):
            start = i
            break
    if start is None:
        start = i_p - 1
    for el in list(body)[start:]:
        if el.tag != qn('w:sectPr'):
            body.remove(el)
    sect = body.find(qn('w:sectPr'))
    flow_dir = os.path.dirname(out)

    def add(el):
        sect.addprevious(el)

    for si, sec in enumerate(spec['sections']):
        h = copy.deepcopy(h1t)
        ts = list(h.iter(qn('w:t')))
        ts[0].text = sec['h'].upper()
        for t in ts[1:]:
            t.text = ''
        add(h)
        for bi, b in enumerate(sec.get('blocks', [])):
            if 'p' in b:
                txt = b['p']
                bold = txt.startswith('**') and txt.endswith('**')
                add(make_para(ptmpl, txt.strip('*') if bold else txt, bold=bold))
            elif 'h2' in b:
                h2 = copy.deepcopy(h2t)
                ts = list(h2.iter(qn('w:t')))
                ts[0].text = b['h2']
                for t in ts[1:]:
                    t.text = ''
                add(h2)
            elif 'table' in b:
                tb = b['table']
                el = copy.deepcopy(sla_tbl)
                n = len(tb['header'])
                widths = [int(w * 567) for w in tb['widths_cm']] if tb.get('widths_cm') else None
                adjust_cols(el, n, widths)
                add(el)
                fill_table(docx.table.Table(el, d._body), tb['rows'], header=tb['header'])
                table_row_flags(el, tb)
                if tb.get('min_row_cm'):  # ISO-W10: baris isian form setinggi tulisan tangan (w:trHeight atLeast)
                    for tr in el.findall(qn('w:tr'))[1:]:
                        trpr = tr.find(qn('w:trPr'))
                        if trpr is None:
                            trpr = tr.makeelement(qn('w:trPr'), {})
                            tr.insert(0 if tr.find(qn('w:tblPrEx')) is None else 1, trpr)
                        trpr.append(trpr.makeelement(qn('w:trHeight'), {qn('w:val'): str(int(tb['min_row_cm'] * 567)), qn('w:hRule'): 'atLeast'}))
                add(make_para(ptmpl, ''))
            elif 'flow' in b:
                png = os.path.join(flow_dir, f"{cfg['doc_key']}_{si}_{bi}.png")
                render_flow({'flow': b['flow']}, png)
                pe = make_para(ptmpl, '')
                add(pe)
                add_picture_capped(docx.text.paragraph.Paragraph(pe, d._body), png)
                if b['flow'].get('caption'):
                    add(make_para(ptmpl, b['flow']['caption']))
    apply_table_defaults(d, cfg.get('table_defaults'))
    dedupe_bookmarks(d)
    label_footer(d, cfg.get('classification', 'INTERNAL'))
    d.save(out)


if __name__ == '__main__':
    main()
