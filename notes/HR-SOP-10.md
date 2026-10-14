# Catatan penyusun HR-SOP-10: Promotion

Status: DRAFTED (spec + notes ada). Spec: specs/HR-SOP-10.json. Mode sop, aksi T2, wave W4, nomor SNX-HR-SOP-10 (nomor SNX lama dipertahankan), department "Human Resources", classification "INTERNAL" (worklist), audit_class kosong. Approval persis dari config/defaults.json: prepared "Sita Nadia Salsabila Widodo / HRGA Officer", reviewed "Aziz Priyo Widakdo / HR Manager", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "HR Manager" (jabatan tanpa nama): sumber menulis Process Owner "HR Lead – Aziz Priyo Widakdo" untuk dokumennya sendiri; data_conflicts memutus Aziz = HR Manager.

Hasil uji terakhir (bukti mentah: /tmp/pen-HR-SOP-10/lint.out.txt dan /tmp/pen-HR-SOP-10/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-SOP-10.json /tmp/pen-HR-SOP-10/HR-SOP-10.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-SOP-10/HR-SOP-10.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "35 butir (USULAN) menunggu ACC". Warn PIC SLA nol (semua PIC langkah dan SLA ada di tabel peran).
- Validator OOXML skill docx: "All validations PASSED!". soffice ke PDF: 15 halaman.
- Diagram /tmp/pen-HR-SOP-10/HR-SOP-10_flow.png dilihat: 13 simpul, rankdir TB, satu cabang putus-putus, teks terbaca. Putaran pertama 14 simpul (tinggi 2249 px, tulisan terlalu kecil di halaman); "Kirim rekomendasi" digabung ke simpul HR Manager sebelumnya dan dua pembaruan akhir dibuat sejajar, tinggi jadi 1916 px.
- Pemeriksaan tambahan atas spec (skrip python3 -I di folder scratchpad sesi, bukan di repo): nol em-dash dan en-dash; nol tanda kutip ganda di isi; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir, komersil, diagnosa, hutang) dan nol frasa meta proses (dokumen sumber, sumber tim, penyusun, draf ini); langkah terpanjang 19 kata (batas 25); semua PIC ada di tabel peran bagian 5; semua kode SNX di badan ada di tabel Dokumen terkait.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas config, control, tools, template, reference, ledger.json, out, qa tidak diubah. Berkas yang saya tulis hanya specs/HR-SOP-10.json dan notes/HR-SOP-10.md; hasil render hanya di /tmp/pen-HR-SOP-10/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (sama dengan prompt; get_file_metadata hari ini; induk folder 1o3tZgAiGtUf631zBhOR9KKWmJVebRG6i = Dep. HR) | read_file_content (teks utuh, 15 jabatan). download_file_content tidak dipakai: yang dibutuhkan hanya teks |
| Kriteria penerimaan | config/checklist.json baris 17 ("SOP Promotion", checked false, tanpa link, tanpa kolom ISO) | ekspor 2026-10-14T19:05:35Z, modifiedTime checklist 2026-10-14T17:47:13.611Z | Description: "Prosedur kenaikan jabatan dan tanggung jawab karyawan berdasarkan prestasi dan kualifikasi." |
| Catatan cacat | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian "HR-JA-001" (bagian 5 baris 1232 sampai 1247) | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran dan nama jabatan | specs/HR-ORG-01.json (DONE): daftar jabatan, definisi Atasan langsung, matriks peran, butir K-01 sampai K-14 | repo kerja | dibaca; nama peran dipakai persis |
| Butir rujukan SNX-HR-JA-01 | specs/HR-JA-01.json (DONE): butir 4.4, 4.5, 4.6, 4.7, wewenang JA-08, JA-12, JA-14 | repo kerja | dibaca; nomor butir yang dirujuk di SOP dicocokkan ke teksnya |
| Peran dan alur akses saat perpindahan peran | specs/ISMS-SOP-02.json: definisi "Mutasi", bagian "Perubahan Akses saat Mutasi" | repo kerja | dibaca; bukan sumber Drive |
| Deskripsi baris tetangga | config/checklist.json baris 6, 9, 10, 18, 19, 20; config/worklist.json (nomor SNX-HR-SOP-11, 12, 13, SNX-HR-FRM-01, 02) | repo kerja | dipakai untuk pengecualian lingkup dan Dokumen terkait |
| Pola format | specs/FAT-SOP-05.json, notes/FAT-SOP-05.md (sibling W3) | repo kerja | dibaca sebagai pembanding bentuk, isinya tidak disalin |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat aturan dokumen seperti "Atasan langsung serta bawahan langsung yang belum ditetapkan secara resmi harus dikonfirmasi oleh manajemen sebelum pengesahan" dan "harus diselesaikan sebelum dokumen diberi status Controlled / Effective" mengatur dokumen Job Analysis, bukan pekerjaan saya; tidak dijalankan, dan efeknya tercermin di open item 11.

