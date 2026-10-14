#!/usr/bin/env python3
"""Perbaiki form xlsx tim (seri SNX) tanpa merusak fitur, lalu buktikan fitur tetap utuh.

Pakai: python3 -I xlsx_patch.py <in.xlsx> <patch.json> <out.xlsx>
patch.json: {"clear_rows": {"Sheet": [5, 6]}, "set": {"Sheet!B4": "nilai"}}
clear_rows mengosongkan sel non-rumus dan warna isi di baris itu (struktur, rumus,
validasi tetap); baris TIDAK dihapus agar rujukan rumus tidak bergeser. Keluar 1 bila fitur berkurang
(sheet, gambar, data validation, conditional formatting) atau masih ada teks CONTOH.
"""
import json, sys, zipfile
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
    for sheet, rows in patch.get('clear_rows', {}).items():
        ws = wb[sheet]
        cleared = set(rows)
        for r in rows:
            # Warna baris dikosongkan ikut baris input pertama di bawahnya yang tidak dikosongkan,
            # agar sel isian tetap seragam (tech_fix W1: dulu warna dibuang, baris input jadi putih).
            nxt = next((k for k in range(r + 1, r + 40) if k not in cleared), None)
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
