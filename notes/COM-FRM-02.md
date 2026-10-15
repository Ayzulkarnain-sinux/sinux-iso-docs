# Catatan penyusun COM-FRM-02: Project Handover Record

Status: DRAFTED (spec + notes ada). Spec: specs/COM-FRM-02.json. Mode generic (FORM), aksi T2, wave W7, nomor SNX-COM-FRM-02 (nomor SNX lama dipertahankan), department "Commercial", classification "INTERNAL", audit_class kosong. Approval persis dari prompt: prepared "Laras Rasmawati / VP Commercial", reviewed "Amirull Yusuf Zulkarnain / Direktur", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Direktur" (jabatan reviewer departemen, tanpa nama; aturan defaults process_owner untuk dokumen tanpa sumber; status USULAN, lihat OI-3). Catatan worklist: kosong.

Hasil uji terakhir (bukti mentah di /tmp/pen-COM-FRM-02/):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-FRM-02.json /tmp/pen-COM-FRM-02/COM-FRM-02.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-COM-FRM-02/COM-FRM-02.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "11 butir (USULAN) menunggu ACC" (lint.out.txt). Putaran pertama sudah pass; putaran berikutnya hanya perbaikan isi dan tata letak. Hasil sesudah putaran perbaikan 1 sama: pass true.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!" (validate.out.txt).
- soffice ke PDF: 16 halaman (COM-FRM-02.pdf). Halaman 9, 11, 13, dan 14 pada render akhir (Cara Mengisi, Tabel 2 sampai Tabel 5, Tabel 10 sampai Tabel 12, Rekaman dan awal Acuan ISO) dilihat sebagai gambar; Tabel 6 sampai Tabel 9 dilihat pada render sebelumnya dan tidak berubah selain teks sel. Putaran pertama memperlihatkan header "No" terpotong di kolom 0,8 cm (Tabel 5) dan "ditandatangani" terpotong di Tabel 2; lebar kolom dan nama kolom diperbaiki ("Status tanda tangan"), lalu dicek ulang.
- Pemeriksaan tambahan atas docx (skrip python3 -I di scratchpad sesi, bukan di repo; keluaran di extra-checks.out.txt): nol em-dash dan en-dash; nol tanda kutip ganda; nol frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir, hal ini); nol frasa meta penyusunan (dokumen sumber, sumber tim, penyusun, draf ini, versi tim); nol "komersil", "diagnosa", "hutang", "resiko", "CEO", "HR Lead", "Lead"; nol rujukan internal AI (termasuk kata HANDOVER huruf besar; judul bagian "Catatan Handover" diganti "Tabel Isian" karena renderer membesarkan judul); semua kode SNX dan POL-OPS-001 di badan tercantum di tabel Dokumen Terkait (dicek dengan skrip: kurang 0, kelebihan 0); semua sel data di Tabel 1 sampai Tabel 12 kosong kecuali kolom No dan label baris tetap (nol baris contoh).
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas config, control, tools, template, reference, ledger.json, out, qa tidak saya ubah. Berkas yang saya tulis hanya specs/COM-FRM-02.json dan notes/COM-FRM-02.md; render hanya di /tmp/pen-COM-FRM-02/; skrip pembangun spec di folder scratchpad sesi.

## 1. Sumber

Baris ini tidak punya berkas sumber (checklist baris 53: tanpa link, tanpa fileId; worklist sources kosong). Bahan yang dipakai adalah dokumen tetangga yang membahas handover Commercial ke Operation:

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist tim, baris 53 (kriteria) dan baris 49, 52 (dokumen tetangga) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (ekspor 2026-10-14T19:05:35Z, dari config/checklist.json) | Dibaca dari config/checklist.json; Drive tidak dibuka |
| SALES STANDARD OPERATING PROCEDURE.pdf (2.666.844 byte) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (get_file_metadata hari ini) | read_file_content, teks penuh; lapisan teks PDF bercampur antar kartu, urutan butir dicocokkan dengan transkripsi di context/audit commercial |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111.296 byte) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata hari ini) | read_file_content, teks penuh |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183.366 byte) | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata hari ini) | read_file_content, teks penuh; dipakai untuk checklist G1 (bagian 8.2) |
| SNX-OPS-FRM-01_Project_Plan_Scope_Timeline.xlsx (153.326 byte) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 | 2026-10-13T06:09:12Z (get_file_metadata hari ini) | Isi sheet Checklist G1 dibaca dari salinan context/audit ops (bagian SNX-OPS-FRM-01); berkas xlsx TIDAK dibuka di Drive, jadi bisa basi bila berkas berubah |
| Catatan cacat dan verdict | context/audit/iso-sinux-supdocs-commercial-2026-10-14.md (bagian COM-Sales-SOP, bagian 5), iso-sinux-supdocs-ops-2026-10-14.md (POL-OPS-001 dan PRO-OPS-001 bagian 5), iso-sinux-supdocs-sintesis-2026-10-14.md (baris 450, 763, 768, 789) | salinan audit 13 sampai 14 Okt | DATA; tidak ada fileId tunggal |
| Pendukung repo (bukan Drive) | specs/COM-SOP-01.json (butir 4.8, 4.11, 4.13, 4.15, 4.16, 4.19, langkah handover, tabel rekaman), specs/COM-SOP-02.json, specs/COM-FRM-01.json (paralel, belum final saat dibaca), specs/OPS-SOP-01.json (butir 4.1, Inisiasi, tabel rekaman), specs/OPS-FRM-06.json, specs/HR-ORG-01.json (K-10, daftar jabatan), specs/FAT-FRM-01.json (pola form T2), config/defaults.json v21 | repo kerja | Dibaca sebagai DATA untuk menyelaraskan istilah dan peran; kutipan dari spec lain bisa basi bila dokumen itu berubah |

