#!/usr/bin/env python3
"""Perbaiki form xlsx tim (seri SNX) tanpa merusak fitur, lalu buktikan fitur tetap utuh.

Pakai: python3 -I xlsx_patch.py <in.xlsx> <patch.json> <out.xlsx>
patch.json: {"clear_rows": {"Sheet": [5, 6]}, "set": {"Sheet!B4": "nilai"}, "add_control_sheet": "<form SNX donor.xlsx>" (opsional)}
clear_rows mengosongkan sel non-rumus dan warna isi di baris itu (struktur, rumus,
validasi tetap); baris TIDAK dihapus agar rujukan rumus tidak bergeser. Keluar 1 bila fitur berkurang
(sheet, gambar, data validation, conditional formatting) atau masih ada teks CONTOH.
"""
import copy, json, sys, zipfile
import openpyxl


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
    for ref, val in patch.get('set', {}).items():
        sheet, cell = ref.rsplit('!', 1)
        wb[sheet][cell] = val
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
