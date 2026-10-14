"""Cari halaman tanpa teks badan (hanya header/footer) di docx out/. Usage: python3 -I blankscan.py <docx>..."""
import subprocess, sys, os, re
out = '/tmp/claude-0/blank'
for f in sys.argv[1:]:
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out, f], capture_output=True)
    pdf = os.path.join(out, os.path.basename(f)[:-5] + '.pdf')
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    bad = []
    for i in range(1, n + 1):
        t = subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout
        words = [w for w in t.split() if not re.fullmatch(r'Page/?|Halaman|-|\d+', w)]
        if len(words) < 8:
            bad.append((i, ' '.join(words)[:60]))
    print(f'{"BLANK" if bad else "ok"}\t{n}\t{os.path.basename(f)}\t{bad}')
