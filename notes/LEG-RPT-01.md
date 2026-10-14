# Catatan penyusun LEG-RPT-01: Legal Compliance Monitoring & Corrective Action Report

Status: DRAFTED. Spec: specs/LEG-RPT-01.json. Mode generic (doc_type_cover "REPORT", doc_type_label "Report"), aksi T1, wave W6, nomor SNX-LEG-RPT-01 (nomor lama dipertahankan), department Legal, classification "RESTRICTED (Internal)", audit_class C2, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". process_owner "Line Manager Legal": sumber tidak memuat butir "Pemilik dokumen", sehingga dipakai jabatan reviewer departemen (config/defaults.json process_owner.rule), tanpa nama.

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-RPT-01.json /tmp/pen-LEG-RPT-01/LEG-RPT-01.docx` berhasil.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-RPT-01/LEG-RPT-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "30 butir (USULAN) menunggu ACC".
- Pratinjau PDF lewat soffice, 14 halaman: sampul, Identity, Revision, Approval, TOC, sembilan bagian. Tabel 7 kolom (Daftar Periksa Pemantauan, Rencana Tindakan Perbaikan) dilihat pada resolusi 70 dpi dan lebar kolom disetel sampai judul kolom tidak patah, kecuali "Vendor/Pemasok" pada sel M4 yang patah satu kali (kosmetik).
- Pemeriksaan tambahan atas spec: nol em-dash dan en-dash, nol "COO" (tidak dibutuhkan di badan dokumen), "Samuel" hanya di blok Approval, "Direktur Utama" satu kali (Kesimpulan), tiap kode SNX yang dirujuk di badan ada di bagian Dokumen Terkait, nol frasa yang dilarang pada daftar mutu bahasa.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Legal Compliance Monitoring & Corrective Action (Google Doc, 7098 byte) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA | 2026-10-14T04:03:12.671Z (get_file_metadata hari ini, sama dengan prompt; createdTime 2026-10-14T03:21:14.656Z) | read_file_content dua kali (satu dengan includeComments true; tidak ada penanda komentar di isi). download_file_content tidak dipakai karena berkas Google Doc berteks lengkap dan struktur tabelnya terbaca utuh; tidak ada docx atau xlsx |
| Kriteria penerimaan | config/checklist.json baris 46 (dept LEG, "Legal Compliance Monitoring & Corrective Action Report", checked true) | tidak diukur ulang | Kolom Description: "Laporan pemantauan kepatuhan yang mencakup temuan, tindakan perbaikan, penanggung jawab, dan status penyelesaian." Kolom iso_9001 dan iso_27001 baris ini null |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, K-13), specs/LEG-SOP-01.json, specs/LEG-SOP-02.json, specs/LEG-SOP-03.json, specs/LEG-FRM-01.json (gaya dan istilah Legal), config/defaults.json v21, context/audit (bagian Legal Risk Register, fileId 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA) | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah. Spec LEG-REG-02, LEG-FRM-02, LEG-FRM-03, LEG-REG-03, LEG-RPT-02 belum ada di specs/ saat disusun |

Pemetaan kriteria ke isi dokumen:

| Unsur kriteria | Letak di dokumen |
|---|---|
| Temuan | Bagian 6.2 Daftar Periksa Pemantauan (kolom Status dan Catatan/Temuan), bagian 6.3 Catatan Temuan |
| Tindakan perbaikan | Bagian 6.3 (baris Tindakan Perbaikan), bagian 6.4 Rencana Tindakan Perbaikan |
| Penanggung jawab | Bagian 6.3 (baris Penanggung Jawab), bagian 6.4 (kolom Penanggung Jawab), bagian 4 Peran |
| Status penyelesaian | Bagian 6.3 (baris Status Tindak Lanjut, Hasil Verifikasi, Tanggal Penutupan), bagian 6.4 (kolom Status Tindak Lanjut), nilai status di bagian 2.2 |

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Catatan temuan dibuat per ketidaksesuaian atau potensi risiko, dan memuat tindakan, penanggung jawab, target, serta status. Di dokumen menjadi bagian 6.3 dan 6.4 | "Bagian ini diisi untuk setiap ketidaksesuaian, kekurangan, atau potensi risiko yang memerlukan tindak lanjut." dan baris tabel "Tindakan Korektif", "Penanggung Jawab", "Target Penyelesaian", "Status Tindak Lanjut" (bagian "Daftar Temuan dan Tindakan Perbaikan") | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |
| 2 | Kesimpulan wajib berbukti, dan bukti yang belum ada tidak boleh menghasilkan status terpenuhi. Di dokumen menjadi Ketentuan butir 4 | "Setiap kesimpulan harus didukung oleh bukti yang dapat ditelusuri. Apabila bukti belum tersedia atau belum diperiksa, status pemenuhan tidak boleh dinyatakan telah terpenuhi." (Metode Pemantauan) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |
| 3 | Status pemantauan punya lima nilai, dan Tidak Berlaku wajib beralasan. Di dokumen menjadi bagian 2.2 dan Ketentuan butir 2 | "Belum Diverifikasi" dengan arti "Bukti belum cukup untuk menyimpulkan status kepatuhan." dan "Tidak Berlaku" dengan arti "Kewajiban tidak relevan terhadap ruang lingkup yang diperiksa, sertai alasan." (Petunjuk Pengisian Status) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |

## 2. Fakta pendukung dan kutipan

Semua kutipan dari fileId 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA. Penanda markdown dan garis miring terbalik di keluaran alat dibuang.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "Laporan ini disusun untuk mendokumentasikan hasil pemantauan kepatuhan hukum perusahaan, mengidentifikasi ketidaksesuaian atau potensi risiko hukum, serta menetapkan tindakan perbaikan dan pencegahan yang diperlukan." dan "membantu menjaga efektivitas penerapan Sistem Manajemen Keamanan Informasi (SMKI), sepanjang relevan dengan ruang lingkup pemantauan." | Bagian 1.1 |
| 2 | Tujuh aspek ruang lingkup | "Pemenuhan perizinan dan legalitas perusahaan." / "Kepatuhan terhadap peraturan perundang-undangan yang berlaku." / "Pemenuhan kewajiban kontraktual dengan pelanggan, vendor, pemasok, dan mitra." / "Pelindungan data pribadi dan kerahasiaan informasi." / "Pemenuhan kewajiban hukum terkait keamanan informasi." / "Kepatuhan terhadap kebijakan dan prosedur internal." / "Tindak lanjut atas temuan pemantauan atau audit sebelumnya." | Bagian 1.2 tabel M1 sampai M8 |
| 3 | Aspek tidak relevan | "Aspek yang tidak relevan dengan kegiatan atau ruang lingkup perusahaan dapat dinyatakan tidak berlaku dengan disertai alasan yang memadai." | Ketentuan butir 2 |
| 4 | Enam metode | "Pemeriksaan dokumen dan catatan perusahaan." / "Penelaahan peraturan perundang-undangan dan perubahan regulasi." / "Pemeriksaan status perizinan dan kewajiban pelaporan." / "Penelaahan kontrak dan dokumen pendukung." / "Wawancara atau konfirmasi kepada unit kerja terkait." / "Pemeriksaan bukti pelaksanaan tindakan perbaikan sebelumnya." | Ketentuan butir 3 |
| 5 | Kolom daftar periksa | "No.", "Aspek yang Dipantau", "Kewajiban/Kriteria Kepatuhan", "Dasar Hukum/Dokumen Acuan", "Bukti yang Diperiksa", "Status", "Catatan/Temuan" | Bagian 6.2 |
| 6 | Tujuh baris aspek di tabel sumber | "Perizinan Perusahaan", "Kepatuhan Regulasi", "Kontrak Customer", "Kontrak Vendor/Pemasok", "Perlindungan Data Pribadi", "Keamanan Informasi", "Tindak Lanjut Temuan Sebelumnya" | Bagian 6.2 (menjadi delapan baris, lihat cacat 10) |
| 7 | Lima status | "Sesuai" / "Tidak Sesuai" / "Sebagian Sesuai" / "Belum Diverifikasi" / "Tidak Berlaku" dengan arti masing-masing, misalnya "Terdapat bukti bahwa kewajiban belum dipenuhi atau terdapat penyimpangan." dan "Sebagian kewajiban telah dipenuhi, tetapi masih terdapat kekurangan." | Bagian 2.2 |
| 8 | Tujuh belas field catatan temuan | "Tanggal Temuan", "Aspek Kepatuhan", "Uraian Temuan", "Persyaratan yang Tidak Terpenuhi", "Dasar Hukum/Dokumen Acuan", "Bukti Pendukung", "Dampak/Potensi Risiko", "Tingkat Risiko", "Penyebab", "Tindakan Korektif", "Penanggung Jawab", "Target Penyelesaian", "Bukti Penyelesaian", "Status Tindak Lanjut", "Hasil Verifikasi", "Tanggal Penutupan" (ditambah "Temuan Nomor") | Bagian 6.3 |
| 9 | Kolom rencana | "No.", "Nomor Temuan", "Tindakan yang Disepakati", "Penanggung Jawab", "Tenggat Waktu", "Bukti Pelaksanaan", "Status" | Bagian 6.4 (kolom diseragamkan, lihat cacat 7) |
| 10 | Lima butir kesimpulan | "Jumlah aspek atau kewajiban yang diperiksa", "aspek dengan status sesuai", "Jumlah temuan ketidaksesuaian", "Jumlah aspek yang belum dapat diverifikasi", "Jumlah tindakan perbaikan yang masih terbuka" | Bagian 6.5 |
| 11 | Larangan menyatakan patuh penuh | "Hindari menyatakan seluruh perusahaan telah patuh apabila masih terdapat aspek yang belum diperiksa atau belum diverifikasi" | Petunjuk Pengisian butir 9 |
| 12 | Lima rekomendasi tetap | "Melaksanakan tindakan korektif terhadap temuan yang belum terselesaikan sesuai tenggat waktu yang disepakati." / "Memastikan setiap unit kerja menyampaikan bukti pemenuhan kewajiban yang menjadi tanggung jawabnya." / "Memantau perubahan peraturan yang berdampak terhadap kegiatan usaha dan kewajiban perusahaan." / "Memperbarui daftar kewajiban hukum, register risiko hukum, serta dokumen terkait apabila diperlukan." / "Melakukan pemantauan ulang terhadap temuan yang memiliki risiko tinggi atau berulang." | Bagian 6.6 (pelaku ditambahkan) |
| 13 | Blok persetujuan per laporan | "Tahapan", "Nama/Jabatan", "Tanggal", "Tanda Tangan" dengan baris "Disusun oleh", "Diperiksa oleh", "Disetujui oleh" | Bagian 6.7 |
| 14 | Nama badan hukum (bukan dari sumber ini) | "PT Strategi Integrasi Nusantara (SINUX)" (context/audit commercial, baris "PT Strategi Integrasi Nusantara (SINUX) adalah perusahaan penyedia solusi Information & Communication Technology (ICT)"); "SOP sebagai panduan kerja resmi Departemen FAT PT Strategi Integrasi Nusantara." (context/audit fat) | Bagian 6.1 sel Nama Perusahaan |

## 3. Keputusan data dan pemetaan peran

- Approval, status, revision, effective_date, review_period, revision_desc: persis dari prompt dan config/defaults.json v21.
- Samuel di badan dokumen: tidak disebut kecuali "Direktur Utama" satu kali di Kesimpulan. Blok Approval memakai "President Director" (renderer dan defaults).
- COO: tidak ada peran COO yang perlu disebut di badan dokumen, jadi aturan "Direktur (COO)" dan "COO" tidak terpakai. Dicek: nol kemunculan "COO".
- Tiket: sumber tidak menyebut sistem tiket. Zammad dan GLPI tidak dipakai di dokumen ini; tidak ada alur tiket yang ditambahkan.
- Vault dan PPN: tidak relevan.
- Klasifikasi: RESTRICTED (Internal) dari prompt. Laporan terisi juga RESTRICTED (Internal) karena memuat temuan hukum (aturan klasifikasi di defaults: hukum = RESTRICTED (Internal)).
- Nama peran bagian 4 mengikuti specs/HR-ORG-01.json (Daftar Jabatan dan Matriks Peran):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| (tidak disebut; "Disusun oleh") | Staff Legal | Matriks Peran HR-ORG-01: Staff Legal = Legal & Compliance (JA-09), "(USULAN), menunggu konfirmasi (K-13)". Prompt menetapkan prepared "Staff Legal" |
| (tidak disebut; "Diperiksa oleh") | Line Manager Legal | Matriks Peran HR-ORG-01: Line Manager Legal = Legal & Compliance (JA-08), "(USULAN), menunggu konfirmasi (K-13)". Prompt menetapkan reviewed "Line Manager Legal" |
| Pelaksana Pemantauan | Staff Legal, dengan label (USULAN) | Sumber hanya menyediakan field nama; peran terdekat di HR-ORG-01 adalah JA-09 |
| Unit Kerja yang Dipantau | tetap "Unit Kerja yang Dipantau" | Bukan jabatan; HR-ORG-01 memuat unit (Commercial, Operation, Legal, Finance, dan lainnya), tidak ada satu jabatan yang bisa dipasangkan |
| Penanggung Jawab | tetap "Penanggung Jawab" (nama dan jabatan, ditulis per temuan) | Pemegangnya berbeda per temuan; tidak dipetakan ke satu jabatan |
| Disetujui oleh | "Penyetuju Laporan", jabatan belum ditetapkan | Sumber tidak menyebut; HR-ORG-01 tidak memuat peran penyetuju laporan Legal |

## 4. Penanganan cacat sumber

Hasil `grep -n 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA context/audit/*.md`: nol baris (0 kemunculan di ketujuh berkas). Menurut context/audit/README.md, sumber yang tidak ada di audit tidak punya catatan cacat; dokumen ini dibuat 14 Okt 2026 03:21Z, sesudah ingest Supporting Documents. Cacat di bawah ini ditemukan lewat pembacaan langsung sumber. Pembanding yang dipakai: bagian Legal Risk Register di context/audit (fileId 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA), karena sumber ini tampak disalin dari templat register itu.

| # | Cacat di sumber | Penanganan |
|---|---|---|
| 1 | Judul halaman sumber "Legal Risk Register", padahal judul berkas "Legal Compliance Monitoring & Corrective Action" (sisa salinan) | Dibuang. Judul dokumen dari checklist baris 46 |
| 2 | Sel Nama Perusahaan berisi "Daftar Risiko Hukum" (nilai keliru, sisa salinan) | Diisi nama badan hukum dari dokumen tim lain (fakta 14). Asumsi, lihat bagian 6 |
| 3 | Pada bacaan pertama, judul bagian tampil dengan tanda bintang literal ("**Informasi Umum**"); pada bacaan kedua tidak | Dianggap artefak ekspor, tidak berpengaruh pada isi. Tidak ada tanda bintang di dokumen |
| 4 | Placeholder "[Periode]", "[Tanggal]", "[Nomor Dokumen]", "[periode]", "[Jumlah]" | Sel isian dikosongkan; kalimat "Berdasarkan pemantauan ... periode [periode]" diganti rujukan ke Periode Pemantauan pada tabel Informasi Umum |
| 5 | Judul bagian 4 "Metode Penilaian Risiko", tetapi isinya daftar periksa pemantauan; tidak ada metode penilaian risiko di dokumen | Diberi judul "Daftar Periksa Pemantauan" (bagian 6.2). Metode penilaian risiko dirujuk ke SNX-LEG-REG-02 sebagai pengecualian lingkup |
| 6 | Judul bagian 6 "Rencana Mitigasi Risiko" memakai istilah mitigasi, sedangkan bagian lain memakai tindakan perbaikan dan tindakan korektif | Diganti "Rencana Tindakan Perbaikan" |
| 7 | Satu hal ditulis dengan beberapa istilah: "Tindakan Korektif" / "tindakan perbaikan" / "Tindakan yang Disepakati"; "Target Penyelesaian" / "Tenggat Waktu"; "Bukti Penyelesaian" / "Bukti Pelaksanaan"; "Status Tindak Lanjut" / "Status"; "unit kerja terkait" / "unit kerja yang dipantau"; "Customer" / "pelanggan"; "Perlindungan" / "Pelindungan" | Satu istilah per hal: Tindakan Perbaikan, Target Penyelesaian, Bukti Penyelesaian, Status Tindak Lanjut, Unit Kerja yang Dipantau, pelanggan, Pelindungan |
| 8 | "Temuan Nomor : [Nomor Dokumen]" mengaitkan nomor temuan dengan nomor dokumen tanpa aturan penomoran | Baris diganti "Nomor Temuan"; berupa nomor urut dalam satu laporan (USULAN). Skema penomoran laporan per periode masuk open items |
| 9 | Catatan Temuan dan tabel rencana memuat kolom yang sama (tindakan, penanggung jawab, target, bukti, status), sehingga isinya bisa berbeda | Ketentuan butir 9: kolom disalin dari Catatan Temuan dan Catatan Temuan yang berlaku (USULAN) |
| 10 | Tujuh butir ruang lingkup tidak sama dengan tujuh baris tabel: butir "Kebijakan dan prosedur internal" tidak punya baris; butir kontrak dipecah dua baris; "mitra" tidak punya baris; butir 4 memuat kerahasiaan informasi tetapi baris hanya data pribadi | Delapan aspek M1 sampai M8 dengan kode. Baris M7 ditambahkan dari butir ruang lingkup. "Mitra" ditempatkan di M4. Baris M5 diberi nama "Pelindungan Data Pribadi dan Kerahasiaan" |
| 11 | Butir kesimpulan 2 ditulis "aspek dengan status sesuai" tanpa kata "Jumlah" | Ditulis "Jumlah aspek berstatus Sesuai" |
| 12 | "Jumlah aspek yang diperiksa" dan "yang belum dapat diverifikasi" bisa tumpang tindih; "temuan ketidaksesuaian" lebih sempit daripada definisi temuan di sumber; "masih terbuka" tanpa nilai status | Petunjuk butir 8 mendefinisikan keduanya (USULAN); butir diubah menjadi "Jumlah temuan" dan "Jumlah aspek berstatus Belum Diverifikasi" |
| 13 | Kolom Status Tindak Lanjut tanpa daftar nilai; kolom Tingkat Risiko tanpa skala | Tiga nilai status (USULAN). Kategori risiko merujuk SNX-LEG-REG-02 (USULAN) |
| 14 | Petunjuk Pengisian Status berada di dalam sel tabel daftar periksa, dan teksnya menempel ("Tidak SesuaiTerdapat bukti") | Dipindah ke tabel nilai Status di bagian 2.2 dengan kolom Arti terpisah. Kalimat "sertai alasan" dipindah ke Ketentuan butir 2 |
| 15 | Rekomendasi berupa kalimat tanpa pelaku ("Melaksanakan", "Memastikan", "Memantau") dan "register risiko hukum" tanpa kode | Pelaku ditulis (Penanggung Jawab, Unit Kerja yang Dipantau, Staff Legal); register risiko hukum menjadi Legal Risk Register (SNX-LEG-REG-02) |
| 16 | Sumber memuat singkatan SMKI, sedangkan dokumen SNX-ISMS dan nama peran ISMS Coordinator memakai ISMS | SMKI dipertahankan (kalimat tim jelas) dan didefinisikan di Istilah dengan penjelasan bahwa ISMS pada kode dokumen merujuk sistem yang sama |
| 17 | Sumber tidak memuat nomor, klasifikasi, pemilik dokumen, atau acuan klausul ISO; tabel persetujuan sumber (Tahapan, Nama/Jabatan, Tanggal, Tanda Tangan) memakai bahasa pengesahan | Nomor, klasifikasi, pemilik dari defaults dan prompt. Tabel persetujuan sumber dipertahankan sebagai persetujuan per laporan (bagian 6.7), kosong sampai diisi; blok Approval dokumen tetap di sampul |
| 18 | Sumber tidak menyebut pengecualian lingkup | Lima butir pengecualian ditarik dari kriteria baris ini dan dokumen Legal lain (USULAN) |

Kalimat bernada perintah di sumber: ada dua, keduanya petunjuk isi formulir untuk pengguna laporan, bukan perintah kepada agen. Keduanya dimasukkan sebagai isi dokumen, bukan dijalankan: "[Uraikan kondisi kepatuhan berdasarkan hasil pemeriksaan dan bukti yang tersedia. Hindari menyatakan ...]" (menjadi Petunjuk butir 9) dan "Petunjuk Pengisian Status" (menjadi bagian 2.2). Dicatat di Open items butir 11.

## USULAN

Dokumen memuat 30 kemunculan label "(USULAN)" ditambah satu label "(USULAN, perlu konfirmasi konsultan)" di bagian Acuan ISO. Jumlah keputusan yang berbeda ada 21.

| # | Butir USULAN | Pemutus yang disarankan |
|---|---|---|
| 1 | Line Manager Legal = Legal & Compliance (JA-08) dan Staff Legal = JA-09 (mengikuti K-13 di SNX-HR-ORG-01) | Legal |
| 2 | Staff Legal sebagai Pelaksana Pemantauan | Legal |
| 3 | Line Manager Legal sebagai pemilik dokumen dan pemeriksa laporan terisi (Ketentuan butir 11) | Legal |
| 4 | Frekuensi laporan satu per triwulan, selaras dengan memo kepatuhan triwulanan di SNX-LEG-SOP-01 prosedur 6.7. Angka triwulan dari sumber lain, diperluas ke laporan ini | Legal |
| 5 | Lima butir pengecualian lingkup (penilaian risiko hukum ke SNX-LEG-REG-02, evaluasi tingkat kepatuhan ke SNX-LEG-RPT-02, penelaahan kontrak ke SNX-LEG-SOP-02, FRM-01, FRM-02, tinjauan data pribadi ke SNX-LEG-FRM-03, keputusan bisnis ke pihak berwenang) | Legal |
| 6 | Tiga nilai Status Tindak Lanjut (Terbuka, Menunggu Verifikasi, Ditutup) beserta artinya | Legal |
| 7 | Kategori Tingkat Risiko Rendah, Sedang, Tinggi, Sangat Tinggi, dengan nilai dan ambang di SNX-LEG-REG-02 | Legal |
| 8 | Aspek Belum Diverifikasi tidak dicatat sebagai temuan; bukti dilengkapi menurut Rekomendasi butir 2 (Ketentuan butir 5) | Legal |
| 9 | Aspek Tidak Sesuai atau Sebagian Sesuai menghasilkan sekurang-kurangnya satu temuan (Ketentuan butir 6) | Legal |
| 10 | Bila Staff Legal dan Unit Kerja yang Dipantau tidak sepakat soal Tindakan Perbaikan, Line Manager Legal memutuskan (Ketentuan butir 7) | Legal |
| 11 | Line Manager Legal meninjau Tingkat Risiko, selaras dengan SNX-LEG-SOP-02 butir 4.11 (Ketentuan butir 8). Butir 4.11 berlaku untuk kontrak, diperluas ke laporan ini | Legal |
| 12 | Kolom di tabel rencana disalin dari Catatan Temuan, dan Catatan Temuan berlaku bila berbeda (Ketentuan butir 9) | Legal |
| 13 | Penutupan temuan: Staff Legal mencatat Hasil Verifikasi, Line Manager Legal menetapkan penutupan, Staff Legal mengisi status Ditutup dan tanggalnya (Ketentuan butir 10) | Legal |
| 14 | Nomor Temuan berupa nomor urut dalam satu laporan (Petunjuk butir 5) | Legal |
| 15 | Penyimpanan di folder Google Drive departemen Legal, dengan pencatat Staff Legal dan pemilik Line Manager Legal (Ketentuan butir 12, bagian Rekaman). Lokasi itu sendiri berlabel USULAN di SNX-LEG-SOP-01 butir 4.24 | Legal |
| 16 | Retensi laporan terisi: pemilihan Kategori 4 (hasil pemeriksaan kepatuhan) atau Kategori 6 (laporan) di SNX-LEG-SOP-03; retensi bukti sama dengan laporan terisi | Legal |
| 17 | Rujukan silang: SNX-LEG-REG-03 untuk daftar peraturan dan kolom Dasar Hukum/Dokumen Acuan, SNX-LEG-REG-01 untuk daftar perizinan, SNX-LEG-REG-02 untuk Legal Risk Register (Petunjuk butir 3, Rekomendasi butir 4, bagian Dokumen Terkait) | Legal |
| 18 | Definisi "Jumlah aspek yang diperiksa" (baris berstatus Sesuai, Sebagian Sesuai, Tidak Sesuai) dan "masih terbuka" (Terbuka atau Menunggu Verifikasi) (Petunjuk butir 8) | Legal |
| 19 | Rekomendasi butir 5: "risiko tinggi" di sumber dibaca sebagai kategori Tinggi atau Sangat Tinggi | Legal |
| 20 | Pembagian baris persetujuan per laporan: Staff Legal menyusun, Line Manager Legal memeriksa, Penyetuju Laporan menyetujui dengan jabatan belum ditetapkan (Peran, Petunjuk butir 10) | Samuel |
| 21 | Tujuh butir klausul ISO 9001:2015 dan ISO/IEC 27001:2022 di bagian Acuan ISO (9001: 10.2, 7.5.3; 27001: 9.1, 10.2, Annex A 5.31, 5.34, 5.36), label "(USULAN, perlu konfirmasi konsultan)" | owner, diteruskan ke konsultan |

## 6. Asumsi (bukan USULAN berlabel, tetapi bukan dari teks sumber)

1. Nama Perusahaan diisi "PT Strategi Integrasi Nusantara (SINUX)" dari dokumen tim lain (fakta 14). Nilai di sumber ("Daftar Risiko Hukum") jelas keliru. Bila Legal ingin sel itu kosong atau memakai entitas lain, ubah di spec dan render ulang.
2. "Mitra" pada butir kontrak sumber ditempatkan di aspek M4 (Kontrak Vendor/Pemasok), karena sumber tidak punya baris untuk mitra.
3. "Dasar Pemantauan" tidak dijelaskan di sumber. Petunjuk butir 2 menafsirkannya sebagai dokumen atau penugasan yang menjadi dasar pemantauan satu periode.
4. "Tanggal Pemantauan" ditafsirkan sebagai tanggal pemeriksaan bukti, dan "Periode Pemantauan" sebagai rentang waktu yang diperiksa (Petunjuk butir 1). Sumber hanya menulis placeholder.
5. Petunjuk butir 4 memuat instruksi mekanis "Staff Legal menambah baris bila satu aspek punya lebih dari satu kewajiban". Tidak berlabel karena tidak menambah fakta atau angka, hanya cara memakai tabel.
6. Daftar Periksa Pemantauan diberi kode M1 sampai M8 dan baris diberi nomor 1 sampai 3 di tabel rencana. Kode dan nomor adalah alat rujuk di dokumen ini.
7. Rekomendasi sumber diperlakukan sebagai rekomendasi tetap pada setiap laporan (kalimatnya tidak bergantung periode), sehingga ditulis berisi dan bukan dikosongkan.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju Laporan per periode belum ditetapkan; sumber hanya punya baris "Disetujui oleh" tanpa jabatan. Dokumen menulis "jabatan pemegang peran ini belum ditetapkan" | Samuel |
| 2 | Batas LEG-RPT-01 dan LEG-RPT-02: Ringkasan Hasil Pemantauan menghitung jumlah aspek Sesuai dan temuan, yang dekat dengan "evaluasi tingkat kepatuhan" di checklist baris 36. Pengecualian lingkup butir 2 menarik batasnya, tetapi belum diputus | Legal |
| 3 | Konsistensi skala Tingkat Risiko dengan SNX-LEG-REG-02: Legal Risk Register sumbernya memakai empat kategori (skor 1 sampai 25), sedangkan SNX-LEG-SOP-01 butir 4.17 sampai 4.19 dan SNX-LEG-SOP-02 butir 4.8 sampai 4.10 memakai tiga (Tinggi, Sedang, Rendah). Spec LEG-REG-02 belum ada saat dokumen ini disusun; cek silang saat LEG-REG-02 berstatus DRAFTED | Legal |
| 4 | Frekuensi laporan dan penetapan periode: sumber hanya punya placeholder "[Periode]". Usulan triwulan (USULAN 4) | Legal |
| 5 | Penomoran laporan per periode dan nomor temuan: sumber menulis "Temuan Nomor : [Nomor Dokumen]" tanpa aturan. Usulan nomor urut per laporan (USULAN 14) | Legal |
| 6 | Pemetaan peran Line Manager Legal dan Staff Legal ke JA-08 dan JA-09 masih menunggu konfirmasi (K-13 di SNX-HR-ORG-01). Bila peta berubah, bagian Peran ikut berubah | owner |
| 7 | Retensi laporan terisi dan bukti belum ditetapkan; periode retensi di SNX-LEG-SOP-03 semuanya USULAN | Legal |
| 8 | Aturan penerimaan atau eskalasi risiko Sangat Tinggi tidak dimuat: SNX-LEG-REG-02 menyebut "pejabat yang berwenang" tanpa jabatan (matriks DoA belum terbit), sehingga dokumen ini tidak menunjuk pemutus | Samuel |
| 9 | Kewajiban memakai laporan ini (kapan wajib dibuat, oleh siapa diminta) tidak ada di sumber | Legal |
| 10 | Konfirmasi nama badan hukum yang diisi di sel Nama Perusahaan (asumsi 1), terutama bila laporan dipakai untuk entitas afiliasi | Legal |
| 11 | Dua kalimat bernada instruksi di sumber (petunjuk isi formulir) dicatat sebagai data, bukan instruksi (bagian 4). Tidak ada kalimat yang menyuruh agen melakukan sesuatu | owner (informasi, tanpa keputusan) |
| 12 | Checklist baris 46 tidak memberi acuan klausul (kolom iso_9001 dan iso_27001 null); klausul pada bagian Acuan ISO seluruhnya USULAN | owner, diteruskan ke konsultan |
| 13 | Sumber tidak memuat butir "Pemilik dokumen"; process_owner diambil dari jabatan reviewer departemen | Legal |

## 8. Jawaban dua pertanyaan sebelum selesai

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama, semuanya sudah diperbaiki di spec akhir:
- Benda sebagai pelaku kata kerja manusia: "Laporan memantau", "Aspek M5 memeriksa", "Hasil Verifikasi menyatakan", "Kesimpulan umum menguraikan", "Daftar Periksa Pemantauan memeriksa", "Butir 4.5 membatasi", "Memakai SNX-LEG-FRM-03". Diganti pelaku peran (Staff Legal, Line Manager Legal) atau rumusan isi ("memuat", "mencakup"). Pemindaian ulang kata kerja menelaah, memeriksa, meminta, memastikan, menyetujui, menunjukkan, menyatakan, menghasilkan, membatasi, menunjuk, merujuk, menguraikan, memantau, mengisi, mencatat, memakai pada seluruh teks spec: sisa kemunculan semuanya berpelaku manusia atau peran. Kolom tabel yang "memakai" nilai diganti "diisi".
- Kalimat Rekomendasi sumber tanpa pelaku ("Memastikan setiap unit kerja ...") diberi pelaku.
- Kalimat Tujuan "Pemantauan mendukung ... dan membantu menjaga" (benda berkata kerja manusia) diganti "Staff Legal melakukan pemantauan untuk ...".
- "Bukti yang diperiksa menunjukkan bahwa kewajiban telah dipenuhi" (benda berkata kerja manusia) diganti "Kewajiban telah dipenuhi menurut bukti yang diperiksa".

Sisa yang disengaja:
- Pembuka kalimat "Staff Legal mencatat ...", "Staff Legal mengisi ..." berulang di Ketentuan dan Petunjuk. Dibiarkan karena aturan satu langkah satu pelaku lebih penting daripada variasi.
- Label "(USULAN)" muncul 30 kali. Dibiarkan karena aturan label per butir berlaku.
- Tidak ada kelompok tiga yang dipaksakan: daftar tiga atau lebih di teks (misalnya nama bukti, lokasi, pemilik) mengikuti isi sumber atau isi kolom, bukan pola retorika. Tidak ada penutup positif, em-dash, penekanan tebal atau huruf kapital, atau atribusi kabur (dicek dengan grep daftar frasa terlarang prompt: nol temuan).

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir di dokumen | Sumber atau status |
|---|---|
| Nama badan hukum di Informasi Umum | Dokumen tim lain (fakta 14), asumsi 1, open item 10 |
| Kode aspek M1 sampai M8 dan nomor baris | Penomoran dokumen ini (asumsi 6), bukan fakta eksternal |
| "delapan aspek", "enam metode", "lima nilai", "tiga nilai" | Hitungan daftar di dokumen sendiri; delapan aspek = tujuh butir sumber ditambah baris M7 (cacat 10); enam metode = sumber; lima nilai = sumber; tiga nilai = USULAN 6 |
| "triwulan" | SNX-LEG-SOP-01 daftar SLA ("Triwulanan"), berlabel USULAN karena lingkupnya diperluas |
| Rujukan butir 4.5, 4.24, prosedur 6.7 (SNX-LEG-SOP-01), butir 4.11 (SNX-LEG-SOP-02), Kategori 4 dan 6 (SNX-LEG-SOP-03) | Dicek terhadap specs/ di repo; bisa basi bila spec itu berubah (open item 3 dan 7) |
| JA-08, JA-09, K-13 | specs/HR-ORG-01.json (Daftar Jabatan dan Butir Menunggu Konfirmasi) |
| Nilai status pemantauan, nama kolom, rekomendasi | Sumber, dengan perbaikan istilah (bagian 4) |
| Status Tindak Lanjut, kategori Tingkat Risiko, nomor temuan, aturan salin dan penutupan | USULAN berlabel (bagian 5) |
| Klausul ISO | USULAN dengan label konsultan (bagian 5, USULAN 21). Judul 7.5.3 (ISO 9001:2015) serta Annex A 5.31 dan 5.34 mengikuti spec Legal lain (LEG-FRM-01, LEG-SOP-01); judul 10.2, 9.1, dan Annex A 5.36 berasal dari pengetahuan umum penyusun tanpa berkas di repo. Seluruhnya perlu konfirmasi konsultan |
| Tanggal, angka lain, nama orang selain Samuel Kristanto Utomo di blok Approval | Nol; sel tanggal dan data faktual dibiarkan kosong |
