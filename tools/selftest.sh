#!/usr/bin/env bash
# Uji integritas perkakas di container baru. Lulus = 6 baris OK.
cd "$(dirname "$0")/.." || exit 1
want=02b9ecd799755a1f270c412456c6aef72e353a3423d114c7c94d69554b4055e6
got=$(sha256sum template/SOP_TEMPLATE.docx | cut -d' ' -f1)
if [ "$got" = "$want" ]; then echo "OK template sha"; else echo "BEDA template sha: $got (template berubah, uji ulang render)"; fi
T=/tmp/selftest; mkdir -p $T
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/UJI-RENDER.json $T/sop.docx && python3 -I tools/lint_doc.py $T/sop.docx sop >/dev/null && echo "OK kontrol positif sop"
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/UJI-GENERIC.json $T/gen.docx && python3 -I tools/lint_doc.py $T/gen.docx generic >/dev/null && echo "OK kontrol positif generic"
if python3 -I tools/lint_doc.py template/SOP_TEMPLATE.docx sop >/dev/null; then echo "GAGAL kontrol negatif: lint meloloskan template mentah"; else echo "OK kontrol negatif"; fi
# Format acuan (sampel yang owner setujui, reference/): renderer tidak boleh mengubah tata letak.
fs=a595f34e6022ab2102c2d25003862493f990944f893ad9cfb55ada7e7888006f
fg=8c189a863677529c8f9916e38965b0e57a96701a8241e8259512f85ba88ebe88
if [ "$(python3 -I tools/format_hash.py $T/sop.docx)" = "$fs" ] && [ "$(python3 -I tools/format_hash.py $T/gen.docx)" = "$fg" ]; then echo "OK format terkunci"; else echo "BEDA format: renderer mengubah tata letak acuan, kembalikan perubahan atau minta LEAD"; fi
# Gerbang gaya harus menembak frasa slop, dan gerbang dummy harus menembak isi uji di nomor resmi.
python3 -I -c "
import json,sys
s=json.load(open('specs/UJI-RENDER.json')); s['purpose'][0]+=' Proses ini sangat penting untuk menjaga sinergi tim.'
json.dump(s,open(sys.argv[1],'w'))
s=json.load(open('specs/UJI-RENDER.json')); s['meta']['number']='SNX-ISMS-SOP-99'
json.dump(s,open(sys.argv[2],'w'))" $T/slop.json $T/dummy.json
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx $T/slop.json $T/slop.docx
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx $T/dummy.json $T/dummy.docx
if python3 -I tools/lint_doc.py $T/slop.docx sop | grep -q '"gaya' && python3 -I tools/lint_doc.py $T/dummy.docx sop | grep -q 'sisa isi uji'; then echo "OK kontrol gaya dan dummy"; else echo "GAGAL kontrol gaya dan dummy: gerbang tidak menembak"; fi
