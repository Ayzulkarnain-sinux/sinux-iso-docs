# Catatan penyusun COM-SOP-01: SOP Sales Process

Status: DRAFTED (spec + notes ada). Spec: specs/COM-SOP-01.json. Mode sop, aksi T1, wave W3, nomor SNX-COM-SOP-01 (nomor SNX lama dipertahankan), department Commercial, classification INTERNAL (worklist), audit_class C2, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Laras Rasmawati / VP Commercial", reviewed "Amirull Yusuf Zulkarnain / Direktur", approved "Samuel Kristanto Utomo / President Director".

Uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-SOP-01.json /tmp/pen-COM-SOP-01/COM-SOP-01.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-COM-SOP-01/COM-SOP-01.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "12 butir (USULAN) menunggu ACC" (nol warn PIC SLA). Validator OOXML skill docx (`/mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!". Pratinjau PDF (soffice) 20 halaman; halaman 15 dilihat pada 110 dpi: diagram 19 simpul, rankdir TB, muat satu halaman, semua label terbaca. Lint dan validator hanya membuktikan format dan larangan pola; kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 1. SALES STANDARD OPERATING PROCEDURE.pdf (2.666.844 byte, 16 bagian, 19 halaman) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (lapisan teks PDF). Urutan teks di lapisan itu bercampur antar kartu (judul tahap, kriteria, dan deliverable berselang-seling); susunan tabel dicocokkan dengan transkripsi di context/audit/iso-sinux-supdocs-commercial-2026-10-14.md. Gambar halaman tidak dibuka di sesi ini (UNMEASURED); panah rantai persetujuan di halaman 10 saya ambil dari catatan audit (render 150 dpi mereka) |
| 2. Commercial Onboarding. Jul 2026.pdf (6.285.535 byte, 27 slide) | 16TIN9Tsv_sBXMrL4KHeO8f6Ao0F-KsAS | 2026-10-05T07:10:01.246Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (lapisan teks). Deck ini 80 detik lebih baru daripada SOP. SOP tetap sumber utama karena dokumen yang diperbaiki; deck dipakai untuk ICP, MEDDICC, SPIN Selling, status CRM, dan sebagai pembanding cacat |
| Kriteria penerimaan | config/checklist.json baris 47 | checklist tidak diukur ulang | Description: "Mengatur lead generation, qualification, opportunity management, customer communication, negosiasi, closing, dan handover." Dipenuhi: Purpose (kalimat pertama menyebut ketujuhnya), dan butir 6.1 Lead Generation, 6.2 Qualification, 6.3 dan 6.4 Opportunity Management, 6.5 Customer Communication, 6.6 Negosiasi, 6.7 Closing, 6.8 Handover |
| Pendukung repo (bukan Drive) | config/defaults.json v21 (data_conflicts), specs/HR-ORG-01.json (daftar jabatan, matriks peran, K-10, K-13), specs/HR-JA-01.json (JA-03, JA-05, JA-06, JA-07), specs/OPS-SOP-01.json dan specs/OPS-PRC-01.json (paket G1), specs/ISMS-PRO-01.json (4.3, 4.10), specs/LEG-SOP-02.json (4.1, 4.3, 6.1), specs/FAT-SOP-01.json (langkah Business Development), context/audit (bagian COM-Sales-SOP dan COM-Commercial-Onboarding-Jul2026) | repo kerja | Dibaca sebagai DATA. Kutipan dari spec lain bisa basi bila dokumen itu berubah. specs/LEG-SOP-02.json ditulis lane lain dan masih Draft saat saya baca |

Kalimat perintah kepada AI di sumber: nihil. Sumber memuat kalimat kewajiban untuk karyawan ("Sales wajib ..."), itu isi SOP, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Proposal hanya dibuat setelah discovery selesai, dan sebelum dikirim ke customer harus melewati tiga pemeriksaan berurutan: review internal, approval harga, approval diskon (jika ada). Dasar butir 4.6, 4.9, dan langkah 6.4 | "Proposal hanya dibuat setelah Discovery selesai. Demo dilakukan bersama Presales apabila diperlukan." dan "Sebelum dikirim ke customer:" lalu "Review internal." "Approval harga." "Approval diskon (jika ada)." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| CRM wajib memuat seluruh aktivitas penjualan dan diperbarui paling lambat 24 jam. Dasar butir 4.3 dan baris SLA | "Seluruh aktivitas penjualan wajib dicatat di CRM." dan "CRM harus diperbarui maksimal 24 jam setelah aktivitas dilakukan." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Handover wajib, dengan handover meeting sebelum implementasi dan enam butir minimal. Dasar butir 4.16 dan 6.8 | "Sales wajib melakukan handover kepada Delivery." lalu "Handover meeting wajib dilakukan sebelum implementasi dimulai." dengan butir "Customer Background", "Scope", "Timeline", "Risks", "Commitment", "Contact Person" | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

Fakta penting lain:

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi |
|---|---|---|---|
| 1 | Pemilik dokumen = VP Commercial (process_owner) | "Commercial Department Document Owner: VP of Commercial" | Sampul SOP; SOP sumber, fileId 19Hex8... |
| 2 | Siklus tinjau sumber 6 bulan; dokumen ini YEARLY menurut defaults | "Review Cycle: Every 6 Months" | Sampul SOP |
| 3 | Lima kriteria qualification dan metode | "Sebelum opportunity masuk ke tahap Proposal, Sales harus memastikan opportunity telah memenuhi kriteria qualification menggunakan BANT atau MEDDICC, serta telah melakukan discovery melalui pendekatan SPIN Selling" | 02 Stage 2, butir 4.6. Kriteria: "Business Need", "Budget", "Decision Maker", "Timeline", "Technical Fit" |
| 4 | Larangan harga dan janji (butir 4.11) | "Sales tidak diperbolehkan:" "Mengubah pricing sendiri." "Memberikan diskon tanpa persetujuan." "Menawarkan fitur yang belum tersedia." "Menjanjikan timeline tanpa konfirmasi Delivery." | 08 Proposal & Pricing Policy |
| 5 | Negosiasi: diskon harus ber-approval, negosiasi strategis melibatkan VP Commercial | "Tidak memberikan diskon tanpa approval." dan "Melibatkan VP Commercial apabila negosiasi strategis." | Stage 7 |
| 6 | Batas respons | "Maksimal 1 hari kerja." (Email), "Maksimal 2 jam kerja." (WhatsApp), "Maksimal 4 jam kerja." (Internal Request) | 07 Customer Communication Standard |
| 7 | Definisi closing berhasil | "Closing dinyatakan berhasil apabila:" "Purchase Order diterima." "Kontrak ditandatangani." "Internal approval selesai." "Project Kick-off atau implementasi telah dimulai sesuai dengan ruang lingkup yang disepakati." | Stage 8 |
| 8 | Dokumen lengkap sebelum handover | "Sales wajib memastikan seluruh dokumen lengkap sebelum handover." | Stage 8 |
| 9 | Delapan kondisi eskalasi ke VP Commercial (bagian 9) | "Segera eskalasikan kepada VP Commercial apabila terjadi:" lalu delapan butir (dua di antaranya "Permintaan diskon di luar kewenangan" dan "Opportunity bernilai strategis") | 14 Escalation Matrix |
| 10 | Penyimpangan prosedur (butir 4.20, bagian 9) | "Penyimpangan terhadap prosedur harus mendapatkan persetujuan dari VP Commercial atau pihak yang berwenang." | 16 SOP Compliance |
| 11 | Lingkup kolaborasi Legal (dasar langkah Legal, USULAN) | "NDA preparation/review" "Contract review" "Commercial terms & conditions" "Contract negotiation support" "Legal compliance" | 09 Internal Collaboration |
| 12 | Scope sumber hanya menyebut Business Development | "SOP ini berlaku untuk seluruh tim Commercial yang saat ini terdiri dari:" lalu satu butir "Business Development" | 02 Scope |
| 13 | Status CRM | "Leads" "Qualified" "Opportunity" "Bid (Proposal/Quote submitted)" "Win/Lost" "Future Nurture" | Deck slide 15, fileId 16TIN9Tsv_sBXMrL4KHeO8f6Ao0F-KsAS |
| 14 | MEDDICC, definisi di definisi dokumen | "MEDDICC adalah framework untuk mengelola dan mengevaluasi kualitas opportunity agar peluang closing lebih tinggi." | Deck slide 13 |
| 15 | Deck menyebut pemberi pricing approval yang tidak ada di struktur organisasi | "Commercial Manager → Pricing & Deal Approval" | Deck slide 16 |
| 16 | Wewenang VP Commercial atas harga (dasar butir 4.10) | "Merekomendasikan harga/diskon untuk persetujuan" | specs/HR-JA-01.json JA-03 Wewenang butir 1 |
| 17 | Wewenang Business Development (dasar butir 4.11) | "Menegosiasikan dalam batas penawaran disetujui" dan "Mengeskalasi diskon/scope yang belum disetujui" | specs/HR-JA-01.json JA-07 Wewenang butir 2 dan 3 |
| 18 | Penerimaan paket handover oleh Delivery | "proyek dimulai hanya sesudah Service Delivery Manager menerima paket G1 dari Commercial" | specs/OPS-SOP-01.json butir 4.1 |
| 19 | Berbagi informasi RESTRICTED hanya dengan NDA atau kontrak | "RESTRICTED dibagikan hanya dengan NDA atau kontrak yang berlaku dan persetujuan Pemilik informasi." dan "Informasi pelanggan minimal RESTRICTED" | specs/ISMS-PRO-01.json butir 4.10 dan 4.3 |
| 20 | Persetujuan Legal sebelum tanda tangan | "Tidak ada kontrak yang ditandatangani sebelum Persetujuan Legal dan semua persetujuan lain yang diwajibkan diperoleh." | specs/LEG-SOP-02.json butir 4.1 |

## 2. Keputusan data dan pemetaan peran

- Sebutan: Direktur (COO) hanya di tabel Definisi (penyebutan pertama di badan dokumen, baris istilah "Direktur (COO)"); sesudahnya COO. Nama Samuel tidak muncul di badan, hanya di blok Approved By (President Director). Nama Laras dan Amirull tidak muncul di badan.
- process_owner "VP Commercial": sumber punya medan "Document Owner: VP of Commercial", jadi bukan USULAN. Nama peran mengikuti HR-ORG-01 (JA-03 "VP Commercial"); sumber menulis "VP of Commercial".
- Tiket (Zammad atau GLPI), vault, PPN: sumber tidak menyebutnya, jadi tidak muncul di badan. Satu rujukan tidak langsung: langkah mengajukan review kontrak dan NDA ke Legal merujuk SNX-LEG-SOP-02 butir 6.1, dan dokumen itu memakai tiket GLPI (USULAN) untuk pengajuan. Saya tidak menulis "GLPI" di dokumen ini agar kanalnya hanya ditetapkan di satu tempat.
- Klasifikasi dokumen INTERNAL (worklist, SOP umum). Data customer, kontrak, dan harga di butir 4.13 diberi RESTRICTED (Internal) sebagai USULAN karena SNX-ISMS-PRO-01 menyebut Commercial belum tercakup.
- Istilah: "customer" dipakai (istilah sumber), bukan "pelanggan" (istilah dokumen Operation) atau "klien" (dokumen FAT). "Business Development" dipakai untuk semua pelaku yang di sumber disebut Sales, Sales Executive, atau tim Sales. "persetujuan" dipakai untuk semua jenis approval (sumber memakai approval dan persetujuan bergantian); "review" dipakai untuk pemeriksaan internal dan kontrak. "Risks" dipakai pada daftar enam butir handover agar sejajar dengan label Inggris lain di daftar itu.

Pemetaan peran sumber ke nama peran di bagian 5 (basis: specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Sales, Sales Executive, tim Sales, Business Development | Business Development | JA-07 Business Development, unit Commercial; tugasnya (prospek, kualifikasi, CRM, demo, proposal, negosiasi, serah terima kontrak) cocok dengan SOP sumber. Penyebutan "Sales" dan "Sales Executive" sebagai Business Development adalah tafsir, USULAN 7 |
| VP of Commercial, VP Commercial | VP Commercial | JA-03 |
| Presales, Presales / Solution Consultant | Manager of Product Tech | HR-ORG-01 tidak punya jabatan Presales. JA-05 punya tugas "Mendukung demo/PoC, technical clarification dan pembahasan solusi pelanggan" dan JA-07 "Mengoordinasikan demo/technical discovery dengan Product Tech". Tafsir, USULAN 7 |
| Delivery, Project Delivery | Delivery (sub divisi); peran Service Delivery Manager | OPS-SOP-01 dan OPS-PRC-01: paket G1 diterima Service Delivery Manager. Jabatan itu USULAN tanpa pemegang (HR-ORG-01 K-10). USULAN 7 |
| Commercial Manager (deck, Pricing & Deal Approval) | tidak dipakai; fungsinya masuk butir 4.10 (VP Commercial merekomendasikan, COO menyetujui) | Tidak ada jabatan itu di HR-ORG-01. USULAN 2 |
| Legal | Legal & Compliance | JA-08 dan JA-09 memakai nama jabatan yang sama. Nama "Line Manager Legal" dan "Staff Legal" di SNX-LEG-SOP-02 tidak dipakai di sini karena pemetaannya ke JA-08 dan JA-09 masih USULAN (K-13) |
| Finance | Finance | JA-10. Finance Lead dan Finance Staff di dokumen FAT belum dipetakan (K-13), jadi tidak dipakai |
| Marketing | Brand & Marketing | JA-06; tugasnya menurut JA-06: "Menyerahkan qualified leads ke Commercial beserta sumber dan statusnya" |
| Management | COO (untuk persetujuan harga) | Sumber hanya menyebut Management pada Prinsip 5 dan deck slide 16 tanpa rincian tugas; peran persetujuan harga diberikan ke COO lewat USULAN 2 |
| Procurement, Technical Support / Managed Services | tidak dipakai | Sumber menyebut tanpa tugas dalam proses sampai handover (Procurement di Prinsip 5; Technical Support hanya di deck slide 16 sebagai After Sales Support, di luar scope) |
| Pelaksana tanda tangan kontrak, pemberi internal approval | tidak dipetakan | Authority Matrix belum bernomor (HR-ORG-01); open item 7 |

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah; grep fileId 19Hex8... dan 16TIN9...)

Sumber 1, Sales SOP (fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Scope hanya "Business Development" padahal isi menyebut Sales Executive, Presales, VP Commercial; komposisi tim tidak konsisten | Diperbaiki: scope menyebut VP Commercial, Business Development, dan Brand & Marketing (unit Commercial menurut HR-ORG-01) dan fungsi lain lewat tabel peran. Lihat pemetaan peran |
| 2 | Tidak ada approver, riwayat revisi, nomor, klasifikasi | Teratasi oleh template dan defaults: SNX-COM-SOP-01, Rev. 00, Draft, INTERNAL, tiga penanda tangan berbeda. "Version 1.0" dan "Effective Date 28th of July, 2026" milik sumber tidak dibawa: dokumen ini Draft rev 00 dengan tanggal efektif kosong (batas keras RUNBOOK 3) |
| 3 | Pricing dan diskon tanpa tingkat kewenangan, ambang, SLA approval, form; deck menyebut Commercial Manager, SOP menyebut VP Commercial | Sebagian diperbaiki: butir 4.10 (USULAN) menetapkan VP Commercial merekomendasikan dan COO menyetujui, margin final COO, sesuai catatan worklist. Ambang diskon, batas margin, dan tenggat approval tidak dikarang: open item 1 |
| 4 | Kriteria qualification SOP (Technical Fit) beda satu butir dengan deck (Project Scope); SOP "BANT atau MEDDICC", deck MEDDICC | Dipilih versi SOP (butir 4.6) karena SOP dokumen yang diperbaiki dan memuat kalimat gerbang proposal. Perbedaan deck dicatat: open item 3 |
| 5 | Stage 6 sampai 10 tanpa label Objective; Stage 2 sampai 10 tanpa KPI per tahap | Tidak perlu label Objective: tahap disusun sebagai prosedur 6.1 sampai 6.8 dengan satu pelaku per langkah. KPI dipindah ke butir 4.18 dalam tiga kelompok sumber, tanpa target |
| 6 | Tidak ada tenggat follow-up lead, approval internal, handover; hanya CRM 24 jam dan batas respons | Tabel SLA hanya memuat angka sumber (24 jam, 1 hari kerja, 2 jam kerja, 4 jam kerja) dan frekuensi Weekly Commercial Rhythm. Tenggat lain tidak dikarang: open item 1 dan 6 |
| 7 | Delivery penerima handover tanpa individu atau form; tidak ada tahap Delivery di 10 tahap; Stage 10 melewati scope | Diperbaiki sebagian: penerima = Service Delivery Manager dan keputusan di checklist G1 SNX-OPS-FRM-01 (USULAN 7), kalimat G1 mengikuti SNX-OPS-SOP-01 butir 4.1. Stage 10 Account Management dikeluarkan dari scope dan tanggung jawabnya dicatat di butir 4.17 (sumber sendiri menulis scope "mulai dari prospecting hingga handover"). Open item 9 dan 13 |
| 8 | KPI SOP (9 butir) tidak identik dengan 8 KPI deck dan KPI individu xlsx | Dipakai daftar SOP (butir 4.18). Target tiap KPI tidak ada di SOP dan dirujuk ke KPI Matrix (belum bernomor, HR-ORG-01). Open item 15 |
| 9 | Alat hanya "CRM" tanpa nama produk; "Sinux Knowledge Base" hanya di deck | Dokumen menulis CRM tanpa nama produk (open item 10). "Sinux Knowledge Base" tidak dibawa: tidak ada di SOP sumber dan tidak ada langkah yang memakainya |
| 10 | Larangan "fitur belum tersedia" dan "timeline tanpa konfirmasi" tanpa mekanisme verifikasi atau rekaman | Larangan dipertahankan (butir 4.11) dan konfirmasi timeline diberi pelaku (Service Delivery Manager) dan rekaman (langkah 6.4.3). Mekanisme verifikasi kepatuhan lain tidak dikarang (sumber hanya CRM) |
| 11 | Cacat tata letak halaman 3 (judul kartu bertumpuk) | Tidak berdampak: isi utuh di lapisan teks |

Sumber 2, Commercial Onboarding (fileId 16TIN9Tsv_sBXMrL4KHeO8f6Ao0F-KsAS):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 12 | Slide 9 Organization Structure kosong | Tidak ada yang diambil dari slide itu. Nama jabatan mengikuti SNX-HR-ORG-01 |
| 13 | Typo "Metodhology", "Digunakkan", "SMB" tanpa kurung tutup; "30609090 Days Plan" | Tidak dibawa; tidak ada butir itu di dokumen |
| 14 | ICP: Large Enterprise ">5.000" dan Enterprise "1.000+" tumpang tindih; rentang 100 sampai 199 tidak tercakup; satuan tidak ditulis | Rentang ukuran tidak disalin. Definisi ICP merujuk deck bagian 08. Open item 11 |
| 15 | Slide 7 dan 22 berbeda tingkat dan jumlah industri | Daftar industri tidak disalin ke dokumen; dirujuk lewat definisi ICP |
| 16 | Slide 15 (Project Scope) lawan SOP (Technical Fit); slide 16 (Commercial Manager) lawan SOP; daftar KPI slide 19 lawan SOP | Lihat nomor 4, 3, 8 di atas |
| 17 | Slide 10 tanpa detail produk; slide 13 memakai placeholder "Vendor A dan Vendor B" | Tidak dibawa. Profil perusahaan, produk, model bisnis, rencana 30-60-90, dan buying process customer di deck tidak masuk karena bukan prosedur penjualan (materi onboarding) |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Urutan Stage 2 dan Stage 3: syarat qualification di Stage 2 menuntut discovery sudah dilakukan, padahal Discovery Meeting adalah Stage 3 | Diperbaiki: butir 4.6 menetapkan dua syarat sebelum proposal (qualification dan discovery meeting selesai), tanpa membalik urutan tahap di prosedur |
| B | Closing "berhasil" memasukkan "Project Kick-off atau implementasi telah dimulai", sedangkan Stage 9 mewajibkan handover meeting sebelum implementasi dimulai dan Stage 8 menyebut dokumen lengkap "sebelum handover" | Diperbaiki sebagian: butir 4.15 mengambil tiga syarat pertama dan menaruh kick-off sesudah paket handover diterima (USULAN 5, selaras SNX-OPS-SOP-01 butir 4.1). Open item 8 |
| C | "Internal Request" (4 jam kerja) tidak jelas arah dan peminta | Didefinisikan "Permintaan dari fungsi internal SINUX kepada Business Development" (tafsir). Open item 6 |
| D | Laporan harian "jika diminta": peminta tidak disebut; penerima laporan mingguan dan bulanan tidak disebut (catatan audit: "Penerima laporan dan format tidak disebutkan") | Penerima = VP Commercial, ditandai USULAN di butir 4.19. Open item 5 |
| E | Paket handover sumber (enam butir) tidak sama dengan Checklist G1 di OPS-PRC-01 ("PO atau kontrak, scope final, SLA tertulis, PIC pelanggan, dan janji lisan tercatat") | Enam butir sumber dipertahankan (butir 4.16) dan keputusan gate memakai Checklist G1. Selisih isi tidak diselaraskan sendiri: open item 9 |
| F | Siklus tinjau sumber 6 bulan, defaults YEARLY | YEARLY dipakai (defaults mengalahkan sumber). Open item 2 |
| G | Frasa penekan dan slogan di sumber (Commercial Mindset, Objective 03, "Customer Success First", "Continuous Improvement", Success Metrics 15, "Thank You!") | Prinsip yang berupa aturan dibawa ke butir 4.1 sampai 4.5. Slogan Commercial Mindset, Objective, Success Metrics, dan Continuous Improvement tidak dibawa sebagai butir sendiri: tidak ada pelaku, tindakan, atau ukuran; "Lessons Learned" tetap ada di laporan bulanan (baris SLA). Prinsip 5 "Collaboration Drives Success" tercakup di tabel peran |
| H | Langkah Business Development di SNX-FAT-SOP-01 (kirim Google Form Data Subskripsi Klien saat PKS ditandatangani, butir 6.1 dokumen itu) tidak ada di SOP sumber | Tidak ditambahkan (bukan tuntutan Description). Dokumen FAT dicantumkan di Dokumen terkait. Open item 12 |

## 4. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kalimat pasif atau tanpa pelaku di sumber diberi pelaku, semuanya dikumpulkan di butir 4.19 dengan satu label (USULAN 6): review internal proposal, tinjauan pipeline dan laporan oleh VP Commercial, penyerahan paket handover, penyimpanan rekaman persetujuan (VP Commercial), NDA dan hasil review kontrak (Legal & Compliance), perbaikan paket ditolak (Business Development). Kutipan dasar: HR-JA-01 JA-03 uraian 3 ("Mengendalikan proses proposal, peninjauan pricing, negosiasi dan persetujuan sebelum penawaran") dan uraian 7 ("Melakukan peninjauan aktivitas tim komersial ..."); OPS-SOP-01 dan OPS-PRC-01 untuk penyerahan paket oleh VP Commercial.
2. Sumber (Stage 9) menyebut Sales yang melakukan handover; dokumen Operation menyebut VP Commercial yang menyerahkan paket G1. Keduanya dipertahankan: Business Development menyusun paket dan menyelenggarakan handover meeting, VP Commercial menyerahkan paket atas nama Commercial. Open item 9.
3. Respons "WhatsApp" dan "Email" dibaca sebagai respons Business Development kepada customer; "Internal Request" dibaca sebagai permintaan internal kepada Business Development. Titik awal hitung tidak disebut sumber.
4. Pemetaan Sales Stage ke tahap proses (butir 4.7) adalah tafsir penyusun; deck hanya mendaftar enam status dan menandai "Bid (Proposal/Quote submitted)". Arti "Future Nurture" (lead yang belum layak sekarang tetapi akan ditindaklanjuti nanti) adalah penjelasan umum penyusun, tidak ada di deck.
5. Definisi BANT (Budget, Authority, Need, Timeline), CRM (Customer Relationship Management), NDA, Purchase Order, Forecast, Customer, Lead, Opportunity, dan Delivery adalah penjelasan penyusun atau kutipan dari dokumen lain, bukan kalimat tim. Definisi MEDDICC dan SPIN Selling dari deck slide 12 dan 13.
6. Diagram bagian 7 diturunkan dari teks sumber dan dokumen Operation. Cabang "Tidak" pada qualification dan pada gerbang closing berhenti di butir yang melarang langkah berikutnya; sumber tidak menggambarkan kegagalan. Loop eskalasi diskon kembali ke negosiasi adalah tafsir (hasil keputusan COO tidak digambar; lihat butir 6.6).
7. Judul klausul ISO di bagian 11 berasal dari pengetahuan standar penyusun, tidak dicocokkan dengan teks standar (UNMEASURED), dan semuanya di bawah satu label "(USULAN, perlu konfirmasi konsultan)". Klausul 9.1.2 (kepuasan pelanggan) sengaja tidak dimasukkan karena dokumen ini tidak punya proses pengukuran kepuasan.
8. Rekaman di bagian 11: lokasi dan retensi tidak ada di sumber, ditulis "Belum ditetapkan". Hanya CRM yang disebut sumber sebagai tempat catatan.
9. Daftar dokumen COM-SOP-02, COM-FRM-01, dan COM-FRM-02 di Dokumen terkait diambil dari judul di config/worklist.json; isinya belum ada saat saya menulis. Kaitannya dengan SOP ini adalah USULAN 8.

## USULAN

Sembilan butir keputusan; dokumen memuat 14 label "(USULAN" (12 persis "(USULAN)", ditambah satu pada butir 4.13 dan satu pada label klausul ISO).

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Pemetaan tahap proses ke Sales Stage CRM (Leads, Qualified, Opportunity, Bid, Win atau Lost, Future Nurture) | Butir 4.7 | owner |
| 2 | Wewenang harga: VP Commercial merekomendasikan harga dan diskon, COO menyetujui dan menetapkan margin final, setiap diskon butuh persetujuan COO sampai ambang ditetapkan. Margin final = owner (catatan worklist) | Butir 4.10, langkah 6.4.4 sampai 6.4.6, 6.6.3 sampai 6.6.5 | owner |
| 3 | Data customer, kontrak, dan harga = RESTRICTED (Internal) untuk Commercial (SNX-ISMS-PRO-01 belum mencakup Commercial) | Butir 4.13 | Fani |
| 4 | Titik waktu keterlibatan Legal: review draf kontrak sebelum tanda tangan, NDA sebelum informasi RESTRICTED dibagikan, dukungan negosiasi kontrak (catatan worklist "tambah langkah Legal") | Butir 4.14, langkah 6.3.1 dan 6.3.2, 6.6.6, 6.7.1 dan 6.7.2 | Legal |
| 5 | Project kick-off dimulai sesudah Service Delivery Manager menerima paket handover, dan tidak lagi masuk syarat closing | Butir 4.15 | owner |
| 6 | Penetapan pelaku yang tidak disebut sumber (VP Commercial: review internal, tinjauan mingguan dan bulanan, penerima laporan, penyerahan paket, penyimpan rekaman persetujuan; Legal & Compliance: penyimpan NDA dan hasil review kontrak; Business Development: perbaikan paket ditolak) | Butir 4.19, bagian 8, bagian 11 | owner |
| 7 | Pemetaan peran: Sales dan Sales Executive ke Business Development; Presales ke Manager of Product Tech; Delivery ke Service Delivery Manager (jabatan usulan tanpa pemegang) | Tabel peran bagian 5 | owner (dengan Fani untuk Service Delivery Manager dan Manager of Product Tech) |
| 8 | Dokumen pasangan COM-SOP-02 (rincian proposal, quotation, harga), COM-FRM-01 (rekaman Business Requirement), COM-FRM-02 (rekaman paket handover); diubah W9: COM-FRM-01 ditulis sebagai rekaman yang menyalin atau merujuk Business Requirement di CRM (USULAN); COM-FRM-02 ditulis sebagai rekaman paket handover tanpa USULAN; kata "calon" dihapus (R1 butir 9, R2) | Dokumen terkait bagian 11, scope | owner |
| 9 | Daftar klausul ISO 9001:2015 (5.3, 7.5.3, 8.2.1, 8.2.2, 8.2.3) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.14, 5.34), label "(USULAN, perlu konfirmasi konsultan)" | Bagian 11, Acuan standar | owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Ambang diskon, batas margin minimum, dan tenggat approval harga tidak ada di sumber. Penetapan COO sebagai penyetuju (USULAN 2) belum diputus tertulis, dan Authority Matrix belum bernomor | owner |
| 2 | Siklus tinjau: sumber 6 bulan, dokumen ini YEARLY (defaults). Konfirmasi bahwa VP Commercial menerima YEARLY | owner |
| 3 | Kriteria qualification: Technical Fit (SOP) atau Project Scope (deck); BANT atau MEDDICC (SOP) atau MEDDICC saja (deck). Skala Opportunity Score, arti "strategis" pada negosiasi dan eskalasi, dan "pihak yang berwenang" untuk penyimpangan prosedur tidak didefinisikan | owner |
| 4 | Status lead yang tidak lolos qualification, dan pencatatan Lost untuk opportunity yang gagal sesudah proposal: sumber tidak mengatur (Future Nurture atau Lost). Bagian 9 hanya melarang proposal, dan langkah 6.7.6 hanya mencatat Win (butir 4.7 tetap menyebut Lost sebagai status saat hasil pasti). Langkah atau baris bagian 9 untuk Lost menunggu keputusan | owner |
| 5 | Penerima dan format laporan harian, mingguan, dan bulanan; peminta laporan harian ("jika diminta"); pelaku tinjauan pipeline dan forecast | owner |
| 6 | Arti "Internal Request" (4 jam kerja), titik awal hitung respons email dan WhatsApp, dan apakah respons internal lewat tiket GLPI (generalist). Deck juga menyebut alat "Pre-sales Request" dan "Proposal & Quotation Template" tanpa bentuk, nomor, atau kanal | owner |
| 7 | Siapa memberi persetujuan internal (syarat closing) dan siapa menandatangani kontrak atas nama SINUX; Authority Matrix belum bernomor | Samuel |
| 8 | Syarat closing: apakah kick-off tetap masuk (versi sumber) atau sesudah handover (USULAN 5) | owner |
| 9 | Siapa yang menyerahkan paket handover (Business Development di sumber, VP Commercial di dokumen Operation) dan selisih isi enam butir paket handover dengan Checklist G1 di SNX-OPS-FRM-01 (SLA tertulis ada di G1, Customer Background, Timeline, dan Risks ada di sumber) | Fani |
| 10 | Nama produk CRM dan lokasi serta retensi rekaman: berkas proposal dan quotation, PO, kontrak yang ditandatangani, persetujuan harga, paket handover, laporan | owner dan Legal |
| 11 | Rentang ukuran perusahaan di deck (ICP) tumpang tindih dan berlubang, dan ICP belum berdokumen terkendali; definisi ICP hanya merujuk deck | owner |
| 12 | Langkah Business Development di SNX-FAT-SOP-01 (kirim Google Form Data Subskripsi Klien saat PKS ditandatangani) belum ada di SOP ini. Perlu diputus apakah masuk di butir 6.7 | FAT |
| 13 | Account management sesudah implementasi (Stage 10 sumber) belum punya prosedur; masuk SOP terpisah atau perluasan scope | owner |
| 14 | Kaitan dengan SNX-COM-SOP-02, SNX-COM-FRM-01, SNX-COM-FRM-02, dan SNX-LEG-SOP-02 dicek ulang sesudah dokumen itu final; tumpang tindih wewenang harga di butir 4.10 dengan COM-SOP-02 perlu dicegah. Pengajuan review kontrak merujuk SNX-LEG-SOP-02 butir 6.1, yang masih Draft; diubah W9: keterangan tiga dokumen itu di bagian 11 sudah memakai isi nyata dokumen tujuan (R1 butir 9, R2); cek ulang final tetap berlaku | owner dan Legal |
| 15 | Target KPI Commercial ada di berkas lain (KPI individu, belum bernomor) dan belum dirujuk ke KPI Matrix; KPI sumber 9 butir lawan 8 butir di deck | owner |
| 16 | Klasifikasi RESTRICTED (Internal) untuk data customer Commercial (USULAN 3): SNX-ISMS-PRO-01 menyatakan Commercial belum tercakup | Fani |
| 17 | SOP sumber tidak punya approver, riwayat revisi, atau klasifikasi, dan sumber menulis "Version 1.0" berlaku 28 Juli 2026. Dokumen ini Draft rev 00; status berlaku sumber lama perlu dihentikan sesudah dokumen ini disahkan | owner |
| 18 | Finance dan Brand & Marketing tercantum di tabel peran dari tabel kolaborasi sumber tanpa langkah prosedur sendiri; Procurement dan Management tidak dipakai. Konfirmasi bahwa itu cukup | owner |

## 5. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya enam tanda; lima sudah saya perbaiki dan satu saya biarkan:
   - Sel tanggung jawab Business Development di tabel peran menyalin urutan langkah bagian 6 dalam satu kalimat panjang. Diperbaiki: sel itu sekarang satu kalimat yang menunjuk bagian 6 dan butir 4.3.
   - Tiga langkah berurutan di butir 6.7 dibuka "Pastikan". Diperbaiki: dua langkah memakai "Periksa", satu tetap "Pastikan" karena sumber memakai kata itu untuk dokumen lengkap dan tanda tangan.
   - "Ketiga persetujuan" di langkah 6.4.7 tidak jelas jumlahnya bila tidak ada diskon. Diperbaiki: "review internal dan persetujuan di butir 4.9".
   - Istilah berganti untuk hal yang sama: approval dan persetujuan, Risks dan Risiko, "bagian 6.5" dan "butir 6.5", status "Opportunity" dan opportunity sebagai peluang. Diperbaiki: satu istilah per hal (persetujuan; Risks; butir untuk sub-proses; "status Opportunity" untuk nilai CRM). Definisi Lead dan Qualification sempat saling merujuk, sudah dipisah.
   - Definisi "Opportunity" semula berbunyi mulai dari qualification, bertabrakan dengan status Opportunity sesudah discovery. Diperbaiki: tanpa titik mulai.
   - Dibiarkan: hampir semua butir kebijakan dibuka dengan "Business Development" dan beberapa butir memuat deret tiga kata ("profesional, jelas, dan berorientasi pada solusi"; "akurat, transparan, dan dapat dipertanggungjawabkan"; "kebutuhan, tantangan, dan tujuan bisnis customer"). Deret itu kalimat tim di sumber dan T1 mempertahankan suara tim; pelaku tunggal per butir mengikuti RUNBOOK 6a.1. Kolom Output memakai pola "X di CRM" karena itu nama rekaman.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa terhadap tabel Fakta kunci dan pemetaan peran:
   - Angka: 24 jam, 1 hari kerja, 2 jam kerja, 4 jam kerja, lima kriteria, enam butir handover, delapan kondisi eskalasi berasal dari sumber. "Setiap tahun" dari defaults (sumber menulis 6 bulan). Tidak ada persentase, nilai, atau ambang buatan saya.
   - Nama: Laras Rasmawati, Amirull Yusuf Zulkarnain, dan Samuel Kristanto Utomo hanya di blok approval (defaults). Tidak ada nama orang lain. Nama peran dari HR-ORG-01 (Service Delivery Manager adalah jabatan usulan tanpa pemegang).
   - Tanggal: nol. Satu penanda waktu, "Commercial Onboarding Jul 2026", adalah judul berkas deck.
   - Tanpa sumber tertulis tetapi ada di dokumen: definisi umum BANT, CRM, NDA, Purchase Order, Forecast, Customer, Lead, Opportunity; arti Future Nurture dan pemetaan Sales Stage (USULAN 1); judul klausul ISO (USULAN 9); tafsir peran (USULAN 7); semua penunjukan pelaku di butir 4.19 (USULAN 6); wewenang harga dan margin (USULAN 2); klasifikasi RESTRICTED untuk Commercial (USULAN 3); titik waktu Legal (USULAN 4); penempatan kick-off (USULAN 5); rujukan ke COM-SOP-02, COM-FRM-01, dan COM-FRM-02 (USULAN 8); dokumen "KPI Matrix" yang disebut HR-ORG-01 tanpa nomor.
   - Rujukan ke dokumen lain (SNX-OPS-SOP-01 butir 4.1, SNX-ISMS-PRO-01 butir 4.3 dan 4.10, SNX-LEG-SOP-02 butir 4.1, 4.3, dan 6.1, SNX-OPS-FRM-01 checklist G1) dicocokkan dengan spec di repo pada saat saya menulis; spec Legal masih Draft dan bisa berubah.

## Sweep

Putaran sweep dari orkestrator (berkas /tmp/claude-0/prompts/COM-SOP-01.sweep.txt), batas tulis specs/COM-SOP-01.json dan notes/COM-SOP-01.md. Temuan pemeriksa dibaca di qa/COM-SOP-01.verify.json (verdict PASS, nol blocking). 11 entri spec diubah; fakta, angka, nama, dan struktur lain tetap. Alasan proses yang dicabut dari badan dokumen dicatat di bawah, bukan di dokumen. Uji sesudah sweep: render_sop.py lalu lint_doc.py sop memberi "pass": true, "fails": [], satu warn "12 butir (USULAN) menunggu ACC"; validate.py: "All validations PASSED!"; blankscan.py: "ok 20 COM-SOP-01.docx []".

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Butir 4.14 (frasa "SOP sumber") | "...Titik waktu keterlibatan Legal & Compliance ini berstatus (USULAN) karena SOP sumber hanya menyebut lingkup kolaborasinya." | "...Titik waktu keterlibatan ini berstatus (USULAN)." |
| 2 | Butir 4.15 (frasa "SOP sumber") | "...(SNX-OPS-SOP-01 butir 4.1); penempatan kick-off sesudah handover berstatus (USULAN), karena SOP sumber memasukkan kick-off atau implementasi ke dalam syarat closing." | "...(SNX-OPS-SOP-01 butir 4.1). Penempatan kick-off sesudah handover berstatus (USULAN)." |
| 3 | Butir 4.19 (frasa "SOP sumber") | "Penetapan pelaku berikut berstatus (USULAN) karena SOP sumber tidak menyebut pelakunya: ..." | "Penetapan pelaku berikut berstatus (USULAN): ..." (isi daftar pelaku tidak berubah) |
| 4 | Tabel peran, Manager of Product Tech | "...Dipetakan dari Presales di SOP sumber (USULAN)." | "...Jabatan ini memegang peran Presales (USULAN)." |
| 5 | Tabel peran, Service Delivery Manager | "...Dipetakan dari Delivery di SOP sumber (USULAN); jabatan usulan tanpa pemegang menurut SNX-HR-ORG-01." | "...Jabatan ini menerima handover di Delivery (USULAN) dan merupakan jabatan usulan tanpa pemegang menurut SNX-HR-ORG-01." |
| 6 | Tabel peran, Business Development | "...Dipetakan dari Sales dan Sales Executive di SOP sumber (USULAN)." | "...Jabatan ini memegang peran Sales dan Sales Executive (USULAN)." |
| 7 | Butir 6.7 langkah 6 (status Lost) | "Perbarui Closing Status dan Sales Stage (Win atau Lost) sesuai butir 4.15." Output "Closing Status dan Sales Stage terbarui di CRM" | "Ubah Closing Status dan Sales Stage menjadi Win sesuai butir 4.15." Output "Closing Status dan Sales Stage Win di CRM". Pada titik itu PO sudah diterima dan kontrak ditandatangani, jadi hasilnya Win. Tempat pencatatan Lost tidak dikarang: open item 4 |
| 8 | Butir 6.3 langkah 7 (dua tindakan) | "Tentukan agenda demo yang menjawab kebutuhan customer, dan jelaskan business context kepada customer." (satu langkah, output "Agenda demo") | Dua langkah: 7 "Tentukan agenda demo yang menjawab kebutuhan customer." (output "Agenda demo") dan 8 "Jelaskan business context kepada customer pada demo." (output "Meeting Notes demo di CRM"). Langkah sesudahnya bergeser menjadi 9 dan 10; tidak ada rujukan langkah 6.3 lain di dokumen |
| 9 | Butir 6.6 langkah 1 (dua tindakan) dan butir 4.11 | Langkah: "Negosiasikan dengan customer hanya dalam batas harga dan diskon yang disetujui, dan jaga value solusi." Butir 4.11 akhir: "Business Development bernegosiasi hanya dalam batas harga dan diskon yang sudah disetujui." | Langkah: "Negosiasikan dengan customer hanya dalam batas harga dan diskon yang disetujui (butir 4.11)." Butir 4.11 akhir: "Dalam negosiasi, Business Development memahami concern customer, menjaga value solusi, dan bernegosiasi hanya dalam batas harga dan diskon yang sudah disetujui." Isi "menjaga value solusi" tetap ada (Stage 7 sumber), dipindah ke aturan |
| 10 | Label klausul ISO (bagian 11, Acuan standar) | "Klausul di bawah berstatus (USULAN, dikonfirmasi konsultan)." | "Klausul di bawah berstatus (USULAN, perlu konfirmasi konsultan)." Label yang sama di notes (asumsi 7 dan USULAN 9) ikut diganti |
| 11 | Alasan yang dicabut dari badan dokumen (disimpan di sini) | Alasan USULAN 4: Sales SOP hanya menyebut lingkup kolaborasi Legal (NDA preparation/review, Contract review, Commercial terms & conditions, Contract negotiation support, Legal compliance), tanpa titik waktu. Alasan USULAN 5: Sales SOP Stage 8 memasukkan "Project Kick-off atau implementasi telah dimulai" ke syarat closing, bertentangan dengan Stage 9. Alasan USULAN 6: Sales SOP tidak menyebut pelaku review internal, tinjauan, penerima laporan, dan penyerah paket. Alasan USULAN 7: Sales SOP memakai Sales, Sales Executive, Presales, dan Delivery, sedangkan SNX-HR-ORG-01 tidak punya jabatan itu | Badan dokumen menyatakan status (USULAN) tanpa alasan proses |

Catatan: kata "sumber" tersisa di badan dokumen hanya sebagai kata benda biasa (CRM sebagai sumber data tunggal; sumber dan status lead; sumber nama jabatan dan sumber tingkat RESTRICTED di Dokumen terkait). Frasa "judul menurut daftar dokumen SINUX, isi belum dikonfirmasi" di tiga baris Dokumen terkait (COM-SOP-02, COM-FRM-01, COM-FRM-02) tidak diubah karena di luar butir sweep; bila orkestrator menganggapnya frasa proses, tulis ulang pada putaran berikutnya.

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| 8 Bagian 9, Service Delivery Manager menolak paket handover | "(SNX-OPS-SOP-01 butir 4.1)" | "(SNX-OPS-SOP-01 butir 4.1 dan bagian 9)" |
| 9 Bagian 11, SNX-COM-SOP-02 | "judul menurut daftar dokumen SINUX, isi belum dikonfirmasi." | "mengatur penyusunan proposal, review scope, validasi harga dan margin, pengecualian komersial, review internal, serta persetujuan harga dan diskon sebelum penawaran dikirim." (USULAN pada rujukan rincian tetap) |
| 9 Bagian 11, SNX-COM-FRM-01 | "judul menurut daftar dokumen SINUX, isi belum dikonfirmasi. Calon rekaman Business Requirement di butir 6.3 (USULAN)." | "mencatat hasil review Commercial atas satu order customer sebelum order diterima. Rekaman Business Requirement di butir 6.3 (USULAN)." |
| 9 Bagian 11, SNX-COM-FRM-02 | "judul menurut daftar dokumen SINUX, isi belum dikonfirmasi. Calon rekaman paket handover di butir 6.8 (USULAN)." | "mencatat isi handover proyek dari Commercial ke tim pelaksana sesudah closing. Rekaman paket handover di butir 6.8 (USULAN)." |
| R2 1a Bagian 11, SNX-COM-FRM-02 | "Rekaman paket handover di butir 6.8 (USULAN)." | "Rekaman paket handover di butir 6.8." |
| R2 2 Bagian 11, SNX-COM-FRM-01 | "Rekaman Business Requirement di butir 6.3 (USULAN)." | "Formulir ini menyalin atau merujuk Business Requirement di CRM, keluaran butir 6.3 (USULAN)." |

Label USULAN pada hubungan ke butir 6.3 tetap karena SNX-COM-FRM-01 sebagai bentuk Business Requirement masih usulan. R2: label USULAN pada hubungan ke butir 6.8 dihapus karena SNX-COM-FRM-02 adalah rekaman serah terima.

Open item ditutup atau diubah: nihil (hanya rujukan diperbaiki).

R2 butir 3: baris USULAN dan Open items yang ditutup atau diubah W9 diberi keterangan "ditutup W9" atau "diubah W9" di barisnya sendiri.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
- Definisi Sales Stage, kalimat penunjuk dihapus: "Pemetaan tahap ke status ada di butir 4.7." Isi pemetaan tetap di butir 4.7 (USULAN).
- Definisi Paket handover: "isi minimalnya di butir 4.16" diganti isi minimalnya (Customer Background, Scope, Timeline, Risks, Commitment, dan Contact Person).
- Tabel peran Legal & Compliance: "Titik keterlibatannya di butir 4.14." diganti isi butir 4.14 beserta label (USULAN).
- Tabel peran Service Delivery Manager, catatan pemetaan dipindah ke sini: "dan merupakan jabatan usulan tanpa pemegang menurut SNX-HR-ORG-01." Fakta jabatan usulan tanpa pemegang tetap tertulis di Dokumen terkait baris SNX-HR-ORG-01 (butir K-10).
### W10 selisih angka
nihil
### W10 catatan
- Pihak luar: "customer" (satu-satunya sebutan di dokumen; sama dengan SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01).
- Nomor butir dan arti butir yang dirujuk form Commercial (4.3, 4.11, 4.13, 4.16, 4.17, 4.19, 6.3, bagian 8 dan 9, definisi Customer) tidak berubah.
- Butir 4.10: label (USULAN) dipindah ke akhir butir; cakupannya tetap pembagian wewenang harga.
### W10 audit pointer
- .definitions[14][1]: lengkap (enam unsur isi minimal paket handover dari butir 4.16: Customer Background, Scope, Timeline, Risks, Commitment, Contact Person; definisi hanya merujuk isi minimal, syarat kelengkapan dokumen closing dan waktu handover meeting tetap di butir 4.16)
- .definitions[18][1]: pointer murni dibuang, isi tidak dinyatakan ulang (pemetaan berlabel USULAN tetap di butir 4.7)
- .roles[5][1]: lengkap (review draf kontrak sebelum ditandatangani, NDA disiapkan atau direview jika diperlukan sebelum informasi RESTRICTED dibagikan, label USULAN titik waktu ikut)
### W10 perbaikan cakupan label (worker, setelah pemeriksa buta)
- Butir 4.10: label dipindah dari kalimat penutup "Pembagian wewenang harga ini berstatus (USULAN)." ke akhir kalimat pertama, sehingga cakupannya sama dengan bed1bb6 ("Wewenang harga berikut berstatus (USULAN): ..." hanya mencakup rekomendasi VP Commercial dan persetujuan serta margin final oleh COO). Aturan sementara "setiap diskon memerlukan persetujuan COO" tetap tanpa label, seperti bed1bb6. Dasar: catatan nonblocking pemeriksa COM-SOP-02 butir 4.7 (pola sama).
