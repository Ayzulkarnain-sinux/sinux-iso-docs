#!/usr/bin/env bash
# Uji integritas perkakas di container baru. Lulus = 4 baris OK.
cd "$(dirname "$0")/.." || exit 1
want=02b9ecd799755a1f270c412456c6aef72e353a3423d114c7c94d69554b4055e6
got=$(sha256sum template/SOP_TEMPLATE.docx | cut -d' ' -f1)
if [ "$got" = "$want" ]; then echo "OK template sha"; else echo "BEDA template sha: $got (template berubah, uji ulang render)"; fi
mkdir -p /tmp/selftest
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/UJI-RENDER.json /tmp/selftest/sop.docx && python3 -I tools/lint_doc.py /tmp/selftest/sop.docx sop >/dev/null && echo "OK kontrol positif sop"
python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/UJI-GENERIC.json /tmp/selftest/gen.docx && python3 -I tools/lint_doc.py /tmp/selftest/gen.docx generic >/dev/null && echo "OK kontrol positif generic"
if python3 -I tools/lint_doc.py template/SOP_TEMPLATE.docx sop >/dev/null; then echo "GAGAL kontrol negatif: lint meloloskan template mentah"; else echo "OK kontrol negatif"; fi
