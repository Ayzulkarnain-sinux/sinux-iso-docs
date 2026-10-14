#!/usr/bin/env python3
"""Pratinjau visual: docx/pdf -> PDF (soffice) -> PNG per halaman (pdftoppm) -> montase grid (PIL).
Pakai: python3 -I reports/orch/preview.py <doc.docx|pdf> <out_dir> [cols] [dpi]"""
import glob, os, subprocess, sys
from PIL import Image
src, od = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
dpi = sys.argv[4] if len(sys.argv) > 4 else '45'
os.makedirs(od, exist_ok=True)
base = os.path.splitext(os.path.basename(src))[0]
pdf = src
if not src.lower().endswith('.pdf'):
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', od, src], check=True, capture_output=True, timeout=240)
    pdf = os.path.join(od, base + '.pdf')
pre = os.path.join(od, 'pg')
for f in glob.glob(pre + '-*.png'): os.remove(f)
subprocess.run(['pdftoppm', '-r', dpi, '-png', pdf, pre], check=True)
pages = sorted(glob.glob(pre + '-*.png'))
ims = [Image.open(p).convert('RGB') for p in pages]
w, h = max(i.width for i in ims), max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
M = Image.new('RGB', (cols * (w + 8), rows * (h + 8)), 'white')
for k, im in enumerate(ims):
    M.paste(im, ((k % cols) * (w + 8), (k // cols) * (h + 8)))
out = os.path.join(od, 'montage.png'); M.save(out)
print(out, len(ims), 'halaman', pdf)
