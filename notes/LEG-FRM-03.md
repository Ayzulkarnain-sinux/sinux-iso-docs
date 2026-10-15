# Catatan penyusun LEG-FRM-03: Data Protection & Confidentiality Compliance Review

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-FRM-03.json. Mode generic, aksi T1, wave W6, nomor SNX-LEG-FRM-03 (nomor SNX dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class B, doc_type_cover "FORM", doc_type_label "Form". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Line Manager Legal" (sumber tidak punya baris "Pemilik dokumen"; lihat Asumsi 1 dan USULAN U1).

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-FRM-03.json /tmp/pen-LEG-FRM-03/LEG-FRM-03.docx` berhasil tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-FRM-03/LEG-FRM-03.docx generic` memberi `"pass": true`, `"fails": []`, `"warns": ["31 butir (USULAN) menunggu ACC"]` (hasil sesudah sweep 15 Okt; sebelum sweep 29). Lulus pada putaran render pertama; putaran berikutnya hanya memperbaiki tata letak dan bahasa (lihat bagian 4 dan bagian Sweep).
- `python3 -I tools/lint_spot.py tools/lint_doc.py` memberi GAGAL 0.
- Sesudah sweep: `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-FRM-03/LEG-FRM-03.docx` memberi "All validations PASSED!" (606 paragraf), dan `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-FRM-03/LEG-FRM-03.docx` memberi `ok 18 LEG-FRM-03.docx []`.
- Pratinjau PDF (soffice, 17 halaman sebelum sweep, 18 halaman sesudahnya): contact sheet semua halaman, lalu halaman 9, 10, 11, 14, 16 dalam resolusi lebih besar. Sampul, Identity, Revision, Approval, TOC, dan 13 bagian tampil. Dua cacat tata letak ditemukan dan diperbaiki: judul kolom "Pemberitahuan" terpotong di tengah kata (kolom Aspek 3,0 cm diperlebar ke 3,5 cm) dan judul "Target Penyelesaian" di tabel temuan terpotong (kolom diperlebar ke 3,2 cm). Sesudah perbaikan, pencarian teks PDF tidak menemukan kata terpotong.
- Pemeriksaan tambahan atas spec: tidak ada em-dash maupun en-dash; semua kode SNX di badan (11 kode) tercantum di bagian Dokumen Terkait dan sebaliknya; "Direktur (COO)" hanya muncul sekali (aspek F.3, sebutan pertama) dan "COO" tidak dipakai lagi; Samuel di badan ditulis "Direktur Utama" (Kesimpulan); tidak ada nama orang di badan; tidak ada kata "penyusun" sebagai rujukan proses, "dokumen sumber", "sumber tim", atau "draf ini" di badan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Data Protection & Confidentiality Compliance Review (Google Doc, 7304 byte) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 | 2026-10-13T16:56:19.285Z (get_file_metadata di sesi ini; sama dengan prompt; createdTime 2026-10-13T16:08:45.598Z) | read_file_content dengan includeComments true. Tidak ada komentar di berkas. Teks utuh dibandingkan dengan transkripsi context/audit (bagian "LEG-Data-Protection-Confidentiality-Review.md"): sama. Format docx tidak diunduh karena struktur 11 bagian dan 8 tabel sudah terbaca penuh lewat teks |
| Kriteria penerimaan | config/checklist.json baris 44 (dept LEG, checked true) | tidak diukur ulang | Description: "Dokumen berisikan daftar evaluasi kepatuhan terhadap kewajiban pelindungan data pribadi dan kerahasiaan informasi." Kolom iso_9001 dan iso_27001 baris ini null |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, butir K-13), specs/LEG-SOP-01.json (butir 4.21, 4.23, 4.24, 4.27, prosedur 6.7, tabel Dokumen terkait), specs/ISMS-SOP-01.json (3 x 24 jam), specs/ISMS-PRO-01.json (butir 4.3, 4.8, 4.9, 4.10, 4.16), specs/ISMS-SOP-02.json (akses), specs/ISMS-SOP-04.json (berita acara pemusnahan), specs/LEG-SOP-03.json (Kategori 7), notes/LEG-REG-01.md (pola), config/defaults.json v21, config/worklist.json | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah. Kuesioner Keamanan SNX-ISMS-FRM-03 butir 9 dan 10 dibaca dari salinan audit (context/audit isms, baris 607 dan 608), bukan dari xlsx Drive (Open items 9) |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md, bagian LEG-Data-Protection-Confidentiality-Review.md (baris 377 sampai 556, bagian 5 baris 539 sampai 553) | salinan audit 13 Okt 2026 | DATA. Perintah: `grep -n 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 context/audit/*.md` (baris 384 dan 528 file legal, baris 84 file sintesis) |

Frasa bernada perintah di sumber dibaca sebagai isi dokumen yang diperbaiki, bukan instruksi untuk penyusun: "Dasar peninjauan harus diverifikasi dan diperbarui sesuai peraturan yang berlaku serta ruang lingkup kegiatan perusahaan pada saat pemeriksaan dilakukan." dan "checklist sesuai hasil penelaahan." Keduanya dicatat di Open items 14 dan dimasukkan sebagai Ketentuan butir 2 dan Petunjuk Pengisian butir 6.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Dasar kewajiban yang ditinjau: ketentuan hukum, kewajiban kontraktual, dan kebijakan serta prosedur internal. Di dokumen menjadi bagian 1 Tujuan dan Kewajiban di Istilah | "Dokumen ini digunakan untuk meninjau kepatuhan perusahaan dalam mengelola data pribadi dan informasi rahasia berdasarkan ketentuan hukum yang berlaku, kewajiban kontraktual, serta kebijakan dan prosedur internal perusahaan yang relevan." (II. Tujuan) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |
| 2 | Daftar periksa punya enam kelompok (A sampai F) berisi 20 aspek, dan kolom "Hal yang Diperiksa" kosong di semua baris. Di dokumen menjadi bagian 8 (23 aspek, tiga di antaranya tambahan USULAN) | "No. \| Aspek yang Ditelaah \| Hal yang Diperiksa \| Status \| Catatan/Tindak Lanjut" lalu "A. Identifikasi dan Dasar Pemrosesan Data", "B. Akses dan Pengamanan Data", "C. Kerahasiaan Informasi", "D. Transfer Data", "E. Retensi dan Penghapusan Data", "F. Hak Subjek Data dan Penanganan Insiden" dan baris seperti "\|  \| Inventarisasi Data \|  \|  \|  \|" (VI. Daftar Periksa Penelaahan Kontrak) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |
| 3 | Status pemeriksaan baku ada lima, dan hasil dicatat sesuai penelaahan. Di dokumen menjadi Istilah (Status Pemeriksaan) dan kolom Status | "Sesuai \| Persyaratan yang ditinjau telah dipenuhi berdasarkan bukti yang diperiksa." / "Belum Diverifikasi \| Pemeriksaan belum selesai atau bukti pendukung belum tersedia." / "Catatan: checklist sesuai hasil penelaahan." (VII. Keterangan Status Pemeriksaan; kutipan dipotong, tiga status lain: Tidak Sesuai, Perlu Perbaikan, Tidak Berlaku) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |

