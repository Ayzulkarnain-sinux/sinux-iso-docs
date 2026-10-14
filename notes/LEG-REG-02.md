# Catatan penyusun LEG-REG-02: Legal Risk Register

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-REG-02.json. Mode generic, aksi T1, wave W6, nomor SNX-LEG-REG-02 (nomor SNX lama dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class C2, doc_type_cover "REGISTER". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Legal dan Compliance" (kata-per-kata dari "Pemilik Dokumen" di sumber, tanpa nama; sekaligus nama jabatan JA-08 dan JA-09 di specs/HR-ORG-01.json).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Legal Risk Register (Google Doc, 7039 byte, induk folder Dep. Legal) | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA | 2026-10-14T03:20:20.270Z (get_file_metadata di sesi ini; cocok dengan prompt) | read_file_content dua kali (tanpa dan dengan includeComments). Tidak ada komentar. Teks dibandingkan dengan transkripsi context/audit: identitas, 11 bagian, skala, 8 area, tabel mitigasi, 6 butir pemantauan, ringkasan, persetujuan, riwayat sama. Audit mencatat modifiedTime 2026-10-13T17:08:49Z, jadi dokumen disunting lagi sesudahnya; perubahan di luar teks (format) tidak terukur |
| Kriteria penerimaan | config/checklist.json baris 45 | tidak diukur ulang | Description: "Daftar risiko hukum yang teridentifikasi, dampak potensial, tingkat risiko, dan langkah mitigasinya." Kolom iso_9001 dan iso_27001 baris ini null; checked TRUE |
| Pembanding: SNX-ISMS-REG-02 (xlsx) | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q | tidak diukur | read_file_content; dipakai hanya untuk ambang kategori ("Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25") |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, unit Management, K-13), specs/LEG-SOP-01.json (butir 4.17 sampai 4.19, 4.24, prosedur 6.10), specs/LEG-SOP-03.json (Kategori 6), specs/LEG-REG-01.json (pola register Legal), config/defaults.json v21, config/worklist.json (nomor SNX dokumen terkait) | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md, bagian legal/LEG-Legal-Risk-Register.md (baris 843 sampai 1020, bagian 5 butir 1 sampai 14) | salinan audit 13 sampai 14 Okt 2026 | DATA; dicocokkan dengan teks Drive terbaru |

Isi sumber tidak memuat kalimat perintah yang ditujukan ke penyusun. Kalimat aturan di dalam sumber ("Jumlah risiko diisi berdasarkan hasil penilaian aktual. Risiko yang belum dinilai tidak boleh dimasukkan ke kategori rendah secara otomatis.") adalah isi dokumen dan dipertahankan sebagai petunjuk pengisian butir 9.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Sumber hanya memuat delapan area risiko bernomor tanpa isi penilaian. Uraian, penyebab, dampak potensial, kemungkinan, dan dampak kosong, sehingga register di spec juga membiarkan sel itu kosong | "No. \| Area Risiko \| Uraian Risiko \| Penyebab/Pemicu \| Dampak Potensial \| Kemungkinan (1-5) \| Dampak (1-5)" lalu "1\\. \| Perizinan Berusaha \|  \|  \|  \|  \|  \|" sampai "8\\. \| Ketenagakerjaan \|  \|  \|  \|  \|  \|" | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |
| Tingkat risiko dihitung dengan rumus kali dan empat kategori; kategori teratas dieskalasi ke "pejabat yang berwenang" tanpa menyebut jabatan | "C. Perhitungan dan Kategori Risiko (Nilai Risiko = Skor Kemungkinan x Skor dampak)" dan "17-25 \| Sangat Tinggi \| Memerlukan eskalasi segera kepada pejabat yang berwenang untuk menentukan tindakan." | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |
| Pemilik dokumen = Legal dan Compliance; status sumber Draf; nomor, revisi, tanggal, penyusun, pemeriksa, penyetuju kosong | "Pemilik Dokumen \| Legal dan Compliance" dan "Status Dokumen \| Draf" dan "Nomor Dokumen \|   \|" | 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |

## 2. Fakta pendukung dan kutipan