Alat Drive yang dipakai hanya baca (get_file_metadata, read_file_content). Nol penulisan, salin, bagi, atau hapus. Kalimat perintah kepada AI di sumber: nihil. Kalimat kewajiban di sumber ("wajib", "Sales wajib ...") adalah isi SOP untuk karyawan, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Handover Commercial ke tim pelaksana wajib memuat enam butir minimal dan didahului handover meeting sebelum implementasi. Dasar butir 4.1 dan 4.2, serta pemetaan enam butir ke Tabel 1, 3, 4, 5, 6, 9, dan 10 | "Stage 9 Project Handover" / "Sales wajib melakukan handover kepada Delivery." / "Minimal mencakup:" / "Handover meeting wajib dilakukan sebelum implementasi dimulai." / "Customer Background" / "Scope" / "Timeline" / "Risks" / "Commitment" / "Contact Person" (teks sel berurutan di hasil baca) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Gate G1 adalah pintu Commercial ke SD dan PM dengan Service Delivery Manager sebagai pemilik; janji ke customer yang tidak tercatat di G1 tidak mengikat Operation sampai Commercial dan COO menyetujui. Dasar butir 4.7, peran Service Delivery Manager, dan peran COO | "G1 Kick-off | Commercial | SD dan PM | Service Delivery Manager | PO atau kontrak, scope final, SLA tertulis, PIC pelanggan, janji lisan tercatat" dan "Janji ke pelanggan yang tidak tercatat di G1 tidak mengikat Operation sampai disetujui Commercial dan COO." (bagian 8) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |
| Checklist G1 untuk paket handover sales memuat scope final beserta yang di luar scope, SLA tertulis, PIC pelanggan dan kanal resmi, jadwal target live dan batasan customer, serta janji lisan. Dasar Tabel 2 sampai Tabel 6, Tabel 10, dan butir 4.7 | "☐ PO atau kontrak ditandatangani dan diarsip." / "☐ Scope teknis final, termasuk daftar yang di luar scope." / "☐ SLA dan target layanan yang dijanjikan ke pelanggan, tertulis." / "☐ PIC pelanggan (teknis, komersial, billing) dan kanal komunikasi resmi." / "☐ Jadwal target live dan batasan pelanggan (window maintenance, blackout)." / "☐ Janji lisan ke pelanggan yang belum ada di kontrak, dicatat terbuka." (bagian 8.2, G1) | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | Kriteria penerimaan baris 53 | "Mencatat scope final, quotation/PO/kontrak, deliverables, jadwal, PIC, dependency, asumsi, risiko, dan komitmen kepada customer yang harus dipenuhi tim pelaksana." | config/checklist.json baris 53 (checked false, tanpa link, kolom ISO null) |
| 2 | Isi proposal yang menjadi asal Tabel 3, 4, 5, dan 8 (butir 4.3) | "Proposal wajib mencakup:" dengan butir "Scope of Work", "Proposed Solution", "Deliverables", "Timeline", "Commercial Proposal", "Assumptions", "Exclusions" (urutan lapisan teks bercampur antar kartu; urutan benar di transkripsi audit commercial, butir Stage 6) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0, Stage 6 |
| 3 | Larangan menjanjikan timeline tanpa konfirmasi Delivery (dasar kolom Tanggal konfirmasi dan butir 4.6) | "Sales tidak diperbolehkan:" ... "Menjanjikan timeline tanpa konfirmasi Delivery." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0, bagian 08 |
| 4 | Syarat closing dan kelengkapan dokumen sebelum handover (definisi Closing dan Dokumen closing, butir 4.1) | "Closing dinyatakan berhasil apabila:" "Purchase Order diterima." "Kontrak ditandatangani." "Internal approval selesai." dan "Sales wajib memastikan seluruh dokumen lengkap sebelum handover." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0, Stage 8 |
| 5 | Service Delivery Manager menerima atau menolak handover G1 | "Wewenang: menerima atau menolak handover G1 dari Commercial." | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, bagian 9.4 |
| 6 | G1 yang tidak lolos mengembalikan paket ke Commercial (butir 4.12) | "G1 tidak lolos: paket dikembalikan ke Commercial, onboarding belum dimulai." | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz, bagian 8.3 |
| 7 | Larangan kredensial di dokumen (butir 4.8) | "Kredensial tidak pernah di grup, chat, tiket, atau dokumen." (kolom Dasar baris P-03 berisi rujukan internal AI; tidak disalin) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, bagian 4, P-03 |
| 8 | Keputusan G1 dicatat di SNX-OPS-FRM-01 sebagai LOLOS atau TAHAN | "Rumus keputusan (sel C14, label B14 \"Keputusan G1\"): =IF(COUNTIF(C5:C12,\"Belum\")=0,\"LOLOS\",\"TAHAN\")" | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3, sheet Checklist G1 (lewat salinan context/audit ops, bukan Drive) |
| 9 | Penerimaan paket G1 oleh Service Delivery Manager dan retensi rekaman rencana proyek | "4.1 Penerimaan paket G1 (ISO 9001:2015 8.2): proyek dimulai hanya sesudah Service Delivery Manager menerima paket G1 dari Commercial, dengan checklist G1 di SNX-OPS-FRM-01 tanpa butir berstatus Belum." dan baris rekaman "Project plan, scope, timeline, checklist G1, dan notulen kick-off pelanggan (SNX-OPS-FRM-01)" / "Drive proyek; pemilik Project Manager" / "Durasi kontrak + 3 tahun" | specs/OPS-SOP-01.json (repo, Draft) |
| 10 | Handover dan penyerahan paket oleh VP Commercial; formulir ini sebagai calon rekaman | "Susun paket handover dengan isi minimal di butir 4.16." (Business Development), "Serahkan paket handover kepada Service Delivery Manager atas nama Commercial (butir 4.19)." (VP Commercial), dan Dokumen terkait "SNX-COM-FRM-02 | Project Handover Record; judul menurut daftar dokumen SINUX, isi belum dikonfirmasi. Calon rekaman paket handover di butir 6.8 (USULAN)." | specs/COM-SOP-01.json (repo, Draft) |
| 11 | Klasifikasi informasi customer dan kontrak (butir 4.14) | "Informasi customer, kontrak, dan harga berklasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 butir 4.3 (USULAN, karena SNX-ISMS-PRO-01 belum mencakup Commercial)." | specs/COM-SOP-01.json butir 4.13 (repo). Kalimat itu di sumbernya sendiri berstatus USULAN |
| 12 | Service Delivery Manager dan Project Manager belum punya pemegang | "Nama jabatan, jenjang, headcount, dan garis lapor ke COO berstatus USULAN di POL-OPS-001, tanpa pemegang bernama." | specs/HR-ORG-01.json, butir K-10 |
| 13 | Dokumen tetangga memakai formulir ini sebagai calon rekaman serah terima | "Serah terima order ke Delivery | Diatur di SNX-COM-SOP-01 butir 6.8 dan SNX-OPS-SOP-01 butir 4.1. Calon rekamannya SNX-COM-FRM-02 (USULAN)." | specs/COM-FRM-01.json (paralel, belum final) |
| 14 | Isi SNX-COM-FRM-01 yang dipakai butir 4.4 (kelompok Kesesuaian Scope dan Delivery Commitment) | "Kelompok C1: Kesesuaian Scope" dan "Kelompok C4: Delivery Commitment" | specs/COM-FRM-01.json (paralel, belum final; bisa berubah) |
| 15 | Judul mirip yang harus dibedakan | "SNX-OPS-FRM-06 | Project Handover / BAST & Closure Report" dengan bagian "A. Berita Acara Serah Terima (BAST) ke pelanggan (gate G2)" dan "B. checklist serah terima internal SD dan PM ke Operation (gate G3)" | context/audit ops, bagian SNX-OPS-FRM-06; specs/OPS-FRM-06.json |