## 2. Fakta pendukung dan kutipan

Semua kutipan dari fileId 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8; penanda markdown (tanda bintang) dibuang.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan kedua: tiga hal yang dikerjakan peninjauan | "Peninjauan ini bertujuan untuk mengidentifikasi potensi ketidaksesuaian, menilai kecukupan pengaturan dan pelaksanaan pengelolaan data, serta menetapkan tindak lanjut atas temuan yang memerlukan perbaikan." (II. Tujuan) | Bagian 1 Tujuan |
| 2 | Lingkup delapan hal | "Peninjauan mencakup pengelolaan data pribadi dan informasi rahasia dalam kegiatan operasional perusahaan, termasuk apabila relevan:" lalu butir 1 sampai 8, dari "Pengumpulan dan penggunaan data pribadi;" sampai "Pemenuhan kewajiban hukum dan kontraktual terkait pelindungan data." (III. Ruang Lingkup) | Bagian 1 Lingkup, tabel delapan baris |
| 3 | Dasar peninjauan enam butir | "Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi;" / "Peraturan pelaksana terkait pelindungan data pribadi dan sistem elektronik yang berlaku;" / "Persyaratan ISO/IEC 27001 yang relevan dengan ruang lingkup sistem manajemen keamanan informasi perusahaan." (IV. Dasar Peninjauan, butir 1, 3, 6) | Bagian 3 |
| 4 | Inventaris tujuh kolom, satu baris kosong | "No. \| Kegiatan \| Jenis Data/Informasi \| Tujuan Penggunaan \| Unit Kerja/PIC \| Sistem/Lokasi Penyimpanan \| Status Verifikasi" (V. Identifikasi Kegiatan Pengelolaan Data) | Bagian 7, tabel 7.1 dan 7.2 (kolom Klasifikasi ditambah, USULAN U8) |
| 5 | Tabel temuan enam kolom, tiga baris kosong | "No. \| Temuan \| Risiko/Dampak \| Tindakan yang Diperlukan \| PIC \| Target Penyelesaian" (VIII. Ringkasan Temua [sic]) | Bagian 9 |
| 6 | Tiga opsi kesimpulan dan baris rekomendasi | "Tidak ditemukan ketidaksesuaian berdasarkan pemeriksaan dan bukti yang tersedia." / "Ditemukan ketidaksesuaian yang memerlukan tindakan perbaikan." / "Terdapat aspek yang belum dapat disimpulkan karena bukti belum tersedia atau verifikasi belum selesai." dan "Rekomendasi" (IX) | Bagian 10 |
| 7 | Blok persetujuan per tinjauan | "Tahapan \| Nama/Jabatan \| Tanggal \| Tanda Tangan" dengan baris "Disusun oleh", "Diperiksa oleh", "Disetujui oleh" (X) | Bagian 10, tabel Persetujuan Tinjauan |
| 8 | Unit kerja pelaksana | "Unit Kerja \| Legal dan Compliance/IT/Unit Terkait" (I. Identitas Dokumen) | Bagian 5 Peran |
| 9 | Fakta dari dokumen lain: 3 x 24 jam | specs/ISMS-SOP-01.json prosedur 6.6 langkah 3: "Putuskan pemberitahuan kepada subjek data dan lembaga berwenang menurut UU PDP, paling lambat 3 x 24 jam sejak diketahui." (pelaku: COO dan Legal & Compliance menurut roles dan exceptions) | Aspek F.3 |
| 10 | Fakta dari dokumen lain: penanganan RESTRICTED | specs/ISMS-PRO-01.json butir 4.10: "RESTRICTED dibagikan hanya dengan NDA atau kontrak yang berlaku dan persetujuan Pemilik informasi."; butir 4.16: "RESTRICTED dimusnahkan dengan hapus aman, dan kertasnya dihancurkan."; butir 4.3: "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan tingkat yang lebih tinggi." | Aspek C.1, C.3, C.4, E.2 |
| 11 | Fakta dari dokumen lain: pencabutan akses | specs/ISMS-SOP-02.json prosedur Pencabutan Akses langkah 2: "Cabut semua akses paling lambat pada hari terakhir kerja; untuk pemberhentian mendadak, cabut segera." | Aspek B.2 |
| 12 | Fakta dari dokumen lain: Kuesioner Keamanan | context/audit isms baris 607 dan 608: butir 9 "Apakah kontrak memuat klausul kerahasiaan, hak audit, dan kepatuhan UU PDP?" dan butir 10 "Bagaimana proses pengembalian dan penghapusan data saat kontrak berakhir?" | Aspek D.1 dan E.3 |
| 13 | Fakta dari dokumen lain: SNX-LEG-SOP-01 | butir 4.21 "Setiap kontrak atau proyek yang melibatkan data pribadi ditinjau terhadap UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi: dasar pemrosesan, peran (pengendali atau prosesor), kewajiban keamanan, dan notifikasi insiden." dan Dokumen terkait: "SNX-LEG-FRM-03 ... padanan hasil tinjauan pelindungan data pribadi di 6.7 langkah 1 (USULAN)." | Aspek A.3, A.5; Dokumen Terkait |

## 3. Pemetaan kriteria, unsur demi unsur

Kriteria: "Dokumen berisikan daftar evaluasi kepatuhan terhadap kewajiban pelindungan data pribadi dan kerahasiaan informasi."

