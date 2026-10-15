# Laporan Run Dokumen ISO SINUX (COS), 15 Oktober 2026

Receipt: ledger.json, config/checklist.json (checklist live, modifiedTime 2026-10-14T17:47:13Z, 87 baris; worklist 88 butir), qa/, reports/w8/ di repo sinux-iso-docs, diukur 15 Oktober 2026 pukul 01.10 sampai 01.20 UTC. Total 1.053 kalimat atau baris berlabel (USULAN) di 70 dokumen.

## Ringkasan

- 70 dokumen target selesai berstatus DONE (Draft Rev00): 44 perbaikan dokumen tim (T1), 23 dokumen baru (T2), 3 baris HOLD yang dipromosikan karena berkas tim terbaca (W7b). Nol dokumen tertahan di gerbang mutu dan nol dokumen terblokir.
- 16 baris HOLD menunggu berkas tim (T3). 2 baris SKIP: Statement of Applicability (lane konsultan, tidak disentuh) dan cetakan SOP.
- 68 dari 70 dokumen lolos pemeriksaan isi independen terhadap sumber dan kriteria checklist. Dua form W5 di luar sampel (SNX-OPS-FRM-03, SNX-ISMS-REG-01) hanya lolos gerbang mesin; SNX-OPS-FRM-03 juga lolos cek PDF.
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
| Legal | 252 | Legal 236 |
| Aziz (HR Manager) | 210 | Human Resource 202 |
| Owner | 202 | Marketing 76, Commercial 67 |
| Fani (VP Tech Operation and Services) | 181 | ISMS 72, Operation 71 |
| FAT | 95 | FAT 90 |
| Samuel (Direktur Utama) | 50 | Human Resource 38 |
| Konsultan (acuan klausul ISO) | 41 | tersebar |
| Laras (VP Commercial) dan lainnya | 22 | Marketing |

Keputusan lintas dokumen yang membuka paling banyak USULAN sekaligus:

| No | Keputusan | Dokumen terdampak | Pemutus |
|---|---|---|---|
| 1 | Ukuran tingkatan jabatan (saat ini jumlah garis lapor sampai Direktur Utama, karena Job Analysis tanpa grading) | SNX-HR-SOP-10 sampai 13, SNX-HR-FRM-01, SNX-HR-FRM-02 | Aziz, owner |
| 2 | Atasan langsung JA-03, JA-05, JA-08, JA-10, JA-11, JA-14 (garis lapor menunggu konfirmasi) | SNX-HR-ORG-01 dan semua dokumen yang memakai garis lapor | Aziz, owner |
| 3 | Authority Matrix (DoA) belum terbit: pejabat penyetuju dan batas nilai | SNX-HR-JA-01, SNX-LEG-FRM-01, SNX-LEG-FRM-02, SNX-FAT-FRM-01, SNX-COM-SOP-02 | Samuel |
| 4 | Pemetaan peran Finance Lead dan Finance Staff ke jabatan JA-10 dan JA-11 | semua dokumen FAT | owner, FAT |
| 5 | Pemetaan Line Manager Legal dan Staff Legal ke JA-08 dan JA-09 | semua dokumen Legal | Aziz, Legal |
| 6 | Masa simpan dan lokasi rekaman yang belum ditetapkan sumber | hampir semua form dan register | Legal, FAT |
| 7 | Tarif PPN 12 persen dan rumus Gov/SOE (WAPU) di register piutang | SNX-FAT-REG-01, SNX-FAT-SOP-05 | FAT |
| 8 | Cakupan register Marketing: Description checklist baris 58 memuat isi baris 57 ditambah validasi klaim, sedangkan judulnya Campaign & Activity Register | SNX-MKT-REG-01, SNX-MKT-REG-02, SNX-MKT-REG-03, SNX-MKT-RPT-01 | owner |
| 9 | Process Owner dokumen Commercial baru: Direktur (aturan default dokumen tanpa sumber) lawan VP Commercial (SOP Commercial dari tim) | SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01 | owner |
| 10 | Susunan Divisi Operation (NOC, SOC, SD dan PM) yang masih berstatus usulan | SNX-HR-ORG-01, SOP HR mutasi dan rotasi, dokumen Operation | owner, Fani |
| 11 | Acuan klausul ISO per dokumen yang tidak diberi checklist | 41 kalimat berlabel "perlu konfirmasi konsultan" | konsultan |

