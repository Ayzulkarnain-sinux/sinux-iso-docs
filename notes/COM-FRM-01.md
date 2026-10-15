# Catatan penyusun COM-FRM-01: Customer Requirement & Order Review Record

Status: DRAFTED (spec + notes ada). Spec: specs/COM-FRM-01.json. Mode generic (doc_type_cover "FORM", doc_type_label "Form"), aksi T2, wave W7, nomor SNX-COM-FRM-01 (nomor SNX lama dipertahankan), department Commercial, classification INTERNAL (worklist), audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Laras Rasmawati / VP Commercial", reviewed "Amirull Yusuf Zulkarnain / Direktur", approved "Samuel Kristanto Utomo / President Director". process_owner "Direktur": aturan defaults untuk dokumen tanpa sumber = jabatan pada kolom reviewed departemen, tanpa nama (lihat open item 1). Catatan worklist: kosong.

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-FRM-01.json /tmp/pen-COM-FRM-01/COM-FRM-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-COM-FRM-01/COM-FRM-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "19 butir (USULAN) menunggu ACC".
- Tata letak: docx dikonversi ke PDF dengan soffice (17 halaman). Render pertama dilihat seluruhnya pada 50 dpi; sesudah perbaikan judul dan lebar kolom, halaman 10, 11, 12, dan 14 dilihat lagi pada 70 dpi. Tabel isian terbaca dan kolom No. serta Rujukan tidak terpotong. Halaman lain tidak dilihat ulang sesudah perbaikan (UNMEASURED). Validator OOXML skill docx tidak dijalankan (UNMEASURED); lint menguji id bookmark ganda.
- Kecocokan kode SNX di badan dengan tabel Dokumen Terkait diperiksa dengan skrip kecil: 12 kode di badan, nol kode kurang, nol kode berlebih.
- Lint dan skrip hanya membuktikan format dan larangan pola. Kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.
- Diagram: tidak ada. Formulir isian tidak memerlukan diagram, dan kriteria baris 52 tidak memintanya.

## 1. Sumber

Prompt menyatakan sumber: tidak ada (T2 tanpa sumber). Tidak ada fileId yang ditugaskan. Alat Drive dimuat dan dipakai hanya untuk baca (get_file_metadata, read_file_content); nol tulis ke Drive. Dua berkas Drive dibaca sebagai sumber terkait karena SNX-COM-SOP-01 dan SNX-COM-SOP-02 bersandar pada keduanya.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist ISO SINUX - 2026, baris 52 (kriteria penerimaan) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (dari config/checklist.json, tidak diukur ulang di Drive) | config/checklist.json baris 52: `checked: false`, `fileId: null`, `link_url: null`. Tidak ada berkas yang tertaut ke baris ini |
| SALES STANDARD OPERATING PROCEDURE.pdf | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (get_file_metadata hari ini) | read_file_content, teks utuh dibaca. Lapisan teks PDF bercampur antar kartu, jadi kutipan di bawah ditulis sebagai potongan terpisah. Halaman tidak dirender sebagai gambar (UNMEASURED) |
| SINUX_Job_Analysis_2026.docx (JA-05 Manager of Product Tech) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini) | Kutipan JA-05 diambil dari salinan context/audit (retrieved 2026-10-13); isi live tidak dibaca ulang (UNMEASURED) |
| POL-OPS-001 (Kebijakan Divisi Operation), checklist gate G1 | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | tidak diukur | Hanya salinan context/audit/iso-sinux-supdocs-ops-2026-10-14.md (retrieved 2026-10-13); tidak dibaca di Drive (UNMEASURED) |
| Pendukung repo (bukan Drive) | - | - | config/defaults.json v21; specs/HR-ORG-01.json (nama peran, K-10, K-13); specs/COM-SOP-01.json dan specs/COM-SOP-02.json (butir yang dirujuk, dan penyebutan SNX-COM-FRM-01); specs/LEG-SOP-02.json, specs/LEG-FRM-01.json, specs/FAT-SOP-01.json, specs/OPS-SOP-01.json, specs/OPS-SOP-05.json, specs/ISMS-PRO-01.json. Dibaca sebagai DATA. Spec lane lain masih Draft; kutipan darinya bisa basi |

Kalimat perintah kepada AI di semua sumber: nihil. Kalimat kewajiban untuk karyawan ("Sales wajib ...") adalah isi SOP, bukan instruksi untuk saya.

Pemetaan kriteria baris 52 ke dokumen:

| Unsur Description | Di dokumen |
|---|---|
| Mencatat kebutuhan customer | Tabel Kebutuhan Customer (B1 sampai B10, delapan topik discovery meeting dan dua baris kebutuhan lain); tabel Informasi Order |
| kesesuaian scope | Kelompok C1 (C1.1 sampai C1.4) |
| kelayakan teknis | Kelompok C2 (C2.1 sampai C2.3) |
| persyaratan kontraktual | Kelompok C3 (C3.1 sampai C3.7) |
| delivery commitment | Kelompok C4 (C4.1 sampai C4.6) |
| hasil review sebelum order diterima | Tabel Temuan dan Tindak Lanjut, Hasil Review, Dasar Hasil Review, Catatan Review dan Persetujuan; Ketentuan butir 7 dan 8 |

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Enam unsur yang wajib dicatat formulir ini, dan titik waktunya (sebelum order diterima). Dasar seluruh struktur Isi Formulir | "Mencatat kebutuhan customer, kesesuaian scope, kelayakan teknis, persyaratan kontraktual, delivery commitment, dan hasil review sebelum order diterima." (checklist baris 52, kolom Description) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist; baris 52 sendiri `fileId: null`) |
| Discovery meeting menghasilkan Business Requirement dan membahas delapan topik minimum. Dasar tabel Kebutuhan Customer B1 sampai B8 dan Ketentuan butir 1 | "Menggali kebutuhan bisnis customer secara menyeluruh." lalu "Minimum Discussion" "Business Challenges" "Existing System" "Current Process" "Pain Points" "Desired Outcome" "Project Timeline" "Budget Expectation" "Decision Process"; "Output" "Discovery Notes" "Business Requirement" "Opportunity Assessment" (Stage 3 Discovery Meeting, urutan dari transkripsi context/audit; lapisan teks PDF bercampur) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Timeline tidak dijanjikan tanpa konfirmasi Delivery, dan closing baru sah bila persetujuan internal selesai. Dasar aspek C4.1 dan Ketentuan butir 8 | "Sales tidak diperbolehkan:" "Mengubah pricing sendiri." "Memberikan diskon tanpa persetujuan." "Menawarkan fitur yang belum tersedia." "Menjanjikan timeline tanpa konfirmasi Delivery." dan "Closing dinyatakan berhasil apabila:" "Purchase Order diterima." "Kontrak ditandatangani." "Internal approval selesai." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