| Unsur kriteria | Letak di dokumen |
|---|---|
| Daftar evaluasi kepatuhan | Bagian 8 Daftar Evaluasi Kepatuhan: enam tabel (8.1 sampai 8.6), 23 aspek, kolom Hal yang Diperiksa, Status, dan Catatan/Tindak Lanjut; lima status di bagian 2; temuan di bagian 9; kesimpulan di bagian 10 |
| Kewajiban pelindungan data pribadi | Kelompok A, B, D, E, F (tabel "Kewajiban yang diuji" di bagian 8, USULAN U7); aspek A.3, A.5, D.2, F.1, F.3 menyebut kewajiban UU PDP dan SNX-LEG-SOP-01 butir 4.21 |
| Kewajiban kerahasiaan informasi | Kelompok C seluruhnya; aspek B.4, B.5, D.1, E.2 untuk informasi RESTRICTED (Internal) dan SECRET menurut SNX-ISMS-PRO-01 |
| Dasar kewajiban (hukum, kontrak, kebijakan internal) | Bagian 1 Tujuan, bagian 3 Dasar Peninjauan (enam butir), Istilah "Kewajiban" |
| Acuan ISO | Bagian 12, tabel Acuan ISO: 4 klausul ISO 9001:2015 dan 12 baris Annex A ISO/IEC 27001:2022, satu label "(USULAN, perlu konfirmasi konsultan)" |

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | II dan III sumber | Delapan butir lingkup jadi tabel. Pengecualian empat butir ditambah karena sumber diam (USULAN U17) |
| 2 Istilah | Istilah di spec; VII sumber | Arti istilah dan lima status. Aturan ada di bagian 4. Arti data pribadi, subjek data, pemrosesan, pengendali, prosesor berlabel USULAN (U18) |
| 3 Dasar Peninjauan | IV sumber | Enam butir sumber; kolom Diverifikasi Pada ditambah untuk catatan sumber "harus diverifikasi dan diperbarui" (U9) |
| 4 Ketentuan Tinjauan | Catatan IV, V sampai IX sumber, aturan SNX-LEG-SOP-01 dan SNX-ISMS-PRO-01 | 14 butir, satu pelaku per butir. Peran yang menetapkan (Line Manager Legal) dan yang mencatat (Staff Legal) dibedakan di butir 10, 11, 13 |
| 5 Peran | Unit Kerja di I sumber; pola SNX-LEG-SOP-01 | Empat peran. Tugas merujuk nomor butir, tidak menyalin kalimat |
| 6 Petunjuk Pengisian | Kolom tabel sumber; catatan VII | Sepuluh butir tentang isi kolom |
| 7 Inventaris Kegiatan Pengelolaan Data | V sumber | Dipecah dua tabel (7.1 dan 7.2) karena delapan kolom membuat judul terpotong di lebar 16 cm; nomor baris sama |
| 8 Daftar Evaluasi Kepatuhan | VI sumber | Enam tabel menggantikan satu tabel dengan baris judul kelompok. Kode aspek A.1 dan seterusnya mengisi kolom No. yang kosong di sumber |
| 9 Ringkasan Temuan | VIII sumber | Tiga baris kosong bernomor |
| 10 Hasil dan Rekomendasi Tinjauan | IX dan X sumber | Tiga opsi dengan kotak centang, rekomendasi, dan tabel Persetujuan Tinjauan. Tanda tangan dan tanggal kosong |
| 11 Dokumen Terkait | Kode yang disebut di badan | 11 kode, semuanya dirujuk di badan |
| 12 Rekaman dan Acuan ISO | Ketentuan 14; kriteria | Dua rekaman; retensi "Belum ditetapkan" mengikuti SNX-LEG-SOP-01 butir 4.27 |
| 13 Kesimpulan | Status dokumen, review_period | Dua kalimat |

Blok sumber yang tidak dibawa ke badan: I Identitas Dokumen (diganti halaman Identity template), dan XI Riwayat Perubahan (diganti Revision History template, satu baris revisi 00). X Catatan Pemeriksaan dan Persetujuan dibawa sebagai tabel Persetujuan Tinjauan karena form ini diisi per periode, berbeda dari blok Approval template yang mengesahkan form itu sendiri.

Diagram tidak dibuat. Sumber tidak punya diagram (audit membuka halaman 1 sampai 6: hanya teks dan tabel). Diagram mermaid di audit diturunkan dari teks dan pemetaan status ke opsi kesimpulan di sana adalah inferensi audit; pemetaan itu masuk sebagai aturan teks berlabel USULAN di Ketentuan butir 13. Kriteria tidak meminta alur.

## 5. Penanganan cacat context/audit (bagian 5, fileId 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8)

