# Laporan Run Dokumen ISO SINUX (COS), 15 Oktober 2026

Receipt (diperbarui ISO-W10, 15 Okt 09.21 UTC; bagian "Perubahan ISO-W10"): ledger.json, config/checklist.json (checklist live, modifiedTime 2026-10-14T17:47:13Z, 87 baris; worklist 88 butir), qa/, reports/w8/, reports/w9/ di repo sinux-iso-docs. Run awal diukur 15 Oktober 2026 pukul 01.10 sampai 01.20 UTC; revisi ISO-W9 (bagian "Perubahan ISO-W9" di bawah) diukur ulang 15 Oktober 2026 pukul 03.40 sampai 04.45 UTC. Sesudah revisi: 1.029 kalimat atau baris berlabel (USULAN) di 70 dokumen.

Laporan ini bahan kerja internal dan tidak diunggah. Berkas yang diunggah hanya isi out/ (dokumen ISO dan out/00_Index/Master_List_COS.xlsx).

## Ringkasan

- 70 dokumen target selesai berstatus DONE (Draft Rev00): 44 perbaikan dokumen tim (T1), 23 dokumen baru (T2), 3 baris HOLD yang dipromosikan karena berkas tim terbaca (W7b). Nol dokumen tertahan di gerbang mutu dan nol dokumen terblokir.
- 16 baris HOLD menunggu berkas tim (T3). 2 baris SKIP: Statement of Applicability (lane konsultan, tidak disentuh) dan cetakan SOP.
- 70 dari 70 dokumen lolos pemeriksaan isi independen terhadap sumber dan kriteria checklist. Dua form W5 yang semula di luar sampel (SNX-OPS-FRM-03, SNX-ISMS-REG-01) diverifikasi di ISO-W9: PASS, 0 pemblokir.
- Revisi ISO-W9 (15 Okt, arahan LEAD G-2 dan G-3 atas keputusan owner): 41 dokumen diubah lewat spec lalu dirender ulang; tiap dokumen yang berubah diperiksa ulang oleh pemeriksa perubahan terpisah (41 dari 41 PASS). Rincian di bagian "Perubahan ISO-W9".
- Revisi ISO-W10 (15 Okt, arahan LEAD G-4, pass bahasa dan form rapi): 60 dari 70 dokumen lolos semua gerbang termasuk pemeriksa bahasa buta; 10 residu dikembalikan ke versi sesudah ISO-W9 dan bernama di reports/REVIEW-W10.md. Rincian di bagian "Perubahan ISO-W10".
- Putaran penghalusan sesudah DONE dijalankan pada 40 dokumen; tiap perubahan diperiksa ulang oleh pemeriksa perubahan terpisah sebelum commit "ISO <KODE> polish".
- Semua dokumen masih Draft: tanda tangan, tanggal efektif, dan pengesahan diisi penyetuju. Label (USULAN) menandai isi yang menunggu keputusan; daftar lengkapnya ada di Master_List_COS.xlsx sheet USULAN.

## Jumlah per departemen

| Departemen | DONE | HOLD (T3) | SKIP | Total |
|---|---|---|---|---|
| Human Resource | 10 | 9 | 1 | 20 |
| Finance, Accounting & Tax | 8 | 4 | 0 | 12 |
| Legal | 12 | 1 | 0 | 13 |
| Commercial | 5 | 2 | 0 | 7 |
| Marketing | 4 | 0 | 0 | 4 |
| Operation | 17 | 0 | 0 | 17 |
| ISMS | 14 | 0 | 1 | 15 |
| Total | 70 | 16 | 2 | 88 |

Catatan FAT: satu baris HOLD (FAT KPI & Performance Monitoring Report) tidak ada lagi di checklist live; tetap dicatat sebagai HOLD.

## Hasil per gelombang

| Gelombang | Isi | DONE |
|---|---|---|
| W0 | Pilot SNX-ISMS-SOP-02 | 1 |
| W1 | Struktur Organisasi, Job Analysis | 2 |
| W2 | SOP dan prosedur Operation dan ISMS | 12 |
| W3 | SOP FAT, Legal, Commercial, Cuti | 6 |
| W4 | SOP HR (Promotion, Demotion, Rotation, Mutation), FAT, Legal, Commercial | 7 |
| W5 | Form dan register Operation dan ISMS (15 xlsx, 3 docx) | 18 |
| W6 | Register, form, laporan Legal | 6 |
| W7 | Dokumen baru HR, FAT, Legal, Commercial, Marketing | 15 |
| W7b | Promosi HOLD FAT (SOP Accounting, Billing & Collection Register, Access Authorization Records) | 3 |

