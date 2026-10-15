# Temuan LEAD ISO-B: pemeriksaan makna buta atas jalur yang disunting sesudah PASS (GAP 2 REVIEW-W10)

Basis: bed1bb6 lawan 0a00bae, 335 pasangan (reports/w11/lead_gap2_pairs.json) dari notes bagian "W10 audit pointer", "W10 audit cakupan label", dan "W10 koreksi worker" di 39 dokumen. Dua pemeriksa buta Opus, baca-saja, 15 Okt 10.00 sampai 11.40 UTC. Kriteria FAIL: (1) makna atau cakupan berubah, (2) cakupan label USULAN bergeser, (3) pelaku, angka, nama, kode, atau rujukan berubah tanpa pengganti setara, (4) rujukan yang dibutuhkan pembaca hilang.

## FAIL (11), wajib dikembalikan ke cakupan bed1bb6
| No | Dokumen | Path spec | Kriteria | Masalah |
|---|---|---|---|---|
| F1 | FAT-SOP-01 | .roles[2][2] | 1 | Final mengikat penerbitan e-Faktur pada persetujuan Finance Lead; butir 4.4 hanya untuk menerbitkan atau mengirim invoice, dan e-Faktur terbit (6.2) sebelum pemeriksaan Finance Lead (6.3) |
| F2 | FAT-SOP-01 | .roles[3][1] | 1 | Tugas memastikan keakuratan atribut invoice hilang |
| F3 | FAT-SOP-01 | .roles[1][1] | 3 | Fakta Project Manager belum punya pemegang (SNX-HR-ORG-01) hilang dari dokumen; kembalikan sebagai fakta singkat tanpa frasa pemetaan |
| F4 | COM-REG-01 | .sections[7].blocks[2].table.rows[0][1] | 2 | Label menutupi klasifikasi INTERNAL yang di butir 4.12 tidak berlabel |
| F5 | FAT-RPT-02 | .sections[4].blocks[2].p | 2 | Label menutupi aturan isi kolom Diminta kepada yang di bed1bb6 tidak berlabel |
| F6 | LEG-FRM-03 | .sections[2].blocks[0].p | 2 | Label kini juga menutupi aturan pengisian (Staff Legal, saat pemeriksaan) |
| F7 | LEG-REG-03 | .sections[8].blocks[0].p | 1 | Pemicu peninjauan melebar; syarat pemberitahuan dari Penanggung Jawab Kegiatan (Ketentuan 9) hilang |
| F8 | LEG-RPT-02 | .sections[7].blocks[1].table.rows[0][1] | 2 | Penetapan Pencatat kehilangan label (SNX-LEG-SOP-03 butir 4.26 seluruhnya USULAN) |
| F9 | MKT-REG-01 | .sections[5].blocks[0].p | 2 | Label baru menutupi aturan satu baris per versi per channel (4.1 kalimat pertama tidak berlabel) |
| F10 | MKT-REG-01 | .sections[5].blocks[6].p | 2 | Label baru menutupi kewajiban menulis lokasi file final (4.14 kalimat pertama tidak berlabel) |
| F11 | MKT-REG-01 | .sections[5].blocks[10].p | 2 | Label baru menutupi pencatatan tanggal persetujuan (label 4.6 hanya pada persetujuan lisan) |

## RAGU yang diputus LEAD
Dikembalikan ke cakupan bed1bb6 (sama dengan FAIL):
| No | Dokumen | Path spec | Putusan |
|---|---|---|---|
| R1 | ISMS-PLN-01 | .procedures[4].intro[0] | Kembalikan rujukan frekuensi uji ke bagian 8 (dibutuhkan pelaksana) |
| R2 | LEG-FRM-01 | .sections[2].blocks[4].p | Pisahkan lagi dua label seperti bed1bb6 |
| R3 | LEG-FRM-01 | .sections[4].blocks[4].p | Kembalikan rujukan jumlah pilihan ke Ketentuan butir 5 |
| R4 | LEG-FRM-01 | .sections[1].blocks[1].table.rows[10][1] | Kembalikan "ditunjuk Unit Kerja Pemohon" |
| R5 | LEG-FRM-01 | .sections[7].blocks[1].table.rows[0][1] | Kembalikan "menurut SNX-ISMS-PRO-01" |
| R6 | LEG-FRM-01 | .sections[7].blocks[1].table.rows[1][1] | Kembalikan dasar usulan (SNX-LEG-SOP-02 butir 4.19 dan SNX-LEG-SOP-03) |
| R7 | LEG-REG-01 | .sections[4].blocks[8].p | Kembalikan cakupan Ketentuan butir 11 |
| R8 | MKT-REG-01 | .sections[2].blocks[0].table.rows[11][1] | Kembalikan ikatan ke daftar Ruang Lingkup; contoh boleh tetap |
| R9 | OPS-SOP-05 | .procedures[1].intro[0] | Label hanya pada nilai batas waktu SOC, bukan pada penugasan Lead SOC |
| R10 | COM-FRM-02 | .sections[4].blocks[1].table.rows[4][1] | Label hanya pada struktur kolom, bukan tugas COO |
| R11 | COM-REG-01 | .sections[5].blocks[10].p | Penetapan Selesai oleh VP Commercial di luar label, seperti butir 4.7 |
| R12 | FAT-FRM-01 | .sections[8].blocks[0].table.rows[4][1] | Langkah 6.3.2 hanya untuk persetujuan utang pajak |
| R13 | FAT-SOP-05 | .policy[5] | Label hanya untuk pelaku: "(USULAN: Finance Lead sebagai pelaku)" |
| R14 | HR-SOP-13 | .policy[0] | Kembalikan "hanya karena kebutuhan organisasi" |
Diterima apa adanya (gaya, fakta tetap ada di dokumen): pemetaan jabatan "Jabatan: Legal & Compliance (JA-0x)" di tabel Peran LEG-FRM-01, LEG-REG-01, LEG-RPT-02.