| # | Cacat di audit | Penanganan |
|---|---|---|
| 1 | Template kosong: 7 dari 9 field Identitas kosong, tanpa klasifikasi | Nomor, revisi, status, klasifikasi, penyusun, pemeriksa, penyetuju dari data baris dan halaman Identity template. Tanggal efektif kosong (batas keras 3) |
| 2 | Kolom "Hal yang Diperiksa" kosong di 20 dari 20 aspek; Status tidak terikat ke lima nilai | Diperbaiki: kolom diisi untuk 23 aspek dengan kriteria dari dokumen SINUX lain (USULAN U5). Status diikat ke lima nilai lewat Petunjuk Pengisian butir 6 dan Ketentuan butir 7. Kolom "Checklist" (kotak centang kosong) di tabel keterangan status tidak dibawa; kotak centang dipakai hanya di opsi kesimpulan |
| 3 | Judul Bagian VI "Daftar Periksa Penelaahan Kontrak" menyalin judul checklist kontrak padahal isinya aspek pelindungan data; judul VIII salah ketik "Temua" | Diperbaiki: bagian 8 diberi judul "Daftar Evaluasi Kepatuhan" (frasa kriteria baris) dan bagian 9 "Ringkasan Temuan" |
| 4 | Kelompok D hanya satu baris, tanpa dasar atau lokasi transfer | Diperbaiki: ditambah D.2 Perjanjian Pemrosesan Data dan D.3 Dasar dan Lokasi Transfer (USULAN U6) |
| 5 | Istilah tidak seragam: lingkup F "insiden", kelompok F "Gangguan" | Diperbaiki: satu istilah "insiden" (Istilah "Insiden pelindungan data"). Nama aspek "Penanganan Gangguan" dan "Pemberitahuan Gangguan" ditulis "Penanganan Insiden" dan "Pemberitahuan Insiden" (F.2 dan F.3). Perubahan nama ini tidak diberi label USULAN di dokumen; dicatat di sini dan di Open items 12 |
| 6 | Tidak ada klausul ISO; keterkaitan ke SoA (5.31, 5.34, status "Perlu keputusan") adalah inferensi | Diperbaiki: tabel Acuan ISO di bagian 12 dengan satu label "(USULAN, perlu konfirmasi konsultan)". SoA = konsultan; kode SoA tidak disebut di badan. Open items 8 |
| 7 | Tidak ada baris peran (pengendali atau prosesor) dan perjanjian pemrosesan data, padahal SOP Divisi Legal 4.5 menyebutnya | Diperbaiki: A.5 Peran Pengendali atau Prosesor dan D.2 Perjanjian Pemrosesan Data (USULAN U6), berdasar SNX-LEG-SOP-01 butir 4.21 dan prosedur 6.7 |
| 8 | Baris "Pemberitahuan Gangguan" tanpa batas waktu dan pemutus; SNX-ISMS-SOP-01 menetapkan 3 x 24 jam dan pemutus COO dan Legal | Diperbaiki: F.3 memuat pemutus (Direktur (COO) dan Departemen Legal) dan batas 3 x 24 jam sejak diketahui. Titik awal "sejak diketahui" tidak didefinisikan, mengikuti SNX-ISMS-SOP-01 (Open items 10) |
| 9 | Inventaris tanpa kolom klasifikasi; dokumen tak berlabel dianggap INTERNAL padahal isi terisi bisa RESTRICTED atau SECRET | Diperbaiki: kolom Klasifikasi (USULAN U8), Ketentuan butir 5 (tulis jenis data, bukan isi data, sesuai butir 4.8 PRO-01 yang melarang data SECRET di dokumen), butir 14 (klasifikasi paling rendah RESTRICTED (Internal), USULAN U16). Form berlabel RESTRICTED (Internal) di footer oleh renderer |
| 10 | Tidak merujuk SNX-ISMS-PRO-01 maupun SNX-ISMS-SOP-04; SOP Divisi Legal 4.7 menyisakan retensi "[ISI: periode retensi]" | Diperbaiki: B.3, B.4, C.1, C.3, C.4, E.2 merujuk butir PRO-01 dan SOP-04. Retensi E.1 merujuk SNX-LEG-SOP-01 butir 4.27 dan usulan di SNX-LEG-SOP-03; periode tidak diisi (Open items 5). Kosakata tiga tingkat "Rahasia, Internal, Publik" di SOP Divisi Legal tidak dibawa; dokumen memakai empat tingkat PRO-01 |
| 11 | Tidak merujuk supplier atau SNX-ISMS-FRM-03; Kuesioner butir 9 dan 10 menguji hal yang sama dengan kelompok C dan E | Diperbaiki: D.1 dan E.3 merujuk butir 9 dan 10 Kuesioner Keamanan; SNX-ISMS-FRM-03 di Dokumen Terkait. Masa simpan FRM-03 "Durasi kontrak + 3 tahun" tidak dibawa karena itu retensi rekaman supplier, bukan rekaman form ini |
| 12 | Rujukan regulasi: tanpa UU No. 1 Tahun 2024; PP No. 71 Tahun 2019 dan Peraturan BSSN No. 4 Tahun 2021 disebut Manual M-SMT-01 | Tidak dibawa ke badan. M-SMT-01 berasal dari paket konsultan berisi residu perusahaan lain (RUNBOOK 0 butir 5), dan sintesis audit menilainya tidak boleh dipakai dalam bentuk sekarang. Butir IV.B dan IV.C ditulis seperti sumber, dengan daftar peraturan pelaksana dicatat di SNX-LEG-REG-03 (USULAN U19). Pemutus: Legal, Open items 4 |
| 13 | Tiga dokumen Legal memakai tiga kosakata status | Dipertahankan: lima nilai sumber dipakai apa adanya. Penyelarasan antardokumen bukan wewenang penyusun (Open items 6) |
| 14 | PDF dan teks Drive identik | Tidak ada tindakan |
| Tambahan | Dua nama dokumen: Nama Dokumen "Tinjauan Kepatuhan Pelindungan Data dan Kerahasiaan" dan judul halaman "Data Protection & Confidentiality Compliance Review" | Satu nama, judul di worklist. Nama Indonesia tidak dipakai |
| Tambahan | Sumber memberi nama kelompok Bagian VI "Kewajiban" dan "Penggunaan Informasi" tanpa penjelasan | Nama aspek dipertahankan; C.2 dan C.4 diberi kriteria yang menjelaskan maksudnya (USULAN U5) |
| Tambahan | Ejaan sumber: "Ringkasan Temua" | Dibetulkan menjadi "Ringkasan Temuan". Sumber memakai ejaan baku lain; tidak ada perbaikan ejaan tambahan |

## Asumsi

1. Process owner "Line Manager Legal". Sumber tidak punya baris "Pemilik dokumen"; yang ada "Unit Kerja: Legal dan Compliance/IT/Unit Terkait". Dipakai jabatan reviewer departemen Legal tanpa nama, sama dengan SNX-LEG-REG-01 dan SNX-LEG-SOP-01.
2. Peran dari SNX-HR-ORG-01: "Legal dan Compliance" di sumber dibaca sebagai Departemen Legal (Line Manager Legal dan Staff Legal, JA-08 dan JA-09, pemetaan USULAN butir K-13); "IT" dipetakan ke VP Tech Operation and Services (JA-04), sama dengan pemetaan SNX-LEG-SOP-01; "Unit Terkait" dibuat peran "PIC Unit Kerja" yang didefinisikan di Istilah karena tidak ada padanan jabatan di SNX-HR-ORG-01. Line Manager Legal dan Staff Legal ditulis sebagai nama peran (matriks peran SNX-HR-ORG-01), bukan nama jabatan; jabatannya Legal & Compliance (JA-08, JA-09), pemetaan USULAN U22.
3. Pembagian "Staff Legal menyusun dan mencatat, Line Manager Legal menetapkan dan memeriksa" mengikuti SNX-LEG-SOP-01 butir 4.6 (USULAN di dokumen itu). Sumber tidak menyebut pelaku sama sekali.
4. Hasil tinjauan pelindungan data pribadi di SNX-LEG-SOP-01 prosedur 6.7 langkah 1 dibaca sebagai lembar tinjauan form ini; dokumen itu sendiri menandainya USULAN.
5. Tiket: B.1 menulis "tiket" tanpa nama sistem karena SNX-ISMS-SOP-02 yang dirujuk menetapkan jalurnya (Service Hub GLPI). Zammad untuk Operation dan GLPI untuk generalist (config/defaults.json) tidak bertentangan.
6. Vault tidak disebut. SNX-ISMS-PRO-01 butir 4.8 menyebut tempat SECRET, dan status "menunggu konfirmasi Ops" untuk vault dihindari dengan merujuk butir itu tanpa menamai sistemnya (B.3).
7. PPN dan Samuel: PPN tidak relevan. Samuel muncul di blok Approval "President Director" (data baris) dan di badan "Direktur Utama" (Kesimpulan). Sebutan "Direktur (COO)" dipakai sekali di F.3 karena sumber (SNX-ISMS-SOP-01) menunjuk COO sebagai pemutus pemberitahuan.
8. 23 aspek = 20 aspek sumber + 3 aspek tambahan berlabel USULAN (A.5, D.2, D.3). Angka 23 dihitung dari spec (assert di skrip penyusun).
9. Kolom Status di daftar evaluasi, sel Catatan, tabel inventaris, temuan, rekomendasi, dan tabel Persetujuan Tinjauan kosong. Baris bernomor 1 sampai 3 adalah baris isian kosong, bukan baris contoh.
10. Kolom Diverifikasi Pada di bagian 3 dibiarkan kosong; tanggal verifikasi bukan data yang boleh diisi penyusun.
11. Kriteria "Hal yang Diperiksa" ditulis sebagai keadaan yang diharapkan ("tercatat", "terikat"), supaya status Sesuai berarti keadaan itu terbukti. Kriteria tidak menambah angka di luar 3 x 24 jam dan "hari terakhir kerja" dari dokumen SINUX lain.

