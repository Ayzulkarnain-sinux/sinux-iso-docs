# Catatan penyusun HR-FRM-02: Annual Training Plan & Training Matrix

Status: DRAFTED (spec + notes ada). Spec: specs/HR-FRM-02.json. Mode generic, aksi T2 tanpa sumber, nomor SNX-HR-FRM-02 (nomor SNX lama dipertahankan), department Human Resources, classification RESTRICTED (Internal), audit_class None, wave W7. Approval persis dari config/defaults.json: prepared Sita Nadia Salsabila Widodo / HRGA Officer, reviewed Aziz Priyo Widakdo / HR Manager, approved Samuel Kristanto Utomo / President Director. status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "HR Manager" (jabatan, tanpa nama): dokumen tanpa sumber memakai jabatan reviewer departemen (config/defaults.json, process_owner.rule, status USULAN).

Hasil uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-FRM-02.json /tmp/pen-HR-FRM-02/HR-FRM-02.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-HR-FRM-02/HR-FRM-02.docx generic` = "pass": true, fails kosong, satu warn (17 label "(USULAN)" menunggu ACC). tools/selftest.sh: 6 baris OK. PDF hasil soffice 10 halaman; header Tabel 1 dan Tabel 2 tidak terpotong di tengah kata (putaran awal dengan 9 kolom memotong "Kode", "Penyelenggara", dan "Keterangan", lalu kolom dikurangi jadi 7). Tabel 2 pindah halaman di antara baris JA-03 dan JA-04, tanpa memecah satu baris. Header Tabel 2 tidak berulang di halaman berikutnya: perilaku renderer, tidak saya ubah. Tidak ada berkas tools, template, config, atau control yang saya ubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Tidak ada sumber tim untuk baris ini (config/worklist.json: "sources": []; aksi T2) | tidak ada | tidak ada | Alat Drive tidak dimuat dan tidak dipakai. Tidak ada berkas sumber yang gagal dibaca |
| Kriteria penerimaan: config/checklist.json baris 10, Description | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist) | 2026-10-14T17:47:13.611Z (kolom modifiedTime di config/checklist.json) | Dibaca langsung dari berkas repo. Baris 10 tanpa fileId, tanpa acuan klausul ISO (iso_9001 dan iso_27001 null), link_text "On progres" |
| Bahan sesama dokumen (bukan sumber faktual form ini) | specs/HR-ORG-01.json, specs/HR-FRM-01.json, specs/HR-SOP-10.json, specs/HR-SOP-12.json, notes/HR-FRM-01.md | spec lokal, bukan berkas Drive | Dipakai untuk nama jabatan (Tabel 2), tingkatan jabatan, rujukan silang ke FRM-02, dan pola rekaman |
| Bahan asal HR-JA-001 (DATA) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z, angka ini saya salin dari notes/HR-ORG-01.md dan tidak saya ukur ulang | Dibaca lewat salinan context/audit/iso-sinux-supdocs-hr-2026-10-14.md |
| Catatan cacat | context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 718; context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian 5; context/audit/iso-sinux-supdocs-isms-2026-10-14.md | salinan audit 13 sampai 14 Okt | DATA. Lihat bagian Penanganan cacat |

Kalimat perintah di bahan yang saya baca: tidak ada yang ditemukan.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria penerimaan: perencanaan tahunan yang memuat jadwal, jenis pelatihan, dan target peserta menurut jenjang jabatan. Tabel 1 memuat kolom Jadwal rencana, Jenis, dan Sasaran peserta; Tabel 2 memetakan jabatan ke pelatihan | "Dokumen perencanaan tahunan yang mengatur jadwal, jenis pelatihan, dan target peserta pelatihan sesuai jenjang jabatan." | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Persyaratan kontrak pelanggan dan pemahaman SOP serta kerahasiaan informasi ada di Job Analysis. Karena itu "persyaratan kontrak pelanggan" menjadi satu dasar kebutuhan di butir 4.4, dan jenis Keamanan informasi dan mutu memuat pemahaman SOP dan kerahasiaan informasi | "Persyaratan tambahan: memahami SOP dan kerahasiaan informasi, sertifikasi profesi/vendor hanya diwajibkan bila ditetapkan dalam competency matrix atau kebutuhan kontrak pelanggan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Job Analysis hanya mencakup 15 jabatan aktif dan tidak memuat grading. Karena itu Tabel 2 memuat 15 baris JA-01 sampai JA-15, dan butir 4.2 memberi jalan keluar dengan kode jabatan selama tingkatan belum terisi | "Cakupan \| 15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Fakta penting lain dan kutipan verbatim

| # | Fakta di form | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | SNX-HR-SOP-12 menugaskan HR Manager mencatat tindakan pelatihan atas kesenjangan keterampilan di form ini (dasar kebutuhan, butir 4.4 dan 4.9) | "mencatat kesenjangan, dan mencatat tindakan pelatihannya di SNX-HR-FRM-02 (butir 6.5, (USULAN))" | specs/HR-SOP-12.json, butir 4.3 |
| 2 | SNX-HR-SOP-10 menugaskan HR Manager memasukkan tindakan pemenuhan syarat kenaikan jabatan ke form ini | "HR Manager memasukkan tindakan pemenuhan syarat ke SNX-HR-FRM-02 dan melapor ke Direktur Utama saat syarat terpenuhi." | specs/HR-SOP-10.json, tabel pengecualian, baris "Keputusan menyetujui dengan syarat" |
| 3 | SNX-HR-FRM-01 menunjuk form ini sebagai tempat rencana pelatihan tahunan dan matriks pelatihan | "Rencana pelatihan tahunan dan matriks pelatihan" dan "Ada di SNX-HR-FRM-02." | specs/HR-FRM-01.json, tabel Ruang Lingkup |
| 4 | Tingkatan jabatan ditetapkan di FRM-01 dengan ukuran jumlah garis lapor | "HR Manager menetapkan tingkatan dari jumlah garis lapor sampai Direktur Utama (JA-01), sama dengan ukuran di SNX-HR-SOP-12 bagian 3 (USULAN)." | specs/HR-FRM-01.json, butir 4.3 |
| 5 | Tabel 1 FRM-01 (tempat tingkatan) masih kosong, jadi butir 4.2 menyediakan kode jabatan sebagai pengganti | Tabel 1 SNX-HR-FRM-01: kolom Tingkatan berisi sel kosong untuk JA-01 sampai JA-15 | specs/HR-FRM-01.json, Matriks Kompetensi |
| 6 | Jabatan Divisi Operation dikecualikan dari Tabel 2 | "Nama jabatan, jenjang, headcount, dan garis lapor ke COO berstatus USULAN di POL-OPS-001, tanpa pemegang bernama." | specs/HR-ORG-01.json, butir K-10 |
| 7 | SOP Training & Development adalah tempat tata cara identifikasi kebutuhan dan pelaksanaan, jadi dikecualikan dan disebut "dalam peninjauan" | "Tata cara identifikasi kebutuhan pelatihan, pelaksanaan, dan pengembangan kemampuan karyawan secara berkala." | config/checklist.json baris 5 (checked false, link null); config/worklist.json HOLD-T3: "tim menandai ada" |
| 8 | Kehadiran dan evaluasi efektivitas ada di SNX-HR-RPT-01, jadi dikecualikan | "Formulir pencatatan kehadiran serta laporan evaluasi efektivitas pelatihan yang telah diselenggarakan." | config/checklist.json baris 11 |
| 9 | Pelatihan untuk pelanggan dikecualikan: peserta form ini pemegang jabatan SINUX | "Training: hands-on untuk ops team (dashboard, API, troubleshooting)." (pelatihan untuk tim ops milik pelanggan di proses onboarding) | context/audit/iso-sinux-supdocs-commercial-2026-10-14.md baris 649 |
| 10 | Klasifikasi RESTRICTED (Internal) | config/defaults.json: "data karyawan, hukum, keuangan, pelanggan = RESTRICTED (Internal)"; config/worklist.json: "classification": "RESTRICTED (Internal)" | defaults v21, worklist (bukan berkas Drive) |
| 11 | Sebutan "Direktur Utama" di badan dokumen; "COO" tidak dipakai | config/defaults.json data_conflicts: "badan dokumen: 'Direktur Utama' (HR-JA-001), termasuk saat sumber menulis CEO" | defaults v21 |
| 12 | Pola rekaman HR: folder Google Drive Departemen HR, pemilik, retensi belum ditetapkan | "Folder Google Drive Departemen HR (USULAN). Pemilik: HR Manager." dan "Belum ditetapkan" | specs/HR-FRM-01.json, bagian Rekaman |
| 13 | Daftar jabatan di Tabel 2, JA-01 sampai JA-15, dan nama jabatannya | Tabel Daftar Jabatan, kolom Kode dan Jabatan (nama disalin persis, termasuk JA-08 dan JA-09 yang sama-sama "Legal & Compliance") | specs/HR-ORG-01.json |

## 3. Pemetaan klausul ISO

Checklist tidak memberi acuan klausul untuk baris ini. Bagian Acuan Klausul ISO memuat lima baris dengan satu label "(USULAN, perlu konfirmasi konsultan)". Judul klausul adalah pengetahuan standar, bukan teks sumber tim.

| Klausul | Alasan | Catatan |
|---|---|---|
| ISO 9001:2015 7.2 Kompetensi | Rencana pelatihan adalah tindakan memperoleh kompetensi yang diperlukan. Evaluasi efektivitas tindakan tidak ada di form ini, dan kalimat tabel menyebutnya agar form tidak terbaca menutup klausul penuh | Pasangan form ini di FRM-01 (standar kompetensi) dan RPT-01 (evaluasi efektivitas) |
| ISO 9001:2015 7.3 Kesadaran | Jenis Keamanan informasi dan mutu memuat pemahaman SOP dan kerahasiaan informasi | HR-JA-001 bagian 2 juga memakai 7.3 untuk pemahaman karyawan (context/audit hr, bagian 5 butir 15) |
| ISO/IEC 27001:2022 7.2 Kompetensi | Klausul yang sama untuk kinerja keamanan informasi | Tafsir penyusun |
| ISO/IEC 27001:2022 7.3 Kesadaran | Klausul kesadaran terhadap kebijakan keamanan informasi | Tafsir penyusun |
| ISO/IEC 27001:2022 Annex A 6.3 Kesadaran, pendidikan, dan pelatihan keamanan informasi | Jadwal dan sasaran pelatihan keamanan informasi ada di Tabel 1 | Di SoA draf, kontrol 6.3 bertanda "Perlu keputusan" (open item 8). Konsultan perlu menilai |

## 4. Keputusan desain dan tafsir

1. Dua tabel, bukan satu. Tabel 1 berorientasi pelatihan (satu baris per pelatihan: jadwal, jenis, sasaran peserta). Tabel 2 berorientasi jabatan (15 baris dari SNX-HR-ORG-01: kode pelatihan yang ditargetkan). Kriteria menyebut "jadwal, jenis pelatihan, dan target peserta pelatihan sesuai jenjang jabatan", dan "Training Matrix" di judul adalah pemetaan jabatan ke pelatihan.
2. Istilah "tingkatan jabatan" dipakai di seluruh form, bukan "jenjang jabatan" dari kriteria, supaya sama dengan SNX-HR-FRM-01, SNX-HR-SOP-12, dan SNX-HR-ORG-01. Definisi disamakan dengan FRM-01 ("Kelompok jabatan di SNX-HR-ORG-01 yang kedudukannya sama dalam susunan organisasi").
3. Semua sel faktual kosong: Identitas Rencana, 10 baris Tabel 1, serta kolom Tingkatan, Kode pelatihan, dan Keterangan di Tabel 2. Tanpa baris contoh. Kode dan nama jabatan di Tabel 2 bukan data faktual baru: disalin dari SNX-HR-ORG-01 (DONE). Nama pemegang jabatan tidak dimasukkan. Sepuluh baris kosong di Tabel 1 adalah kapasitas tata letak, bukan klaim jumlah pelatihan.
4. Sasaran peserta berhenti di tingkatan jabatan atau kode jabatan, tidak sampai nama karyawan (butir 4.7). Tindakan perorangan dari SNX-HR-SOP-10 dan SNX-HR-SOP-12 masuk sebagai baris dengan kode jabatan sebagai sasaran (butir 7.6). Nama peserta yang hadir dicatat di SNX-HR-RPT-01.
5. Tingkatan di FRM-01 belum terisi, sehingga form ini tidak bisa menunggu. Butir 4.2: selama itu HR Manager menetapkan sasaran dengan kode jabatan JA-nn dan kolom Tingkatan di Tabel 2 dikosongkan.
6. Empat jenis pelatihan (Teknis, Perilaku, Keamanan informasi dan mutu, Sertifikasi profesi atau vendor) tidak ada di sumber. Tiga dari empatnya mengikuti kata di bahan yang ada: kompetensi perilaku dan sertifikasi (FRM-01), pemahaman SOP dan kerahasiaan informasi (JA-001 butir 4.7). Seluruh daftar berlabel USULAN.
7. Lima dasar kebutuhan di butir 4.4 berasal dari dokumen yang saling merujuk (FRM-01, SOP-12, SOP-10) dan dari persyaratan kontrak pelanggan (JA-001). Dasar kelima ("dasar lain") menampung sisanya di kolom Keterangan. Berlabel USULAN.
8. Peran: HR Manager menetapkan, HRGA Officer mencatat, Direktur Utama menyetujui. Satu pengecualian yang dinyatakan: HR Manager mencatat sendiri baris dari SOP-10 dan SOP-12, karena kedua SOP itu menyebut HR Manager sebagai pencatat (butir 4.9 dan 7.6). Nama peran persis seperti di daftar jabatan HR-ORG-01 (HR Manager JA-14, HRGA Officer JA-12, Direktur Utama JA-01).
9. Anggaran, jumlah peserta per pelatihan, dan jam pelatihan minimum tidak diminta kriteria dan tidak ada sumbernya. Anggaran dikecualikan eksplisit di Ruang Lingkup; dua lainnya open item 6 dan 7. Jumlah peserta bisa dihitung dari Tabel 2.
10. Penyelenggara (internal atau eksternal) sempat jadi kolom Tabel 1, lalu dibuang bersama kolom Jumlah peserta karena kolom 9 membuat header terpotong di halaman potret dan keduanya tidak diminta kriteria.
11. Bagian 3 hanya arti istilah. Aturan ada di Dasar dan Ketentuan (butir 4.1 sampai 4.10). Daftar jenis ada di bagian 6 dan hanya ditunjuk dari definisi.
12. Sebutan COO tidak muncul di badan dokumen, jadi aturan "Direktur (COO)" tidak terpakai. JA-02 ditulis "Direktur" seperti di HR-ORG-01. Samuel ditulis "Direktur Utama" di badan dokumen dan "President Director" hanya di blok Approved By.
13. Zammad, GLPI, vault, PPN: tidak relevan untuk form ini dan tidak disebut.
14. Setiap kode dokumen di badan ada di tabel Dokumen Terkait: SNX-HR-ORG-01, SNX-HR-FRM-01, SNX-HR-RPT-01, SNX-HR-SOP-10, SNX-HR-SOP-12, SNX-ISMS-PRO-01, dan SOP Training & Development (belum bernomor). Kode JA-nn, P-nn, dan K-10 adalah penomoran butir atau baris, bukan kode dokumen.
15. Status SOP Training & Development ditulis "dalam peninjauan", bukan "belum ada": checklist baris 5 tidak bertanda dan tanpa tautan, tetapi worklist HOLD-T3 mencatat "tim menandai ada".
16. Bagian Rekaman mengikuti pola FRM-01: lokasi folder Google Drive Departemen HR (USULAN), pemilik HR Manager, retensi "Belum ditetapkan" karena angka retensi tanpa sumber dilarang.

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Anggaran dan biaya pelatihan tidak dimuat di form ini | Ruang Lingkup, tabel pengecualian | Aziz bersama FAT |
| U2 | Kode pelatihan berbentuk P-nn | Definisi, butir 7.5 | Aziz |
| U3 | Selama Tabel 1 FRM-01 belum terisi: sasaran peserta memakai kode jabatan JA-nn dan kolom Tingkatan di Tabel 2 dikosongkan | Butir 4.2 | Aziz |
| U4 | Satu salinan form berlaku untuk satu tahun rencana | Butir 4.3 | Aziz |
| U5 | Lima dasar kebutuhan: standar kompetensi FRM-01, kesenjangan keterampilan sesudah rotasi, syarat kenaikan jabatan, persyaratan kontrak pelanggan, dasar lain | Butir 4.4 | Aziz |
| U6 | Baris sebuah jabatan di Tabel 2 memuat kode pelatihan yang sasarannya sama dengan tingkatan atau kode jabatan itu | Butir 4.6 | Aziz |
| U7 | Sasaran peserta berhenti di tingkatan atau kode jabatan, tanpa nama karyawan | Butir 4.7 | Aziz; Legal untuk sisi data pribadi |
| U8 | Baris Tabel 1 yang sudah disetujui tidak dihapus dan Jadwal rencana tidak diubah | Butir 4.8 | Aziz |
| U9 | HR Lead mencatat sendiri baris dari SOP-10 dan SOP-12; selain itu HRGA Officer mencatat | Butir 4.9, 7.6 | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U10 | Pembagian tugas HR Lead (menetapkan, memeriksa, meninjau), HRGA Officer (mencatat, menurunkan Tabel 2), Direktur Utama (menyetujui) | Bagian Peran | Aziz; Samuel untuk peran penyetuju; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U11 | Empat jenis pelatihan beserta artinya | Bagian Jenis Pelatihan | Aziz |
| U12 | Langkah pengisian 7.1 sampai 7.11 | Bagian Cara Mengisi | Aziz |
| U13 | Lokasi rekaman: folder Google Drive Departemen HR; pemilik HR Lead | Bagian Rekaman | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U14 | SNX-HR-SOP-10 mencatat tindakan pemenuhan syarat kenaikan jabatan di form ini | Dokumen Terkait | Aziz; diubah W9: rujukan dialihkan ke SNX-HR-SOP-10 bagian 9 (LEAD G-3 B4 butir 5) dan ditulis "butir 4.4 dan 4.9 form ini" (R2) |
| U15 | SNX-HR-SOP-12 mencatat tindakan pelatihan atas kesenjangan keterampilan di form ini | Dokumen Terkait | Aziz; diubah W9: rujukan butir ditulis "butir 4.4 dan 4.9 form ini" (R2) |
| U16 | Peninjauan lebih awal bila SNX-HR-FRM-01 atau SNX-HR-ORG-01 berubah (peninjauan tahunan sendiri dari review_period YEARLY) | Kesimpulan | Aziz |
| U17 | Klausul ISO 9001:2015 7.2 dan 7.3, ISO/IEC 27001:2022 7.2, 7.3, dan Annex A 6.3 | Acuan Klausul ISO | Konsultan (SoA dan pemetaan klausul), dicatat Legal |

Jumlah USULAN: 17 butir. Label "(USULAN)" tercetak 17 kali di dokumen, termasuk satu baris istilah di tabel Definisi yang bukan butir, ditambah label "(USULAN, perlu konfirmasi konsultan)" milik U17; hitungan lint "17 butir" adalah angka label itu. Tidak ada angka bisnis tanpa sumber: tidak ada tanggal, retensi, jam pelatihan, jumlah peserta, atau anggaran.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Tingkatan jabatan belum bernilai: Tabel 1 SNX-HR-FRM-01 kosong dan garis lapor JA-03, JA-05, JA-08, JA-10, JA-11, dan JA-14 masih menunggu konfirmasi di SNX-HR-ORG-01 (K-01 sampai K-04). Sasaran peserta berdasarkan tingkatan baru bisa diisi sesudah itu | Aziz, lalu owner untuk garis lapor; diubah W9: JA-03 dan JA-04 kini dua garis tegas ke Direktur dan Direktur Utama (LEAD G-3 A3), tidak menunggu; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu (A4) |
| 2 | Isi Identitas Rencana, Tabel 1, dan Tabel 2 kosong dan menunggu keputusan HR Lead. Tidak ada sumber yang menyebut pelatihan, jadwal, atau sasaran SINUX | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| 3 | SOP Training & Development belum terlihat sebagai berkas (checklist baris 5 tanpa tautan; worklist HOLD-T3 mencatat "tim menandai ada"). Form ini menyebutnya "dalam peninjauan". Periksa ulang saat berkas terlihat dan selaraskan dasar kebutuhan di butir 4.4 | Aziz; LEAD untuk status HOLD |
| 4 | Penyetuju rencana tiap tahun: blok Approved By berisi Direktur Utama (template, D2). Belum diputus apakah tiap salinan tahunan perlu tanda tangan Direktur Utama atau cukup HR Lead | Owner atau Samuel; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| 5 | Retensi dan lokasi salinan tahunan: retensi "Belum ditetapkan", lokasi berlabel USULAN mengikuti pola SOP-10, SOP-12, dan FRM-01 | Legal untuk retensi; Aziz untuk lokasi dan pemilik |
| 6 | Jumlah peserta per pelatihan dan anggaran tidak punya kolom. Bila perlu untuk perencanaan biaya, tambahkan kolom atau tabel | Aziz bersama FAT |
| 7 | Jam pelatihan minimum per karyawan per tahun: tidak ada sumber, tidak ditulis | Aziz |
| 8 | SoA draf menandai Annex A 6.3 "Perlu keputusan", padahal RTP-004 dan RTP-013 memilihnya. Bila 6.3 diputus Berlaku, form ini menjadi rencana pelatihan untuk kontrol itu | Konsultan (SoA) dan owner |
| 9 | Persyaratan kontrak pelanggan yang mewajibkan pelatihan atau sertifikasi tertentu: tidak ada sumber kontrak mana | Aziz bersama Fani untuk jabatan Operation |
| 10 | Rujukan SNX-HR-SOP-10, SNX-HR-SOP-12, dan SNX-HR-FRM-01 cocok dengan isi spec saat ini; periksa ulang bila salah satunya berubah. Kedua SOP menyebut form ini "dalam pengerjaan" | LEAD |
| 11 | Delapan jabatan Divisi Operation masih USULAN tanpa pemegang (HR-ORG-01 K-10) dan dikecualikan dari Tabel 2. Baris ditambah sesudah jabatan disahkan | Owner |
| 12 | data_conflicts yang konfirmasinya belum selesai dan relevan: jabatan Aziz "HR Manager" (konfirmasi: owner atau Aziz) dan ejaan "Samuel Kristanto Utomo" (konfirmasi: owner atau Samuel). Dipakai sesuai kolom "pakai", tidak dipilih ulang | Owner; ditutup W9: jabatan Aziz HR Lead dan ejaan Kristanto berstatus selesai (defaults v22) |
| 13 | process_owner "HR Manager" mengikuti aturan dokumen tanpa sumber (jabatan reviewer departemen), status USULAN di defaults | Aziz; ditutup W9: process_owner kini HR Lead (defaults v22) |

## Penanganan cacat context/audit

Perintah: `grep -n "Annual Training Plan & Trainin" context/audit/*.md`. Hasil: satu baris, context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md:718 ("9. Annual Training Plan & Training Matrix."), butir ke-9 dalam daftar HR. Tidak ada bagian dokumen sendiri dan tidak ada "Catatan kualitas dan celah" (bagian 5) untuk baris ini. Saya membaca bagian 5 pada dokumen HR terkait (HR-JA-001, baris 1232 sampai 1248), sintesis baris 446, dan catatan SoA kontrol 6.3 di dokumen ISMS (baris 2170).

| Cacat | Relevansi | Penanganan |
|---|---|---|
| Tidak ada cacat tercatat untuk dokumen ini | Langsung | Tidak ada yang diperbaiki; dicatat di sini |
| HR bagian 5 butir 2: tidak ada grade, "grading tidak dicantumkan" | Tidak langsung | Tingkatan tidak diambil dari sumber; butir 4.2 memakai kode jabatan selama tingkatan belum terisi (U3). Open item 1 |
| HR bagian 5 butir 13: sertifikasi hanya bila ditetapkan competency matrix atau kontrak pelanggan; masa pengalaman minimum belum ada | Tidak langsung | Sertifikasi ditetapkan di SNX-HR-FRM-01; form ini hanya memuat pelatihan berjenis Sertifikasi profesi atau vendor. Persyaratan kontrak pelanggan jadi dasar kebutuhan (butir 4.4). Masa pengalaman minimum tidak dimuat |
| HR bagian 5 butir 11: ejaan Samuel dan sebutan CEO | Ya | "Samuel Kristanto Utomo" di blok Approved By dan "Direktur Utama" di badan, sesuai defaults |
| HR bagian 5 butir 15: ISO 9001:2015 7.3 dan 7.5 dipakai di JA-001 | Tidak langsung | 7.3 dipakai di Acuan Klausul ISO. 7.5 (informasi terdokumentasi) tidak dipetakan karena kriteria baris ini tidak meminta pengendalian dokumen; Rekaman (lokasi, pemilik, retensi) tetap ada |
| ISMS: kontrol 6.3 "Perlu keputusan" di SoA padahal dipilih RTP-004 dan RTP-013 | Ya | Bukan cacat form ini dan bukan wilayah penyusun (SoA = konsultan). Dicatat sebagai open item 8 |
| Sintesis baris 446: "satu matriks kompetensi dan rekam pelatihan/awareness" | Ya | Checklist memuat tiga baris terpisah (matriks kompetensi, rencana dan matriks pelatihan, laporan kehadiran dan evaluasi), jadi form ini hanya rencana dan matriks pelatihan. Awareness records bukan salah satu dari 88 baris checklist dan tidak dimasukkan |
| HR bagian 5 butir 1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 | Tidak relevan | Menyangkut status, kalimat terpotong, frasa kompetensi, garis lapor, nama unit, peran Finance, dan teks identik di HR-JA-001. Bukan isi form ini |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Tujuan kalimat kedua memakai label "Hasil yang dijaga" dari panduan gaya dan klaim pemakaian oleh auditor, tanpa sumber. Sesama form (HR-FRM-01) sudah menghapus pola ini pada putaran 1. Saya tulis ulang menjadi kalimat biasa tentang isi form.
- Benda berkata kerja manusia: "Kriteria form ini tidak memintanya" dan "kedua SOP itu menugaskan HR Manager". Saya ganti dengan "Tidak termasuk kriteria form ini" dan "sesuai rumusan kedua SOP itu". Di Dokumen Terkait, "menugaskan" diganti "menurut dokumen itu, HR Manager mencatat".
- Pasif tanpa pelaku padahal pelakunya diketahui: butir 4.2 ("ditulis dengan kode jabatan"), 4.4 ("yang ditulis di kolom"), 4.6 ("diturunkan"), 4.8 ("ditulis di kolom"). Semuanya kini menyebut HR Manager atau HRGA Officer, atau memakai kalimat isi ("Baris sebuah jabatan di Tabel 2 memuat ...").
- Satu fakta di dua tempat: aturan perubahan jadwal sempat ada di butir 4.8 dan langkah 7.11 dengan kalimat hampir sama. Butir 4.8 kini hanya larangan menghapus dan mengubah, langkah 7.11 memuat tindakan menulis jadwal baru.
- Istilah ganda: "jenjang" (kriteria) dan "tingkatan" (dokumen lain). Satu istilah, "tingkatan jabatan". "Menulis" dan "mencatat" untuk tindakan yang sama: peran pencatat memakai "mencatat" (7.3, 7.5, 7.6, 7.7), "menulis" hanya untuk isian identitas dan keterangan.
- Yang masih bisa terdengar buatan: langkah 7.1 sampai 7.11 hampir semuanya diawali "HRGA Officer", sesuai RUNBOOK §6a.2 (satu tindakan, satu pelaku); definisi Pelatihan dan arti empat jenis pelatihan bisa ditempel ke perusahaan mana pun. Itu sifat definisi, dan daftar jenis berlabel USULAN. Saya tidak menambah kalimat penjelas.
- Tidak ada pembuka generik, penutup positif, em-dash, en-dash, tebal, tanda kutip penekanan, "tidak hanya ... tetapi juga", atau frasa pengisi. Kesimpulan dua kalimat tanpa pujian. Lint gaya lulus.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: 15 jabatan dan JA-01 sampai JA-15 dari specs/HR-ORG-01.json (bersumber Job Analysis). "P-01, P-02" adalah bentuk penomoran (U2). Sepuluh baris kosong Tabel 1 adalah kapasitas tata letak. K-10 adalah nomor butir di HR-ORG-01. Nomor klausul ISO (7.2, 7.3, Annex A 6.3) adalah pengetahuan standar, berlabel USULAN. Tidak ada tanggal, retensi, jam, jumlah peserta, atau anggaran di dokumen.
- Nama: tiga nama di blok approval dari config/defaults.json. Badan dokumen hanya memuat jabatan, tanpa nama orang. Nama jabatan Tabel 2 dari specs/HR-ORG-01.json. Tidak ada nama baru.
- Sistem: "Folder Google Drive Departemen HR" mengikuti pola FRM-01, SOP-10, dan SOP-12, berlabel USULAN. Zammad, GLPI, dan vault tidak disebut.
- Tanpa sumber langsung: empat jenis pelatihan (U11), lima dasar kebutuhan (U5, tiga di antaranya dari dokumen sesama), pembagian tugas tiga peran (U10), aturan satu salinan per tahun (U4), aturan tanpa nama karyawan (U7), dan seluruh langkah pengisian (U12). Semuanya berlabel USULAN.
- Dikutip dari sumber: pemahaman SOP dan kerahasiaan informasi serta persyaratan kontrak pelanggan (JA-001 butir 4.7); kriteria baris (checklist baris 10); klasifikasi (worklist dan defaults).
- Status "dalam peninjauan" untuk SOP Training & Development tidak diukur ulang di Drive; dasarnya checklist baris 5 dan worklist HOLD-T3. Saya tulis sebagai open item 3 dan tidak menyebutnya "belum ada".

## Sweep

Dasar: /tmp/claude-0/prompts/HR-FRM-02.sweep.txt; temuan pemeriksa di qa/HR-FRM-02.verify.json (data). Hanya butir 1 yang diubah. Fakta, angka, nama, dan struktur lain tetap. Tidak ada label USULAN baru.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1a. Kesimpulan, kalimat 1 | "Form ini berstatus Draft, dan baru dipakai sebagai rencana sesudah HR Manager mengisi Tabel 1 dan Tabel 2 dan Direktur Utama menandatangani blok Approved By." | "Form ini berstatus Draft, dan baru dipakai sebagai rencana sesudah HRGA Officer mencatat Tabel 1 dan Tabel 2 menurut penetapan HR Manager, dan Direktur Utama menandatangani blok Approved By." (sama dengan tabel Peran: HR Manager menetapkan, HRGA Officer mencatat) |
| 1b. Cara Mengisi, kalimat pembuka (lokasi yang sama di temuan pemeriksa) | "Langkah berikut berstatus (USULAN) sampai HR Manager dan Direktur Utama mengesahkan form ini." | "Langkah berikut berstatus (USULAN) sampai Direktur Utama menandatangani blok Approved By." (penyetuju hanya Direktur Utama menurut tabel Peran) |
| 2. Rujukan dokumen FAT bernomor (SNX-FAT-SOP-06, SNX-FAT-REG-01, SNX-FAT-FRM-02) | Tidak ada rujukan ke dokumen FAT di badan dokumen. Satu-satunya "dalam peninjauan" dan "belum bernomor" adalah SOP Training & Development (dokumen HR, bukan FAT); "Accounting & Tax" adalah nama jabatan JA-11 | Tidak diubah. Butir tidak berlaku untuk form ini |

Uji sesudah sweep: render_sop.py lalu lint_doc.py generic = "pass": true (satu warn, 17 label USULAN); validate.py skill docx = "All validations PASSED!"; blankscan.py = "ok 10 HR-FRM-02.docx []".

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 | Process Owner, Reviewed, butir 4.2 dan 4.9, bagian Peran, butir 7.4 sampai 7.11, Identitas Rencana, Tabel 2 JA-14, Rekaman, Kesimpulan, Dokumen Terkait SOP-12 | HR Manager | HR Lead |
| R2 1 | Dokumen Terkait SNX-HR-SOP-12 | Rotation: ... di form ini (butir 4.4 dan 4.9) (USULAN). | Rotation: ... di form ini (butir 4.4 dan 4.9 form ini) (USULAN). Butir 4.4 dan 4.9 milik form ini (SNX-HR-SOP-12 butir 4.4 berisi pemisahan peran dan butir 4.9 masa rotasi). |
| 5 | Dokumen Terkait SNX-HR-SOP-10 | Promotion: menurut dokumen itu, HR Manager mencatat tindakan pemenuhan syarat kenaikan jabatan di form ini (butir 4.4 dan 4.9) (USULAN). | Promotion: menurut bagian 9 dokumen itu (baris Keputusan menyetujui dengan syarat), HR Lead mencatat tindakan pemenuhan syarat kenaikan jabatan di form ini (butir 4.4 dan 4.9 form ini) (USULAN). |
| R2 | Notes USULAN U9, U10, U13 dan open item 2, 4 | HR Manager | HR Lead, dengan catatan "diubah W9" di baris itu |
- SPV tidak ditambahkan: kolom Tingkatan ada di Tabel 2 dan dikosongkan menurut butir 4.2, jadi tidak ada tingkat jabatan yang ditulis; SPV tidak ditambah (diubah R2: alasan lama "dokumen tidak punya kolom tingkat jabatan" tidak tepat).
- A3: dokumen hanya mendaftar JA-03 dan JA-04 sebagai baris Tabel 2; tidak ada garis lapor atau tingkatan yang dihitung. Tidak ada perubahan.
- B4: "SOP Training & Development, dalam peninjauan" sudah seragam di Ruang Lingkup dan Dokumen Terkait; tidak diubah. Rujukan ke SNX-HR-SOP-10 bagian 9 dicek terhadap kerangka: baris Keputusan menyetujui dengan syarat ada dan memuat pencatatan ke SNX-HR-FRM-02. Rujukan "butir 4.4 dan 4.9" di baris SNX-HR-SOP-12 adalah butir form ini (R2: kini ditulis "butir 4.4 dan 4.9 form ini", sama dengan baris SNX-HR-SOP-10); SNX-HR-SOP-12 butir 4.3 dan 6.5 memuat pencatatan ke SNX-HR-FRM-02, jadi baris itu tidak diubah selain jabatan.

Open item ditutup atau diubah (status baris lama diubah di tabel Open items):
- ditutup W9: process_owner HR Manager diganti HR Lead mengikuti defaults v22.
- ditutup W9: konfirmasi jabatan Aziz (HR Lead) dan ejaan Samuel Kristanto Utomo berstatus selesai di defaults v22.
- diubah W9: garis lapor JA-03 dan JA-04 sudah diputus owner; JA-05, JA-08, JA-10, JA-11, JA-14 tetap menunggu konfirmasi.
