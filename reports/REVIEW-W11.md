# REVIEW ISO-W11: verifikasi LEAD atas W10 dan koreksi cakupan substansi (15 Oktober 2026)

Pelaksana: LEAD ISO-B, langsung di sesi LEAD, tanpa sesi worker baru (owner menutup sesi ISO hari ini). Basis: bed1bb6 (substansi terverifikasi) dan 0a00bae (W10-DONE). Bukti: reports/w11/, notes/<KODE>.md bagian "W11 koreksi LEAD".

## Ringkasan
Paket final terdiri dari 60 dokumen berbahasa W10 dan 10 residu identik bed1bb6. Substansi semua dokumen setara bed1bb6 pada setiap unit yang diperiksa. Status Draft, siap diunggah dan direvisi manual oleh tim.

## Verifikasi mandiri atas 0a00bae
| Gerbang | Hasil |
|---|---|
| Diff substansi 60 dokumen (butir, heading, nama, kode) | 0 selisih |
| Pemindai bahasa (calque, lewat, sel rata kiri-kanan, tabel tanpa header, petunjuk diawali peran paling banyak 25 persen) | 0 pelanggaran; pola STARTS_ROLE diperbaiki (GAP 1 W10) |
| Xlsx: 51 sheet data (freeze, landscape, fitToWidth 1, print titles) | lengkap; 24 sheet gambar atau ringkasan dikecualikan sesuai daftar |
| Lint, OOXML, selftest | 70 dari 70; selftest 6 OK di klon bersih |
| Refcheck mandiri | 0 tujuan tidak ada |
| Drive 56 sumber (54 DONE plus 2 SKIP) | sama, 09.58 sampai 10.00 UTC |
| Staging dan jadwal | nol packet dari worker, nol jadwal aktif |

## Pemeriksaan makna buta (yang tidak tercakup gerbang mesin)
| Cakupan | Unit | FAIL | RAGU |
|---|---|---|---|
| Jalur audit pasca-PASS (GAP 2 W10) | 335 | 11 | 16 |
| Unit berisiko: label, token rujukan atau angka, teks menyusut lebih dari 25 persen, sel xlsx | 523 | 9 | 22 |
| Sampel acak unit bahasa-murni (seed 20261015) | 150 dari 1.482 | 0 | 1 |
Polanya: label (USULAN) yang dipindah ke akhir kalimat ikut menutupi aturan yang tadinya tidak berlabel; fakta pengganti penunjuk yang menyempit atau melebar; pelaku yang hilang.

## Koreksi
53 path di 25 dokumen dikembalikan ke cakupan bed1bb6 dengan bahasa W10, termasuk RAGU yang diputus LEAD (reports/w11/lead_gap2_temuan.md). Pemeriksa buta terpisah atas 53 perbaikan: 3 FAIL, lalu dibetulkan, lalu satu sisa dibetulkan dan PASS. Semua 25 build lolos gerbang worker (halaman form tidak naik). Master List dan USULAN-OPEN dibangun ulang (1.061 butir berlabel USULAN, 942 open item).
Diterima apa adanya: tiga sel pemetaan jabatan "Jabatan: Legal & Compliance (JA-0x)", kalimat perintah di sheet xlsx yang pelakunya tertulis di daftar, label pada node gambar FAT-SOP-04, serta penghapusan "jabatan tanpa pemegang" di COM-SOP-01, COM-SOP-02, dan COM-FRM-02 (faktanya tetap ada di Dokumen Terkait).

## Residu dan risiko
- 10 residu (OPS-FRM-10, LEG-FRM-02, LEG-REG-04, LEG-RPT-01, MKT-REG-02, MKT-REG-03, MKT-RPT-01, OPS-SOP-01, OPS-SOP-02, ISMS-PRO-01) tetap bergaya W9. Owner memilih revisi manual oleh tim.
- 1.332 unit bahasa-murni tidak diperiksa makna satu per satu. Sampel 150 unit menghasilkan 0 FAIL, jadi batas atas 95 persen kira-kira 2 persen. Tim membaca semua dokumen saat revisi manual.
- Tampilan di Microsoft Word belum dilihat manusia (render diukur di LibreOffice): HUMAN-VERDICT.
- STYLE-v23 §3.5 dan §3.7 diperbarui: label per kalimat untuk butir campuran, dan tidak boleh menambah pemutus yang tidak disebut versi asal.