Temuan utama tentang sumber: SINUX_Job_Analysis_2026.docx tidak memuat prosedur, syarat, atau kriteria kenaikan jabatan. Isinya jabatan, persyaratan, kompetensi, wewenang, dan rujukan ISO. Karena itu baris ini T2 murni: kerangka prosedur diturunkan dari kriteria baris dan dari fakta sumber yang relevan (di bawah), dan seluruh langkah 6.1 sampai 6.4 diberi label (USULAN) di intro butir 6.1.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Prestasi diukur lewat proses manajemen kinerja yang dikendalikan HR: penilaian berkala dan kalibrasi hasil. Dipakai di 4.3 dan butir 6.2 | JA-14 (HR Lead), A. Uraian Jabatan butir 4: "Mengendalikan proses manajemen kinerja, termasuk penyusunan KPI, penilaian berkala, kalibrasi hasil, rencana perbaikan kinerja, dan pengarsipan dokumen." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Kualifikasi dinilai terhadap kompetensi yang ditetapkan, kesenjangan ditindaklanjuti dan dibuktikan; masa pengalaman minimum belum ditetapkan. Dipakai di 4.2 dan butir 6.2 | Bagian 2: "ISO 9001:2015 klausul 7.2: tetapkan kompetensi yang diperlukan, nilai kompetensi aktual, lakukan tindakan jika terdapat kesenjangan, simpan bukti pendukung." Bagian B tiap jabatan: "Masa pengalaman minimum ditentukan setelah job evaluation." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 3 | Keputusan kepegawaian mengikuti persetujuan tertulis; HR hanya merekomendasikan ke approver; jabatan tidak otomatis memberi hak tanda tangan kontrak atau otorisasi keuangan. Dipakai di 4.5, 4.6, tabel peran, butir 6.3 | JA-14 E.4: "Merekomendasikan hiring, salary action, disciplinary action dan policy kepada approver". Batasan umum tiap jabatan: "keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." Bagian 2: "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tanggung jawab dan wewenang harus dikomunikasikan dan dipahami | "ISO 9001:2015 klausul 5.3: tanggung jawab dan kewenangan harus ditetapkan, dikomunikasikan dan dipahami." (Bagian 2) | 4.7, butir 6.4 langkah 1 dan 2, SLA konfirmasi |
| 2 | Cakupan Job Analysis tanpa jabatan kosong dan grading | "15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." (tabel kontrol, baris Cakupan) | Definisi Kenaikan jabatan (kedudukan di SNX-HR-ORG-01, bukan grade); open item 2 |
| 3 | KPI dan targetnya di dokumen lain | "KPI dalam dokumen merupakan usulan indikator, target numerik, bobot dan sumber data ditetapkan pada KPI Matrix terpisah." (Bagian 2) | 4.3, Dokumen terkait |
| 4 | Kompetensi aktual dan kebutuhan kompetensi tiap jabatan ada di tangan HR | "Memastikan kebutuhan kompetensi tiap jabatan telah ditetapkan, kesenjangan kompetensi dievaluasi, serta rencana dan efektivitas pelatihan ditindaklanjuti." (JA-14 A butir 5) | Butir 6.2 langkah 5, pengecualian "Keputusan menyetujui dengan syarat" |
| 5 | HR Manager (di sumber HR Lead) tidak menetapkan, hanya merekomendasikan | JA-14 E.4 (kutipan Fakta kunci 3) | Tabel peran, kolom Authority |
| 6 | HRGA Officer memelihara data, kontrak, personal file; wewenangnya | "Memelihara data karyawan, kontrak, personal file dan administrasi orientasi karyawan baru/proses keluar karyawan." (JA-12 A butir 1); wewenang JA-12: "Meminta kelengkapan data/dokumen", "Memproses administrasi dalam SOP", "Mengeskalasi keputusan HR dan persetujuan ke HR Lead" | Definisi Personal file, tabel peran, butir 6.2 dan 6.4 |
| 7 | HR mengendalikan perubahan data kepegawaian | "Mengendalikan administrasi kepegawaian, termasuk perjanjian kerja, pengelolaan berkas karyawan, orientasi karyawan baru, perubahan data, dan proses pengakhiran hubungan kerja." (JA-14 A butir 3) | Butir 6.4 langkah 3 dan 4 |
| 8 | Legal meninjau kontrak tenaga kerja; wewenangnya | "Melakukan legal peninjauan kontrak pelanggan, vendor, tenaga kerja dan kemitraan." (JA-08 A butir 1); wewenang JA-08: "Memberikan legal clearance/rekomendasi", "Meminta revisi klausul berisiko" | Tabel peran Legal & Compliance (JA-08), bagian 9 |
| 9 | Direktur Utama mengesahkan perubahan organisasi; atasan JA-01 adalah organ perusahaan | "Mengesahkan kebijakan utama, anggaran dan perubahan organisasi sesuai kewenangan korporasi." (JA-01 A butir 6); "Organ perusahaan sesuai ketentuan dan anggaran dasar (verifikasi)" (JA-01 Atasan Langsung) | Dasar USULAN pemberi persetujuan; pengecualian kenaikan ke JA-01 |
| 10 | Kriteria dan deskripsi baris tetangga | Baris 6: "Prosedur standar penilaian kinerja karyawan secara berkala untuk mengukur pencapaian target kerja dan kompetensi." Baris 18: "Prosedur penurunan jabatan atau tingkat posisi akibat penurunan kinerja atau pelanggaran aturan perusahaan." Baris 19: "Prosedur perpindahan tugas/fungsi karyawan dalam tingkatan jabatan yang sama untuk penyegaran atau pengembangan keterampilan." Baris 20: "Prosedur pemindahan karyawan ke unit kerja, divisi, atau lokasi operasional lain sesuai kebutuhan organisasi." (config/checklist.json) | Definisi Penilaian kinerja; Scope: pengecualian |
| 11 | Perubahan akses saat perpindahan peran | Definisi "Mutasi": "Perpindahan peran seseorang." Langkah: "Beri tahu mutasi paling lambat pada hari efektif." (specs/ISMS-SOP-02.json, bukan sumber Drive) | 4.8, butir 6.4 langkah 5, SLA |
| 12 | Kenaikan jabatan mengubah pemegang yang tercatat di dua dokumen | HR-ORG-01 kolom "Pemegang" dan "Melapor ke"; Job Analysis tabel identitas "Pemegang Jabatan" | Butir 6.4 langkah 6 |

