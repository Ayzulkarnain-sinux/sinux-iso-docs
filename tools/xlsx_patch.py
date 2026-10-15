#!/usr/bin/env python3
"""Perbaiki form xlsx tim (seri SNX) tanpa merusak fitur, lalu buktikan fitur tetap utuh.

Pakai: python3 -I xlsx_patch.py <in.xlsx> <patch.json> <out.xlsx>
patch.json: {"clear_rows": {"Sheet": [5, 6]}, "set": {"Sheet!B4": "nilai"}, "add_control_sheet": "<form SNX donor.xlsx>" (opsional),
            "extend_validation": {"Sheet": {"K5:K6": "K5:K1000"}}, "copy_row_style": {"Sheet": {"from": 5, "rows": [7, 1000]}},
            "fill_formula": {"Sheet!J": {"rows": [5, 1000], "formula": "=IF(D{r}=\"\", \"\", TODAY() - D{r})"}} (ketiganya opsional, ISO-W9),
            "freeze": {"Sheet": "A5"}, "wrap_cols": {"Sheet": {"rows": [4, 200], "cols": ["B", "D"]}}, "col_widths": {"Sheet": {"B": 40}},
            "page_setup": {"Sheet": {"orientation": "landscape", "fitToWidth": 1, "fitToHeight": 0, "print_title_rows": "4:4"}},
            "fit_rows": {"Sheet": {"rows": [3, 38]}}; wrap_cols menerima "valign": "top" (opsional, ISO-W10)}
clear_rows mengosongkan sel non-rumus dan warna isi di baris itu (struktur, rumus,
validasi tetap); baris TIDAK dihapus agar rujukan rumus tidak bergeser. Keluar 1 bila fitur berkurang
(sheet, gambar, data validation, conditional formatting) atau masih ada teks CONTOH.
"""
import copy, json, sys, zipfile
import openpyxl
from openpyxl.utils import get_column_letter


def features(path):
    wb = openpyxl.load_workbook(path)
    f = {}
    for ws in wb.worksheets:
        nform = sum(1 for row in ws.iter_rows() for c in row
                    if isinstance(c.value, str) and c.value.startswith('='))
        f[ws.title] = (len(getattr(ws, '_images', [])), len(getattr(ws, '_charts', [])),
                       len(ws.data_validations.dataValidation), len(ws.conditional_formatting), nform)
    with zipfile.ZipFile(path) as z:
        media = len([n for n in z.namelist() if n.startswith(('xl/media/', 'xl/charts/'))])
        vba = any('vbaProject' in n for n in z.namelist())
    return f, media, vba


# Label medan "Kontrol Dokumen" seri SNX yang ikut disalin; nilai lain dikosongkan agar isi donor tidak terbawa.
CONTROL_LABELS = {'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A17', 'A29',
                  'A30', 'B30', 'C30', 'D30', 'E30', 'A34', 'A35', 'B35', 'C35', 'D35', 'A36', 'A37', 'A38'}


def add_control_sheet(wb, donor_path):
    """tech_fix W7b: sumber Google Sheet tanpa sheet Kontrol Dokumen. Salin tata letak sheet itu dari form
    SNX donor ke posisi pertama; sheet tim tidak disentuh. Hanya bila sumber belum punya sheet itu."""
    from openpyxl.utils import get_column_letter
    name = 'Kontrol Dokumen'
    if name in wb.sheetnames:
        print(json.dumps({'pass': False, 'why': 'sumber sudah punya sheet Kontrol Dokumen; pakai set'}))
        sys.exit(1)
    src = openpyxl.load_workbook(donor_path)[name]
    ws = wb.create_sheet(name, 0)
    for row in src.iter_rows():
        for c in row:
            n = ws.cell(row=c.row, column=c.column, value=c.value if c.coordinate in CONTROL_LABELS else None)
            if c.has_style:
                n.font, n.fill, n.border = copy.copy(c.font), copy.copy(c.fill), copy.copy(c.border)
                n.alignment, n.number_format, n.protection = copy.copy(c.alignment), c.number_format, copy.copy(c.protection)
    for m in src.merged_cells.ranges:
        ws.merge_cells(str(m))
    for k, d in src.column_dimensions.items():
        ws.column_dimensions[k].width = d.width
    for k, d in src.row_dimensions.items():
        ws.row_dimensions[k].height = d.height
    wb.active = 0
    return name