## USULAN yang perlu keputusan

Jumlah kalimat atau baris berlabel (USULAN) di dokumen jadi, dikelompokkan menurut pemutus yang disarankan (rincian per kalimat: Master_List_COS.xlsx, sheet USULAN):

| Pemutus | Jumlah | Departemen terbanyak |
|---|---|---|
| Legal | 238 | Legal 226 |
| Aziz (HR Lead) | 213 | Human Resource 210 |
| Fani (VP Tech Operation and Services) | 180 | ISMS 72, Operation 71 |
| Owner | 177 | Commercial 63, Marketing 56 |
| FAT | 112 | FAT 107 |
| Samuel (Direktur Utama) | 49 | Human Resource 38 |
| Konsultan (acuan klausul ISO) | 41 | Legal 12, Human Resource 10 |
| Laras (VP Commercial) dan lainnya | 19 | Marketing 17 |

Angka di atas sesudah revisi ISO-W9 (total 1.029; sebelum revisi 1.053). Label USULAN yang hilang di W9 terutama pemetaan peran Legal dan batas cakupan Marketing yang kini sudah diputus.

Keputusan lintas dokumen yang membuka paling banyak USULAN sekaligus:

| No | Keputusan | Dokumen terdampak | Pemutus |
|---|---|---|---|
| 1 | Ukuran tingkatan jabatan (saat ini jumlah garis lapor sampai Direktur Utama, karena Job Analysis tanpa grading). Sejak JA-03 dan JA-04 punya dua garis tegas (W9), ukuran ini bermakna ganda untuk JA-03, JA-04, dan bawahannya; perlu aturan jalur mana yang dihitung | SNX-HR-SOP-10 sampai 13, SNX-HR-FRM-01, SNX-HR-FRM-02 | Aziz, owner |
| 2 | Atasan langsung JA-05, JA-08, JA-10, JA-11, JA-14 (garis lapor menunggu konfirmasi, K-02 sampai K-04). JA-03 dan JA-04 sudah diputus di W9: dua garis tegas ke Direktur dan Direktur Utama | SNX-HR-ORG-01 dan semua dokumen yang memakai garis lapor | Aziz, owner |
| 3 | Authority Matrix (DoA) belum terbit: pejabat penyetuju dan batas nilai | SNX-HR-JA-01, SNX-LEG-FRM-01, SNX-LEG-FRM-02, SNX-FAT-FRM-01, SNX-COM-SOP-02 | Samuel |
| 4 | Finance Lead dan Finance Staff (W9: tetap nama peran; Finance Lead dijalankan Direktur sampai jabatannya terisi, Finance Staff dijalankan JA-10 dan JA-11, keduanya berlabel USULAN; Reviewed By dokumen FAT = Direktur). Sisa keputusan: pengisian jabatan Finance Lead | semua dokumen FAT | owner, FAT |
| 5 | Pemetaan Line Manager Legal dan Staff Legal: DIPUTUS di W9 (JA-08 Ester Febe Utomo, JA-09 Alif Altamziz; Prepared dan Reviewed dokumen Legal bernama) | semua dokumen Legal | selesai |
| 6 | Masa simpan dan lokasi rekaman yang belum ditetapkan sumber | hampir semua form dan register | Legal, FAT |
| 7 | Tarif PPN 12 persen dan rumus Gov/SOE (WAPU) di register piutang | SNX-FAT-REG-01, SNX-FAT-SOP-05 | FAT |
| 8 | Cakupan register Marketing: DIPUTUS di W9 (REG-01 satu-satunya register materi dan klaim; REG-02 hanya pelaksanaan campaign dan aktivitas; REG-03 lead; RPT-01 membaca REG-02 dan REG-03). Sisa: Description checklist baris 58 berisi pengendalian materi baris 57 yang diperluas dengan validasi klaim, bukan pelaksanaan campaign sesuai judulnya; perlu dibetulkan Brand & Marketing | SNX-MKT-REG-01, SNX-MKT-REG-02, SNX-MKT-REG-03, SNX-MKT-RPT-01 | tim Brand & Marketing |
| 9 | Process Owner dokumen Commercial baru: DIPUTUS di W9 (VP Commercial) | SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01 | selesai |
| 10 | Susunan Divisi Operation (NOC, SOC, SD dan PM) yang masih berstatus usulan | SNX-HR-ORG-01, SOP HR mutasi dan rotasi, dokumen Operation | owner, Fani |
| 11 | Acuan klausul ISO per dokumen yang tidak diberi checklist | 41 kalimat berlabel "perlu konfirmasi konsultan" | konsultan |