## USULAN

Jumlah: 26 butir (U26 ditambah saat sweep). Penanda "(USULAN" di spec: 34 kemunculan (lint menghitung 31 yang berbentuk persis "(USULAN)"); satu butir bisa muncul di beberapa tempat. Satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 12.

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Process owner Line Manager Legal | Identity; Peran | Legal |
| U2 | Pembagian peran Staff Legal (menyusun, mencatat, menyimpan) dan Line Manager Legal (menetapkan, memeriksa, memilih kesimpulan), mengikuti SNX-LEG-SOP-01 butir 4.6; termasuk Line Manager Legal mengisi tahapan Diperiksa oleh | Ketentuan 1 sampai 14; Peran | Legal |
| U3 | VP Tech Operation and Services memberi keterangan teknis untuk kelompok B, dipetakan dari unit IT | Ketentuan 6; Peran | Fani |
| U4 | Periode tinjauan setahun sekali | Ketentuan 1 | Legal |
| U5 | Isi kolom Hal yang Diperiksa untuk 23 aspek | Bagian 8 | Legal |
| U6 | Tiga aspek tambahan: A.5 Peran Pengendali atau Prosesor, D.2 Perjanjian Pemrosesan Data, D.3 Dasar dan Lokasi Transfer | Bagian 8 | Legal |
| U7 | Pemetaan kelompok A sampai F ke kewajiban yang diuji (pelindungan data pribadi, kerahasiaan informasi, atau keduanya) | Bagian 8, tabel pembuka | Legal |
| U8 | Kolom Klasifikasi baru di inventaris | Bagian 7; Petunjuk 3 | Legal |
| U9 | Kolom Diverifikasi Pada baru di Dasar Peninjauan | Bagian 3; Ketentuan 2 | Legal |
| U10 | Kolom Unit Kerja/PIC dan PIC memuat nama jabatan menurut SNX-HR-ORG-01, bukan nama orang | Petunjuk 4 | Legal |
| U11 | Nilai Status Verifikasi: "Sudah diverifikasi" atau "Belum Diverifikasi" | Petunjuk 5 | Legal |
| U12 | Kolom Temuan diawali kode aspek | Petunjuk 8 | Legal |
| U13 | Aspek berstatus Tidak Sesuai atau Perlu Perbaikan dicatat sebagai baris temuan | Ketentuan 10 | Legal |
| U14 | Line Manager Legal menetapkan PIC dan target penyelesaian temuan, Staff Legal mencatat | Ketentuan 11 | Legal |
| U15 | Aturan memilih opsi kesimpulan dari status aspek | Ketentuan 13 | Legal |
| U16 | Lembar terisi disimpan di folder Google Drive departemen Legal dengan klasifikasi paling rendah RESTRICTED (Internal) | Ketentuan 14; Rekaman | Legal |
| U17 | Empat pengecualian lingkup (telaah seluruh klausul kontrak, prosedur insiden, penetapan klasifikasi, penetapan retensi) | Bagian 1 | Legal |
| U18 | Arti data pribadi, subjek data, pemrosesan, pengendali, dan prosesor dalam bahasa sederhana; dicocokkan dengan teks UU PDP | Bagian 2 | Legal |
| U19 | Daftar peraturan pelaksana dicatat di SNX-LEG-REG-03 | Bagian 3 butir 3; Dokumen Terkait | Legal |
| U20 | SNX-LEG-SOP-01 prosedur 6.7 memuat hasil tinjauan yang dicatat di form ini | Dokumen Terkait | Legal |
| U21 | SNX-LEG-FRM-01 dan SNX-LEG-FRM-02 sebagai telaah lengkap kontrak | Bagian 1; Dokumen Terkait | Legal |
| U22 | Pemetaan peran Line Manager Legal dan Staff Legal ke jabatan Legal & Compliance JA-08 dan JA-09 (butir K-13 di SNX-HR-ORG-01) | Peran (paragraf penutup); Dokumen Terkait | owner; ditutup W9: owner 15 Okt memutus pemetaan Legal, label USULAN dan menunggu konfirmasi dihapus |
| U23 | Peran penyetuju lembar tinjauan; Line Manager Legal memutuskannya | Peran | Legal (Line Manager Legal) |
| U24 | Bukti yang diperiksa tetap di sistem asal dengan pemilik PIC Unit Kerja | Rekaman | Legal |
| U25 | Daftar klausul ISO 9001:2015 dan ISO/IEC 27001:2022 | Bagian 12 | owner (konfirmasi lewat konsultan) |
| U26 | Kategori SNX-LEG-SOP-03 untuk lembar tinjauan (Kategori 4 dokumen penelaahan Legal atau Kategori 7 dokumen pelindungan data dan kerahasiaan) dan periode retensinya | Rekaman; Dokumen Terkait | Legal |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Isi kolom Hal yang Diperiksa (U5) dan tiga aspek tambahan (U6) perlu persetujuan sebelum form dipakai. Kriteria disusun dari SNX-LEG-SOP-01, SNX-ISMS-PRO-01, SNX-ISMS-SOP-01, SNX-ISMS-SOP-02, dan SNX-ISMS-FRM-03 yang masih berstatus Draft atau dalam peninjauan; bila dokumen itu berubah, kriteria ikut diperiksa ulang | Legal |
| 2 | Frekuensi tinjauan tidak ada di sumber. Setahun sekali (U4) mengikuti review_period YEARLY; belum ada keputusan | Legal |
| 3 | Peran penyetuju tiap lembar tinjauan tidak ada di sumber (blok "Disetujui oleh" kosong); blok Approval template menyetujui form, bukan lembar. Dokumen menulis Line Manager Legal memutuskannya (U23) | Legal |
| 4 | Peraturan pelaksana UU PDP dan sistem elektronik: apakah UU No. 1 Tahun 2024, PP No. 71 Tahun 2019, dan Peraturan BSSN No. 4 Tahun 2021 (disebut Manual M-SMT-01 menurut audit) masuk SNX-LEG-REG-03. Belum dibawa ke form ini | Legal |
| 5 | Periode retensi dokumen pelindungan data (Kategori 7 di SNX-LEG-SOP-03, usulan 5 tahun) belum ditetapkan dan belum diperiksa terhadap UU No. 27 Tahun 2022. Kategori mana yang berlaku bagi lembar tinjauan (Kategori 4 atau 7) belum diputus (U26). Kolom Retensi di bagian 12 tertulis "Belum ditetapkan" | Legal |
| 6 | Tiga dokumen Legal memakai tiga kosakata status berbeda (audit butir 13). Form ini memakai lima nilai sumber; penyelarasan antardokumen belum diputus | Legal |
| 7 | Jalur penerimaan permintaan hak subjek data (F.1) tidak ditemukan di dokumen SINUX yang dibaca. Kriteria F.1 menanyakan jalur yang SINUX tetapkan; bila belum ada, aspek itu akan berstatus Perlu Perbaikan | Legal |
| 8 | Keterkaitan form ini ke SoA (kontrol 5.31 dan 5.34, status "Perlu keputusan", pemilik ISMS Coordinator menurut audit) adalah inferensi audit. SoA di tangan konsultan; form ini belum dirujuk SoA. Jabatan ISMS Coordinator belum ditetapkan (SNX-HR-ORG-01 butir K-13) | owner; diubah W9: rujukan K-13 pada jabatan ISMS Coordinator tidak lagi berlaku untuk peran Legal; K-13 kini milik peran Finance |
| 9 | Kuesioner Keamanan butir 9 dan 10 dikutip dari salinan audit, bukan dari xlsx SNX-ISMS-FRM-03 di Drive | verifikator |
| 10 | Titik awal "sejak diketahui" untuk 3 x 24 jam belum didefinisikan di SNX-ISMS-SOP-01 (form SNX-ISMS-FRM-02 menghitung dari waktu deteksi menurut notes/ISMS-SOP-01.md); F.3 mengikuti kata SNX-ISMS-SOP-01 | Legal |
| 11 | Tabel temuan (bagian 9) tidak punya kolom status penyelesaian karena sumber tidak punya. Hubungan temuan ke SNX-LEG-RPT-01 (kriteria baris 46: temuan, tindakan perbaikan, penanggung jawab, status penyelesaian) belum ditetapkan | Legal |
| 12 | Nama aspek "Penanganan Gangguan" dan "Pemberitahuan Gangguan" diganti "Insiden" (cacat 5) tanpa label USULAN di dokumen | Legal |
| 13 | SNX-LEG-FRM-01 dan SNX-LEG-FRM-02 sedang disusun lane lain (spec ada di repo, belum diverifikasi). Rujukan form ini memakai judul worklist; cek konsistensi saat verifikasi | verifikator |
| 14 | Dua kalimat sumber bernada perintah ("Dasar peninjauan harus diverifikasi dan diperbarui ..." dan "checklist sesuai hasil penelaahan") diperlakukan sebagai isi dokumen, bukan instruksi, dan dimuat sebagai Ketentuan butir 2 dan Petunjuk butir 6 | Legal |
| 15 | Kriteria memuat "lokasi di luar wilayah Indonesia" (D.3) sebagai contoh lokasi transfer; sumber tidak menyebut transfer lintas negara dan tidak ada fakta SINUX tentang lokasi data | Legal |
| 16 | SNX-LEG-SOP-01 (pemilik memo kepatuhan dan register: Staff Legal) dan SNX-LEG-SOP-03 (pemilik semua kategori dokumen Legal: Line Manager Legal) berbeda soal pemilik rekaman Legal. Form ini mengikuti SNX-LEG-SOP-03; selisih kedua SOP belum diputus | Legal |

