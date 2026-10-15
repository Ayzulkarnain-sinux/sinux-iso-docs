# PLAN ISO-W9 (WORKER-ISO-02, orkestrator) — baca ini dulu sesudah konteks diringkas

Dasar: control/LEAD-GUIDE.md G-2 dan G-3; owner gaspol 15 Okt 02:31Z ("make sure semua aman dan cek juga gap ... improve sesuai goals ... jangan sampai mislead"). Keadaan = ledger.json (kunci "w9"). Batas: RUNBOOK §0, status Draft, Drive baca saja, nol staging, nol kanon KB.

## Urutan
1. SELESAI 02:34Z G-2 butir 3: git mv out/00_Index/Laporan_Run.md -> reports/Laporan_Run.md; README dan PLAYBOOK diperbarui. RUNBOOK §1/§11 masih menyebut out/00_Index (RUNBOOK milik LEAD, tidak disunting; dicatat di REVIEW-W9).
2. SELESAI B1 alat: reports/orch/refcheck2.py (keluaran penuh per rujukan, nomor heading dari urutan numPr, langkah tabel, kontrol positif FRM-10 @4a40352). Baseline: reports/w9/refcheck_baseline.{tsv,json}. Kerangka bernomor: refcheck2.py dump /tmp/claude-0/w9/struct.
3. Pemeriksa makna (Workflow, opus) atas 614 rujukan (silang semua + internal non-ADA): /tmp/claude-0/w9/sem/batch_1..8.json -> reports/w9/refsem.json.
4. tech_fix: render_sop.py opsi tabel generic "repeat_header"/"cant_split" (opt-in, format acuan tetap); xlsx_patch.py opsi "extend_validation", "copy_row_style", "fill_formula" (A10). Selftest 6 OK sesudahnya.
5. Penyusun per klaster (sonnet, maks 5 serentak), brief di /tmp/claude-0/prompts/w9/<KLASTER>.txt:
   HR-STRUKTUR (HR-ORG-01, HR-JA-01) | HR-SOP (10, 11, 12, 13) | HR-LAIN (HR-SOP-08, HR-FRM-01, HR-FRM-02, HR-RPT-01) |
   FAT-A (SOP-01, 05, 06) | FAT-B (SOP-04, FRM-01, RPT-02) | FAT-X (REG-01, FRM-02 xlsx) | LEG-A (SOP-01..03) | LEG-B (REG-01..04) |
   LEG-C (FRM-01..03, RPT-01..02) | COM (FRM-01, FRM-02, REG-01, SOP-02) | MKT (RPT-01, REG-01..03) | OPS (OPS-FRM-10 + perbaikan rujukan dokumen Ops/ISMS lain + notes A9).
6. Orkestrator: render ke out/, lint, OOXML, blankscan, diff teks (sebelum = HEAD), grep bukti.
7. Pemeriksa perubahan buta (opus) per dokumen berubah -> qa/<KEY>.w9.json; B3 verifikator §8.2 untuk OPS-FRM-03 dan ISMS-REG-01 -> qa/<KEY>.verify.json.
8. FAIL -> satu sampai dua putaran perbaikan. PASS -> commit "ISO <KEY> polish".
9. Gerbang C: selftest, refcheck2 final, metascan, grep (HR Manager, Divisi Legal, label JA-03/JA-04), modifiedTime 54 sumber, Master List + USULAN-OPEN dibangun ulang (34 item LEAD ditutup per butir), reports/Laporan_Run.md bagian "Perubahan ISO-W9".
10. D: ledger current_wave W9-DONE, reports/REVIEW-W9.md, commit "ISO W9 penutupan", push, hapus watchdog, BERHENTI, ringkasan 10 baris.

## Temuan GAP awal (diukur, menunggu pemeriksa makna)
- 9 SOP menampilkan butir kebijakan bagian 4 tanpa nomor "4.n" (ISMS-PLN-01, ISMS-SOP-01..04, OPS-PRC-01, OPS-SOP-02..04), padahal 18 SOP lain bernomor; 11 rujukan menunjuk paragraf tanpa nomor (ADA_TANPA_NOMOR), termasuk HR-SOP-10..13 ke SNX-ISMS-SOP-02 dengan nomor yang saling beda (4.8 vs 4.9).
- Rujukan nomor yang tidak ada: FAT-SOP-05 -> FAT-SOP-04 6.5; LEG-SOP-01 -> LEG-SOP-03 4.27; LEG-SOP-02 -> LEG-SOP-03 6.9; COM-SOP-01 -> COM-FRM-02 6.8 (dan teks "isi belum dikonfirmasi" basi); HR-SOP-12 -> HR-FRM-02 "dalam pengerjaan" (basi); OPS-FRM-10 -> OPS-SOP-04/05 (G-2 butir 1).
- A8: Description checklist baris 58 bukan salinan persis baris 57 (ratio 0.696): baris 58 = isi baris 57 + validasi klaim. Open item tim ditulis presisi.