Semua dari fileId 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA; penanda markdown dan garis miring terbalik dibuang.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di docx hasil |
|---|---|---|---|
| 1 | Tujuan | "Dokumen ini bertujuan untuk mengidentifikasi, mendokumentasikan, menilai, dan memantau risiko hukum yang berkaitan dengan kegiatan usaha perusahaan." / "Daftar risiko hukum digunakan untuk menentukan prioritas penanganan risiko, menetapkan tindakan pengendalian, menunjuk penanggung jawab, dan memantau pelaksanaan tindakan perbaikan atau mitigasi." | 1 Tujuan |
| 2 | Lingkup | "Daftar risiko hukum mencakup risiko yang timbul dari kegiatan usaha, hubungan kontraktual, perizinan, kewajiban berdasarkan peraturan perundang-undangan, pengelolaan data dan informasi, hubungan dengan pihak ketiga, serta aspek hukum lain yang relevan dengan operasional perusahaan." | 1 Lingkup |
| 3 | Sumber pencatatan risiko | "Risiko dicatat berdasarkan hasil pemeriksaan, evaluasi kontrak, pemantauan peraturan, laporan unit kerja, insiden, temuan audit, atau sumber informasi lain yang dapat dipertanggungjawabkan." | 1 Lingkup; Ketentuan butir 1 |
| 4 | Tiga peran sumber | "Departemen Legal dan Compliance", "Pemilik Risiko (Risk Owner)", "Manajemen atau Pihak yang Berwenang" dengan 4, 3, dan 2 tugas | 5 Peran; Ketentuan butir 1 sampai 16 |
| 5 | Tugas Departemen Legal dan Compliance | "Mengidentifikasi dan mendokumentasikan risiko hukum yang relevan." / "Melakukan penilaian risiko bersama unit kerja terkait jika diperlukan." / "Memberikan rekomendasi pengendalian atau mitigasi." / "Memantau status tindakan mitigasi dan memperbarui daftar risiko." | Ketentuan butir 1, 3, 5, 10 |
| 6 | Tugas Pemilik Risiko | "Memberikan informasi mengenai risiko pada kegiatan yang menjadi tanggung jawabnya." / "Melaksanakan tindakan mitigasi yang telah disepakati." / "Menyampaikan bukti pelaksanaan dan perkembangan tindak lanjut kepada pihak terkait." | Ketentuan butir 2, 8, 9; Istilah Pemilik Risiko |
| 7 | Tugas Manajemen | "Meninjau risiko yang memerlukan perhatian atau keputusan manajemen." / "Menentukan tindak lanjut atas risiko sesuai tingkat kewenangan dan mekanisme internal perusahaan." | Ketentuan butir 12, 14 |
| 8 | Skala Kemungkinan lima tingkat dengan keterangan | "1 \| Sangat Rendah \| Kemungkinan terjadinya sangat kecil berdasarkan informasi yang tersedia." sampai "5 \| Sangat Tinggi \| Risiko sangat mungkin terjadi atau berulang." | 3.1 Tingkat Kemungkinan (teks dipertahankan) |
| 9 | Skala Dampak lima tingkat tanpa keterangan | "1 \| Tidak Signifikan \|  \|" sampai "5 \| Sangat Tinggi \|  \|" | 3.2 Tingkat Dampak (keterangan USULAN) |
| 10 | Empat kategori dan penanganannya | "1-4 \| Rendah \| Dipantau dan dikendalikan melalui prosedur yang relevan." / "5-9 \| Sedang \| Menetapkan tindakan pengendalian yang sesuai dan memantau pelaksanaannya." / "10-16 \| Tinggi \| Memerlukan rencana mitigasi dan pemantauan prioritas." | 3.3 Nilai Risiko dan Kategori Risiko |
| 11 | Tabel mitigasi tujuh kolom, tiga baris kosong | "No. \| Risiko yang Ditangani \| Tindakan Mitigasi \| Penanggung Jawab \| Target Penyelesaian \| Bukti Penyelesaian \| Status" | 7.3 Rencana Mitigasi dan 7.4 Pelaksanaan Mitigasi (dipecah dua, lihat bagian 4) |
| 12 | Pemantauan | "Daftar risiko ditinjau secara berkala dan ketika terdapat perubahan signifikan pada kegiatan usaha, peraturan, kontrak, teknologi, atau proses operasional." | Ketentuan butir 17 (frekuensi bulanan USULAN) |
| 13 | Risiko tinggi dan sangat tinggi dibahas dengan pihak berwenang | "Risiko dengan kategori tinggi dan sangat tinggi diprioritaskan untuk dibahas bersama pihak yang berwenang." | Ketentuan butir 12 |
| 14 | Penilaian ulang setelah mitigasi | "Nilai risiko ditinjau kembali setelah tindakan mitigasi dilaksanakan untuk menilai apakah tingkat risiko telah berubah." | Ketentuan butir 11 |
| 15 | Risiko yang belum dapat ditangani | "Risiko yang belum dapat ditangani harus tetap dicatat, disertai alasan, rencana tindak lanjut, dan keputusan pihak yang berwenang apabila diperlukan." | Ketentuan butir 16; tabel Riwayat Penilaian dan Status |
| 16 | Riwayat penilaian dan status | "Riwayat perubahan penilaian dan status risiko dipelihara agar dapat ditelusuri." | Ketentuan butir 15; tabel Riwayat Penilaian dan Status (USULAN) |
| 17 | Ringkasan Risiko | "Jumlah risiko diisi berdasarkan hasil penilaian aktual. Risiko yang belum dinilai tidak boleh dimasukkan ke kategori rendah secara otomatis." | Petunjuk Pengisian butir 9 |