## 3. Pemetaan kriteria (Description baris 53)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| "scope final" | Tabel 3 (Uraian scope final), Tabel 4 (di luar scope); butir 4.2 dan 4.3 | Checklist G1 butir 2; Sales SOP Stage 9 (Scope) |
| "quotation/PO/kontrak" | Tabel 2 (nomor, tanggal, status tanda tangan, lokasi arsip; baris tetap Quotation, PO, Kontrak) | Checklist G1 butir 1; Sales SOP Stage 8 |
| "deliverables" | Tabel 3 (kolom Deliverable), satu baris satu deliverable | Sales SOP Stage 6 (bagian Deliverables proposal) |
| "jadwal" | Tabel 5 (milestone, tanggal target, batasan customer, dasar jadwal, tanggal konfirmasi Service Delivery Manager); butir 4.6 | Checklist G1 butir 6; Sales SOP bagian 08 |
| "PIC" | Tabel 6 (PIC customer teknis, komersial, billing; PIC SINUX; kanal resmi) | Checklist G1 butir 5; Sales SOP Stage 9 (Contact Person) |
| "dependency" | Tabel 7; definisi Dependency; butir 4.8 untuk dependency akses | Kriteria baris 53; PRO-OPS-001 G3 menyebut "ketergantungan vendor" sebagai isi as-built (dasar istilah) |
| "asumsi" | Tabel 8, disalin dari bagian Assumptions proposal | Sales SOP Stage 6 |
| "risiko" | Tabel 9; butir 4.5 dan 4.9 | Sales SOP Stage 9 (Risks) |
| "komitmen kepada customer yang harus dipenuhi tim pelaksana" | Tabel 10 (komitmen, sumber, batas waktu atau ukuran, Dipenuhi oleh); butir 4.7 dan 4.10; definisi Tim pelaksana | Checklist G1 butir 3 dan 7; POL-OPS-001 bagian 8 ketentuan 3 |

Pemetaan klausul ISO (bagian Rekaman dan Acuan ISO, satu label "(USULAN, perlu konfirmasi konsultan)"; checklist baris 53 tidak memberi acuan klausul: iso_9001 dan iso_27001 null). Judul klausul adalah pengetahuan standar, bukan teks sumber, dan tidak dicocokkan dengan teks standar (UNMEASURED):

| Klausul | Butir atau tabel | Alasan |
|---|---|---|
| ISO 9001:2015 7.4 Komunikasi | Tabel 6, butir 4.10 | PIC, kanal resmi, dan penyampaian isi ke tim pelaksana |
| ISO 9001:2015 7.5.3 Pengendalian informasi terdokumentasi | tabel Rekaman | Lokasi, pemilik, retensi, klasifikasi |
| ISO 9001:2015 8.2.3 Tinjauan persyaratan untuk produk dan jasa | Tabel 2 sampai 4, 9, 10 | Persyaratan customer yang berlaku saat closing; COM-SOP-01 sudah memakai klausul ini |
| ISO 9001:2015 8.5.1 Pengendalian produksi dan penyediaan jasa | Tabel 3, 5, 10 | Informasi tentang hasil yang harus dicapai tim pelaksana |
| ISO/IEC 27001:2022 Annex A 5.12 Klasifikasi informasi | butir 4.14 | Klasifikasi formulir kosong dan terisi; COM-SOP-01 dan COM-FRM-01 memakai klausul ini |
| ISO/IEC 27001:2022 Annex A 5.14 Transfer informasi | butir 4.8, 4.10 | Informasi customer berpindah ke tim pelaksana; larangan kredensial |
| ISO/IEC 27001:2022 Annex A 5.31 Persyaratan hukum, perundang-undangan, regulasi, dan kontraktual | Tabel 2, 10 | Persyaratan kontraktual dan komitmen; COM-FRM-01 memakai klausul ini |
| ISO/IEC 27001:2022 Annex A 5.33 Perlindungan rekaman | tabel Rekaman | Lokasi dan retensi rekaman |

