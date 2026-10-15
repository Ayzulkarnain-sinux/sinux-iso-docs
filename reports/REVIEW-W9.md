# REVIEW ISO-W9: perbaikan pasca vonis dokumen ISO (15 Oktober 2026)

Receipt: repo sinux-iso-docs, basis 4a40352 (15 Okt 02.21 UTC), kerja W9 02.31 sampai 04.50 UTC. Arahan: control/LEAD-GUIDE.md G-2 (02.04 UTC) dan G-3 (02.21 UTC). Bukti mesin di reports/w9/, hasil pemeriksa per dokumen di qa/<KODE>.w9.json, riwayat per dokumen di commit "ISO <KODE> polish" (`git log 4a40352..HEAD`).

## RINGKASAN

Verdict: G-2 dan G-3 selesai seluruhnya, tanpa residu karena waktu. 41 dokumen diubah lewat specs/ lalu dirender ulang. Tiap dokumen yang berubah lolos pemeriksa perubahan buta yang terpisah dari penyusun: 41 dari 41 PASS dalam 67 pemeriksaan, dan 4 dokumen butuh satu putaran perbaikan. Semua gerbang C rc 0 dengan bukti di reports/w9/. Dua klaim ditarik: klaim refcheck W8 dan GAP di rencana W9 sendiri. Status semua dokumen tetap Draft. Nol tanda tangan, nol tanggal efektif, nol mutasi Drive, nol staging, nol kanon KB, nol kredensial.

## A. Data lintas dokumen (G-3 A1 sampai A10)

