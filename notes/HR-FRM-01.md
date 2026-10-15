# Catatan penyusun HR-FRM-01: Employee Competency Matrix

Status: DRAFTED (spec + notes ada). Spec: specs/HR-FRM-01.json. Mode generic, aksi T2 tanpa sumber, nomor SNX-HR-FRM-01 (nomor SNX lama dipertahankan), department Human Resources, classification RESTRICTED (Internal), audit_class None, wave W7. Approval persis dari config/defaults.json: prepared Sita Nadia Salsabila Widodo / HRGA Officer, reviewed Aziz Priyo Widakdo / HR Manager, approved Samuel Kristanto Utomo / President Director. process_owner "HR Manager" (jabatan, tanpa nama): dokumen tanpa sumber memakai jabatan reviewer departemen (config/defaults.json, process_owner.rule, status USULAN).

Hasil uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-FRM-01.json /tmp/pen-HR-FRM-01/HR-FRM-01.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-HR-FRM-01/HR-FRM-01.docx generic` = "pass": true, fails kosong, satu warn (12 label (USULAN) menunggu ACC). Validator OOXML skill docx (dijalankan dari foldernya): "All validations PASSED!". tools/selftest.sh: 6 baris OK (putaran awal). PDF hasil soffice 10 halaman, tiap halaman berisi teks badan (cacat tata letak putaran 1: baris Rekaman dan JA-08 pecah halaman, diperbaiki lewat lebar kolom). Tidak ada berkas tools, template, config, atau control yang saya ubah. Putaran perbaikan 1 (orkestrator, verifikator PASS dengan 7 temuan nonblocking, qa/HR-FRM-01.verify.r1.json dan qa/HR-FRM-01.pdfcheck.json): semua tujuh butir dikerjakan, lihat bagian Penanganan putaran 1.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Tidak ada sumber tim untuk baris ini (config/worklist.json: "sources": []; aksi T2) | tidak ada | tidak ada | Alat Drive tidak dimuat dan tidak dipakai. Tidak ada berkas sumber yang gagal dibaca |
| Kriteria penerimaan: config/checklist.json baris 9, Description | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist) | 2026-10-14T17:47:13.611Z (kolom modifiedTime di config/checklist.json) | Dibaca langsung dari berkas repo. Baris 9 tanpa fileId, tanpa acuan klausul ISO, link_text "On progres" |
| Bahan sesama dokumen (bukan sumber faktual form ini) | specs/HR-ORG-01.json, specs/HR-JA-01.json, specs/HR-SOP-10.json, specs/HR-SOP-12.json | spec lokal, bukan berkas Drive | Dipakai untuk nama jabatan (Tabel 1), butir yang dirujuk, dan konsistensi rujukan silang |
| Bahan asal HR-JA-001 (DATA) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z, angka ini saya salin dari notes/HR-JA-01.md dan tidak saya ukur ulang | Dibaca lewat salinan context/audit/iso-sinux-supdocs-hr-2026-10-14.md |
| Catatan cacat | context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 717 dan bagian 5 di context/audit/iso-sinux-supdocs-hr-2026-10-14.md | salinan audit 13 sampai 14 Okt | DATA. Lihat bagian Penanganan cacat |

Kalimat perintah di bahan yang saya baca: tidak ada yang ditemukan.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria penerimaan: matriks standar keterampilan, pengetahuan, dan perilaku per tingkatan jabatan. Tabel 2 memakai tiga kolom itu dan satu baris per tingkatan | "Matriks pemetaan standar keterampilan, pengetahuan, dan perilaku yang wajib dimiliki karyawan pada setiap tingkatan jabatan." | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Sertifikasi profesi atau vendor hanya wajib bila ditetapkan di Competency Matrix atau diminta kontrak pelanggan, dan masa pengalaman minimum menunggu job evaluation. Karena itu Tabel 1 punya kolom sertifikasi dan Dasar sertifikasi, dan masa pengalaman dikecualikan | "sertifikasi profesi/vendor hanya diwajibkan bila ditetapkan dalam competency matrix atau kebutuhan kontrak pelanggan. Masa pengalaman minimum ditentukan setelah job evaluation." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Job Analysis tidak memuat grading dan hanya mencakup 15 jabatan aktif. Karena itu tingkatan jabatan tidak diambil dari sumber, kolom Tingkatan dikosongkan, dan Tabel 1 memuat 15 baris JA-01 sampai JA-15 | "Cakupan \| 15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Fakta penting lain dan kutipan verbatim

| # | Fakta di form | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | Form ini dibaca sebagai Competency Matrix di JA-01 dan dirujuk SOP-10 dan SOP-12 | "Employee Competency Matrix. Dibaca sebagai Competency Matrix di butir 4.7 (USULAN)." | specs/HR-JA-01.json, Dokumen Terkait |
| 2 | Ukuran tingkatan jabatan sementara (butir 4.3) | "Jenjang sebuah jabatan di SNX-HR-ORG-01, dihitung dari jumlah garis lapor sampai Direktur Utama (JA-01). Dua jabatan satu tingkatan bila jumlah garis lapornya sama. SNX-HR-JA-01 tidak memuat grading, sehingga ukuran ini (USULAN)." | specs/HR-SOP-12.json, tabel Definisi (bagian 3), istilah Tingkatan jabatan |
| 3 | SOP-12 memakai tingkatan dari form ini bila sudah disahkan | "Bila SNX-HR-FRM-01 sudah disahkan dan menetapkan tingkatan jabatan, HR Manager memakai tingkatan itu (USULAN)." | specs/HR-SOP-12.json, butir 4.2 |
| 4 | SOP-10 memakai form ini sebagai acuan tambahan | "Bila SNX-HR-FRM-01 sudah disahkan, HR Manager memakainya sebagai acuan tambahan (USULAN)." | specs/HR-SOP-10.json |
| 5 | Kompetensi teknis mencakup keterampilan dan pengetahuan; kompetensi perilaku = perilaku (butir 4.1) | "Pengetahuan dan keterampilan teknis yang dibutuhkan jabatan (hard skills)." dan "Sikap dan kemampuan kerja bersama yang dibutuhkan jabatan (soft skills)." | specs/HR-JA-01.json, tabel Definisi |
| 6 | KPI per jabatan ada di KPI Matrix (pengecualian) | "Indikator kinerja di dokumen ini adalah usulan indikator. Target numerik, bobot, dan sumber data ditetapkan di KPI Matrix." | specs/HR-JA-01.json, butir 4.6 |
| 7 | Daftar jabatan, kode, dan nama di Tabel 1 | Tabel Daftar Jabatan, kolom Kode dan Jabatan, JA-01 sampai JA-15 (nama disalin persis, termasuk JA-08 dan JA-09 yang sama-sama "Legal & Compliance") | specs/HR-ORG-01.json |
| 8 | Delapan jabatan Divisi Operation dikecualikan dari Tabel 1 | "Nama jabatan, jenjang, headcount, dan garis lapor ke COO berstatus USULAN di POL-OPS-001, tanpa pemegang bernama." | specs/HR-ORG-01.json, butir K-10 |
| 9 | Klasifikasi RESTRICTED (Internal) | config/defaults.json: "data karyawan, hukum, keuangan, pelanggan = RESTRICTED (Internal)"; config/worklist.json: "classification": "RESTRICTED (Internal)" | defaults v21, worklist (bukan berkas Drive) |
| 10 | Sebutan "Direktur Utama" di badan dokumen; "COO" tidak dipakai | config/defaults.json data_conflicts: "badan dokumen: 'Direktur Utama' (HR-JA-001), termasuk saat sumber menulis CEO" | defaults v21 |
| 11 | Pembeda JA-08 dan JA-09 di Tabel 1 | "JA-08 dan JA-09 memakai nama jabatan yang sama. Pembedanya garis lapor: JA-09 melapor ke JA-08." | specs/HR-ORG-01.json, paragraf di bawah Daftar Jabatan |
| 12 | Pola rekaman HR: lokasi folder Google Drive Departemen HR, pemilik, retensi berlabel USULAN | "Personal file karyawan di folder Google Drive Departemen HR (USULAN). Pemilik: HRGA Officer." dan "Selama karyawan bekerja di SINUX (USULAN)" | specs/HR-SOP-10.json dan specs/HR-SOP-12.json, tabel rekaman. Retensi tidak ditiru karena bukan untuk form ini |

## 3. Pemetaan klausul ISO

Checklist tidak memberi acuan klausul untuk baris ini. Bagian Acuan Klausul ISO memuat tiga baris dengan satu label "(USULAN, perlu konfirmasi konsultan)". Judul klausul adalah pengetahuan standar, bukan teks sumber tim.

| Klausul | Alasan | Catatan |
|---|---|---|
| ISO 9001:2015 7.2 Kompetensi | Form menetapkan kompetensi yang diperlukan (butir a klausul). Penilaian aktual, tindakan memperoleh kompetensi, dan bukti kompetensi karyawan tidak ada di form, dan kalimat tabel menyebutnya agar form tidak terbaca menutup klausul penuh | JA-001 memakai 7.2 untuk kompetensi (context/audit hr, Ringkasan) |
| ISO/IEC 27001:2022 7.2 Kompetensi | Klausul yang sama untuk ISMS | Tafsir penyusun |
| ISO/IEC 27001:2022 Annex A 6.3 Kesadaran, pendidikan, dan pelatihan keamanan informasi | Kolom Pengetahuan dan Perilaku dapat memuat standar keamanan informasi | Tafsir penyusun. Context/audit sintesis (Council 2, butir 6) menulis "bukti A 6.1/7.2 di matriks kompetensi + NDA" tanpa judul klausul. Saya memetakan 7.2 dan A 6.3. A 6.1 (Screening, edisi 2022) tidak saya ambil karena form ini tidak memuat tahap seleksi. Konsultan perlu menilai |

## 4. Keputusan desain dan tafsir

1. Dua tabel, bukan satu. Tabel 1 per jabatan (15 baris dari SNX-HR-ORG-01) memuat Tingkatan dan sertifikasi, sesuai butir 4.7 JA-001 dan permintaan SOP-12 butir 4.2 agar form ini menetapkan tingkatan. Tabel 2 per tingkatan memuat tiga kolom kompetensi sesuai kriteria "pada setiap tingkatan jabatan". Satu tabel 15 baris dengan semua kolom terlalu lebar untuk halaman potret 16 cm.
2. Semua sel faktual kosong: Tingkatan, sertifikasi, Dasar sertifikasi, dan seluruh Tabel 2. Tanpa baris contoh. Nama jabatan dan kode di Tabel 1 bukan data faktual baru: disalin dari SNX-HR-ORG-01 (DONE). Nama pemegang jabatan tidak dimasukkan.
3. Enam baris kosong di Tabel 2 adalah kapasitas tata letak, bukan klaim jumlah tingkatan. Teks di bawah judul Tabel 2 memberi izin menambah baris.
4. Tiga kolom kompetensi memetakan ke Job Analysis: keterampilan dan pengetahuan = kompetensi teknis, perilaku = kompetensi perilaku (butir 4.1, dari definisi di JA-01).
5. Ukuran tingkatan (butir 4.3) disamakan dengan SOP-12 agar dua dokumen tidak bertentangan. Tingkatan jabatan yang garis lapornya masih menunggu konfirmasi di SNX-HR-ORG-01 (K-01 sampai K-04) diberi keterangan, bukan ditebak.
6. Peran: HR Manager menetapkan, HRGA Officer mencatat, Direktur Utama menyetujui. Nama peran persis seperti di daftar jabatan HR-ORG-01 (HR Manager JA-14, HRGA Officer JA-12, Direktur Utama JA-01). Pembagian ini turunan dari blok Prepared By, Reviewed By, dan Approved By, bukan dari sumber, jadi berlabel USULAN.
7. Skala penguasaan 1 sampai 4 ditambahkan karena kata "standar" pada kriteria perlu ukuran. Seluruh skala berlabel USULAN.
8. Bagian 3 hanya arti istilah. Aturan ada di Dasar dan Ketentuan (butir 4.1 sampai 4.6). Rujukan ke SOP-12 bagian 3 disebut sekali di butir 4.3 dan sekali di tabel Dokumen Terkait sebagai penunjuk, tanpa menyalin kalimat definisinya.
9. Sebutan COO tidak muncul di badan dokumen, jadi aturan "Direktur (COO)" tidak terpakai. JA-02 ditulis "Direktur" seperti di HR-ORG-01. Samuel ditulis "Direktur Utama" di badan dokumen dan "President Director" hanya di blok Approved By.
10. Zammad, GLPI, vault, PPN: tidak relevan untuk form ini dan tidak disebut.
11. Setiap kode dokumen di badan ada di tabel Dokumen Terkait: SNX-HR-ORG-01, SNX-HR-JA-01, SNX-HR-SOP-10, SNX-HR-SOP-12, SNX-HR-FRM-02, SNX-ISMS-PRO-01, dan KPI Matrix (belum bernomor, seperti di HR-ORG-01). Kode JA-nn dan K-10 adalah penomoran butir di dokumen lain, bukan kode dokumen.
12. Status SNX-HR-FRM-02 tidak ditulis "belum ada" atau "dalam pengerjaan": hanya judul dan fungsinya. Rujukan yang sama dipakai SOP-10 dan SOP-12 dengan "dalam pengerjaan"; kecocokan cek setelah FRM-02 jadi (open item 8).
13. Putaran 1: Tujuan ditulis ulang dengan dua kalimat biasa. Label "Hasil yang dijaga" dan klaim pemakaian oleh auditor dihapus karena tanpa sumber.
14. Putaran 1: definisi Tingkatan jabatan tidak lagi memakai "jenjang" dan "sejenjang". Rumusan baru: kelompok jabatan di SNX-HR-ORG-01 yang kedudukannya sama dalam susunan organisasi, dengan penunjuk ke butir 4.3. Ukuran jumlah garis lapor tetap hanya di butir 4.3.
15. Putaran 1: kolom Jabatan JA-08 dan JA-09 diberi pembeda dari HR-ORG-01 (JA-09 melapor ke JA-08). Nama Finance, Accounting & Tax, dan Brand & Marketing tidak diubah karena sama persis dengan Daftar Jabatan HR-ORG-01 (JA-10, JA-11, JA-06).
16. Putaran 1: bagian Rekaman ditambahkan (rekaman, lokasi dan pemilik, retensi). Lokasi mengikuti pola SNX-HR-SOP-10 dan SNX-HR-SOP-12 dan berlabel USULAN. Pemilik HR Manager adalah process_owner. Retensi ditulis "Belum ditetapkan" karena tidak ada sumber.

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Tingkatan ditentukan dari jumlah garis lapor sampai Direktur Utama (JA-01), sama dengan SOP-12 | Butir 4.3 | Aziz |
| U2 | Standar Tabel 2 berlaku sebagai batas bawah, kompetensi khusus jabatan tetap mengikuti SNX-HR-JA-01 | Butir 4.4 | Aziz |
| U3 | Pembagian tugas HR Lead (menetapkan dan memeriksa), HRGA Officer (mencatat), Direktur Utama (menyetujui) | Bagian Peran dan Cara Mengisi | Aziz; Samuel untuk peran penyetuju; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U4 | Skala penguasaan 1 sampai 4 (Dasar, Mandiri, Mahir, Ahli) beserta artinya | Bagian Skala Penguasaan | Aziz |
| U5 | SNX-HR-SOP-10 memakai form ini sebagai acuan tambahan penilaian kualifikasi | Dokumen Terkait | Aziz |
| U6 | SNX-HR-SOP-12 memakai tingkatan jabatan dari form ini pada butir 4.2 | Dokumen Terkait | Aziz |
| U7 | Peninjauan lebih awal bila SNX-HR-ORG-01 atau SNX-HR-JA-01 berubah (peninjauan tahunan sendiri dari review_period YEARLY) | Kesimpulan | Aziz |
| U8 | Klausul ISO 9001:2015 7.2, ISO/IEC 27001:2022 7.2, dan Annex A 6.3 | Acuan Klausul ISO | Legal bersama konsultan (konsultan memutus; Legal mencatat) |
| U9 | Kompetensi perilaku di SNX-HR-JA-01 sama dengan perilaku di form ini (kompetensi teknis = keterampilan dan pengetahuan) | Butir 4.1 | Aziz |
| U10 | Form ini dibaca sebagai Competency Matrix yang dirujuk SNX-HR-JA-01 butir 4.7 (label sama dengan JA-01) | Butir 4.5 dan Dokumen Terkait | Aziz |
| U11 | Lokasi rekaman: folder Google Drive Departemen HR; pemilik HR Lead | Bagian Rekaman | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |

Jumlah USULAN: 11 butir (label "(USULAN)" tercetak 12 kali karena U10 muncul di dua tempat, tidak termasuk istilah "(USULAN)" di tabel Definisi dan label "(USULAN, perlu konfirmasi konsultan)" milik U8). Tidak ada angka bisnis tanpa sumber selain skala 1 sampai 4 (U4) dan jumlah baris kosong (keputusan 3). Retensi tidak diisi.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Dasar tingkatan jabatan belum diputus. Garis lapor JA-03, JA-05, JA-08, JA-10, JA-11, dan JA-14 masih menunggu konfirmasi di SNX-HR-ORG-01 (K-01 sampai K-04), sehingga tingkatannya ikut tidak pasti | Aziz, lalu owner untuk garis lapor; diubah W9: JA-03 dan JA-04 kini dua garis tegas ke Direktur dan Direktur Utama (LEAD G-3 A3), tidak menunggu; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu (A4) |
| 2 | Isi Tabel 1 (Tingkatan, sertifikasi, Dasar sertifikasi) dan Tabel 2 kosong dan menunggu keputusan HR Lead. Tidak ada sumber yang menyebut standar per tingkatan | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| 3 | Tempat mencatat hasil penilaian kompetensi aktual karyawan dan bukti kompetensi (ISO 9001:2015 7.2 butir b dan d) tidak ditetapkan di form ini. Checklist memuat baris SOP Performance Appraisal berstatus T3 HOLD dan Employee Personnel File Checklist; belum jelas yang mana | Aziz |
| 4 | Retensi rekaman form ini tertulis "Belum ditetapkan" karena tidak ada sumber, dan lokasi (folder Google Drive Departemen HR) berlabel USULAN mengikuti SNX-HR-SOP-10 dan SNX-HR-SOP-12. Angka retensi dilarang tanpa sumber | Legal untuk retensi; Aziz untuk lokasi dan pemilik |
| 5 | Delapan jabatan Divisi Operation masih USULAN tanpa pemegang (HR-ORG-01 K-10) dan dikecualikan dari Tabel 1. Baris ditambah sesudah jabatan disahkan | Owner |
| 6 | Job evaluation dan masa pengalaman minimum (JA-001 butir 4.7) belum ada tanggal. Form ini tidak memuatnya | Aziz |
| 7 | Sertifikasi profesi atau vendor yang wajib per jabatan dan kontrak pelanggan yang mewajibkannya tidak ada sumber | Aziz bersama Fani untuk jabatan Operation |
| 8 | Rujukan SNX-HR-SOP-10, SNX-HR-SOP-12, dan SNX-HR-FRM-02 cocok dengan isi spec saat ini; periksa ulang setelah FRM-02 jadi (W7) dan bila SOP-10 atau SOP-12 diubah | LEAD |
| 9 | Jumlah baris Tabel 2 (6) menyesuaikan jumlah tingkatan yang diputus | Aziz |
| 10 | data_conflicts yang konfirmasinya belum selesai dan relevan untuk form ini: jabatan Aziz "HR Manager" (konfirmasi: owner atau Aziz) dan ejaan "Samuel Kristanto Utomo" (konfirmasi: owner atau Samuel). Dipakai sesuai kolom "pakai", tidak dipilih ulang | Owner; ditutup W9: jabatan Aziz HR Lead dan ejaan Kristanto berstatus selesai (defaults v22) |
| 11 | Context/audit sintesis baris 446 menyebut "satu matriks kompetensi dan rekam pelatihan/awareness". Form ini hanya matriks standar; rekaman pelatihan dan awareness tidak dimasukkan | Aziz |
| 12 | process_owner "HR Manager" mengikuti aturan dokumen tanpa sumber (jabatan reviewer departemen), status USULAN di defaults | Aziz; ditutup W9: process_owner kini HR Lead (defaults v22) |
| 13 | Sejak JA-03 dan JA-04 punya dua garis tegas (LEAD G-3 A3), ukuran tingkatan "jumlah garis lapor sampai Direktur Utama (JA-01)" (butir 4.3, USULAN) bermakna ganda untuk JA-03, JA-04, dan bawahannya: satu garis lewat Direktur dan satu garis langsung ke Direktur Utama. Teks dokumen tidak diubah | Aziz dan owner (R2) |

## Penanganan cacat context/audit

Perintah: `grep -n "Employee Competency Matrix" context/audit/*.md`. Hasil: satu baris, context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md:717 ("8. Employee Competency Matrix."), butir dalam daftar HR. Tidak ada bagian dokumen sendiri dan tidak ada "Catatan kualitas dan celah" untuk baris ini. Saya membaca bagian 5 pada dokumen HR terkait (HR-JA-001, baris 1232 sampai 1250) dan sintesis baris 446 dan 521.

| Cacat | Relevansi | Penanganan |
|---|---|---|
| HR bagian 5 butir 13: sertifikasi hanya bila ditetapkan competency matrix; masa pengalaman minimum belum ada | Langsung | Kolom sertifikasi dan Dasar sertifikasi di Tabel 1 (butir 4.5). Masa pengalaman dikecualikan di Ruang Lingkup. Open item 6 dan 7 |
| HR bagian 5 butir 2: tidak ada grade dan grading tidak dicantumkan | Langsung | Tingkatan tidak diambil dari sumber; butir 4.3 memakai ukuran sementara yang sama dengan SOP-12 (U1); sel Tingkatan kosong. Open item 1 |
| HR bagian 5 butir 4: frasa kompetensi janggal ("Risk pemahaman karyawan", "pelanggan communication", dan seterusnya) | Tidak langsung | Form tidak menyalin satu pun nama kompetensi. Pemulihan frasa sudah dikerjakan di specs/HR-JA-01.json (notes/HR-JA-01.md, butir 4, USULAN U7 di sana). Butir 7.6 meminta HRGA Officer mengambil kompetensi dari SNX-HR-JA-01 |
| HR bagian 5 butir 11: ejaan Samuel dan sebutan CEO | Ya | "Samuel Kristanto Utomo" di blok Approved By dan "Direktur Utama" di badan, sesuai defaults |
| HR bagian 5 butir 5, 6, 7, 8, 9: garis lapor dan nama unit tidak seragam | Tidak langsung | Bukan isi form ini. Garis lapor ada di SNX-HR-ORG-01, dan butir 4.3 memberi keterangan menunggu konfirmasi |
| HR bagian 5 butir 1, 3, 10, 12, 14, 15 | Tidak relevan | Butir 1: status dokumen JA-001; 3: kalimat terpotong JA-001; 10: Finance Lead dan Finance Staff tidak muncul di form ini; 12: teks identik antar jabatan; 14: jumlah tabel; 15: klausul 7.3 dan 7.5 JA-001 |
| Sintesis Council 2 butir 6: "bukti A 6.1/7.2 di matriks kompetensi" | Ya | Dipetakan ke 7.2 dan A 6.3, dengan alasan di bagian 3 |

## Penanganan putaran 1

| # | Permintaan orkestrator | Perubahan di spec |
|---|---|---|
| 1 | Tujuan: hapus "Hasil yang dijaga" dan klaim auditor | Tujuan kini dua kalimat: isi form (standar untuk pemegang jabatan per tingkatan) dan pencatatan sertifikasi menurut penetapan HR Manager atau persyaratan kontrak pelanggan |
| 2 | Pasif tanpa pelaku di 4.3, 4.5, teks di bawah Tabel 2 | 4.3: HR Manager menetapkan tingkatan, HRGA Officer menulis keterangan menunggu konfirmasi. 4.5: HR Manager menetapkan sertifikasi wajib, HRGA Officer menulis dasarnya. Teks Tabel 2: HRGA Officer menambah baris |
| 3 | Benda sebagai pelaku di Tujuan dan 4.2 | Tujuan tidak lagi memuat "jabatan mewajibkan". 4.2: HR Manager menetapkan satu tingkatan, pemegang jabatan wajib memiliki kompetensi yang sama menurut Tabel 2 |
| 4 | Satu istilah | Tujuan memakai "pemegang jabatan". Baris pengecualian dan baris ISO 7.2 juga memakai "pemegang jabatan" agar sama. Definisi Tingkatan jabatan tanpa "jenjang" |
| 5 | Parafrase JA-01 butir 4.7 lengkap dan label USULAN | Butir 4.5 dan baris SNX-HR-JA-01 di Dokumen Terkait memuat dua alternatif (ditetapkan di Competency Matrix atau kontrak pelanggan memuat persyaratannya) dan label USULAN pada pembacaan form ini sebagai Competency Matrix. Butir 4.1 diberi label USULAN pada pemetaan kompetensi perilaku |
| 6 | Tabel rekaman | Bagian Rekaman baru, satu baris: form yang disahkan, folder Google Drive Departemen HR (USULAN), pemilik HR Manager, retensi "Belum ditetapkan" |
| 7 | JA-08 dan JA-09 | JA-08 "Legal & Compliance (tempat JA-09 melapor)" dan JA-09 "Legal & Compliance (melapor ke JA-08)" |

Temuan pdfcheck yang saya kerjakan tanpa mengubah isi: lebar kolom Tabel 1 diubah supaya baris JA-08 dan JA-09 tidak memanjang, sehingga baris Rekaman tidak lagi pecah antarhalaman. Temuan pdfcheck lain (baris JA-04 pecah, header Tabel 1 tidak berulang, rata kiri-kanan sel) berasal dari renderer dan tidak saya ubah.

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Benda memakai kata kerja manusia: "Form ini menetapkan", "kontrak pelanggan memintanya", "SNX-HR-JA-01 menyerahkan", "Butir 4.7 menyatakan", "Form ini membaca jabatan", "Tabel 2 menetapkan kompetensi". Semua saya tulis ulang menjadi isi ("Form ini memuat ...", "Tabel 2 memuat ...", "Menurut butir 4.7 ..."), atau pelakunya diganti peran HR Manager, HRGA Officer, atau Direktur Utama.
- Definisi Pengetahuan memuat daftar tiga ("prosedur, kebijakan, dan sistem kerja"). Terdengar seperti tiga yang dipaksakan. Saya potong menjadi dua contoh.
- Tujuan: "tiga kelompok kompetensi" pada Ruang Lingkup adalah tiga dari kriteria checklist, bukan tiga yang dipaksakan. Saya biarkan.
- Langkah 7.1 sampai 7.9 hampir semuanya diawali "HRGA Officer". Terbaca seragam, tetapi tiap langkah satu tindakan dan satu pelaku, sesuai RUNBOOK §6a.2. Saya biarkan.
- Arti skala 1 sampai 4 dan definisi Keterampilan serta Perilaku bisa ditempel ke perusahaan mana pun. Ini sifat skala dan definisi. Saya beri label USULAN pada skala dan tidak menambah kalimat penjelas.
- Putaran 1: Tujuan memakai label "Hasil yang dijaga" dari panduan gaya dan klaim pemakaian oleh auditor. Terbaca mekanis dan tanpa sumber, jadi saya tulis ulang menjadi dua kalimat biasa. Butir 4.3, 4.5, dan teks di bawah Tabel 2 sempat pasif tanpa pelaku, kini menyebut HR Manager atau HRGA Officer. Butir 4.2 dan Tujuan sempat memberi kata kerja pada jabatan ("jabatan yang mewajibkan", "jabatan memakai standar"), kini pelakunya HR Manager atau pemegang jabatan. "karyawan" dan "jenjang" sempat dipakai berganti dengan "pemegang jabatan" dan "tingkatan"; kini satu istilah.
- Tidak ada pembuka generik, penutup positif, em-dash, en-dash, tebal, tanda kutip penekanan, "tidak hanya ... tetapi juga", atau frasa pengisi. Kesimpulan dua kalimat, tanpa pujian. Lint gaya lulus.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: 15 jabatan, JA-01 sampai JA-15, dan delapan jabatan Divisi Operation dari specs/HR-ORG-01.json. Skala 1 sampai 4 (U4) dan enam baris kosong Tabel 2 (keputusan 3) tidak bersumber: yang pertama berlabel USULAN, yang kedua kapasitas tata letak. Tidak ada tanggal di dokumen.
- Nama dan jabatan: tiga nama di blok approval dari config/defaults.json. Badan dokumen hanya memuat jabatan, tidak ada nama orang. Nama jabatan Tabel 1 dari specs/HR-ORG-01.json. Nama baru tidak ada.
- Kode dokumen: SNX-HR-FRM-02, SNX-HR-SOP-10, SNX-HR-SOP-12, SNX-HR-ORG-01, SNX-HR-JA-01 dan SNX-ISMS-PRO-01 dari config/worklist.json dan specs terkait, bukan dari berkas Drive. Judul SNX-ISMS-PRO-01 dari specs/ISMS-PRO-01.json.
- Tanpa sumber langsung: pembagian tugas tiga peran (U3), kolom Dasar sertifikasi hanya berisi "form ini atau kontrak pelanggan" (turunan butir 4.7 JA-001), klasifikasi RESTRICTED (Internal) dari worklist, label K-10 (nomor butir di HR-ORG-01), klausul ISO dan judulnya (U8).
- Putaran 1 menambah: lokasi folder Google Drive Departemen HR (U11, mengikuti pola SOP-10 dan SOP-12, berlabel USULAN); retensi tidak diisi; pembeda JA-08 dan JA-09 dari HR-ORG-01; label USULAN pada pemetaan kompetensi (U9) dan pembacaan sebagai Competency Matrix (U10). Klaim pemakaian oleh auditor sudah dihapus.
- Sudah saya perbaiki di teks: tidak ada klaim "belum ada" untuk FRM-02 atau dokumen penilaian kinerja, dan tidak ada angka retensi, lokasi penyimpanan, atau masa pengalaman minimum. Semuanya open item.

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 | Process Owner, Reviewed, butir 4.2 sampai 4.5, 7.3, 7.4, 7.6, 7.8, 7.9, bagian Peran, Rekaman, Acuan ISO, Dokumen Terkait, Kesimpulan | HR Manager | HR Lead |
| A2 | Tabel 1 baris JA-14, kolom Jabatan | HR Manager | HR Lead |

| R2 | Notes open item 2 | keputusan HR Manager | keputusan HR Lead |
| R2 | Notes open item baru 13 | tidak ada | ukuran tingkatan butir 4.3 ganda untuk JA-03, JA-04, dan bawahannya (pemutus Aziz dan owner) |
| R2 | Notes USULAN U3, U11 | HR Manager | HR Lead, dengan catatan "diubah W9" di baris itu |
- SPV tidak ditambahkan: kolom Tingkatan di Tabel 1 memuat ukuran jumlah garis lapor (butir 4.3), bukan tingkat jabatan Lead/SPV; ragu, maka tidak ditambah.
- A3: tingkatan JA-03 dan JA-04 tidak dihitung di dokumen (sel Tingkatan kosong, butir 4.3 hanya aturan). Tidak ada ukuran yang diubah, tidak ada hitung ulang. Kalimat butir 4.3 tentang garis yang menunggu konfirmasi tetap benar untuk JA-05, JA-08, JA-10, JA-11, JA-14.
- B4 rujukan dicek terhadap kerangka: SNX-HR-JA-01 butir 4.6 dan 4.7 ada; SNX-HR-SOP-12 bagian 3 (definisi Tingkatan jabatan) dan butir 4.2 ada; SNX-HR-FRM-02 ada dengan judul sama. Tidak ada rujukan yang diubah.

Open item ditutup atau diubah (status baris lama diubah di tabel Open items):
- ditutup W9: process_owner HR Manager diganti HR Lead mengikuti defaults v22.
- ditutup W9: konfirmasi jabatan Aziz (HR Lead) dan ejaan Samuel Kristanto Utomo berstatus selesai di defaults v22.
- diubah W9: garis lapor JA-03 dan JA-04 sudah diputus owner; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu konfirmasi.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
- Definisi Tingkatan jabatan: "Dasar penetapannya ada di butir 4.3." Kalimat penunjuk (STYLE §3.2); aturannya tetap di butir 4.3.
- Matriks Kompetensi, paragraf pembuka: "Pengisian kolom lain mengikuti butir 7.3 sampai 7.7." Kalimat penunjuk; butir 7.3 sampai 7.7 tetap ada di Cara Mengisi.
- Dokumen Terkait SNX-HR-JA-01: "(butir 4.1 dan 7.6)". Rujukan balik ke butir sendiri, tidak perlu dibuka pembaca.
- Dokumen Terkait SNX-HR-SOP-12: "bagian 3 dokumen itu memuat ukuran tingkatan jabatan yang dipakai butir 4.3." Ditulis ulang "sumber ukuran tingkatan jabatan di form ini"; bagian 3 tetap disebut di butir 4.3.
- Dokumen Terkait SNX-ISMS-PRO-01: "(butir 4.6)". Rujukan balik.
### W10 selisih angka
nihil (subst_diff build kosong)
### W10 catatan
Pihak luar: "pelanggan" (satu-satunya sebutan di dokumen ini, pada "kontrak pelanggan").
Cara Mengisi ditulis sebagai kalimat perintah untuk HRGA Officer (pencatat di tabel Peran); butir 7.9 menyebut HR Lead dan Direktur Utama di tengah kalimat.
Butir 4.5: label (USULAN) tetap hanya pada pembacaan form ini sebagai Competency Matrix; kalimat itu dipindah ke akhir butir.
"Record (rekaman)" di header tabel bagian Rekaman sebagai jembatan heading beku. Tabel 2 diberi min_row_cm 1.4 untuk tulisan tangan.

### W10 rujukan USULAN dicek (adjudikasi worker, gerbang rujukan USULAN)
- .sections[2].blocks[0].table.rows[6][1]: tanpa label; definisi istilah; dasar penetapan berlabel (USULAN) tetap di butir 4.3.
### W10 audit pointer
- .sections[2].blocks[0].table.rows[6][1]: lengkap; kalimat penunjuk "Dasar penetapannya ada di butir 4.3" dibuang (STYLE §3.2), definisi Tingkatan jabatan tetap; butir 4.3 tetap ada beserta label (USULAN).
- .sections[7].blocks[0].p: lengkap; kalimat penunjuk "Pengisian kolom lain mengikuti butir 7.3 sampai 7.7" dibuang; petunjuk 7.1 sampai 7.9 ada di bagian 7 Cara Mengisi tepat sebelum tabel, tidak ada langkah yang hilang.
- .sections[10].blocks[0].table.rows[1][1]: lengkap; penunjuk "(butir 4.1 dan 7.6)" dibuang; rujukan butir 4.7 dokumen JA-01 tetap ("Butir 4.7 dokumen itu"), syarat sertifikasi dan label (USULAN) tetap.
- .sections[10].blocks[0].table.rows[3][1]: lengkap; rujukan "bagian 3 dokumen itu" dan "butir 4.3" dibuang dari baris Dokumen Terkait; ukuran yang sama tetap dinyatakan di butir 4.3 ("sama seperti di SNX-HR-SOP-12 bagian 3 (USULAN)"); syarat pengesahan dan label (USULAN) tetap.
- .sections[10].blocks[0].table.rows[5][1]: lengkap; penunjuk "(butir 4.6)" dibuang, klasifikasi RESTRICTED (Internal) tetap disebut.
