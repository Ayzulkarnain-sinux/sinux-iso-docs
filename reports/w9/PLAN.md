# PLAN ISO-W9 (WORKER-ISO-02, orkestrator): baca ini dulu sesudah konteks diringkas

Dasar: control/LEAD-GUIDE.md G-2 dan G-3; owner gaspol 15 Okt 02:31Z ("make sure semua aman dan cek juga gap ... improve sesuai goals ... jangan sampai mislead"). Keadaan = ledger.json (kunci "w9"). Batas: RUNBOOK §0, status Draft, Drive baca saja, nol staging, nol kanon KB.

## Urutan
1. SELESAI 02:34Z G-2 butir 3: git mv out/00_Index/Laporan_Run.md -> reports/Laporan_Run.md; README dan PLAYBOOK diperbarui. RUNBOOK §1/§11 masih menyebut out/00_Index (RUNBOOK milik LEAD, tidak disunting; dicatat di REVIEW-W9).
2. SELESAI B1 alat: reports/orch/refcheck2.py (keluaran penuh per rujukan, nomor heading dari urutan numPr, langkah tabel, kontrol positif FRM-10 @4a40352). Baseline: reports/w9/refcheck_baseline.{tsv,json}. Kerangka bernomor: refcheck2.py dump /tmp/claude-0/w9/struct.
3. Pemeriksa makna (Workflow, opus) atas 614 rujukan (silang semua + internal non-ADA): /tmp/claude-0/w9/sem/batch_1..8.json -> reports/w9/refsem.json.
4. tech_fix: render_sop.py opsi tabel generic "repeat_header"/"cant_split" (opt-in, format acuan tetap); xlsx_patch.py opsi "extend_validation", "copy_row_style", "fill_formula" (A10). Selftest 6 OK sesudahnya.
5. Penyusun per klaster (sonnet, maks 5 serentak), brief di /tmp/claude-0/prompts/w9/<KLASTER>.txt:
   HR-STRUKTUR (HR-ORG-01, HR-JA-01) | HR-SOP (10, 11, 12, 13) | HR-LAIN (HR-SOP-08, HR-FRM-01, HR-FRM-02, HR-RPT-01) |
   FAT-A (SOP-01, 05, 06) | FAT-B (SOP-04, FRM-01, RPT-02) | FAT-X (REG-01, FRM-02 xlsx) | LEG-A (SOP-01..03) | LEG-B (REG-01..04) |
   LEG-C (FRM-01..03, RPT-01..02) | COM (FRM-01, FRM-02, REG-01, SOP-02, SOP-01) | MKT (RPT-01, REG-01..03) | OPS-REF (OPS-FRM-10, ISMS-SOP-01 + notes A9). Workflow wf_bab51c1d-3f6 diluncurkan 03:08Z.
6. Orkestrator: render ke out/, lint, OOXML, blankscan, diff teks (sebelum = HEAD), grep bukti.
7. Pemeriksa perubahan buta (opus) per dokumen berubah -> qa/<KEY>.w9.json; B3 verifikator §8.2 untuk OPS-FRM-03 dan ISMS-REG-01 -> qa/<KEY>.verify.json.
8. FAIL -> satu sampai dua putaran perbaikan. PASS -> commit "ISO <KEY> polish".
9. Gerbang C: selftest, refcheck2 final, metascan, grep (HR Manager, Divisi Legal, label JA-03/JA-04), modifiedTime 54 sumber, Master List + USULAN-OPEN dibangun ulang (34 item LEAD ditutup per butir), reports/Laporan_Run.md bagian "Perubahan ISO-W9".
10. D: ledger current_wave W9-DONE, reports/REVIEW-W9.md, commit "ISO W9 penutupan", push, hapus watchdog, BERHENTI, ringkasan 10 baris.

## Temuan GAP (sesudah pemeriksa makna 03:00Z, reports/w9/refsem.json)
- RETRAKSI orkestrator 03:05Z: klaim di versi PLAN sebelumnya bahwa FAT-SOP-05 -> FAT-SOP-04 6.5, LEG-SOP-01 -> LEG-SOP-03 4.27, LEG-SOP-02 -> LEG-SOP-03 6.9, COM-SOP-01 -> COM-FRM-02 6.8, dan HR-SOP-10..13 -> ISMS-SOP-02 4.8/4.9 adalah rujukan rusak itu SALAH. Mesin salah menebak tujuan; nomor itu milik dokumen asal sendiri. Kanal: pemeriksa makna opus (R043, R054, R058, R080, R097, R119, R144, R163) + cek langsung orkestrator pada kerangka (HR-SOP-10 4.8 = Hak akses, HR-SOP-11 4.9 = Hak akses, HR-SOP-12 menulis "SOP ini", LEG-SOP-01 4.27 = retensi).
- 614 rujukan diperiksa: 424 OK, 167 salah tafsir mesin yang setelah dinilai ulang OK, 3 ke dokumen tim di luar set (tidak dapat dicek), 3 tanpa nomor tampak (ISMS-SOP-01 ke sheet Investigasi ISMS-FRM-02), 13 basi, 4 rusak. Perbaikan nyata: reports/w9/ref_fixes.json (22 butir; 11 di OPS-FRM-10 = G-2 butir 1).
- Klaster penomoran 9 SOP DIBATALKAN: tidak ada rujukan yang benar-benar menunjuk butir kebijakan tanpa nomor. Dicatat sebagai GAP konsistensi tampilan (9 SOP tanpa "4.n", 18 SOP dengan "4.n") untuk keputusan LEAD/owner.
- GAP keterbacaan: 160 rujukan "butir X" di tabel Dokumen Terkait atau tabel peran menunjuk dokumen asal sendiri tetapi terletak di baris dokumen lain (47 sudah bertanda "SOP ini"). Benar isinya, mudah salah baca. Tidak diubah di W9 (melebar); usulan konvensi "butir X SOP ini" di REVIEW-W9.
- Status basi: COM-SOP-01 (3 baris "isi belum dikonfirmasi/calon"), COM-FRM-01 ("calon rekaman" COM-FRM-02), COM-SOP-02 bagian 11 ("calon bentuknya" COM-FRM-01), HR-SOP-10/12 ("dalam pengerjaan"), FAT-FRM-01 (status T3 seragam).
- A8: Description checklist baris 58 bukan salinan persis baris 57 (ratio 0.696): baris 58 = isi baris 57 + validasi klaim. Open item tim ditulis presisi.
