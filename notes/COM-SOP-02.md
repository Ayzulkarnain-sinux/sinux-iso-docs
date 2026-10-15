# Catatan penyusun COM-SOP-02: Proposal, Quotation & Pricing Control

Status: DRAFTED (spec + notes ada). Spec: specs/COM-SOP-02.json. Mode sop, aksi T2, wave W4, nomor SNX-COM-SOP-02 (nomor SNX lama dipertahankan), department Commercial, classification INTERNAL (worklist), audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Laras Rasmawati / VP Commercial", reviewed "Amirull Yusuf Zulkarnain / Direktur", approved "Samuel Kristanto Utomo / President Director". process_owner "VP Commercial": medan "Document Owner: VP of Commercial" ada di Sales SOP, jadi bukan USULAN; nama peran mengikuti SNX-HR-ORG-01 (JA-03). Catatan worklist: kosong.

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-SOP-02.json /tmp/pen-COM-SOP-02/COM-SOP-02.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-COM-SOP-02/COM-SOP-02.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "17 butir (USULAN) menunggu ACC" (nol warn PIC SLA; angka sesudah sweep, sebelumnya 11).
- Validator OOXML skill docx (`/mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- Diagram bagian 7 (20 simpul, rankdir TB, enam keputusan) dirender dan gambarnya dilihat: semua label terbaca, semua panah sesuai daftar edges. Halaman PDF hasil soffice tidak dibuat (UNMEASURED: tata letak halaman docx tidak diperiksa mata).
- Lint dan validator hanya membuktikan format dan larangan pola. Kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah. Kecocokan kode SNX di badan dengan tabel Dokumen terkait diperiksa dengan skrip kecil: nol kode kurang.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 1. SALES STANDARD OPERATING PROCEDURE.pdf (2.666.844 byte, 19 halaman) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (lapisan teks) dan download_file_content; halaman 10 dirender 90 dpi dengan pdftoppm dan dilihat. Lapisan teks bercampur antar kartu, jadi susunan dicocokkan dengan transkripsi di context/audit/iso-sinux-supdocs-commercial-2026-10-14.md. Halaman lain tidak dibuka sebagai gambar (UNMEASURED) |
| 2. SINUX_Job_Analysis_2026.docx (51.426 byte, 15 jabatan) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (teks utuh) dan download_file_content; paket docx diperiksa dengan python3 -I: 17 tabel, nol perubahan terlacak, nol komentar, nol gambar |
| Kriteria penerimaan | config/checklist.json baris 49 (checked: false) | checklist tidak diukur ulang | Description: "Mengatur penyusunan proposal, validasi harga dan margin, review scope, pengecualian komersial, serta otorisasi sebelum penawaran dikirim." Pemetaan di bawah |
| Pendukung repo (bukan Drive) | config/defaults.json v21 (data_conflicts), specs/HR-ORG-01.json (daftar jabatan, matriks peran, K-02, K-10, K-13), specs/COM-SOP-01.json (butir 4.6, 4.8 sampai 4.11, 4.13, 6.4), specs/FAT-SOP-01.json (butir 4.5, 4.8), specs/LEG-SOP-02.json (butir 4.3, 6.1), specs/ISMS-PRO-01.json (butir 4.10, 4.19), notes/COM-SOP-01.md, context/audit (bagian COM-Sales-SOP dan HR-JA-001) | repo kerja | Dibaca sebagai DATA. Spec FAT dan LEG masih Draft dan ditulis lane lain; kutipan darinya bisa basi |

Kalimat perintah kepada AI di kedua sumber: nihil. Kalimat kewajiban untuk karyawan ("Sales wajib ...") adalah isi SOP, bukan instruksi untuk saya.

Pemetaan kriteria baris 49 ke dokumen:

| Unsur Description | Di dokumen |
|---|---|
| penyusunan proposal | Butir 4.1, 4.2, 4.12; prosedur 6.1 |
| validasi harga dan margin | Butir 4.6, 4.7; prosedur 6.3; peran Finance dan Accounting & Tax |
| review scope | Butir 4.4, 4.5; prosedur 6.2; Catatan review scope |
| pengecualian komersial | Definisi, butir 4.9 dan 4.10, 4.11; prosedur 6.4; bagian 9 |
| otorisasi sebelum penawaran dikirim | Butir 4.7, 4.8; prosedur 6.5; Catatan persetujuan penawaran; SLA bagian 8 |

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Sebelum penawaran dikirim ke customer ada tiga pemeriksaan berurutan: review internal, approval harga, approval diskon (jika ada). Proposal hanya dibuat setelah Discovery selesai. Dasar butir 4.1, 4.8, prosedur 6.5 | "Proposal hanya dibuat setelah Discovery selesai." dan "Sebelum dikirim ke customer:" lalu tiga kotak berpanah satu arah: "Review internal." "Approval harga." "Approval diskon (jika ada)." (urutan dari render halaman 10) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Sales dilarang mengubah pricing sendiri, memberi diskon tanpa persetujuan, menawarkan fitur yang belum tersedia, dan menjanjikan timeline tanpa konfirmasi Delivery. Dasar butir 4.3 dan 4.4 | "Sales tidak diperbolehkan:" "Mengubah pricing sendiri." "Memberikan diskon tanpa persetujuan." "Menawarkan fitur yang belum tersedia." "Menjanjikan timeline tanpa konfirmasi Delivery." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| VP Commercial mengendalikan proses sebelum penawaran, mengevaluasi margin dan diskon, merekomendasikan harga dan diskon, dan boleh menolak pengajuan yang belum lengkap. Dasar butir 4.7, 4.8, langkah 6.4.3 dan 6.5.1 | "Mengevaluasi margin, diskon, perubahan scope dan potensi komitmen di luar kontrak." (JA-03 uraian 6); "Merekomendasikan harga/diskon untuk persetujuan" dan "Menolak submission komersial yang belum lengkap" (JA-03 wewenang 1 dan 3) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

Fakta penting lain:

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi |
|---|---|---|---|
| 1 | Proposal wajib memuat tujuh bagian (butir 4.2) | "Proposal wajib mencakup:" "Scope of Work" "Proposed Solution" "Deliverables" "Timeline" "Commercial Proposal" "Assumptions" "Exclusions" | Sales SOP Stage 6, hal. 10 |
| 2 | Proposal dan quotation dicatat di CRM, batas 24 jam (butir 4.14, bagian 8) | "Seluruh aktivitas penjualan wajib dicatat di CRM." dan "CRM harus diperbarui maksimal 24 jam setelah aktivitas dilakukan." Daftar wajib memuat "Proposal" dan "Quotation" | Sales SOP 06 CRM Policy, hal. 13 |
| 3 | Eskalasi ke VP Commercial untuk diskon di luar kewenangan, konflik kontrak, isu legal (bagian 9) | "Segera eskalasikan kepada VP Commercial apabila terjadi:" "Permintaan diskon di luar kewenangan." "Konflik kontrak." "Isu legal." | Sales SOP 14 Escalation Matrix, hal. 17 |
| 4 | Larangan negosiasi harga di luar kewenangan | "Tidak melakukan pricing negotiation di luar kewenangan." "Tidak melakukan overpromise." | Sales SOP 13 Code of Conduct, hal. 17 |
| 5 | Penyimpangan prosedur (bagian 9) | "Penyimpangan terhadap prosedur harus mendapatkan persetujuan dari VP Commercial atau pihak yang berwenang." | Sales SOP 16 SOP Compliance, hal. 18 |
| 6 | Konfirmasi timeline dan scope oleh Delivery; dukungan Finance, Legal, Presales (peran dan butir 4.4, 4.5, 4.11) | Delivery: "Timeline confirmation" "Scope clarification"; Finance: "Commercial terms"; Legal: "Contract review" "Commercial terms & conditions"; Presales: "Solution design" | Sales SOP 09 Internal Collaboration, hal. 15 |
| 7 | Pemilik dokumen sumber = VP of Commercial (process_owner) | "Commercial Department Document Owner: VP of Commercial" | Sampul Sales SOP |
| 8 | Business Development menegosiasikan dalam batas penawaran yang disetujui dan mengeskalasi diskon dan scope yang belum disetujui (peran BD) | "Menegosiasikan dalam batas penawaran disetujui" "Mengeskalasi diskon/scope yang belum disetujui" | Job Analysis JA-07 wewenang 2 dan 3 |
| 9 | Manager of Product Tech menyusun desain, BOM/BOQ, sizing, asumsi teknis proposal dan mengeskalasi proposal yang tidak feasible | "Menyusun desain tingkat tinggi, BOM/BOQ, sizing dan asumsi teknis proposal." dan "Mengeskalasi proposal yang tidak feasible" | Job Analysis JA-05 uraian 3, wewenang 3 |
| 10 | Finance menyediakan data margin dan COGS (langkah 6.3.2) | "Menyediakan data margin/COGS yang relevan untuk verifikasi komersial bersama Accounting." | Job Analysis JA-10 uraian 6 |
| 11 | Accounting & Tax memverifikasi klasifikasi COGS dan margin, dan boleh meminta koreksi (langkah 6.3.4, bagian 9) | "Memverifikasi klasifikasi COGS, biaya proyek dan margin yang dilaporkan." dan "Meminta koreksi jurnal/dokumen" | Job Analysis JA-11 uraian 5, wewenang 1 |
| 12 | Legal & Compliance memegang template, klausul standar, dan daftar deviasi; memberi clearance atau rekomendasi dan meminta revisi klausul berisiko | "Memelihara template kontrak, klausul standar dan daftar deviasi hukum." "Memberikan legal clearance/rekomendasi" "Meminta revisi klausul berisiko" | Job Analysis JA-08 uraian 2, wewenang 1 dan 2 |
| 13 | Hak tanda tangan dan otorisasi keuangan tidak otomatis melekat pada jabatan; keputusan mengikuti delegasi tertulis (butir 4.7, bagian 9) | "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." dan "tetap mengikuti delegasi dan persetujuan tertulis yang berlaku" | Job Analysis bagian 2 dan batasan umum JA-01 sampai JA-15 |
| 14 | TOP di atas standar disetujui Direktur Utama secara tertulis (butir 4.10, langkah 6.4.9) | "Direktur Utama menyetujui TOP di atas 14 hari secara tertulis sebelum PKS atau PO disepakati." | specs/FAT-SOP-01.json butir 4.8 (repo, Draft) |
| 15 | Legal dilibatkan sebelum komitmen tertulis kepada pihak luar (butir 4.11) | "Pemohon melibatkan Legal sejak negosiasi komersial, sebelum ada komitmen tertulis kepada pihak luar." | specs/LEG-SOP-02.json butir 4.3 (repo, Draft) |
| 16 | Dokumen teknis untuk customer pemerintah tanpa harga (butir 4.12) | "Dokumen teknis untuk pelanggan pemerintah tidak memuat harga, diskon, tier, maupun roadmap komersial." | specs/ISMS-PRO-01.json butir 4.19 (repo, Draft) |
| 17 | Wewenang harga yang sudah dipakai SOP penjualan (butir 4.7 dibuat sama) | "VP Commercial merekomendasikan harga dan diskon, COO menyetujuinya dan menetapkan margin final." | specs/COM-SOP-01.json butir 4.10 (repo, USULAN) |

## 2. Keputusan data dan pemetaan peran

- Sebutan: Direktur (COO) hanya di tabel Definisi (penyebutan pertama di badan), sesudahnya COO. Bagian 1 dan 2 tidak menyebut COO. Samuel di badan = "Direktur Utama"; namanya hanya di blok Approved By. Nama Laras dan Amirull hanya di blok approval.
- Tiket: Zammad untuk Ops, GLPI untuk generalist. Dokumen tidak menyebut tiket karena sumber tidak mengaturnya dan kanal pengajuan ke Legal sudah ada di SNX-LEG-SOP-02 butir 6.1. Kanal permintaan ke Finance, Accounting & Tax, Manager of Product Tech, dan Service Delivery Manager belum diputus: open item 9.
- Vault: tidak relevan, tidak disebut.
- PPN: satu rumusan hanya di SNX-FAT-SOP-01 butir 4.5 (12%, USULAN di dokumen itu). Dokumen ini tidak menyebut tarif; Accounting & Tax memverifikasi perlakuan PPN dengan merujuk butir itu.
- Klasifikasi dokumen INTERNAL (worklist). Harga dan margin di dalamnya RESTRICTED (Internal) sebagai USULAN 5.
- Istilah: "customer" (bukan pelanggan atau klien), "persetujuan" untuk approval, "review" untuk semua pemeriksaan internal dan Legal, "penawaran" = proposal dan quotation sebagai satu paket. "Business Development" dipakai untuk pelaku yang di Sales SOP disebut Sales.

Pemetaan peran sumber ke nama peran di bagian 5 (basis: specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Sales | Business Development | JA-07; sama dengan COM-SOP-01. Tafsir, di bawah USULAN 7 |
| VP of Commercial, VP Commercial | VP Commercial | JA-03 |
| Presales | Manager of Product Tech | HR-ORG-01 tidak punya jabatan Presales. JA-05 memuat BOM/BOQ, sizing, asumsi teknis proposal, dukungan demo. USULAN 7 |
| Delivery | Service Delivery Manager | OPS-SOP-01 dan HR-ORG-01 K-10; jabatan usulan tanpa pemegang. USULAN 7 |
| Finance | Finance | JA-10. Finance Lead dan Finance Staff di dokumen FAT belum dipetakan (K-13), jadi tidak dipakai |
| Accounting | Accounting & Tax | JA-11 |
| Legal | Legal & Compliance | JA-08 dan JA-09 memakai nama jabatan yang sama; Line Manager Legal dan Staff Legal di SNX-LEG-SOP-02 belum dipetakan (K-13) |
| Pihak yang menyetujui harga dan diskon (tidak disebut di sumber) | COO; Direktur Utama untuk TOP | USULAN 1 dan 2 |
| Commercial Manager (disebut catatan audit untuk deck onboarding, Pricing & Deal Approval) | tidak dipakai | Tidak ada jabatan itu di HR-ORG-01. Deck tidak dibaca di sesi ini (UNMEASURED), hanya catatan audit |
| Procurement, Management (Prinsip 5 Sales SOP) | tidak dipakai | Tanpa rincian tugas di proses proposal |

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah; grep fileId 19Hex8... dan 1m91Wrf...)

Sumber 1, Sales SOP (fileId 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Scope hanya "Business Development" padahal isi menyebut Sales Executive, Presales, VP Commercial | Diperbaiki: scope menyebut Business Development dan VP Commercial sebagai pelaku, fungsi lain lewat tabel peran |
| 2 | Tidak ada approver, riwayat revisi, nomor, klasifikasi | Teratasi oleh template dan defaults. "Version 1.0" dan "Effective Date 28th of July, 2026" tidak dibawa: dokumen ini Draft rev 00, tanggal efektif kosong (batas keras RUNBOOK 3) |
| 3 | Pricing dan diskon tanpa tingkat kewenangan, ambang, SLA approval, form | Sebagian diperbaiki: butir 4.7 dan 4.10 menetapkan pemutus (USULAN), selaras COM-SOP-01 butir 4.10; rekaman diberi nama (Lembar harga dan margin, Catatan persetujuan penawaran); SLA berbasis kejadian di bagian 8. Ambang diskon, batas margin minimum, tenggat tiap tahap tidak dikarang: open item 1 |
| 4 | Kriteria qualification SOP berbeda dari deck onboarding | Tidak relevan untuk dokumen ini; qualification dirujuk ke SNX-COM-SOP-01 butir 4.6 |
| 5 | Stage 6 sampai 10 tanpa label Objective, Stage 2 sampai 10 tanpa KPI | Tidak berdampak: prosedur 6.1 sampai 6.5 memakai satu pelaku per langkah. KPI di luar scope dokumen ini |
| 6 | Tidak ada tenggat follow-up, approval internal, atau handover | Bagian 8 memakai angka sumber hanya untuk CRM (24 jam) dan menunjuk batas respons ke SNX-COM-SOP-01 bagian 8. Review internal dan persetujuan diberi titik waktu (sebelum penawaran dikirim) tanpa angka durasi; baris "Belum ditetapkan" dibuat eksplisit: open item 1 |
| 7 | Delivery penerima handover tanpa individu | Handover di luar scope. Fungsi Delivery dalam konfirmasi timeline dan scope dipetakan ke Service Delivery Manager (USULAN 7) |
| 8 | KPI sumber tidak identik dengan deck dan xlsx | Di luar scope dokumen ini |
| 9 | Alat hanya "CRM" tanpa nama produk | Ditulis CRM tanpa nama produk: open item 17 |
| 10 | Larangan "fitur belum tersedia" dan "timeline tanpa konfirmasi" tanpa mekanisme verifikasi atau rekaman | Diperbaiki: butir 4.4 dan 4.5, langkah 6.2.5 (konfirmasi Service Delivery Manager), dan Catatan review scope sebagai rekaman (USULAN 6 dan 8) |
| 11 | Cacat tata letak halaman 3 | Tidak berdampak |

Sumber 2, Job Analysis (fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 12 | Frasa kompetensi janggal dari penggantian kata otomatis | Tidak ada frasa itu yang dibawa. Frasa sejenis ditemukan di JA-03 uraian 3: "pricing peninjauan". Dibaca sebagai peninjauan pricing; tidak dikutip di badan dokumen. Tidak tercatat di audit (temuan tambahan) |
| 13 | Atasan JA-08, JA-10, JA-11 "Management / Direktur", JA-14 tidak satu atasan | Tidak dipakai di badan. Dokumen ini tidak menyebut garis lapor; pembahasan Product Tech di open item 10 |
| 14 | Tidak ada jabatan Finance Lead dan Finance Staff | Dipakai "Finance" (JA-10) dan "Accounting & Tax" (JA-11) |
| 15 | Ejaan Samuel Kristianto vs Kristanto; sebutan CEO | Badan memakai "Direktur Utama"; blok Approved By memakai ejaan template (defaults) |
| 16 | Tidak ada batas nominal atau tingkat persetujuan keuangan atau kontrak per jabatan | Tidak dikarang. Butir 4.7 memakai penyetuju sementara (USULAN) dan merujuk Authority Matrix: open item 1 dan 2 |
| 17 | Pelaporan Manager of Product Tech tidak konsisten (JA-05 ke Direktur, JA-03 minta konfirmasi) | Tujuan eskalasi solusi tidak feasible ke VP Commercial berlabel USULAN (butir 4.5): open item 10 |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Lapisan teks PDF menggabungkan "Demo dilakukan bersama Presales apabila diperlukan." (objective Stage 5) dengan kalimat pembuka Stage 6. Render halaman 10 menunjukkan dua pernyataan terpisah di dua kartu | Kutipan "Proposal hanya dibuat setelah Discovery selesai." diambil dari render. Tidak berdampak pada isi; notes/COM-SOP-01.md mengutip bentuk gabungan |
| B | Sumber memuat "Approval harga" dan "Approval diskon (jika ada)" tanpa pelaku dan tanpa rekaman | Pelaku diberi lewat USULAN 1, rekaman Catatan persetujuan penawaran diberi pemilik VP Commercial (USULAN 6) |
| C | Sumber tidak membedakan permintaan diskon sebelum approval pertama dan permintaan di luar approval | Dipisah: diskon yang diajukan di penawaran awal masuk persetujuan biasa (langkah 6.5.4); perubahan sesudah persetujuan = pengecualian komersial (definisi, butir 4.9) |
| D | Rujukan "Authority Matrix" (HR-ORG-01, Job Analysis) dan "matriks DoA" (SNX-LEG-SOP-02) kemungkinan satu dokumen | Dokumen ini memakai Authority Matrix; open item 13 |

## 4. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Pemilihan urutan prosedur: review scope (6.2) sebelum validasi harga (6.3), karena BOM/BOQ dan scope yang dikonfirmasi menjadi dasar harga. Urutan review internal, approval harga, approval diskon tetap persis urutan sumber (6.5).
2. Definisi Assumptions, BOM/BOQ, COGS, Margin, Margin final, Exclusions, TOP, Review internal, Review scope adalah penjelasan penyusun, bukan kalimat tim. "sejak tanggal invoice" pada TOP diambil dari SNX-FAT-SOP-01 butir 4.8.
3. "Review internal" dibaca sebagai pemeriksaan paket (proposal, quotation, Catatan review scope, lembar harga dan margin). Sumber tidak mendefinisikannya dan tidak menyebut pelaku. Pelaku VP Commercial berstatus USULAN 6.
4. Tiga nama rekaman (Lembar harga dan margin, Catatan review scope, Catatan persetujuan penawaran) adalah rekaman baru buatan dokumen ini. Tidak ada baris checklist untuk ketiganya.
5. Persetujuan harga dibaca berlaku untuk setiap penawaran; persetujuan diskon hanya bila ada diskon (mengikuti "Approval diskon (jika ada)").
6. "Pengecualian komersial" didefinisikan dari lima jenis yang punya jalur keputusan di sumber atau dokumen terkait: perubahan harga, diskon, scope, atau timeline sesudah persetujuan; TOP di atas standar; klausul yang menyimpang dari template; komitmen di luar kontrak. Larangan fitur belum tersedia dan timeline tanpa konfirmasi tetap larangan (butir 4.4), bukan pengecualian, karena sumber tidak memberi jalur persetujuan untuknya.
7. Persetujuan TOP di atas standar saya taruh sebelum penawaran dikirim. SNX-FAT-SOP-01 butir 4.8 hanya mensyaratkannya sebelum PKS atau PO disepakati. Penempatan lebih awal berstatus USULAN 2.
8. Klausul ISO di bagian 11 berasal dari pengetahuan standar saya, tidak dicocokkan dengan teks standar (UNMEASURED), semuanya di bawah satu label "(USULAN, perlu konfirmasi konsultan)". Klausul 9.1.2 dan 7.2 sengaja tidak dimasukkan: dokumen ini tidak punya proses kepuasan atau kompetensi.
9. Retensi semua rekaman "Belum ditetapkan"; lokasi berkas tidak ditetapkan kecuali CRM (satu-satunya tempat catatan di sumber).
10. SLA: hanya angka 24 jam yang dari sumber. Tidak ada durasi review, verifikasi, atau persetujuan yang saya buat. Baris terakhir tabel SLA menyatakan itu terang-terangan.
11. Diagram bagian 7 diturunkan dari prosedur 6.1 sampai 6.5 dan bagian 9. Jalur "Tidak" pada persetujuan COO (kembali ke review internal) adalah tafsir dari gerbang butir 4.8; sumber tidak menggambarkan penolakan.
12. Rujukan butir ke dokumen lain (SOP-01 butir 4.6, 4.13, 6.3; FAT-SOP-01 butir 4.5, 4.8; LEG-SOP-02 butir 4.3, 6.1; ISMS-PRO-01 butir 4.19; ORG-01 K-10) dicocokkan dengan spec di repo pada saat saya menulis. Spec FAT, LEG, dan ISMS masih Draft.

## USULAN

Sepuluh butir keputusan. Spec memuat 17 kemunculan persis "(USULAN)" sesudah sweep (satu di antaranya baris definisi label itu sendiri; label kini ada langsung pada kalimat yang bersangkutan) dan satu label "(USULAN, perlu konfirmasi konsultan)" pada klausul ISO.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Wewenang harga: VP Commercial merekomendasikan, COO menyetujui harga dan diskon dan menetapkan margin final; sampai ambang dan batas margin ditetapkan, setiap penawaran dan setiap diskon butuh persetujuan COO. Selaras COM-SOP-01 butir 4.10 | Butir 4.7; langkah 6.5.2 sampai 6.5.4 | owner |
| 2 | Pemutus pengecualian komersial: COO (diskon, harga baru, klausul, komitmen di luar kontrak) dan Direktur Utama (TOP di atas standar, sebelum penawaran dikirim); perubahan scope atau timeline diproses ulang lewat 6.2, 6.3, 6.5 | Butir 4.10; langkah 6.4.8 dan 6.4.9 | owner (Samuel untuk TOP) |
| 3 | Verifikasi harga dan margin setiap penawaran oleh Finance (data) dan Accounting & Tax (klasifikasi COGS, margin, perlakuan PPN) sebelum review internal | Butir 4.6; langkah 6.3.2 dan 6.3.4 | FAT |
| 4 | Titik waktu Legal & Compliance: review klausul dan syarat komersial yang menyimpang sebelum penawaran dikirim | Butir 4.11; langkah 6.4.4 dan 6.4.5 | Legal |
| 5 | COGS, margin, dan lembar harga dan margin berklasifikasi RESTRICTED (Internal); harga mengikuti COM-SOP-01 butir 4.13 | Butir 4.13; bagian 11 | Fani |
| 6 | Penetapan pelaku yang tidak disebut sumber (Finance dan Accounting & Tax dalam validasi; Manager of Product Tech eskalasi ke VP Commercial; VP Commercial review internal dan penyimpan Catatan persetujuan penawaran; Legal & Compliance penyimpan hasil review; Business Development melengkapi penawaran ditolak) dan tiga rekaman baru | Butir 4.5 dan 4.8; bagian 9 dan 11 (label di tiap kalimat) | owner |
| 7 | Pemetaan peran: Presales ke Manager of Product Tech, Delivery ke Service Delivery Manager (jabatan usulan tanpa pemegang) | Tabel peran bagian 5 | owner (dengan Fani) |
| 8 | Pembagian rumah aturan: rincian proposal, quotation, dan harga ada di SOP ini, ringkasannya di COM-SOP-01 butir 4.8 sampai 4.11 dan 6.4 | Dokumen terkait bagian 11 | owner |
| 9 | SNX-COM-FRM-01 sebagai bentuk Catatan review scope; diubah W9: SNX-COM-FRM-01 ditulis sebagai bentuk rekaman Catatan review scope tanpa kata "calon"; label (USULAN) dipasang kembali pada hubungan itu (R2) | Dokumen terkait dan rekaman bagian 11 | owner |
| 10 | Daftar klausul ISO 9001:2015 (5.3, 7.5.3, 8.2.1, 8.2.2, 8.2.3, 8.2.4) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.14), label "(USULAN, perlu konfirmasi konsultan)" | Bagian 11, Acuan standar | owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Ambang diskon, batas margin minimum, dan tenggat review internal, verifikasi, dan persetujuan tidak ada di sumber. Authority Matrix belum bernomor dan tidak diketahui memuat ambang | owner |
| 2 | Penetapan COO sebagai penyetuju (USULAN 1 dan 2) belum diputus tertulis; hubungan dengan Direktur Utama untuk nilai atau jenis penawaran tertentu belum ada | owner dan Samuel |
| 3 | Tumpang tindih dengan SNX-COM-SOP-01: butir 4.8 sampai 4.11, 6.4, dan 6.6 di sana memuat aturan yang sama dengan butir 4.2, 4.3, 4.4, 4.7, 4.8, 6.4, dan 6.5 di sini. Perlu satu rumah dan rujukan satu arah. Sampai diputus, butir 4.7 di kedua dokumen harus tetap identik | owner |
| 4 | Bentuk rekaman: Lembar harga dan margin, Catatan review scope, Catatan persetujuan penawaran tidak punya baris checklist. Putuskan formulir baru, dilebur ke SNX-COM-FRM-01 (checklist baris 52), atau berkas biasa; juga lokasi, pemilik, retensi semua rekaman | owner dan Legal |
| 5 | Verifikasi Finance dan Accounting & Tax: berlaku untuk setiap penawaran atau di atas nilai tertentu; pemetaan Finance Lead dan Finance Staff ke jabatan (K-13) | FAT |
| 6 | PPN pada harga penawaran: rumusan tunggal ada di SNX-FAT-SOP-01 butir 4.5 (12%, USULAN) dan belum diputus FAT | FAT |
| 7 | TOP standar berstatus USULAN di SNX-FAT-SOP-01 butir 4.8; persetujuan Direktur Utama di SOP ini ditaruh sebelum penawaran dikirim, lebih awal daripada batas di dokumen FAT (sebelum PKS atau PO) | FAT dan Samuel |
| 8 | Harga berklasifikasi RESTRICTED (Internal) berbenturan dengan SNX-ISMS-PRO-01 butir 4.10 (RESTRICTED dibagikan ke luar hanya dengan NDA atau kontrak dan persetujuan Pemilik informasi). Apakah persetujuan COO di butir 6.5 dihitung sebagai persetujuan Pemilik informasi, dan apakah NDA wajib sebelum penawaran berharga dikirim | Fani dan Legal |
| 9 | Kanal permintaan antarfungsi (Finance, Accounting & Tax, Manager of Product Tech, Service Delivery Manager): GLPI (generalist) atau Zammad (Ops). Batas lingkup "generalist" belum dirinci owner | owner |
| 10 | Tujuan eskalasi solusi yang tidak feasible (VP Commercial, USULAN 6) dan garis lapor Manager of Product Tech yang belum dikonfirmasi (K-02) | owner |
| 11 | Arti "strategis", "pihak yang berwenang", "di luar kewenangan", dan "komitmen di luar kontrak" tidak didefinisikan di sumber | owner |
| 12 | Tata cara delegasi saat COO atau Direktur Utama berhalangan. Job Analysis hanya menyebut "Mendelegasikan kewenangan dengan bukti tertulis" (JA-01) | Samuel |
| 13 | Satu nama untuk dokumen wewenang: Authority Matrix (HR-ORG-01, Job Analysis) atau matriks DoA (SNX-LEG-SOP-02) | owner dan Legal |
| 14 | Siklus tinjau: Sales SOP menulis 6 bulan, dokumen ini YEARLY (defaults) | owner |
| 15 | Service Delivery Manager dan Manager of Product Tech sebagai padanan Delivery dan Presales: jabatan pertama usulan tanpa pemegang (K-10) | Fani |
| 16 | Customer pemerintah: SNX-ISMS-PRO-01 butir 4.19 hanya melarang harga di dokumen teknis; saluran penyampaian harga ke customer pemerintah tidak diatur | Fani |
| 17 | Nama produk CRM dan lokasi simpan berkas proposal, quotation, dan lembar harga dan margin | owner |
| 18 | Status berlaku Sales SOP lama ("Version 1.0", efektif 28 Juli 2026) sesudah SOP ini dan SNX-COM-SOP-01 disahkan; sumber lama memuat "Approval harga" tanpa pelaku | owner |

## 5. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya enam tanda; semuanya sudah diperbaiki kecuali satu yang saya biarkan:
   - Butir 6.5 membuka dengan kalimat yang menyalin aturan urutan dan syarat kirim di butir 4.8. Diperbaiki: satu kalimat yang menunjuk butir 4.8.
   - Definisi "Review internal" menyebut pelaku VP Commercial tanpa label, sementara butir 4.15 memberi label USULAN untuk pelaku yang sama. Diperbaiki: definisi menunjuk butir 4.15 (sesudah sweep: butir 4.8, karena butir 4.15 dihapus).
   - Butir 4.4 dan 4.5 sama-sama menyebut Service Delivery Manager mengonfirmasi timeline. Diperbaiki: butir 4.4 menunjuk butir 4.5 sebagai satu-satunya tempat pelaku konfirmasi.
   - Definisi "Pengecualian komersial" tidak mencakup perubahan harga dan timeline yang butir 4.9 sebut. Diperbaiki: definisi dan butir 4.9 disamakan, butir 4.9 tidak lagi mengulang daftarnya.
   - Kalimat kesimpulan pertama berbentuk pasif tanpa pelaku ("dinilai dalam evaluasi"). Diperbaiki: kembali ke susunan kalimat tim ("menjadi bagian dari evaluasi kinerja dan probation").
   - Frasa dalam deskripsi dokumen terkait memakai kata "sumber" ("sumber butir 4.6"), yang terbaca seperti frasa proses penyusunan. Diperbaiki: "memuat".
   - Dibiarkan: hampir semua butir kebijakan dan langkah prosedur dibuka dengan "Business Development", dan bagian 9 memakai pola "X tidak dapat ..., Business Development tidak ...". Itu mengikuti aturan satu pelaku per butir (RUNBOOK 6a.1) dan satu pelaku mengerjakan sebagian besar langkah di proses ini. Kolom Output memakai pola nama rekaman karena itu nama rekaman. Daftar tujuh bagian proposal di butir 4.2 adalah daftar tim, bukan kelompok tiga yang dipaksakan.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa terhadap tabel Fakta kunci, Fakta penting lain, dan pemetaan peran:
   - Angka: satu, yaitu 24 jam (Sales SOP hal. 13), dipakai pada lingkupnya (pembaruan CRM atas proposal dan quotation). "1 hari kerja" dan "2 jam kerja" tidak diulang; bagian 8 menunjuk SNX-COM-SOP-01 bagian 8. Nol persentase, nilai, ambang, atau durasi buatan saya. "Maksimal 24 jam" tidak diperluas ke review atau persetujuan.
   - Nama: Laras Rasmawati, Amirull Yusuf Zulkarnain, dan Samuel Kristanto Utomo hanya di blok approval (prompt dan defaults). Nol nama orang lain. Nama peran dari SNX-HR-ORG-01; Service Delivery Manager adalah jabatan usulan tanpa pemegang.
   - Tanggal: nol. Satu penanda waktu di notes ini ("28th of July, 2026") adalah tanggal efektif Sales SOP, tidak dibawa ke dokumen.
   - Tanpa sumber tertulis tetapi ada di dokumen, semuanya berlabel atau tercatat di notes: definisi umum Assumptions, BOM/BOQ, COGS, Margin, Exclusions, TOP; tiga nama rekaman baru; pemutus harga dan margin (USULAN 1); pemutus pengecualian dan penempatan persetujuan TOP (USULAN 2); verifikasi Finance dan Accounting & Tax serta cek PPN (USULAN 3); titik waktu Legal (USULAN 4); klasifikasi COGS dan margin (USULAN 5); penunjukan pelaku (USULAN 6); pemetaan peran (USULAN 7); judul klausul ISO (USULAN 10).
   - Tidak berlabel di dokumen tetapi tafsir saya: pembagian pengecualian komersial lima jenis (definisi) dan urutan prosedur 6.1 sampai 6.5. Dicatat di asumsi 1 dan 6.
   - Rujukan ke spec lain dicocokkan dengan isinya saat ini; tiga di antaranya (FAT, LEG, ISMS) masih Draf dan bisa berubah.

## Sweep

Putaran sweep 15 Okt 2026, satu butir: pengantar 6.1 sampai 6.3 pasif tanpa pelaku; butir 4.15 menjadi wadah USULAN; istilah Personel Commercial tidak ada di bagian 5. Satu butir diubah, tiga bagian. Fakta, angka, nama, dan struktur lain tetap. Salinan spec sebelum sweep: /tmp/pen-COM-SOP-02/COM-SOP-02.before-sweep.json.

| # | Lokasi | Sebelum | Sesudah |
|---|---|---|---|
| 1a | Pengantar 6.1 | "Proposal disusun dari Business Requirement hasil discovery meeting. Commercial Proposal diisi sesudah harga dan margin terverifikasi (butir 6.3)." | "Business Development menyusun proposal dari Business Requirement hasil discovery meeting, dan mengisi Commercial Proposal sesudah harga dan margin terverifikasi (butir 6.3)." |
| 1a | Pengantar 6.2 | "Review scope dilakukan sesudah draf proposal ada dan sebelum review internal (butir 4.5)." | "Business Development meminta review scope sesudah draf proposal ada dan sebelum review internal (butir 4.5)." |
| 1a | Pengantar 6.3 | "Lembar harga dan margin disusun untuk setiap penawaran. ..." | "Business Development menyusun lembar harga dan margin untuk setiap penawaran. ..." (kalimat kedua tetap) |
| 1b | Butir 4.15 | Satu butir berisi semua penetapan USULAN (pelaku dan rekaman), dirujuk dari definisi, butir 4.6, tabel peran, langkah 6.2.4 dan 6.5.5, bagian 9, dan bagian 11 | Butir 4.15 dihapus. Label (USULAN) dipindah ke kalimat yang bersangkutan, rujukan "(butir 4.15)" dihapus atau diarahkan, rincian di bawah |
| 1b | Butir 4.6 | "... dari Finance (butir 6.3 dan 4.15)." | "... dari Finance (butir 6.3). Keterlibatan Finance dan Accounting & Tax ini berstatus (USULAN)." |
| 1b | Butir 4.5 | Tanpa kalimat eskalasi | Ditambah "Manager of Product Tech mengeskalasi solusi yang tidak feasible kepada VP Commercial (USULAN)." Langkah 6.2.4 kini merujuk butir 4.5 |
| 1b | Butir 4.8 | Tanpa pelaku review internal | Ditambah "VP Commercial melakukan review internal; penunjukan pelaku ini berstatus (USULAN)." Definisi Review internal dan baris bagian 9 "VP Commercial menolak penawaran" kini merujuk butir 4.8 |
| 1b | Tabel peran, VP Commercial | "... menyimpan Catatan persetujuan penawaran (butir 4.15)." | "... menyimpan Catatan persetujuan penawaran (butir 4.8 dan bagian 11)." |
| 1b | Langkah 6.5.5 | "... keputusan pengecualian komersial (butir 4.15)." | "... keputusan pengecualian komersial." |
| 1b | Bagian 9, penawaran ditolak | "Business Development melengkapi penawaran sesuai alasan penolakan, dan VP Commercial mengulang review internal (butir 4.15)." | "Business Development melengkapi penawaran sesuai alasan penolakan (USULAN), dan VP Commercial mengulang review internal (butir 4.8)." |
| 1b | Bagian 11, rekaman | Catatan review scope: "... SNX-COM-FRM-01 adalah calon bentuknya (USULAN)"; lembar harga dan margin tanpa label; Catatan persetujuan penawaran: "pemilik VP Commercial (butir 4.15)"; hasil review Legal: "pemilik Legal & Compliance (butir 4.15)" | Tiga rekaman baru berlabel "Rekaman baru (USULAN)" pada barisnya (Catatan review scope dengan "calon bentuknya SNX-COM-FRM-01", Catatan persetujuan penawaran tanpa rujukan butir); hasil review Legal: "pemilik Legal & Compliance (USULAN)" |
| 1c | Bagian 9, baris terakhir | "Personel Commercial perlu menyimpang dari prosedur" / "Personel itu memperoleh persetujuan VP Commercial atau pihak yang berwenang atas penyimpangan tersebut." | "Business Development perlu menyimpang dari prosedur" / "Business Development memperoleh persetujuan VP Commercial atau pihak yang berwenang atas penyimpangan tersebut." |
| 1c | Conclusion kalimat 1 | "... evaluasi kinerja dan probation Personel Commercial." | "... evaluasi kinerja dan probation Business Development dan VP Commercial." |

Catatan keputusan sweep:
- Sebutan "Business Development dan VP Commercial" pada Conclusion mengikuti peran Commercial yang ada di tabel peran bagian 5. Sumber menulis "seluruh anggota tim Commercial"; Brand & Marketing tidak punya peran di SOP ini, sehingga tidak disebut. Ini penyempitan sebutan, bukan fakta baru; bila owner ingin semua personel Commercial tercakup, pemutusnya owner.
- Pengganti "Personel Commercial" di bagian 9 hanya Business Development, karena penyimpangan oleh VP Commercial sendiri tidak diatur sumber ("pihak yang berwenang" tetap tanpa definisi, open item 11).
- Nama tiga rekaman tidak diseragamkan huruf kapitalnya di putaran ini (temuan pemeriksa lain, di luar butir sweep). Penulisan sekarang: "Catatan review scope" dan "Catatan persetujuan penawaran" berhuruf kapital C, "lembar harga dan margin" huruf kecil di badan.
- Tidak disentuh karena di luar butir: kalimat Purpose ke-2, kemiripan butir 4.7 dengan SNX-COM-SOP-01 butir 4.10 (open item 3), kata "segera" di bagian 9, dan nilai "Belum ditetapkan" pada tenggat dan retensi (open item 1, 4, 17).

Uji sesudah sweep (lulus pada putaran pertama):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-SOP-02.json /tmp/pen-COM-SOP-02/COM-SOP-02.docx`: selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-COM-SOP-02/COM-SOP-02.docx sop`: `"pass": true`, `"fails": []`, satu warn "17 butir (USULAN) menunggu ACC", nol warn PIC SLA.
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-COM-SOP-02/COM-SOP-02.docx`: "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-COM-SOP-02/COM-SOP-02.docx`: `ok	20	COM-SOP-02.docx	[]`.

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| B2 Bagian 9, baris terakhir | "Business Development perlu menyimpang dari prosedur" / "Business Development memperoleh persetujuan VP Commercial atau pihak yang berwenang ..." | "Business Development atau VP Commercial perlu menyimpang dari prosedur" / "Business Development atau VP Commercial yang perlu menyimpang memperoleh persetujuan VP Commercial atau pihak yang berwenang ..." |
| 7 Bagian 11 Dokumen terkait, SNX-COM-FRM-01 | "judul menurut daftar dokumen SINUX. Calon bentuk Catatan review scope (USULAN)." | "bentuk rekaman Catatan review scope." |
| 7 Bagian 11 Rekaman, Catatan review scope | "calon bentuknya SNX-COM-FRM-01" | "bentuk rekamannya SNX-COM-FRM-01" (pemilik tetap Business Development) |
| R2 1b Bagian 11 Rekaman, Catatan review scope | "bentuk rekamannya SNX-COM-FRM-01" | "bentuk rekamannya SNX-COM-FRM-01 (USULAN)" |
| R2 1b Bagian 11 Dokumen terkait, SNX-COM-FRM-01 | "bentuk rekaman Catatan review scope." | "bentuk rekaman Catatan review scope (USULAN)." |

B2: Conclusion kalimat 1 sudah memuat Business Development dan VP Commercial (hasil sweep), sehingga tidak diubah. Brand & Marketing tidak punya peran di bagian 5, jadi tidak disebut; bila owner ingin Brand & Marketing tercakup, perlu peran baru di bagian 5 (open item, pemutus owner).

Open item ditutup atau diubah:
- Penyempitan "Personel Commercial" (catatan sweep 1c, bagian 9): ditutup W9 (B2), cakupan dikembalikan ke Business Development dan VP Commercial.

R2 butir 3: baris USULAN dan Open items yang ditutup atau diubah W9 diberi keterangan "ditutup W9" atau "diubah W9" di barisnya sendiri.