## Open items

Tiap dokumen mencatat open item di bagian notes masing-masing (folder notes/ di repo). Ringkasan sesudah revisi ISO-W9: 942 butir terbuka, terbanyak untuk Fani (315), owner (257), Legal (150), Aziz (109); 46 butir ditutup di W9, termasuk 34 dari 34 butir berpemutus LEAD (alasan per butir di reports/w9/lead_items.json). Sebelum revisi: 985 butir. Rincian per pemutus untuk tinjauan internal: reports/USULAN-OPEN-per-pemutus.md (bagian akhir memuat daftar butir yang ditutup beserta alasannya).

## Dokumen T3 yang masih ditunggu dari tim

| Baris | Departemen | Judul checklist |
|---|---|---|
| 3 | HR | SOP Recruitment & Selection |
| 4 | HR | SOP Employee Onboarding |
| 5 | HR | SOP Training & Development |
| 6 | HR | SOP Performance Appraisal |
| 7 | HR | SOP Employee Offboarding |
| 12 | HR | Employee Personnel File Checklist |
| 13 | HR | Employee Confidentiality / NDA Acknowledgement Records |
| 14 | HR | SOP Company Asset |
| 15 | HR | SOP Payroll Process |
| 24 | FAT | SOP Account Receivable & Collection |
| 25 | FAT | SOP Payment and Disbursement Approval |
| 31 | FAT | Financial Document Register |
| (tidak ada di checklist live) | FAT | FAT KPI & Performance Monitoring Report |
| 43 | Legal | NDA / Confidentiality Agreement Template |
| 50 | Commercial | SOP Sales Incentive Process |
| 51 | Commercial | Sales Pipeline & Opportunity Register |

Tim menandai baris ini ada, tetapi berkasnya tidak terbaca saat pengukuran ulang W0. Begitu berkas tersedia, baris diproses sebagai T1 di run berikutnya.

## Perubahan ISO-W9

Dasar: arahan LEAD G-2 (15 Okt 02.04 UTC) dan G-3 (02.21 UTC) di control/LEAD-GUIDE.md, atas keputusan owner. Semua perubahan isi lewat specs/ lalu dirender ulang. Status tetap Draft, tanpa tanda tangan dan tanggal efektif. Commit per dokumen berjudul "ISO <KODE> polish".

