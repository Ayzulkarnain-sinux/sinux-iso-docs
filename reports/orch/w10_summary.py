#!/usr/bin/env python3
"""ISO-W10: tabel per dokumen dari reports/w10/gates/KEY.json dan qa/KEY.w10.json (bahan REVIEW-W10).
Pakai (root repo): python3 -I reports/orch/w10_summary.py > reports/w10/close/ringkasan_gerbang.md"""
import glob, json, os


def ba(g, k):
    a, b = (g.get('scan_bed1bb6') or {}).get(k), (g.get('scan') or {}).get(k)
    a, b = (len(a) if isinstance(a, list) else a), (len(b) if isinstance(b, list) else b)
    return '-' if a is None and b is None else f'{a}→{b}'


rows, tot = [], {'PASS': 0, 'RESIDU': 0, 'LAIN': 0}
for f in sorted(glob.glob('reports/w10/gates/*.json')):
    g = json.load(open(f, encoding='utf-8'))
    k = g['key']
    try:
        q = json.load(open(f'qa/{k}.w10.json', encoding='utf-8'))
        qs = f"{q['verdict']} " + '/'.join(str(q['scores'].get(x)) for x in 'abcd')
    except FileNotFoundError:
        q, qs = None, '-'
    st = 'RESIDU' if g.get('residu') else ('PASS' if g.get('pass') and q and q['verdict'] == 'PASS' else 'LAIN')
    tot[st] += 1
    fm = g.get('form') or {}
    pg = f"{fm['pages_bed1bb6']}→{fm['pages_w10']}; ISI {fm['isi_page_bed1bb6']}→{fm['isi_page_w10']}" if fm else str(g.get('pages', '-'))
    sc = g.get('scan') or {}
    ir = f"{sc.get('instr_role_start', '-')}/{sc.get('instr_items', '-')}"
    rows.append(f"| {k} | {g['mode']} | {st} | {qs} | {ba(g, 'calque')} | {ba(g, 'lewat')} | {ba(g, 'justified_cells')} | "
                f"{ba(g, 'tables_ge3_no_header')} | {ir} | {ba(g, 'usulan')} | {ba(g, 'pointer')} | {pg} | {','.join(g.get('subst_diff') or {}) or '-'} |")
print(f"Dokumen: {sum(tot.values())}; PASS {tot['PASS']}, RESIDU {tot['RESIDU']}, LAIN {tot['LAIN']}. "
      'Kolom x→y = bed1bb6→W10 (residu: percobaan terakhir sebelum dikembalikan). instr = instr_role_start/instr_items.')
print('| KEY | mode | status | qa a/b/c/d | calque | lewat | justified | tabel≥3 tanpa header | instr | usulan | pointer | halaman | subst_diff |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
print('\n'.join(rows))