## Sweep

Putaran sweep 15 Okt 2026 dari orkestrator WORKER-ISO-01 (instruksi /tmp/claude-0/prompts/LEG-FRM-03.sweep.txt; temuan pemeriksa di qa/LEG-FRM-03.verify.json, verdict PASS, 9 temuan nonblocking). Hanya dua butir yang diubah, yaitu butir 1 dan butir 2 di instruksi; fakta, angka, nama, dan struktur bagian tidak berubah. Satu baris Istilah ditambah (Persetujuan akses) dan satu USULAN ditambah (U26).

| Butir | Letak | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Aspek A.1 | "Semua kegiatan pengolahan data pribadi atau informasi rahasia tercatat di inventaris" | "Semua kegiatan pengelolaan data pribadi atau informasi rahasia tercatat di inventaris", sama dengan istilah terdefinisi "Kegiatan pengelolaan data" |
| 1 | Istilah; aspek B.1 dan B.2 | B.1 "dengan approval yang tercatat"; B.2 "sesuai persetujuan"; tanpa definisi | Baris baru "Persetujuan akses: Izin yang diberikan untuk satu permintaan akses ke sistem, menurut SNX-ISMS-SOP-02."; B.1 dan B.2 sama-sama memakai "persetujuan akses". "Approval" tersisa hanya sebagai nama blok template |
| 1 | Bagian 5, paragraf penutup | "Legal memutuskannya (USULAN)" dan "Jabatan penyetuju lembar tinjauan belum ditetapkan" | "Line Manager Legal memutuskannya (USULAN)" dan "Peran penyetuju lembar tinjauan belum ditetapkan". Pemutus di notes (U23, Open items 3) disamakan dengan dokumen: Legal (Line Manager Legal), sebelumnya tertulis Samuel di notes |
| 1 | Aspek B.4 | "Data RESTRICTED (Internal) dan SECRET dikirim lewat kanal resmi kepada penerima yang berhak, tidak lewat kanal pribadi (SNX-LEG-SOP-01 butir 4.23; SNX-ISMS-PRO-01 butir 4.9)." | "Informasi RESTRICTED (Internal) dan SECRET dikirim hanya lewat kanal resmi, tidak lewat kanal pribadi (SNX-LEG-SOP-01 butir 4.23). Informasi RESTRICTED (Internal) dikirim kepada penerima yang berhak, dan informasi SECRET lewat kanal yang ditetapkan SNX-ISMS-PRO-01 butir 4.9." Butir 4.9 hanya mengatur "penerima yang berhak" untuk RESTRICTED; kanal SECRET lebih ketat |
| 1 | Aspek E.2 | "Data yang melewati masa retensi dihapus aman, kertasnya dihancurkan, dan pemusnahan media dicatat dengan berita acara (SNX-ISMS-PRO-01 butir 4.16; SNX-ISMS-SOP-04)." | "Data RESTRICTED (Internal) dan SECRET yang melewati masa retensi dihapus aman, dan kertas RESTRICTED (Internal) dihancurkan (SNX-ISMS-PRO-01 butir 4.16). Pemusnahan media dicatat dengan berita acara (SNX-ISMS-SOP-04)." Butir 4.16 menetapkan hapus biasa untuk INTERNAL dan penghancuran kertas hanya untuk RESTRICTED |
| 1 | Dokumen Terkait, baris SNX-HR-ORG-01 | "Tempat nama jabatan Line Manager Legal, Staff Legal, dan VP Tech Operation and Services ditetapkan. Line Manager Legal dan Staff Legal dipetakan ke JA-08 dan JA-09 (USULAN, butir K-13)." | "Matriks peran memuat Line Manager Legal dan Staff Legal sebagai peran, dan VP Tech Operation and Services sebagai jabatan JA-04. Butir K-13 memuat pemetaan peran Legal ke jabatan." Label USULAN dan JA-08 dan JA-09 pindah ke bagian 5 (satu tempat) |
| 1 | Dokumen Terkait, baris SNX-LEG-SOP-03; Petunjuk 4 | "Legal" berdiri sendiri: "dokumen penelaahan Legal", "Pemilik rekaman Legal", "Untuk Legal" | "dokumen penelaahan oleh Departemen Legal", "Pemilik rekaman", "Untuk Departemen Legal"; semua memakai istilah terdefinisi. Tidak ada lagi "Legal" tunggal di badan, kecuali sebagai bagian nama peran dan nama dokumen |
| 2 | Bagian 5, paragraf penutup | Pemetaan ke JA-08 dan JA-09 hanya ada di Dokumen Terkait | Kalimat baru di awal paragraf: "Line Manager Legal dan Staff Legal adalah nama peran yang dipetakan ke jabatan Legal & Compliance (JA-08, JA-09) di SNX-HR-ORG-01 (USULAN)." |
| 2 | Petunjuk Pengisian butir 4 | "memuat nama jabatan menurut SNX-HR-ORG-01, bukan nama orang (USULAN)." | "memuat nama peran atau jabatan menurut SNX-HR-ORG-01, bukan nama orang. Untuk Departemen Legal, tulis peran Line Manager Legal atau Staff Legal (USULAN)." |
| 2 | Bagian 5, baris Line Manager Legal | "Pemilik form ini (USULAN)." | "Pemilik form ini (USULAN) dan pemilik rekaman lembar tinjauan menurut SNX-LEG-SOP-03." |
| 2 | Bagian 12, tabel Rekaman, baris lembar tinjauan | "Pemilik: Staff Legal." dan retensi "Belum ditetapkan. Usulan penetapan ada di SNX-LEG-SOP-03." | "Pemilik: Line Manager Legal, mengikuti SNX-LEG-SOP-03." dan retensi "Belum ditetapkan. Kategori SNX-LEG-SOP-03 untuk lembar tinjauan, Kategori 4 atau 7, belum diputus (USULAN)." |
| 2 | Dokumen Terkait, baris SNX-LEG-SOP-03 | "Kategori 7 memuat dokumen pelindungan data dan kerahasiaan. Usulan periode retensinya ada di sana." | Kategori 4 (dokumen penelaahan oleh Departemen Legal, termasuk hasil pemeriksaan kepatuhan) ditambahkan di samping Kategori 7, dan "Pemilik rekaman dan usulan periode retensi ada di sana" |

