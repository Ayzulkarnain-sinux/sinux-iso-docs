#!/usr/bin/env python3
"""ISO-W9: render spec terkini satu KEY ke /tmp/claude-0/w9/render/, lalu diff teks terhadap versi out/ di commit dasar
(4a40352, sebelum W9) dan diff spec. Dipakai pemeriksa perubahan buta dan orkestrator (cek render out/ = render yang diperiksa).
Pakai (root repo): python3 -I reports/orch/w9diff.py KEY [--base REV]
  -> /tmp/claude-0/w9/diff/KEY.diff, KEY.spec.diff, render /tmp/claude-0/w9/render/KEY.{docx,xlsx}; cetak ringkasan + sha teks."""
import difflib, hashlib, json, os, subprocess, sys

KEY = sys.argv[1]
BASE = sys.argv[sys.argv.index('--base') + 1] if '--base' in sys.argv else '4a40352'
L = json.load(open('ledger.json'))
D = next(d for d in L['docs'] if d.get('key') == KEY)
OUT = D['out_path']
XLSX = OUT.endswith('.xlsx')
R = '/tmp/claude-0/w9/render'
os.makedirs(R, exist_ok=True)
os.makedirs('/tmp/claude-0/w9/diff', exist_ok=True)
TXT = ("import docx,sys;d=docx.Document(sys.argv[1]);print('\\n'.join(p.text for p in d.paragraphs));"
       "[print(' | '.join(c.text for c in r.cells)) for t in d.tables for r in t.rows]")
TXX = ("import openpyxl,sys;wb=openpyxl.load_workbook(sys.argv[1]);"
       "[print(ws.title, c.coordinate, c.value) for ws in wb.worksheets for r in ws.iter_rows() for c in r if c.value is not None]")


def text_of(path):
    return subprocess.run(['python3', '-I', '-c', TXX if XLSX else TXT, path], capture_output=True, text=True).stdout


def main():
    if XLSX:
        new = f'{R}/{KEY}.xlsx'
        r = subprocess.run(['python3', '-I', 'tools/xlsx_patch.py', f'/tmp/src/{KEY}.xlsx', f'specs/{KEY}.patch.json', new], capture_output=True, text=True)
        spec = f'specs/{KEY}.patch.json'
    else:
        new = f'{R}/{KEY}.docx'
        r = subprocess.run(['python3', '-I', 'tools/render_sop.py', 'template/SOP_TEMPLATE.docx', f'specs/{KEY}.json', new], capture_output=True, text=True)
        spec = f'specs/{KEY}.json'
    if r.returncode:
        print('RENDER GAGAL', r.stdout[-400:], r.stderr[-400:])
        sys.exit(2)
    old = f'{R}/{KEY}.base{os.path.splitext(OUT)[1]}'
    open(old, 'wb').write(subprocess.run(['git', 'show', f'{BASE}:{OUT}'], capture_output=True).stdout)
    a, b = text_of(old).splitlines(), text_of(new).splitlines()
    diff = '\n'.join(difflib.unified_diff(a, b, f'sebelum ({BASE})', 'sesudah (spec terkini)', lineterm='', n=1))
    open(f'/tmp/claude-0/w9/diff/{KEY}.diff', 'w').write(diff)
    sd = subprocess.run(['git', 'diff', BASE, '--', spec], capture_output=True, text=True).stdout
    open(f'/tmp/claude-0/w9/diff/{KEY}.spec.diff', 'w').write(sd)
    minus = sum(1 for x in diff.splitlines() if x.startswith('-') and not x.startswith('---'))
    plus = sum(1 for x in diff.splitlines() if x.startswith('+') and not x.startswith('+++'))
    print(f"{KEY}: {minus} baris lama, {plus} baris baru; diff /tmp/claude-0/w9/diff/{KEY}.diff; spec.diff {len(sd)} byte; "
          f"render {new}; sha_teks {hashlib.sha256('\n'.join(b).encode()).hexdigest()[:16]}")


if __name__ == '__main__':
    main()