| Butir | Dikerjakan | Bukti | Sisa |
|---|---|---|---|
| A1 Ejaan Kristanto | SNX-HR-ORG-01 memakai Kristanto; K-07 ditulis sudah diputus. SNX-HR-JA-01 sudah benar, tidak diubah | qa/HR-ORG-01.w9.json; reports/w9/grep.txt (Kristianto 1, hanya kalimat K-07 yang menjelaskan ejaan lama) | nihil |
| A2 HR Lead | HR Lead menggantikan HR Manager di 10 dokumen HR; K-06 diperbarui. SPV tidak ditambahkan karena tidak ada dokumen dengan kolom tingkat jabatan | qa/HR-*.w9.json; grep.txt (HR Manager 1, hanya K-06; SPV 0) | nihil |
| A3 Garis JA-03 dan JA-04 | Garis JA-01 ke JA-03 tegas tanpa label, garis baru JA-01 ke JA-04, K-01 ditutup; 27 dokumen yang memakai garis lapor diselaraskan | qa/*.w9.json (27 dokumen menyebut A3); edges bagan di specs/HR-ORG-01.json: ja01 ke ja03 dan ja01 ke ja04 tanpa label | ukuran tingkatan jabatan (jumlah garis lapor) jadi bermakna ganda untuk JA-03, JA-04, dan bawahannya (OPEN DECISION 1) |
| A4 Garis lain tetap | Garis JA-05, JA-08, JA-10, JA-11, JA-14 tidak diubah | grep.txt (label K-02, K-03, K-04 utuh); qa/*.w9.json | nihil |
| A5 Legal bernama | JA-08 Ester Febe Utomo, JA-09 Alif Altamziz; label USULAN pemetaan dihapus; "Departemen Legal"; Daffa 0 | qa/LEG-*.w9.json; grep.txt (USULAN pemetaan 0, Divisi Legal 0 di dokumen, Daffa 0) | "Divisi Legal" 3 kali di kolom sumber Master List (nama berkas Drive tim, dikutip apa adanya); 53 tulisan "departemen Legal" berhuruf d kecil di 10 docx (kosmetik) |
| A6 Finance Lead dan Staff | Definisi kedua peran; Reviewed By dokumen FAT = Amirull Yusuf Zulkarnain / Direktur; K-13 diperbarui; 10 dokumen | qa/FAT-*.w9.json, qa/HR-ORG-01.w9.json; refsem2.json (rujukan K-13 dan bagian definisi OK) | pengisian jabatan Finance Lead (owner) |
| A7 PO Commercial | Process Owner SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01 = VP Commercial | qa/COM-*.w9.json | nihil |
| A8 Restrukturisasi MKT | REG-01 satu-satunya register materi dan klaim; REG-02 pelaksanaan campaign dan aktivitas; REG-03 lead; RPT-01 membaca REG-02 dan REG-03 | qa/MKT-*.w9.json | Description checklist baris 58 bukan salinan persis baris 57 (baris 57 ditambah validasi klaim); perlu dibetulkan tim Brand & Marketing |
| A9 Gambar xlsx | Gambar tidak diubah; open item ditutup | qa/OPS-FRM-10.w9.json; gate_final.jsonl (fitur gambar tidak berkurang) | nihil |
| A10 FAT-REG-01 | Validasi K dan L sampai baris 1000; rumus Days overdue di AR baris 5 sampai 1000 = TODAY() dikurangi Due date (pola sheet AP); AP baris 7 dikosongkan | qa/FAT-REG-01.w9.json; gate_final.jsonl (rumus AR 0 menjadi 996, validasi 2 tetap, AP 8 rumus tetap) | HUMAN-VERDICT: teks panjang di sel tanpa wrap; perlu dilihat saat dicetak |

## B. Mutu (G-3 B1 sampai B4)

| Butir | Dikerjakan | Bukti | Sisa |
|---|---|---|---|
| B1 G-2 butir 3 | Laporan_Run dipindah ke reports/ (git mv); rujukan di reports/orch diperbarui | commit 3f6ef70 | RUNBOOK §1 dan §11 masih menyebut out/00_Index/Laporan_Run.md; RUNBOOK milik LEAD, tidak disunting |
| B1 G-2 butir 1 | SNX-OPS-FRM-10: enam rujukan basi ke SOP-04 dan SOP-05 dibetulkan (11 rujukan di form itu disesuaikan); commit "ISO OPS-FRM-10 polish" | commit 6784c68; reports/w9/ref_fixes.json; qa/OPS-FRM-10.w9.json | nihil |
| B1 G-2 butir 2 | Pemeriksaan rujukan diulang dengan reports/orch/refcheck2.py: keluaran penuh (TSV dan JSON, 2.242 kemunculan), kontrol positif SOP-04 Bagian 7.5 di versi lama FRM-10, ditambah pemeriksaan makna dua putaran (614 dan 134 rujukan). Angka di Laporan_Run diperbaiki; klaim W8 ditarik | reports/w9/refcheck_baseline.*, refcheck_final.*, refsem.json, refsem2.json; Laporan_Run bagian Gerbang mutu | 3 rujukan ke dokumen tim di luar set (POL-OPS-001, PRO-OPS-001) tidak dapat dicek |
| B2 Residu 6 dokumen | SNX-HR-SOP-11, SNX-HR-SOP-13, SNX-COM-SOP-02, SNX-MKT-RPT-01, SNX-MKT-REG-01, SNX-MKT-REG-02 dikerjakan. Pertentangan SNX-HR-SOP-13 bagian 9 dengan butir 4.3 hilang lewat pengecualian Direktur Utama di 4.3 berlabel (USULAN) | qa/<KODE>.w9.json; Laporan_Run tabel Residu mutu | SNX-HR-SOP-13: kasus Direktur Utama hanya sebagai Atasan Langsung Asal belum disebut di 4.3 (Samuel, Aziz). SNX-COM-SOP-02: Brand & Marketing tidak ditambahkan karena tidak punya peran di bagian 5 (owner) |
| B3 Verifikasi 2 form | SNX-OPS-FRM-03 dan SNX-ISMS-REG-01 diverifikasi isi terhadap sumber: PASS, 0 pemblokir | qa/OPS-FRM-03.verify.json, qa/ISMS-REG-01.verify.json | nihil |
| B4 Open item dan tabel | 34 dari 34 open item berpemutus LEAD ditutup dengan alasan; sebutan dokumen yang belum ada diseragamkan "dalam peninjauan"; tabel SNX-HR-RPT-01 dan SNX-MKT-RPT-01 diberi baris judul berulang (w:tblHeader) dan baris tidak terbelah (w:cantSplit) lewat tech_fix renderer opt-in | reports/w9/lead_items.json; grep.txt (dalam pengerjaan 0); ledger.json w9.tech_fixes; selftest.txt 6 OK | 942 open item lain tetap terbuka untuk pemutus non-LEAD |

## C. Gerbang (semua rc 0)

| Gerbang | Command | Bukti | Hasil |
|---|---|---|---|
| Selftest | `bash tools/selftest.sh` | reports/w9/selftest.txt | 6 OK, rc 0 |
| Lint dan OOXML | lint_doc.py per docx; validator OOXML skill docx | reports/w9/gate_final.jsonl | 53 docx lint lulus, 53 PASSED |
| Fitur xlsx | features() dari tools/xlsx_patch.py, HEAD dibanding 4a40352; teks CONTOH | reports/w9/gate_final.jsonl | 17 xlsx, 0 fitur berkurang, 0 CONTOH |
| Blankscan | `python3 -I reports/orch/blankscan.py <docx>` | reports/w9/gate_final.jsonl | 0 halaman kosong di 53 docx |
| qa W9 | pemeriksa perubahan buta per dokumen | qa/<KODE>.w9.json (41 berkas) | 41 PASS |
| Refcheck penuh | `python3 -I reports/orch/refcheck2.py final` | reports/w9/refcheck_final.tsv, refcheck_final.json | rc 0; kontrol positif menembak (3 kemunculan TIDAK_ADA di versi lama); 0 TIDAK_ADA dan 0 DOK_TIDAK_ADA sesudah putusan makna. 613 rujukan silang atau non-ADA punya putusan makna: 610 OK, 3 tidak dapat dicek |
| Metascan | `python3 -I reports/orch/metascan.py` | reports/w9/metascan.txt | 0 temuan, kontrol positif menembak, rc 0 |
| Grep | `python3 -I grepgate.py` (teks paragraf, tabel, header, footer, sel xlsx dari 71 berkas out/) | reports/w9/grep.txt | HR Manager 1 (K-06); Divisi Legal 0 di dokumen; label menunggu konfirmasi pada garis JA-01 dan JA-02 ke JA-03 dan JA-04 nol |
| modifiedTime 54 sumber | Drive get_file_metadata, hanya baca, dua kali (03.40 sampai 03.55 UTC dan 04.42 UTC saat penutupan) | reports/w9/sources_modtime.json (kunci rows dan ukur_ulang_penutupan) | 54 dari 54 sama dengan ledger pada kedua pengukuran |
| Master List dan USULAN-OPEN | `python3 -I reports/orch/w8.py` | reports/w9/w8_rebuild.txt | 88 baris, 1.029 USULAN, 942 terbuka, 46 ditutup, kelompok LEAD 0, 0 sel memuat label W9 |
| Laporan_Run | bagian "Perubahan ISO-W9", baris gerbang dan penyimpangan W9 | reports/Laporan_Run.md | ada |
| Nol staging | transkrip sesi dan semua subagen; ledger staging_final | reports/w9/staging_nol.txt | satu-satunya panggilan = paket W8 1982 (01.22 UTC, sebelum gaspol W9); staging_final tidak berubah |

## GAP

| GAP | Dampak | Mitigasi yang diusulkan |
|---|---|---|
| 160 rujukan "butir X" di baris tabel menunjuk dokumen asalnya sendiri tanpa penanda "SOP ini" | Isinya benar, tetapi mudah salah baca. Bukti: dua pemeriksa makna membaca rujukan SNX-HR-SOP-11 "(butir 4.9 dan 6.5)" secara berbeda | Konvensi "SOP ini" atau "form ini" di semua rujukan diri, satu putaran khusus berarahan LEAD |
| 9 SOP tanpa nomor tampak "4.n" pada butir kebijakan (SNX-ISMS-PLN-01, SNX-ISMS-SOP-01 sampai 04, SNX-OPS-PRC-01, SNX-OPS-SOP-02 sampai 04) | Tidak ada rujukan yang benar-benar menunjuk butir tanpa nomor; hanya beda gaya antar-SOP | Keputusan LEAD atau owner: seragamkan atau biarkan |
| Pemeriksa makna putaran 2 tidak menjawab 4 dari 134 rujukan | Keempatnya diputus orkestrator dari kerangka dokumen, bukan oleh pemeriksa terpisah | Tercatat per baris di refsem2.json (sumber: orkestrator) |
| RUNBOOK §1 dan §11 menyebut lokasi lama Laporan_Run | Pembaca RUNBOOK mencari di out/00_Index | LEAD memperbarui RUNBOOK |

## OPEN DECISION

1. Ukuran tingkatan jabatan untuk JA-03, JA-04, dan bawahannya sesudah ada dua garis tegas: jalur mana yang dihitung (Aziz, owner).
2. Pengisian jabatan Finance Lead (owner).
3. SNX-HR-SOP-13: kasus Direktur Utama hanya sebagai Atasan Langsung Asal (Samuel, Aziz).
4. SNX-COM-SOP-02: perlukah Brand & Marketing diberi peran di bagian 5 (owner).
5. Description checklist baris 58 (tim Brand & Marketing).

## RESIDUAL RISK

- Paket staging 1982 (W8, PENDING) memuat klaim refcheck W8 yang sudah ditarik dan angka sebelum revisi. W9 tidak mengirim staging, jadi peninjau paket itu perlu membaca reports/Laporan_Run.md versi ini.
- Tampilan cetak SNX-FAT-REG-01 (teks tanpa wrap) belum dilihat manusia: HUMAN-VERDICT.
- 3 rujukan ke dokumen tim di luar set tidak dapat dicek sampai dokumen itu tersedia.

## Retraksi

| Klaim | Kanal bukti klaim | Kanal bukti retraksi |
|---|---|---|
| W8: "177 rujukan dicek, 0 rusak" | reports/w8/refcheck.txt | berkas itu hanya berisi "{}"; alat W8 tidak membaca sub-nomor di luar bagian 4 dan 6; kontrol positif SOP-04 Bagian 7.5 lolos di alat lama dan menembak di refcheck2 |
| Rencana W9 (03.05 UTC): rujukan LEG, FAT, dan HR-SOP rusak | keluaran refcheck2 awal | pemeriksa makna (refsem.json) dan cek kerangka langsung: rujukan ke dokumen asal sendiri. Klaster penomoran dibatalkan |

## Tafsir yang dipakai

- Days overdue = TODAY() dikurangi Due date, mengikuti rumus yang sudah ada di sheet AP.
- SNX-LEG-SOP-01 menyebut versi lama sebagai "versi 0.1 SOP ini", tidak memakai judul lain.
- A8: baris 58 checklist tidak diperlakukan sebagai salinan persis baris 57.
- SPV tidak ditambahkan karena syarat "bila ada kolom tingkat jabatan" tidak terpenuhi di dokumen mana pun.
- Gerbang "nol Divisi Legal" diterapkan pada teks dokumen. Nama berkas Drive tim di kolom sumber Master List tidak diubah, karena mengubahnya berarti salah mengutip sumber.
- Vonis BASI pemeriksa putaran 2 atas SNX-HR-SOP-11 (Q016) ditolak dengan dua kanal: pola tabel bagian 11 dan putusan putaran 1 (R120).
