#!/usr/bin/env python3
"""Sidik format docx: sha256 atas document.xml + styles.xml + footer*.xml + header*.xml,
tanpa ukuran gambar (wp:extent, a:ext) agar beda versi graphviz tidak dianggap beda format.

Pakai: python3 -I format_hash.py <doc.docx>
"""
import hashlib, re, sys, zipfile

z = zipfile.ZipFile(sys.argv[1])
names = ['word/document.xml', 'word/styles.xml'] + sorted(
    n for n in z.namelist() if re.match(r'word/(header|footer)\d*\.xml$', n))
h = hashlib.sha256()
for n in names:
    x = z.read(n).decode('utf-8')
    h.update(re.sub(r'<(wp:extent|a:ext)\b[^>]*/>', '', x).encode('utf-8'))
print(h.hexdigest())
