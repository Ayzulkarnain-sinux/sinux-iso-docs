#!/usr/bin/env python3
"""ISO-W10 gerbang 6 (LEAD G-4): hitungan HR Lead, Kristanto, Divisi Legal, Daffa (dan pembanding W9) harus sama
antara out/ bed1bb6 dan out/ sekarang, per dokumen. Teks: paragraf, tabel, header, footer docx; semua sel xlsx.
Pakai (root repo): python3 -I reports/orch/w10_grepgate.py > reports/w10/grepgate.txt ; keluar 1 bila ada selisih
pada istilah wajib atau kontrol positif gagal."""
import io, json, re, subprocess, sys
import docx, openpyxl
from docx.oxml.ns import qn

TERMS = {'HR Lead': r'HR Lead', 'Kristanto': r'Kristanto', 'Divisi Legal': r'Divisi Legal', 'Daffa': r'Daffa',
         'HR Manager': r'HR Manager', 'Kristianto': r'Kristianto', 'em-dash': '—'}
WAJIB = ('HR Lead', 'Kristanto', 'Divisi Legal', 'Daffa')
BASE = 'bed1bb6'


def text(name, blob):
    if name.endswith('.xlsx'):
        wb = openpyxl.load_workbook(io.BytesIO(blob))
        return '\n'.join(str(c.value) for ws in wb for r in ws.iter_rows() for c in r if c.value is not None)
    d = docx.Document(io.BytesIO(blob))
    parts = [''.join(t.text or '' for t in p.iter(qn('w:t'))) for p in d.element.body.iter(qn('w:p'))]
    for s in d.sections:
        for hf in (s.header, s.footer):
            parts += [''.join(t.text or '' for t in p.iter(qn('w:t'))) for p in hf._element.iter(qn('w:p'))]
    return '\n'.join(parts)


def count(t):
    return {k: len(re.findall(p, t)) for k, p in TERMS.items()}


L = json.load(open('ledger.json'))
docs = sorted(d['out_path'] for d in L['docs'] if d['state'] == 'DONE')
# Kontrol positif: teks sintetis memuat setiap istilah tepat sekali.
ctrl = count(' '.join(['HR Lead', 'Kristanto', 'Divisi Legal', 'Daffa', 'HR Manager', 'Kristianto', '—']))
ok_ctrl = all(v == 1 for v in ctrl.values())
print(f'KONTROL POSITIF: {ctrl} -> {"OK" if ok_ctrl else "GAGAL"}')
tot_a = dict.fromkeys(TERMS, 0)
tot_b = dict.fromkeys(TERMS, 0)
beda = []
for p in docs:
    a = count(text(p, subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True).stdout))
    b = count(text(p, open(p, 'rb').read()))
    for k in TERMS:
        tot_a[k] += a[k]
        tot_b[k] += b[k]
        if a[k] != b[k]:
            beda.append((p, k, a[k], b[k]))
print(f'{len(docs)} dokumen out/ (Master List tidak ikut; dibangun ulang terpisah)')
print('| Istilah | bed1bb6 | W10 | Wajib sama |')
print('|---|---|---|---|')
for k in TERMS:
    print(f'| {k} | {tot_a[k]} | {tot_b[k]} | {"ya" if k in WAJIB else "pembanding"} |')
print('SELISIH PER DOKUMEN:' if beda else 'SELISIH PER DOKUMEN: nihil')
for p, k, x, y in beda:
    print(f'   {k}: {x} -> {y}  {p}')
fail = (not ok_ctrl) or any(k in WAJIB for _, k, _, _ in beda) or tot_b['em-dash']
sys.exit(1 if fail else 0)