def main():
    src, patch_path, out = sys.argv[1:4]
    patch = json.load(open(patch_path, encoding='utf-8'))
    before, media0, vba = features(src)
    if vba:
        print(json.dumps({'pass': False, 'why': 'berkas bermakro, jangan disentuh'}))
        sys.exit(1)
    wb = openpyxl.load_workbook(src)
    from openpyxl.styles import PatternFill
    if patch.get('delete_rows'):
        print(json.dumps({'pass': False, 'why': 'delete_rows dilarang, pakai clear_rows'}))
        sys.exit(1)
    import copy
    added = add_control_sheet(wb, patch['add_control_sheet']) if patch.get('add_control_sheet') else None
    for sheet, rows in patch.get('clear_rows', {}).items():
        ws = wb[sheet]
        cleared = set(rows)
        for r in rows:
            # Warna baris dikosongkan ikut baris input pertama di bawahnya yang tidak dikosongkan,
            # agar sel isian tetap seragam (tech_fix W1: dulu warna dibuang, baris input jadi putih).
            nxt = next((k for k in range(r + 1, r + 40) if k not in cleared), None)
            # v2: hanya baris input kosong (tanpa nilai) yang jadi acuan warna; baris legenda/label tidak.
            if nxt and any(c.value is not None and not (isinstance(c.value, str) and c.value.startswith('=')) for c in ws[nxt]):
                nxt = None
            for c in ws[r]:
                if isinstance(c.value, str) and c.value.startswith('='):
                    continue
                c.value = None
                ref = ws.cell(row=nxt, column=c.column) if nxt else None
                c.fill = copy.copy(ref.fill) if ref is not None and ref.fill is not None and ref.fill.fill_type else PatternFill(fill_type=None)
    # tech_fix ISO-W9 (LEAD G-3 A10): perpanjang rentang validasi data, salin gaya sel satu baris ke rentang baris,
    # dan isi rumus berpola per baris ({r} = nomor baris). Validasi yang dirujuk harus ada persis; selain itu gagal.
    from openpyxl.worksheet.cell_range import MultiCellRange
    for sheet, m in patch.get('extend_validation', {}).items():
        ws = wb[sheet]
        for old_rng, new_rng in m.items():
            dv = next((v for v in ws.data_validations.dataValidation if str(v.sqref) == old_rng), None)
            if dv is None:
                print(json.dumps({'pass': False, 'why': f'validasi {sheet}!{old_rng} tidak ada'}))
                sys.exit(1)
            dv.sqref = MultiCellRange(new_rng)
    for sheet, spec in patch.get('copy_row_style', {}).items():
        ws = wb[sheet]
        a, b = spec['rows']
        for c in ws[spec['from']]:
            if c.has_style:
                for r in range(a, b + 1):
                    ws.cell(row=r, column=c.column)._style = copy.copy(c._style)
    for ref, spec in patch.get('fill_formula', {}).items():
        sheet, col = ref.rsplit('!', 1)
        a, b = spec['rows']
        for r in range(a, b + 1):
            wb[sheet][f'{col}{r}'] = spec['formula'].replace('{r}', str(r))
    for ref, val in patch.get('set', {}).items():
        sheet, cell = ref.rsplit('!', 1)
        wb[sheet][cell] = val
    # tech_fix ISO-W10 (LEAD G-4 butir 7): freeze, wrap_cols, col_widths, page_setup. Sheet tak dikenal atau
    # sheet bergambar (alur proses) ditolak, agar gambar alur tidak ikut diubah.
    def sheet_ok(name):
        if name not in wb.sheetnames or getattr(wb[name], '_images', []):
            print(json.dumps({'pass': False, 'why': f'sheet {name} tidak ada atau berisi gambar; tidak diubah'}))
            sys.exit(1)
        return wb[name]
    for sheet, cell in patch.get('freeze', {}).items():
        sheet_ok(sheet).freeze_panes = cell
    for sheet, spec in patch.get('wrap_cols', {}).items():
        ws = sheet_ok(sheet)
        a, b = spec['rows']
        cols = spec.get('cols') or [get_column_letter(i) for i in range(1, ws.max_column + 1)]
        for r in range(a, b + 1):
            for col in cols:
                c = ws[f'{col}{r}']
                al = copy.copy(c.alignment)
                al.wrap_text = True
                if spec.get('valign'):
                    al.vertical = spec['valign']
                c.alignment = al
    for sheet, widths in patch.get('col_widths', {}).items():
        ws = sheet_ok(sheet)
        for col, w in widths.items():
            ws.column_dimensions[col].width = w
    for sheet, ps in patch.get('page_setup', {}).items():
        ws = sheet_ok(sheet)
        ws.page_setup.orientation = ps.get('orientation', 'landscape')
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth = ps.get('fitToWidth', 1)
        ws.page_setup.fitToHeight = ps.get('fitToHeight', 0)
        if ps.get('paperSize'):
            ws.page_setup.paperSize = ps['paperSize']  # 8 = A3, untuk register yang sangat lebar
        if ps.get('print_title_rows'):
            ws.print_title_rows = ps['print_title_rows']
    # fit_rows: tinggi baris dari panjang teks sel ber-wrap dan lebar kolom (Excel tidak menyesuaikan sendiri saat dibuka).
    # Hanya menaikkan tinggi, tidak menurunkan. ponytail: lebar huruf rata-rata ditaksir, bukan diukur dari font.
    for sheet, spec in patch.get('fit_rows', {}).items():
        ws = sheet_ok(sheet)
        a, b = spec['rows']
        for r in range(a, b + 1):
            need = 0
            for c in ws[r]:
                if not isinstance(c.value, str) or c.value.startswith('=') or not c.alignment.wrap_text:
                    continue
                w = ws.column_dimensions[c.column_letter].width or 8.43
                cap = w * (0.7 if c.font.b else 0.85)  # huruf per baris, dikalibrasi dari render LibreOffice (OPS-FRM-08 Register)
                lines = 0
                for seg in c.value.split('\n'):
                    n, cur = 1, 0
                    for word in seg.split():
                        if cur and cur + 1 + len(word) > cap:
                            n, cur = n + 1, len(word)
                        else:
                            cur += (1 if cur else 0) + len(word)
                    lines += n
                need = max(need, lines * (c.font.sz or 11) * 1.35 + 3)
            cur = ws.row_dimensions[r].height or 15
            if need > cur:
                ws.row_dimensions[r].height = round(need, 1)
    wb.save(out)
    after, media1, _ = features(out)
    fails = []
    if added:
        before = {added: after[added], **before}
    if list(before) != list(after):
        fails.append(f'sheet berubah: {list(before)} -> {list(after)}')
    for k, v in before.items():
        a = after.get(k)
        if a and any(x < y for x, y in zip(a, v)):
            fails.append(f'fitur berkurang di {k}: {v} -> {a}')
    if media1 < media0:
        fails.append(f'media/chart berkurang {media0} -> {media1}')
    wb2 = openpyxl.load_workbook(out)
    for ws in wb2.worksheets:
        if ws.title in ('Kontrol Dokumen',):
            continue
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and 'CONTOH' in c.value:
                    fails.append(f'masih ada CONTOH di {ws.title}!{c.coordinate}')
                    break
    print(json.dumps({'pass': not fails, 'fails': fails, 'features_before': before,
                      'features_after': after}, ensure_ascii=False, default=str))
    sys.exit(0 if not fails else 1)


if __name__ == '__main__':
    main()