## 4. Penanganan cacat context/audit

`grep -n "Project Handover Record" context/audit/*.md` tidak menemukan satu baris pun (keluaran kosong). Dokumen ini tidak punya bagian 5 Catatan kualitas sendiri (T2 tanpa sumber). Cacat yang relevan diambil dari dokumen tetangga dan verdict sintesis:

| Berkas sumber | Cacat tercatat | Penanganan |
|---|---|---|
| Sales SOP (audit commercial, bagian 5) | "Delivery disebut sebagai penerima handover ... tanpa penerima individu atau form terdefinisi" dan "Tidak ada form handover bernomor" | Penerima = Service Delivery Manager (SNX-COM-SOP-01 dan SNX-OPS-SOP-01); form = dokumen ini. Service Delivery Manager belum punya pemegang (OI-5) |
| Sales SOP (bagian 5) | "Tidak ada tenggat untuk follow-up lead, approval internal, atau handover" | Tidak ada batas waktu yang dikarang; formulir tidak menetapkan angka. Jadi OI-6 |
| Sales SOP (bagian 5) | Kontrol "Menjanjikan timeline tanpa konfirmasi Delivery" tanpa rekaman bukti selain CRM | Kolom Tanggal konfirmasi Service Delivery Manager di Tabel 5 menjadi rekaman bukti (USULAN, butir 4.6) |
| Sales SOP, Stage 8 | Syarat closing memasukkan "Project Kick-off atau implementasi telah dimulai", padahal handover wajib sebelum implementasi | Definisi Closing hanya memuat PO diterima, kontrak ditandatangani, persetujuan internal selesai (selaras SNX-COM-SOP-01 butir 4.15) |
| Sales SOP (bagian 5) | Komposisi tim tidak konsisten (Business Development, Sales Executive, Presales) | Peran memakai nama dari SNX-HR-ORG-01; Business Development memegang tugas Sales dan Sales Executive (USULAN, mengikuti SNX-COM-SOP-01) |
| POL-OPS-001 (audit ops, bagian 5 butir 3 dan 7) | Pemilik dokumen COO lawan Head of Operation; rujukan internal AI di kolom Dasar | Hanya bagian 8 ketentuan 3 dan kebijakan P-03 yang dikutip; kolom Dasar dan rujukan internal tidak disalin. Pemilik formulir ini tidak bergantung pada pemilik POL |
| POL-OPS-001 (bagian 5 butir 2) | Butir bertanda USULAN didaftar | Bagian 8 ketentuan 3 tidak bertanda USULAN di sumber (ketentuan 2 bertanda), jadi dipakai sebagai aturan tanpa label tambahan |
| PRO-OPS-001 dan SNX-OPS-FRM-01 | Checklist G1 memuat 7 butir di PRO-OPS-001 dan 8 butir di sheet Checklist G1 (butir 8: klasifikasi data pelanggan dan kebutuhan keamanan informasi) | Dokumen ini hanya memuat butir yang diminta kriteria baris 53. Butir sizing dan arsitektur serta klasifikasi data tetap di checklist G1. Jadi OI-2 |
| Sintesis baris 450 | "Handover G1 di prosedur Ops" (Com 5, 10; Ops 7), pemilik Ops; Com 10 (Sales-to-Operations Handover Checklist) bertier P dan Com 5 bertier G (sintesis baris 763, 768, dan tabel tier) | Checklist baris 53 tetap meminta dokumen dan worklist menetapkan T2, jadi formulir dibuat. Ketegangan dengan verdict digabung dicatat sebagai OI-1; formulir tidak menduplikasi keputusan gate G1 (tetap di SNX-OPS-FRM-01) |
| Sintesis baris 789 | SNX-OPS-FRM-06 berjudul Project Handover / BAST & Closure Report | Judul mirip dibedakan di Ruang Lingkup dan Dokumen Terkait. Jadi OI-8 |

## 5. Asumsi

| # | Asumsi | Alasan |
|---|---|---|
| A1 | process_owner = "Direktur" | Dokumen tanpa sumber; aturan defaults: jabatan pada kolom reviewed departemen, tanpa nama. Status USULAN (OI-3) |
| A2 | "Tim pelaksana" di kriteria = Service Delivery Manager, Project Manager, dan peran Divisi Operation lain yang menjalankan proyek | SNX-OPS-SOP-01 memberi tugas proyek ke Service Delivery Manager, Project Manager, NOC Engineer, SOC Analyst. SNX-COM-SOP-01 menyebutnya Delivery. Kriteria tidak mendefinisikannya (USULAN U-02) |
| A3 | "Setiap handover" mencakup proyek dan layanan baru yang sudah closing | Sales SOP Stage 9 dan SNX-COM-SOP-01 butir 4.16 |
| A4 | Harga, diskon, dan margin tidak masuk formulir | Kriteria tidak menyebut nilai; POL-OPS-001 P-06 melarang Operation memberi harga atau diskon; pengendalian harga ada di SNX-COM-SOP-02. Pengecualian ini USULAN (U-01) |
| A5 | "Dependency" memakai ejaan Inggris sebagai satu istilah kerja | Kata itu ada di kriteria; SNX-COM-FRM-01 memakai "dependensi", dicatat di OI-7 |
| A6 | "5 baris" per tabel isian dan 8 baris di Tabel 6 adalah ukuran tata letak, bukan klaim kapasitas | Kalimat di dokumen: "Tambah baris bila isian lebih banyak daripada baris yang tersedia." |
| A7 | Business Development mengisi formulir; VP Commercial menyerahkan paket; Service Delivery Manager menerima atau menolak; Project Manager memeriksa dan memakai Tabel 9 | SNX-COM-SOP-01 (langkah handover, butir 4.19) dan SNX-OPS-SOP-01 (Inisiasi); pembagian di formulir ini USULAN |
| A8 | "Commercial" di POL-OPS-001 bagian 8 ketentuan 3 dibaca sebagai VP Commercial | POL-OPS-001 P-06 menunjuk "Commercial (Laras)" dan Laras = VP Commercial menurut defaults. Pemetaan USULAN (U-10) |
| A9 | Satu istilah tiap hal: "formulir" (bukan form), "paket handover", "gate G1", "tim pelaksana", "dependency", "komitmen", "PIC", "deliverable" | RUNBOOK §6a butir 7 dan pelajaran W0; "formulir" mengikuti SNX-COM-FRM-01 |
| A10 | Samuel di badan dokumen = "Direktur Utama" (hanya di kalimat blok Approval); Amirull disebut "Direktur (COO)" pada penyebutan pertama (baris definisi), sesudahnya "COO"; nama keduanya hanya di blok Approval | config/defaults.json data_conflicts |
| A11 | Tabel 12 dan baris Tabel 11 "Hasil gate G1" menyalin hasil dari SNX-OPS-FRM-01, bukan menjadi sumber keputusan | SNX-COM-SOP-01 bagian 11: "Keputusan gate G1 dicatat di SNX-OPS-FRM-01" |