| Butir | Yang dikerjakan | Dokumen |
|---|---|---|
| G-2 butir 1 | Enam rujukan basi SNX-OPS-FRM-10 ke SNX-OPS-SOP-04 dan SNX-OPS-SOP-05 dibetulkan; total 11 rujukan di form itu disesuaikan | SNX-OPS-FRM-10 |
| G-2 butir 2 | Pemeriksaan rujukan diulang dengan alat baru (reports/orch/refcheck2.py): keluaran penuh, kontrol positif, ditambah pemeriksaan makna dua putaran | lihat Gerbang mutu |
| G-2 butir 3 | Laporan ini dipindah dari out/00_Index ke reports/ (git mv); rujukan di perkakas internal diperbarui | reports/ |
| A1 | Ejaan Kristanto dipakai; K-07 ditulis sudah diputus | SNX-HR-ORG-01 (SNX-HR-JA-01 sudah benar) |
| A2 | HR Lead menggantikan HR Manager; K-06 diperbarui. SPV tidak ditambahkan karena tidak ada dokumen dengan kolom tingkat jabatan | 10 dokumen HR |
| A3 | Garis JA-01 ke JA-03 tegas tanpa label, garis baru JA-01 ke JA-04; K-01 ditutup; dokumen yang memakai garis lapor atau nama atasan diselaraskan | 27 dokumen |
| A4 | Garis JA-05, JA-08, JA-10, JA-11, JA-14 tidak diubah (diperiksa) | 5 dokumen yang menyebutnya |
| A5 | Peran Legal bernama (JA-08 Ester Febe Utomo, JA-09 Alif Altamziz); label USULAN pemetaan dihapus; sebutan "Departemen Legal" | 14 dokumen |
| A6 | Definisi Finance Lead dan Finance Staff; Reviewed By dokumen FAT = Amirull Yusuf Zulkarnain / Direktur; K-13 diperbarui | 10 dokumen |
| A7 | Process Owner = VP Commercial | SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01 |
| A8 | Restrukturisasi register Marketing (lihat keputusan 8) | 4 dokumen MKT |
| A9 | Gambar xlsx tidak diubah; open item gambar ditutup | SNX-OPS-FRM-10 |
| A10 | Validasi kolom K dan L sampai baris 1000; rumus Days overdue = TODAY() dikurangi Due date (pola sheet AP); baris 7 sheet AP dikosongkan | SNX-FAT-REG-01 |
| B2 | Residu W8 enam dokumen (tabel Residu mutu); pertentangan SNX-HR-SOP-13 bagian 9 dengan butir 4.3 hilang | 6 dokumen |
| B3 | SNX-OPS-FRM-03 dan SNX-ISMS-REG-01 diverifikasi isi: PASS, 0 pemblokir | 2 form |
| B4 | 34 open item berpemutus LEAD ditutup dengan alasan; sebutan dokumen yang belum ada diseragamkan menjadi "dalam peninjauan"; tabel SNX-HR-RPT-01 dan SNX-MKT-RPT-01 diberi baris judul berulang dan baris tidak terbelah | 17 dokumen |
| Rujukan | 22 rujukan basi, rusak, atau berstatus basi dari pemeriksaan makna dibetulkan (reports/w9/ref_fixes.json) | 9 dokumen |

Cara kerja: 12 klaster penyusun pada dokumen yang tidak beririsan; tiap dokumen yang berubah diperiksa pemeriksa perubahan buta yang terpisah dari penyusun. 67 pemeriksaan untuk 41 dokumen; 4 dokumen (SNX-FAT-FRM-01, SNX-FAT-REG-01, SNX-HR-JA-01, SNX-MKT-REG-01) butuh satu putaran perbaikan. Hasil akhir 41 dari 41 PASS (qa/<KODE>.w9.json). Teks keluaran yang di-commit identik dengan teks yang diperiksa.

Klaim yang ditarik di ISO-W9 (tercatat di ledger.json retractions):

1. Klaim W8 "177 rujukan dicek, 0 rusak" (baris gerbang W8 di bawah).
2. Rencana W9 mencatat dugaan rujukan rusak di dokumen LEG, FAT, dan HR-SOP. Ternyata rujukan itu menunjuk butir dokumen asalnya sendiri dan salah ditebak alat. Dibuktikan lewat pemeriksa makna dan cek kerangka dokumen. Rencana perbaikan penomoran dibatalkan.

Tafsir yang dipakai saat arahan tidak merinci: rumus Days overdue mengikuti pola sheet AP; SNX-LEG-SOP-01 menyebut versi lamanya "versi 0.1 SOP ini", bukan judul lain; Description checklist baris 58 tidak identik dengan baris 57; SPV tidak ditambahkan; "Divisi Legal" tetap muncul 3 kali di kolom sumber Master List karena itu nama berkas Drive tim yang dikutip apa adanya.

## Perubahan ISO-W10

Dasar: arahan LEAD G-4 (pass bahasa dan form rapi) di control/LEAD-GUIDE.md, atas keputusan owner; gaspol owner 06.52 UTC ("Gaspol, saya prefer all document. Make sure semua dikerjakan dengan baik"). Basis substansi bed1bb6. Semua perubahan isi lewat specs/ (docx) atau patch xlsx di atas berkas bed1bb6, lalu dirender ulang. Status tetap Draft, tanpa tanda tangan dan tanggal efektif. Nomor butir dan heading tidak berubah (dijaga mesin).

