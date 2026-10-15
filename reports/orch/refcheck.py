#!/usr/bin/env python3
"""Cek rujukan silang 'SNX-<KODE> butir/bagian/langkah N.M' di specs terhadap spec dokumen tujuan (mode sop).
Pakai (dari root repo): python3 -I reports/orch/refcheck.py [KEY...]  -> JSON {KEY: [rujukan rusak]}"""
import glob, json, re, sys

L = json.load(open('ledger.json'))
by_num = {d['number']: d for d in L['docs'] if d.get('number')}
REF = re.compile(r'(SNX-[A-Z]+-[A-Z]+-\d\d)\s*(?:\(|,)?\s*(?:butir|bagian|Bagian|langkah)\s+(\d+)(?:\.(\d+))?')


def broken(key):
    spec = f'specs/{key}.json'
    text = open(spec, encoding='utf-8').read()
    out = []
    for m in REF.finditer(text):
        num, a, b = m.group(1), int(m.group(2)), m.group(3)
        t = by_num.get(num)
        if t is None:
            out.append(f'{m.group(0)}: nomor tidak ada di set dokumen')
            continue
        if t['mode'] != 'sop' or not glob.glob(f"specs/{t['key']}.json"):
            continue  # mode generic/xlsx: penomoran bebas, tidak dicek mesin
        s = json.load(open(f"specs/{t['key']}.json", encoding='utf-8'))
        if not 1 <= a <= 11:
            out.append(f'{m.group(0)}: bagian {a} tidak ada (SOP punya bagian 1 sampai 11)')
        elif b and a == 4 and int(b) > len(s.get('policy', [])):
            out.append(f"{m.group(0)}: {num} hanya punya butir 4.1 sampai 4.{len(s['policy'])}")
        elif b and a == 6 and int(b) > len(s.get('procedures', [])):
            out.append(f"{m.group(0)}: {num} hanya punya 6.1 sampai 6.{len(s['procedures'])}")
    return sorted(set(out))


if __name__ == '__main__':
    keys = sys.argv[1:] or [d['key'] for d in L['docs'] if d['state'] == 'DONE' and glob.glob(f"specs/{d['key']}.json")]
    res = {k: r for k in keys if (r := broken(k))}
    print(json.dumps(res, ensure_ascii=False, indent=1))