Fakta penting lain:

| # | Fakta di dokumen | Kutipan verbatim | Posisi |
|---|---|---|---|
| 1 | Manager of Product Tech menilai kelayakan solusi dan menyusun desain, BOM/BOQ, sizing, dan asumsi teknis; mengeskalasi proposal yang tidak feasible (kelompok C2, tabel Peran) | "Mengumpulkan kebutuhan teknis dan menilai kelayakan solusi bersama Commercial." "Menyusun desain tingkat tinggi, BOM/BOQ, sizing dan asumsi teknis proposal." "Melakukan peninjauan risiko implementasi, lisensi, kompatibilitas dan dependensi vendor." "Mengeskalasi proposal yang tidak feasible" | Job Analysis JA-05 uraian 2, 3, 4 dan wewenang 3 (salinan context/audit), fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Service Delivery Manager dan Delivery mengonfirmasi timeline dan scope (kelompok C4) | "Delivery" "Project handover" "Timeline confirmation" "Scope clarification" | Sales SOP 09 Internal Collaboration, fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| 3 | Legal terlibat pada review kontrak dan syarat dan ketentuan komersial (kelompok C3, Ketentuan butir 5) | "Legal" "NDA preparation/review" "Contract review" "Commercial terms & conditions" "Contract negotiation support" "Legal compliance" | Sales SOP 09 Internal Collaboration, fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| 4 | Item gate G1 yang menyangkut janji kepada customer (aspek C4.3, C4.4, C4.5) | "SLA dan target layanan yang dijanjikan ke pelanggan, tertulis." "Jadwal target live dan batasan pelanggan (window maintenance, blackout)." "Janji lisan ke pelanggan yang belum ada di kontrak, dicatat terbuka." | POL-OPS-001 bagian 8.2, checklist G1 (salinan context/audit), fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |
| 5 | SNX-COM-FRM-01 sudah dirujuk dua dokumen Commercial sebagai calon rekaman (dokumen ini memadukan keduanya, USULAN 2) | COM-SOP-01 dokumen terkait: "Calon rekaman Business Requirement di butir 6.3 (USULAN)." COM-SOP-02 dokumen terkait: "Calon bentuk Catatan review scope (USULAN)." | specs/COM-SOP-01.json, specs/COM-SOP-02.json (repo, Draft) |
| 6 | Legal dilibatkan sebelum ada komitmen tertulis kepada pihak luar | "Pemohon melibatkan Legal sejak negosiasi komersial, sebelum ada komitmen tertulis kepada pihak luar." | specs/LEG-SOP-02.json butir 4.3 (repo, Draft) |
| 7 | TOP di atas standar disetujui Direktur Utama secara tertulis (aspek C3.3) | "Direktur Utama menyetujui TOP di atas 14 hari secara tertulis sebelum PKS atau PO disepakati." | specs/FAT-SOP-01.json butir 4.8 (repo, Draft). Angka 14 hari tidak dibawa ke formulir |
| 8 | Target standar SLA dan larangan bahasa kompensasi di proposal (aspek C4.3) | "Bahasa kompensasi atau service credit hanya ada di dokumen kontraktual, tidak di materi pemasaran atau proposal." | specs/OPS-SOP-05.json butir 4.1 (repo, Draft). Angka availability di butir itu tidak dibawa |
| 9 | Informasi customer minimal RESTRICTED (Ketentuan butir 10, Rekaman) | "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan tingkat yang lebih tinggi." | specs/ISMS-PRO-01.json butir 4.3 (repo, Draft) |
| 10 | Pembaruan CRM dan pencatatan aktivitas penjualan di CRM (Ketentuan butir 10, Rekaman) | "Seluruh aktivitas penjualan wajib dicatat di CRM." | Sales SOP 06 CRM Policy, fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

## 2. Keputusan data dan pemetaan peran