Alasan penyelarasan pemilik rekaman: SNX-LEG-SOP-03 (specs/LEG-SOP-03.json, tabel Rekaman) menetapkan pemilik Line Manager Legal untuk semua kategori dokumen Legal, termasuk Kategori 4 dan 7; SNX-LEG-SOP-01 menulis pemilik memo kepatuhan dan register Staff Legal. Instruksi sweep memilih SNX-LEG-SOP-03, jadi lembar tinjauan dimiliki Line Manager Legal. Ketentuan butir 14 tetap "Staff Legal menyimpan" karena itu tindakan menyimpan, bukan kepemilikan rekaman. Perbedaan SNX-LEG-SOP-01 dan SNX-LEG-SOP-03 soal pemilik rekaman sendiri tidak diselesaikan di sini (Open items 16). Baris rekaman kedua (bukti yang diperiksa) tetap berpemilik PIC Unit Kerja (USULAN U24) karena bukti tetap di sistem unit asalnya dan bukan rekaman Legal menurut SNX-LEG-SOP-03.

Kategori 4 atau 7: teks SNX-LEG-SOP-03 menempatkan "hasil pemeriksaan kepatuhan" di Kategori 4 ("Sama dengan dokumen yang ditelaah", USULAN) dan "dokumen pelindungan data dan kerahasiaan" di Kategori 7 (usulan 5 tahun). Lembar tinjauan ini memenuhi keduanya, jadi pilihan kategori dan periodenya menjadi USULAN U26 dan tidak diputus penyusun.

Temuan pemeriksa yang sengaja tidak diubah karena di luar butir sweep: kapitalisasi nilai Status Verifikasi dan nilai bersama "Belum Diverifikasi" (Petunjuk 5), narasi "ditambahkan" dan "aspek tambahan" di bagian 3, 7, dan 8, dua tindakan dalam satu butir di Ketentuan 2 dan 11, serta Direktur (COO) di F.3 yang tidak ada di tabel Peran (pemeriksa menilainya dapat diterima). Semuanya tetap tercatat untuk keputusan orkestrator.

Hasil uji sesudah sweep: render berhasil; lint_doc generic pass true, fails kosong, warn "31 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan `ok 18 LEG-FRM-03.docx []`. Pencarian teks: tidak ada em-dash atau en-dash; semua 11 kode SNX di badan ada di Dokumen Terkait; pola benda dengan kata kerja manusia tidak menemukan temuan baru.