## 3. Hasil uji

Perintah render: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-REG-02.json /tmp/pen-LEG-REG-02/LEG-REG-02.docx` (berhasil, tanpa galat).

Perintah lint: `python3 -I tools/lint_doc.py /tmp/pen-LEG-REG-02/LEG-REG-02.docx generic`

Hasil terakhir: `"pass": true`, `"fails": []`, `"warns": ["13 butir (USULAN) menunggu ACC"]` (keluaran tersimpan di /tmp/pen-LEG-REG-02/lint_final.json). Putaran 1 sudah lulus lint; putaran berikutnya hanya memperbaiki tata letak (lihat bawah), memecah satu butir panjang, dan menghapus kata sifat tanpa ukuran di keterangan skala Dampak.

Pratinjau visual (soffice ke PDF, 14 halaman, contact sheet dan halaman 8, 10, 11, 12 dibaca): sampul, Identity, Revision, Approval, TOC, dan sepuluh bagian tampil. Diagram alur (11 simpul, "rankdir": "TB") terbaca. Perbaikan tata letak karena isi: judul kolom terpotong di tengah kata ("Kemungkinan", "Penanggung Jawab", "Penyelesaian", "No") pada tabel tujuh kolom, diatasi dengan memecah tabel Rencana Mitigasi menjadi dua (empat kolom) dan membuang kolom Area dari tabel Penilaian Risiko (nomor baris sama dengan tabel Identifikasi). Cek terakhir lewat pdftotext: tidak ada judul kolom terpotong di tengah kata.

Kode dokumen yang dirujuk di badan (12 kode, termasuk dirinya) dicek dengan skrip: semua selain SNX-LEG-REG-02 tercantum di tabel Dokumen Terkait.

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Sumber bagian II dan III | Dipersingkat menjadi tiga kalimat tujuan; kalimat tim dipertahankan. Kalimat pengecualian lingkup ditambah (USULAN) karena sumber diam |
| 2 Istilah | Baru | Hanya arti istilah; aturan di bagian 4. Peran Legal dan Compliance dihubungkan ke Line Manager Legal dan Staff Legal |
| 3 Metode Penilaian | Sumber bagian V | Skala Kemungkinan dan kategori dari sumber; keterangan Dampak USULAN; matriks 5 x 5 dihitung dari rumus; diagram alur diturunkan dari teks sumber (sumber tidak punya diagram) |
| 4 Ketentuan Pengelolaan | Sumber bagian IV dan VIII | 20 butir, satu pelaku per butir; pelaku sumber "Departemen Legal dan Compliance" dipisah menjadi Staff Legal (mencatat) dan Line Manager Legal (memeriksa, membahas, mengeskalasi), USULAN |
| 5 Peran | Sumber bagian IV | Empat peran dengan rujukan nomor butir; nama peran sama dengan ketentuan |
| 6 Petunjuk Pengisian | Baru | Sepuluh butir; sel data dibiarkan kosong |
| 7 Isi Register | Sumber bagian VI, VII, IX | Enam tabel; delapan area terisi nama, sel lain kosong, tanpa baris contoh |
| 8 Dokumen Terkait | Audit bagian 5 | 11 kode; pemetaan area ke dokumen USULAN |
| 9 Rekaman dan Acuan ISO | Baru | Retensi "Belum ditetapkan" (tidak ada angka di sumber); satu label "(USULAN, perlu konfirmasi konsultan)" untuk empat klausul |
| 10 Kesimpulan | Baru | Dua kalimat |
| Tidak dipindah | Sumber bagian I, X, XI | Identitas, catatan pemeriksaan dan persetujuan, dan riwayat perubahan dokumen sudah dipegang blok Identity, Approval, dan Revision History pada halaman depan template; tidak digandakan |

## 5. Penanganan cacat context/audit (bagian 5, 14 butir)

| Butir audit | Penanganan | Alasan |
|---|---|---|
| 1. Template belum berisi penilaian, enam field identitas kosong | Penilaian tetap kosong; field identitas diisi dari data baris dan blok template | Tidak ada sumber untuk uraian, penyebab, dampak, atau skor; mengisinya berarti mengarang. Dicatat di Open items |
| 2. Selisih PDF dan teks resmi | Tertutup; dicocokkan ulang | Teks Drive modifiedTime 2026-10-14T03:20:20.270Z memuat 7 kolom dan 8 area, sama dengan audit |
| 3. Salah ketik "Kekayaan Intelektuan" dan "Skor dampak" | Diperbaiki | Menjadi "Kekayaan Intelektual" dan "skor Dampak" |
| 4. Skala Dampak tanpa keterangan | Diperbaiki, USULAN | Keterangan kualitatif tanpa angka; pemutus Legal |
| 5. Tabel VI tanpa kolom Nilai Risiko, Kategori, Pemilik Risiko; tabel VII tanpa ID risiko | Diperbaiki sebagian, USULAN | Kolom Nilai Risiko, Kategori Risiko, Pemilik Risiko ditambah (juga memenuhi "tingkat risiko" di kriteria). ID risiko: kolom Risiko yang Ditangani memuat nomor dan area (Petunjuk butir 7). Kolom "kontrol yang sudah ada" tidak ditambah: tidak diminta kriteria dan tidak ada di sumber |
| 6. Frekuensi tinjauan "secara berkala" | Diperbaiki, USULAN | Bulanan (butir 17), mengikuti laporan bulanan ke Manajemen di SNX-LEG-SOP-01 prosedur 6.10 dan tinjauan bulanan register izin. Register ini belum disebut di SNX-LEG-SOP-01 sebagai rekaman: Open items |
| 7. Tiga tingkat di SOP Divisi Legal lawan empat kategori | Dicatat di Dokumen Terkait, USULAN | Risiko Tinggi menurut butir 4.17 dicatat dan dinilai di register. Padanan Sedang dan Rendah tidak dipaksakan: Open items |
| 8. Selisih dengan SNX-ISMS-REG-02 dan SNX-OPS-FRM-02 | Dicatat; aturan naik ke register ISMS tidak ditambah | Ambang REG-02 diverifikasi di Drive; pada skala 5 x 5 kategori tiap sel sama, hanya nama teratas beda (Kritis). Aturan baru "naik ke register ISMS" adalah proses di luar sumber dan kriteria. Sebagai gantinya Lingkup memberi batas (USULAN). REG-02 juga mengatur penerimaan risiko Kritis oleh COO secara tertulis dan rencana penanganan wajib mulai Sedang; kedua hal itu tidak disamakan: Open items |
| 9. Tanpa label klasifikasi | Diperbaiki | RESTRICTED (Internal) di meta; footer otomatis |
| 10. Keterkaitan dengan register perizinan | Dicatat di Dokumen Terkait | SNX-LEG-REG-01 sebagai dasar fakta area Perizinan Berusaha; kolom tindak lanjut ada di tabel Rencana dan Pelaksanaan Mitigasi |
| 11. Tidak ada tautan checklist ke baris register | Dicatat di Dokumen Terkait, USULAN | Pemetaan area 2 sampai 5 ke SNX-LEG-FRM-01, -02, -03; tidak ada kolom tautan baru, temuan dicatat manual lewat Ketentuan butir 1 |
| 12. Selisih dengan SNX-ISMS-FRM-03 | Tidak diperbaiki | Skala Tinggi, Sedang, Rendah di FRM-03 adalah kritikalitas supplier, bukan skor risiko hukum. Menghubungkan keduanya adalah keputusan Legal dan Fani: Open items |
| 13. "Manajemen atau Pihak yang Berwenang" tanpa jabatan | Diperbaiki, USULAN | Manajemen = Direktur Utama dan Direktur (COO), mengikuti SNX-LEG-SOP-01 |
| 14. Tidak ada klausul ISO | Diperbaiki, USULAN | Empat klausul di Acuan ISO dengan satu label konsultan. Hubungan ke SoA 5.31 tidak ditulis di dokumen (status SoA "Perlu keputusan", lane konsultan) |

## USULAN

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
| 14 | Empat klausul ISO 9001:2015 dan ISO/IEC 27001:2022 (9001 6.1 dan 7.5.3; Annex A 5.31 dan 5.34) | Acuan ISO | owner (meneruskan ke konsultan) |

## Open items

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
| 11 | Pemilik dokumen tingkat jabatan: sumber menulis unit, bukan jabatan; JA-08 dan JA-09 sama-sama bernama Legal & Compliance di SNX-HR-ORG-01 | Aziz |
| 12 | Tata letak: renderer tidak mengatur baris tabel agar tidak terbelah antarhalaman. Di PDF pratinjau, baris judul tabel 7.4 terbelah antara halaman 11 dan 12 (nilai bergantung paginasi, bisa berbeda di Word). HUMAN-VERDICT: lihat di Word sebelum dikirim. Bukan perubahan renderer (di luar batas tulis) | orkestrator |

## Asumsi

1. "Departemen Legal dan Compliance" di sumber dibaca sebagai Line Manager Legal dan Staff Legal; peran tim sumber dipetakan ke nama peran di specs/HR-ORG-01.json (matriks peran: Line Manager Legal = JA-08, Staff Legal = JA-09, keduanya USULAN di sana).
2. Risiko berkategori Sedang memakai tabel Rencana Mitigasi untuk mencatat "tindakan pengendalian yang sesuai" (kategori Sedang di sumber menyebut tindakan pengendalian, tabel mitigasi sumber tidak membatasi kategori).
3. "Unit kerja terkait" (penilaian bersama) dibaca sebagai Pemilik Risiko, karena Pemilik Risiko adalah peran unit tempat risiko timbul.
4. Tabel mitigasi sumber dipecah dua (Rencana Mitigasi dan Pelaksanaan Mitigasi) hanya karena lebar halaman; kolom dan urutan sumber utuh.
5. Matriks 5 x 5 dihitung dari rumus dan tabel kategori sumber, bukan tabel dari sumber. Nilai yang mungkin pada skala 1 sampai 5 tidak mencakup 17, 18, 19.
6. Format "1-4" di sumber ditulis "1 sampai 4" (aturan rentang).

## Pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Hasil pemeriksaan teks spec dan perbaikannya:

| Temuan | Perbaikan |
|---|---|
| Keterangan skala Dampak memakai kata sifat tanpa ukuran ("serius", "sangat serius"), khas teks isian | Dihapus; keterangan kini hanya menyebut akibat yang bisa dilihat (perlu keputusan Manajemen, dapat menghentikan kegiatan usaha). Tetap berlabel USULAN |
| Butir 17 memuat tiga tindakan dalam satu kalimat 36 kata | Dipecah menjadi butir 17 dan 18; rujukan nomor di Peran dan Rekaman diperbarui |
| Susunan "(USULAN, ...)" di dalam kurung lain pada butir laporan bulanan | Disatukan menjadi satu kurung |
| Benda sebagai pelaku kata kerja manusia (aturan tambahan orkestrator): "Register ini mengidentifikasi, mencatat, menilai, dan memantau", "Penilaian mempertimbangkan", "Tabel ... memakai nomor baris", "Butir 4.17 mengklasifikasikan", "Butir 4.24 menunjuk", "Kategori 6 mengelompokkan", "Area ... mencatat", "Matriks menunjukkan" | Ditulis ulang sebagai isi atau dengan pelaku peran ("Register ini memuat ...", "Penilaian terdiri dari ...", "Nomor baris tabel ... sama dengan ...", "Butir 4.17 sampai 4.19 memuat klasifikasi ...", "Baris memuat ..."). Dicek ulang dengan pemindai regex atas subjek benda dan kata kerja manusia pada seluruh teks spec; sisa temuan (dua baris) adalah positif palsu (subjek peran, atau "Nilai Risiko" sebagai objek) |
| Dua kalimat "Kolom X berstatus (USULAN)" berpola sama | Dibiarkan: pola itu sama dengan dokumen Legal lain dan tiap kalimat menunjuk butir yang berbeda |
| Hampir tiap butir ketentuan diawali "Staff Legal" | Dibiarkan: aturan RUNBOOK menuntut satu pelaku per butir dan pelaku sebenarnya memang sama |
| Kalimat pemisah antartabel dan "Hasil yang dijaga" gaya templat | Tidak dipakai; tujuan memakai kalimat sumber |
| Kata dilarang (em-dash, en-dash, "holistik", "sangat penting", "perlu dicatat bahwa", penutup generik, kelompok tiga dipaksakan) | Dicek: lint lulus dan grep em-dash dan en-dash pada spec menghasilkan nol. Daftar tiga yang tersisa (kategori Sedang, Tinggi, dan Sangat Tinggi; tiga dokumen FRM) adalah daftar nyata, bukan pemaksaan |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?** Pemeriksaan satu per satu:

| Butir di spec | Sumber |
|---|---|
| Delapan area risiko, skala Kemungkinan, kategori dan rentang 1 sampai 25, rumus, daftar peran, enam butir pemantauan | Drive 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA |
| Matriks 5 x 5 dan catatan nilai 17 sampai 19 | Dihitung dari rumus sumber; bukan angka baru |
| Tinggi 10 sampai 19 dan Kritis 20 sampai 25 pada SNX-ISMS-REG-02 | Drive 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q, dibaca di sesi ini |
| JA-08, JA-09, unit Management, nama peran | specs/HR-ORG-01.json |
| Butir 4.17 sampai 4.19, 4.24, prosedur 6.10 | specs/LEG-SOP-01.json (dibaca di sesi ini) |
| Kategori 6 | specs/LEG-SOP-03.json |
| Nomor SNX dokumen terkait dan judulnya | config/worklist.json dan checklist baris 40, 41, 42, 44 |
| Keterangan Dampak, bulanan, folder Drive, klausul ISO dan judulnya (termasuk terjemahan judul Annex A 5.34), pemetaan area ke dokumen, pemisahan tugas Staff Legal dan Line Manager Legal, definisi Mitigasi dan Risiko hukum | Tanpa sumber internal; semua berlabel USULAN atau berupa definisi istilah tanpa angka. Terjemahan judul Annex A 5.34 tidak diukur terhadap teks standar: perlu konfirmasi konsultan |
| Nama orang | Hanya "Samuel Kristanto Utomo / President Director" (data baris, blok Approval). Badan dokumen memakai "Direktur Utama" dan "Direktur (COO)" sekali |
| Tanggal dan angka retensi | Tidak ada di spec |

Kesimpulan pemeriksaan: tidak ada fakta, angka, nama, atau tanggal tanpa sumber yang tidak berlabel. Dua titik yang belum terbukti mesin: terjemahan judul Annex A 5.34 dan kecocokan teks Drive terbaru dengan format aslinya (HUMAN-VERDICT, Open items 10).