## 3. Pemetaan kriteria (Description baris 17)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| Prosedur kenaikan jabatan | Bagian 6, butir 6.1 sampai 6.4; diagram bagian 7; SLA bagian 8; penanganan bagian 9 | Turunan kriteria, USULAN |
| dan tanggung jawab karyawan | Butir 6.4 (uraian jabatan tujuan beserta batas wewenang, konfirmasi karyawan, perubahan hak akses); kebijakan 4.5, 4.7, 4.8; definisi Kenaikan jabatan memuat "tanggung jawab dan wewenang jabatan itu" | JA bagian 2 (5.3), JA-14 E; Fakta pendukung 1 dan 3 |
| berdasarkan prestasi | Kebijakan 4.1 dan 4.3; butir 6.2 langkah 2 dan 3 (hasil penilaian kinerja, kesimpulan prestasi) | JA-14 A butir 4 |
| dan kualifikasi | Kebijakan 4.2; definisi Kualifikasi; butir 6.2 langkah 4 dan 5 (kesimpulan kualifikasi, kesenjangan kompetensi) | JA bagian 2 (7.2), struktur Bagian B sampai D tiap jabatan |

Tafsir: "kenaikan jabatan dan tanggung jawab karyawan" dibaca sebagai kenaikan jabatan beserta tanggung jawab baru yang menyertainya (bukan dua proses terpisah). Bacaan lain, kenaikan tanggung jawab tanpa pindah jabatan, tidak dicakup karena kriteria baris tetangga memberi perpindahan dalam tingkatan yang sama ke SNX-HR-SOP-12. Ini saya catat sebagai asumsi 1.

