# Catatan penyusun HR-RPT-01: Training Attendance & Training Evaluation Report

Status: DRAFTED (spec + notes ada). Spec: specs/HR-RPT-01.json. Mode generic, aksi T2 tanpa sumber, nomor SNX-HR-RPT-01 (nomor SNX lama dipertahankan), department Human Resources, classification RESTRICTED (Internal), audit_class None, wave W7. doc_type_cover "REPORT", doc_type_label "Report". Approval persis dari config/defaults.json: prepared Sita Nadia Salsabila Widodo / HRGA Officer, reviewed Aziz Priyo Widakdo / HR Manager, approved Samuel Kristanto Utomo / President Director. status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "HR Manager" (jabatan, tanpa nama): dokumen tanpa sumber memakai jabatan reviewer departemen (config/defaults.json, process_owner.rule, status USULAN). Catatan worklist kosong.

Hasil uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-RPT-01.json /tmp/pen-HR-RPT-01/HR-RPT-01.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-HR-RPT-01/HR-RPT-01.docx generic` = "pass": true, fails kosong, satu warn ("18 butir (USULAN) menunggu ACC"). Keluaran lint tersimpan di /tmp/pen-HR-RPT-01/lint_final.txt. Docx dirender ke PDF dengan soffice (12 halaman) dan halaman badan dilihat; judul kolom Daftar Hadir dan Hasil per Peserta sempat terpotong di render pertama dan lebarnya sudah disetel; label Rujukan Rencana dipersingkat agar tidak terbelah. Tabel Tindak Lanjut terbelah antar halaman di render LibreOffice (judul kolom di halaman 10, baris di halaman 11); ini tata letak, bukan isi. Validator OOXML skill docx dan tools/selftest.sh tidak saya jalankan (selftest menulis ke /tmp/selftest yang dipakai bersama penyusun lain). Tidak ada berkas tools, template, config, control, reference, out, qa, atau ledger yang saya ubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Tidak ada sumber tim untuk baris ini (config/worklist.json: "sources": []; aksi T2) | tidak ada | tidak ada | Tidak ada berkas sumber yang gagal dibaca. Alat Drive dimuat dan dipakai hanya untuk dua pembacaan di bawah |
| Kriteria penerimaan: config/checklist.json baris 11, Description | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (Checklist ISO SINUX - 2026) | 2026-10-14T17:47:13.611Z (get_file_metadata hari ini, sama dengan kolom modifiedTime di config/checklist.json) | Dibaca dari berkas repo. Baris 11 tanpa fileId dokumen, tanpa acuan klausul ISO, link_text "On progres", checked false |
| Bahan pendukung, bukan sumber faktual dokumen: SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini, cocok dengan notes/HR-ORG-01.md) | read_file_content, teks penuh. Dipakai hanya untuk tugas HRGA Officer (JA-12) dan HR Manager (JA-14) terkait pelatihan, dan butir ISO 7.2 di bagian 2 sumber |
| Bahan sesama dokumen (bukan berkas Drive) | specs/HR-ORG-01.json, specs/HR-JA-01.json, specs/HR-FRM-01.json, specs/HR-FRM-02.json, specs/ISMS-PRO-01.json | spec lokal | Nama jabatan, nomor butir JA-12 butir 6 dan JA-14 butir 5 di SNX-HR-JA-01, daftar jenis pelatihan dan kolom Kode di SNX-HR-FRM-02, butir 4.8 dan 4.15 SNX-ISMS-PRO-01, serta kecocokan istilah antardokumen |
| Catatan cacat | context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 719 (dan bagian lain yang disebut di bagian "Penanganan cacat") | salinan audit 13 sampai 14 Okt | DATA, lihat Penanganan cacat |

Kalimat perintah di bahan yang saya baca: ada satu pola di context/audit sintesis, yaitu kalimat "Jangan membuat rekaman bertanggal mundur" (tabel ajudikasi konflik, baris "Audit internal Agustus dan TM 21 Sep"). Saya catat sebagai open item 12 dan tidak menjalankannya sebagai instruksi; larangan tanggal mundur yang sama berlaku sendiri lewat RUNBOOK §0 butir 3 dan dipakai di butir 4.2 dokumen. Job Analysis tidak memuat kalimat perintah untuk pembaca.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria penerimaan: dokumen mencatat kehadiran dan mengevaluasi efektivitas pelatihan yang sudah berlangsung. Karena itu dokumen memuat Daftar Hadir, empat aspek evaluasi efektivitas, kesimpulan, dan tindak lanjut untuk satu pelatihan, dan sel isiannya kosong | "Formulir pencatatan kehadiran serta laporan evaluasi efektivitas pelatihan yang telah diselenggarakan." | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| HRGA Officer menyiapkan bukti pelaksanaan dan evaluasi pelatihan. Karena itu HRGA Officer menjadi pencatat dan penyimpan laporan terisi (Peran, butir 6.2 sampai 6.19) | "Menyiapkan bukti pelaksanaan pelatihan, evaluasi dan dokumentasi audit HR." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 (JA-12, Uraian Jabatan A butir 6) |
| HR Manager menindaklanjuti efektivitas pelatihan dan kesenjangan kompetensi. Karena itu HR Manager menetapkan Kesimpulan Efektivitas dan tindakan atas kesenjangan (butir 4.8 dan 4.9) | "Memastikan kebutuhan kompetensi tiap jabatan telah ditetapkan, kesenjangan kompetensi dievaluasi, serta rencana dan efektivitas pelatihan ditindaklanjuti." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 (JA-14, Uraian Jabatan A butir 5) |

## 2. Fakta penting lain dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | ISO 9001:2015 7.2 menuntut evaluasi tindakan memperoleh kompetensi dan bukti pendukung (dasar Acuan Klausul ISO) | "ISO 9001:2015 klausul 7.2: tetapkan kompetensi yang diperlukan, nilai kompetensi aktual, lakukan tindakan jika terdapat kesenjangan, simpan bukti pendukung." | 1m91..., bagian 2 Job Analysis |
| 2 | Rencana pelatihan tahunan di dokumen lain dan dikecualikan | "Dokumen perencanaan tahunan yang mengatur jadwal, jenis pelatihan, dan target peserta pelatihan sesuai jenjang jabatan." | config/checklist.json baris 10 (fileId checklist di atas) |
| 3 | Tata cara identifikasi kebutuhan dan pelaksanaan pelatihan di dokumen lain dan dikecualikan | "Tata cara identifikasi kebutuhan pelatihan, pelaksanaan, dan pengembangan kemampuan karyawan secara berkala." | config/checklist.json baris 5 |
| 4 | Standar kompetensi di SNX-HR-FRM-01 dan dikecualikan | "Matriks pemetaan standar keterampilan, pengetahuan, dan perilaku yang wajib dimiliki karyawan pada setiap tingkatan jabatan." | config/checklist.json baris 9 |
| 5 | Data karyawan masuk tingkat RESTRICTED (dasar butir 4.11) | "Informasi hanya untuk peran atau divisi yang membutuhkan; dipecah per domain: ops, commercial, legal, hr, finance. Contoh: topologi dan konfigurasi pelanggan, register risiko, laporan insiden, kontrak, harga, data karyawan." | specs/ISMS-PRO-01.json, tabel tingkat klasifikasi |
| 6 | Penyimpanan RESTRICTED di sistem resmi dengan akses terbatas per peran (butir 4.11, bagian Rekaman) | "RESTRICTED disimpan di sistem resmi dengan akses terbatas per peran." | specs/ISMS-PRO-01.json, butir 4.8 |
| 7 | Retensi RESTRICTED mengikuti master list dan kontrak; jangka tidak ditulis | "RESTRICTED disimpan sesuai master list dan kontrak." | specs/ISMS-PRO-01.json, butir 4.15 |
| 8 | SNX-HR-FRM-02 menunjuk dokumen ini untuk kehadiran dan evaluasi | "Kehadiran peserta dan evaluasi efektivitas pelatihan" (butir yang dikecualikan) dan "Ada di SNX-HR-RPT-01." | specs/HR-FRM-02.json, Ruang Lingkup |
| 9 | Daftar jenis pelatihan dan kolom Kode ada di SNX-HR-FRM-02 | "Kode \| Nama pelatihan \| Jenis \| Dasar kebutuhan \| Sasaran peserta \| Jadwal rencana \| Keterangan" | specs/HR-FRM-02.json, Tabel 1 |
| 10 | Pelatihan untuk pelanggan, vendor, dan partner dikecualikan di FRM-02 | "Pelatihan untuk pelanggan, vendor, dan partner" \| "Peserta di form ini hanya pemegang jabatan SINUX." | specs/HR-FRM-02.json, Ruang Lingkup |
| 11 | Rekaman kegiatan bergantung kejadian cukup ditunjukkan mekanismenya, dan rekaman tidak bertanggal mundur | "rekaman yang bergantung kejadian (clearance, keluhan) cukup ditunjukkan mekanismenya bila kejadiannya belum ada." dan "Jangan membuat rekaman bertanggal mundur." | context/audit sintesis, bagian 2 butir REVISI 1 dan bagian 5 (baris "Audit internal Agustus dan TM 21 Sep") |
| 12 | Awareness ISMS wajib punya rekaman nyata sebelum stage 2 (dasar cakupan sesi kesadaran, USULAN) | "awareness ISMS (27001 7.3) seluruh karyawan harus sudah terjadi dengan rekaman nyata 2 sampai 3 bulan sebelum stage 2." | context/audit sintesis, bagian 6 butir 7 |
| 13 | Rekam pelatihan dan awareness digabung di satu catatan HR oleh council | "HR: HR-JA-001 final + bagan + wewenang; satu prosedur siklus karyawan; satu matriks kompetensi dan rekam pelatihan/awareness; satu form clearance" | context/audit sintesis, bagian 3 |
| 14 | Butir ini berstatus WAJIB (W) di tier council: perlu rekaman mandiri, bukan hanya isi di dokumen induk | "HR (17) \| 8, 10, 13 (3) \|" (kolom WAJIB; butir 10 = Training Attendance & Training Evaluation Report menurut daftar baris 719) | context/audit sintesis, bagian 2 tabel tier |
| 15 | Peran dan sebutan: HR Manager, HRGA Officer, Direktur Utama; COO tidak muncul di badan dokumen | config/defaults.json data_conflicts: "badan dokumen: 'Direktur Utama' (HR-JA-001), termasuk saat sumber menulis CEO" | defaults v21 |

Pemetaan peran ke HR-ORG-01 (instruksi: nama peran memakai HR-ORG-01, peran lain dipetakan ke jabatan terdekat dan dicatat di sini): HR Manager = JA-14, HRGA Officer = JA-12, Direktur Utama = JA-01 (persis nama di daftar jabatan). "Atasan langsung" memakai istilah yang didefinisikan SNX-HR-ORG-01. "Peserta" dan "Pelatih" tidak ada sebagai jabatan di HR-ORG-01; keduanya peran per pelatihan, bukan jabatan tetap, dan tidak dipetakan ke JA-nn (pelatih bisa dari penyelenggara luar).

## 3. Pemetaan klausul ISO

Checklist tidak memberi acuan klausul untuk baris ini. Bagian Acuan Klausul ISO memuat lima baris dengan satu label "(USULAN, perlu konfirmasi konsultan)". Judul klausul adalah pengetahuan standar, bukan teks sumber tim.

| Klausul | Alasan | Catatan |
|---|---|---|
| ISO 9001:2015 7.2 Kompetensi | Butir c (tindakan memperoleh kompetensi dan evaluasi efektivitasnya) dan butir d (bukti kompetensi) paling dekat dengan dokumen ini. Penetapan kompetensi (butir a) ada di SNX-HR-FRM-01 dan ditulis begitu di tabel | Job Analysis bagian 2 memakai 7.2 untuk hal yang sama |
| ISO 9001:2015 7.5.3 Pengendalian informasi terdokumentasi | Laporan terisi adalah rekaman yang butuh lokasi, pemilik, klasifikasi (bagian Rekaman) | Tafsir penyusun |
| ISO/IEC 27001:2022 7.2 Kompetensi | Klausul yang sama untuk ISMS | Tafsir penyusun |
| ISO/IEC 27001:2022 7.3 Kesadaran | Berlaku bila sesi kesadaran dicatat di dokumen ini, yaitu cakupan USULAN U1 | Sintesis bagian 6 butir 7 menyebut 27001 7.3 untuk awareness |
| ISO/IEC 27001:2022 Annex A 6.3 Kesadaran, pendidikan, dan pelatihan keamanan informasi | Pelatihan keamanan informasi yang diselenggarakan masuk laporan ini | Kontrol 6.3 "wajib Ya" menurut ajudikasi council di sintesis bagian 5 (baris Dua SoA), tetapi status di SoA berlabel "Perlu keputusan" di salinan audit ISMS; konsultan menilai |

ISO 9001:2015 7.3 (Kesadaran) tidak dimasukkan: sesi kesadaran mutu bukan penyebab dokumen ini dibuat, dan Job Analysis menyebut 7.3 tanpa rincian. Konsultan dapat menambahkannya. ISO/IEC 27001:2022 7.5.3 juga tidak dimasukkan agar bagian ini tidak mengulang 9001 7.5.3.

## 4. Keputusan desain dan tafsir

1. Satu laporan = satu pelatihan. Struktur terdiri dari Informasi Pelatihan, Daftar Hadir, Ringkasan Kehadiran, Evaluasi Efektivitas per Aspek, Hasil per Peserta, Kesimpulan Efektivitas, Tindak Lanjut, dan Pengesahan. Kriteria hanya menyebut kehadiran dan evaluasi efektivitas; tabel Tindak Lanjut ditambahkan karena JA-14 butir 5 menuntut efektivitas "ditindaklanjuti" dan ISO 9001 7.2 butir c menuntut tindakan atas kesenjangan.
2. Semua sel faktual kosong: Informasi Pelatihan, Daftar Hadir, Ringkasan, kolom hasil, Kesimpulan, Tindak Lanjut, dan Pengesahan. Tanpa baris contoh. Terisi hanya: judul kolom, nomor urut baris, kode dan nama aspek E1 sampai E4, dan peran di tabel Pengesahan.
3. Jumlah baris kosong (10 di Daftar Hadir dan Hasil per Peserta, 3 di Tindak Lanjut) adalah kapasitas tata letak, bukan klaim jumlah peserta. Teks pembuka bagian 7 memberi izin menambah baris.
4. Empat aspek E1 sampai E4 (reaksi, pemahaman, penerapan, hasil pekerjaan) adalah rancangan penyusun, berlabel USULAN. Tidak ada angka ambang, skala nilai, atau jangka waktu yang ditulis: Kriteria Keberhasilan dan Tanggal Evaluasi Lanjutan diisi per pelatihan oleh HR Manager. Nilai Efektif, Sebagian Efektif, dan Belum Efektif didefinisikan terhadap Kriteria Keberhasilan itu, bukan terhadap persentase.
5. Nama model evaluasi dari luar tidak dipakai di teks agar tidak menyisipkan rujukan tanpa sumber.
6. Peran: HR Manager menetapkan dan memeriksa, HRGA Officer mencatat dan menyimpan, Pelatih menilai E2, Atasan langsung menilai E3 dan E4, Peserta menandatangani dan memberi umpan balik, Direktur Utama menyetujui lewat blok Approved By. Pembagian ini turunan dari blok Prepared By, Reviewed By, Approved By dan dari JA-12 dan JA-14, jadi berlabel USULAN. Penetapan dan pencatatan dibedakan konsisten di butir 4.3, 4.8, 4.9, bagian 5, dan langkah 6.1 sampai 6.19.
7. Bagian 3 hanya arti istilah dan arti nilai kolom. Aturannya di bagian 4. Peninjauan tahunan hanya ditulis di Kesimpulan, tidak di Peran.
8. Selaras dengan SNX-HR-FRM-02 yang sudah ada di specs saat saya menulis: istilah "sasaran peserta" dan "jadwal rencana", kolom Kode di Tabel 1 sebagai Rujukan Rencana, daftar jenis pelatihan dipakai lewat rujukan (bukan disalin), dan pengecualian pelatihan untuk pelanggan, vendor, dan partner. Tindakan pelatihan lanjutan dicatat di SNX-HR-FRM-02 (butir 4.9, USULAN), sama dengan yang ditulis SNX-HR-SOP-12; SOP-12 tidak dirujuk di badan dokumen ini sehingga tidak masuk tabel Dokumen Terkait.
9. Sebutan COO tidak muncul di badan dokumen, jadi aturan "Direktur (COO)" tidak terpakai. Samuel ditulis "Direktur Utama" di badan dan "President Director" hanya di blok Approved By. Tidak ada nama orang di badan dokumen.
10. Zammad, GLPI, vault, PPN: tidak relevan dan tidak disebut. Satu-satunya sistem yang disebut adalah Google Drive (SNX-ISMS-PRO-01 butir 4.8 menyebutnya sebagai sistem resmi).
11. Setiap kode dokumen di badan ada di tabel Dokumen Terkait: SNX-HR-FRM-01, SNX-HR-FRM-02, SNX-HR-ORG-01, SNX-HR-JA-01, SNX-ISMS-PRO-01, dan SOP Training & Development (belum bernomor). Dicek dengan pemindai regex atas teks spec: tidak ada kode yang hilang.
12. Frasa "belum ada" tidak dipakai. SOP Training & Development ditulis "belum bernomor" dan "Menjadi isi", tanpa menyatakan status berkasnya. SNX-HR-FRM-02 hanya ditulis judul dan fungsinya.
13. Retensi: tidak ada angka. Kalimat di bagian Rekaman memuat aturan yang ada di SNX-ISMS-PRO-01 butir 4.15 dan menyebut pemutus jangka (HR Manager bersama Legal, USULAN).

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Cakupan memuat pelatihan oleh penyelenggara luar dan sesi kesadaran ISO dan keamanan informasi | Ruang Lingkup | Aziz; konsultan untuk sisi ISO |
| U2 | Peserta hanya karyawan SINUX; pelatihan untuk pelanggan, vendor, dan partner dikecualikan | Ruang Lingkup | Owner |
| U3 | HR Lead menetapkan Tujuan Pembelajaran dan Kriteria Keberhasilan sebelum pelatihan dimulai | Butir 4.3, langkah 6.1 | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U4 | Tanda tangan peserta pada Daftar Hadir menjadi bukti kehadiran | Butir 4.4 | Aziz |
| U5 | Evaluasi efektivitas memakai empat aspek E1 sampai E4 beserta arti masing-masing | Butir 4.5, bagian 3 | Aziz |
| U6 | E3 dan E4 diisi pada Tanggal Evaluasi Lanjutan yang ditentukan HR Lead tiap pelatihan | Butir 4.6 | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U7 | Tindakan pelatihan lanjutan dicatat di SNX-HR-FRM-02 | Butir 4.9, Dokumen Terkait | Aziz |
| U8 | Peserta Tidak Hadir tidak dinilai pada E2 sampai E4, dan HR Lead memutuskan pelatihan susulan | Butir 4.10 | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U9 | Pembagian tugas HR Lead, HRGA Officer, Peserta, Pelatih, Atasan langsung, dan Direktur Utama | Peran, langkah 6.1 sampai 6.19 | Aziz; Samuel untuk peran penyetuju; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U10 | Daftar nilai kolom Status Kehadiran, Status Hasil, Kesimpulan Efektivitas, dan Status pada Tindak Lanjut | Bagian 3, Nilai pada Kolom Status dan Kesimpulan | Aziz |
| U11 | Lokasi rekaman (folder Google Drive departemen Human Resources), pencatat HRGA Officer, pemilik HR Lead, bukti disimpan bersama laporan terisi | Rekaman | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U12 | Jangka retensi laporan terisi dan bukti | Rekaman | Legal bersama Aziz |
| U13 | HR Lead memakai SNX-HR-FRM-01 untuk menulis Tujuan Pembelajaran bila pelatihan menutup kesenjangan kompetensi | Dokumen Terkait | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U14 | Lima klausul ISO 9001:2015 dan ISO/IEC 27001:2022 | Acuan Klausul ISO | Legal bersama konsultan (konsultan memutus; Legal mencatat) |

Jumlah USULAN: 14 butir. Teks dokumen memuat 18 label "(USULAN)" karena beberapa butir diberi label di lebih dari satu kalimat; lint menghitung 18. Tidak ada angka bisnis tanpa sumber di dokumen.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Tidak ada sumber tim. Seluruh struktur berasal dari kriteria checklist, tugas JA-12 dan JA-14, dan tafsir penyusun. Aziz perlu memeriksa apakah tim sudah punya formulir kehadiran atau lembar evaluasi yang dipakai; bila ada, struktur dokumen ini disesuaikan | Aziz |
| 2 | Lembar umpan balik peserta (E1), instrumen tes atau penilaian pelatih (E2), dan lembar penilaian atasan langsung (E3 dan E4) belum dibakukan. Dokumen ini hanya memuat kolom Metode dan Bukti yang diisi per pelatihan | Aziz |
| 3 | Isi Kriteria Keberhasilan dan selang waktu ke Tanggal Evaluasi Lanjutan ditetapkan per pelatihan oleh HR Lead. Tidak ada angka acuan di sumber | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| 4 | Lokasi folder dan hak akses laporan terisi, serta jangka retensi, belum ditetapkan. SNX-ISMS-PRO-01 butir 4.15 hanya menyebut "master list dan kontrak" | Aziz untuk lokasi; Legal untuk retensi |
| 5 | SOP Training & Development belum bernomor (checklist baris 5 tanpa berkas, T3 HOLD). Kode dan kecocokan rujukan di Ruang Lingkup dan Dokumen Terkait dicek setelah dokumen itu ada. SNX-HR-FRM-02 menulis status dokumen yang sama sebagai "dalam peninjauan", sedangkan dokumen ini menulis "belum bernomor"; samakan setelah LEAD memutus | LEAD, lalu Aziz; diubah W9: SOP Training & Development ditulis "dalam peninjauan" seragam dengan SNX-HR-FRM-02; kode tetap menunggu dokumennya bernomor |
| 6 | SNX-HR-FRM-02 ditulis paralel (ledger IN_PROGRESS saat saya mulai). Periksa ulang kolom Kode, daftar jenis pelatihan, dan butir 4.9 bila FRM-02 diubah | LEAD |
| 7 | Cakupan sesi kesadaran ISO dan keamanan informasi, dan pelatihan oleh penyelenggara luar (U1). Council menggabungkan rekam pelatihan dan awareness di satu catatan HR, sedangkan checklist 88 baris tidak punya baris awareness terpisah; belum jelas apakah sesi awareness memakai laporan ini | Aziz dan konsultan |
| 8 | Tempat mencatat pelatihan yang SINUX berikan kepada pelanggan (dikecualikan di U2). Salinan audit Commercial menyebut kegiatan "Training: hands-on untuk ops team" sebagai bagian layanan | Owner; Fani untuk sisi Operation |
| 9 | Pelatih dari penyelenggara luar tidak terikat peran Pelatih lewat dokumen internal. Cara memperoleh hasil penilaian E2 dari mereka (kontrak, laporan penyelenggara) belum ditetapkan | Aziz |
| 10 | Garis lapor yang menentukan "atasan langsung" peserta masih menunggu konfirmasi untuk JA-03, JA-05, JA-08, JA-10, JA-11, dan JA-14 (SNX-HR-ORG-01, butir K-01 sampai K-04). Penilai E3 dan E4 untuk peserta itu belum pasti | Owner; diubah W9: JA-03 dan JA-04 kini dua garis tegas ke Direktur dan Direktur Utama (LEAD G-3 A3), tidak menunggu; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu (A4) |
| 11 | data_conflicts yang konfirmasinya belum selesai dan relevan: jabatan Aziz "HR Manager" (konfirmasi: owner atau Aziz) dan ejaan "Samuel Kristanto Utomo" (konfirmasi: owner atau Samuel). Dipakai sesuai kolom "pakai" | Owner; ditutup W9: jabatan Aziz HR Lead dan ejaan Kristanto berstatus selesai (defaults v22) |
| 12 | Kalimat perintah di DATA: "Jangan membuat rekaman bertanggal mundur" (context/audit sintesis). Dicatat, tidak dijalankan sebagai instruksi; butir 4.2 mengikuti RUNBOOK §0 butir 3 | LEAD |
| 13 | Penomoran daftar HR di context/audit sintesis tidak seragam: butir dissent bagian 6 menulis "HR 9" untuk awareness, padahal daftar baris 718 sampai 720 menaruh butir 9 = Annual Training Plan & Training Matrix dan butir 11 = ISO Awareness. Dokumen ini tidak bersandar pada nomor itu | LEAD |
| 14 | SNX-ISMS-PRO-01 menulis cakupannya Divisi Operation dan perluasan ke Human Resources berstatus USULAN, padahal tingkat RESTRICTED (Internal) dipakai semua dokumen HR menurut config/defaults.json. Butir 4.11 merujuk butir 4.8 dokumen itu; rujukan itu berlaku penuh setelah cakupan diperluas | Owner |
| 15 | process_owner "HR Manager" mengikuti aturan dokumen tanpa sumber, status USULAN di defaults | Aziz; ditutup W9: process_owner kini HR Lead (defaults v22) |
| 16 | Tabel Tindak Lanjut terbelah antar halaman di render LibreOffice. Perlu dilihat di Word oleh orang; bukan hasil yang bisa dipastikan mesin | HUMAN-VERDICT, Aziz atau LEAD; ditutup W9: tabel diberi repeat_header dan cant_split (LEAD G-3 B4); render ulang lolos lint, validasi, blankscan |

## Penanganan cacat context/audit

Perintah: `grep -n "Training Attendance & Training" context/audit/*.md`. Hasil: satu baris, context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md:719 ("10. Training Attendance & Training Evaluation Report."), butir ke-10 dalam daftar HR. Tidak ada bagian dokumen sendiri dan tidak ada "Catatan kualitas dan celah" untuk baris ini. Saya membaca daftar HR di sintesis (baris 709 sampai 726), tabel tier dan penggabungan (bagian 2 dan 3), ajudikasi konflik (bagian 5), dissent (bagian 6), dan bagian 5 Catatan kualitas di dokumen HR-JA-001 (context/audit hr, baris 1232 sampai 1250), karena Job Analysis adalah sumber peran.

| Cacat atau catatan | Relevansi | Penanganan |
|---|---|---|
| Sintesis bagian 2: butir HR 10 bertier WAJIB (W), bukan G. Wajib berlaku pada isi dan bukti, rekaman bergantung kejadian cukup ditunjukkan mekanismenya | Langsung | Dokumen ini berdiri sendiri sebagai rekaman. Karena kejadiannya belum ada, dokumen hanya memuat mekanisme (struktur dan petunjuk) dan tidak memuat baris contoh atau data buatan |
| Sintesis bagian 5: audit perdana, jangan membuat rekaman bertanggal mundur | Langsung | Butir 4.2: tanggal adalah tanggal kejadian sebenarnya, dan HRGA Officer tidak mengisi kehadiran, hasil evaluasi, atau tanggalnya sebelum peristiwanya terjadi. Tidak ada tanggal di dokumen. Open item 12 mencatat kalimat itu sebagai pola perintah di DATA |
| Sintesis bagian 3: rekam pelatihan dan awareness digabung dalam satu catatan HR bersama matriks kompetensi | Langsung | Checklist menjaga FRM-01, FRM-02, dan RPT-01 sebagai tiga baris terpisah dan scope dibatasi 88 baris, jadi dokumen ini tetap berdiri sendiri. Rekam awareness dimasukkan lewat cakupan USULAN U1, bukan dokumen baru. Open item 7 |
| Sintesis bagian 6 butir 7: nomor "HR 9" untuk awareness tidak cocok dengan daftar | Tidak langsung | Tidak dipakai sebagai dasar. Open item 13 |
| Sintesis bagian 6 butir 6 (council 2, Fable): "bukti A 6.1/7.2 di matriks kompetensi + NDA" tanpa judul klausul | Tidak langsung | Dokumen ini memetakan 7.2 dan A 6.3, bukan A 6.1 (Screening) karena tidak memuat tahap seleksi. Alasan di bagian 3 |
| HR-JA-001 bagian 5 butir 4: frasa kompetensi janggal ("pelatihan evaluation" muncul di JA-14 C butir 5, "Competency mapping, TNA dan pelatihan evaluation") | Tidak langsung | Tidak ada nama kompetensi yang disalin. Dokumen hanya mengutip JA-12 A butir 6 dan JA-14 A butir 5, yang kalimatnya utuh |
| HR-JA-001 bagian 5 butir 11: ejaan Samuel dan sebutan CEO | Ya | "Samuel Kristanto Utomo" di blok Approved By, "Direktur Utama" di badan, sesuai defaults |
| HR-JA-001 bagian 5 butir 2 dan 13: tidak ada grading, masa pengalaman minimum belum ada | Tidak langsung | Tidak dipakai: laporan ini tidak menetapkan tingkatan atau pengalaman |
| HR-JA-001 bagian 5 butir 5 sampai 9: garis lapor dan nama unit tidak seragam | Tidak langsung | Memengaruhi siapa "atasan langsung" peserta. Open item 10 |
| HR-JA-001 bagian 5 butir 1, 3, 10, 12, 14, 15 | Tidak relevan | Status JA-001, kalimat terpotong, Finance Lead dan Finance Staff, teks identik antar jabatan, jumlah tabel, klausul 7.3 dan 7.5 JA-001 |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Benda memakai kata kerja manusia. Saya cek tiap kalimat dengan subjek "Laporan", "Tabel", "Daftar Hadir", dan "Tanda tangan". Yang tersisa memuat atau menjadi sesuatu ("Laporan ini memuat", "Tabel ... memuat", "Daftar Hadir menjadi bukti", "Tanda tangan ... menjadi bukti kehadiran"). Tidak ada kalimat "laporan menetapkan", "tabel menentukan", atau "laporan memastikan". Pelaku tindakan selalu HR Manager, HRGA Officer, Peserta, Pelatih, atau Atasan langsung.
- Ekor penegas dan pengisi: tidak ada "tanpa terkecuali", "perlu dicatat bahwa", "dalam rangka", "adapun". Kesimpulan dua kalimat tanpa pujian.
- Draf pertama memakai "kolom Rujukan Rencana baris pelatihan itu di SNX-HR-FRM-02, dan mengosongkannya" dalam satu kalimat bertumpuk. Saya pecah jadi dua kalimat pendek (langkah 6.3). Peninjauan tahunan sempat tertulis di Peran dan di Kesimpulan; saya hapus dari Peran karena tempatnya di Kesimpulan.
- Kelompok tiga yang tersisa: "pengetahuan, keterampilan, atau perilaku" (definisi Pelatihan dan Tujuan Pembelajaran), "materi, pelatih, dan penyelenggaraan" (E1), "nama, jabatan, dan unit" (kolom Daftar Hadir). Ketiganya adalah isi nyata, bukan tiga yang dipaksakan: tiga kelompok kompetensi sama dengan SNX-HR-FRM-01 dan tiga hal yang dinilai di umpan balik peserta. Saya biarkan dan catat di sini.
- Sinonim: "evaluasi" dipakai untuk kegiatan dan tabel (Evaluasi Efektivitas, Tanggal Evaluasi Lanjutan) dan "menilai" untuk tindakan penilai; "pelatihan susulan" (untuk peserta Tidak Hadir) dan "pelatihan lanjutan" (untuk menutup kesenjangan) adalah dua hal berbeda. Kedua pasangan bisa terbaca sinonim; saya biarkan karena artinya berbeda dan sudah dipisah di butir 4.9 dan 4.10, tetapi verifikator perlu menilai.
- Langkah 6.1 sampai 6.19 hampir semuanya diawali nama peran. Terbaca seragam, tetapi tiap langkah satu tindakan dan satu pelaku, sesuai RUNBOOK §6a.2. Saya biarkan. Dua langkah memuat dua kata kerja (6.6 dan 6.16) untuk satu keluaran yang sama; panjangnya di bawah sekitar 28 kata.
- Definisi "Pelatihan", "Peserta", dan skala nilai Hadir, Tidak Hadir bisa ditempel ke perusahaan mana pun. Itu sifat definisi dan nilai; tidak ada kalimat yang saya tambah untuk membuatnya terdengar meyakinkan, dan nilai berlabel USULAN.
- Tidak ada pembuka generik, penutup positif, em-dash, en-dash, tebal, kutip penekanan, "tidak hanya ... tetapi juga", atau kosakata AI English. Lint gaya lulus (fails kosong).

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: empat aspek E1 sampai E4 (tanpa sumber, berlabel USULAN, U5). Sepuluh baris Daftar Hadir dan Hasil per Peserta serta tiga baris Tindak Lanjut adalah kapasitas tata letak, tidak ditulis sebagai klaim di teks selain izin menambah baris. Nomor butir 4.8 dan 4.15 SNX-ISMS-PRO-01 dan JA-12 butir 6, JA-14 butir 5 SNX-HR-JA-01 dicek langsung terhadap isi specs. Tidak ada angka bisnis, persentase, ambang, atau jangka retensi.
- Nama dan jabatan: tiga nama di blok approval dari config/defaults.json. Badan dokumen hanya memuat jabatan (HR Manager, HRGA Officer, Direktur Utama) dari specs/HR-ORG-01.json dan peran fungsional (Peserta, Pelatih, Atasan langsung) tanpa nama orang. Tidak ada nama baru.
- Tanggal: tidak ada tanggal di dokumen. Effective Date kosong.
- Kode dan sistem: kelima kode SNX dari config/worklist.json dan specs terkait, bukan dari berkas Drive. Judul SNX-ISMS-PRO-01 dari specs/ISMS-PRO-01.json. Google Drive dari butir 4.8 SNX-ISMS-PRO-01. "Master list" dari butir 4.15 dokumen yang sama.
- Tanpa sumber langsung: seluruh pembagian peran (U9), cakupan penyelenggara luar dan sesi awareness (U1), pengecualian pelatihan pelanggan (U2, dasar sebagian dari FRM-02), daftar nilai kolom (U10), lokasi rekaman (U11), klausul ISO beserta judulnya (U14). Semuanya berlabel USULAN di teks.
- Sudah saya perbaiki di teks: tidak ada klaim "belum ada" untuk SOP Training & Development atau SNX-HR-FRM-02, tidak ada angka retensi, dan nilai kolom diberi label USULAN lewat satu kalimat di bawah judul tabelnya (draf pertama belum berlabel).

## Sweep

Putaran sweep 15 Okt 2026, butir 1 dari orkestrator: "pasif 4.5-4.7, isi bagian 4 terulang di bagian 6" (temuan nonblocking di qa/HR-RPT-01.verify.json). Fakta, angka, nama, struktur, dan label USULAN tidak berubah; kalimat bagian 4 yang pasif diberi pelaku (HRGA Officer atau HR Manager, sesuai Peran), dan langkah bagian 6 yang menyalin isi butir bagian 4 kini merujuk nomor butirnya. Satu butir diubah, 10 kalimat spec berubah (tiap sebelum dan sesudah di bawah).

| Letak | Sebelum | Sesudah |
|---|---|---|
| 4.5 | "Setiap aspek diisi metode, bukti, dan ringkasan hasil, dan bukti disimpan bersama laporan terisi." | "HRGA Officer mencatat metode, bukti, dan ringkasan hasil tiap aspek." (penyimpanan bukti tetap di langkah 6.19 dan bagian 8) |
| 4.6 | "E1 dan E2 diisi sesudah pelatihan selesai. E3 dan E4 diisi pada Tanggal Evaluasi Lanjutan, yang ditentukan HR Manager untuk tiap pelatihan (USULAN)." | "HRGA Officer mencatat hasil E1 dan E2 sesudah pelatihan selesai, dan hasil E3 dan E4 pada Tanggal Evaluasi Lanjutan. HR Manager menetapkan tanggal itu untuk tiap pelatihan (USULAN)." ("ditentukan" jadi "menetapkan", sama dengan butir 4.3, langkah 6.1, dan Peran) |
| 4.7 | "Aspek yang tidak dinilai diisi Tidak Dinilai pada Ringkasan Hasil, dengan alasan di kolom Catatan. Hasil yang tidak punya bukti tidak ditulis." | "HRGA Officer menulis Tidak Dinilai di Ringkasan Hasil untuk aspek yang tidak dinilai, dan di Status Hasil untuk peserta yang tidak dinilai, dengan alasan di kolom Catatan. HRGA Officer tidak menulis hasil yang tidak punya bukti." |
| 6.1 | "... Tanggal Evaluasi Lanjutan sebelum pelatihan dimulai." | "... Tanggal Evaluasi Lanjutan (butir 4.3 dan 4.6)." |
| 6.5 | "Peserta menandatangani Daftar Hadir pada hari pelatihan." | "Peserta menandatangani Daftar Hadir (butir 4.4)." |
| 6.11 | "HRGA Officer mencatat metode, bukti, dan ringkasan hasil E1 sampai E4 di tabel Evaluasi Efektivitas per Aspek." | "HRGA Officer mengisi tabel Evaluasi Efektivitas per Aspek untuk E1 sampai E4 (butir 4.5 dan 4.6)." |
| 6.13 | "HRGA Officer menulis Tidak Dinilai di Ringkasan Hasil atau Status Hasil, dan alasannya di kolom Catatan, untuk aspek atau peserta yang tidak dinilai." | "HRGA Officer mengisi Tidak Dinilai untuk aspek atau peserta yang tidak dinilai (butir 4.7)." |
| 6.14 | "HR Manager membandingkan hasil dengan Kriteria Keberhasilan, lalu menulis Kesimpulan Efektivitas, Dasar Kesimpulan, dan Kesenjangan yang ditemukan." | "HR Manager mengisi tabel Kesimpulan Efektivitas (butir 4.8)." |
| 6.15 | "HR Manager menetapkan tindakan, penanggung jawab, dan target selesai untuk tiap Kesenjangan." | "HR Manager menetapkan tindakan atas tiap Kesenjangan (butir 4.9)." |
| Peran, baris HRGA Officer | "(butir 4.2, 4.5, 4.9, dan 4.11)" | "(butir 4.2, 4.5 sampai 4.7, 4.9, dan 4.11)" (karena 4.6 dan 4.7 kini menyebut HRGA Officer) |

Tidak diubah, sesuai batas putaran: butir nonblocking lain di verify.json (sinonim "penilaian" dan "evaluasi", bukti hadir daring, pembanding Status Hasil, status SOP Training & Development, cakupan SNX-ISMS-PRO-01, dan selarasnya SNX-HR-FRM-02 butir 4.4). Semuanya tetap tercatat di Open items atau menunggu putaran berikut; tidak ada fakta baru dan tidak ada USULAN baru.

Uji sesudah sweep: render_sop.py = ok; lint_doc.py generic = "pass": true, fails kosong, satu warn (18 label USULAN); validate.py = "All validations PASSED!" (528 paragraf); reports/orch/blankscan.py = "ok 12 HR-RPT-01.docx []".

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 | Process Owner, Reviewed, butir 4.3, 4.6, 4.8 sampai 4.10, bagian Peran, langkah 6.1, 6.14, 6.15, 6.18, tabel Pengesahan (Pemeriksa), Rekaman, Dokumen Terkait, Kesimpulan | HR Manager | HR Lead |
| B4 | Ruang Lingkup, baris tata cara identifikasi kebutuhan pelatihan | Menjadi isi SOP Training & Development (belum bernomor). | Menjadi isi SOP Training & Development (dalam peninjauan). |
| B4 | Dokumen Terkait, baris Belum bernomor | SOP Training & Development: tata cara identifikasi ... | SOP Training & Development, dalam peninjauan: tata cara identifikasi ... |
| B4 | Semua 15 blok table | tanpa flag | "repeat_header": true dan "cant_split": true |
| R2 | Notes USULAN U3, U6, U8, U9, U11, U13 dan open item 3 | HR Manager | HR Lead, dengan catatan "diubah W9" di baris itu |
- SPV tidak ditambahkan: dokumen tidak punya kolom tingkat jabatan.
- A3: "Atasan langsung" ditulis sebagai peran generik; tidak ada JA-03 atau JA-04. Tidak ada perubahan.
- B4 rujukan dicek terhadap kerangka: SNX-HR-JA-01 uraian JA-12 dan JA-14 (butir 6 dan 5) ada; SNX-ISMS-PRO-01 butir 4.8 dan 4.15 ada; SNX-HR-FRM-02 Tabel 1 dan butir 4.9 ada; SNX-HR-FRM-01 ada. Tidak ada rujukan yang diubah. Kode SOP Training & Development tetap "Belum bernomor" di kolom Kode, sama dengan SNX-HR-FRM-02.

Open item ditutup atau diubah (status baris lama diubah di tabel Open items):
- ditutup W9: process_owner HR Manager diganti HR Lead mengikuti defaults v22.
- ditutup W9: konfirmasi jabatan Aziz (HR Lead) dan ejaan Samuel Kristanto Utomo berstatus selesai di defaults v22.
- diubah W9: garis lapor JA-03 dan JA-04 sudah diputus owner; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu konfirmasi.
- ditutup W9: tabel terbelah antarhalaman, diatasi dengan baris judul berulang dan baris tidak terbelah (LEAD G-3 B4); pemeriksaan visual di Word tetap boleh oleh orang.
- diubah W9: penulisan SOP Training & Development diseragamkan menjadi "dalam peninjauan".

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
- Tujuan: label "Hasil yang dijaga:" dihapus; isinya ditulis ulang sebagai dua kalimat biasa.
- Tabel Peran: rujukan balik "(butir 4.3, 4.6, 4.8 sampai 4.10)", "(butir 4.2, 4.5 sampai 4.7, 4.9, dan 4.11)", "(butir 4.4 dan 4.5)", "(butir 4.5)", "(butir 4.5 dan 4.6)". Tugasnya sudah tertulis di sel; nomor butir tetap di Dasar dan Ketentuan.
- Rekaman: "(butir 4.11)". Acuan Klausul ISO: "(bagian 8)" dan "(cakupan USULAN di bagian 2)"; fakta USULAN-nya dibawa sebagai label (USULAN) di akhir sel. Dokumen Terkait SNX-HR-FRM-02: "butir 4.9" dari "(butir 4.9, USULAN)".
- Definisi Daftar Hadir: "Tabel di bagian 7" menjadi "Tabel di bagian Isi Laporan". Dokumen Terkait SNX-HR-JA-01: "bagian 5" menjadi "bagian Peran".
### W10 selisih angka
- usul_butir "6.19" baru: kalimat penunjuk "di lokasi pada bagian 8" diganti faktanya, "folder Google Drive departemen Human Resources", yang di tabel Rekaman berlabel USULAN; label ikut dibawa (Pelajaran sapuan). Aturannya tidak berubah.
### W10 catatan
Pihak luar: "pelanggan" (satu-satunya sebutan, di Ruang Lingkup). Dokumen yang belum ada ditulis "SOP Training & Development (dalam review)".
Petunjuk Pengisian ditulis sebagai kalimat perintah untuk HRGA Officer; butir milik HR Lead, Peserta, Pelatih, dan Atasan langsung (6.1, 6.5, 6.8 sampai 6.10, 6.14, 6.15, 6.18) menyebut perannya di tengah atau akhir kalimat. Nama peran tidak berubah.
Daftar Hadir diberi min_row_cm 0.9, Hasil per Peserta 0.8, Kesimpulan Efektivitas 1.2, Tindak Lanjut dan Pengesahan Laporan Terisi 1.0, untuk tulisan tangan dan tanda tangan.
### W10 audit pointer
- .sections[2].blocks[0].table.rows[4][1]: lengkap; "bagian 7" diganti nama bagiannya "bagian Isi Laporan"; isi definisi tetap.
- .sections[4].blocks[1].table.rows[0][1]: lengkap; penunjuk balik "(butir 4.3, 4.6, 4.8 sampai 4.10)" dibuang; tiga tugas HR Lead tetap; syarat waktu dan label (USULAN) tetap di butir 4.3 dan seterusnya.
- .sections[4].blocks[1].table.rows[1][1]: lengkap; penunjuk "(butir 4.2, 4.5 sampai 4.7, 4.9, dan 4.11)" dibuang; tugas HRGA Officer tetap; aturan tanggal kejadian tetap di butir 4.2.
- .sections[4].blocks[1].table.rows[2][1]: lengkap; penunjuk "(butir 4.4 dan 4.5)" dibuang; tugas Peserta tetap; label (USULAN) bukti kehadiran tetap di butir 4.4.
- .sections[4].blocks[1].table.rows[3][1]: lengkap; penunjuk "(butir 4.5)" dibuang.
- .sections[4].blocks[1].table.rows[4][1]: lengkap; penunjuk "(butir 4.5 dan 4.6)" dibuang.
- .sections[5].blocks[18].p: lengkap; "lokasi pada bagian 8" diganti isi bagian 8 (folder Google Drive departemen Human Resources) beserta label (USULAN).
- .sections[7].blocks[0].table.rows[0][1]: lengkap; penunjuk "(butir 4.11)" dibuang; akses terbatas, pencatat, pemilik (USULAN) tetap.
- .sections[8].blocks[1].table.rows[1][2]: lengkap; penunjuk "(bagian 8)" dibuang.
- .sections[8].blocks[1].table.rows[3][2]: lengkap; "(cakupan USULAN di bagian 2)" diganti label (USULAN), status usulan tetap.
- .sections[9].blocks[0].table.rows[1][1]: lengkap; penunjuk "(butir 4.9, USULAN)" menjadi "(USULAN)"; fungsi dokumen dan label tetap.

### W10 audit cakupan label
- .sections[4].blocks[0].p: OK (pembagian tugas tetap berlabel)
- .sections[5].blocks[18].p: OK (rujukan lokasi bagian 8 yang berlabel diganti fakta)
- .sections[8].blocks[1].table.rows[3][2]: OK (label cakupan bagian 2 tetap)
- .sections[9].blocks[0].table.rows[1][1]: OK (label tetap pada kalimat kedua)