- Sebutan: "Direktur (COO)" pada sebutan pertama di badan dokumen, yaitu baris Istilah; sesudahnya "COO". Bagian Tujuan dan Lingkup tidak menyebut COO. Samuel di badan = "Direktur Utama"; namanya dan "President Director" hanya di blok approval. Nama Laras dan Amirull hanya di blok approval. Nol nama orang lain di dokumen.
- Process Owner di blok Identity = "Direktur" (jabatan kolom reviewed, tanpa nama). Di badan, jabatan itu ditulis "COO" (tabel Peran memberi label "Pemilik dokumen ini menurut blok Identity (USULAN)").
- Tiket: Zammad untuk Ops, GLPI untuk generalist. Dokumen tidak menyebut tiket. Satu-satunya kanal yang punya rujukan, permintaan review kontrak ke Legal & Compliance, memakai SNX-LEG-SOP-02 butir 6.1 (di sana berstatus USULAN, GLPI). Kanal permintaan ke Manager of Product Tech dan Service Delivery Manager belum diputus: open item 5.
- Vault: tidak relevan, tidak disebut.
- PPN: satu rumusan hanya di SNX-FAT-SOP-01 butir 4.5; aspek C3.2 merujuk butir itu tanpa tarif. Keputusan FAT atas tarif tetap open (open item 10).
- Klasifikasi blok Identity: INTERNAL (worklist). Formulir terisi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 butir 4.3 (Ketentuan butir 10). Footer renderer tidak menampilkan label karena INTERNAL.
- Istilah: "customer" (bukan pelanggan atau klien, kecuali judul klausul ISO), "review" untuk semua pemeriksaan, "penawaran" = proposal dan quotation, "timeline" (bukan jadwal), "dependensi" (bukan dependency), "persyaratan kontraktual" untuk syarat dalam PO atau kontrak, "kebutuhan" untuk yang customer minta.