| Yang dikerjakan | Hasil | Bukti |
|---|---|---|
| Peta istilah STYLE §1.5 dan diksi §2.5 (rekaman, tiket, formulir, tinjauan, lewat, sesudah) lewat satu skrip mekanis sebelum penyusun bahasa | diterapkan ke 70 dokumen; heading beku tidak dipetakan (jembatan istilah pada pemakaian pertama); judul klausul ISO dikembalikan | reports/w10/terms/, terms_summary.json |
| Pass bahasa per dokumen (penyusun Opus effort medium, per departemen) | 60 dokumen lolos pemeriksa bahasa buta, 10 residu dikembalikan ke bed1bb6 | qa/<KODE>.w10.json, reports/w10/residu/ |
| Kerapian docx: rata kiri, header tabel berulang, baris tidak terbelah, paragraf sebelum tabel menempel, lebar kolom langkah SOP | 60 dokumen; justified_cells 2.152 menjadi 0, tabel tanpa header 693 menjadi 0 | reports/w10/gates/ |
| Kerapian xlsx: freeze, wrap, landscape, fitToWidth 1, print titles, tinggi baris, A3 untuk register sangat lebar | 17 xlsx lolos; menutup residu cetak SNX-FAT-REG-01 | reports/w10/xlsx_sheets.json, xlsx_effective/ |
| Audit pointer retroaktif dan audit cakupan label (USULAN) atas semua dokumen yang lolos | 211 jalur pointer di 20 dokumen diaudit: 198 lengkap, 10 rujukan dikembalikan, 3 dilengkapi; 113 jalur label diaudit, 37 diperbaiki ke cakupan bed1bb6, ditambah 3 koreksi worker (SNX-COM-REG-01, SNX-COM-SOP-01, SNX-COM-SOP-02) | notes/<KODE>.md subjudul "W10 audit pointer" dan "W10 audit cakupan label" |

Angka bahasa pada 60 dokumen lolos (bed1bb6 ke W10): calque 53 ke 0; "lewat" 136 ke 0; kalimat penunjuk 51 ke 0; butir instruksi yang diawali nama peran 35 ke 9 dari 861; jumlah kata 134.425 ke 133.338; label (USULAN) 954 ke 993. Label bertambah karena rujukan ke butir berlabel yang diganti fakta wajib membawa labelnya. Form docx (17 lolos): total halaman 226 ke 225, halaman awal bagian isi tidak naik di dokumen mana pun.

## Gerbang mutu yang diukur