## USULAN

14 kemunculan label "(USULAN" di spec (satu adalah baris definisi label itu sendiri) ditambah satu label klausul "(USULAN, perlu konfirmasi konsultan)"; dikelompokkan jadi 14 butir. Pemutus yang disarankan memakai kelompok: owner, Samuel, Aziz, FAT, Legal, Fani.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U-01 | Batas cakupan: enam pengecualian (kebutuhan sebelum order, harga dan margin, keputusan gate G1, project charter dan register risiko, BAST dan G3, penagihan) | Ruang Lingkup | owner |
| U-02 | Arti tim pelaksana: Service Delivery Manager, Project Manager, dan peran Divisi Operation lain yang menjalankan proyek | Definisi | Fani |
| U-03 | Klasifikasi: formulir kosong INTERNAL, formulir terisi RESTRICTED (Internal) | Butir 4.14; baris Rekaman | Fani (pemilik klasifikasi Operation dan ISMS) dan owner |
| U-04 | Struktur kolom Tabel 1 sampai Tabel 12, termasuk kolom Status tanda tangan, Tanggal konfirmasi Service Delivery Manager, Sumber komitmen, dan Dipenuhi oleh | Butir 4.15; Tabel Isian | owner |
| U-05 | Butir 4.1 (waktu pengisian sesudah closing dan sebelum handover meeting), 4.2 (pemetaan enam butir minimal ke tabel), 4.3 (asal isi tabel dari bagian proposal), 4.4 (memakai hasil SNX-COM-FRM-01) | Butir 4.15 | owner |
| U-06 | Perbedaan antara quotation, PO, dan kontrak dicatat di Tabel 9 dan dibawa ke handover meeting | Butir 4.5 | Legal |
| U-07 | Project Manager memakai Tabel 9 sebagai bahan risiko awal di SNX-OPS-FRM-02 | Butir 4.9; Peran; Dokumen Terkait | Fani |
| U-08 | Service Delivery Manager menyebut jabatan tim pelaksana pemenuh tiap komitmen; Business Development mencatat hasil pembahasan di Tabel 11 | Butir 4.10; Peran | Fani |
| U-09 | Tanda tangan tiga peran di Tabel 12, dengan tanda tangan Service Delivery Manager sebagai tanda terima untuk diperiksa dan bukan keputusan gate G1 | Butir 4.13; Tabel 12 | owner dan Fani |
| U-10 | Pemetaan peran: Business Development memegang tugas Sales dan Sales Executive; "Commercial" di POL-OPS-001 bagian 8 ketentuan 3 dibaca VP Commercial; VP Commercial menyerahkan paket (butir 4.19 SNX-COM-SOP-01 berstatus USULAN di sana) | Peran; butir 4.11 | owner |
| U-11 | COO sebagai pemilik dokumen (formulir kosong; Process Owner "Direktur"), peninjau tahunan, dan penetap struktur kolom; diubah W9: COO tidak lagi pemilik dokumen atau peninjau tahunan, hanya penetap struktur kolom; pemilik dan peninjau VP Commercial (A7) | Identity; Peran; butir 4.15; Kesimpulan | owner |
| U-12 | Lokasi rekaman Folder Google Drive Departemen Commercial; pencatat Business Development; pemilik formulir terisi dan penetap lokasi rekaman VP Commercial | Peran; Rekaman baris 1; Kesimpulan | owner |
| U-13 | Retensi Durasi kontrak + 3 tahun untuk formulir terisi (angka sumber hanya untuk rekaman rencana proyek dan checklist G1 di SNX-OPS-SOP-01; perluasan ke formulir ini) | Rekaman baris 1 | Legal dan Fani |
| U-14 | Daftar klausul ISO 9001:2015 (7.4, 7.5.3, 8.2.3, 8.5.1) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.14, 5.31, 5.33), label "(USULAN, perlu konfirmasi konsultan)" | Acuan ISO | owner, setelah konfirmasi konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-1 | Verdict sintesis menggabungkan handover G1 ke prosedur Ops (Com 5 dan 10, Ops 7), sedangkan checklist baris 53 meminta formulir Commercial sendiri. Putuskan: tetap formulir terpisah (seperti sekarang, keputusan gate G1 tetap di SNX-OPS-FRM-01) atau dilebur ke sheet Checklist G1 | owner dan Fani |
| OI-2 | Butir checklist G1 yang tidak diminta kriteria baris 53 tidak dimasukkan: sizing dan arsitektur yang dipakai di proposal, serta klasifikasi data pelanggan dan kebutuhan keamanan informasi (butir 8 sheet Checklist G1; PRO-OPS-001 hanya memuat tujuh butir). Putuskan apakah ditambahkan ke formulir ini atau tetap di checklist G1 | Fani |
| OI-3 | Pemilik dokumen: Process Owner "Direktur" mengikuti aturan dokumen tanpa sumber, sedangkan SNX-COM-SOP-01 dan SNX-COM-SOP-02 menetapkan VP Commercial sebagai pemilik proses penjualan dan Sales SOP menulis "Document Owner: VP of Commercial". SNX-COM-FRM-01 memakai "Direktur" juga; ditutup W9: Process Owner diputus VP Commercial (A7) | owner |
| OI-4 | Lokasi, pemilik, dan retensi rekaman: SNX-COM-SOP-01 mencatat "belum ditetapkan", formulir ini memberi usulan (U-12, U-13). Samakan satu keputusan untuk seluruh rekaman Commercial (paket handover, PO, kontrak). Angka Durasi kontrak + 3 tahun diambil dari SNX-OPS-SOP-01 yang berstatus Draft dengan angka USULAN | owner dan Legal |
| OI-5 | Service Delivery Manager dan Project Manager adalah jabatan usulan tanpa pemegang (K-10). Penerima handover belum punya nama, sehingga formulir belum bisa dijalankan sampai ada pemegang atau penunjukan sementara | owner dan Fani |
| OI-6 | Tidak ada tenggat handover di sumber mana pun (antara closing, handover meeting, dan penyerahan paket). Formulir tidak memuat angka. Putuskan apakah perlu batas waktu | Fani dan owner |
| OI-7 | Konsistensi dengan SNX-COM-FRM-01 yang disusun paralel dan belum final: butir 4.4 menyebut nama kelompok Kesesuaian Scope dan Delivery Commitment; istilah dependency (formulir ini) lawan dependensi (SNX-COM-FRM-01). Cek ulang saat kedua dokumen final | owner |
| OI-8 | Judul mirip dengan SNX-OPS-FRM-06 (Project Handover / BAST & Closure Report) yang mencatat penyerahan ke customer dan ke Operation. Risiko salah pakai; pertimbangkan penyelarasan judul atau penjelasan di kedua dokumen | Fani dan owner |
| OI-9 | Kolom A baris 53 di checklist berisi "Sales Pipeline Tracker", tidak terkait Description baris itu. Dicatat sebagai data dan tidak dipakai; tanyakan apakah pemetaan baris keliru | owner |
| OI-10 | Judul klausul ISO tidak dicocokkan dengan teks standar (UNMEASURED); konfirmasi konsultan sebelum dokumen disahkan | owner, lewat konsultan |
| OI-11 | SNX-COM-SOP-01 butir 6.8 dan tabel rekamannya masih menyebut formulir ini sebagai calon rekaman (USULAN). Sesudah formulir ini disahkan, SNX-COM-SOP-01 perlu menyebutnya sebagai rekaman resmi; diubah W9: SNX-COM-SOP-01 bagian 11 kini menyebut formulir ini sebagai rekaman paket handover tanpa "calon" dan tanpa USULAN pada hubungan itu (R1 butir 9, R2); butir 6.8 SNX-COM-SOP-01 tidak memuat rujukan nomor formulir ini | owner |
| OI-12 | Klasifikasi: SNX-ISMS-PRO-01 belum mencakup Commercial (catatan di SNX-COM-SOP-01 butir 4.13). Tingkat RESTRICTED (Internal) untuk formulir terisi belum punya dasar tertulis di SNX-ISMS-PRO-01 | Fani |
| OI-13 | Dokumen sumber yang dipakai (Sales SOP, POL-OPS-001, PRO-OPS-001) berstatus Draft atau tanpa persetujuan; isi bisa berubah setelah disahkan. Cek ulang butir 4.6, 4.7, 4.8 saat POL-OPS-001 dan PRO-OPS-001 disahkan COO | Fani |