## Open items

Tiap dokumen mencatat open item di bagian notes masing-masing (folder notes/ di repo). Ringkasan: 985 butir, terbanyak untuk Fani (316), owner (266), Legal (151), Aziz (112). Rincian per pemutus untuk tinjauan internal: reports/USULAN-OPEN-per-pemutus.md.

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

## Gerbang mutu yang diukur

| Klaim | Cara ukur | Bukti | Hasil |
|---|---|---|---|
| Frasa meta proses penyusunan nol di seluruh out/ | pola (dokumen sumber, sumber tim, di sumber, draf ini, belum berdokumen, penyusun bukan nama peran) pada 70 berkas, kontrol positif pada versi lama SNX-LEG-SOP-02 | reports/w8/metascan.txt | 0 temuan; kontrol positif menembak |
| Rujukan silang ke butir SOP lain ada | 177 rujukan "SNX-... butir/bagian N.M" dicek terhadap jumlah butir dokumen tujuan | reports/w8/refcheck.txt | 0 rujukan rusak |
| Tidak ada halaman kosong | render PDF tiap docx, teks per halaman | reports/w8/blankscan.txt | 53 docx, 0 halaman kosong |
| Format sama dengan acuan | renderer terkunci (sidik format), pemeriksa PDF pada 12 dokumen | tools/selftest.sh, qa/*.pdfcheck.json | selftest 6 OK; 12 PASS |
| Lint dan validasi OOXML | lint_doc dan validator OOXML tiap render | qa/*.lint.json, ledger.json | semua lulus |

## Residu mutu (belum diselesaikan, dicatat apa adanya)

Temuan tidak memblokir dari pemeriksa yang belum diubah, per dokumen:

| Dokumen | Residu |
|---|---|
| SNX-HR-SOP-11 | istilah mutasi bentrok dengan butir 4.9; satu kalimat pasif baru; penerima tanggapan di bagian 9 belum jelas; "berkas usulan" belum didefinisikan; NOC, SOC, SD dan PM tanpa definisi |
| SNX-HR-SOP-13 | aturan Direktur Utama di bagian 9 bertentangan dengan butir 4.3; label (USULAN) bergeser di bagian 9; NOC dan SOC disebut divisi, sedangkan SNX-HR-SOP-12 menyebut sub divisi dalam unit Operation |
| SNX-COM-SOP-02 | pengganti istilah "Personel Commercial" mempersempit cakupan bagian 9 dan Kesimpulan |
| SNX-MKT-RPT-01 | arti Aktivitas belum sama dengan SNX-MKT-REG-02; status "belum Selesai" ikut mencakup Dibatalkan |
| SNX-MKT-REG-01 | penurunan klasifikasi dicatat di bukti persetujuan, sedangkan SNX-ISMS-PRO-01 mencatatnya di SNX-ISMS-REG-01 |
| SNX-MKT-REG-02 | irisan kolom dengan SNX-MKT-REG-01 dan irisan daftar aktivitas dengan SNX-MKT-RPT-01 belum dihapus (struktur form dikunci); menunggu keputusan cakupan owner |

Temuan tidak memblokir lain per dokumen tersimpan di qa/<KODE>.verify.json dan qa/<KODE>.sweep.json.

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

Nol mutasi Google Drive, nol tulisan ke kanon KB, nol tanda tangan atau tanggal efektif, nol kredensial di keluaran. Ringkasan run ini dikirim ke antrean tinjauan admin pada 15 Okt 01.22 UTC (status PENDING, menunggu tinjauan owner).

## Cara unduh dan unggah

1. Unduh: repo sinux-iso-docs di GitHub, tombol Code, Download ZIP. Dokumen ada di folder out/ per departemen; ringkasan di out/00_Index.
2. Tinjau: buka Master_List_COS.xlsx, filter sheet USULAN per pemutus; buka dokumen terkait dan putuskan tiap label (USULAN).
3. Unggah sesudah tinjauan: buat folder baru "COS Draft ISO" di Supporting Documents pada Shared Drive ISO SINUX, unggah isi out/ apa adanya. Berkas tim yang sudah ada tidak ditimpa.
4. Pengesahan: isi tanda tangan dan tanggal efektif di blok Approval tiap dokumen sesudah semua USULAN diputus; ubah status Draft menjadi status sah lewat penyetuju.