## Jawaban dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI, dan apa yang diperbaiki.**

| Temuan | Tindakan |
|---|---|
| Benda menjadi pelaku kata kerja manusia: "Tinjauan mengidentifikasi ... menilai ... menetapkan", "Form ini hanya memeriksa", "Tabel ... mencatat", "Blok Approval ... mengesahkan", "Kelompok C dan D memeriksa", "Kuesioner ... menanyakan", "Butir ... mewajibkan", "Daftar ... untuk mengevaluasi", "Sistem ... mencatat" (sekitar 20 kalimat, sesuai pesan tambahan orkestrator) | Ditulis ulang dengan pelaku peran dari bagian Peran ("Departemen Legal meninjau untuk ...") atau sebagai isi ("Form ini hanya mencakup ...", "Tabel 7.1 dan 7.2 memuat ...", "Pengesahan form ini tercatat di blok Approval"). Pencarian pola benda + kata kerja manusia sesudahnya hanya menemukan satu positif palsu (deskripsi tugas Staff Legal di tabel Peran, pelakunya manusia) |
| Kalimat kriteria A sampai F berpola mirip ("Tiap ... tercatat ...", "dihapus aman, ... dicatat ...") | Sebagian divariasikan (A.1, A.3, B.5). Sisanya dibiarkan karena tiap kalimat memang menyatakan satu keadaan yang dapat dibuktikan; polanya seragam karena fungsinya seragam. Ruang rapi masih ada bila verifikator menilai monoton |
| Penanda "(USULAN)" rapat | Dipertahankan karena RUNBOOK 0 butir 4 dan 6 mewajibkannya. Satu label menutup satu kalimat atau satu tabel, bukan tiap kata |
| Pola "Staff Legal ..." di awal hampir semua butir Ketentuan | Disengaja: satu butir satu pelaku (RUNBOOK 6a butir 1 dan 2) |
| Frasa kosong, penutup generik, kelompok tiga yang dipaksakan, rentang palsu, ekor penegas, lindung nilai bertumpuk | Dicari dan tidak ditemukan; lint gaya lulus tanpa temuan. Kelompok tiga yang tersisa (tiga opsi kesimpulan, tiga status Tidak Sesuai, Perlu Perbaikan, Belum Diverifikasi, daftar jenis data) mengikuti isi sumber |
| Teks bagian 8 panjang karena kolom tabel dijustifikasi di template (celah antarkata lebar di sel sempit) | Kolom Hal yang Diperiksa diperlebar ke 6,1 cm; format template tidak diubah |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber.**

| Butir di dokumen | Sumber | Status |
|---|---|---|
| 3 x 24 jam dan pemutus COO dan Legal (F.3) | specs/ISMS-SOP-01.json (prosedur 6.6, SLA baris 10, roles) | Bersumber; titik awal "sejak diketahui" tidak didefinisikan (Open items 10) |
| "paling lambat pada hari terakhir kerja" (B.2) | specs/ISMS-SOP-02.json, Pencabutan Akses | Bersumber |
| Nomor butir SNX-ISMS-PRO-01 (4.3, 4.8, 4.9, 4.10, 4.16), SNX-LEG-SOP-01 (4.21, 4.23, 4.24, 4.27, prosedur 6.7) | Dicocokkan dengan teks spec masing-masing | Bersumber; bisa basi bila dokumen itu direvisi |
| Kuesioner Keamanan butir 9 dan 10 (D.1, E.3) | Salinan audit isms baris 607 dan 608 | Bersumber dari salinan audit, belum dari xlsx Drive (Open items 9) |
| 23 aspek, 20 dari sumber dan 3 tambahan | Hitungan spec | Terukur; tiga aspek tambahan berlabel USULAN |
| "Setahun sekali" untuk periode tinjauan | Tidak ada di sumber | Berlabel USULAN (U4) |
| Nomor klausul dan judul ISO 9001:2015 dan Annex A ISO/IEC 27001:2022 | Pengetahuan umum atas isi standar, bukan dari berkas repo | Berlabel "(USULAN, perlu konfirmasi konsultan)" (U25) |
| Arti data pribadi, subjek data, pemrosesan, pengendali, prosesor | Bahasa sederhana, bukan kutipan UU | Berlabel USULAN (U18) |
| JA-08, JA-09, butir K-13 | specs/HR-ORG-01.json | Bersumber |
| Nama orang | Hanya Samuel Kristanto Utomo di blok Approval (data baris) | Bersumber; badan tanpa nama orang |
| Tanggal | Tidak ada di dokumen; tanggal efektif, tanda tangan, dan Diverifikasi Pada kosong | Sesuai batas keras 3 |
| "Lokasi di luar wilayah Indonesia" (D.3) | Tidak ada di sumber; contoh generik pada aspek berlabel USULAN | Open items 15 |

Tidak ada kredensial, kata sandi, PIN, atau token di spec atau notes ini.


## ISO-W9

| butir | sebelum | sesudah |
|---|---|---|
| Blok Approval, Prepared By | Staff Legal | Alif Altamziz / Staff Legal |
| Blok Approval, Reviewed By | Line Manager Legal | Ester Febe Utomo / Line Manager Legal |
| Bagian Peran, paragraf penutup | ... (JA-08, JA-09) di SNX-HR-ORG-01 (USULAN). | ... (JA-08, JA-09) di SNX-HR-ORG-01. |
| Dokumen Terkait, baris SNX-HR-ORG-01 | Butir K-13 memuat pemetaan peran Legal ke jabatan. | Line Manager Legal dipetakan ke JA-08 dan Staff Legal ke JA-09. (Rujukan K-13 dihapus: K-13 kini milik peran Finance, bukan Legal.) |
| R2: USULAN U22, notes | baris tanpa penanda W9 | ditambah "ditutup W9" di baris itu (alasan satu baris) |
| R2: Open item 8, notes | baris tanpa penanda W9 | ditambah "diubah W9" di baris itu (alasan satu baris) |

Open item:
- Pemetaan Legal (USULAN K-13 di tabel USULAN dan catatan lama): ditutup W9: owner 15 Okt memutus Line Manager Legal = JA-08 Ester Febe Utomo, Staff Legal = JA-09 Alif Altamziz (LEAD G-3 A5); label USULAN dan menunggu konfirmasi pada pemetaan itu dihapus. USULAN lain tetap.
- A3: dokumen hanya menyebut JA-04 sebagai jabatan VP Tech Operation and Services, tanpa atasan atau garis lapor; tidak diubah.
