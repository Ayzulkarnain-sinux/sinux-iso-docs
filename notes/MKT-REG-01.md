# Catatan penyusun MKT-REG-01: Marketing Content, Material & Claims Approval Register

Status: DRAFTED (spec + notes ada). Spec: specs/MKT-REG-01.json. Mode generic (doc_type_cover "REGISTER", doc_type_label "Register"), aksi T2, wave W7, nomor SNX-MKT-REG-01 (nomor SNX lama dipertahankan), department "Marketing", classification INTERNAL, audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Zilly Dwinata / Brand & Marketing", reviewed "Laras Rasmawati / VP Commercial", approved "Samuel Kristanto Utomo / President Director". process_owner "VP Commercial": dokumen tanpa sumber memakai jabatan reviewer departemennya (Marketing: Laras Rasmawati / VP Commercial), tanpa nama. Catatan worklist: kosong.

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-REG-01.json /tmp/pen-MKT-REG-01/MKT-REG-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-01/MKT-REG-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "31 butir (USULAN) menunggu ACC" (putaran sweep).
- Tata letak: docx dikonversi ke PDF dengan soffice (14 halaman). Putaran 0: halaman 7, 8, 10, dan 11 dilihat pada 70 dpi; header "Pemverifikasi" sempat terpotong dan judul h2 sempat dinomori 4.1 oleh renderer, keduanya diperbaiki. Putaran perbaikan 1 (kolom baris 58 ditambahkan): halaman 11, 12, dan 13 dilihat pada 70 dpi; header "Versi" di Tabel 1 sempat terpotong menjadi "Vers/i", kolom dilebarkan, halaman 11 dilihat ulang (terbaca utuh). Halaman lain tidak dilihat ulang sesudah putaran 1 (UNMEASURED). `python3 -I reports/orch/blankscan.py /tmp/pen-MKT-REG-01/MKT-REG-01.docx` memberi `ok 14` dengan daftar halaman kosong `[]`. Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py MKT-REG-01.docx`, dijalankan tanpa -I karena skrip itu mengimpor modul sebelahnya) memberi "All validations PASSED!". Putaran sweep: render 15 halaman; halaman 5 (Ruang Lingkup) dan halaman 9 (Peran) dilihat pada 70 dpi, tabel pengecualian dan tabel Peran terbaca utuh; halaman lain tidak dilihat ulang (UNMEASURED). `python3 -I reports/orch/blankscan.py` memberi `ok 15 []`, validator OOXML "All validations PASSED!".
- Kecocokan kode SNX di badan dengan tabel Dokumen Terkait diperiksa dengan skrip kecil (putaran sweep): 9 kode di badan (tambah SNX-MKT-REG-03), nol kode kurang, nol kode berlebih.
- Pola terlarang yang tidak ditembak lint (meta proses "sumber", "penyusun", "draf ini", "belum ada" untuk dokumen, em-dash, en-dash, tanda kutip, tanda bintang, "Lead", "dalam rangka", "adapun", ejaan "komersil" dan "diagnosa") dicari dengan skrip kecil pada teks spec. Dua temuan ("siapa pun penyusunnya", "datanya belum ada") ditinjau: yang pertama diganti, yang kedua menyangkut sel tabel dan dibiarkan.
- Lint dan skrip hanya membuktikan format dan larangan pola. Kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.
- Diagram: tidak ada. Register tidak memerlukan diagram dan kriteria baris 57 tidak memintanya.

## 1. Sumber

Prompt menyatakan sumber: tidak ada (T2 tanpa sumber). Tidak ada fileId yang ditugaskan. Alat Drive dimuat dan dipakai hanya untuk baca (get_file_metadata, read_file_content); nol tulis ke Drive. Berkas berikut dibaca sebagai bahan terkait karena peran dan klaim di register ini bersandar padanya.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist ISO SINUX - 2026, baris 57 (kriteria penerimaan) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (get_file_metadata hari ini, sama dengan config/checklist.json) | config/checklist.json baris 57: `checked: false`, `fileId: null`, `link_url: null`. Tidak ada berkas yang tertaut ke baris ini. Baris 56, 58, dan 59 dibaca sebagai pembanding |
| SINUX_Job_Analysis_2026.docx (HR-JA-001; JA-04, JA-05, JA-06, JA-08) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini) | read_file_content, teks utuh dibaca hari ini. Status di berkas itu: "DRAF – Menunggu verifikasi jabatan dan persetujuan Management" |
| SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io | 2026-10-13T06:09:00Z (get_file_metadata hari ini) | Kutipan tingkat PUBLIC diambil dari salinan context/audit/iso-sinux-supdocs-isms-2026-10-14.md dan specs/ISMS-PRO-01.json (Draft). Isi live tidak dibaca ulang (UNMEASURED) |
| Sales Playbook.xlsx | 1RVxuhUAFVTqwbtArb9uG4i2paG7Ph35w | 2026-10-13T06:31:48.927Z (get_file_metadata hari ini) | Hanya salinan context/audit (retrieved 2026-10-13). Dipakai untuk contoh jenis klaim. Isi live tidak dibaca (UNMEASURED) |
| KPI COMMERCIAL & MARKETING.xlsx | 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb | 2026-10-13T06:41:25.963Z (get_file_metadata hari ini) | Hanya salinan context/audit (retrieved 2026-10-13). Dipakai untuk open item volume konten. Isi live tidak dibaca (UNMEASURED) |
| Pendukung repo (bukan Drive) | - | - | config/defaults.json v21; specs/HR-ORG-01.json (nama peran, K-10, K-13); specs/ISMS-PRO-01.json (butir 4.1, 4.2, 4.5, definisi PUBLIC); specs/OPS-SOP-05.json (butir 4.1); specs/COM-SOP-02.json, specs/OPS-SOP-04.json (judul dan pembagian lingkup); specs/COM-REG-01.json (pola register Commercial). Dibaca sebagai DATA. Spec lane lain masih Draft; kutipan darinya bisa basi. specs/MKT-RPT-01 dan specs/MKT-REG-02 belum ada saat saya mulai menulis; sesudah register ini selesai keduanya muncul dan saya hanya membaca daftar bagian, ruang lingkup, dan rujukan ke MKT-REG-01 pada MKT-REG-02 (tanpa mengubahnya) |

Kalimat perintah kepada AI di semua sumber: nihil. Kalimat kewajiban untuk karyawan di Job Analysis ("Menjaga konsistensi pesan ...") adalah uraian jabatan, bukan instruksi untuk saya.

Pemetaan kriteria baris 57 dan baris 58 ke dokumen (keputusan cakupan orkestrator, putaran perbaikan 1: register ini memuat semua field kedua baris; SNX-MKT-REG-02 menjadi register pelaksanaan campaign dan aktivitas yang merujuk ke ID persetujuan di register ini):

| Unsur Description | Di dokumen |
|---|---|
| Mengendalikan materi untuk kebutuhan eksternal (baris 57 dan 58) | Tujuan, Ruang Lingkup, Dasar dan Ketentuan butir 4.1 sampai 4.16 |
| Cakupan: company profile, website, social media, product brochure, presentation deck, campaign material, event collateral (kata "termasuk" di kedua baris) | Ruang Lingkup, kalimat pertama ("termasuk", daftar tidak tertutup) |
| Field nama materi (57 dan 58) | Tabel 1, kolom Nama Materi |
| Field channel (57) dan jenis konten/channel (58) | Tabel 1, kolom Jenis Konten dan kolom Channel (dipisah) |
| Field produk/layanan terkait (58) | Tabel 1, kolom Produk atau Layanan Terkait |
| Field versi (57 dan 58) | Tabel 1, kolom Versi |
| Field lokasi file final (57 dan 58) | Tabel 1, kolom Lokasi File Final |
| Field PIC (57 dan 58) | Tabel 2, kolom PIC |
| Field reviewer/approver (57 dan 58) | Tabel 2, kolom Reviewer dan Approver (dipisah supaya dua peran yang berbeda terlihat) |
| Field tanggal persetujuan (57 dan 58) | Tabel 2, kolom Tanggal Persetujuan |
| Field status publikasi (57 dan 58) | Tabel 3, kolom Status Publikasi (lima nilai di bagian 3) |
| Field klaim yang perlu diverifikasi (58) | Tabel 4, kolom Klaim yang Perlu Diverifikasi |
| Field sumber/bukti pendukung (58) | Tabel 4, kolom Sumber atau Bukti Pendukung |
| Memastikan keakuratan informasi dan validasi klaim produk/layanan sebelum dipublikasikan (58) | Tujuan (Yang dijaga); butir 4.10 sampai 4.13; Tabel 5 (Pemverifikasi, Hasil Verifikasi, Tanggal Verifikasi) |
| Bukti: materi final dan approval sebelum dipublikasikan (57); materi final yang telah disetujui, bukti verifikasi klaim yang relevan, dan catatan persetujuan sebelum dipublikasikan (58) | Tabel 1 (Lokasi File Final), Tabel 2 (Bukti Persetujuan), Tabel 5 (Bukti Verifikasi), butir 4.6 dan 4.7 (persetujuan tertulis dan Tanggal Publikasi tidak lebih awal dari Tanggal Persetujuan), tabel Rekaman |
| Judul baris 57 memuat "Claims Approval" | Tabel 4 dan Tabel 5; butir 4.10 sampai 4.13 |
| Penautan dari register campaign ke persetujuan (keputusan orkestrator) | Kolom ID (ID persetujuan) di Tabel 1 sampai Tabel 3; baris Ruang Lingkup dan Dokumen Terkait untuk SNX-MKT-REG-02 (USULAN) |

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Register wajib memuat field baris 57 (delapan field) dan, menurut Description baris 58 yang memuat seluruh isi baris 57, tambahan jenis konten, produk atau layanan terkait, klaim yang perlu diverifikasi, dan sumber atau bukti pendukung; bukti berupa materi final, bukti verifikasi klaim, dan catatan persetujuan sebelum publikasi. Dasar struktur kolom Tabel 1 sampai Tabel 5 dan butir 4.6, 4.7, 4.10 sampai 4.13 | Baris 57: "Field minimum: nama materi, channel, versi, PIC, reviewer/approver, tanggal persetujuan, status publikasi, dan lokasi file final." dan "Bukti: materi final dan approval sebelum dipublikasikan." Baris 58: "serta memastikan keakuratan informasi dan validasi klaim produk/layanan sebelum dipublikasikan.", "Field minimum: nama materi, jenis konten/channel, produk/layanan terkait, versi, klaim yang perlu diverifikasi, sumber/bukti pendukung, PIC, reviewer/approver, tanggal persetujuan, status publikasi, dan lokasi file final." dan "Bukti: materi final yang telah disetujui, bukti verifikasi klaim yang relevan, serta catatan persetujuan sebelum dipublikasikan." (config/checklist.json, kolom Description) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist; baris 57 dan 58 sendiri `fileId: null`) |
| Brand & Marketing menyiapkan materi, menjaga persetujuan publikasi, menjadwalkan publikasi hanya setelah persetujuan, dan mengarsipkan materi serta izin penggunaan aset. Dasar peran pencatat dan PIC (butir 4.2, 4.3, 4.7, 4.14) dan kolom Lokasi File Final | "Menyiapkan materi brand, konten digital, company profile dan sales collateral." "Menjaga konsistensi pesan, identitas visual dan persetujuan publikasi." "Mengarsipkan materi, izin penggunaan aset dan evaluasi kegiatan." dan wewenang "Menjadwalkan publikasi setelah persetujuan" (JA-06, uraian 2, 3, 7 dan wewenang 2) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Materi pemasaran baru berklasifikasi PUBLIC setelah disetujui. Dasar butir 4.5 dan kolom Bukti Persetujuan sebagai syarat sebelum terbit | "PUBLIC" "Informasi yang disetujui untuk umum" "Company profile, materi pemasaran yang sudah disetujui, halaman website" (SNX-ISMS-PRO-01 bagian 4 Tingkat klasifikasi; juga ada di specs/ISMS-PRO-01.json bagian Definisi) | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |

Fakta penting lain:

| # | Fakta di dokumen | Kutipan verbatim | Posisi |
|---|---|---|---|
| 1 | Manager of Product Tech sebagai Pemverifikasi klaim produk (tabel butir 4.11) | "Memastikan kesiapan solusi dan validitas teknis produk yang ditawarkan perusahaan." dan wewenang "Memberi rekomendasi kelayakan teknis" | Job Analysis JA-05 tujuan jabatan dan wewenang 1, fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | VP Tech Operation and Services sebagai Pemverifikasi klaim kinerja layanan (tabel butir 4.11) | "Memastikan delivery proyek dan layanan teknis memenuhi scope, mutu, SLA dan kebutuhan pelanggan." | Job Analysis JA-04 tujuan jabatan, fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 3 | Legal & Compliance sebagai Pemverifikasi klaim sertifikasi, kepatuhan, izin, dan penyebutan pihak luar (tabel butir 4.11) | "Memberikan legal clearance/rekomendasi" | Job Analysis JA-08 wewenang 1, fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 4 | Bahasa kompensasi tidak boleh di materi pemasaran (butir 4.12) | "Bahasa kompensasi atau service credit hanya ada di dokumen kontraktual, tidak di materi pemasaran atau proposal." (angka availability di butir yang sama tidak dibawa) | specs/OPS-SOP-05.json butir 4.1 (repo, Draft) |
| 5 | Pemilik informasi menetapkan klasifikasi, dan hanya ia yang boleh menurunkannya (butir 4.5) | "Pemilik informasi menetapkan klasifikasi saat informasi dibuat atau diterima." dan "Hanya Pemilik informasi yang boleh menurunkan klasifikasi, dan penurunannya dicatat." | specs/ISMS-PRO-01.json butir 4.1 dan 4.2 (repo, Draft) |
| 6 | Materi dari Sales Playbook memuat klaim sertifikasi, kinerja, dan perbandingan biaya. Dasar jenis klaim di tabel butir 4.11 dan definisi Klaim | "Compliance: audit BI (Bank Indonesia), OJK (sektor keuangan), ISO 27001/9001 dalam progress." dan "Klaim komersial kunci di jawaban: Cloud SLA 99.9% uptime; support response 1 jam (kritis) dan 4 jam (tinggi); OrionVE \">60% TCO lebih murah\" vs VMware" (angka tidak dibawa ke dokumen) | context/audit/iso-sinux-supdocs-commercial-2026-10-14.md baris 579 dan 642 (salinan Sales Playbook), fileId 1RVxuhUAFVTqwbtArb9uG4i2paG7Ph35w |
| 7 | Company Profile dan Product Deck sudah dipakai Sales tetapi tidak bernomor dan tidak ada berkasnya di ledger. Dasar butir 4.15 (materi yang terbit sebelum register berlaku) | "Sales wajib memahami penggunaan: CRM; Sinux Knowledge Base; Company Profile; Product Deck; Proposal & Quotation Template; Pre-sales Request." dan "tidak ada berkas berjudul company profile pada ledger B1 sampai B7" | context/audit/iso-sinux-supdocs-commercial-2026-10-14.md baris 170 dan 346; Sales SOP fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| 8 | Brand & Marketing tidak punya wewenang persetujuan di proses penjualan. Dasar Approver bukan Brand & Marketing (butir 4.4) | "Tidak ada wewenang persetujuan di SOP ini." | specs/COM-SOP-01.json tabel peran, Brand & Marketing (repo, Draft) |

## 2. Keputusan data dan pemetaan peran

- Sebutan: Samuel di badan = "Direktur Utama" (kalimat setelah tabel Peran dan Kesimpulan); nama dan "President Director" hanya di blok approval. COO tidak disebut di badan, jadi aturan "Direktur (COO)" tidak terpakai. Nama Laras dan Zilly hanya di blok approval. Nol nama orang lain di dokumen.
- Process Owner di blok Identity = "VP Commercial". Di badan, VP Commercial adalah pemilik register (tabel Peran dan Rekaman).
- Tiket: Zammad untuk Ops, GLPI untuk generalist. Dokumen tidak menyebut tiket karena kanal permintaan verifikasi klaim belum ada di sumber mana pun: open item 4.
- Vault, PPN: tidak relevan, tidak disebut.
- Klasifikasi blok Identity: INTERNAL (worklist). Materi disetujui = PUBLIC menurut butir 4.5 (USULAN). Footer renderer tidak menampilkan label karena INTERNAL.
- Istilah: "materi" (bukan konten atau kolateral, kecuali dua nama jenis dari kriteria), "file final" (bukan berkas), "pihak luar" (bukan eksternal sebagai kata benda), "terbit" untuk status dan kata kerja, "publikasi" hanya untuk nama kolom dan kata benda, "Reviewer" dan "Approver" dengan huruf kapital sebagai istilah terdefinisi, "ID persetujuan" untuk nomor baris versi materi (header kolom "ID"), "jenis konten" hanya untuk kolom Jenis Konten dan definisinya (nama field dari baris 58).
- Peran yang menetapkan (Approver, Reviewer, Pemverifikasi) dibedakan dari peran yang mencatat (Brand & Marketing) di butir 4.2 sampai 4.14, tabel Peran, dan Cara Mengisi: semua penulisan ke Tabel 1 sampai Tabel 4 dilakukan Brand & Marketing.

Pemetaan peran sumber ke nama peran di tabel Peran (basis specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Brand & Marketing (JA-06) | Brand & Marketing | JA-06 |
| "Commercial - Laras Rasmawati" (atasan JA-06 di Job Analysis) | VP Commercial | JA-03; cacat Job Analysis nomor 6 (nama departemen ditulis sebagai atasan) |
| Manager of Product Tech (JA-05) | Manager of Product Tech | JA-05 |
| VP Tech Operation and Services (JA-04) | VP Tech Operation and Services | JA-04 |
| Legal & Compliance (JA-08, JA-09) | Legal & Compliance | JA-08 dan JA-09 memakai nama jabatan sama; Line Manager Legal dan Staff Legal belum dipetakan (K-13), jadi tidak dipakai |
| Pemilik informasi (SNX-ISMS-PRO-01) | Pemilik informasi (peran menurut PRO-01, dipegang VP Commercial: USULAN 6) | ISMS-REG-01 menentukan pemilik aset; tidak dibaca. Penurunan klasifikasi hanya oleh Pemilik informasi (PRO-01 butir 4.2) |
| ISMS Coordinator | tidak dipakai | HR-ORG-01 K-13: belum ditetapkan |
| Service Delivery Manager (pemilik SNX-OPS-SOP-05) | tidak dipakai | HR-ORG-01 K-10: jabatan usulan tanpa pemegang. Klaim kinerja layanan ke VP Tech Operation and Services |
| Direktur (COO) | tidak dipakai | Tidak punya tugas pada register ini |

## 3. Penanganan cacat context/audit

Perintah: `grep -n "Marketing Content, Material & " context/audit/*.md` memberi nol baris. Judul register ini tidak punya bagian di context/audit, jadi tidak ada bagian 5 Catatan kualitas dan celah untuk dokumen ini sendiri. Grep pendukung: `grep -n -i "marketing" context/audit/*.md` dan `grep -n -i "company profile\|brand guideline\|positioning" context/audit/*.md`. Dari hasilnya saya membaca bagian 5 Job Analysis (HR-JA-001, fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1), karena peran di register ini bersandar padanya, dan butir 13 daftar open item di sintesis.

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Job Analysis berstatus DRAF, nomor "usulan", bukan dokumen terkendali (bagian 5 nomor 1) | Peran Brand & Marketing dan ketiga Pemverifikasi bersandar pada dokumen Draft. Semua penugasan Pemverifikasi berlabel USULAN. Open item 4 |
| 2 | Atasan JA-06 ditulis "Commercial - Laras Rasmawati", bukan jabatan (nomor 6) | Dokumen memakai "VP Commercial" menurut HR-ORG-01 (JA-03) |
| 3 | Dua jabatan berjudul "Legal & Compliance" tanpa pembeda; Line Manager Legal dan Staff Legal tidak dipetakan (nomor 9) | Dokumen memakai "Legal & Compliance" tanpa pembeda, mengikuti HR-ORG-01. Pembeda tidak diperlukan karena tugas Pemverifikasi berlaku untuk jabatan itu |
| 4 | Ejaan Samuel Kristianto vs Kristanto, dan sebutan CEO (nomor 11) | Blok approval memakai "Samuel Kristanto Utomo / President Director" menurut defaults; badan memakai "Direktur Utama" |
| 5 | Teks Persyaratan tambahan dan Hubungan Kerja identik di 15 jabatan; frasa kompetensi janggal (nomor 4, 12) | Tidak menyentuh register ini; tidak ada kutipan dari bagian itu |
| 6 | Penamaan unit tidak seragam; Manager of Product Tech tidak konsisten (nomor 5, 8) | Tidak menyentuh register ini |
| 7 | Sintesis butir 13: klaim Sales Playbook bertentangan dengan KB (SLA 99.9% dan backup "setiap VM + standby", respons kritis 1 jam vs SNX-OPS-SOP-04 15 menit Ack, dan larangan positioning produk tertentu) | Register ini tidak dapat menyelesaikan pertentangan itu. Register menyediakan Tabel 4, Tabel 5, dan butir 4.12 supaya klaim jenis itu diperiksa sebelum terbit. Angka tidak dibawa ke dokumen. Open item 5 dan 8 |
| 8 | Company Profile dirujuk Sales SOP tetapi tidak bernomor dan tidak ada berkasnya di ledger (commercial, baris 346) | Butir 4.15 mengatur pencatatan materi yang sudah terbit sebelum register berlaku. Open item 7 |
| 9 | KPI Brand & Marketing: nama "Zilly" dan "Zily", blok OLD dan baru berbeda (commercial) | Nama hanya di blok approval dengan ejaan dari prompt ("Zilly Dwinata"); sama dengan HR-ORG-01 |

## 4. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Judul baris 57 memuat "Claims Approval" dan Description baris 58 memuat kriteria klaim (keakuratan informasi, validasi klaim, field klaim dan sumber/bukti pendukung, bukti verifikasi klaim). Sesuai keputusan cakupan orkestrator (putaran perbaikan 1), register ini memuat semua field baris 57 dan baris 58. Dasar Tabel 4 dan Tabel 5: judul baris 57 dan Description baris 58. Label (USULAN) hanya pada keputusan pembagian cakupan dengan SNX-MKT-REG-02 (register pelaksanaan campaign dan aktivitas yang merujuk tiap materi ke ID persetujuan di register ini), bukan pada keberadaan tabel klaim.
2. Satu baris = satu versi satu materi satu channel, dengan satu ID persetujuan, supaya Tanggal Persetujuan dan Tanggal Publikasi bisa dibandingkan per channel dan SNX-MKT-REG-02 dapat merujuk satu persetujuan. Tidak ada sumber yang menentukan satuan pencatatan (USULAN 3). Tabel 5 dipisah dari Tabel 4 supaya satu klaim punya satu baris di tiap tabel dan tabel tidak terlalu lebar untuk halaman portrait.
3. VP Commercial memegang Approver dan Reviewer untuk semua materi. Alasan: Job Analysis JA-06 tidak menyebut penyetuju publikasi; JA-06 bukan penyetuju (wewenang: mengusulkan, menjadwalkan, dan meminta koreksi); Sales SOP menyatakan Brand & Marketing tanpa wewenang persetujuan; JA-03 adalah atasan langsung JA-06. Penyetuju untuk company profile dan website bisa saja lebih tinggi: open item 2.
4. Lima nilai Status Publikasi (Draf, Dalam Peninjauan, Disetujui, Terbit, Ditarik) adalah susunan saya. Register Commercial (SNX-COM-REG-01) memakai tiga nilai status, tetapi tidak ada sumber untuk status materi pemasaran.
5. Pemetaan jenis klaim ke Pemverifikasi mengikuti tujuan jabatan dan wewenang di Job Analysis (kutipan di Fakta penting lain nomor 1 sampai 3). Tidak ada sumber yang menyebut jabatan itu memverifikasi klaim pemasaran.
6. Google Drive sebagai tempat simpan mengikuti SNX-ISMS-PRO-01 butir 4.8 (INTERNAL disimpan di sistem resmi SINUX, termasuk Drive). Jalur folder tidak diketahui dan tidak dikarang. Departemen Commercial dipakai karena JA-06 berunit Commercial.
7. Nol angka waktu atau nilai di dokumen. Tidak ada tenggat peninjauan, batas jumlah klaim, atau persen. Angka dari bahan terkait (99.9%, 1 jam, 15 menit, 60%, 12 konten per bulan) sengaja tidak disalin. Angka yang ada hanya nomor butir, nomor klausul ISO, kode JA, dan "10 baris" (USULAN 1).
8. Klausul ISO di Acuan ISO berasal dari pengetahuan standar saya, tidak dicocokkan dengan teks standar (UNMEASURED), semuanya di bawah satu label "(USULAN, perlu konfirmasi konsultan)". 9001: 8.2.1 (komunikasi dengan customer, termasuk informasi tentang produk dan jasa), 8.2.2 (klaim tentang produk dan jasa dapat dipenuhi), 7.5.3 (versi, lokasi, akses). 27001: Annex A 5.12 (klasifikasi), 5.32 (hak kekayaan intelektual, untuk izin penggunaan aset). Klausul 7.4 (komunikasi) dan 7.5.2 tidak dimasukkan karena tumpang tindih dengan 8.2.1 dan 7.5.3.
9. Tanggal dan nomor versi: tidak ada tanggal di dokumen. Penomoran versi dimulai dari 1 dan naik satu (butir 6.4, USULAN lewat butir 4.8). Format tanggal tidak ditetapkan; Cara Mengisi hanya meminta "tanggal lengkap".
10. Definisi Customer disamakan dengan register Commercial (SNX-COM-REG-01) agar istilah konsisten antar departemen; tidak ada rujukan butir karena kodenya tidak dipakai di badan.

## USULAN

Hitungan di paragraf ini dari sebelum W9 (diubah W9: sesudah W9 lint menghitung 25 butir USULAN). Spec memuat 31 kemunculan persis "(USULAN)" (satu di antaranya baris definisi label itu sendiri) dan satu label "(USULAN, perlu konfirmasi konsultan)" pada Acuan ISO. Dikelompokkan jadi 20 butir keputusan. Sesuai putaran perbaikan 1, label tidak dipasang pada keberadaan Tabel 4 dan Tabel 5 (dasarnya judul baris 57 dan Description baris 58); label ada pada pembagian cakupan dan butir yang tidak punya dasar tertulis.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Pembagian kolom ke Tabel 1 sampai Tabel 5 dan 10 baris tersedia (field-nya dari baris 57 dan 58; pengelompokannya susunan saya) | Isi Register | owner |
| 2 | Pembagian cakupan: register ini memuat semua field baris 57 dan 58; SNX-MKT-REG-02 menjadi register pelaksanaan campaign dan aktivitas yang merujuk tiap materi ke ID persetujuan di register ini (keputusan orkestrator) | Ruang Lingkup (baris pengecualian); Dokumen Terkait; Isi Register (kolom ID) | owner ; diubah W9: A8 diputus owner; REG-02 hanya mencatat pelaksanaan Aktivitas dan memuat ID Persetujuan Materi dari register ini, label batas dihapus |
| 3 | Satu baris per versi per materi per channel, dengan satu ID persetujuan; Tabel 1 sampai Tabel 3 memakai ID sama, Tabel 4 dan Tabel 5 memakai nomor klaim sama | Butir 4.1 | owner |
| 4 | Brand & Marketing sebagai pencatat dan PIC bawaan; VP Commercial dapat menunjuk PIC lain | Butir 4.2, 4.3 | owner |
| 5 | VP Commercial sebagai Approver semua materi dan Reviewer bawaan | Butir 4.4 | owner dan Samuel |
| 6 | VP Commercial sebagai Pemilik informasi atas materi; Pemilik informasi menurunkan klasifikasi INTERNAL menjadi PUBLIC saat Approver menyetujui versi, dan penurunan tercatat di bukti persetujuan yang sama | Butir 4.5; tabel Peran; Definisi; Rekaman; Acuan ISO | Fani ; diubah W9: Pemilik informasi mencatat penurunan klasifikasi di SNX-ISMS-REG-01 mengikuti SNX-ISMS-PRO-01, bukan di bukti persetujuan; register ini hanya merujuk |
| 7 | Persetujuan tertulis; persetujuan lisan tidak dihitung | Butir 4.6 | owner |
| 8 | Perubahan isi memicu versi baru dan baris baru; baris lama tidak dihapus | Butir 4.8 | owner |
| 9 | Status Ditarik; Approver memutuskan penarikan; Brand & Marketing menarik materi | Butir 4.9; Status Publikasi; Tabel 3 | owner |
| 10 | Lima nilai Status Publikasi | Definisi; butir 4.16 | owner |
| 11 | Pemverifikasi per jenis klaim: Manager of Product Tech, VP Tech Operation and Services, Legal & Compliance, dan jabatan yang VP Commercial tunjuk | Butir 4.11 dan tabelnya; tabel Peran | Fani dan Legal |
| 12 | Penolakan klaim availability atau SLA yang beda dari target standar, dan penolakan bahasa kompensasi di materi | Butir 4.12 | Fani |
| 13 | Approver tidak menyetujui versi yang memuat klaim tanpa sumber atau bukti pendukung, klaim tanpa hasil verifikasi, atau klaim yang ditolak | Butir 4.13 | owner |
| 14 | Bukti persetujuan dan bukti verifikasi disimpan di lokasi yang sama dengan file final; Google Drive folder departemen Commercial; pemilik rekaman | Butir 4.14; Rekaman | owner |
| 15 | Materi yang sudah terbit sebelum register berlaku dicatat sebagai Terbit, ditinjau Approver, Tanggal Persetujuan memakai tanggal peninjauan tanpa tanggal mundur, dikecualikan dari batas butir 4.7 | Butir 4.15 | owner dan Samuel |
| 16 | Batas cakupan dokumen Marketing (keputusan orkestrator): SNX-MKT-RPT-01 = rencana pemasaran dan tinjauan kinerja; SNX-MKT-REG-01 (register ini) = persetujuan materi eksternal dan validasi klaim; SNX-MKT-REG-02 = pelaksanaan campaign dan aktivitas yang menautkan materi ke ID persetujuan di register ini; SNX-MKT-REG-03 = hasil lead dan serah terima ke Sales. Pengecualian lain: proposal dan quotation per customer (SNX-COM-SOP-02), komunikasi insiden (SNX-OPS-SOP-04) | Ruang Lingkup; Dokumen Terkait | owner ; ditutup W9: batas dokumen Marketing sudah diputus owner (A8), label USULAN pada batas dihapus; REG-01 menjadi satu-satunya register materi, konten, dan persetujuan klaim |
| 17 | Retensi semua rekaman "Belum ditetapkan" dan lokasi di Rekaman | Rekaman | owner dan Legal |
| 18 | Pembagian tugas pada tabel Peran | Peran | owner |
| 19 | VP Commercial meninjau register setiap tahun | Kesimpulan | owner |
| 20 | Daftar klausul ISO 9001:2015 (8.2.1, 8.2.2, 7.5.3) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.32), label "(USULAN, perlu konfirmasi konsultan)" | Rekaman dan Acuan ISO | owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Selisih Description baris 57 (judul "Marketing Content, Material & Claims Approval Register") dan baris 58 (judul "Marketing Campaign & Activity Register"), terukur dari config/checklist.json. (a) Kalimat pertama: baris 58 menulis "materi dan konten pemasaran" (baris 57: "materi") dan menambah ekor ", serta memastikan keakuratan informasi dan validasi klaim produk/layanan sebelum dipublikasikan"; daftar jenis materi sama. (b) Field minimum: baris 57 menulis "channel", baris 58 menulis "jenis konten/channel" dan menyisipkan "produk/layanan terkait" (sesudah channel), "klaim yang perlu diverifikasi" dan "sumber/bukti pendukung" (sesudah versi); delapan field lainnya sama dan berurutan sama. (c) Bukti: baris 57 "materi final dan approval sebelum dipublikasikan"; baris 58 "materi final yang telah disetujui, bukti verifikasi klaim yang relevan, serta catatan persetujuan sebelum dipublikasikan". Judul baris 58 (campaign dan aktivitas) tidak cocok dengan isinya, sedangkan judul baris 57 ("Claims Approval") cocok. Keputusan cakupan orkestrator (USULAN, putaran perbaikan 1): register ini memuat semua field baris 57 dan 58; SNX-MKT-REG-02 menjadi register pelaksanaan campaign dan aktivitas yang merujuk tiap materi ke ID persetujuan di register ini. Perlu konfirmasi owner, dan checklist baris 58 perlu disesuaikan dengan keputusan itu | owner ; diubah W9: owner memutus A8; register ini satu-satunya register materi, konten, dan persetujuan klaim. Temuan baris 58 pindah ke open item 15 |
| 2 | Approver untuk semua materi saat ini VP Commercial. Belum diputus apakah company profile, website, dan klaim sertifikasi memerlukan persetujuan Direktur Utama, dan apakah Reviewer perlu orang yang berbeda dari Approver | owner dan Samuel |
| 3 | Lokasi folder Google Drive, pemilik folder, dan retensi file final, bukti persetujuan, bukti verifikasi, dan izin penggunaan aset belum ditetapkan di sumber mana pun | owner dan Legal |
| 4 | Penugasan Pemverifikasi (Manager of Product Tech, VP Tech Operation and Services, Legal & Compliance) bersandar pada Job Analysis yang berstatus DRAF. Kanal permintaan verifikasi klaim (Zammad untuk Ops, GLPI untuk generalist, atau lainnya) dan batas waktu verifikasi belum diputus. Batas lingkup "generalist" belum dirinci owner | Fani dan owner |
| 5 | Klaim di Sales Playbook (SLA, backup, respons kritis, perbandingan TCO, sertifikasi "dalam progress") bertentangan atau belum dibuktikan menurut sintesis butir 13. Register tidak menyelesaikan isinya; perlu keputusan angka dan kalimat klaim yang boleh dipakai di materi eksternal | Fani dan owner |
| 6 | Volume konten social media: KPI Brand & Marketing menyebut "Minimal 12 konten/bulan (relevant and engaging content with increasing engagement and reach)" (KPI COMMERCIAL & MARKETING.xlsx, fileId 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb, salinan context/audit baris 475). Pencatatan per konten bisa memenuhi 10 baris dalam sebulan. Putuskan apakah social media dicatat per konten atau per kalender konten | owner |
| 7 | Materi yang sudah terbit (Company Profile, Product Deck, website) belum punya persetujuan tertulis yang dapat ditunjukkan. Butir 4.15 mengusulkan peninjauan tanpa tanggal mundur; belum diputus siapa dan kapan peninjauan itu dilakukan | owner dan Samuel |
| 8 | Sintesis butir 13 menyebut "larangan positioning" produk tertentu (Arcfra). Daftar produk atau merek yang tidak boleh dipositioningkan tidak ditemukan di bahan yang dibaca, jadi Pemverifikasi klaim produk belum punya acuan itu | owner |
| 9 | Harga dan diskon di materi eksternal: SNX-ISMS-PRO-01 menyebut harga sebagai contoh RESTRICTED, dan SNX-COM-SOP-02 mengatur harga untuk customer tertentu. Belum diputus apakah materi umum boleh memuat harga, dan siapa memverifikasinya (butir 4.11, baris "klaim jenis lain") | owner dan Samuel |
| 10 | VP Commercial sebagai Pemilik informasi atas materi pemasaran (USULAN 6) belum tercatat. Pencarian "marketing", "company profile", "materi pemasaran", dan "Commercial" di notes/ISMS-REG-01.md dan specs/ISMS-REG-01.patch.json tidak menemukan aset materi pemasaran; isi xlsx live tidak dibaca (UNMEASURED). ISMS Coordinator juga belum ditetapkan (HR-ORG-01 K-13). Perlu keputusan siapa Pemilik informasi untuk materi pemasaran dan apakah aset itu masuk SNX-ISMS-REG-01 | Fani ; tetap terbuka; W9 memindahkan pencatatan penurunan klasifikasi ke SNX-ISMS-REG-01 (butir 4.5) |
| 11 | SNX-MKT-RPT-01 dan SNX-MKT-REG-02 disusun lane lain di wave yang sama. Spec MKT-REG-02 yang muncul sesudah register ini selesai juga mencatat materi, klaim, bukti pendukung, persetujuan, dan lokasi file final, dan memuat butir 4.15 yang menyamakan nama materi dan nomor versi dengan SNX-MKT-REG-01. Menurut keputusan cakupan orkestrator (open item 1), SNX-MKT-REG-02 seharusnya menjadi register pelaksanaan campaign dan aktivitas yang merujuk ke ID persetujuan di register ini; spec MKT-REG-02 perlu disesuaikan oleh lane-nya (saya tidak mengubah file itu). Putaran sweep menambah SNX-MKT-REG-03 (hasil lead dan serah terima ke Sales) di Ruang Lingkup dan Dokumen Terkait. Uraian isi RPT-01, REG-02, dan REG-03 di dokumen ini mengikuti batas cakupan dari orkestrator dan Description baris 56 dan 59; isi spec ketiganya tidak dibaca ulang, jadi keselarasan perlu dicek bila spec mereka berubah | owner ; ditutup W9: REG-02 diubah lewat A8 (kolom materi dan klaim dihapus, hanya ID Persetujuan Materi) |
| 12 | Rujukan butir ke dokumen lain (SNX-ISMS-PRO-01 butir 4.1 dan 4.2, SNX-OPS-SOP-05 butir 4.1) dicocokkan dengan spec di repo saat saya menulis. Spec lane lain masih Draft dan bisa berubah | owner |
| 13 | Klausul ISO belum dicocokkan dengan teks standar | owner, diteruskan ke konsultan |
| 14 | Tidak ada kalimat perintah kepada AI di bahan yang dibaca. Tidak ada open item dari sisi ini | - |

## 5. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya enam tanda; lima sudah diperbaiki, satu dibiarkan:
   - Istilah terdefinisi ditulis dengan dua huruf: "reviewer, approver" di Tujuan dan "Reviewer, Approver" di bagian lain. Diperbaiki: huruf kapital di semua tempat.
   - "di luar SINUX" dan "pihak luar" dipakai untuk hal yang sama. Diperbaiki: satu istilah, "pihak luar", dengan definisinya.
   - "Penetapan itu mengikuti SNX-ISMS-PRO-01" memberi dokumen kata kerja manusia. Diperbaiki: "diatur di".
   - "Ia menulis lokasi file final ... bukti persetujuan: USULAN" memakai kata ganti yang ambigu dan label yang tidak sesuai bentuk "(USULAN)". Diperbaiki: dipecah jadi dua kalimat, pelakunya Brand & Marketing, label "(USULAN)".
   - "siapa pun penyusunnya" mirip frasa meta proses penyusunan. Diperbaiki: "siapa pun yang menyusunnya".
   - Putaran perbaikan 1: kolom baru "Jenis Konten" memakai kata "konten" untuk hal yang di bagian lain disebut "materi". Diperbaiki: "konten" hanya dipakai sebagai nama kolom dan di definisi "Jenis konten" ("macam sebuah materi menurut daftar di bagian 2"). Kolom Klaim, Sumber atau Bukti Pendukung, Pemverifikasi, hasil, tanggal, dan bukti verifikasi semula hendak digabung di satu tabel tujuh kolom; dipecah menjadi Tabel 4 dan Tabel 5 agar header tidak terpotong. Kata "Bukti pendukung" diberi definisi yang mencakup "sumber" supaya satu istilah dipakai untuk nama kolom dan teks.
   - Dibiarkan: hampir tiap butir Cara Mengisi dibuka dengan "Brand & Marketing", dan banyak butir Ketentuan diakhiri "(USULAN)". Yang pertama mengikuti aturan satu pelaku per langkah (RUNBOOK 6a.1 dan 6a.2) dan satu peran memang menulis semua tabel. Yang kedua adalah label wajib karena tidak ada sumber tertulis untuk register baru ini.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa terhadap tabel Fakta kunci, Fakta penting lain, dan pemetaan peran:
   - Angka: tidak ada angka waktu, nilai, atau persen. Angka yang ada hanya nomor butir dan klausul, kode JA, jumlah "10 baris" (USULAN 1), "lima nilai" (USULAN 10), dan nomor versi awal 1 (butir 6.6). Angka dari bahan terkait (99.9%, 1 jam, 15 menit, 60%, 12 konten per bulan) tidak dibawa ke dokumen.
   - Nama: Zilly Dwinata, Laras Rasmawati, dan Samuel Kristanto Utomo hanya di blok approval (prompt dan defaults). Nol nama orang lain. Nama peran dari HR-ORG-01 dan Job Analysis; Legal & Compliance dipakai tanpa memilih antara JA-08 dan JA-09.
   - Tanggal: nol di dokumen. Tanggal di notes ini adalah modifiedTime berkas sumber.
   - Tanpa kutipan sumber tetapi ada di dokumen, semuanya berlabel USULAN atau tercatat di notes: pembagian cakupan dengan SNX-MKT-REG-02 dan kolom ID persetujuan (USULAN 2 dan 3), Pemverifikasi per jenis klaim dan penolakan klaim (USULAN 11 sampai 13); Tabel 4 dan Tabel 5 sendiri tidak berlabel karena bersandar pada judul baris 57 dan Description baris 58; lima nilai status (USULAN 10); status Ditarik (USULAN 9); butir 4.15 (USULAN 15); pengecualian lingkup (USULAN 16); lokasi Google Drive (USULAN 14, dasar PRO-01 butir 4.8); klausul ISO (USULAN 20).
   - Tidak berlabel di dokumen tetapi tafsir saya: definisi Customer yang disamakan dengan register Commercial (asumsi 10); Dokumen Terkait SNX-MKT-RPT-01 "Memuat rencana dan evaluasi kinerja marketing", diturunkan dari Description baris 56 tanpa membaca dokumennya (open item 11); frasa "pemilik register menurut blok Identity" mengikuti aturan process_owner di defaults.
   - Rujukan butir ke dokumen lain (SNX-ISMS-PRO-01 butir 4.1 dan 4.2; SNX-OPS-SOP-05 butir 4.1) dicocokkan dengan spec di repo saat saya menulis. Jabatan di Job Analysis dikutip dari teks live hari ini.

## Sweep

Putaran sweep atas instruksi orkestrator, dua butir. Butir lain di qa/MKT-REG-01.verify.json (status publikasi dan penolakan versi, pemilik bukti pendukung, lokasi folder, butir 6.25, istilah "ID Persetujuan Materi" di MKT-REG-02, label butir 4.10, "kanal kerja resmi") tidak diubah karena instruksi sweep membatasi perubahan pada butir 1 dan 2; temuan itu tetap berlaku sebagai catatan nonblocking.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Klasifikasi PUBLIC bertentangan dengan SNX-ISMS-PRO-01 butir 4.2 | Butir 4.5: "Materi berklasifikasi INTERNAL sampai Approver menetapkan PUBLIC saat menyetujui versinya." Peran Approver menetapkan klasifikasi PUBLIC; Acuan ISO 5.12 "sampai Approver menetapkan PUBLIC" | Butir 4.5: VP Commercial menjadi Pemilik informasi atas materi (USULAN); materi berklasifikasi INTERNAL sampai Pemilik informasi menurunkannya menjadi PUBLIC saat Approver menyetujui versinya, dan penurunan tercatat di bukti persetujuan yang sama (USULAN); penetapan dan penurunan diatur di SNX-ISMS-PRO-01 butir 4.1 dan 4.2. Definisi menambah "Pemilik informasi"; tabel Peran: baris baru Pemilik informasi, baris Approver tidak lagi menetapkan klasifikasi, baris VP Commercial memegang tiga peran, kalimat pengantar menyebut Pemilik informasi sebagai peran menurut PRO-01; Acuan ISO 5.12 "sampai Pemilik informasi menurunkannya menjadi PUBLIC"; baris Dokumen Terkait SNX-ISMS-PRO-01 menyebut peran Pemilik informasi dan penurunan klasifikasi. USULAN 6 dan open item 10 ditulis ulang |
| 2 | Batas cakupan dokumen Marketing | Pengecualian: "Rencana dan evaluasi kinerja marketing" (RPT-01) dan "Pelaksanaan campaign dan aktivitas marketing" (REG-02: "merujuk tiap materi"); tanpa REG-03; Ruang Lingkup tidak menyebut verifikasi klaim; Dokumen Terkait RPT-01 "Memuat rencana dan evaluasi kinerja marketing" tanpa label, tanpa baris REG-03 | Ruang Lingkup menambah kalimat "Register ini juga mencakup verifikasi klaim di dalam materi." Pengecualian: RPT-01 = rencana pemasaran dan tinjauan kinerja (sasaran, audiens, positioning, channel, rencana aktivitas, KPI, realisasi, evaluasi, tindakan korektif); REG-02 menautkan tiap materi ke ID persetujuan di register ini; baris baru REG-03 = hasil lead dan serah terima lead kepada Sales; semua berlabel (USULAN). Dokumen Terkait: RPT-01 "rencana pemasaran dan tinjauan kinerja (USULAN)", REG-02 tetap, baris baru REG-03 (merujuk nama campaign di REG-02, USULAN). USULAN 16 dan open item 11 ditulis ulang. Pemutus: owner |

Uji sweep (semua dari /home/claude/iso-run): render tanpa galat; `python3 -I tools/lint_doc.py ... generic` pass, fails kosong, warn "31 butir (USULAN)"; `python3 /mnt/skills/public/docx/scripts/office/validate.py` "All validations PASSED!"; `python3 -I reports/orch/blankscan.py` `ok 15 []`. Kode SNX di badan dan Dokumen Terkait cocok (9 kode).

## ISO-W9

Putaran ISO-W9 (LEAD G-3 A8, B2; owner GO). Batas tulis: specs/MKT-REG-01.json dan notes/MKT-REG-01.md. Meta dan blok approval tidak berubah (sama dengan defaults v22 MKT). Rujukan silang baru: SNX-ISMS-REG-01 (Information Asset Register) ada di repo dan PRO-01 langkah "Catat penurunan klasifikasi di SNX-ISMS-REG-01" dilakukan Pemilik informasi; SNX-ISMS-REG-01 ditambah ke Dokumen Terkait.

| Butir | Sebelum | Sesudah |
|---|---|---|
| Ruang Lingkup paragraf 1 | mencakup verifikasi klaim | tambah: register ini satu-satunya register materi, konten, dan persetujuan klaim SINUX |
| Pengecualian baris RPT-01, REG-03 | "(USULAN)" | label dihapus (batas diputus) |
| Pengecualian baris REG-02 | "Pelaksanaan campaign dan aktivitas marketing ... menautkan tiap materi ... (USULAN)" | "Pelaksanaan Aktivitas pemasaran ... hanya memuat ID persetujuan dari register ini untuk materi yang dipakai" |
| 4.5 | penurunan itu tercatat di bukti persetujuan yang sama (USULAN) | Pemilik informasi mencatat penurunan itu di SNX-ISMS-REG-01 mengikuti SNX-ISMS-PRO-01; register ini hanya merujuk |
| Peran Pemilik informasi | mencatat penurunan di bukti persetujuan | mencatat penurunan di SNX-ISMS-REG-01 |
| Dokumen Terkait REG-02, REG-03, RPT-01 | tautan materi; label USULAN | pelaksanaan Aktivitas pemasaran dengan ID persetujuan; nama Aktivitas; label dihapus |
| Dokumen Terkait baru | tidak ada | SNX-ISMS-REG-01 |

Open item yang ditutup atau diubah W9: lihat kolom Pemutus pada tabel Open items. Open item baru:

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 15 | Description checklist baris 58 berisi pengendalian materi baris 57 yang diperluas dengan validasi klaim, bukan pelaksanaan campaign sesuai judulnya (Marketing Campaign & Activity Register); perlu dibetulkan Brand & Marketing. Pengukuran: teks baris 58 tidak identik dengan baris 57. | Brand & Marketing |
| 16 | A3: dokumen ini menyebut JA-04 hanya sebagai dasar Pemverifikasi klaim kinerja layanan (VP Tech Operation and Services), tanpa atasan atau garis lapor; tidak ada yang diselaraskan | - |

Uji (spec W9): render, `lint_doc.py ... generic`: pass true, fails kosong, 25 butir USULAN; `validate.py`: All validations PASSED; `blankscan.py`: ok 15 halaman []; `w9diff.py MKT-REG-01`: diff hanya baris di tabel di atas.

Perbaikan putaran 1 ISO-W9 (pemeriksa buta, pemblokir rujukan butir):

| Butir | Sebelum | Sesudah |
|---|---|---|
| Dokumen Terkait baris SNX-ISMS-REG-01 | "menurut SNX-ISMS-PRO-01 (butir 4.5)" terbaca sebagai PRO-01 butir 4.5 (Pelabelan) | "menurut SNX-ISMS-PRO-01 (butir 4.5 register ini)", merujuk butir 4.5 dokumen ini |

Open item: tidak ada yang ditutup atau diubah pada putaran ini.

### ISO-W9 R2

R2 tidak mengubah spec MKT-REG-01 (butir R2 1 sampai 3 tidak menyentuh dokumen ini). Perubahan hanya pada notes: baris USULAN dan Open items yang ditutup atau diubah W9 kini memuat "ditutup W9" atau "diubah W9" di barisnya sendiri (USULAN 2, 6, 16; open item 1, 10, 11 sudah).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Butir 4.5 asli: "4.5 VP Commercial menjadi Pemilik informasi atas materi (USULAN). Materi berklasifikasi INTERNAL sampai Pemilik informasi menurunkannya menjadi PUBLIC saat Approver menyetujui versinya (USULAN). ..." Dua label digabung jadi satu label di akhir butir (STYLE §3.5); kalimat dirangkai sehingga label tetap meliputi kedua ketentuan. Butir 4.5 tetap berstatus USULAN.
### W10 kalimat dihapus atau dipindah
- Definisi Materi: "Jenis yang tercakup ada di bagian 2." dihapus (kalimat penunjuk; daftar jenis tetap di Ruang Lingkup).
- Definisi Jenis konten: "menurut daftar di bagian 2" diganti contoh jenisnya (company profile, product brochure, presentation deck, campaign material, event collateral).
- Tabel butir 4.11, baris Kinerja layanan: "Target availability standar ada di SNX-OPS-SOP-05 butir 4.1." dihapus (fakta yang sama tetap di butir 4.12; satu rujukan per sel).
- Butir 4.12: "sebab menurut SNX-OPS-SOP-05 butir 4.1 bahasa itu hanya ada di dokumen kontraktual" ditulis "karena SNX-OPS-SOP-05 membatasi bahasa itu pada dokumen kontraktual" (rujukan butir 4.1 sudah ada di kalimat sebelumnya).
- Butir 4.14: "(bagian 8)" setelah "tabel Record" dihapus. Butir 4.16: "di bagian 3" dihapus.
- Tabel Peran: rujukan "(butir 4.2 dan 4.3)", "(butir 4.7, 4.9, 4.10, 4.14, dan 4.15)", "(butir 4.4 dan 4.5)", "(butir 4.3)", "(butir 4.11)", "(butir 4.4)", "(butir 4.6, 4.9, 4.13, dan 4.15)", "(butir 4.5)", "(butir 4.11 sampai 4.13)", "(butir 4.11 dan 4.13)" dihapus.
- Cara Mengisi: rujukan "(butir 4.1)" di 6.1, "(butir 4.14)" di 6.7, "(butir 4.4)" di 6.10, "(butir 4.6)" di 6.11, "(butir 4.10)" di 6.18 dan 6.20, "(butir 4.10 dan 4.14)" di 6.24 dihapus; 6.3 "sesuai daftar di bagian 2" ditulis "sesuai daftar di bagian Ruang Lingkup".
- Acuan ISO 7.5.3: "Pemilik register ada di tabel Record, dan klasifikasi materi di butir 4.5." ditulis "beserta pemilik register dan klasifikasi materi (butir 4.5)".
- Peran, paragraf pembuka: "Pembagian tugas berikut berstatus (USULAN)." dipindah ke akhir paragraf: "Pembagian tugas di tabel berikut belum diputuskan (USULAN)."
### W10 selisih angka
nihil (subst_diff kosong).
### W10 catatan
- Pihak luar: "customer" (satu-satunya sebutan di dokumen ini).
- Istilah Marketing English: claim (jembatan "claim (klaim)" di Tujuan; heading dan kolom "Klaim yang Perlu Diverifikasi" serta "Verifikasi Klaim" beku), content (header kolom "Jenis Konten" dirapikan menjadi "Jenis Content"), review (jembatan "review (peninjauan)" untuk h2 Tabel 2), record (jembatan "Record (rekaman)" di Definisi).
- Cara Mengisi jadi kalimat perintah untuk Brand & Marketing (pencatat register di tabel Peran); 0 dari 25 diawali peran.
- Tabel isian diberi min_row_cm 0.8 (1.0 dan 0.9 menaikkan halaman jadi 16).
- Ruang Lingkup: "rencana aktivitas" ditulis "rencana Aktivitas" agar "Aktivitas" satu arti dengan SNX-MKT-REG-02 dan SNX-MKT-RPT-01.

### W10 rujukan USULAN dicek (adjudikasi worker, gerbang rujukan USULAN)
- .sections[4].blocks[1].table.rows[0][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[4].blocks[1].table.rows[1][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[4].blocks[1].table.rows[6][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[4].blocks[1].table.rows[7][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[4].blocks[1].table.rows[8][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[4].blocks[1].table.rows[9][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[5].blocks[0].p (butir 6.1): label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[5].blocks[6].p (butir 6.7): label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[5].blocks[9].p (butir 6.10): tanpa label; instruksi mekanis pengisian kolom; penetapan Approver (USULAN) tidak dinyatakan ulang.
- .sections[5].blocks[10].p (butir 6.11): label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.

### W10 audit pointer
- .sections[2].blocks[0].table.rows[11][1]: lengkap (definisi; contoh jenis content dari Ruang Lingkup, dan butir 6.3 tetap menunjuk daftar di bagian Ruang Lingkup)
- .sections[2].blocks[0].table.rows[14][1]: lengkap (kalimat penunjuk lokasi "Jenis yang tercakup ada di bagian 2" dibuang sesuai STYLE §3.2; daftar tetap ada di Ruang Lingkup)
- .sections[3].blocks[11].table.rows[1][2]: lengkap (kolom dasar penunjukan; target availability SNX-OPS-SOP-05 butir 4.1 tetap dirujuk di butir 4.12 yang memuat aturan tolak)
- .sections[3].blocks[14].p: lengkap (pelaku Brand & Marketing, benda yang disimpan, lokasi pada tabel Record (heading Rekaman, jembatan Record (rekaman) di Definisi), lokasi file final di Tabel 1, label USULAN)
- .sections[3].blocks[16].p: lengkap (lima nilai, nama tabel Status Publikasi tetap disebut, label USULAN)
- .sections[4].blocks[1].table.rows[0][1]: lengkap (rujukan beruntun dibuang; tugas tertulis di sel, batas tanggal publikasi tetap dirujuk butir 6.16 (butir 4.7), urutan catat sebelum Reviewer tercermin di 6.13 dan 6.14, label USULAN)
- .sections[4].blocks[1].table.rows[1][1]: dilengkapi (pihak alternatif Reviewer: "dan Reviewer selain dirinya untuk materi tertentu", disalin dari butir 4.4)
- .sections[4].blocks[1].table.rows[2][1]: lengkap (PIC bertanggung jawab atas satu materi; penetapan PIC ada di butir 4.3 dan sel VP Commercial)
- .sections[4].blocks[1].table.rows[3][1]: lengkap (Reviewer meninjau sebelum Approver memutuskan; penetapan Reviewer di butir 4.4 dan butir 6.9)
- .sections[4].blocks[1].table.rows[4][1]: rujukan dikembalikan (kriteria tidak menyetujui versi dengan claim tanpa bukti, tanpa hasil verifikasi, atau ditolak: "sesuai butir 4.13")
- .sections[4].blocks[1].table.rows[5][1]: lengkap (pelaku, saat penurunan ke PUBLIC, pencatatan di SNX-ISMS-REG-01, pemegang VP Commercial, label USULAN)
- .sections[4].blocks[1].table.rows[6][1]: rujukan dikembalikan (kriteria tolak claim availability atau SLA dan bahasa kompensasi: "sesuai butir 4.12")
- .sections[4].blocks[1].table.rows[7][1]: lengkap (jenis claim sesuai tabel butir 4.11, label USULAN; aturan pemeriksaan di sel Pemverifikasi yang merujuk butir 4.12)
- .sections[4].blocks[1].table.rows[8][1]: lengkap (jenis claim kinerja layanan sesuai tabel butir 4.11, label USULAN; aturan tolak di sel Pemverifikasi yang merujuk butir 4.12)
- .sections[4].blocks[1].table.rows[9][1]: lengkap (jenis claim sesuai tabel butir 4.11, label USULAN)
- .sections[5].blocks[0].p: lengkap (satu baris per versi per channel, ID persetujuan, ID yang sama di Tabel 1 sampai 3 melalui definisi ID persetujuan, nomor claim yang sama di butir 6.21, label USULAN)
- .sections[5].blocks[2].p: lengkap (rujukan tetap ada sebagai "bagian Ruang Lingkup")
- .sections[5].blocks[6].p: lengkap (jalur folder dan nama file final di kolom Lokasi File Final, label USULAN)
- .sections[5].blocks[9].p: lengkap (jabatan Approver; penetapan Approver dirujuk butir 6.9 (butir 4.4) di paragraf sebelumnya)
- .sections[5].blocks[10].p: lengkap (urutan setelah persetujuan, tanggal lengkap, label USULAN)
- .sections[5].blocks[17].p: lengkap (satu baris per claim, ID persetujuan di kolom ID Materi)
- .sections[5].blocks[19].p: lengkap (nama dan lokasi, tanpa isi)
- .sections[5].blocks[23].p: dilengkapi (", tanpa isinya", disalin dari butir 4.10)

### W10 audit cakupan label
- .sections[3].blocks[3].p: diperbaiki (tambah label pada kalimat Approver; di bed1bb6 seluruh butir 4.4 satu kalimat berlabel)
- .sections[3].blocks[4].p: OK (label tetap mencakup Pemilik informasi dan klasifikasi INTERNAL; rujukan SNX-ISMS-PRO-01 tetap tanpa label)
- .sections[4].blocks[0].p: OK (label tetap pada pembagian tugas)
- .sections[4].blocks[1].table.rows[0][1]: OK (pembagian tugas tabel berlabel di bed1bb6; label baru menggantikan rujukan butir)
- .sections[4].blocks[1].table.rows[1][1]: OK (rujukan butir 4.3, 4.4, 4.5, 4.11 yang berlabel diganti fakta)
- .sections[4].blocks[1].table.rows[6][1]: OK (rujukan butir 4.11 sampai 4.13 yang berlabel diganti)
- .sections[4].blocks[1].table.rows[7][1]: OK (rujukan butir 4.11 dan 4.13 yang berlabel diganti)
- .sections[4].blocks[1].table.rows[8][1]: OK (rujukan butir 4.11 sampai 4.13 yang berlabel diganti)
- .sections[4].blocks[1].table.rows[9][1]: OK (rujukan butir 4.11 dan 4.13 yang berlabel diganti)
- .sections[5].blocks[0].p: OK (rujukan butir 4.1 yang berlabel diganti)
- .sections[5].blocks[6].p: OK (rujukan butir 4.14 yang berlabel diganti)
- .sections[5].blocks[10].p: OK (rujukan butir 4.6 yang berlabel diganti)
- .sections[6].blocks[0].p: OK (label tetap pada 10 baris dan pembagian kolom)