Klausul ISO (checklist baris 17 tidak memberi acuan; semua satu label "(USULAN, dikonfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur |
|---|---|---|
| ISO 9001:2015 5.3 Peran, tanggung jawab, dan wewenang organisasi | 4.4, 4.5, 4.7 | 6.3, 6.4 langkah 1 dan 2; tabel peran |
| ISO 9001:2015 7.2 Kompetensi | 4.1, 4.2, 4.3 | 6.2 |
| ISO 9001:2015 7.5.3 Pengendalian informasi terdokumentasi | 4.9 | 6.4 langkah 4; tabel rekaman |
| ISO/IEC 27001:2022 Annex A 5.2 Peran dan tanggung jawab keamanan informasi | 4.5 | tabel peran |
| ISO/IEC 27001:2022 Annex A 5.18 Hak akses | 4.8 | 6.4 langkah 5 |

Klausul 5.3, 7.2, dan keterkaitan 7.3 dan 7.5 ada di sumber (bagian 2 Job Analysis). Klausul 7.5.3, Annex A 5.2, dan Annex A 5.18 serta judul semuanya saya tulis dari ingatan tanpa membuka teks standar (tidak diukur ulang di sesi ini); sumber tidak menyebut ISO/IEC 27001 sama sekali (audit butir 15). Klausul 7.3 tidak dibawa karena tidak ada langkah yang mengukur kesadaran selain konfirmasi 4.7, yang saya petakan ke 5.3 seperti kalimat sumber.

## 4. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" HR-JA-001 (fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status DRAF, Revision "03 -", Effective Date "-", nomor "usulan" | Tidak menyangkut SOP ini. Template dan defaults: nomor SNX-HR-SOP-10, Rev 00, Draft, tanggal dan tanda tangan kosong. Job Analysis tetap dirujuk lewat nomor SNX-HR-JA-01 |
| 2 | Tanpa KPI per jabatan, bagan organisasi, grade; posisi kosong tidak dicantumkan | Relevan. KPI: SOP tidak menulis angka KPI, merujuk KPI Matrix (4.3). Grade: definisi Kenaikan jabatan memakai kedudukan di SNX-HR-ORG-01, bukan grade (USULAN, open item 2). Posisi kosong: pengecualian 2 di bagian 9 memuat jabatan tujuan yang belum tercantum |
| 3 | Kalimat terpotong di Bagian 1 paragraf 2 | Tidak dipakai. SOP tidak mengutip Bagian 1 |
| 4 | Frasa kompetensi janggal ("pihak terkait management", "pelanggan communication", "Risk pemahaman karyawan", dan lainnya) | Relevan karena kompetensi jabatan tujuan menjadi dasar kualifikasi. SOP tidak mengutip satu pun frasa kompetensi; ia merujuk SNX-HR-JA-01, yang sudah memulihkan frasa itu (USULAN di dokumen itu). Open item 12 mengingatkan pemeriksaan sebelum SOP dipakai |
| 5 | Pelaporan Manager of Product Tech tidak konsisten | Relevan untuk Atasan Langsung JA-05. Pengecualian 3 di bagian 9: bila kolom Melapor ke berlabel menunggu konfirmasi, Direktur Utama menunjuk Atasan Langsung (USULAN). Open item 11 |
| 6 | Atasan JA-06 dan JA-07 ditulis nama departemen | Tidak menyangkut SOP ini; SNX-HR-ORG-01 sudah memakai "VP Commercial" |
| 7 | Atasan JA-08, JA-10, JA-11, JA-14 tidak satu | Sama dengan butir 5: pengecualian 3 dan open item 11 |
| 8 | Nama unit tidak seragam | Tidak menyangkut SOP ini. Unit tidak disebut di badan; department di meta memakai "Human Resources" (defaults) |
| 9 | Dua jabatan "Legal & Compliance" tanpa pembeda | Relevan untuk peninjauan kontrak. Peran ditulis "Legal & Compliance (JA-08)" di tabel peran, bagian 9, dan Authority, supaya tidak ambigu |
| 10 | Tidak ada jabatan Finance Lead dan Finance Staff | Tidak menyangkut SOP ini; tidak dipakai |
| 11 | Ejaan nama Direktur Utama dan sebutan CEO | Badan dokumen memakai "Direktur Utama"; "President Director" hanya di blok Approved By; ejaan "Kristanto" mengikuti data_conflicts. Tidak ada "CEO". Open item 10 |
| 12 | Teks B dan F identik di 15 jabatan; empat varian pendidikan; tidak ada batas nominal wewenang | Relevan untuk kualifikasi: SOP merujuk persyaratan per jabatan (SNX-HR-JA-01 butir 4.9) tanpa menyalin kalimat. Batas nominal wewenang tidak ada, jadi SOP merujuk Authority Matrix (4.5) |
| 13 | Masa pengalaman minimum dan sertifikasi belum ada | Relevan langsung. Kebijakan 4.2 menyatakan masa itu ditentukan sesudah job evaluation dan memberi jalan sementara (USULAN). Open item 3 |
| 14 | Selisih jumlah tabel 34 lawan 17 | Tidak menyangkut SOP ini |
| 15 | Rujukan ISO: 7.3 dan 7.5 hanya padanan standar; tidak ada ISO/IEC 27001 | Relevan: ISO/IEC 27001 ditambahkan berlabel USULAN (bagian 3 di atas) |

Cacat tambahan yang saya temukan: sumber menyebut "approver" dan "Management / Authorized Director" tanpa menyebut siapa yang menyetujui kenaikan jabatan; ini menjadi USULAN U2 dan open item 4.

Aturan lintas dokumen dari RUNBOOK §6 yang tidak terpicu: tiket (HR bukan Ops; langkah akses memakai SNX-ISMS-SOP-02, yang memuat Service Hub (GLPI)), vault, PPN, Fani, sebutan COO (badan memakai "Direktur Utama"; "Direktur" tidak disebut sama sekali), backup. Sumber tidak memuat rujukan internal AI; tidak ada yang dibuang.

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kriteria dibaca sebagai kenaikan jabatan beserta tanggung jawab baru (lihat bagian 3).
2. Pemisahan peran: Atasan Langsung mengusulkan; HRGA Officer memeriksa kelengkapan dan melampirkan bahan (wewenang JA-12: meminta kelengkapan dokumen, memproses administrasi); HR Manager menyimpulkan dan merekomendasikan (pola JA-14 E.4 untuk hiring, salary action, disciplinary action); Direktur Utama memutuskan; HRGA Officer mencatat. "Menetapkan" (Direktur Utama) dan "mencatat" (HRGA Officer) dibedakan di 4.4, tabel peran, bagian 6, dan tabel rekaman.
3. Bahan penilaian kinerja diambil dari arsip HR (JA-14 butir 4 menyebut pengarsipan dokumen manajemen kinerja). Isi SOP Performance Appraisal tidak saya baca (open item 8).
4. Kenaikan jabatan diperlakukan seperti pengangkatan dalam kalimat "Batasan umum": memerlukan persetujuan tertulis. Sumber tidak menyatakan kenaikan jabatan termasuk di situ (USULAN, 4.6).
5. Pemberitahuan perubahan jabatan untuk hak akses dipegang HRGA Officer: SNX-ISMS-SOP-02 menyebut "HR atau atasan langsung" tanpa menunjuk peran. Batas "paling lambat pada tanggal berlaku" disalin dari "paling lambat pada hari efektif" di dokumen itu; istilah disamakan menjadi "tanggal berlaku" supaya satu istilah untuk satu hal.
6. Kode SNX-HR-SOP-11, 12, 13, SNX-HR-FRM-01, 02 dari config/worklist.json; SNX-ISMS-SOP-02, SNX-ISMS-PRO-01, judulnya, dan istilah "Mutasi" dari specs/ISMS-SOP-02.json dan specs/HR-ORG-01.json. Isi FRM-01 dan FRM-02 belum ada (W7); keterangan di tabel Dokumen terkait hanya deskripsi checklist baris 9 dan 10 ("On progres" di kolom tautan, ditulis "dalam pengerjaan").
7. Berkas tim SOP Performance Appraisal ditandai TRUE di checklist baris 6 dengan tautan; tanpa nomor SNX di worklist. Di tabel Dokumen terkait ditulis "SOP Performance Appraisal" dengan keterangan "Dalam peninjauan" dan kode mengikuti hasil peninjauan; tidak ditulis "belum ada".
8. Definisi Hari kerja dan Personal file adalah penjelasan saya. "Hari libur resmi" tidak ada di sumber SOP ini; konsep yang sama ada di Peraturan Perusahaan Pasal 22 menurut notes/HR-JA-01.md (berkas itu tidak saya buka).
9. Bagian 4 dan 6 tidak menyebut tiket HR. Sumber tidak menyebut tiket untuk proses HR, dan batas "generalist" belum dirinci owner; tidak ada alur tiket yang saya tambahkan.

## USULAN

Label di dokumen: 35 kemunculan "(USULAN)" (lint). Dikelompokkan menjadi 19 butir keputusan di bawah, dengan pemutus yang disarankan.

| # | Butir USULAN | Letak | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Seluruh kerangka prosedur 6.1 sampai 6.4 (usulan, penilaian, persetujuan, penyerahan tanggung jawab); sumber tidak memuat prosedur kenaikan jabatan | Intro butir 6.1; diagram | Aziz |
| U2 | Direktur Utama memutuskan; HR Manager hanya merekomendasikan; kenaikan jabatan berlaku hanya sesudah keputusan tertulis | 4.6, tabel peran, butir 6.3 | Samuel |
| U3 | Batas waktu 3, 5, 5, dan 2 hari kerja, serta konfirmasi karyawan sebelum tanggal berlaku | Bagian 8 | Aziz, lalu Samuel |
| U4 | Hari kerja tidak termasuk hari libur resmi | Definisi | Aziz |
| U5 | Pengalaman dinilai dari kalimat persyaratan pendidikan dan pengalaman sampai masa pengalaman minimum ditetapkan; SNX-HR-FRM-01 sebagai acuan tambahan bila sudah disahkan | 4.2, Dokumen terkait | Aziz |
| U6 | Ambang hasil penilaian kinerja ditetapkan Direktur Utama atas usulan HR Manager, lalu SOP direvisi | 4.3, Kesimpulan | Samuel |
| U7 | Pengecualian lingkup: penetapan gaji dan tunjangan di jabatan baru; kenaikan ke JA-01 | Bagian 2 | Aziz (gaji), Samuel (JA-01) |
| U8 | Konfirmasi tertulis karyawan atas uraian jabatan tujuan, dan penundaan tanggal berlaku bila belum dikonfirmasi | 4.7, butir 6.4, bagian 9 | Aziz |
| U9 | Perubahan jabatan diperlakukan sebagai perpindahan peran di SNX-ISMS-SOP-02; HRGA Officer memberi tahu Atasan Langsung | 4.8, butir 6.4 langkah 5 | Fani (pemilik alur akses), Aziz |
| U10 | Rekaman berklasifikasi RESTRICTED (Internal) | 4.9 | Aziz |
| U11 | Lokasi rekaman: personal file di folder Google Drive Departemen HR; pemilik HRGA Officer | Bagian 11 | Aziz |
| U12 | Retensi: selama karyawan bekerja di SINUX | Bagian 11 | Aziz, Legal |
| U13 | Pemegang jabatan di SNX-HR-ORG-01 dan SNX-HR-JA-01 diperbarui lewat revisi; jabatan tujuan yang belum tercantum ditambahkan lewat revisi yang disahkan Direktur Utama | Butir 6.4 langkah 6, bagian 9 | Aziz, Samuel |
| U14 | Direktur Utama menunjuk Atasan Langsung bila garis lapor berlabel menunggu konfirmasi | Bagian 9 | Samuel |
| U15 | Peninjauan Legal & Compliance (JA-08) atas perubahan perjanjian kerja | Tabel peran, bagian 9 | Legal |
| U16 | Persetujuan dengan syarat: HR Manager memasukkan tindakan ke SNX-HR-FRM-02 dan melapor sebelum data diperbarui | Bagian 9, Dokumen terkait | Aziz |
| U17 | Cara memeriksa kepatuhan: membandingkan rekaman dengan langkah dan batas waktu | Kesimpulan | Aziz |
| U18 | "Kenaikan jabatan" = ke jabatan yang kedudukannya lebih tinggi dalam SNX-HR-ORG-01 (tanpa grading) | Definisi | Aziz, owner |
| U19 | Acuan klausul ISO 9001:2015 5.3, 7.2, 7.5.3 dan ISO/IEC 27001:2022 Annex A 5.2, 5.18 | Bagian 11 | konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Sumber tidak memuat prosedur atau kriteria kenaikan jabatan SINUX. Seluruh bagian 6 adalah usulan; bila HR sudah punya praktik tertulis atau kebiasaan, ganti usulan dengan itu | Aziz |
| 2 | Tidak ada grading atau jenjang jabatan ("grading tidak dicantumkan"), sehingga "jabatan yang lebih tinggi" hanya terbaca dari garis lapor. Bila grading disusun, ubah definisi Kenaikan jabatan | Aziz, owner |
| 3 | Ambang hasil penilaian kinerja minimum dan masa pengalaman minimum belum ada (menunggu job evaluation dan KPI Matrix) | Aziz, Samuel |
| 4 | Pemberi persetujuan: Authority Matrix belum ada, dan sumber hanya menulis "approver" dan "Management / Authorized Director". Direktur Utama diusulkan; belum diputus apakah Direktur (JA-02) menyetujui untuk jabatan di bawahnya | Samuel |
| 5 | Kenaikan gaji atau tunjangan yang menyertai kenaikan jabatan: dokumen mana yang mengaturnya (berkas tim SOP Payroll Process tidak saya buka). SOP ini mengecualikannya | Aziz, FAT |
| 6 | Perlu atau tidaknya perubahan perjanjian kerja untuk kenaikan jabatan, dan siapa menandatangani | Legal |
| 7 | Benturan peran tidak diatur karena sumber tidak punya kontrol pengganti: HR Manager adalah atasan langsung HRGA Officer; bila HRGA Officer atau HR Manager yang diusulkan, orang yang sama bisa mengusulkan, menilai, dan mencatat usulannya sendiri | Samuel, Aziz |
| 8 | Isi berkas tim SOP Performance Appraisal (fileId dari checklist baris 6: 1bHeaK1uX6PcmrKmjB3zr2CdBk9rg5AN6) tidak dibaca. Istilah penilaian kinerja, skala nilai, dan lokasi arsip diambil dari deskripsi checklist; cocokkan sesudah peninjauan, dan beri kode dokumennya di tabel Dokumen terkait | Aziz |
| 9 | Bentuk usulan kenaikan jabatan: form khusus tidak ada dan di luar 88 baris checklist, jadi SOP menyebut "usulan tertulis" tanpa kode. Perlu form atau tidak | Aziz (bila perlu, catat di reports/PROPOSALS.md oleh LEAD) |
| 10 | Konfirmasi data_conflicts yang dipakai di dokumen ini: ejaan "Kristanto" (owner atau Samuel) dan jabatan Aziz "HR Manager" lawan "HR Lead" di sumber (owner atau Aziz) | owner |
| 11 | Garis lapor berlabel menunggu konfirmasi di SNX-HR-ORG-01 (K-01 sampai K-05) menentukan siapa Atasan Langsung JA-01, JA-03, JA-05, JA-08, JA-10, JA-11, JA-14 | Samuel, owner |
| 12 | Frasa kompetensi rusak di sumber dipulihkan oleh SNX-HR-JA-01 (USULAN di dokumen itu) dan menjadi dasar kualifikasi; HR Manager perlu mengonfirmasi pemulihan itu sebelum SOP dipakai | Aziz |
| 13 | SNX-HR-FRM-01 dan SNX-HR-FRM-02 dirujuk padahal baru dikerjakan di W7; periksa kecocokan rujukan setelah keduanya jadi | LEAD |
| 14 | Pemetaan "HR" di SNX-ISMS-SOP-02 ke HRGA Officer dan istilah "hari efektif" lawan "tanggal berlaku" perlu disamakan bila SNX-ISMS-SOP-02 direvisi | Fani |
| 15 | Nomor dan judul klausul ISO dari ingatan, tidak diukur terhadap teks standar | konsultan |
| 16 | Retensi rekaman kepegawaian sesudah karyawan keluar dan lokasi personal file yang sebenarnya (Drive atau lain) | Aziz, Legal |

## 6. Dua pertanyaan penutup

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan saat membaca ulang teks yang dirender, dan perbaikannya:
- Kurung bersarang "(butir 6.4, (USULAN))" muncul empat kali karena label disisipkan mekanis. Diperbaiki menjadi "(butir 6.4) (USULAN)".
- Kalimat Purpose kedua membuka dengan "Hasil yang dijaga:", frasa dari RUNBOOK yang tidak dipakai orang HR. Diganti kalimat biasa.
- Pola "setujui, setujui dengan syarat, atau tolak" dan pembagian empat peran di 4.4 terbaca seperti kelompok tiga yang dipaksakan. Saya cek: keduanya berasal dari struktur proses (tiga hasil keputusan, empat pelaku nyata), jadi dipertahankan, bukan dihias.
- Sisa yang masih terasa mesin dan sengaja dipertahankan: 35 label "(USULAN)" (aturan RUNBOOK §0 butir 4), seragamnya pola "Judul (ISO ...): kalimat" di butir 4.1 sampai 4.9 (mengikuti pola dokumen W3), dan kalimat 5 sampai 20 kata yang rata. Itu wajar untuk SOP, tetapi pembaca akan merasakannya.
- Dua baris pengecualian hasil penalaran saya sendiri (pengganti peran bila yang diusulkan HRGA Officer atau HR Manager, dan alur kerja bila Atasan Langsung belum jelas) saya periksa terhadap aturan "kontrol pengganti hanya bila ada di sumber": yang pertama dihapus dari dokumen dan menjadi open item 7; yang kedua dipertahankan karena tanpa itu lima jabatan tidak bisa menjalankan langkah 6.1 (berlabel USULAN, open item 11).
- Tidak ada pembuka generik, kata kosong, em-dash, atau en-dash di dokumen; lint dan pemeriksaan tambahan menyatakan nol temuan.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: 3, 5, 5, dan 2 hari kerja di bagian 8 tidak punya sumber; semuanya berlabel (USULAN) (U3). "Paling lambat pada tanggal berlaku" berasal dari SNX-ISMS-SOP-02, bukan dari Job Analysis; dipakai pada lingkup yang sama (pemberitahuan perubahan peran). Tidak ada angka lain, tidak ada tanggal, tidak ada nilai uang.
- Nama: hanya blok Approval (dari config/defaults.json). Badan dokumen memakai peran: HR Manager, HRGA Officer, Direktur Utama, Atasan Langsung, Karyawan yang diusulkan, Legal & Compliance (JA-08). "Karyawan yang diusulkan" dan "Atasan Langsung" bukan jabatan di SNX-HR-ORG-01; "Atasan Langsung" didefinisikan dengan kolom Melapor ke dokumen itu.
- Tanpa sumber langsung dan berlabel USULAN: Direktur Utama sebagai pemberi persetujuan (U2); seluruh kerangka langkah (U1); lokasi, pemilik, retensi, dan klasifikasi rekaman (U10 sampai U12); klausul ISO (U19); pengecualian lingkup (U7).
- Tanpa sumber langsung dan tidak berlabel, perlu dicek verifikator: (a) kode SNX-HR-SOP-11, 12, 13 dan SNX-HR-FRM-01, 02 (dari worklist, bukan dari berkas Drive); (b) definisi Personal file dan Penilaian kinerja (dari deskripsi checklist dan JA-12, bukan berkas SOP Performance Appraisal); (c) rujukan butir 4.4, 4.5, 4.6, 4.7 pada SNX-HR-JA-01 (dicocokkan ke specs/HR-JA-01.json, bukan ke dokumen yang sudah di-render); (d) kode wewenang JA-08, JA-12, JA-14 (dari sumber dan HR-ORG-01).
- Tidak ada kata sandi, token, atau kredensial di berkas mana pun; nama sistem yang disebut hanya Google Drive.
