# Catatan penyusun LEG-FRM-02: Vendor / Supplier Contract Review Checklist

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-FRM-02.json. Mode generic, aksi T1, wave W6, nomor SNX-LEG-FRM-02 (nomor SNX lama dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class B, doc_type_cover "FORM". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Line Manager Legal": sumber tidak punya baris "Pemilik dokumen" (hanya "Unit Kerja: Legal dan Compliance"), jadi dipakai jabatan reviewer departemen tanpa nama (USULAN 10).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Vendor/Supplier Contract Review Checklist (Google Doc, 6979 byte) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg | 2026-10-13T16:07:51.089Z (get_file_metadata di sesi ini; cocok dengan prompt; createdTime 2026-10-13T15:41:29.607Z) | read_file_content dua kali (tanpa dan dengan includeComments); isi sama, tidak ada komentar di berkas. download_file_content tidak dipakai: berkas Google Doc, teks dan tabelnya terbaca utuh (10 bagian, 8 tabel). Struktur dibandingkan dengan transkripsi context/audit (7 halaman, gambar dibuka oleh audit): sama |
| Kriteria penerimaan | config/checklist.json baris 42 | tidak diukur ulang | Description: "Dokumen berisikan daftar periksa untuk meninjau \nkontrak vendor atau pemasok guna memastikan \nperlindungan kepentingan perusahaan." Kolom iso_9001 dan iso_27001 baris ini null |
| Pendukung repo (bukan Drive) | specs/LEG-SOP-02.json (butir 4.6, 4.8 sampai 4.12, 4.19, 6.1, 6.3, 6.5, 6.7, bagian 8, daftar peran), specs/LEG-SOP-01.json (butir 4.24), specs/LEG-SOP-03.json (kategori 4), specs/HR-ORG-01.json (JA-08, JA-09, K-13), specs/ISMS-PRO-01.json (aturan berbagi ke pihak luar), notes/ISMS-FRM-03.md (SUP-001 sampai SUP-008, kolom klausul keamanan), specs/LEG-REG-01.json (pola Acuan ISO dan Rekaman, definisi NIB), config/defaults.json v21, config/worklist.json | repo kerja | Nomor butir dan istilah bisa basi bila dokumen itu berubah (open item 9) |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md baris 1321 sampai 1517 (bagian 5 baris 1498 sampai 1514), context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 89 | salinan audit 13 Okt 2026 | DATA; dibandingkan dengan teks Drive terbaru |

Perintah: `grep -n 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg context/audit/*.md` (tiga baris: dua di file legal, satu di file sintesis).

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tujuan form: panduan menelaah kontrak vendor atau pemasok. Sumber tidak menulis kata "kepentingan perusahaan"; unsur itu dari kriteria baris dan ditulis di Tujuan sebagai "agar kepentingan SINUX sebagai perusahaan terlindungi" | "Dokumen ini digunakan sebagai panduan untuk menelaah kontrak dengan vendor atau pemasok guna mengidentifikasi risiko hukum dan kontraktual, memastikan kejelasan hak dan kewajiban para pihak, serta menilai kecukupan ketentuan mengenai kerahasiaan, pelindungan data, keamanan informasi, dan keberlangsungan layanan apabila relevan." (Tujuan) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |
| Daftar periksa sumber berisi 9 kelompok dan 29 baris aspek, tetapi kolom Hal yang Diperiksa, Status, dan Catatan kosong di semua baris, sehingga isi kolom Hal yang Diperiksa ditulis (USULAN 1) | Header "No. \| Aspek yang Ditelaah \| Hal yang Diperiksa \| Status \| Catatan/Tindak Lanjut", baris kelompok "Identitas dan Kewenangan Para Pihak", lalu baris "  \| Identitas Vendor \|   \|   \|   " (Daftar Periksa Penelaahan Kontrak) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |
| Telaah ditentukan oleh jenis layanan, akses, ketergantungan, dan risiko, tetapi tabel Informasi Kontrak sumber hanya punya 11 isian administratif; tiga isian ditambah (USULAN 5) | "Pemeriksaan dilakukan berdasarkan jenis layanan, akses vendor terhadap informasi atau sistem perusahaan, tingkat ketergantungan perusahaan terhadap vendor, serta risiko yang timbul dari hubungan kontraktual tersebut." (Ruang Lingkup, paragraf 2) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |

## 2. Fakta pendukung dan kutipan

Kutipan dari fileId 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg; penanda markdown dan garis miring terbalik di keluaran alat dibuang.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Lingkup barang dan jasa | "Daftar periksa ini digunakan untuk menelaah kontrak dengan vendor atau pemasok yang menyediakan barang maupun jasa kepada perusahaan, termasuk penyedia infrastruktur teknologi informasi, pusat data, komputasi awan, perangkat lunak, perangkat keras, jasa implementasi, pemeliharaan, konsultasi, dan layanan pendukung lainnya." | Lingkup |
| 2 | Satu-satunya isian identitas yang terisi | "Unit Kerja \| Legal dan Compliance" | Halaman depan (diganti Identity template, department "Legal" dari data baris) |
| 3 | 11 isian Informasi Kontrak | "Nama Vendor/Pemasok", "Alamaat Vendor/Pemasok", "Nama/Jenis Kontrak", "Nomor Kontrak", "Barang/Layanan yang Disediakan", "Nilai Kontrak", "Jangka Waktu Kontrak", "Unit Kerja Pemohon", "PIC Internal", "Tanggal Penerimaan", "Target Penyelesaian" | Informasi Kontrak; 11 dipertahankan, tabel diperluas jadi 16 |
| 4 | Sembilan kelompok aspek | "Identitas dan Kewenangan Para Pihak", "Ruang Lingkup dan Pelaksanaan", "Biaya dan Pembayaran", "Kerahasiaan, Pelindungan Data, dan Hak Kekayaan Intelektual", "Keamanan Informasi", "Risiko Hukum dan Tanggung Jawab", "Keberlangsungan dan Pengakhiran Layanan", "Penyelesaian Sengketa", "Persetujuan dan Penandatanganan" | Daftar Periksa, kelompok 1 sampai 9 |
| 5 | Tiga opsi hasil penelaahan | "Tidak terdapat isu berdasarkan pemeriksaan yang dilakukan" / "Terdapat isu yang harus ditindaklanjuti sebelum penandatanganan." / "Diperlukan pembahasan lebih lanjut dengan vendor unit kerja terkait." | Ringkasan Hasil Penelaahan; Hasil Telaah dan Rekomendasi 7.1 |
| 6 | Tiga opsi rekomendasi | "Dapat dilanjutkan ke tahap persetujuan dan penandatanganan." / "Dapat dilanjutkan setelah tindak lanjut yang disyaratkan diselesaikan dan diverifikasi." / "Belum direkomendasikan untuk ditandatangani karena terdapat risiko atau isu material yang belum diselesaikan." | Rekomendasi; 7.3 |
| 7 | Tiga isian ringkasan dan dasar rekomendasi | "Temuan utama dan Risiko Hukum", "Perubahan atau tindak lanjut yang diperlukan", "Pihak yang bertanggung jawab dan target penyelesaian", "Dasar rekomendasi" (semua berisi "…") | 7.2 dan 7.4 |
| 8 | Blok tanda tangan per telaah | "Tahapan \| Nama/Jabatan \| Tanggal \| Tanda Tangan" dengan baris Disusun oleh, Diperiksa oleh, Disetujui oleh | Catatan Pemeriksaan dan Persetujuan; bagian 8 |
| 9 | Tiga lokasi penyimpanan | "Lokasi kontrak yang ditelaah", "Lokasi hasil penelaahan", "Lokasi korespondensi" (nilai "[lokasi/tautan berkas]") | Lokasi Penyimpanan Dokumen; 8.1 |
| 10 | Pembagian peran review dan tingkat risiko | specs/LEG-SOP-02.json butir 4.8 sampai 4.10 (Tinggi, Sedang, Rendah), butir 4.12 (Pejabat Berwenang memutuskan penerimaan risiko Tinggi), prosedur 6.5 (Line Manager Legal memutuskan hasil review), prosedur 6.7 (konfirmasi kewenangan tertulis), daftar peran Pemohon, PIC Bisnis, Pejabat Berwenang | Peran, Petunjuk Pengisian, Dokumen Terkait |
| 11 | Kolom klausul keamanan di daftar supplier | notes/ISMS-FRM-03.md: "Kontrak dan NDA memuat klausul keamanan Belum diketahui 8"; ID "SUP-001 sampai SUP-008" | Informasi Kontrak (ID Supplier); Dokumen Terkait |
| 12 | Aturan berbagi informasi ke pihak luar | specs/ISMS-PRO-01.json: "RESTRICTED dibagikan hanya dengan NDA atau kontrak yang berlaku dan persetujuan Pemilik informasi. SECRET dilarang dibagikan, kecuali kepada pemiliknya" | Daftar Periksa butir 4.2 |
| 13 | Repositori dokumen legal | specs/LEG-SOP-01.json butir 4.24: "Staff Legal menyimpan dokumen legal di repositori resmi, yaitu folder Google Drive departemen Legal (USULAN)." | Petunjuk Pengisian butir 20 |

## 3. Hasil uji

Render: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-FRM-02.json /tmp/pen-LEG-FRM-02/LEG-FRM-02.docx` (berhasil, tanpa galat).

Lint: `python3 -I tools/lint_doc.py /tmp/pen-LEG-FRM-02/LEG-FRM-02.docx generic`

Hasil terakhir: `"pass": true`, `"fails": []`, `"warns": ["18 butir (USULAN) menunggu ACC"]`. Putaran pertama sudah lulus lint. Putaran berikutnya hanya memperbaiki tata letak dan bahasa: judul kelompok memakai awalan "Kelompok n" (tanpa itu nomor bagian otomatis 6.1 bertabrakan dengan nomor butir 1.1); lebar kolom No, Aspek, dan Risiko dinaikkan karena kata terpotong di tengah ("Pemas-ok", "Risik-o", "N-o"); kalimat butir Hal yang Diperiksa ditulis aktif (bagian 7). Pratinjau PDF (soffice, 19 halaman) dilihat: sampul, Identity, Revision, Approval, TOC, 11 bagian, sembilan tabel Daftar Periksa (6 kolom), tabel Informasi Kontrak, Ringkasan, Catatan Pemeriksaan; pencarian teks PDF tidak menemukan kata terpotong sesudah perbaikan terakhir. Satu tabel kecil (Catatan Pemeriksaan) terbelah antarhalaman: tata letak dibekukan, tidak diubah. `python3 -I tools/lint_spot.py tools/lint_doc.py` memberi GAGAL 0. Pemeriksaan tambahan atas spec: tidak ada em-dash atau en-dash; tidak ada "draf ini", "dokumen sumber", "sumber tim" di badan; "Direktur (COO)" dan "COO" tidak dipakai (sumber tidak menyebut COO); Samuel di badan ditulis "Direktur Utama" (Kesimpulan), "President Director" hanya di blok Approval; tidak ada nama orang di badan; PPN tidak disebut (butir Pajak ditulis tanpa rumusan PPN); semua kode SNX di badan ada di bagian Dokumen Terkait (tujuh kode; nomor dokumen ini hanya di meta dan sampul).

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Tujuan dan Ruang Lingkup sumber | Kalimat tim dipertahankan dengan istilah dibakukan. Unsur "kepentingan perusahaan" dari kriteria. Pengecualian kontrak pelanggan ditambah (USULAN 13) |
| 2 Istilah | Istilah di spec; empat nilai Status | Hanya arti. Aturan ada di Petunjuk Pengisian |
| 3 Peran | Daftar peran SNX-LEG-SOP-02; blok Identitas sumber | Enam peran. Isi tugas merujuk nomor butir Petunjuk, tidak menyalin kalimat |
| 4 Petunjuk Pengisian | Kriteria + cacat audit | 25 butir, tiap butir satu tindakan dan satu pelaku |
| 5 Informasi Kontrak | Bagian IV sumber | 11 isian sumber + 5 isian tambahan (USULAN 5). Sel Informasi kosong |
| 6 Daftar Periksa Telaah Kontrak | Bagian V sumber | Sembilan tabel per kelompok, 31 butir (29 sumber + 4.5 dan 6.4). Kolom Status, Risiko, Catatan kosong. Kolom Hal yang Diperiksa diisi (USULAN 1). Tabel dipecah per kelompok karena sel kelompok tidak bisa digabung di renderer dan kolom judul kelompok terlalu sempit |
| 7 Hasil Telaah dan Rekomendasi | Bagian VI dan VII sumber | Kotak centang "☐", tiga opsi tiap bagian persis sumber; tabel Temuan dan Tindak Lanjut memecah "Pihak yang bertanggung jawab dan target penyelesaian" jadi dua kolom |
| 8 Catatan Pemeriksaan dan Persetujuan | Bagian VIII dan IX sumber | Tanda tangan per telaah. Blok Approval halaman depan mengesahkan form, tabel ini mengesahkan satu lembar. Lokasi Penyimpanan: sel kosong |
| 9 Dokumen Terkait | Kode yang disebut di badan | Tujuh kode |
| 10 Rekaman dan Acuan ISO | Petunjuk 20, pola LEG-REG-01 | Retensi "Belum ditetapkan" mengikuti SNX-LEG-SOP-03; klausul berlabel satu kali |
| 11 Kesimpulan | Status dokumen, review_period | Dua kalimat |

Blok sumber yang tidak dibawa ke badan: Identitas Dokumen (diganti halaman Identity), Riwayat Perubahan Dokumen (diganti Revision History template, satu baris revisi 00), baris judul halaman, dan teks "[lokasi/tautan berkas]" (diganti sel kosong).

Diagram: tidak dibuat. Sumber tidak punya diagram, kriteria tidak meminta, dan audit mencatat penghubung antara opsi Hasil dan opsi Rekomendasi hanya inferensi.

Kriteria penerimaan, unsur demi unsur:

| Unsur kriteria | Letak di dokumen |
|---|---|
| Daftar periksa | Bagian 6, sembilan tabel, 31 butir ber-kolom Hal yang Diperiksa, Status, Risiko, Catatan/Tindak Lanjut |
| Untuk meninjau kontrak vendor atau pemasok | Bagian 1 Tujuan dan Lingkup; istilah "Vendor/Pemasok" di Istilah; Informasi Kontrak (bagian 5); Hasil Telaah dan Rekomendasi (bagian 7) |
| Guna memastikan perlindungan kepentingan perusahaan | Tujuan (kalimat pertama); butir Daftar Periksa yang memeriksa hak SINUX (2.2, 2.4, 2.5, 3.2, 4.4, 4.5, 5.3, 6.2, 6.3, 7.3); Rekomendasi dengan dasar tertulis (7.3 dan 7.4); persetujuan tiga tahap (bagian 8) |

## 5. Penanganan cacat context/audit (bagian 5, fileId 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg)

| # | Cacat di audit | Penanganan |
|---|---|---|
| 1 | Template kosong: hanya Unit Kerja terisi; tanpa nomor, revisi, tanggal, pemilik, penyetuju, status, klasifikasi | Identity, Revision, Approval dari data baris. Tanggal efektif dan tanda tangan kosong. Klasifikasi RESTRICTED (Internal) |
| 2 | Hal yang Diperiksa kosong 29 dari 29; Status tanpa nilai baku; tanpa kolom tingkat risiko | Hal yang Diperiksa diisi untuk 31 butir (USULAN 1). Empat nilai Status (USULAN 4). Kolom Risiko dengan skala SNX-LEG-SOP-02 (USULAN 3) |
| 3 | Kelompok 4 menyebut Hak Kekayaan Intelektual tanpa barisnya | Butir 4.5 Kekayaan Intelektual ditambah (USULAN 2) |
| 4 | Salah ketik "Alamaat"; opsi Hasil ke-3 kehilangan kata "dan" | "Alamat Vendor/Pemasok"; "dengan Vendor/Pemasok dan Unit Kerja Terkait". Kebijakan "salah ketik template dipertahankan" berlaku untuk template Aziz, bukan untuk teks isian tim |
| 5 | "Kewenangan Penandatangan" (G1.2) dan "Kewenangan Penandatanganan" (G9.2) mirip; kelompok 8 satu baris bernama hampir sama | Dibedakan: "Kewenangan Penandatangan Vendor/Pemasok" (1.2) dan "Kewenangan Penandatanganan SINUX" (9.2) (USULAN 8). Kelompok 8 dengan baris "Hukum dan Penyelesaian Sengketa" dipertahankan: nama sumber, tidak menyesatkan |
| 6 | Judul bagian VIII beda dari checklist pelanggan; opsi Hasil 1 tanpa titik | Judul "Catatan Pemeriksaan dan Persetujuan" dipertahankan (nama sumber ini). Titik dilengkapi. Keselarasan judul dengan SNX-LEG-FRM-01 = open item 8 |
| 7 | Informasi Kontrak tanpa kritikalitas, ketergantungan, akses | Tiga isian ditambah: Akses, Klasifikasi Informasi yang Diakses, Tingkat Ketergantungan (USULAN 5). Butir Daftar Periksa 5.1 dan 7.1 merujuk isian itu |
| 8 | Empat klausul kritis SNX-LEG-SOP-02 tanpa baris (hak penangguhan, kekayaan intelektual, force majeure, tumpang tindih) dan sanksi SLA | Kekayaan intelektual jadi 4.5, keadaan kahar jadi 6.4 (USULAN 2). Hak penangguhan masuk butir 3.2, tumpang tindih masuk butir 1.4, sanksi dan kompensasi masuk butir 2.2 (USULAN 1) |
| 9 | Rekam jejak sengketa tanpa baris; persetujuan DoA tanpa acuan pejabat | Rekam jejak sengketa masuk butir 1.3. Butir 9.1 dan 9.2 merujuk SNX-LEG-SOP-02 butir 6.7 dan konfirmasi tertulis Pejabat Berwenang. Pemegang jabatan Pejabat Berwenang = open item 1 |
| 10 | Tidak ada field nomor register permintaan dan tidak ada rujukan target SOP | Isian Nomor Referensi Permintaan ditambah (USULAN 5). Petunjuk 5 merujuk SNX-LEG-SOP-02 bagian 8, angka target tidak disalin |
| 11 | Tidak ada ID supplier atau hasil yang bisa disalin ke kolom klausul keamanan SNX-ISMS-FRM-03; FRM-03 tidak menyebut checklist ini | Isian ID Supplier ditambah (USULAN 5). Hubungan ke kolom FRM-03 ditulis di Dokumen Terkait berlabel (USULAN 6). Perubahan di FRM-03 sendiri di luar batas tulis lane ini: open item 7 |
| 12 | Padanan butir kuesioner FRM-03 (insiden, hak audit, subkontraktor, pengembalian data, backup, SLA); butir teknis tidak ada | Padanan ada: 5.2, 5.3, 2.5, 4.4, 7.1, 2.2 dan 6.2. Butir teknis FRM-03 (sertifikasi, lokasi data, kontrol akses dan MFA, enkripsi, vulnerability management, eskalasi 24x7) tidak ditambah: itu penilaian teknis di FRM-03; butir 5.1 hanya memeriksa kewajiban keamanan di kontrak |
| 13 | Istilah tidak seragam (Vendor/Pemasok, supplier, penyedia eksternal); pemilik proses beda | "Vendor/Pemasok" dipakai di seluruh badan; Istilah mencatat bahwa FRM-03 menyebutnya supplier. "Penyedia eksternal" milik dokumen manual lain, tidak dipakai. Pemilik proses = open item 7 |
| 14 | Tanpa label klasifikasi; butir 4.1 dan 4.2 tidak menanyakan klasifikasi informasi dan persetujuan pemilik informasi | Klasifikasi RESTRICTED (Internal) dan label footer otomatis. Butir 4.2 memeriksa klasifikasi dan persetujuan pemilik menurut SNX-ISMS-PRO-01. Isian Klasifikasi Informasi ditambah |
| 15 | Lokasi masih placeholder; nomor dokumen tidak konsisten | Placeholder dibuang, sel kosong. Petunjuk 20 menunjuk folder Google Drive departemen Legal (USULAN 12). Nomor SNX-LEG-FRM-02 dari data baris |
| 16 | Tidak ada masa simpan hasil telaah | Rekaman: "Belum ditetapkan. Usulan penetapan ada di SNX-LEG-SOP-03." Angka retensi tidak ditulis |

## Asumsi

1. "Catatan Pemeriksaan dan Persetujuan" (sumber bagian VIII, dengan kolom Tanggal dan Tanda Tangan) dibaca sebagai pengesahan per telaah, sedangkan Disusun/Diperiksa/Disetujui di Identitas Dokumen dibaca sebagai pengesahan form. Dua tingkat itu dijelaskan di bagian 8.
2. Kalimat sumber "Catatan: checklist sesuai hasil penelaahan." dibaca sebagai petunjuk pengisian ("beri tanda centang"), karena "checklist" dipakai sebagai kata kerja. Dijadikan kalimat petunjuk di 7.1 dan 7.3.
3. Pembagian peran mengikuti SNX-LEG-SOP-02: Staff Legal menelaah dan mengisi, Line Manager Legal memeriksa dan memberi Persetujuan Legal, Pejabat Berwenang menyetujui transaksi.
4. Pemetaan peran ke HR-ORG-01: Line Manager Legal dan Staff Legal ada di matriks (JA-08, JA-09, menunggu K-13). Peran lain tidak ada di sana. Pejabat Berwenang tidak dipetakan ke jabatan karena SNX-LEG-SOP-02 dan HR-ORG-01 tidak menetapkannya; jabatan terdekat menurut fungsi adalah Direktur Utama (JA-01) dan Direktur (JA-02), tidak ditulis di badan. Unit Kerja Pemohon dan PIC Internal adalah peran per transaksi, bukan jabatan tetap. Unit Kerja Terkait ditulis dengan nama fungsi dari SNX-LEG-SOP-02 (Finance, Accounting & Tax, IT, fungsi keamanan informasi), tanpa jabatan.
5. Nama unit: badan dokumen memakai "Legal" (data baris dan department_labels), bukan "Legal dan Compliance" milik sumber (open item 5).

## USULAN

| # | Butir USULAN | Pemutus yang disarankan |
|---|---|---|
| 1 | Isi kolom Hal yang Diperiksa untuk 31 butir. Diturunkan dari nama aspek sumber, aspek review di SNX-LEG-SOP-02 butir 6.3, dan kuesioner SNX-ISMS-FRM-03 (lewat audit). Tidak ada angka, nama, atau tanggal | Legal (Line Manager Legal) |
| 2 | Dua butir tambahan: 4.5 Kekayaan Intelektual dan 6.4 Keadaan Kahar | Legal |
| 3 | Kolom Risiko dengan skala Tinggi, Sedang, Rendah dari SNX-LEG-SOP-02 butir 4.8 sampai 4.10 | Legal |
| 4 | Empat nilai Status (Sesuai, Perlu Tindak Lanjut, Perlu Pembahasan, Tidak Relevan) dan aturan memilih Hasil Telaah dari status (Petunjuk butir 15) | Legal |
| 5 | Lima isian tambahan Informasi Kontrak: ID Supplier di SNX-ISMS-FRM-03, Nomor Referensi Permintaan, Akses, Klasifikasi Informasi yang Diakses, Tingkat Ketergantungan | Legal; ID Supplier: Fani |
| 6 | Hasil kelompok 4 dan 5 dipakai memverifikasi kolom klausul keamanan di Daftar Supplier SNX-ISMS-FRM-03 | Fani |
| 7 | Padanan istilah: PIC Internal sama dengan PIC Bisnis, Unit Kerja Pemohon sama dengan Pemohon (SNX-LEG-SOP-02) | Legal |
| 8 | Dua baris "Kewenangan Penandatangan" dibedakan jadi pihak Vendor/Pemasok dan pihak SINUX | Legal |
| 9 | Tanda tangan per lembar: Disusun oleh Staff Legal, Diperiksa oleh Line Manager Legal, Disetujui oleh Pejabat Berwenang (Petunjuk butir 25) | Samuel |
| 10 | Line Manager Legal sebagai pemilik dokumen (Process Owner) | owner |
| 11 | Kolom Pihak yang Bertanggung Jawab memuat nama jabatan menurut SNX-HR-ORG-01, bukan nama orang | Aziz |
| 12 | Lokasi lembar dan hasil telaah di folder Google Drive departemen Legal (SNX-LEG-SOP-01 butir 4.24) | Legal |
| 13 | Kontrak pelanggan dikecualikan dari form ini dan memakai SNX-LEG-FRM-01 | Legal |
| 14 | Butir Risiko Tinggi yang belum diputus Pejabat Berwenang berarti rekomendasi ketiga (Petunjuk butir 18) | Legal; penerimaan risiko Tinggi tetap di Samuel |
| 15 | Pemetaan Line Manager Legal dan Staff Legal ke JA-08 dan JA-09 (K-13 di SNX-HR-ORG-01) | Aziz |
| 16 | Acuan ISO: sembilan klausul (ISO 9001:2015 8.4.2, 8.4.3, 7.5.3; ISO/IEC 27001:2022 Annex A 5.19, 5.20, 5.22, 5.31, 5.34, 6.6), berlabel satu kali "(USULAN, perlu konfirmasi konsultan)" | owner, setelah konsultan |
| 17 | Pemilik rekaman Line Manager Legal (kategori 4 untuk lembar dan kategori 1 untuk kontrak di SNX-LEG-SOP-03) dan retensi mengikuti SNX-LEG-SOP-03 | Legal |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Pemegang jabatan Pejabat Berwenang dan matriks DoA. SNX-LEG-SOP-02 dan HR-ORG-01 (Authority Matrix) menyebut dokumen itu belum disusun. Butir 9.2 dan baris Disetujui oleh bergantung padanya | Samuel |
| 2 | Apakah NDA, addendum, perpanjangan, dan kontrak mitra kerja sama yang bukan Vendor/Pemasok memakai form ini. Sumber diam; SNX-LEG-SOP-02 mencakup jenis itu | Legal |
| 3 | Aturan menurunkan Hasil Telaah ke Rekomendasi. Sumber tidak memetakan; audit menandai penghubung itu inferensi. Petunjuk 15 dan 18 baru usulan | Legal |
| 4 | Penomoran lembar terisi. Form hanya punya satu Nomor Dokumen; lembar dibedakan lewat Nomor Referensi Permintaan | Legal |
| 5 | Nama unit: sumber "Legal dan Compliance", data baris "Legal", HR-ORG-01 menamai jabatan "Legal & Compliance". Badan dokumen memakai "Legal" | owner |
| 6 | Kolom Hal yang Diperiksa perlu ditinjau Legal sebelum ACC. Konsultan dapat menambah butir teknis keamanan supplier yang sengaja tidak dimasukkan (cacat 12) | Legal, konsultan |
| 7 | Pembagian tanggung jawab verifikasi klausul keamanan supplier: SNX-ISMS-FRM-03 berada di Operation, form ini di Legal. FRM-03 dan SoA tidak menyebut form ini | Fani, Legal |
| 8 | Keselarasan dengan SNX-LEG-FRM-01 (judul bagian pengesahan, nilai Status, kolom Risiko). Berkas itu disusun lane lain dan tidak dibandingkan di sini | verifikator |
| 9 | Nomor butir dan istilah dari SNX-LEG-SOP-01, SNX-LEG-SOP-02, SNX-LEG-SOP-03, SNX-ISMS-PRO-01, dan SNX-HR-ORG-01 diambil dari specs di repo saat ini. Basi bila dokumen itu berubah; verifikator cek ulang | verifikator |
| 10 | Retensi lembar terisi belum ditetapkan; usulan ada di SNX-LEG-SOP-03 | Legal |
| 11 | Isi sumber tidak memuat kalimat perintah ke agen. Dua kalimat "Catatan: checklist ..." adalah petunjuk pengisian form dan diperlakukan sebagai data (Asumsi 2) | nihil |

## Pemeriksaan mutu bahasa

**Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?** Di putaran pertama ada empat hal. (a) Sekitar 20 butir Hal yang Diperiksa berakhir dengan "tercantum" atau "diatur" dalam pasif seragam. (b) Beberapa kalimat memberi kata kerja manusia ke benda: "Daftar Periksa memeriksa", "Kelompok 5 memeriksa", "Telaah mengidentifikasi", "Informasi Kontrak mencatat". (c) Petunjuk tentang tanda centang hasil (semula butir 8, kini butir 15) mengulang "dipilih" tiga kali. (d) Frasa kaku "baru boleh dipakai" di butir 2.5. Perbaikan: butir Daftar Periksa ditulis aktif dengan subjek "Kontrak" dan kata kerja isi ("mengatur", "mencantumkan", "merinci"); kalimat Acuan ISO diberi pelaku (Staff Legal) atau lokasi (dicek di kelompok 5); butir tanda centang hasil disusun ulang dengan tiga bentuk kalimat berbeda; Tujuan alinea 2 diawali "Telaah dilakukan untuk". Aturan tambahan orkestrator (benda tidak menjadi pelaku kata kerja manusia) diperiksa dengan memindai spec untuk kata kerja menelaah, memeriksa, meminta, memastikan, menyetujui, mengecek, menentukan, memutuskan, menilai, mengesahkan, menetapkan, mewajibkan, menunjuk, mengidentifikasi, memverifikasi, mengonfirmasi, dan memilih. Setiap kemunculan dibaca: pelakunya peran di bagian Peran (Staff Legal, Line Manager Legal, Pejabat Berwenang, PIC Internal) atau "Kontrak" dengan kata kerja isi. Diubah sesudah pemindaian: "Ketiganya menentukan butir" jadi "Staff Legal memakai ketiganya untuk memilih butir"; "Akses ... menentukan butir Daftar Periksa" jadi "Staff Legal memilih butir ... menurut akses"; "Tabel ini mengesahkan" dan "Blok Approval ... mengesahkan" jadi "mencatat pengesahan"; "Butir 4.24 menunjuk folder" jadi "memuat folder"; tiga butir "Kontrak mewajibkan" jadi "Kontrak mengatur bahwa ... memerlukan" atau "mengatur kewajiban"; "Kontrak memberi SINUX hak" jadi "Kontrak mencantumkan hak SINUX"; "menilai pemenuhannya" jadi "mengukur pemenuhannya". Lint tetap lulus sesudah perubahan. Sisa yang disengaja: pola "Kontrak mencantumkan ..." berulang karena itu daftar periksa; daftar empat unsur di Tujuan alinea 2 dan daftar jenis vendor di Lingkup tetap karena itu suara tim sumber (T1).

**Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?** Tidak ada angka bisnis, harga, nomor izin, tanggal, atau nama orang di badan dokumen. Nama Samuel Kristanto Utomo hanya di blok Approval dari data baris. Yang tidak berasal dari Drive dan sudah dilabeli: isi 31 butir Hal yang Diperiksa (pengetahuan kontrak umum, USULAN 1); empat nilai Status (USULAN 4); skala Tinggi, Sedang, Rendah dan nomor butir dari specs repo (bukan Drive, open item 9); nama fungsi Finance, Accounting & Tax, IT dari SNX-LEG-SOP-02; definisi NIB dan "OSS" dari spec LEG-REG-01. Perbaikan yang dilakukan: butir 9.1 semula memuat "Persetujuan Legal" sebagai hal yang diperiksa, padahal persetujuan itu diberikan sesudah form diisi (melingkar), lalu dibuang; butir 4.2 dilengkapi "kepada Vendor/Pemasok" agar aturan SECRET tidak terbaca lebih luas dari aturan PRO-01; PPN tidak disebut karena rumusan FAT belum ada.

## Sweep

Sweep dari orkestrator, dua butir. Perubahan hanya di specs/LEG-FRM-02.json dan notes ini. Fakta, angka, nama, dan struktur bagian lain tidak diubah.

**Butir 1: istilah telaah, penelaahan, dan review berganti; langkah dengan lebih dari satu tindakan**

| # | Sebelum | Sesudah |
|---|---|---|
| 1a | Judul bagian 6 "Daftar Periksa Penelaahan Kontrak" | "Daftar Periksa Telaah Kontrak" |
| 1b | Judul bagian 7 "Ringkasan Hasil dan Rekomendasi"; subjudul dan header "Hasil Penelaahan"; Petunjuk 8 "Ringkasan Hasil Penelaahan"; Rekaman menyebut "Ringkasan" | Judul bagian 7 "Hasil Telaah dan Rekomendasi"; subjudul dan header "Hasil Telaah"; Petunjuk 15 "tabel Hasil Telaah"; Rekaman "semua tabel dari Informasi Kontrak sampai Catatan Pemeriksaan dan Persetujuan" |
| 1c | Tabel lokasi "Lokasi hasil penelaahan" | "Lokasi hasil telaah" |
| 1d | Istilah Persetujuan Legal: "review hukum atas kontrak" | "telaah hukum atas kontrak" |
| 1e | Dokumen Terkait SNX-LEG-SOP-02: "penyusunan dan review kontrak (6.3)" | "penyusunan dan telaah kontrak (6.3)" |
| 1f | Petunjuk 5: "Staff Legal memeriksa tiap butir Daftar Periksa terhadap kontrak dan mengisi kolom Status ..." | Petunjuk 10: "Staff Legal mengisi kolom Status tiap butir Daftar Periksa dari hasil menelaah kontrak ..." |
| 1g | Petunjuk 2 (empat isian dalam satu butir) | Dipecah jadi butir 2 (tabel Informasi Kontrak), 3 (Nomor Referensi Permintaan), 4 (ID Supplier); Petunjuk 3 jadi butir 5 (Target Penyelesaian), teks tetap |
| 1h | Petunjuk 4 (lima kalimat, tiga isian dan pemakaiannya) | Dipecah jadi butir 6 (Akses), 7 (Klasifikasi Informasi), 8 (Tingkat Ketergantungan), 9 (memilih butir Daftar Periksa yang relevan) |
| 1i | Petunjuk 5 (mengisi Status dan menulis alasan Tidak Relevan) | Butir 10 (Status) dan butir 11 (alasan Tidak Relevan) |
| 1j | Petunjuk 7 (meminta masukan dan menulis masukan) | Butir 13 (meminta masukan Unit Kerja Terkait) dan butir 14 (menulis masukan di Catatan/Tindak Lanjut) |
| 1k | Petunjuk 9 (menulis baris Temuan dan mengisi kolom jabatan) | Butir 16 (baris Temuan dan Tindak Lanjut) dan butir 17 (nama jabatan di kolom Pihak yang Bertanggung Jawab, USULAN) |
| 1l | Petunjuk 10 (memilih rekomendasi dan menulis dasarnya) | Butir 18 (memilih rekomendasi) dan butir 19 (menulis dasar rekomendasi) |
| 1m | Petunjuk 13 (memeriksa, menandatangani, memberi Persetujuan Legal atau mengembalikan) | Butir 22 (memeriksa lembar), 23 (menandatangani baris Diperiksa oleh), 24 (Persetujuan Legal atau mengembalikan lembar) |
| 1n | Petunjuk 6, 8, 11, 12, 14 | Butir 12, 15, 20, 21, 25; teks sama kecuali "tabel Hasil Telaah" di butir 15. Total butir Petunjuk: 14 menjadi 25 |
| 1o | Rujukan nomor butir di tabel Peran, Rekaman, dan Acuan ISO | Disesuaikan: Staff Legal butir 1 sampai 21; Line Manager Legal butir 5 dan 22 sampai 24; Unit Kerja Terkait butir 13; Pejabat Berwenang butir 25; Rekaman butir 20; ISO 9001:2015 8.4.2 butir 9 |

Keputusan istilah: "telaah" untuk meninjau kontrak (Staff Legal). "Review" tinggal di nama dokumen (SNX-LEG-SOP-02, SNX-LEG-FRM-01, judul form) dan di Istilah Telaah sebagai padanan SNX-LEG-SOP-02. "Memeriksa" tinggal untuk Line Manager Legal memeriksa lembar (butir 22) dan untuk nama bawaan sumber: "Hak Pemeriksaan", "Diperiksa oleh", "Catatan Pemeriksaan dan Persetujuan". "Meninjau" di Tujuan berasal dari kriteria baris dan terikat ke Istilah Telaah ("Peninjauan kontrak ..."); "Line Manager Legal meninjau form ini setiap tahun" adalah tinjauan berkala atas form, bukan telaah kontrak. Judul sumber ("Penelaahan") diubah ke "Telaah" karena satu istilah untuk satu hal lebih diutamakan daripada kata persis judul sumber.

**Butir 2: konsistensi Legal**

| # | Sebelum | Sesudah |
|---|---|---|
| 2a | Dokumen Terkait SNX-HR-ORG-01: "Sumber nama jabatan Line Manager Legal dan Staff Legal." | "Sumber pemetaan peran Line Manager Legal dan Staff Legal ke jabatan Legal & Compliance (JA-08, JA-09) (USULAN)." |
| 2b | Tabel Peran: "Dipetakan ke jabatan Legal & Compliance (JA-09) ..." dan "(JA-08) ..." | "Peran ini dipetakan ke jabatan Legal & Compliance (JA-09) ..." dan "(JA-08) ...", label menunggu K-13 dan (USULAN) tetap |
| 2c | Rekaman, lembar terisi: "Pemilik: Line Manager Legal (USULAN)" | "Pemilik: Line Manager Legal (kategori 4 di SNX-LEG-SOP-03, USULAN)" |
| 2d | Rekaman, kontrak dan korespondensi: "Pemilik: Line Manager Legal (USULAN)" | "Pemilik: Line Manager Legal (kategori 1 di SNX-LEG-SOP-03 untuk kontrak, USULAN)" |

Pemeriksaan selaras dengan SNX-LEG-SOP-03 (specs/LEG-SOP-03.json): tabel Rekaman memberi pemilik Line Manager Legal untuk kategori 1 (dokumen kontraktual) dan kategori 4 (dokumen penelaahan Legal), dan butir 4.1 menugaskan Staff Legal mencatat dokumen di register. Dokumen ini sudah sama; yang ditambah hanya rujukan kategorinya. Pemetaan lembar terisi ke kategori 4 adalah usulan: kategori 4 memuat hasil uji tuntas, hasil pemeriksaan kepatuhan, dan ringkasan risiko, tetapi tidak menyebut checklist telaah kontrak (label USULAN sudah di sel). Retensi tidak diubah. Folder repositori tetap merujuk SNX-LEG-SOP-01 butir 4.24; SNX-LEG-SOP-03 butir 4.8 menyebut folder yang sama. Catatan untuk orkestrator di luar batas tulis ini: SNX-LEG-SOP-01 memberi pemilik Staff Legal pada rekaman kontrak, sedangkan SNX-LEG-SOP-03 memberi pemilik Line Manager Legal.

**Hasil uji sweep**

Perintah: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-FRM-02.json /tmp/pen-LEG-FRM-02/LEG-FRM-02.docx` (berhasil); `python3 -I tools/lint_doc.py /tmp/pen-LEG-FRM-02/LEG-FRM-02.docx generic` memberi `"pass": true`, `"fails": []`, `"warns": ["18 butir (USULAN) menunggu ACC"]` (turun dari 19 karena dua label di Rekaman kini berbentuk "(kategori ..., USULAN)" dan satu label ditambah di Dokumen Terkait); `python3 /mnt/skills/public/docx/scripts/office/validate.py` memberi "All validations PASSED!"; `python3 -I reports/orch/blankscan.py` memberi `ok 19 LEG-FRM-02.docx []`.


## ISO-W9

| butir | sebelum | sesudah |
|---|---|---|
| Blok Approval, Prepared By | Staff Legal | Alif Altamziz / Staff Legal |
| Blok Approval, Reviewed By | Line Manager Legal | Ester Febe Utomo / Line Manager Legal |
| Tabel Peran, Staff Legal | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| Tabel Peran, Line Manager Legal | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| Dokumen Terkait, baris SNX-HR-ORG-01 | (JA-08, JA-09) (USULAN). | (JA-08, JA-09). |

Open item:
- Pemetaan Legal (USULAN K-13 di tabel USULAN dan catatan lama): ditutup W9: owner 15 Okt memutus Line Manager Legal = JA-08 Ester Febe Utomo, Staff Legal = JA-09 Alif Altamziz (LEAD G-3 A5); label USULAN dan menunggu konfirmasi pada pemetaan itu dihapus. USULAN lain tetap.
- A3: tidak ada garis lapor JA-03/JA-04 di dokumen ini.
