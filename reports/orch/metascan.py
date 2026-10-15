#!/usr/bin/env python3
"""LEAD G-1: ukur frasa meta proses penyusunan di seluruh out/ (target nol) + kontrol positif.
Pakai (root repo): python3 -I reports/orch/metascan.py  -> laporan teks; keluar 1 bila ada temuan."""
import glob, re, subprocess, sys

PAT = re.compile(r'(?i)\b(dokumen sumber|sumber tim|di sumber|draf ini|belum berdokumen)\b')
PENYUSUN = re.compile(r'(?i)\bpenyusun\b')
ROLE_OK = ('SNX-OPS-FRM-03', 'SNX-OPS-FRM-06', 'SNX-OPS-FRM-10')  # G-1: "penyusun" di sini nama peran formulir, sah


def text(path, blob=None):
    code = ("import docx,sys,io;d=docx.Document(io.BytesIO(sys.stdin.buffer.read()));print('\\n'.join(p.text for p in d.paragraphs));"
            "print('\\n'.join(c.text for t in d.tables for r in t.rows for c in r.cells))") if path.endswith('.docx') else \
           "import openpyxl,sys,io;wb=openpyxl.load_workbook(io.BytesIO(sys.stdin.buffer.read()));print('\\n'.join(str(c.value) for ws in wb.worksheets for r in ws.iter_rows() for c in r if c.value is not None))"
    data = blob if blob is not None else open(path, 'rb').read()
    return subprocess.run(['python3', '-I', '-c', code], input=data, capture_output=True).stdout.decode()


# Kontrol positif: LEG-SOP-02 versi sebelum perbaikan (commit pertama berkas itu) harus menembak.
p = glob.glob('out/04_Legal/SNX-LEG-SOP-02 *.docx')[0]
first = subprocess.run(['git', 'log', '--format=%h', '--diff-filter=A', '--', p], capture_output=True, text=True).stdout.split()[-1]
old = subprocess.run(['git', 'show', f'{first}:{p}'], capture_output=True).stdout
ctrl = PAT.findall(text(p, old))
print(f'KONTROL POSITIF LEG-SOP-02 @{first}: {len(ctrl)} temuan {sorted(set(m.lower() for m in ctrl))} -> {"OK" if ctrl else "GAGAL: pola tidak menembak"}')

hits = 0
for f in sorted(glob.glob('out/*/*.docx') + glob.glob('out/*/*.xlsx')):
    if '00_Index' in f:
        continue
    t = text(f)
    lines = [ln.strip() for ln in t.splitlines() if PAT.search(ln)]
    if not any(r in f for r in ROLE_OK):
        lines += [ln.strip() for ln in t.splitlines() if PENYUSUN.search(ln)]
    if lines:
        hits += len(lines)
        print(f'TEMUAN {f}:')
        for ln in sorted(set(lines)):
            print(f'   - {ln[:200]}')
print(f'TOTAL baris bertemuan: {hits} (target 0)')
sys.exit(1 if hits or not ctrl else 0)
