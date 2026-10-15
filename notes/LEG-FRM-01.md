# Catatan penyusun LEG-FRM-01: Customer Contract Review Checklist

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-FRM-01.json. Mode generic, aksi T1, wave W6, nomor SNX-LEG-FRM-01 (nomor lama dipertahankan; sumber tidak bernomor), department Legal, classification RESTRICTED (Internal), audit_class B. Approval persis: prepared Staff Legal, reviewed Line Manager Legal, approved Samuel Kristanto Utomo / President Director. Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Line Manager Legal" (sumber tidak punya field Pemilik Dokumen; jabatan reviewer departemen, tanpa nama; USULAN 1).

Hasil uji terakhir (bukti mentah: /tmp/pen-LEG-FRM-01/render.out.txt, /tmp/pen-LEG-FRM-01/lint.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-FRM-01.json /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx`: exit 0, tanpa keluaran.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx generic`: `"pass": true`, `"fails": []`, satu warn "32 butir (USULAN) menunggu ACC" (38 kemunculan label di spec). Hasil sesudah putaran sweep (bagian "Sweep"); tiap halaman badan (halaman 5 sampai 16) berisi teks, halaman 1 sampai 4 adalah sampul, Identity, Revision History, Approval, dan daftar isi template.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- soffice ke PDF: 16 halaman, dilihat per montase. Tidak ada diagram (lihat Asumsi 5). Header tabel kadang jatuh di dasar halaman; itu perilaku renderer, bukan isi.
- Pemeriksaan tambahan atas teks hasil render (python3 -I): nol em-dash dan en-dash; nol frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, tanpa terkecuali, tanpa kompromi, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, hulu ke hilir, sesegera mungkin); nol "dokumen sumber", "sumber tim", "penyusun", "draf ini", "Direksi", "Lead", "tim" berdiri sendiri, "komersil", "belum ada"; semua 10 kode SNX di badan (kecuali kode dokumen ini) ada di tabel Dokumen Terkait; nol kalimat identik di dua bagian (satu-satunya duplikat adalah baris header tabel Daftar Periksa, delapan kali, karena satu tabel per kelompok).
- tools/selftest.sh tidak dijalankan. Berkas tools, template, config, control, reference, ledger, out, qa tidak diubah. Berkas yang saya tulis hanya specs/LEG-FRM-01.json dan notes/LEG-FRM-01.md; hasil render hanya di /tmp/pen-LEG-FRM-01/. Berkas lain yang terlihat berubah di `git status` (ledger.json, reports/orch/*, notes/COM-SOP-02.md, specs/COM-SOP-02.json, qa/COM-SOP-02.lint.json, out/05_Commercial/...) bukan hasil kerja saya.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Customer Contract Review Checklist (Google Doc), sumber utama | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY | 2026-10-13T16:04:38.493Z (nilai dari prompt; get_file_metadata tidak dimuat di sesi ini, tidak diukur ulang) | read_file_content, teks penuh. 10 bagian (Identitas Dokumen sampai Riwayat Perubahan), 22 baris aspek dalam 8 kelompok, kolom Hal yang Diperiksa, Status, Catatan/Tindak Lanjut kosong. download_file_content tidak dipakai karena struktur tabel sudah terbaca lengkap dan tercatat di context/audit |
| SOP Contract Review and Legal Approval (draf tim), bahan isi kolom Hal yang Diperiksa | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE | 2026-10-14T09:08:19.129Z (dari notes/LEG-SOP-02.md, tidak diukur ulang di sesi ini) | read_file_content, teks penuh. Daftar sumber ini di checklist ada di butir "Referensi dan Dokumen Terkait" sebagai "Contract Review Checklist" |
| SOP Divisi Legal | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (dari notes/LEG-SOP-02.md, tidak diukur ulang) | read_file_content, teks penuh. Bahan tiga baris tambahan (butir 4.1 "Klausul kritis yang wajib diperiksa") |
| Kriteria penerimaan | config/checklist.json baris 41 | tidak berlaku | Description: "Dokumen berisikan daftar periksa untuk meninjau \nkontrak customer dan mengidentifikasi risiko hukum \nserta komersial." Klausul ISO di checklist: kosong (iso_9001 dan iso_27001 null) |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md, bagian "legal/LEG-Checklist-Contract-Review.md" (baris 162 sampai 373, sampai sebelum bagian "## 6. Kata kunci retrieval" milik berkas berikutnya) | salinan audit 13 sampai 14 Okt | DATA. `grep -n 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY context/audit/*.md`: baris 169 dan 315 (legal), baris 83 (sintesis) |
| Peran | specs/HR-ORG-01.json (DONE), config/defaults.json | repo kerja | Matriks peran: Line Manager Legal = Legal & Compliance (JA-08), Staff Legal = Legal & Compliance (JA-09), keduanya "(USULAN), menunggu konfirmasi (K-13)". Penomoran butir SNX-LEG-SOP-01 dan SNX-LEG-SOP-02 yang saya rujuk mengikuti specs/LEG-SOP-01.json dan specs/LEG-SOP-02.json saat penyusunan; pembaca wajib menurunkan ulang bila spec itu berubah |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Satu kalimat imperatif di checklist ("Catatan: checklist sesuai hasil penelaahan", "checklist sesuai dengan rekomendasi") adalah petunjuk pengisian formulir, diperlakukan sebagai isi dan ditulis ulang di Petunjuk Pengisian butir 5.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Cakupan: kontrak antara perusahaan dan pelanggan, enam jenis layanan atau kerja sama | "Daftar periksa ini digunakan untuk menelaah kontrak antara perusahaan dan pelanggan, termasuk perjanjian layanan teknologi informasi, layanan komputasi awan, penjualan perangkat keras, layanan implementasi, layanan pemeliharaan, dan bentuk kerja sama komersial lainnya." (Ruang Lingkup) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |
| 2 | Tujuan: identifikasi risiko hukum, kejelasan hak dan kewajiban, dan penelaahan sebelum penandatanganan oleh pihak berwenang | "untuk mengidentifikasi risiko hukum, memastikan kejelasan hak dan kewajiban para pihak, serta memastikan bahwa ketentuan kontrak telah ditelaah sebelum ditandatangani oleh pihak yang berwenang." (Tujuan) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |
| 3 | Rekomendasi punya tiga opsi yang berbeda dari tiga opsi Hasil Penelaahan; opsi ketiga menahan penandatanganan | "Belum direkomendasikan untuk ditandatangani karena terdapat risiko atau isu material yang belum diselesaikan." (Rekomendasi, opsi ketiga) | 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di spec |
|---|---|---|---|
| 1 | Unit Kerja di sumber "Legal dan Compliance"; tidak ada field Pemilik Dokumen | "Unit Kerja \| Legal dan Compliance" (Identitas Dokumen). Field lain (Nama Dokumen, Nomor Dokumen, Nomor Revisi, Tanggal Penerbitan, Disusun, Diperiksa, Disetujui, Status Dokumen) kosong | meta.department "Legal" (defaults), meta.process_owner |
| 2 | Informasi Kontrak 9 field, semua kosong | "Nama Klien", "Nama/Jenis Kontrak", "Nomor Kontrak", "Nilai Kontrak", "Jangka Waktu Kontrak", "Unit Kerja Pemohon", "PIC Internal", "Tanggal Penerimaan", "Target Penyelesaian" (Informasi Kontrak) | bagian Isi Formulir, tabel Informasi Kontrak |
| 3 | Daftar Periksa 8 kelompok, 22 aspek | Kelompok: "Identitas dan Kewenangan Para Pihak", "Ruang Lingkup dan Pelaksanaan", "Harga dan Pembayaran", "Hak, Kewajiban, dan Risiko Hukum", "Data, Kerahasiaan, dan Kekayaan Intelektual", "Jangka Waktu dan Pengakhiran", "Penyelesaian Sengketa dan Ketentuan Umum", "Persetujuan dan Penandatanganan" | bagian Isi Formulir, tabel Kelompok C1 sampai C8 |
| 4 | Kolom Daftar Periksa | "No." / "Aspek yang Ditelaah" / "Hal yang Diperiksa" / "Status" / "Catatan/Tindak Lanjut"; tiga kolom terakhir kosong di 22 baris | idem |
| 5 | Tiga opsi Hasil Penelaahan | "Tidak terdapat temuan berdasarkan pemeriksaan yang dilakukan"; "Terdapat temuan yang harus ditindaklanjuti sebelum penandatanganan."; "Diperlukan pembahasan lebih lanjut dengan unit kerja terkait." | Ringkasan Hasil Penelaahan (kata sumber dipertahankan; hanya "unit kerja terkait" ditulis "Unit Kerja Terkait" menurut tabel Istilah) |
| 6 | Tiga opsi Rekomendasi | "Dapat dilanjutkan ke tahap persetujuan dan penandatanganan."; "Dapat dilanjutkan setelah tindak lanjut yang disyaratkan diselesaikan dan diverifikasi." | Rekomendasi |
| 7 | Tiga field isian ringkasan | "Temuan utama dan Risiko Hukum"; "Perubahan atau tindak lanjut yang diperlukan"; "Pihak yang bertanggung jawab dan target penyelesaian"; "Dasar rekomendasi" (masing-masing "…") | Temuan Utama dan Risiko (tabel 7 kolom); Dasar rekomendasi |
| 8 | Blok persetujuan | "Tahapan \| Nama/Jabatan \| Tanggal \| Tanda Tangan" dengan baris "Disusun oleh", "Diperiksa oleh", "Disetujui oleh" | Catatan Penelaahan dan Persetujuan |
| 9 | Tiga lokasi penyimpanan | "Lokasi kontrak yang ditelaah", "Lokasi hasil penelaahan", "Lokasi korespondensi", masing-masing "[lokasi/tautan berkas]" | Lokasi Penyimpanan Dokumen (placeholder dikosongkan) |
| 10 | Checklist dipakai bila dipilih | "checklist review, jika digunakan;" (SOP Contract Review, Review dan Persetujuan Legal butir 1.2) | Ketentuan butir 1; USULAN 12 |
| 11 | Risiko hukum dan komersial diidentifikasi, tingkat Tinggi, Sedang, Rendah | "SOP ini juga bertujuan untuk memastikan bahwa risiko hukum dan komersial diidentifikasi" (Tujuan butir 2); tabel "Tingkat Risiko \| Kriteria Umum \| Penanganan" Tinggi, Sedang, Rendah (Identifikasi dan Klasifikasi Risiko) | Tujuan, Nilai Status dan Tingkat Risiko, tabel Temuan |
| 12 | DoA belum ada | "Batas persetujuan berdasarkan jenis dan nilai transaksi mengacu pada matriks DoA Perusahaan, yaitu [TBD]." dan "Apabila DoA belum tersedia atau kewenangan tidak jelas, Staff Legal mengeskalasi kepada Line Manager Legal untuk memperoleh konfirmasi tertulis dari pihak berwenang sebelum kontrak ditandatangani." (SOP Contract Review, Persetujuan Bisnis dan Persetujuan Berdasarkan DOA butir 4 dan 5); "Matriks delegasi wewenang (DoA) penandatanganan kontrak." (SOP Divisi Legal, Lampiran yang Disarankan, belum disusun) | C8.1, C8.2, peran Pejabat Berwenang |

### Asal isi kolom Hal yang Diperiksa

Kolom itu kosong di checklist (22 dari 22 baris). Agar daftar periksa dapat dipakai, tiap baris diisi dari dua dokumen tim yang menyebutnya sebagai acuan. Tidak ada kriteria baru di luar yang berlabel (USULAN) di spec.

| Aspek | Sumber isi (verbatim) | Berkas |
|---|---|---|
| C1.1 | "nama badan hukum dan bentuk badan usaha"; "alamat dan identitas perusahaan"; "akta pendirian dan perubahan serta dokumen pengesahan/penerimaan pemberitahuan yang relevan"; "NIB dan izin yang relevan dengan kegiatan usaha, jika diperlukan"; "informasi risiko atau sengketa yang relevan dan dapat diverifikasi" | 1E_8 (Pemeriksaan Awal) |
| C1.2 | "identitas serta kewenangan penandatangan"; "surat kuasa atau dasar kewenangan lainnya, jika relevan" | 1E_8 |
| C2.1 | "Kejelasan layanan, barang, pekerjaan, deliverable, dan tanggung jawab." | 1E_8 (tabel Aspek) |
| C2.2 | "deliverable" (aspek Ruang lingkup); "ruang lingkup dan deliverable" | 1E_8; 19pe butir 4.1 |
| C2.3 | "Denda atau sanksi yang relevan."; "SLA dan sanksi" | 1E_8; 19pe |
| C2.4 | "potensi tumpang tindih wilayah/produk/pihak dengan kontrak lain" | 19pe butir 4.1 |
| C3.1 | "PIC memastikan kesesuaian ketentuan komersial dengan kesepakatan bisnis." | 1E_8 (Persetujuan Bisnis butir 1) |
| C3.2 | "Harga, pajak, jadwal pembayaran, invoice, biaya tambahan, serta kondisi pembayaran."; "termasuk apakah pembayaran bergantung pada pembayaran klien akhir" | 1E_8; 19pe |
| C3.3 | "Harga, pajak, jadwal pembayaran, invoice, biaya tambahan, serta kondisi pembayaran." | 1E_8 |
| C3.4 | idem (biaya tambahan) | 1E_8 |
| C4.1 | "Pembagian kewajiban serta mekanisme pemenuhan prestasi."; "Keadaan ingkar janji, masa perbaikan, dan konsekuensinya." | 1E_8 |
| C4.2 | "Pembatasan tanggung jawab, ganti rugi, dan pengecualian yang relevan." | 1E_8 |
| C4.3 | idem; "tanggung jawab yang tidak dibatasi atau tidak proporsional" | 1E_8 (Identifikasi Risiko butir 3) |
| C4.4 | "Keadaan kahar, pemberitahuan, dan akibat hukumnya." | 1E_8 |
| C4.5 | "hak penangguhan pembayaran atau layanan" | 19pe |
| C5.1 | "Cakupan informasi rahasia, pengecualian, dan kewajiban setelah kontrak berakhir." | 1E_8 |
| C5.2 | "Peran para pihak, tujuan pemrosesan, kewajiban keamanan, dan penanganan insiden jika relevan."; "dasar pemrosesan, peran (pengendali/prosesor), kewajiban keamanan, dan notifikasi insiden" | 1E_8; 19pe butir 4.5 |
| C5.3 | "Kepemilikan, lisensi, penggunaan, dan hasil pekerjaan."; "IP didaftarkan atas nama pihak lain" | 1E_8; 19pe bagian 5 |
| C5.4 | "Kontrol yang dipersyaratkan, akses, pelaporan insiden, dan tanggung jawab pihak terkait." | 1E_8 |
| C6.1 | "Tanggal efektif, durasi, perpanjangan, dan batas pemberitahuan." | 1E_8 |
| C6.2 | "Dasar, prosedur, akibat, dan kewajiban setelah pengakhiran."; "tidak adanya mekanisme pengakhiran yang memadai" | 1E_8 |
| C7.1, C7.2 | "Hukum yang berlaku, forum, dan mekanisme penyelesaian sengketa." | 1E_8 |
| C7.3 | "Kesesuaian dengan lampiran, addendum, kontrak terkait, dan dokumen transaksi lainnya." | 1E_8 |
| C8.1 | "Persetujuan Legal tidak dengan sendirinya menggantikan persetujuan bisnis, keuangan, keamanan informasi, atau kewenangan penandatanganan yang dipersyaratkan." | 1E_8 (Definisi) |
| C8.2 | "Kontrak diajukan kepada pejabat yang berwenang sesuai DoA, anggaran dasar, surat kuasa, atau ketentuan internal yang berlaku."; kutipan DoA di fakta 12 | 1E_8 |

## 3. Asumsi

1. Kata "customer" di Description dibaca sebagai "pelanggan" (kata di sumber). Seluruh dokumen memakai "pelanggan".
2. Unsur "komersial" di Description dipenuhi lewat Tujuan, definisi Risiko komersial, kolom Jenis Risiko di tabel Temuan Utama dan Risiko, dan baris Harga dan Pembayaran. Sumber hanya menyebut "Risiko Hukum" pada field temuan; SOP Contract Review menyebut risiko hukum dan komersial (fakta 11).
3. Satu istilah dipakai: "formulir" untuk dokumen ini dan salinannya yang terisi, "daftar periksa" hanya untuk tabel Daftar Periksa dan judul unsur Description, "penelaahan" untuk pemeriksaan satu kontrak dengan formulir ini (definisi di tabel Istilah), "Departemen Legal" untuk Line Manager Legal dan Staff Legal, "Unit Kerja Pemohon" dan "PIC Internal" (nama field di sumber), "Pejabat Berwenang" (istilah SNX-LEG-SOP-02) untuk "pihak yang berwenang" di sumber. Nama jabatan dan judul dokumen yang memuat kata Legal (Legal & Compliance, Legal Operational, Persetujuan Legal) tidak diubah.
4. Kode aspek C1.1 sampai C8.2 dipakai untuk rujukan silang. Kolom "No." di sumber kosong; audit memakai kode yang sama. Nilai kode bukan fakta dari sumber.
5. Tidak ada diagram. Sumber tidak punya diagram (audit: "Tidak ada diagram di sumber (mermaid diturunkan dari teks)"), dan alur mermaid di audit memuat pemetaan opsi Hasil ke Rekomendasi yang audit sendiri sebut inferensi. Menggambarnya berarti memutus pemetaan itu (lihat Open items 3).
6. Identitas Dokumen di sumber (9 field) diwakili halaman depan dan tabel Identity; Riwayat Perubahan diwakili tabel Revision History template. Keduanya tidak diulang di badan dokumen. Satu baris riwayat revisi di sumber (kosong) tidak dibawa.
7. Satu tabel per kelompok (8 tabel) dipilih karena renderer tidak membuat baris judul kelompok tebal dalam satu tabel.
8. Rujukan butir SNX-LEG-SOP-01 dan SNX-LEG-SOP-02 dan kode SNX lain mengikuti worklist dan spec yang ada saat ini; kode itu belum berstatus sah.

## 4. Penanganan cacat context/audit

Bagian 5.1 (perubahan dari versi 3 halaman ke 6 halaman) dan 5.2 (celah versi baru). Butir 5.1 yang berstatus SELESAI atau tetap dinilai bersama butir 5.2.

| Cacat (audit) | Penanganan | Pemutus bila USULAN |
|---|---|---|
| 5.2.1 Template kosong; hanya Unit Kerja terisi | Identitas diisi dari data baris (nomor, department, klasifikasi, pemilik, penanda tangan, status Draft, revisi 00, YEARLY). Tanggal efektif tetap kosong. Sel isian per kontrak tetap kosong (form) | USULAN 1 (pemilik) |
| 5.2.2a Kolom Hal yang Diperiksa kosong 22 dari 22 | Diisi dari SOP Contract Review dan SOP Divisi Legal (tabel di atas). Empat baris tambahan dan empat kriteria berlabel (USULAN) | USULAN 2, 7, 9 sampai 12 |
| 5.2.2b Status tanpa nilai baku | Tiga nilai baku: Sesuai, Perlu Tindak Lanjut, Tidak Berlaku (USULAN) | USULAN 4 |
| 5.2.2c Tidak ada kolom tingkat risiko | Tabel Temuan Utama dan Risiko dengan kolom Jenis Risiko dan Tingkat Risiko; kriteria Tinggi, Sedang, Rendah dirujuk ke SNX-LEG-SOP-02 butir 4.8 sampai 4.10, tidak disalin (USULAN) | USULAN 3 |
| 5.2.3a "Perlindungan" vs "Pelindungan" | Ditulis "Pelindungan Data Pribadi" (judul UU, ejaan di SOP Divisi Legal butir 4.5 dan checklist tim lain). Dicatat sebagai perubahan ejaan baris C5.2 | Legal bila ingin sebaliknya |
| 5.2.3b "Kewenangan Penandatangan" dan "Kewenangan Penandatanganan" | Dibedakan menurut pihak: C1.2 Kewenangan Penandatangan Pelanggan, C8.2 Kewenangan Penandatanganan SINUX, dengan Hal yang Diperiksa yang berbeda (USULAN) | USULAN 8 |
| 5.2.4 Kelompok 7 hanya dua baris; Keadaan Kahar di kelompok 4 | Baris Konsistensi Dokumen ditambahkan di kelompok 7 (C7.3, USULAN). Keadaan Kahar tetap di kelompok 4 (urutan sumber dipertahankan) | USULAN 7 |
| 5.2.5 Cakupan terhadap 12 klausul kritis SOP Divisi Legal: butir 4 hak penangguhan, butir 12 tumpang tindih, butir 2 klien akhir, butir 9 sanksi, butir 5 perpanjangan | Hak penangguhan = baris C4.5 baru; tumpang tindih = baris C2.4 baru; klien akhir = Hal yang Diperiksa C3.2; sanksi dan service credit = C2.3; perpanjangan = C6.1 (sudah memuat kata itu) | USULAN 7 |
| 5.2.6 Tidak ada legalitas atau rekam jejak sengketa pelanggan; DoA tanpa pejabat | Legalitas dan informasi sengketa = Hal yang Diperiksa C1.1. DoA: C8.1 dan C8.2 merujuk matriks DoA dan konfirmasi tertulis lewat Line Manager Legal (bersumber SNX-LEG-SOP-02); pejabat tetap belum ditetapkan, jadi open item | Open items 1 |
| 5.2.7 Tidak ada kelompok Keamanan Informasi, subkontraktor, perubahan layanan, keberlangsungan layanan, jaminan | Keamanan Informasi = baris C5.4 baru (USULAN, aspek itu ada di SOP Contract Review). Kelompok lain tidak ditambahkan: sumbernya tidak memuat aspek itu untuk kontrak pelanggan (scope creep); dicatat di Open items 5 | USULAN 7; Open items 5 |
| 5.2.8 Tidak merujuk SNX-OPS-SOP-05 dan SOP-04, tidak ada kompensasi atau service credit | C2.3 memuat ketentuan kompensasi atau service credit dan pembanding SNX-OPS-SOP-05 (USULAN). SNX-OPS-SOP-04 tidak dirujuk: audit hanya menyebut SOP-05 untuk target SLA dan service credit | USULAN 10 |
| 5.2.9 Klasifikasi informasi pelanggan; formulir tanpa label | Formulir berlabel RESTRICTED (Internal) (data baris); C5.1 memuat pembanding klasifikasi menurut SNX-ISMS-PRO-01 (USULAN); Ketentuan butir 8 menyatakan formulir terisi RESTRICTED (Internal). Tiga tingkat "Rahasia, Internal, Publik" di SOP Divisi Legal tidak dipakai | USULAN 11 |
| 5.2.10 Tidak ada baris verifikasi izin usaha SINUX | Kalimat tambahan di C2.1 merujuk SNX-LEG-REG-01 (USULAN, audit menyebutnya inferensi) | USULAN 9 |
| 5.2.11 Tidak ada baris ketergantungan pada pihak ketiga (supplier FRM-03) | Tidak ditambahkan sebagai baris. Ketergantungan pembayaran pada pihak ketiga sudah tertangkap di C3.2. Sisanya di Open items 5 | Open items 5 |
| 5.2.12 Selisih lingkup dengan SOP Billing | Tidak diubah: fungsi dokumen berbeda (review kontrak, bukan penagihan). Lingkup formulir mengikuti sumber | tidak ada |
| 5.2.13 Tidak ada klausul ISO | Enam klausul diusulkan di bagian Acuan ISO dengan satu label "(USULAN, perlu konfirmasi konsultan)" | USULAN 19 |
| 5.1 butir 4 SELESAI (opsi Rekomendasi kini berbeda dari opsi Hasil) | Dipertahankan apa adanya | tidak ada |
| 5.1 butir 5 (kalimat "checklist sesuai ..." tanpa penjelasan tanda) | Diganti petunjuk eksplisit: ganti ☐ dengan ☒ (Petunjuk butir 5), dengan aturan satu atau lebih pilihan untuk Hasil dan satu pilihan untuk Rekomendasi (USULAN) | USULAN 5 |
| 5.1 butir 8 (placeholder "[lokasi/tautan berkas]") | Sel dikosongkan, petunjuk di Petunjuk butir 10; lokasi kerja folder Google Drive Legal (USULAN) | USULAN 15 |

Label field sumber: "Nama Klien" dan opsi "Tidak terdapat temuan berdasarkan pemeriksaan yang dilakukan" dikembalikan persis seperti sumber pada putaran perbaikan 1 (opsi itu tanpa titik, seperti sumber). Satu-satunya redaksi opsi yang berbeda dari sumber: opsi ketiga menulis "Unit Kerja Terkait" (istilah di tabel Istilah) untuk "unit kerja terkait".

Pemetaan peran ke SNX-HR-ORG-01: Staff Legal dan Line Manager Legal ada di matriks peran (JA-09 dan JA-08, USULAN K-13). Peran sumber yang tidak ada di sana dan pemetaannya: Unit Kerja Pemohon dan PIC Internal bukan jabatan melainkan peran proses (dibiarkan sebagai peran); Unit Kerja Terkait = unit di SNX-HR-ORG-01 (Finance, Accounting & Tax, Operation) sesuai bidang temuan; Pejabat Berwenang = jabatan terdekat Manajemen (Direktur Utama dan Direktur (COO), definisi di SNX-LEG-SOP-01) tetapi tidak ditulis sebagai pemegang karena matriks DoA belum terbit. Sebutan COO tidak muncul di badan dokumen sehingga aturan "Direktur (COO)" tidak terpakai. Samuel di badan dokumen ditulis "Direktur Utama" (satu kali, Kesimpulan).

## USULAN

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Process owner dan pemilik formulir = Line Manager Legal (sumber tanpa field Pemilik Dokumen; Unit Kerja "Legal dan Compliance"). Rekaman formulir terisi: pencatat Staff Legal, pemilik Line Manager Legal, selaras dengan records di specs/LEG-SOP-02.json ("pencatat Staff Legal; pemilik Line Manager Legal (butir 4.19)") dan di specs/LEG-SOP-03.json (semua kategori: "pemilik Line Manager Legal") | Legal |
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
| 13 | Wajib atau tidaknya formulir ini untuk setiap kontrak pelanggan (SNX-LEG-SOP-02 menyebut checklist review "jika digunakan") | Legal |
| 14 | Formulir baru untuk setiap telaah ulang kontrak yang berubah material | Legal |
| 15 | Folder Google Drive departemen Legal sebagai lokasi formulir terisi dan lokasi kontrak (mengikuti SNX-LEG-SOP-01 butir 4.24) | Legal |
| 16 | PIC Internal setara PIC Bisnis, dan Unit Kerja Pemohon setara Pemohon, di SNX-LEG-SOP-02 | Legal |
| 17 | Pengecualian lingkup: kontrak vendor dan pemasok ke SNX-LEG-FRM-02; tinjauan pelindungan data yang menyeluruh ke SNX-LEG-FRM-03; padanan formulir ini dengan Contract Review Checklist di SNX-LEG-SOP-02 | Legal |
| 18 | Pemetaan Staff Legal dan Line Manager Legal ke JA-09 dan JA-08 (K-13 di SNX-HR-ORG-01) | Aziz |
| 19 | Enam klausul ISO: 9001 8.2.3, 8.2.4, 7.5.3; 27001 Annex A 5.31, 5.32, 5.34 (satu label "USULAN, perlu konfirmasi konsultan") | owner (konfirmasi konsultan) |
| 20 | Definisi Risiko hukum dan Risiko komersial di Istilah | Legal |
| 21 | Definisi "Klien akhir" sebagai pelanggan dari pelanggan SINUX (sumber SOP memakai kata itu tanpa definisi), dan "Klien" sebagai sebutan lain pelanggan pada field Nama Klien | Legal |
| 22 | Retensi formulir terisi mengikuti Kategori 4 (dokumen penelaahan Legal) dan retensi kontrak beserta korespondensi mengikuti Kategori 1 (dokumen kontraktual) di SNX-LEG-SOP-03; baris Rekaman dan Dokumen Terkait dirujukkan ke kategori itu | Legal |

## Open items

1. Matriks DoA belum terbit: pejabat untuk C8.1 dan C8.2 serta isi baris Disetujui oleh belum bisa ditetapkan. Pemutus: Samuel, owner.
2. Apakah Persetujuan Legal oleh Line Manager Legal sudah cukup sebagai "Disetujui oleh", atau diisi Pejabat Berwenang (USULAN 6). Pemutus: Samuel, Legal.
3. Sumber tidak memetakan opsi Hasil Penelaahan ke opsi Rekomendasi (misalnya apakah "Tidak terdapat temuan" selalu berarti "Dapat dilanjutkan"). Formulir mempertahankan keduanya sebagai pilihan terpisah. Pemutus: Legal.
4. Kriteria Hal yang Diperiksa belum ditinjau Legal; kolom Status dan Tingkat Risiko belum punya keputusan tertulis (USULAN 4 dan 3). Pemutus: Legal.
5. Aspek yang ada di checklist vendor tetapi tidak ditambahkan di sini: subkontraktor, perubahan layanan, keberlangsungan layanan, jaminan dan kualitas, ketergantungan pada pihak ketiga (audit 5.2.7 dan 5.2.11). Scope creep terhadap Description; Legal memutuskan perlu tidaknya.
6. Pengelolaan nomor: sumber tidak bernomor, SNX-LEG-FRM-01 dari worklist. Tidak ada nomor lama untuk diganti.
7. Ejaan "Pelindungan" vs "Perlindungan" di C5.2 belum diputus Legal; checklist tim lain memakai "Pelindungan".
8. Penomoran butir SNX-LEG-SOP-01 (4.21, 4.24) dan SNX-LEG-SOP-02 (4.2, 4.7, 4.8 sampai 4.10, 4.14, 6.1, 6.4, 6.7) harus dicek ulang bila kedua SOP itu direvisi. Pemutus: orkestrator saat render ulang massal.
9. modifiedTime 1E_8 dan 19pe tidak diukur ulang di sesi ini (diambil dari notes/LEG-SOP-02.md). Pemutus: orkestrator bila perlu.
10. Retensi formulir terisi dan kontrak mengikuti Kategori 4 dan Kategori 1 di SNX-LEG-SOP-03 (USULAN 22); periode angkanya hanya ada di SNX-LEG-SOP-03 dan belum diputus. Pemutus: Legal.

## 5. Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?**
Temuan dan perbaikan:
- Benda diberi kata kerja manusia. Klaim awal saya di bagian ini (hanya Tujuan yang perlu diperbaiki, dan pola itu tidak ada lagi) keliru: verifikator menemukan tujuh kalimat lain, dan pemindaian saya hanya menangkap kalimat Tujuan. Sudah ditulis ulang pada putaran perbaikan 1 (lihat bagian 6): pelaku diganti peran dari bagian Peran, atau kalimat dirumuskan sebagai isi ("Aspek C5.3 mencakup pemeriksaan ...").
- Baris relasi di Dokumen Terkait memakai kata "review" di satu tempat dan "penelaahan" di tempat lain untuk hal yang sama, dan bagian lain memakai "dokumen ini" untuk "formulir ini". Disamakan menjadi "formulir ini" dan "penelaahan"; "Contract Review Checklist" tetap sebagai nama berkas SOP-02.
- Label (USULAN) muncul 38 kali. Itu mekanis tetapi dibutuhkan (RUNBOOK §6a.3); label hanya dipasang pada kalimat yang tidak bersumber dari checklist atau dua SOP tim, dan satu kalimat pengantar menyatukan label enam aspek tambahan.
- Kolom Hal yang Diperiksa berupa frasa benda berderet ("Tanggal efektif, durasi, perpanjangan, dan batas pemberitahuan"). Itu bentuk yang dipakai SOP tim sendiri (T1), jadi dipertahankan, bukan diganti kalimat utuh. Daftar tiga unsur yang muncul berasal dari sumber (Hasil: tiga opsi, Status: tiga nilai usulan dari tiga status minimal yang dibutuhkan), bukan dipaksakan.
- Tidak ada atribusi kabur, frasa otoritas semu, ekor penegas, rentang palsu, kutip atau huruf kapital untuk penekanan, penutup positif, dan penegasan kosong (diperiksa dengan pola di atas).

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**
- Nama orang: hanya Samuel Kristanto Utomo / President Director (defaults), sebutan "Direktur Utama" di Kesimpulan. Tidak ada nama lain.
- Angka: "delapan kelompok" (Istilah; sumber 8 kelompok), "sembilan field" (Petunjuk butir 1; sumber 9 field), "empat baris tabel Temuan" (kerangka isian, bukan fakta), nomor butir SNX-LEG-SOP-01 dan SNX-LEG-SOP-02 dan kode klausul ISO (berlabel USULAN untuk ISO; butir SOP bersumber dari spec rekan). Tidak ada angka waktu, SLA, nilai, atau persentase di dokumen.
- Tanggal: tidak ada. Tanggal efektif kosong, tidak ada tanggal mundur.
- Sistem: Google Drive (USULAN, mengikuti SNX-LEG-SOP-01 butir 4.24). Zammad dan GLPI tidak disebut karena sumber tidak membutuhkannya.
- Kode dokumen SNX lain (LEG-SOP-01 sampai 03, LEG-FRM-02 dan 03, LEG-REG-01, ISMS-PRO-01 dan SOP-01, OPS-SOP-05, HR-ORG-01): semua ada di worklist.json. Isi hubungan yang diklaim tiap kode berlabel (USULAN) bila tidak bersumber (FRM-02, FRM-03, REG-01, ISMS-SOP-01, OPS-SOP-05).
- Satu klaim bersumber dari kutipan audit, bukan dari berkas aslinya: isi SNX-OPS-SOP-05 ("Bahasa kompensasi atau service credit hanya ada di dokumen kontraktual") dan SNX-ISMS-PRO-01 ("Informasi pelanggan minimal RESTRICTED") dan SNX-ISMS-SOP-01 (notifikasi insiden). Ketiga berkas itu belum saya buka; dalam dokumen hanya dipakai sebagai pembanding berlabel (USULAN), tanpa angka.

## 6. Putaran perbaikan 1 (temuan qa/LEG-FRM-01.verify.r1.json)

| # | Temuan | Perubahan di specs/LEG-FRM-01.json |
|---|---|---|
| 1 | Pemblokir: benda sebagai pelaku (tujuh kalimat) | Lingkup: "Departemen Legal memakai formulir ini untuk menelaah kontrak ..." dan "Staff Legal menyesuaikan penelaahan dengan ...". Pengecualian: "Formulir ini hanya memuat catatan risikonya" dan "... hanya memuat pemeriksaan ketentuan kontraknya". Peran Unit Kerja Terkait: "bila Staff Legal mencentang pilihan pembahasan lebih lanjut pada Hasil Penelaahan". Acuan ISO 8.2.3, 8.2.4, 7.5.3, 5.31: pelaku Staff Legal; 5.32 dan 5.34: "Aspek C5.3 (C5.2) mencakup pemeriksaan ...". Pemindaian luas atas seluruh spec (subjek Formulir, Tabel, Aspek, Daftar Periksa, Hasil Penelaahan, Penelaahan, Kolom, Prosedur, Butir, kode SNX, Rekomendasi, Temuan, Status, Persetujuan Legal dengan kata kerja menelaah, memeriksa, meminta, menetapkan, memutuskan, mengatur, menyebut, menunjuk, menentukan, memastikan, mengidentifikasi, mencatat, menggantikan) juga menemukan dan memperbaiki: "Butir 4.21 mengatur ... butir 4.24 menunjuk ..." menjadi "memuat"; "Formulir terisi memuat ... sehingga memakai tingkat RESTRICTED" menjadi "Staff Legal memberinya tingkat RESTRICTED (Internal)"; "Persetujuan Legal tidak menggantikannya" (C8.1 dan Ketentuan butir 6) menjadi "bukan pengganti". Sisa temuan pemindaian hanya kalimat dengan pelaku Departemen Legal |
| 2 | Pemilik rekaman beda dengan SNX-LEG-SOP-02 | Tabel Rekaman dan peran Line Manager Legal: pencatat Staff Legal, pemilik Line Manager Legal (USULAN, SNX-LEG-SOP-02 butir 4.19), sama dengan records di specs/LEG-SOP-02.json. USULAN 1 di atas diperbarui |
| 3 | Baris Dokumen Terkait SNX-LEG-SOP-02 | "Prosedur itu memakai istilah checklist review dan mencantumkan formulir ini sebagai SNX-LEG-FRM-01, checklist review untuk kontrak pelanggan (USULAN)." Sesuai related_documents di specs/LEG-SOP-02.json |
| 4 | Satu istilah "Departemen Legal" | "rekomendasi Legal" menjadi "rekomendasi Departemen Legal"; "selain Legal" menjadi "selain Departemen Legal"; "folder Google Drive departemen Legal" menjadi "Departemen Legal" (Ketentuan butir 8 dan tabel Rekaman); "menunggu keputusan Legal" menjadi "Line Manager Legal"; "(USULAN: diputuskan Legal)" menjadi "(USULAN: Line Manager Legal memutuskan)". Istilah "Penelaahan" didefinisikan ulang agar cocok dengan pemakaiannya sebagai tindakan: "Pemeriksaan satu kontrak pelanggan dengan formulir ini, dari pengisian Informasi Kontrak sampai Rekomendasi." |
| 5 | Satu kata kerja untuk menandai kotak | Ketentuan butir 5, Petunjuk butir 5, dan kalimat di Isi Formulir sekarang memakai "mencentang" dengan tanda ☒ pada kotak ☐ |
| 6 | Kalimat pasif "Penelaahan disesuaikan ..." | "Staff Legal menyesuaikan penelaahan dengan jenis layanan, karakteristik transaksi, dan risiko tiap kontrak." |
| 7 | Label sumber diubah tanpa catatan | "Nama Klien" dan "Tidak terdapat temuan berdasarkan pemeriksaan yang dilakukan" dikembalikan persis seperti sumber. USULAN 21 dihapus (tinggal 20 butir). Catatan redaksi tersisa di bagian 4 |

Hasil uji sesudah putaran 1: render exit 0; lint_doc generic "pass": true; validator OOXML lulus; PDF 16 halaman. Hasil uji akhir ada di bagian 7.

## 7. Putaran perbaikan 2 (temuan qa/LEG-FRM-01.verify.r2.json)

| # | Temuan | Perubahan di specs/LEG-FRM-01.json |
|---|---|---|
| 1 | Pemblokir: pengantar Daftar Periksa menyebut Hal yang Diperiksa diisi Staff Legal | Kalimat menjadi "Staff Legal mengisi kolom Status dan Catatan/Tindak Lanjut sesuai Petunjuk Pengisian." Pemindaian atas semua kalimat yang memuat "Hal yang Diperiksa", "centang", "diisi", "ditulis", "memakai": hanya Petunjuk butir 2 (membaca tanpa mengubah), definisi Status Sesuai, dan header tabel yang menyebutnya; tidak ada kalimat lain yang bertentangan |
| 2 | Pasif tanpa pelaku | Ketentuan butir 1: "Staff Legal memakai satu formulir untuk satu kontrak pelanggan dan mengisinya sesudah Unit Kerja Pemohon menyerahkan permintaan penelaahan secara lengkap". Petunjuk butir 1, 2, 6: pelaku Staff Legal |
| 3 | Benda sebagai pelaku di Istilah dan Dokumen Terkait | "Kolom Status berisi satu dari tiga nilai", "Kolom Tingkat Risiko ... berisi nilai Tinggi, Sedang, atau Rendah", Petunjuk butir 3 "berisi"; baris SOP-02: "Formulir ini tercantum di prosedur itu sebagai SNX-LEG-FRM-01, checklist review untuk kontrak pelanggan (USULAN)." |
| 4 | Perintah mencentang tiga kali | Instruksi lengkap (tanda ☒ pada kotak ☐) hanya di Petunjuk butir 5. Ketentuan butir 5 dan paragraf di Isi Formulir merujuk butir itu; aturan jumlah pilihan tetap di Ketentuan butir 5 |
| 5 | "pihak berwenang" di tabel pengecualian | Menjadi "Tetap milik Pejabat Berwenang dan Unit Kerja Terkait sesuai bidangnya". Kalimat sumber SNX-LEG-SOP-02 ("pihak berwenang di bidangnya") tidak membedakan keduanya; pemetaan ke dua peran terdefinisi saya pilih karena keputusan transaksi ada pada Pejabat Berwenang dan masukan bidang pada Unit Kerja Terkait |
| 6 | Rujukan silang tabel Peran | Line Manager Legal: "Ketentuan butir 1, 2, 4, 5, dan 6". Unit Kerja Pemohon: butir 1 dan 2 sekarang menyebutnya (penyerah permintaan) |
| 7 | Baris SNX-HR-ORG-01 | "Line Manager Legal dan Staff Legal adalah nama peran di matriks peran, dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09) (USULAN)." Label USULAN mengikuti butir K-13 di SNX-HR-ORG-01; pemutus Aziz (USULAN 18) |
| 8 | Kapitalisasi Jenis Risiko | "Hukum, Komersial, atau Hukum dan Komersial" (Petunjuk butir 6) |

Hasil uji akhir putaran 2 (diperbarui di bagian "Sweep"): render exit 0 (tanpa keluaran); lint_doc generic "pass": true, fails kosong, satu warn (28 butir USULAN); validator OOXML "All validations PASSED!"; nol em-dash dan en-dash di spec; PDF 16 halaman, halaman 5 sampai 16 berisi teks badan (126 sampai 371 kata per halaman, dihitung dengan pdftotext), halaman 1 sampai 4 adalah sampul, Identity, Revision History, Approval, dan daftar isi template.

## Sweep

Putaran sweep atas temuan qa/LEG-FRM-01.verify.json (verdict PASS, enam nonblocking) dan konsistensi Legal. Perubahan hanya di specs/LEG-FRM-01.json (builder di /tmp/pen-LEG-FRM-01, bukan di repo) dan notes ini. Fakta, angka, nama, dan struktur lain tetap.

Butir 1 (r3 nonblocking):
- Pengulangan Istilah dan Petunjuk, Status: Petunjuk butir 3 "Kolom Status berisi satu dari tiga nilai pada bagian Istilah." menjadi "Staff Legal mengisi kolom Status dengan salah satu nilai di bagian Istilah." (daftar nilai tinggal di Istilah).
- Pengulangan Istilah dan Petunjuk, Tingkat Risiko: Petunjuk butir 6 "Kolom Tingkat Risiko memuat Tinggi, Sedang, atau Rendah." menjadi "Staff Legal mengisi kolom Tingkat Risiko dengan salah satu nilai di bagian Istilah."
- Pasif, Istilah Tidak Berlaku: "Alasan ditulis di Catatan/Tindak Lanjut." menjadi "Staff Legal menulis alasannya di Catatan/Tindak Lanjut."
- Pasif, pengecualian lingkup: "Tidak ditelaah dengan formulir ini." menjadi "Departemen Legal tidak menelaahnya dengan formulir ini."
- Pasif lain dengan pelaku diketahui, Istilah Aspek: "Satu hal pada kontrak yang ditelaah, ditulis satu baris pada tabel Daftar Periksa ..." menjadi "Satu hal pada kontrak yang ditelaah. Tiap aspek mendapat satu baris pada tabel Daftar Periksa ...". Petunjuk butir 4: "... dan perubahan yang diminta." menjadi "... dan usulan perubahan." (kata "usulan perubahan" dari SOP-02: "menyampaikan usulan perubahan kepada pihak lawan"). Pasif lain di spec dipindai dan dibiarkan: kalimat opsi Hasil dan Rekomendasi dari sumber (T1), "Hasil yang dijaga", dan "Jabatan pemegang peran ini belum ditetapkan" (pelaku belum ditetapkan, tercakup open item 1).
- Klien vs pelanggan: tambah baris Istilah "Klien | Sebutan lain untuk pelanggan pada field Nama Klien. Klien akhir adalah pelanggan dari pelanggan SINUX (USULAN)." Field Nama Klien dan "klien akhir" di C3.2 tetap seperti sumber. Definisi klien akhir tidak ada di sumber, sehingga berlabel USULAN 21.
- Kualifier C1.1 terpangkas: "Nama badan hukum dan bentuk badan usaha, alamat, serta kesesuaiannya dengan akta pendirian, akta perubahan, dan NIB pelanggan. Informasi risiko atau sengketa pelanggan yang dapat diverifikasi." menjadi "Nama badan hukum, bentuk badan usaha, dan alamat pelanggan. Kesesuaian identitas itu dengan akta pendirian dan perubahan serta dokumen pengesahan atau penerimaan pemberitahuan yang relevan. NIB dan izin yang relevan dengan kegiatan usaha, jika diperlukan. Informasi risiko atau sengketa pelanggan yang relevan dan dapat diverifikasi." (kata sumber: "NIB dan izin yang relevan dengan kegiatan usaha, jika diperlukan").
- Dua "dan" berderet di Tujuan: "... mengidentifikasi risiko hukum dan risiko komersial dan memastikan hak dan kewajiban para pihak jelas." menjadi "... mengidentifikasi risiko hukum serta risiko komersial, dan memastikan hak dan kewajiban para pihak jelas."
- Petunjuk butir 1 nilai literal: "... dan menulis tidak ada pada field yang tidak ada di kontrak." menjadi "... dan menulis tanda strip (-) pada field yang tidak ada di kontrak." Ini konvensi pengisian, bukan fakta; diusulkan pemeriksa, tidak berlabel.

Butir 2 (konsistensi Legal):
- Nama peran: Peran Staff Legal "Dipetakan ke Legal & Compliance (JA-09) di SNX-HR-ORG-01 ..." menjadi "Peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." Sama untuk Line Manager Legal (JA-08), rumusan SNX-LEG-SOP-03. Baris SNX-HR-ORG-01 di Dokumen Terkait: ", dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09) (USULAN)" menjadi ", dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09), menunggu konfirmasi (K-13) (USULAN)". Tidak ada kalimat lain di spec yang menyebut Line Manager Legal atau Staff Legal sebagai nama jabatan (diperiksa dengan pencarian "jabatan" di spec: kata itu hanya muncul pada pemetaan JA-08 dan JA-09 di Peran dan Dokumen Terkait, pada jabatan pemegang peran Pejabat Berwenang, pada Petunjuk butir 7 (jabatan penanggung jawab tindak lanjut), dan pada Petunjuk butir 9 (nama dan jabatan penanda tangan).
- Pemilik rekaman: records di specs/LEG-SOP-03.json menetapkan pemilik Line Manager Legal untuk semua kategori; dokumen ini sudah memakai pemilik Line Manager Legal dan pencatat Staff Legal (selaras SNX-LEG-SOP-02 butir 4.19). Perubahan: pemilik di Peran dan tabel Rekaman kini merujuk "SNX-LEG-SOP-02 butir 4.19 dan SNX-LEG-SOP-03" (Peran Line Manager Legal dan dua baris Rekaman); Peran Staff Legal menyebut "sebagai pencatat rekaman". Tidak ada perbedaan pemilik yang perlu dijelaskan.
- Lokasi dan retensi mengikuti SNX-LEG-SOP-03: Ketentuan butir 8 "(USULAN, SNX-LEG-SOP-01 butir 4.24)" menjadi "(USULAN, SNX-LEG-SOP-01 butir 4.24 dan SNX-LEG-SOP-03 butir 4.8)". Kolom Retensi tabel Rekaman "Belum ditetapkan. Usulan penetapan ada di SNX-LEG-SOP-03." menjadi "Mengikuti Kategori 4 di SNX-LEG-SOP-03 (USULAN)." untuk formulir terisi (Kategori 4 = dokumen penelaahan Legal) dan "Mengikuti Kategori 1 di SNX-LEG-SOP-03 (USULAN)." untuk kontrak dan korespondensi (Kategori 1 = dokumen kontraktual dan dokumen terkait; apakah korespondensi termasuk Kategori 1 belum dikonfirmasi, USULAN 22). Angka periode tidak disalin ke dokumen ini. Baris Dokumen Terkait SNX-LEG-SOP-03 menjadi "Memuat tujuh kategori dokumen legal dan usulan periode retensinya. Formulir terisi masuk Kategori 4, dan kontrak beserta korespondensi masuk Kategori 1 (USULAN)."
- Formulir kosong (template) sendiri masuk Kategori 6 (dokumen internal Departemen Legal, "checklist" disebut di SNX-LEG-SOP-03); tidak ditambahkan sebagai baris Rekaman karena di luar butir sweep.

Hasil uji akhir sweep (bukti mentah: /tmp/pen-LEG-FRM-01/render.out.txt, /tmp/pen-LEG-FRM-01/lint.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-FRM-01.json /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx`: exit 0, tanpa keluaran.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx generic`: `"pass": true`, `"fails": []`, satu warn "32 butir (USULAN) menunggu ACC".
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx`: "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-FRM-01/LEG-FRM-01.docx`: `ok 16 LEG-FRM-01.docx []`.
- Nol em-dash dan en-dash di spec.