## Jawaban dua pertanyaan akhir (sebelum selesai)

1. Apa yang membuat teks ini terdengar buatan AI, dan perbaikannya.
   - Cara Mengisi awalnya 29 kalimat berpola sama ("Business Development menulis di Tabel n ..."), berulang dan sebagian hanya mengulang judul kolom. Diganti satu tabel petunjuk per kolom atau kelompok kolom (24 baris), tanpa pengulangan judul kolom yang sudah jelas.
   - Definisi Asumsi, Risiko, Deliverable, dan Quotation awalnya kalimat umum yang bisa ditempel ke perusahaan mana pun. Diberi jangkar SINUX (bagian Assumptions dan Deliverables di proposal, Risks di paket handover, tahap proposal dan quotation di SNX-COM-SOP-01), dan kata "resmi" yang tidak bersumber dibuang dari definisi Quotation.
   - Kolom Hubungan di Acuan ISO memakai benda sebagai pelaku ("butir 4.5 membawa", "Handover memindahkan", "butir 4.8 melarang") dan satu hubungan memakai kata kerja manusia pada tabel. Ditulis ulang dengan pelaku peran (Business Development) atau kata "memuat".
   - Judul bagian "Catatan Handover" menumpuk kata istilah kerja dan terbaca HANDOVER huruf besar. Diganti "Tabel Isian".
   - Peran dan Ketentuan awalnya menyebut "paket", "paket G1", dan "paket handover" bergantian. Diseragamkan jadi paket handover; "gate G1" dipakai untuk gerbangnya.
   - Sisa yang dibiarkan: pola kutipan "(SNX-... butir n)" berulang di Dasar dan Ketentuan. Itu penelusuran ke dokumen asal, bukan pengisi. Kalimat kedua Tujuan ("Dengan satu catatan ini ...") dibiarkan karena memuat hasil yang dijaga (RUNBOOK §6a.4).
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber.
   - Nama orang: nol di badan. Nama hanya di blok Approval, dari config/defaults.json. Tanggal: nol. Angka: satu, "Durasi kontrak + 3 tahun", berlabel USULAN dan bersumber dari tabel rekaman SNX-OPS-SOP-01 pada lingkup rekaman rencana proyek (U-13).
   - Fakta tanpa kutipan sumber langsung, semuanya berlabel USULAN atau tercatat sebagai open item: pembagian pelaku di Peran dan butir 4.1 sampai 4.5, 4.9, 4.10, 4.13 (U-04 sampai U-09); arti tim pelaksana (U-02); lokasi dan pemilik rekaman (U-12); pengecualian cakupan (U-01); klasifikasi formulir terisi (U-03).
   - Yang saya periksa ulang dan koreksi: nomor butir SNX-COM-SOP-01 untuk klasifikasi awalnya tertulis 4.14 di draf, benar 4.13 (diperbaiki di butir 4.14 dan di Dokumen Terkait); status "belum ada" untuk dokumen tetangga tidak dipakai (SNX-COM-FRM-01 ditulis tanpa klaim keberadaan; isinya dicatat paralel di OI-7). Tugas Service Delivery Manager menyebut pemenuh komitmen awalnya hanya ada di Peran dan Cara Mengisi tanpa butir; dipindah ke butir 4.10 agar tercakup label USULAN di butir 4.15.
   - Tidak diukur: judul klausul ISO terhadap teks standar (OI-10); isi sheet Checklist G1 langsung dari Drive (dibaca dari salinan audit); isi SNX-COM-FRM-01 final (OI-7). Tidak ada angka yang saya klaim tanpa pengukuran.