Pemetaan peran sumber ke nama peran di tabel Peran (basis specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Sales, Sales Executive | Business Development | JA-07; sama dengan COM-SOP-01 dan COM-SOP-02 |
| VP of Commercial | VP Commercial | JA-03 |
| Presales | Manager of Product Tech | JA-05; HR-ORG-01 tidak punya jabatan Presales; sama dengan COM-SOP-02 |
| Delivery | Service Delivery Manager | OPS-SOP-01 dan HR-ORG-01 K-10: jabatan usulan tanpa pemegang |
| Legal | Legal & Compliance | JA-08 dan JA-09 memakai nama jabatan yang sama; Line Manager Legal dan Staff Legal belum dipetakan (K-13), jadi tidak dipakai |
| Pihak yang menyetujui harga dan diskon (tidak disebut sumber) | COO | COM-SOP-02 butir 4.7 (USULAN di sana) |
| Pihak yang memutuskan TOP di atas standar | Direktur Utama | FAT-SOP-01 butir 4.8 |
| Finance, Accounting & Tax | tidak dipakai | Tidak punya tugas pada formulir ini; verifikasi harga dan PPN ada di COM-SOP-02 butir 6.3 |
| Head of Operation, NOC, SOC | tidak dipakai | Kelayakan operasi tidak masuk formulir: open item 7 |

## 3. Penanganan cacat context/audit

Perintah: `grep -n "Customer Requirement & Order R" context/audit/*.md` memberi nol baris. Judul dokumen ini tidak punya bagian di context/audit, jadi tidak ada bagian 5 Catatan kualitas dan celah untuk dokumen ini sendiri. Dua grep pendukung: `grep -n "COM-FRM-01" context/audit/*.md` nol baris; `grep -n -i "Customer Requirement" context/audit/*.md` hanya menemukan daftar dokumen di sintesis (SOP Customer Requirement Identification & Review, Customer Requirement Review Records, tanpa isi). Karena formulir ini bersandar pada Sales SOP, saya membaca bagian 5 Sales SOP (fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0) dan menangani tiap cacat yang menyentuh formulir ini.

| # | Cacat tercatat (Sales SOP, bagian 5) | Penanganan |
|---|---|---|
| 1 | Pricing dan diskon tanpa tingkat kewenangan, ambang, SLA approval, atau form | Formulir tidak memutuskan harga. Aspek C3.2 merujuk Catatan persetujuan penawaran milik SNX-COM-SOP-02. Ambang dan tenggat tidak dikarang: open item 3 dan 4 |
| 2 | Tidak ada tenggat untuk approval internal | Formulir tidak memuat angka waktu. Target selesai tiap temuan ditulis pengisi di tabel Temuan dan Tindak Lanjut. Tenggat review: open item 4 |
| 3 | Delivery sebagai penerima tanpa individu atau form terdefinisi | Peran Service Delivery Manager (jabatan usulan tanpa pemegang, K-10); open item 8 |
| 4 | "Menjanjikan timeline tanpa konfirmasi Delivery" tanpa mekanisme verifikasi atau rekaman | Diperbaiki: aspek C4.1 dan baris Delivery commitment di Catatan Review dan Persetujuan menjadi rekamannya |
| 5 | "Approval harga" dan "Approval diskon" tanpa pelaku | Pelaku tidak dikarang di formulir ini. Aspek C3.2 menyebut COO menurut SNX-COM-SOP-02 butir 4.7, yang berstatus USULAN di dokumen itu: open item 3 |
| 6 | Scope SOP menyebut Business Development, isi menyebut Sales Executive, Presales, VP Commercial | Nama peran memakai HR-ORG-01 (Business Development, Manager of Product Tech, VP Commercial); pemetaan di bagian 2 |
| 7 | Tidak ada nomor, penyetuju, riwayat revisi, klasifikasi | Teratasi oleh template dan defaults. "Version 1.0" dan "Effective Date 28th of July, 2026" tidak dibawa |
| 8 | Alat hanya "CRM" tanpa nama produk | Ditulis CRM tanpa nama produk: open item 9 |
| 9 | Closing mensyaratkan "Internal approval selesai" tanpa pelaku dan rekaman | Formulir ini menyediakan rekaman dan pelaku (VP Commercial menetapkan Hasil Review). Penempatan di Closing SNX-COM-SOP-01 butir 6.7 belum ada: open item 2 |
| 10 | KPI tidak identik, kriteria qualification berbeda dengan deck, cacat tata letak halaman 3, tidak ada tenggat follow-up lead | Tidak menyentuh formulir ini |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | SNX-COM-SOP-01 menyebut SNX-COM-FRM-01 calon rekaman Business Requirement, SNX-COM-SOP-02 menyebutnya calon Catatan review scope. Dua peran berbeda untuk satu dokumen | Formulir memadukan keduanya: tabel Kebutuhan Customer = rekaman Business Requirement, kelompok C1, C2, dan C4 tahap pertama = Catatan review scope. USULAN 2, open item 2 |
| B | SNX-COM-SOP-01 butir 4.15 memakai "PO diterima" (diterima = sampai ke SINUX), formulir memakai "order diterima" (pernyataan SINUX menerima) | Dibedakan di Istilah ("Order diterima", USULAN 3). Review jatuh di antara PO sampai dan pernyataan menerima. Open item 2 |

## 4. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Formulir diisi dua tahap: sebelum penawaran masuk review internal (kelompok C1, C2, C4, selaras SNX-COM-SOP-02 butir 6.2), dan saat PO atau draf kontrak datang (kelompok C3 dan perbandingan dengan penawaran). Pembagian ini mengikuti dua dokumen yang menyebut formulir ini sebagai calon rekaman; tidak ada sumber yang menetapkannya.
2. "Dokumen order" didefinisikan sebagai penawaran ditambah PO atau draf kontrak supaya satu daftar periksa berlaku di kedua tahap.
3. Delapan topik di tabel Kebutuhan Customer dipakai utuh dari "Minimum Discussion" Sales SOP. Dua baris kebutuhan lain (B9, B10) adalah ruang untuk kebutuhan yang muncul di PO atau RFP tetapi tidak ada di discovery meeting.
4. Kode dan isi aspek C1.1 sampai C4.6 adalah susunan penyusun, diturunkan dari: peran dan wewenang di Job Analysis (C2), SNX-COM-SOP-02 butir 6.2 (C1, C2, C4.1), butir 4.9 sampai 4.11 (C3.4), item gate G1 di POL-OPS-001 (C4.3 sampai C4.5), dan butir di FAT, OPS, LEG, ISMS yang dirujuk. Seluruh susunan berstatus USULAN (Isi Formulir, kalimat pembuka). C3.6 dan C4.6 diberi label sendiri karena tidak punya dasar kutipan.
5. Pembagian pengisi kelompok C3: Business Development mengisi C3.1 sampai C3.3 (perbandingan PO dengan penawaran dan TOP), Legal & Compliance mengisi C3.4 sampai C3.7. Tafsir saya dari pembagian tugas di SNX-COM-SOP-02 dan SNX-LEG-SOP-02.
6. Hasil Review tiga nilai (Diterima, Diterima dengan Syarat, Belum Dapat Diterima) dan tiga nilai Status mengikuti pola formulir Legal (SNX-LEG-FRM-01: Sesuai, Perlu Tindak Lanjut, Tidak Berlaku). Nama nilai adalah usulan, bukan kutipan.
7. VP Commercial sebagai penetap Hasil Review dan pemilik formulir terisi mengikuti pola SNX-COM-SOP-02 butir 4.15 (VP Commercial menyimpan Catatan persetujuan penawaran). Tidak ada sumber yang menyebut siapa menetapkan penerimaan order.
8. Klausul ISO di Acuan ISO berasal dari pengetahuan standar saya, tidak dicocokkan dengan teks standar (UNMEASURED), semuanya di bawah satu label "(USULAN, perlu konfirmasi konsultan)". Klausul 9001 8.2.1 sampai 8.2.4 dan 7.5.3 selaras dengan COM-SOP-02 dan LEG-SOP-02. 27001: 4.2, Annex A 5.31, 5.12. Annex A 5.14 (transfer informasi) tidak dimasukkan karena formulir tidak mengirim informasi ke luar.
9. Retensi semua rekaman "Belum ditetapkan"; lokasi berkas tidak ditetapkan kecuali CRM (satu-satunya tempat catatan di Sales SOP).
10. Nol angka waktu atau nilai di formulir: tidak ada tenggat, ambang, persen, atau jumlah hari. Angka 14 hari TOP dan angka availability di dokumen FAT dan OPS sengaja tidak disalin.
11. Tidak ada tanggal dan tidak ada nomor izin, harga, atau nilai kontrak di dokumen. Sel isian faktual (nama customer, PIC, nomor PO, tanggal, nilai) kosong dan tanpa baris contoh.

## USULAN

Spec memuat 19 kemunculan persis "(USULAN)" (satu di antaranya baris definisi label itu sendiri), dua label "(USULAN, ...)" pada tabel Peran, dan satu label "(USULAN, perlu konfirmasi konsultan)" pada klausul ISO. Dikelompokkan jadi 12 butir keputusan.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Satu formulir untuk satu order, dibuka sesudah discovery meeting | Ketentuan butir 1; Lingkup | owner |
| 2 | Formulir memadukan calon rekaman Business Requirement (COM-SOP-01 butir 6.3) dan calon Catatan review scope (COM-SOP-02 butir 6.2), diisi dua tahap; diubah W9: SNX-COM-FRM-01 kini ditulis menyalin atau merujuk Business Requirement di CRM (keluaran butir 6.3, USULAN) dan bentuk Catatan review scope (USULAN), tanpa kata "calon" (R2) | Ketentuan butir 3 dan 4; Dokumen Terkait | owner |
| 3 | Arti "Order diterima" dan larangan Business Development menyatakan order diterima sebelum Hasil Review sah | Istilah; Ketentuan butir 8 | owner dan Samuel |
| 4 | VP Commercial menetapkan Hasil Review dan menjadi pemilik formulir terisi; tiga nilai Hasil Review dan tiga nilai Status | Istilah; Ketentuan butir 7; tabel Peran; Rekaman | owner |
| 5 | Susunan aspek daftar periksa C1.1 sampai C4.6 dan pembagian pengisinya | Isi Formulir; tabel Peran | owner |
| 6 | Aspek C3.6: kesesuaian jenis order dengan perizinan di SNX-LEG-REG-01 | Isi Formulir C3.6; Dokumen Terkait | Legal |
| 7 | Aspek C4.6: ketersediaan tim pelaksana pada timeline | Isi Formulir C4.6 | Fani |
| 8 | COO sebagai pemilik dokumen menurut blok Identity (hasil aturan "jabatan reviewer"); ditutup W9: COO tidak lagi pemilik dokumen, Process Owner VP Commercial (A7) | Tabel Peran | owner |
| 9 | Manager of Product Tech mengeskalasi solusi yang tidak feasible kepada VP Commercial (selaras COM-SOP-02 butir 4.15) | Tabel Peran | owner |
| 10 | Order tambahan dan perpanjangan untuk customer yang sudah berjalan di luar scope | Lingkup | owner |
| 11 | Status calon dari SNX-COM-FRM-02, SNX-LEG-FRM-01 sebagai daftar periksa lengkap, dan SNX-LEG-REG-01 sebagai tempat perizinan; diubah W9: SNX-COM-FRM-02 ditulis sebagai rekaman serah terima tanpa "calon" dan tanpa USULAN (butir 6 dan R2); SNX-LEG-FRM-01 dan SNX-LEG-REG-01 tetap USULAN | Lingkup; Dokumen Terkait | Legal |
| 12 | Daftar klausul ISO 9001:2015 (8.2.1, 8.2.2, 8.2.3, 8.2.4, 7.5.3) dan ISO/IEC 27001:2022 (4.2, Annex A 5.31, 5.12), label "(USULAN, perlu konfirmasi konsultan)" | Rekaman dan Acuan ISO | owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Process Owner "Direktur" (COO) mengikuti aturan dokumen tanpa sumber di defaults. SNX-COM-SOP-01 dan SNX-COM-SOP-02 memakai VP Commercial karena Sales SOP menulis "Document Owner: VP of Commercial". Putuskan apakah formulir ini juga berpemilik VP Commercial; bila ya, blok Identity dan tabel Peran perlu diubah; ditutup W9: Process Owner diputus VP Commercial (A7) | owner |
| 2 | SNX-COM-SOP-01 butir 6.7 (Closing) dan butir 4.15 belum menyebut formulir ini; Closing hanya mensyaratkan "PO diterima", "kontrak ditandatangani", "persetujuan internal selesai". Perlu satu rujukan satu arah dari SOP ke formulir, titik pemakaian di antara PO sampai dan pernyataan menerima order, dan kepastian bahwa formulir ini memegang dua peran calon rekaman (cacat tambahan A dan B) | owner |
| 3 | Pemutus penerimaan order belum ada di sumber. Penetapan VP Commercial (USULAN 4) belum memuat batas nilai atau jenis order yang perlu COO atau Direktur Utama. Authority Matrix belum bernomor; harga dan margin di COM-SOP-02 butir 4.7 masih USULAN | owner dan Samuel |
| 4 | Tenggat penyelesaian kelompok C1 sampai C4 dan Hasil Review tidak ada di sumber; formulir tidak memuat angka waktu | owner |
| 5 | Kanal permintaan review dari Business Development ke Manager of Product Tech dan Service Delivery Manager: Zammad (Ops) atau GLPI (generalist). Batas lingkup "generalist" belum dirinci owner | owner |
| 6 | Lokasi simpan, pemilik, dan retensi formulir terisi, PO, kontrak, dan hasil review kontrak belum ditetapkan di sumber mana pun | owner dan Legal |
| 7 | Kelayakan operasi (dukungan NOC atau SOC sesudah live) tidak masuk formulir. POL-OPS-001 menaruh Operation sebagai pihak Consulted pada discovery dan sizing; pengisi di formulir ini belum diputus | Fani |
| 8 | Service Delivery Manager adalah jabatan usulan tanpa pemegang (HR-ORG-01 K-10); kelompok C4 belum punya pengisi bernama | Fani dan owner |
| 9 | Nama produk CRM dan lokasi simpan berkas penawaran belum disebut sumber | owner |
| 10 | PPN pada harga order dan TOP standar masih USULAN di SNX-FAT-SOP-01 (butir 4.5 dan 4.8); aspek C3.2 dan C3.3 hanya merujuk, tanpa tarif atau hari | FAT |
| 11 | Formulir kosong INTERNAL, formulir terisi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 butir 4.3. Apakah blok Identity cukup memuat INTERNAL, atau formulir terisi perlu label footer | Fani |
| 12 | Susunan aspek C1 sampai C4 belum dikonfirmasi pemilik proses; Legal perlu mencocokkan C3.4 sampai C3.7 dengan SNX-LEG-FRM-01 supaya tidak ada aspek ganda | Legal dan owner |
| 13 | Penyebutan SNX-COM-FRM-02 (Project Handover Record) bergantung pada isi dokumen itu, yang disusun lane lain di wave yang sama; ditutup W9: SNX-COM-FRM-02 sudah ada dan ditulis sebagai rekaman serah terima | owner |
| 14 | Klausul ISO belum dicocokkan dengan teks standar | owner, diteruskan ke konsultan |
| 15 | Tidak ada kalimat perintah kepada AI di sumber yang dibaca. Tidak ada open item dari sisi ini | - |

## 5. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya tujuh tanda; semuanya sudah diperbaiki, satu dibiarkan:
   - Aspek yang sama diberi dua nama: "jadwal" dan "timeline", "dependency" dan "dependensi", "persyaratan customer" dan "kebutuhan customer". Diperbaiki: satu istilah per hal (timeline, dependensi, kebutuhan untuk yang customer minta, persyaratan kontraktual untuk syarat di PO atau kontrak).
   - Definisi "Dokumen order" menyebut penawaran yang sudah terkirim, padahal tahap pertama berlangsung sebelum penawaran terkirim. Diperbaiki: definisi mencakup draf dan versi terkirim.
   - Kalimat "Ketentuan butir 10 mewajibkan lokasinya tertulis" memberi bagian dokumen kata kerja manusia. Diperbaiki: pelakunya Business Development. Kalimat "Butir 4.11 melarang ..." diganti "berisi larangan".
   - "meminta peran ... menilai ulang kelompoknya" bertabrakan dengan istilah "Review ulang". Diperbaiki: "mengisi ulang kelompoknya".
   - Judul h2 bernomor ganda ("6.4 C1. ...") membuat tabel sulit dirujuk. Diperbaiki: huruf A sampai G dibuang, kelompok memakai "Kelompok C1: ...".
   - Kolom No. dan Rujukan terlalu sempit sehingga kode C1.1 terpotong menjadi dua baris. Diperbaiki: kolom dilebarkan.
   - Dibiarkan: hampir tiap butir Ketentuan dan baris Peran dibuka dengan "Business Development", dan kolom Hal yang Diperiksa memakai pola "X sesuai dengan Y". Itu mengikuti aturan satu pelaku per butir (RUNBOOK 6a.1) dan satu pelaku mengerjakan sebagian besar langkah. Enam unsur di kalimat Tujuan adalah daftar dari kriteria baris 52, bukan kelompok tiga yang dipaksakan.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa terhadap tabel Fakta kunci, Fakta penting lain, dan pemetaan peran:
   - Angka: nol angka waktu, nilai, persen, atau ambang di dokumen. Angka yang ada hanya nomor klausul ISO dan nomor butir dokumen SNX yang dirujuk, kode JA-nn, dan K-10. Angka dari sumber (14 hari TOP, availability, 24 jam CRM, batas respons) tidak dibawa.
   - Nama: Laras Rasmawati, Amirull Yusuf Zulkarnain, dan Samuel Kristanto Utomo hanya di blok approval (prompt dan defaults). Nol nama orang lain. Nama peran dari SNX-HR-ORG-01; Service Delivery Manager adalah jabatan usulan tanpa pemegang.
   - Tanggal: nol di dokumen. Tanggal di notes ini adalah modifiedTime berkas sumber.
   - Tanpa kutipan sumber tetapi ada di dokumen, semuanya berlabel USULAN atau tercatat di notes: definisi umum Assumptions, BOM/BOQ, Exclusions, TOP (disalin dari definisi COM-SOP-02, bukan kalimat Sales SOP); susunan aspek C1 sampai C4 dan nilai Status serta Hasil Review (USULAN 4 dan 5); aspek C3.6 dan C4.6 (USULAN 6 dan 7); pembagian dua tahap (USULAN 2); judul klausul ISO (USULAN 12).
   - Tidak berlabel di dokumen tetapi tafsir saya: pembagian pengisi C3 antara Business Development dan Legal & Compliance (asumsi 5), dan pengecualian "order tambahan dan perpanjangan" yang diturunkan dari COM-SOP-01 butir 4.17 (berlabel USULAN di Lingkup).
   - Rujukan butir ke dokumen lain (COM-SOP-01 butir 4.3, 4.11, 4.17, 4.19, 6.3, 6.8; COM-SOP-02 butir 4.10, 4.15, 6.2, 6.4; LEG-SOP-02 butir 6.1; FAT-SOP-01 butir 4.5, 4.8; OPS-SOP-01 butir 4.1; OPS-SOP-05 butir 4.1; ISMS-PRO-01 butir 4.3; HR-ORG-01 K-10) dicocokkan dengan spec di repo saat saya menulis. Spec lane lain masih Draft dan bisa berubah. SNX-OPS-FRM-06 dan SNX-LEG-REG-01 dicocokkan hanya pada judul (specs/OPS-FRM-06.json dan specs/LEG-REG-01.json), isinya tidak dibaca.

## Sweep

Putaran penghalusan atas perintah orkestrator (berkas /tmp/claude-0/prompts/COM-FRM-01.sweep.txt). Satu butir diubah, di specs/COM-FRM-01.json saja.

| # | Lokasi | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Aspek C3.2, kolom Hal yang Diperiksa | "Harga dan diskon di PO atau kontrak sama dengan penawaran yang COO setujui (Catatan persetujuan penawaran, SNX-COM-SOP-02 butir 4.15). Perlakuan PPN mengikuti SNX-FAT-SOP-01 butir 4.5." | "Harga dan diskon di PO atau kontrak sama dengan penawaran yang COO setujui menurut SNX-COM-SOP-02 butir 4.7, wewenang yang berstatus USULAN di dokumen itu. Rekaman persetujuannya Catatan persetujuan penawaran (butir 4.15). Perlakuan PPN mengikuti SNX-FAT-SOP-01 butir 4.5." |

Catatan: butir 4.7 sekarang menjadi rujukan wewenang COO, butir 4.15 tetap hanya untuk rekaman. Isi bagian 3 butir 5 notes ini (C3.2 merujuk butir 4.7) kini cocok dengan docx. Tidak ada keputusan baru; status USULAN wewenang COO tetap dibawa dari SNX-COM-SOP-02, pemutus open item 3 (owner dan Samuel). Temuan nonblocking lain di qa/COM-FRM-01.verify.json tidak diubah karena di luar butir perintah.

Uji sesudah perubahan: render_sop.py selesai tanpa galat; lint_doc.py generic "pass": true, fails kosong, satu warn "19 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan.py "ok 17 COM-FRM-01.docx []".

### Sweep r1 (perbaikan pemblokir: butir 4.15 SNX-COM-SOP-02 dihapus)

SNX-COM-SOP-02 kini hanya punya butir 4.1 sampai 4.14 (specs/COM-SOP-02.json dibaca ulang). Lima rujukan "butir 4.15" di specs/COM-FRM-01.json diganti. Mulai dari sini, penyebutan "butir 4.15" di bagian lain notes ini (bagian 1 sampai 5 dan Sweep di atas) bersifat historis dan tidak lagi berlaku.

| # | Lokasi | Sebelum | Sesudah | Dasar padanan |
|---|---|---|---|---|
| 1 | Aspek C3.2 | "... wewenang yang berstatus USULAN di dokumen itu. Rekaman persetujuannya Catatan persetujuan penawaran (butir 4.15)." | "... wewenang yang berstatus (USULAN) di dokumen itu. Catatan persetujuan penawaran memuat persetujuan itu (bagian 11 SNX-COM-SOP-02)." Label dibakukan jadi "(USULAN)" dan kalimat diberi predikat, keduanya di kalimat yang sama | Tabel rekaman COM-SOP-02: "Catatan persetujuan penawaran" ada di bagian 11, tanpa butir |
| 2 | Tabel Peran, Manager of Product Tech | "(USULAN, SNX-COM-SOP-02 butir 4.15)" | "(USULAN, SNX-COM-SOP-02 butir 4.5)" | COM-SOP-02 butir 4.5 kini memuat eskalasi solusi tidak feasible ke VP Commercial (USULAN) |
| 3 | Tabel Peran, VP Commercial | "(USULAN, selaras dengan SNX-COM-SOP-02 butir 4.15)" | "(USULAN, selaras dengan bagian 11 SNX-COM-SOP-02)" | Tabel rekaman COM-SOP-02 menulis pemilik Catatan persetujuan penawaran VP Commercial, tanpa butir |
| 4 | Dokumen Terkait, SNX-COM-SOP-02 | "butir 4.15 dan 4.10 mengatur Catatan persetujuan penawaran dan pemutus pengecualian komersial, dan butir 6.4 mengatur prosesnya" | "butir 4.10 mengatur pemutus pengecualian komersial, butir 6.4 mengatur prosesnya, dan bagian 11 memuat Catatan persetujuan penawaran" | Butir 4.10 dan 6.4 masih ada; rekaman di bagian 11 |
| 5 | Rekaman, baris Catatan persetujuan penawaran | "Pemilik: VP Commercial (SNX-COM-SOP-02 butir 4.15)." | "Pemilik: VP Commercial (bagian 11 SNX-COM-SOP-02)." | Tabel rekaman COM-SOP-02 |

Jumlah "(USULAN)" persis di spec naik dari 19 ke 20 karena label di butir 1. Tidak ada keputusan baru; status USULAN dibawa dari SNX-COM-SOP-02. Dua temuan nonblocking lain di qa/COM-FRM-01.sweep.r1.json (baris COO di tabel Peran tanpa rujukan, dan temuan verifikasi lama) tidak diubah karena di luar perintah.

Uji: `python3 -I reports/orch/refcheck.py COM-FRM-01` memberi `{}`; render_sop.py tanpa galat; lint_doc.py generic "pass": true, fails kosong, satu warn "20 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan.py "ok 17 COM-FRM-01.docx []".

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A7 Identity | Process Owner "Direktur" | Process Owner "VP Commercial" |
| A7 Peran, baris VP Commercial | "Pemilik formulir terisi (USULAN, selaras dengan bagian 11 SNX-COM-SOP-02)." | "Pemilik dokumen ini menurut blok Identity (USULAN) dan pemilik formulir terisi (USULAN)." (sekaligus butir 5: rujukan bagian 11 dihapus karena bagian 11 SNX-COM-SOP-02 tidak menetapkan pemilik Catatan review scope; VP Commercial sebagai pemilik proses ada di bagian 5 SNX-COM-SOP-02, bukan rujukan yang dipakai di sini) |
| A7 Peran, baris COO | "Pemilik dokumen ini menurut blok Identity (USULAN). Menyetujui harga ..." | "Menyetujui harga ..." |
| A7 Kesimpulan | "COO meninjau formulir ini setiap tahun" | "VP Commercial meninjau formulir ini setiap tahun" |
| 6 Dokumen Terkait / Lingkup | "Calon rekamannya SNX-COM-FRM-02 (USULAN)." (baris Serah terima order ke Delivery) | "Rekaman serah terimanya SNX-COM-FRM-02." |
| 6 Dokumen Terkait, SNX-COM-FRM-02 | "Calon rekaman paket handover sesudah order diterima (USULAN)." | "Rekaman paket handover sesudah order diterima." |
| R2 1a Dokumen Terkait, baris SNX-COM-SOP-02 | "Formulir ini calon bentuk Catatan review scope (USULAN)." | "Formulir ini bentuk Catatan review scope (USULAN)." |
| R2 2 Dokumen Terkait, baris SNX-COM-SOP-01 | "Formulir ini calon rekaman Business Requirement di butir 6.3 (USULAN)." | "Formulir ini menyalin atau merujuk Business Requirement di CRM, keluaran butir 6.3 (USULAN)." |

Butir 3 (A3): COM-FRM-01 hanya menulis "Jabatan JA-03 di SNX-HR-ORG-01"; tidak ada atasan atau garis lapor JA-03/JA-04 yang perlu diselaraskan.

Open item ditutup atau diubah:
- Open item 1 (Process Owner Direktur vs VP Commercial): ditutup W9 (A7).

R2 butir 3: baris USULAN dan Open items yang ditutup atau diubah W9 diberi keterangan "ditutup W9" atau "diubah W9" di barisnya sendiri.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Peran, baris VP Commercial: "Pemilik dokumen ini menurut blok Identity (USULAN) dan pemilik form terisi (USULAN)." Ditulis ulang "Pemilik form ini dan form terisi (USULAN)."; dua label digabung menjadi satu label di akhir butir (STYLE §3.5). Isi usulan tidak berubah.
### W10 kalimat dihapus atau dipindah
- Peran, kalimat penunjuk dihapus: "(Ketentuan butir 1, 3 sampai 6, dan 8 sampai 10)", "(Ketentuan butir 3 dan 4)" (Manager of Product Tech dan Service Delivery Manager), "(Ketentuan butir 4 dan 5)", "(Ketentuan butir 7)". Tugasnya sudah tertulis di sel yang sama.
- Rekaman, baris Form terisi per order: rujukan "(Ketentuan butir 10)" dihapus (penunjuk).
- Peran, baris Business Development: "Dipetakan ke Business Development (JA-07) di SNX-HR-ORG-01." ditulis ulang "Jabatan JA-07 di SNX-HR-ORG-01." (catatan pemetaan dijadikan fakta jabatan, sama dengan baris lain).
- Peran, baris Service Delivery Manager, catatan pemetaan dipindah ke sini: "Jabatan usulan tanpa pemegang di SNX-HR-ORG-01 (K-10)." Fakta yang sama tetap tertulis di Dokumen Terkait baris SNX-HR-ORG-01.
- "Kolom Status berisi satu dari tiga nilai pada bagian Istilah" dan "Kolom Status memakai nilai pada bagian Istilah" diganti faktanya: Sesuai, Perlu Tindak Lanjut, atau Tidak Berlaku.
### W10 selisih angka
nihil (subst_diff build kosong).
### W10 catatan
- Sebutan pihak luar: customer (dipakai di semua dokumen Commercial; "pelanggan" hanya tersisa di judul klausul ISO 9001 8.2.1).
- Padanan heading pada kemunculan pertama: "Form (formulir)" di Tujuan, "record (rekaman)" di Hasil yang dijaga. Acuan ISO "Bagian Record" diganti "Tabel Rekaman" mengikuti heading.
- Lebar kolom daftar periksa C1 sampai C4 menjadi 1,4/2,9/6,4/2,0/3,3 cm agar kode aspek tidak terpotong dan kolom Catatan lebih lebar; min_row_cm 1,0 pada tabel Temuan dan Tindak Lanjut serta Catatan Review dan Persetujuan.
- Calque diperbaiki 8 (termasuk "yang COO setujui" yang tidak terdeteksi pemindai).

### W10 label digabung (dicatat worker, STYLE §3.5 dan §3.6)
- tabel Peran, VP Commercial: beberapa label (USULAN) digabung menjadi satu label di akhir butir; tidak ada aturan yang kehilangan status USULAN.
  - Asli: "Menetapkan Hasil Review, menulis dasarnya, dan memeriksa kolom Selesai (Ketentuan butir 7). Pemilik dokumen ini menurut blok Identity (USULAN) dan pemilik formulir terisi (USULAN). Jabatan JA-03 di SNX-HR-ORG-01."
  - W10: "Menetapkan Hasil Review, menulis dasarnya, dan memeriksa kolom Selesai. Jabatan JA-03 di SNX-HR-ORG-01. Pemilik form ini dan form terisi (USULAN)."

### W10 rujukan USULAN dicek (adjudikasi worker, gerbang rujukan USULAN)
- .sections[3].blocks[0].table.rows[0][1]: tanpa label; uraian tugas umum Business Development, kewajiban berlabel (USULAN) di Ketentuan tidak dinyatakan ulang (keputusan sama dengan LEG-FRM-01 tabel Peran).
### W10 audit pointer
- .sections[3].blocks[0].table.rows[0][1]: lengkap; penunjuk balik "(Ketentuan butir 1, 3 sampai 6, dan 8 sampai 10)" dibuang; tugas Business Development tertulis di sel yang sama dan langkahnya tetap di Ketentuan butir 1 sampai 10.
- .sections[3].blocks[0].table.rows[1][1]: lengkap; penunjuk "(Ketentuan butir 3 dan 4)" dibuang; tugas C2, eskalasi, label (USULAN), dan rujukan SNX-COM-SOP-02 butir 4.5 tetap.
- .sections[3].blocks[0].table.rows[2][1]: lengkap; penunjuk "(Ketentuan butir 3 dan 4)" dibuang; catatan "Jabatan usulan tanpa pemegang (K-10)" tercatat terpisah di atas, fakta tetap di Dokumen Terkait baris SNX-HR-ORG-01.
- .sections[3].blocks[0].table.rows[3][1]: lengkap; penunjuk "(Ketentuan butir 4 dan 5)" dibuang; tugas C3.4 sampai C3.7 dan rujukan SNX-LEG-SOP-02 tetap.
- .sections[3].blocks[0].table.rows[4][1]: lengkap; penunjuk "(Ketentuan butir 7)" dibuang; tugas menetapkan Hasil Review dan memeriksa kolom Selesai tetap; urutan dan syaratnya tetap di Ketentuan butir 7.
- .sections[7].blocks[1].table.rows[0][1]: lengkap; penunjuk "(Ketentuan butir 10)" dibuang; pencatat, pemilik (USULAN), lokasi, dan klasifikasi tetap.

### W10 audit cakupan label
- .sections[2].blocks[0].p: OK (label tetap hanya pada satu form untuk satu order)
- .sections[3].blocks[0].table.rows[1][1]: diperbaiki (kalimat dipisah lagi; mengisi kelompok C2 keluar dari kalimat berlabel, label hanya pada eskalasi)
- .sections[3].blocks[0].table.rows[4][1]: OK (dua label pemilik digabung, cakupan sama)

### W11 koreksi LEAD (cakupan dikembalikan ke bed1bb6, 15 Okt)
- .sections[0].blocks[5].table.rows[4][1]: cakupan, label, pelaku, atau rujukan dikembalikan ke bed1bb6 (temuan pemeriksa makna buta LEAD, reports/w11/)