| Klaim | Cara ukur | Bukti | Hasil |
|---|---|---|---|
| Substansi beku (ISO-W10) | w10_langscan diff bed1bb6 lawan W10 per dokumen (butir, heading, nama orang, kode SNX tidak boleh muncul; selisih angka dan usul_butir tercatat di notes); kontrol positif diff OPS-FRM-10 versi 4a40352 menembak "7.5" | reports/w10/gates/, reports/w10/close/langscan_diff_kontrol_positif.txt | 60 lolos; kontrol positif menembak |
| Bahasa (ISO-W10) | w10_langscan scan per berkas final | reports/w10/close/gate_final.jsonl | 60 dokumen lolos: calque 0, lewat 0, justified_cells 0, tabel tanpa header 0, butir instruksi diawali peran paling banyak 25 persen |
| Pemeriksa bahasa buta (ISO-W10) | rubrik a sampai d, PASS bila semua 4 atau lebih; gagal sekali satu putaran perbaikan, gagal kedua kembali ke bed1bb6 | qa/<KODE>.w10.json, .w10.r1.json, .w10.r2.json | 60 PASS (43 putaran pertama, 17 sesudah perbaikan); 10 residu |
| Lint, OOXML, halaman kosong, fitur xlsx (ISO-W10) | lint_doc, validator OOXML, blankscan pada 53 docx; fitur xlsx_patch dan CONTOH pada 17 xlsx, dibanding bed1bb6 | reports/w10/close/gate_final.txt, gate_final.jsonl | 53 lint lulus, 53 OOXML PASSED, 0 halaman kosong; 0 fitur xlsx berkurang, 0 CONTOH |
| Rujukan (ISO-W10) | refcheck2 tag w10 pada 70 berkas; 13 rujukan yang kalimatnya diubah W10 diputus ulang terhadap putusan W9 | reports/w10/close/refcheck_w10.txt, .tsv, .json; reports/w10/refsem_w10.json | 1.793 kemunculan; kontrol positif menembak; 0 TIDAK_ADA, 0 DOK_TIDAK_ADA |
| Frasa meta, sebutan beku, sumber (ISO-W10) | metascan; grepgate HR Lead, Kristanto, Divisi Legal, Daffa bed1bb6 lawan W10; modifiedTime 54 sumber 07.02 dan 09.00 UTC | reports/w10/close/metascan.txt, grepgate.txt; reports/w10/sources_modtime.json | metascan 0 dengan kontrol positif; HR Lead 248=248, Kristanto 93=93, Divisi Legal 0, Daffa 0; 54 dari 54 sumber sama pada kedua pengukuran |
| Rujukan butir dan bagian ada (ISO-W9) | refcheck2 pada 70 berkas (53 docx, 17 xlsx): 2.242 kemunculan, 383 rujukan silang unik; kontrol positif "SNX-OPS-SOP-04 Bagian 7.5" di versi lama SNX-OPS-FRM-10 wajib terbaca TIDAK_ADA; 613 rujukan silang dan rujukan yang tidak terbaca ADA diperiksa makna dalam dua putaran | reports/w9/refcheck_final.tsv, refcheck_final.json, refsem.json, refsem2.json | rc 0; kontrol positif menembak; 0 TIDAK_ADA sesudah putusan makna; 610 OK, 3 tidak dapat dicek karena menunjuk dokumen tim di luar set (POL-OPS-001, PRO-OPS-001) |
| Frasa meta nol (ISO-W9) | metascan pada 70 berkas, kontrol positif | reports/w9/metascan.txt | 0 temuan; kontrol positif menembak |
| Lint, OOXML, halaman kosong (ISO-W9) | lint_doc, validator OOXML, blankscan pada 53 docx | reports/w9/gate_final.jsonl | 53 lint lulus, 53 OOXML PASSED, 0 halaman kosong |
| Fitur xlsx utuh (ISO-W9) | fitur xlsx_patch (sheet, gambar, chart, validasi, conditional formatting, rumus) dibanding versi sebelum W9, teks CONTOH | reports/w9/gate_final.jsonl | 17 xlsx, 0 fitur berkurang, 0 teks CONTOH |
| Selftest perkakas (ISO-W9) | tools/selftest.sh | reports/w9/selftest.txt | 6 OK |
| Sebutan lama hilang (ISO-W9) | grep teks 70 berkas dan Master List | reports/w9/grep.txt | HR Manager 1 (hanya K-06, diizinkan), Divisi Legal 0 di dokumen, Daffa 0, em-dash 0; garis JA-01 dan JA-02 ke JA-03 dan JA-04 tanpa label menunggu konfirmasi (teks dan edges bagan di spec SNX-HR-ORG-01). Satu-satunya label yang menyentuh JA-03 adalah garis JA-05 ke JA-03 (K-02), yang menurut A4 tidak diubah |
| Sumber tidak berubah selama W9 (ISO-W9) | modifiedTime 54 berkas sumber, hanya baca, diukur 03.40 sampai 03.55 UTC dan diulang saat penutupan | reports/w9/sources_modtime.json | 54 dari 54 sama pada kedua pengukuran |
| Frasa meta proses penyusunan nol di seluruh out/ (W8) | pola (dokumen sumber, sumber tim, di sumber, draf ini, belum berdokumen, penyusun bukan nama peran) pada 70 berkas, kontrol positif pada versi lama SNX-LEG-SOP-02 | reports/w8/metascan.txt | 0 temuan; kontrol positif menembak |
| Rujukan silang ke butir SOP lain ada (W8, DITARIK di ISO-W9) | klaim W8 "177 rujukan dicek, 0 rusak" tidak berbukti: reports/w8/refcheck.txt hanya berisi "{}" dan alat W8 tidak mengecek sub-nomor di luar bagian 4 dan 6, sehingga "SNX-OPS-SOP-04 Bagian 7.5" lolos | reports/w8/refcheck.txt | diganti hasil ISO-W9 di bagian "Perubahan ISO-W9" |
| Tidak ada halaman kosong (W8) | render PDF tiap docx, teks per halaman | reports/w8/blankscan.txt | 53 docx, 0 halaman kosong |
| Format sama dengan acuan | renderer terkunci (sidik format), pemeriksa PDF pada 12 dokumen | tools/selftest.sh, qa/*.pdfcheck.json | selftest 6 OK; 12 PASS |
| Lint dan validasi OOXML | lint_doc dan validator OOXML tiap render | qa/*.lint.json, ledger.json | semua lulus |

## Residu mutu

Residu ISO-W10 (gagal kedua pemeriksa bahasa buta; spec, notes, dan out dikembalikan ke bed1bb6; percobaan tersimpan di reports/w10/residu/): SNX-OPS-FRM-10, SNX-LEG-FRM-02, SNX-LEG-REG-04, SNX-LEG-RPT-01, SNX-MKT-REG-02, SNX-MKT-REG-03, SNX-MKT-RPT-01, SNX-OPS-SOP-01, SNX-OPS-SOP-02, SNX-ISMS-PRO-01. Isinya sama dengan versi sesudah ISO-W9. Rincian per dokumen di reports/REVIEW-W10.md.

Residu W8 (6 dokumen) dikerjakan di ISO-W9 (arahan LEAD G-3 B2):

| Dokumen | Residu W8 | Status sesudah ISO-W9 |
|---|---|---|
| SNX-HR-SOP-11 | istilah mutasi bentrok dengan butir 4.9; satu kalimat pasif baru; penerima tanggapan di bagian 9 belum jelas; "berkas usulan" belum didefinisikan; NOC, SOC, SD dan PM tanpa definisi | selesai; penerima tanggapan kasus JA-12 ditetapkan HR Lead berlabel (USULAN), pemutus Samuel dan owner |
| SNX-HR-SOP-13 | aturan Direktur Utama di bagian 9 bertentangan dengan butir 4.3; label (USULAN) bergeser; istilah NOC dan SOC beda dengan SNX-HR-SOP-12 | selesai; pertentangan bagian 9 dengan 4.3 hilang lewat pengecualian Direktur Utama di butir 4.3 berlabel (USULAN). Sisa: kasus Direktur Utama hanya sebagai Atasan Langsung Asal belum disebut di 4.3 (pemutus Samuel, Aziz) |
| SNX-COM-SOP-02 | pengganti "Personel Commercial" mempersempit cakupan bagian 9 dan Kesimpulan | sebagian: bagian 9 dikembalikan; Brand & Marketing tidak ditambahkan karena tidak punya peran di bagian 5 (open item owner) |
| SNX-MKT-RPT-01 | arti Aktivitas belum sama dengan SNX-MKT-REG-02; belum Selesai mencakup Dibatalkan | selesai lewat A8 |
| SNX-MKT-REG-01 | penurunan klasifikasi dicatat di bukti persetujuan | selesai: mengikuti SNX-ISMS-PRO-01 di SNX-ISMS-REG-01; REG-01 hanya merujuk |
| SNX-MKT-REG-02 | irisan kolom dengan REG-01 dan irisan aktivitas dengan RPT-01 | selesai lewat A8 (kolom materi dan klaim dihapus) |

Temuan tidak memblokir lain per dokumen tersimpan di qa/<KODE>.verify.json, qa/<KODE>.sweep.json, dan qa/<KODE>.w9.json.

## Penyimpangan dan catatan proses

| Waktu (UTC) | Hal | Penanganan |
|---|---|---|
| 14 Okt 19.05 | Container tanpa graphviz; selftest awal 2/6 | apt-get install graphviz; selftest 6/6 (reports/W0-selftest.txt) |
| 14 Okt W0 | Pesan owner dibaca keliru sebagai izin bersyarat untuk mulai | Ditarik kembali; run menunggu kata "gaspol" dari owner (21.23) |
| 14 Okt 21.33 sampai 15 Okt 00.00 | Lima perbaikan teknis perkakas: xlsx_patch (warna baris dikosongkan, dua versi; tambah sheet Kontrol Dokumen untuk sumber Google Sheet), render diagram (garis putus-putus untuk garis lapor menunggu konfirmasi), pemeriksaan halaman kosong otomatis | Cadangan berkas lama disimpan; selftest 6 OK sesudah tiap perubahan; rincian di ledger.json tech_fixes |
| 14 Okt W2 | Sesaat enam penyusun berjalan bersamaan (batas lima) | Sesudahnya perbaikan diantrekan sampai slot kosong |
| 15 Okt 00.33 | Satu agen penyusun FAT-REG-01 mengambil salinan berkas dari log sesinya sesudah satu perintahnya ditolak pengaman | Salinan itu tidak dipakai; sumber diunduh ulang dari Drive (hanya baca), isi sel terbukti identik, keluaran dirender dari salinan bersih |
| 15 Okt 00.35 | Orkestrator menyebut Description checklist baris 58 "identik" dengan baris 57 | Dikoreksi lewat pengukuran ulang (tidak identik; baris 58 = baris 57 ditambah validasi klaim); keputusan cakupan disesuaikan |
| 15 Okt 00.50 | Arahan LEAD G-1 (frasa meta) | Dipatuhi: sweep sebelum Master List, ukur ulang nol, commit "polish" sejak G-1 terbaca (delapan sweep sebelumnya ter-commit "DONE") |
| Beberapa kali | Pemeriksa menjalankan git log/status hanya baca padahal prompt melarang git | Tidak ada perubahan keadaan; prompt diperjelas |
| 15 Okt 03.05 (W9) | Rencana W9 mencatat dugaan rujukan rusak di dokumen LEG, FAT, dan HR-SOP | Ditarik dengan dua kanal (pemeriksa makna dan cek kerangka); klaster penomoran dibatalkan |
| 15 Okt W9 R1 | Dua instruksi penyusun kurang lengkap (pengecualian nama di SNX-HR-ORG-01 dan SNX-HR-JA-01; satu sebutan "dalam pengerjaan") dan satu penyusun menghapus kode dokumen dari "(butir K-13)" | Diperbaiki di putaran R2, diperiksa ulang PASS |
| 15 Okt W9 | Pembuat Master List membaca keterangan "diubah W9" di sel pemutus sebagai pemutus LEAD, dan menulis label internal "ISO-W9" di Master List | Keterangan dibuang sebelum pengelompokan; label dinetralkan; kelompok LEAD 0 |
| 15 Okt 04.40 (W9) | Pemeriksa makna putaran 2 tidak menjawab 4 dari 134 rujukan dan memvonis 1 rujukan basi yang di putaran 1 diputus OK | Kelimanya diputus dari kerangka dokumen; vonis basi ditolak karena rujukan menunjuk SNX-HR-SOP-11 sendiri; nol perubahan dokumen (reports/w9/refsem2.json) |
| 15 Okt 04.45 (W9) | Skrip gerbang akhir menjalankan lint_doc pada 17 xlsx (alat itu hanya untuk docx) | Diganti cek fitur xlsx_patch; bukan cacat dokumen |

| 15 Okt 06.52 sampai 09.20 (W10) | Batas 3 subagen paralel sempat terlampaui sekali; tiga agen menjalankan git hanya baca; satu agen me-render ulang dokumen yang sudah lolos sehingga gerbang audit pointer menolaknya | Agen dihentikan tanpa perubahan berkas; tercatat di ledger agent_incidents; dokumen itu lolos sesudah audit pointer |
| 15 Okt W10 | Skrip istilah memetakan "lewat" bermakna "terlampaui" menjadi "melalui" di 3 tempat (SNX-ISMS-REG-04, SNX-LEG-REG-04, SNX-HR-SOP-11) dan judul klausul ISO | Dibetulkan penyusun; judul klausul dikembalikan mesin (isotitles) |
| 15 Okt W10 | Cakupan label (USULAN) bergeser saat kalimat digabung atau dipisah (ditemukan pemeriksa di SNX-HR-SOP-10, 11, 12) | Satu putaran perbaikan; audit cakupan label retroaktif atas semua dokumen lolos |

Nol mutasi Google Drive, nol tulisan ke kanon KB, nol tanda tangan atau tanggal efektif, nol kredensial di keluaran. Ringkasan run awal dikirim ke antrean tinjauan admin pada 15 Okt 01.22 UTC (paket 1982, status PENDING). Paket itu memuat klaim rujukan W8 yang sudah ditarik dan angka sebelum revisi ISO-W9. ISO-W9 tidak mengirim apa pun ke staging, jadi paket itu perlu dibaca bersama laporan ini.

## Cara unduh dan unggah

1. Unduh: repo sinux-iso-docs di GitHub, tombol Code, Download ZIP. Dokumen ada di folder out/ per departemen; daftar induk di out/00_Index/Master_List_COS.xlsx. Laporan ini ada di reports/ dan tidak ikut diunggah.
2. Tinjau: buka Master_List_COS.xlsx, filter sheet USULAN per pemutus; buka dokumen terkait dan putuskan tiap label (USULAN).
3. Unggah sesudah tinjauan: buat folder baru "COS Draft ISO" di Supporting Documents pada Shared Drive ISO SINUX, unggah isi out/ apa adanya. Berkas tim yang sudah ada tidak ditimpa.
4. Pengesahan: isi tanda tangan dan tanggal efektif di blok Approval tiap dokumen sesudah semua USULAN diputus; ubah status Draft menjadi status sah lewat penyetuju.