## Putaran perbaikan 1 (dari qa/COM-FRM-02.verify.r1.json)

Hanya specs/COM-FRM-02.json dan notes/COM-FRM-02.md yang diubah. Butir yang diubah:

| Temuan | Perubahan | Lokasi |
|---|---|---|
| Pemblokir: dua pemilik, hanya satu di Peran | Dibedakan: COO = pemilik dokumen (formulir kosong), sesuai blok Identity (Process Owner Direktur = COO di badan); VP Commercial = pemilik formulir terisi dan penetap lokasi rekaman. Keduanya ditulis di baris Peran masing-masing dengan label (USULAN) dan sama dengan baris Rekaman ("Pemilik formulir terisi: VP Commercial (USULAN)"). Acuan ISO 7.5.3 menyebut "formulir terisi" | Peran (COO, VP Commercial); Rekaman baris 1; Acuan ISO 7.5.3 |
| Departemen sebagai pelaku; penetap struktur kolom tidak sama | Butir 4.15 dan Kesimpulan: COO menetapkan struktur kolom; Kesimpulan menambah VP Commercial menetapkan lokasi rekaman. Butir 4.7 dan baris COO: "VP Commercial dan COO" menggantikan "Commercial dan COO" (POL-OPS-001 menulis Commercial; pemetaan ke VP Commercial tetap berlabel USULAN di baris VP Commercial). Tugas COO menetapkan struktur kolom ditambahkan di baris COO | Butir 4.7, 4.15; Peran (COO); Kesimpulan |
| Pasif tanpa pelaku | Ruang Lingkup: "Business Development tidak memakai formulir ini untuk butir berikut (USULAN)". Butir 4.4: "Bila ada SNX-COM-FRM-01 yang terisi untuk order handover ini, Business Development memakai ...". Butir 4.8: "Business Development menulis dependency akses sebagai kebutuhan, tanpa kredensialnya" | Ruang Lingkup; butir 4.4, 4.8 |
| Quotation melingkar | "Penawaran harga SINUX kepada customer. Pengendaliannya ada di SNX-COM-SOP-02." | Definisi |
| Sinonim paket G1 | Dokumen Terkait SNX-OPS-SOP-01 memakai "penerimaan paket handover" | Dokumen Terkait |
| Label tinjauan tahunan | Baris COO: "Meninjau formulir ini setiap tahun (USULAN)" | Peran |
| Benda sebagai pelaku | Tujuan: "Formulir ini memuat isi handover ..."; Acuan ISO 8.2.3: "Tabel 9 memuat perbedaan antar dokumen" | Tujuan; Acuan ISO |

Uji ulang sesudah perubahan: render tanpa galat; `python3 -I tools/lint_doc.py ... generic` pass true, fails kosong, warn 11 butir USULAN (lint.out.txt); validator OOXML "All validations PASSED!" (validate.out.txt); PDF 16 halaman, tiap halaman berisi teks di luar header dan footer (pdf-pages.out.txt: halaman 1 sampul 15 kata, halaman lain 45 sampai 382 kata); pemeriksaan teks nol em-dash, en-dash, kutip ganda, frasa terlarang, meta penyusunan, rujukan internal AI, dan nol sel data terisi di Tabel 1 sampai Tabel 12 (extra-checks.out.txt).

## Sweep

Butir 1 (cakupan isian Business Development: Peran dan butir 4.1 menyebut Tabel 1 sampai Tabel 10, Cara Mengisi menyebut Tabel 1 sampai Tabel 11). Disatukan: Tabel 1 sampai Tabel 10 diisi sebelum handover meeting, Tabel 11 sesudahnya. Tidak ada fakta, angka, atau nama baru.

