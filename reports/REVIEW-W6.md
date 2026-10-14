# REVIEW-W6 (2026-10-14T23:49:47Z)

## SNX-LEG-REG-01 Company Licenses & Permits Register
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-REG-01 Company Licenses & Permits Register (Rev00 DRAFT).docx
- Sumber: Company Licenses and Permits Register (1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk, modifiedTime 2026-10-13T10:52:13.121Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tabel register sumber kosong: tiga baris bernomor tanpa isi, dan tidak punya kolom jadwal perpanjangan, sehingga kolom itu ditambahkan sesuai kriteria (USULAN 4) | "No. \| Nama Dokumen \| Nomor Dokumen \| Instansi Penerbit \| Kegiatan Usaha/KBLI \| Tanggal Penerbitan \| Masa Berlaku \| Status \| Penanggung Jawab" lalu baris "1 \|   \|   \|   \|   \|   \|   \|   \|   \|", "2 ...", "3 ..." | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |
| Dokumen bermasa berlaku dipantau lewat tanggal kedaluwarsa dan ketentuan perpanjangan | "Dokumen yang memiliki masa berlaku dipantau berdasarkan tanggal kedaluwarsa serta ketentuan perpanjangan yang berlaku." (Pemantauan dan Tindak Lanjut, butir 2) | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |
| Pencantuman jenis dokumen tidak berarti wajib; kewajiban diverifikasi | "Pencantuman suatu jenis dokumen dalam daftar ini tidak dengan sendirinya menyatakan bahwa dokumen tersebut diwajibkan bagi perusahaan. Kewajiban masing-masing dokumen harus diverifikasi berdasarkan kondisi dan kegiatan usaha perusahaan." (Ruang Lingkup) | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |

### USULAN
| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan: prepared Staff Legal, reviewed Line Manager Legal, approved Samuel Kristanto Utomo / President Director; sumber menulis "[Nama/Jabatan]" tanpa isi (config/defaults.json D2) | Blok Approval halaman depan | owner |
| 2 | Process owner = Line Manager Legal (sumber tanpa "Pemilik dokumen") | Identity; Peran | Legal |
| 3 | Pembagian peran: Staff Legal mencatat, memperbarui, memantau; Line Manager Legal memeriksa isi register dan memverifikasi akta. Sumber hanya menyebut "Departemen Legal dan Compliance" | Ketentuan 1, 2; Peran | Legal |
| 4 | Kolom Jadwal Perpanjangan (tanggal pengingat dan tanggal target pengajuan perpanjangan). Kolom dituntut kriteria; sumber tidak punya kolom itu dan tanggal target pengajuan tidak ada di sumber mana pun | Istilah; Petunjuk Pengisian 5; tabel 6.1 | Legal |
| 5 | Kolom Lokasi Bukti, tabel Tindak Lanjut, dan tabel Catatan Pemeriksaan, untuk menutup cacat 4 dan 5 serta butir sumber VII.G | Bagian 6, tabel 6.2 sampai 6.4 | Legal |
| 6 | Kolom Penanggung Jawab ditulis nama jabatan menurut SNX-HR-ORG-01, bukan nama orang | Petunjuk Pengisian 7 | Legal |
| 7 | Status Perlu Diperbarui dan Kedaluwarsa juga memicu tindak lanjut (sumber hanya menyebut Belum Tersedia dan Belum Diverifikasi) | Ketentuan 7 | Legal |
| 8 | Folder Google Drive departemen Legal sebagai lokasi bukti pendukung dan register (mengikuti SNX-LEG-SOP-01 butir 4.24 yang juga USULAN) | Ketentuan 10; Rekaman | Legal |
| 9 | Pengecualian lingkup: kontrak dengan pelanggan atau vendor (register kontrak di SNX-LEG-SOP-01) dan daftar peraturan (SNX-LEG-REG-03); sumber tidak menyebut pengecualian | Lingkup | Legal |
| 10 | Pemilihan sembilan jenis dokumen pada baris awal tabel, termasu

### Open items
1. Semua sel data register kosong: nomor NIB, kode KBLI, nomor akta, Anggaran Dasar, NPWP, instansi, tanggal, masa berlaku, status, penanggung jawab, dan lokasi bukti tidak ada di sumber (tabel sumber hanya tiga baris kosong). Register belum bisa jadi bukti audit sampai Legal mengisinya dari dokumen asli. Penentu: Legal.
2. Konflik angka pengingat izin: SOP Divisi Legal 4.4 butir 3 menulis "pengingat perpanjangan 90 hari sebelum jatuh tempo" (kepada penanggung jawab izin menurut SNX-LEG-SOP-01), sedangkan Jobdesk Staff Legal menulis "Mengirim pengingat jatuh tempo kontrak dan izin kepada PIC bisnis pada 90, 60, dan 30 hari sebelumnya". Dokumen memakai 90 hari. Penentu: Legal.
3. Frekuensi pemeriksaan: sumber register hanya "secara berkala"; tinjauan bulanan berasal dari Jobdesk Staff Legal dan SNX-HR-JA-01. Dokumen memakai bulanan. Penentu: Legal.
4. Batas waktu memperbarui register setelah ada penerbitan, perubahan, atau pencabutan tidak ada di sumber (register kontrak punya batas 2 hari kerja, tidak dipakai di sini). Penentu: Legal.
5. Jabatan Pejabat yang Berwenang untuk pemeriksaan atau persetujuan tidak ditetapkan sumber. Penentu: Legal.
6. Penanggung jawab izin per jenis dokumen (misalnya NPWP: Legal, Finance, atau Accounting & Tax) tidak ada di sumber. Penentu: Legal dan FAT.
7. KBLI bukan izin tersendiri. Kriteria menyebutnya sebagai jenis, jadi dicatat sebagai baris 2. Apakah KBLI dicatat per NIB atau per kegiatan usaha, dan apakah Anggaran Dasar dicatat terpisah dari Akta Pendirian, tidak dinyatakan sumber. Penentu: Legal.
8. Batas dengan SNX-LEG-REG-04 (Company Legal Documents Register): kedua dokumen bisa memuat Akta Pendirian dan Anggaran Dasar, dan SNX-LEG-REG-04 juga memuat masa berlaku. Perlu diputuskan satu dokumen sebagai pemilik tiap jenis. Penentu: L
- Sweep (b): Departemen Legal tidak ada di tabel Peran; dua kalimat pasif; istilah berganti (verify nonblocking)

## SNX-LEG-FRM-01 Customer Contract Review Checklist
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 2; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-FRM-01 Customer Contract Review Checklist (Rev00 DRAFT).docx
- Sumber: Customer Contract Review Checklist (1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY, modifiedTime 2026-10-13T16:04:38.493Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Cakupan: kontrak antara perusahaan dan pelanggan, enam jenis layanan atau kerja sama | "Daftar periksa ini digunakan untuk menelaah kontrak antara perusahaan dan pelanggan, termasuk perjanjian layanan teknologi informasi, layanan komputasi awan, penjualan perangkat keras, layanan implementasi, layanan pemeliharaan, dan bentuk kerja sama komersial lainnya." (Ruang Lingkup) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |
| 2 | Tujuan: identifikasi risiko hukum, kejelasan hak dan kewajiban, dan penelaahan sebelum penandatanganan oleh pihak berwenang | "untuk mengidentifikasi risiko hukum, memastikan kejelasan hak dan kewajiban para pihak, serta memastikan bahwa ketentuan kontrak telah ditelaah sebelum ditandatangani oleh pihak yang berwenang." (Tujuan) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |
| 3 | Rekomendasi punya tiga opsi yang berbeda dari tiga opsi Hasil Penelaahan; opsi ketiga menahan penandatanganan | "Belum direkomendasikan untuk ditandatangani karena terdapat risiko atau isu material yang belum diselesaikan." (Rekomendasi, opsi ketiga) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |

### USULAN
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Process owner dan pemilik formulir = Line Manager Legal (sumber tanpa field Pemilik Dokumen; Unit Kerja "Legal dan Compliance"). Rekaman formulir terisi: pencatat Staff Legal, pemilik Line Manager Legal, selaras dengan records di specs/LEG-SOP-02.json ("pencatat Staff Legal; pemilik Line Manager Legal (butir 4.19)") | Legal |
| 2 | Isi kolom Hal yang Diperiksa 26 baris, dari dua dokumen tim (tabel Asal isi); kolom itu kosong di checklist | Legal |
| 3 | Kolom Jenis Risiko (Hukum, Komersial, Hukum dan komersial) dan Tingkat Risiko (Tinggi, Sedang, Rendah) pada tabel Temuan Utama dan Risiko; tabel 7 kolom menggantikan tiga field teks | Legal |
| 4 | Tiga nilai Status: Sesuai, Perlu Tindak Lanjut, Tidak Berlaku, beserta artinya | Legal |
| 5 | Aturan centang: Hasil Penelaahan boleh lebih dari satu pilihan kecuali "Tidak terdapat temuan"; Rekomendasi satu pilihan | Legal |
| 6 | Baris Disetujui oleh pada Catatan Penelaahan dan Persetujuan diisi Pejabat Berwenang (Line Manager Legal memberi Persetujuan Legal dan mengisi Diperiksa oleh) | Samuel (menunggu matriks DoA), bersama owner |
| 7 | Empat aspek tambahan: C2.4 Tumpang Tindih dengan Kontrak Lain, C4.5 Hak Penangguhan Pembayaran atau Layanan, C5.4 Keamanan Informasi, C7.3 Konsistensi Dokumen | Legal |
| 8 | Pemisahan C1.2 (penandatangan pelanggan) dan C8.2 (penandatangan SINUX) | Legal |
| 9 | C2.1: kesesuaian jenis layanan dengan kegiatan usaha dan perizinan di SNX-LEG-REG-01 | Legal |
| 10 | C2.3: kesesuaian target SLA dengan SNX-OPS-SOP-05 | Fani |
| 11 | C5.1: tingkat klasifikasi informasi pelanggan menurut SNX-ISMS-PRO-01 | Legal |
| 12 | C5.4: kesesuaian kewajiban pemberitahuan insiden dengan keputusan notifikasi di SNX-ISMS-SOP-01 | Fani |
| 13 | Wajib at

### Open items
1. Matriks DoA belum terbit: pejabat untuk C8.1 dan C8.2 serta isi baris Disetujui oleh belum bisa ditetapkan. Pemutus: Samuel, owner.
2. Apakah Persetujuan Legal oleh Line Manager Legal sudah cukup sebagai "Disetujui oleh", atau diisi Pejabat Berwenang (USULAN 6). Pemutus: Samuel, Legal.
3. Sumber tidak memetakan opsi Hasil Penelaahan ke opsi Rekomendasi (misalnya apakah "Tidak terdapat temuan" selalu berarti "Dapat dilanjutkan"). Formulir mempertahankan keduanya sebagai pilihan terpisah. Pemutus: Legal.
4. Kriteria Hal yang Diperiksa belum ditinjau Legal; kolom Status dan Tingkat Risiko belum punya keputusan tertulis (USULAN 4 dan 3). Pemutus: Legal.
5. Aspek yang ada di checklist vendor tetapi tidak ditambahkan di sini: subkontraktor, perubahan layanan, keberlangsungan layanan, jaminan dan kualitas, ketergantungan pada pihak ketiga (audit 5.2.7 dan 5.2.11). Scope creep terhadap Description; Legal memutuskan perlu tidaknya.
6. Pengelolaan nomor: sumber tidak bernomor, SNX-LEG-FRM-01 dari worklist. Tidak ada nomor lama untuk diganti.
7. Ejaan "Pelindungan" vs "Perlindungan" di C5.2 belum diputus Legal; checklist tim lain memakai "Pelindungan".
8. Penomoran butir SNX-LEG-SOP-01 (4.21, 4.24) dan SNX-LEG-SOP-02 (4.2, 4.7, 4.8 sampai 4.10, 4.14, 6.1, 6.4, 6.7) harus dicek ulang bila kedua SOP itu direvisi. Pemutus: orkestrator saat render ulang massal.
9. modifiedTime 1E_8 dan 19pe tidak diukur ulang di sesi ini (diambil dari notes/LEG-SOP-02.md). Pemutus: orkestrator bila perlu.
10. Retensi formulir terisi belum ditetapkan; usulan penetapan ada di SNX-LEG-SOP-03 (bukan di dokumen ini). Pemutus: Legal.
- Sweep (b): r3 nonblocking, klien vs pelanggan, kualifier C1.1 terpangkas, pasif, pengulangan Istilah dan Petunjuk

## SNX-LEG-FRM-02 Vendor / Supplier Contract Review Checklist
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-FRM-02 Vendor - Supplier Contract Review Checklist (Rev00 DRAFT).docx
- Sumber: Vendor/Supplier Contract Review Checklist (1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg, modifiedTime 2026-10-13T16:07:51.089Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tujuan form: panduan menelaah kontrak vendor atau pemasok. Sumber tidak menulis kata "kepentingan perusahaan"; unsur itu dari kriteria baris dan ditulis di Tujuan sebagai "agar kepentingan SINUX sebagai perusahaan terlindungi" | "Dokumen ini digunakan sebagai panduan untuk menelaah kontrak dengan vendor atau pemasok guna mengidentifikasi risiko hukum dan kontraktual, memastikan kejelasan hak dan kewajiban para pihak, serta menilai kecukupan ketentuan mengenai kerahasiaan, pelindungan data, keamanan informasi, dan keberlangsungan layanan apabila relevan." (Tujuan) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |
| Daftar periksa sumber berisi 9 kelompok dan 29 baris aspek, tetapi kolom Hal yang Diperiksa, Status, dan Catatan kosong di semua baris, sehingga isi kolom Hal yang Diperiksa ditulis (USULAN 1) | Header "No. \| Aspek yang Ditelaah \| Hal yang Diperiksa \| Status \| Catatan/Tindak Lanjut", baris kelompok "Identitas dan Kewenangan Para Pihak", lalu baris "  \| Identitas Vendor \|   \|   \|   " (Daftar Periksa Penelaahan Kontrak) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |
| Telaah ditentukan oleh jenis layanan, akses, ketergantungan, dan risiko, tetapi tabel Informasi Kontrak sumber hanya punya 11 isian administratif; tiga isian ditambah (USULAN 5) | "Pemeriksaan dilakukan berdasarkan jenis layanan, akses vendor terhadap informasi atau sistem perusahaan, tingkat ketergantungan perusahaan terhadap vendor, serta risiko yang timbul dari hubungan kontraktual tersebut." (Ruang Lingkup, paragraf 2) | 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg |

### USULAN
| # | Butir USULAN | Pemutus yang disarankan |
|---|---|---|
| 1 | Isi kolom Hal yang Diperiksa untuk 31 butir. Diturunkan dari nama aspek sumber, aspek review di SNX-LEG-SOP-02 butir 6.3, dan kuesioner SNX-ISMS-FRM-03 (lewat audit). Tidak ada angka, nama, atau tanggal | Legal (Line Manager Legal) |
| 2 | Dua butir tambahan: 4.5 Kekayaan Intelektual dan 6.4 Keadaan Kahar | Legal |
| 3 | Kolom Risiko dengan skala Tinggi, Sedang, Rendah dari SNX-LEG-SOP-02 butir 4.8 sampai 4.10 | Legal |
| 4 | Empat nilai Status (Sesuai, Perlu Tindak Lanjut, Perlu Pembahasan, Tidak Relevan) dan aturan memilih Hasil Penelaahan dari status (Petunjuk butir 8) | Legal |
| 5 | Lima isian tambahan Informasi Kontrak: ID Supplier di SNX-ISMS-FRM-03, Nomor Referensi Permintaan, Akses, Klasifikasi Informasi yang Diakses, Tingkat Ketergantungan | Legal; ID Supplier: Fani |
| 6 | Hasil kelompok 4 dan 5 dipakai memverifikasi kolom klausul keamanan di Daftar Supplier SNX-ISMS-FRM-03 | Fani |
| 7 | Padanan istilah: PIC Internal sama dengan PIC Bisnis, Unit Kerja Pemohon sama dengan Pemohon (SNX-LEG-SOP-02) | Legal |
| 8 | Dua baris "Kewenangan Penandatangan" dibedakan jadi pihak Vendor/Pemasok dan pihak SINUX | Legal |
| 9 | Tanda tangan per lembar: Disusun oleh Staff Legal, Diperiksa oleh Line Manager Legal, Disetujui oleh Pejabat Berwenang (Petunjuk butir 14) | Samuel |
| 10 | Line Manager Legal sebagai pemilik dokumen (Process Owner) | owner |
| 11 | Kolom Pihak yang Bertanggung Jawab memuat nama jabatan menurut SNX-HR-ORG-01, bukan nama orang | Aziz |
| 12 | Lokasi lembar dan hasil telaah di folder Google Drive departemen Legal (SNX-LEG-SOP-01 butir 4.24) | Legal |
| 13 | Kontrak pelanggan dikecualikan dari form ini dan memakai SNX-LEG-FRM-01 | Legal |
| 14 | Butir Risiko Tinggi yang belum diputus P

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Pemegang jabatan Pejabat Berwenang dan matriks DoA. SNX-LEG-SOP-02 dan HR-ORG-01 (Authority Matrix) menyebut dokumen itu belum disusun. Butir 9.2 dan baris Disetujui oleh bergantung padanya | Samuel |
| 2 | Apakah NDA, addendum, perpanjangan, dan kontrak mitra kerja sama yang bukan Vendor/Pemasok memakai form ini. Sumber diam; SNX-LEG-SOP-02 mencakup jenis itu | Legal |
| 3 | Aturan menurunkan Hasil Penelaahan ke Rekomendasi. Sumber tidak memetakan; audit menandai penghubung itu inferensi. Petunjuk 8 dan 10 baru usulan | Legal |
| 4 | Penomoran lembar terisi. Form hanya punya satu Nomor Dokumen; lembar dibedakan lewat Nomor Referensi Permintaan | Legal |
| 5 | Nama unit: sumber "Legal dan Compliance", data baris "Legal", HR-ORG-01 menamai jabatan "Legal & Compliance". Badan dokumen memakai "Legal" | owner |
| 6 | Kolom Hal yang Diperiksa perlu ditinjau Legal sebelum ACC. Konsultan dapat menambah butir teknis keamanan supplier yang sengaja tidak dimasukkan (cacat 12) | Legal, konsultan |
| 7 | Pembagian tanggung jawab verifikasi klausul keamanan supplier: SNX-ISMS-FRM-03 berada di Operation, form ini di Legal. FRM-03 dan SoA tidak menyebut form ini | Fani, Legal |
| 8 | Keselarasan dengan SNX-LEG-FRM-01 (judul bagian pengesahan, nilai Status, kolom Risiko). Berkas itu disusun lane lain dan tidak dibandingkan di sini | verifikator |
| 9 | Nomor butir dan istilah dari SNX-LEG-SOP-01, SNX-LEG-SOP-02, SNX-LEG-SOP-03, SNX-ISMS-PRO-01, dan SNX-HR-ORG-01 diambil dari specs di repo saat ini. Basi bila dokumen itu berubah; verifikator cek ulang | verifikator |
| 10 | Retensi lembar terisi belum ditetapkan; usulan ada di SNX-LEG-SOP-03 | Legal |
| 11 | Isi sumber tidak memuat kalimat perintah ke agen. Dua kalimat "Catatan: checklist ..
- Sweep (b): istilah telaah/penelaahan/review berganti; langkah dengan lebih dari satu tindakan (verify nonblocking)

## SNX-LEG-FRM-03 Data Protection & Confidentiality Compliance Review
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-FRM-03 Data Protection & Confidentiality Compliance Review (Rev00 DRAFT).docx
- Sumber: Data Protection & Confidentiality Compliance Review (1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8, modifiedTime 2026-10-13T16:56:19.285Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Dasar kewajiban yang ditinjau: ketentuan hukum, kewajiban kontraktual, dan kebijakan serta prosedur internal. Di dokumen menjadi bagian 1 Tujuan dan Kewajiban di Istilah | "Dokumen ini digunakan untuk meninjau kepatuhan perusahaan dalam mengelola data pribadi dan informasi rahasia berdasarkan ketentuan hukum yang berlaku, kewajiban kontraktual, serta kebijakan dan prosedur internal perusahaan yang relevan." (II. Tujuan) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |
| 2 | Daftar periksa punya enam kelompok (A sampai F) berisi 20 aspek, dan kolom "Hal yang Diperiksa" kosong di semua baris. Di dokumen menjadi bagian 8 (23 aspek, tiga di antaranya tambahan USULAN) | "No. \| Aspek yang Ditelaah \| Hal yang Diperiksa \| Status \| Catatan/Tindak Lanjut" lalu "A. Identifikasi dan Dasar Pemrosesan Data", "B. Akses dan Pengamanan Data", "C. Kerahasiaan Informasi", "D. Transfer Data", "E. Retensi dan Penghapusan Data", "F. Hak Subjek Data dan Penanganan Insiden" dan baris seperti "\|  \| Inventarisasi Data \|  \|  \|  \|" (VI. Daftar Periksa Penelaahan Kontrak) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |
| 3 | Status pemeriksaan baku ada lima, dan hasil dicatat sesuai penelaahan. Di dokumen menjadi Istilah (Status Pemeriksaan) dan kolom Status | "Sesuai \| Persyaratan yang ditinjau telah dipenuhi berdasarkan bukti yang diperiksa." / "Belum Diverifikasi \| Pemeriksaan belum selesai atau bukti pendukung belum tersedia." / "Catatan: checklist sesuai hasil penelaahan." (VII. Keterangan Status Pemeriksaan; kutipan dipotong, tiga status lain: Tidak Sesuai, Perlu Perbaikan, Tidak Berlaku) | 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8 |

### USULAN
Jumlah: 25 butir. Penanda "(USULAN" di spec: 33 kemunculan (lint menghitung 29 yang berbentuk persis "(USULAN)"); satu butir bisa muncul di beberapa tempat. Satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 12.

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
| U14 | Line Manage

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Isi kolom Hal yang Diperiksa (U5) dan tiga aspek tambahan (U6) perlu persetujuan sebelum form dipakai. Kriteria disusun dari SNX-LEG-SOP-01, SNX-ISMS-PRO-01, SNX-ISMS-SOP-01, SNX-ISMS-SOP-02, dan SNX-ISMS-FRM-03 yang masih berstatus Draft atau dalam peninjauan; bila dokumen itu berubah, kriteria ikut diperiksa ulang | Legal |
| 2 | Frekuensi tinjauan tidak ada di sumber. Setahun sekali (U4) mengikuti review_period YEARLY; belum ada keputusan | Legal |
| 3 | Penyetuju tiap lembar tinjauan tidak ada di sumber (blok "Disetujui oleh" kosong); blok Approval template menyetujui form, bukan lembar | Samuel |
| 4 | Peraturan pelaksana UU PDP dan sistem elektronik: apakah UU No. 1 Tahun 2024, PP No. 71 Tahun 2019, dan Peraturan BSSN No. 4 Tahun 2021 (disebut Manual M-SMT-01 menurut audit) masuk SNX-LEG-REG-03. Belum dibawa ke form ini | Legal |
| 5 | Periode retensi dokumen pelindungan data (Kategori 7 di SNX-LEG-SOP-03, usulan 5 tahun) belum ditetapkan dan belum diperiksa terhadap UU No. 27 Tahun 2022. Kolom Retensi di bagian 12 tertulis "Belum ditetapkan" | Legal |
| 6 | Tiga dokumen Legal memakai tiga kosakata status berbeda (audit butir 13). Form ini memakai lima nilai sumber; penyelarasan antardokumen belum diputus | Legal |
| 7 | Jalur penerimaan permintaan hak subjek data (F.1) tidak ditemukan di dokumen SINUX yang dibaca. Kriteria F.1 menanyakan jalur yang SINUX tetapkan; bila belum ada, aspek itu akan berstatus Perlu Perbaikan | Legal |
| 8 | Keterkaitan form ini ke SoA (kontrol 5.31 dan 5.34, status "Perlu keputusan", pemilik ISMS Coordinator menurut audit) adalah inferensi audit. SoA di tangan konsultan; form ini belum dirujuk SoA. Jabatan ISMS Coordinator belum ditetapkan (SNX-HR-ORG-01 butir K-13) | owner |
| 9 | Kuesion
- Sweep (b): istilah pengolahan A.1, approval/persetujuan, Legal tanpa definisi; E.2 dan B.4 merangkum ISMS-PRO-01 terlalu luas; baris HR-ORG-01 menyebut peran sebagai jabatan (verify nonblocking)

## SNX-LEG-REG-02 Legal Risk Register
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-REG-02 Legal Risk Register (Rev00 DRAFT).docx
- Sumber: Legal Risk Register (1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA, modifiedTime 2026-10-14T03:20:20.270Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Sumber hanya memuat delapan area risiko bernomor tanpa isi penilaian. Uraian, penyebab, dampak potensial, kemungkinan, dan dampak kosong, sehingga register di spec juga membiarkan sel itu kosong | "No. \| Area Risiko \| Uraian Risiko \| Penyebab/Pemicu \| Dampak Potensial \| Kemungkinan (1-5) \| Dampak (1-5)" lalu "1\\. \| Perizinan Berusaha \|  \|  \|  \|  \|  \|" sampai "8\\. \| Ketenagakerjaan \|  \|  \|  \|  \|  \|" | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |
| Tingkat risiko dihitung dengan rumus kali dan empat kategori; kategori teratas dieskalasi ke "pejabat yang berwenang" tanpa menyebut jabatan | "C. Perhitungan dan Kategori Risiko (Nilai Risiko = Skor Kemungkinan x Skor dampak)" dan "17-25 \| Sangat Tinggi \| Memerlukan eskalasi segera kepada pejabat yang berwenang untuk menentukan tindakan." | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |
| Pemilik dokumen = Legal dan Compliance; status sumber Draf; nomor, revisi, tanggal, penyusun, pemeriksa, penyetuju kosong | "Pemilik Dokumen \| Legal dan Compliance" dan "Status Dokumen \| Draf" dan "Nomor Dokumen \|   \|" | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |

### USULAN
14 butir. Semua berlabel "(USULAN)" di spec, kecuali butir 14 yang berlabel "(USULAN, perlu konfirmasi konsultan)".

| # | USULAN | Posisi | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Peran "Legal dan Compliance" (pemilik dokumen) dipasangkan ke Line Manager Legal dan Staff Legal (JA-08 dan JA-09) | Istilah | Aziz (pemilik SNX-HR-ORG-01, K-13) |
| 2 | "Manajemen" = Direktur Utama dan Direktur (COO), menggantikan "pejabat yang berwenang" | Istilah; Ketentuan butir 12 sampai 14 | Samuel |
| 3 | Pengecualian lingkup: risiko keamanan informasi (SNX-ISMS-REG-02) dan risiko proyek (SNX-OPS-FRM-02) tidak dicatat; area 4 dan 5 hanya akibat hukum | Lingkup | Legal dan Fani |
| 4 | Keterangan lima tingkat Dampak | Metode Penilaian 3.2 | Legal |
| 5 | Pembagian tugas Staff Legal (mencatat) dan Line Manager Legal (memeriksa, membahas, mengeskalasi) | Ketentuan butir 6; Peran | Legal |
| 6 | Tinjauan register setiap bulan | Ketentuan butir 17 | Legal |
| 7 | Jumlah risiko Tinggi dan Sangat Tinggi masuk laporan bulanan ke Manajemen | Ketentuan butir 19 | Legal |
| 8 | Penyimpanan di folder Google Drive departemen Legal, klasifikasi RESTRICTED (Internal) | Ketentuan butir 20; Rekaman | Legal |
| 9 | Pemilik Risiko dan Penanggung Jawab ditulis sebagai nama jabatan | Petunjuk butir 6 | Legal |
| 10 | Kolom Nilai Risiko, Kategori Risiko, Pemilik Risiko, dan tabel Riwayat Penilaian dan Status | Isi Register | Legal |
| 11 | Pemetaan area risiko ke dokumen terkait | Dokumen Terkait | Legal |
| 12 | Penyelarasan nama kategori teratas "Sangat Tinggi" dengan "Kritis" di SNX-ISMS-REG-02 | Dokumen Terkait | Fani dan Legal |
| 13 | Risiko Tinggi menurut SNX-LEG-SOP-01 butir 4.17 dicatat dan dinilai di register | Dokumen Terkait | Legal |
| 14 | Empat klausul ISO 9001:2015 dan ISO/IEC 2700

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Isi register kosong: uraian, penyebab, dampak potensial, kemungkinan, dampak, pemilik risiko untuk delapan area. Kriteria meminta "risiko yang teridentifikasi"; sumber hanya memuat nama area. Bahan awal ada di SNX-LEG-SOP-01 butir 4.17 (contoh risiko Tinggi) dan butir 4.21, tetapi menyalinnya sebagai isi register berarti mengarang penilaian | Legal bersama Pemilik Risiko |
| 2 | Apakah delapan area sudah lengkap (sumber memproses sengketa, somasi, dan klaim di SNX-LEG-SOP-01, tetapi tidak menjadikannya area) | Legal |
| 3 | Penerimaan risiko Sangat Tinggi: SNX-ISMS-REG-02 menetapkan COO secara tertulis, register ini hanya menulis eskalasi ke Manajemen | owner |
| 4 | Kriteria penanganan Sedang dan Tinggi berbeda dari SNX-ISMS-REG-02 (di sana rencana penanganan wajib mulai Sedang). Register ini mencatat tindakan pengendalian Sedang di tabel Rencana Mitigasi sebagai tafsir (asumsi 2) | Legal dan Fani |
| 5 | Padanan tiga tingkat SNX-LEG-SOP-01 (butir 4.17 sampai 4.19) ke empat kategori untuk Sedang dan Rendah belum diputus | Legal |
| 6 | SNX-LEG-SOP-01 belum menyebut register ini sebagai rekaman; butir 6.10 hanya menyebut "risiko Tinggi" | Legal |
| 7 | Nilai yang diizinkan di kolom Status Rencana Mitigasi belum ditetapkan (sumber tidak memberi); kolom dibiarkan bebas | Legal |
| 8 | Retensi register dan bukti mitigasi belum ditetapkan; usulan Kategori 6 ada di SNX-LEG-SOP-03 | Legal |
| 9 | Hubungan hasil evaluasi supplier SNX-ISMS-FRM-03 (kritikalitas) dengan area Kontrak Vendor | Legal dan Fani |
| 10 | Dokumen sumber disunting sesudah audit (modifiedTime lebih baru ±10 jam); perubahan di luar teks tidak terukur | Legal (pemilik sumber) |
| 11 | Pemilik dokumen tingkat jabatan: sumber menulis unit, bukan 
- Kriteria terpenuhi pada struktur; 8 area risiko kosong karena sumber kosong, Legal mengisi (verify)

## SNX-LEG-RPT-01 Legal Compliance Monitoring & Corrective Action Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-RPT-01 Legal Compliance Monitoring & Corrective Action Report (Rev00 DRAFT).docx
- Sumber: Legal Compliance Monitoring & Corrective Action (1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA, modifiedTime 2026-10-14T04:03:12.671Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Catatan temuan dibuat per ketidaksesuaian atau potensi risiko, dan memuat tindakan, penanggung jawab, target, serta status. Di dokumen menjadi bagian 6.3 dan 6.4 | "Bagian ini diisi untuk setiap ketidaksesuaian, kekurangan, atau potensi risiko yang memerlukan tindak lanjut." dan baris tabel "Tindakan Korektif", "Penanggung Jawab", "Target Penyelesaian", "Status Tindak Lanjut" (bagian "Daftar Temuan dan Tindakan Perbaikan") | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |
| 2 | Kesimpulan wajib berbukti, dan bukti yang belum ada tidak boleh menghasilkan status terpenuhi. Di dokumen menjadi Ketentuan butir 4 | "Setiap kesimpulan harus didukung oleh bukti yang dapat ditelusuri. Apabila bukti belum tersedia atau belum diperiksa, status pemenuhan tidak boleh dinyatakan telah terpenuhi." (Metode Pemantauan) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |
| 3 | Status pemantauan punya lima nilai, dan Tidak Berlaku wajib beralasan. Di dokumen menjadi bagian 2.2 dan Ketentuan butir 2 | "Belum Diverifikasi" dengan arti "Bukti belum cukup untuk menyimpulkan status kepatuhan." dan "Tidak Berlaku" dengan arti "Kewajiban tidak relevan terhadap ruang lingkup yang diperiksa, sertai alasan." (Petunjuk Pengisian Status) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |

### USULAN
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
| 12 | Kolom di ta

### Open items
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
| 10 | Konf
- Sweep (b): nama kolom Tingkat Risiko vs Kategori Risiko di LEG-REG-02 (skala sama); lihat qa/LEG-RPT-01.verify.json nonblocking