| Lokasi | Sebelum | Sesudah |
|---|---|---|
| Butir 4.1 | "Business Development mengisi Tabel 1 sampai Tabel 10 sesudah closing dan sebelum handover meeting. Dokumen closing sudah lengkap pada saat itu (SNX-COM-SOP-01 butir 4.16)." | "Business Development mengisi Tabel 1 sampai Tabel 10 sesudah closing dan sebelum handover meeting, lalu mengisi Tabel 11 sesudah handover meeting. Dokumen closing sudah lengkap sebelum handover meeting (SNX-COM-SOP-01 butir 4.16)." |
| Peran, baris Business Development | "Mengisi Tabel 1 sampai Tabel 10, mencatat hasil handover meeting dan penolakan paket handover di Tabel 11, dan melengkapi paket handover yang ditolak (...)" | "Mengisi Tabel 1 sampai Tabel 10 sebelum handover meeting dan Tabel 11 sesudahnya (hasil handover meeting dan penolakan paket handover), serta melengkapi paket handover yang ditolak (...)" |
| Cara Mengisi, kalimat pembuka | "Business Development mengisi Tabel 1 sampai Tabel 11 menurut petunjuk berikut." | "Business Development mengisi Tabel 1 sampai Tabel 10 sebelum handover meeting dan Tabel 11 sesudahnya (butir 4.1), menurut petunjuk berikut." |

Catatan: teks butir 1 di berkas instruksi sweep terpotong di awal ("kupan isian ..."); saya membacanya sebagai cakupan isian Business Development dan hanya mengubah tiga kalimat di atas. Bila yang dimaksud lain, mohon dikirim ulang. Butir 4.1 tetap tercakup label USULAN di butir 4.15.

Uji sesudah sweep (bukti di /tmp/pen-COM-FRM-02/): render tanpa galat; lint_doc generic pass true, fails kosong, warn 11 butir USULAN (lint.out.txt); validator OOXML "All validations PASSED!" (validate.out.txt); `python3 -I reports/orch/blankscan.py` memberi "ok 16 COM-FRM-02.docx []" (blankscan.out.txt).


## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A7 Identity | Process Owner "Direktur" | Process Owner "VP Commercial" |
| A7 Peran, baris VP Commercial | "... (butir 4.11). Pemilik formulir terisi (USULAN, bagian Rekaman) ..." | Ditambah "Pemilik dokumen ini menurut blok Identity (USULAN) dan meninjau formulir ini setiap tahun (USULAN)." sebelum kalimat pemilik formulir terisi |
| A7 Peran, baris COO | "Pemilik dokumen (formulir kosong) menurut blok Identity (USULAN). Meninjau formulir ini setiap tahun (USULAN). Menetapkan struktur kolom (butir 4.15)." | "Menetapkan struktur kolom (butir 4.15)." |
| A7 Kesimpulan | "VP Commercial menetapkan lokasi rekaman, dan COO meninjau formulir ini setiap tahun (USULAN)." | "VP Commercial menetapkan lokasi rekaman dan meninjau formulir ini setiap tahun (USULAN)." |

Butir 3 (A3): tidak ada atasan atau garis lapor JA-03/JA-04 di dokumen ini; tidak diubah. Kalimat "COO menetapkan struktur kolomnya" tetap (bukan butir pemilik dokumen).

Open item ditutup atau diubah:
- OI-3 (pemilik dokumen Direktur vs VP Commercial) dan U-11 (COO sebagai pemilik dokumen dan peninjau tahunan): ditutup W9 (A7). COO tetap penetap struktur kolom.

R2: tidak ada perubahan spec untuk dokumen ini; hanya baris open item dan USULAN yang ditandai ditutup atau diubah W9 (butir 3).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Peran, baris VP Commercial: "Pemilik dokumen ini menurut blok Identity (USULAN) dan meninjau form ini setiap tahun (USULAN). Pemilik form terisi (USULAN, bagian Record) dan menetapkan lokasi record-nya." Ditulis ulang satu kalimat dengan satu label di akhir butir (STYLE §3.5); ketiga usulan tetap tercakup.
### W10 kalimat dihapus atau dipindah
- Peran, kalimat pengantar, catatan pemetaan dipindah ke sini: "Service Delivery Manager dan Project Manager adalah jabatan usulan tanpa pemegang di sana (butir K-10)." Fakta yang sama tetap tertulis di Dokumen Terkait baris SNX-HR-ORG-01.
- Peran, rujukan penunjuk dihapus: "(butir 4.1 sampai 4.5, 4.10, 4.12)" (Business Development), "(butir 4.6)" dan "(butir 4.10, 4.11)" (Service Delivery Manager), "butir 4.9;" (Project Manager), "(butir 4.15)" (COO, diganti fakta "struktur kolom Tabel 1 sampai Tabel 12").
- Cara Mengisi, kalimat pengantar: rujukan "(butir 4.1)" dihapus.
- Rekaman, baris form terisi: "Klasifikasi menurut butir 4.14." diganti fakta "Klasifikasi RESTRICTED (Internal)."; catatan penyusunan "Angka berasal dari record rencana proyek dan checklist G1 di SNX-OPS-SOP-01; perluasan ke form ini belum diputus." ditulis ulang menjadi dasar usulan di sel yang sama: retensi mengikuti record rencana proyek dan checklist G1 di SNX-OPS-SOP-01, perluasannya ke form ini masih usulan.
- Acuan ISO: "Tabel Record" diganti "Tabel Rekaman" mengikuti heading.
### W10 selisih angka
nihil (subst_diff build kosong).
### W10 catatan
- Sebutan pihak luar: customer (sama dengan semua dokumen Commercial).
- Calque diperbaiki 5, plus "sudah ia terima" di butir 4.13. "antar dokumen" ditulis "antardokumen".
- Lebar tabel Peran, Cara Mengisi, pengecualian, dan Definisi disetel ke total 16 cm; min_row_cm 0,8 pada Tabel 3 sampai Tabel 10 dan 1,2 pada Tabel 12 agar cukup untuk tulisan tangan. Halaman tetap 16, ISI tetap mulai halaman 10.

### W10 koreksi worker (temuan nonblocking qa/COM-FRM-02.w10.json)
- Tabel Rekaman: kalimat pengganti rujukan "Klasifikasi menurut butir 4.14" membawa label butir asal: "Klasifikasi form terisi RESTRICTED (Internal) (USULAN)."
