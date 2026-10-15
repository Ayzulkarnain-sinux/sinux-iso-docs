# Catatan penyusun FAT-SOP-04: Financial Document Control & Retention

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-SOP-04.json. Mode sop, aksi T2, wave W4, nomor SNX-FAT-SOP-04 (nomor SNX lama dipertahankan), department "Finance, Accounting & Tax", classification "INTERNAL", audit_class kosong. Approval persis dari config/defaults.json: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Finance Lead" (jabatan tanpa nama), alasan di bagian Asumsi butir A1.

Hasil uji terakhir (bukti mentah: /tmp/pen-FAT-SOP-04/lint.out.txt, /tmp/pen-FAT-SOP-04/validate.out.txt, /tmp/pen-FAT-SOP-04/extra-checks.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-SOP-04.json /tmp/pen-FAT-SOP-04/FAT-SOP-04.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-SOP-04/FAT-SOP-04.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "37 butir (USULAN) menunggu ACC" (sesudah putaran sweep). Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!" (diulang sesudah putaran sweep). `python3 -I reports/orch/blankscan.py /tmp/pen-FAT-SOP-04/FAT-SOP-04.docx` sesudah sweep: "ok 15" (tanpa halaman kosong).
- soffice ke PDF: 15 halaman. Diagram /tmp/pen-FAT-SOP-04/FAT-SOP-04_flow.png dilihat: sembilan simpul, rankdir TB, satu cabang putus-putus, teks terbaca. Montase halaman dilihat: tata letak sesuai template, tabel dan diagram tidak terpotong.
- Pemeriksaan tambahan atas spec (skrip python3 -I di folder scratchpad sesi, bukan di repo): nol em-dash dan en-dash; nol tanda kutip ganda dan nol tebal di isi; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir) dan nol frasa meta proses (dokumen sumber, sumber tim, penyusun, draf ini, versi tim); nol "komersil", "diagnosa", "hutang", "CEO", "COO", "HR Lead"; langkah terpanjang 19 kata (batas 25); semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode SNX di badan ada di tabel Dokumen terkait; tidak ada "Lead" atau "tim" tanpa keterangan.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas config, control, tools, template, reference, ledger.json, out, qa tidak diubah. Berkas yang saya tulis hanya specs/FAT-SOP-04.json dan notes/FAT-SOP-04.md; hasil render hanya di /tmp/pen-FAT-SOP-04/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx (158648 byte) | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io | 2026-10-13T06:09:00Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content, teks penuh Bagian 1 sampai 10 |
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content, teks penuh 15 jabatan. download_file_content tidak dipakai: yang dibutuhkan hanya teks |
| 1. SOP Billing and Invoicing (Google Doc, 139861 byte), sumber pendukung di luar daftar prompt | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI | 2026-10-14T08:06:56.942Z (get_file_metadata hari ini, sama dengan notes/FAT-SOP-01.md) | read_file_content, hanya baca. Dipakai karena memuat satu-satunya ketentuan arsip dan retensi FAT yang tertulis (Bagian 8.2) dan akses folder (7.1). Bila LEAD tidak menghendaki sumber ini, butir yang bergantung padanya: angka 10 tahun, struktur folder Tahun / Nama Klien / Nomor Invoice, pemusnahan dengan Berita Acara dan persetujuan Finance Lead dan Direktur Utama, akses personel FAT dan Direktur Utama (butir 4.4, 4.5, 4.8, 4.9) |
| Kriteria penerimaan | config/checklist.json baris 26 ("SOP Financial Document Control & Retention", checked false, tanpa link, tanpa kolom ISO) | ekspor 2026-10-14T19:05:35Z, modifiedTime checklist 2026-10-14T17:47:13.611Z | Description: "SOP ini menjelaskan pengarsipan dokumen baik hardcopy maupun softcopy" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md (PRO-01, bagian 5 dari baris 1099), context/audit/iso-sinux-supdocs-hr-2026-10-14.md (HR-JA-001, bagian 5 dari baris 1232), context/audit/iso-sinux-supdocs-fat-2026-10-14.md (SOP Billing, bagian 5 butir 11 sampai 13) | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran dan nama jabatan | specs/HR-ORG-01.json (DONE): daftar jabatan, matriks peran, butir K-13 | repo kerja | Dibaca; nama peran dipakai persis |
| Pembanding dokumen FAT | specs/FAT-SOP-01.json (DONE), specs/FAT-SOP-05.json dan notes/FAT-SOP-05.md (LINT_PASS), specs/ISMS-PRO-01.json, specs/ISMS-SOP-03.json, specs/HR-JA-01.json | repo kerja | Dibaca sebagai DATA untuk menyelaraskan istilah, butir yang dirujuk, dan SLA. Kutipan dari spec lain bisa basi bila dokumen itu berubah. Tabel Pelaporan SOP Tax (1 hari, Lead) saya kutip dari notes/FAT-SOP-05.md, berkasnya sendiri (1iMKby6u4X8MYyGlrC5qz73D0y2anOv87) tidak saya buka |
| Status baris terkait | config/checklist.json baris 31 (Financial Document Register: checked false), config/worklist.json (HOLD-T3 tanpa key), CONTEXT-PACK-v19 (menyebut "on review") | repo kerja | Dasar penulisan "belum bernomor" untuk Financial Document Register |

Kalimat perintah kepada AI di sumber: nihil. Sumber memuat kalimat kewajiban untuk karyawan (misalnya "wajib"), itu isi SOP, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Softcopy dokumen penagihan disimpan sebagai PDF di folder Google Drive Departemen FAT dengan struktur folder Tahun / Nama Klien / Nomor Invoice (butir 4.4, 6.2) | "Seluruh berkas penagihan (Invoice, e-Faktur, PKS, PO, BAST) wajib disimpan dalam format digital (.pdf) di folder Google Drive Departemen FAT." dan "Struktur penamaan folder wajib menggunakan format: [Tahun] / [Nama Klien] / [Nomor Invoice]." (8.2) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| Hardcopy diberi label pada sampul atau halaman pertama (butir 4.3, 6.3) | "Media fisik dan kertas" / "Label pada sampul atau halaman pertama" (Bagian 5, tabel Pelabelan, sel Media dan sel Cara pelabelan) | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| Dokumen penagihan dan bukti perpajakan disimpan minimal 10 tahun, lalu dimusnahkan dengan Berita Acara dan persetujuan Finance Lead dan CEO (butir 4.8, 4.9) | "Seluruh arsip dokumen penagihan dan bukti perpajakan wajib disimpan selama minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001." dan "Setelah masa retensi berakhir, pemusnahan dokumen wajib dicatat dalam Berita Acara Pemusnahan Dokumen dengan persetujuan Finance Lead dan CEO." (8.2; penanda tebal pada "10 (sepuluh) tahun" dibuang dari kutipan) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber (fileId) dan posisi |
|---|---|---|---|
| 1 | Tingkat RESTRICTED mencakup domain finance (butir 4.2) | "Hanya untuk peran atau tim yang membutuhkan; dipecah per domain: ops, commercial, legal, hr, finance" | 1h5Pt..., Bagian 4, baris RESTRICTED |
| 2 | Cakupan PRO-01 baru Divisi Operation, jadi penerapan ke FAT = USULAN (butir 4.2) | "Berlaku untuk semua informasi yang dibuat, diterima, disimpan, atau diproses oleh personel Divisi Operation dan pihak ketiga yang bekerja atas nama SINUX, dalam bentuk apa pun: dokumen, spreadsheet, email, chat, tiket, log, konfigurasi, backup, database, rekaman, dan kertas." | 1h5Pt..., Bagian 2 |
| 3 | Label folder Drive (butir 4.3) | "Nama folder atau deskripsi menyebut tingkat; izin akses sesuai tingkat" | 1h5Pt..., Bagian 5, baris Folder Drive |
| 4 | RESTRICTED disimpan di sistem resmi dengan akses terbatas (butir 4.5) | "Sistem resmi dengan akses terbatas per peran" | 1h5Pt..., Bagian 6, baris Penyimpanan |
| 5 | Pencetakan RESTRICTED (butir 4.6) | "Seperlunya, diambil langsung dari printer, tidak ditinggal" | 1h5Pt..., Bagian 6, baris Cetak |
| 6 | Pemusnahan RESTRICTED: hancurkan kertas, hapus aman softcopy (butir 4.9) | "Hapus aman; kertas dihancurkan" | 1h5Pt..., Bagian 6, baris Pemusnahan |
| 7 | Pembagian ke pihak luar (bagian 9) | "Butuh NDA atau kontrak yang berlaku dan persetujuan pemilik informasi" | 1h5Pt..., Bagian 6, baris Berbagi ke pihak luar |
| 8 | Pengecualian harus tertulis, berbatas waktu, disetujui dua peran (bagian 9) | "Pengecualian hanya sah bila tertulis, berbatas waktu, disetujui pemilik informasi dan ISMS Coordinator." | 1h5Pt..., Bagian 9 |
| 9 | Pelanggaran penanganan dilaporkan sebagai event keamanan (bagian 9) | "Pelanggaran penanganan informasi RESTRICTED atau SECRET dilaporkan sebagai event keamanan sesuai SNX-ISMS-SOP-01 dan ditindak sesuai kebijakan disipliner perusahaan." | 1h5Pt..., Bagian 9 |
| 10 | Pemilik informasi menetapkan klasifikasi (butir 4.10, definisi) | "Pemilik informasi (pemilik aset pada SNX-ISMS-REG-01) menetapkan klasifikasi saat informasi dibuat atau diterima." | 1h5Pt..., Bagian 4, Aturan penentuan |
| 11 | Akses folder FAT hanya personel FAT dan Direktur Utama; dokumen keuangan dinyatakan rahasia (butir 4.2, 4.5) | "Akses terhadap folder Google Drive FAT dan Register Penagihan di Google Sheets dibatasi secara ketat hanya untuk personel FAT dan CEO." dan "Seluruh dokumen keuangan, daftar harga (rate card), data tagihan klien, dan informasi rekening bank diklasifikasikan sebagai dokumen Rahasia (Confidential)." (penanda tebal dibuang) | 1sZfT..., 7.1 |
| 12 | Bukti potong dari klien diterima FAT (scope) | "Tim Finance wajib mencatat estimasi pemotongan PPh Pasal 23 pada Register Penagihan dan melakukan rekonsiliasi saat Bukti Potong (Bupot) diterima dari klien." | 1sZfT..., 5.2 |
| 13 | Perubahan atau pembatalan invoice dicatat dengan alasan dan bukti persetujuan (bagian 9) | "Setiap perubahan nominal, revisi tanggal, atau pembatalan invoice yang telah disetujui wajib dicatat alasan perubahan beserta bukti persetujuannya dalam sistem pengarsipan." | 1sZfT..., 4.2 |
| 14 | Hardcopy ada di FAT: berkas fisik hanya bila PKS mensyaratkan; BAST ditandatangani dua pihak (bahan butir 4.1) | "Pengiriman berkas fisik (cetak resmi bertanda tangan dan berstempel) melalui kurir hanya dilakukan jika secara eksplisit dipersyaratkan dalam PKS / Kontrak dengan klien." dan "Bukti formal penyelesaian pekerjaan atau penyerahan jasa yang telah ditandatangani oleh kedua belah pihak." | 1sZfT..., 5.3 dan 8.1 |
| 15 | Jenis dokumen keuangan lain (scope) | "Memeriksa kelengkapan payment request dan kesesuaian dengan persetujuan." (JA-10 A.4); "Memverifikasi bukti pembayaran aktual untuk eligible collection SIP." (JA-10 A.3); "Menyusun laporan kas dan exception pembayaran berkala." (JA-10 A.7); "Menyusun laporan keuangan dan analisis varians." (JA-11 A.3) | 1m91W..., JA-10 dan JA-11 bagian A |
| 16 | Accounting & Tax menjaga kelengkapan faktur, bukti potong, arsip akuntansi (bahan peran Finance Staff dan Finance Lead, belum dipetakan) | "Mengendalikan kelengkapan faktur, bukti potong dan arsip akuntansi." (JA-11 A.6); "Memelihara arsip, retensi dokumen dan kontrol akses sesuai kebijakan." (JA-12 A.5, arsip HR, tidak dipakai di badan dokumen) | 1m91W... |
| 17 | SLA pengarsipan bukti lapor 1 hari, Lead (bagian 8) | Tabel IV SOP Tax baris 5: "Pelaporan" / "Pengarsipan dokumen bukti lapor (BPE, SPT, Kode billing dan bukti bayar)" / "1 day" / "Lead" (kutipan dari notes/FAT-SOP-05.md, berkas Drive tidak dibuka) | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| 18 | Kriteria baris | "SOP ini menjelaskan pengarsipan dokumen baik hardcopy maupun softcopy" (config/checklist.json baris 26) | tidak berlaku |

## 3. Pemetaan kriteria (Description baris 26)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| SOP menjelaskan pengarsipan dokumen | Purpose kalimat 1; Scope; butir 4.1 sampai 4.9; bagian 6.1 sampai 6.4; rekaman bagian 11 | Sumber 1sZfT... 8.2 untuk dokumen penagihan dan bukti perpajakan; sisanya (USULAN) |
| hardcopy | Definisi Hardcopy dan Tempat simpan hardcopy; butir 4.1, 4.3, 4.5, 4.6, 4.7; bagian 6.3 (label, simpan, catat); bagian 6.4 langkah 4 dan 7; baris rekaman Hardcopy | Label dan cetak dari PRO-01; langkah simpan dan catat (USULAN); lokasi fisik tidak ada di sumber (OI-1) |
| softcopy | Definisi Softcopy dan Folder arsip FAT; butir 4.1, 4.3, 4.4, 4.5; bagian 6.2; bagian 6.4 langkah 5; baris rekaman Softcopy | Sumber 1sZfT... 8.2 dan 7.1 |

Pemetaan klausul ISO (bagian 11, satu label "(USULAN, perlu konfirmasi konsultan)"; checklist tidak memberi acuan klausul untuk baris ini). Judul klausul adalah pengetahuan standar, bukan teks sumber:

| Klausul | Butir | Alasan |
|---|---|---|
| ISO 9001:2015 7.5.3 | 4.1, 4.4, 4.7, 4.8 | Pengendalian informasi terdokumentasi: penyimpanan, akses, retensi, pemusnahan. PRO-01 memakai klausul ini; SOP Billing tidak memetakan 7.5 (cacat butir 13) |
| ISO/IEC 27001:2022 Annex A 5.12, 5.13 | 4.2, 4.3 | Klasifikasi dan pelabelan; PRO-01 memakai keduanya |
| Annex A 5.15 | 4.5 | Kontrol akses. Tidak ada di header PRO-01; dipakai juga di specs/FAT-SOP-01.json |
| Annex A 5.33 | 4.8 | Perlindungan rekaman; SOP Billing menyebut A.5.33 untuk catatan keuangan |
| Annex A 7.10 | 4.6 | Media penyimpanan; PRO-01 memakainya untuk baris Cetak |
| Annex A 8.10 | 4.9 | Penghapusan informasi; PRO-01 memakainya untuk baris Pemusnahan |

Annex A 8.12 dari Bagian 3 PRO-01 tidak dipakai (lihat penanganan cacat).

## 4. Penanganan cacat context/audit

| Berkas sumber | Cacat tercatat | Penanganan |
|---|---|---|
| PRO-01 (isms audit, bagian 5) | Cakupan Bagian 2 hanya Divisi Operation; divisi lain, termasuk FAT, tidak disebut | Klasifikasi FAT memakai tingkat PRO-01 dengan label (USULAN) di butir 4.2; U-05 dan OI-3 |
| PRO-01 | Annex A 8.12 ada di Bagian 3 tetapi tidak di header; di SoA 8.12 belum dipetakan | 8.12 tidak dipakai di dokumen ini |
| PRO-01 | A 5.33 ada di header tetapi tidak ada bagian isi yang membahas perlindungan record secara eksplisit; SoA memetakannya ke baris Retensi | 5.33 dipakai hanya untuk butir 4.8 (retensi), dengan label klausul (USULAN) |
| PRO-01 | Retensi merujuk "master list" tanpa nomor; kesamaan dengan SNX-OPS-ML-00 adalah inferensi audit | Retensi FAT tidak bersandar pada master list. Dasarnya SOP Billing 8.2. Daftar masa simpan per jenis dokumen FAT jadi OI-6 |
| PRO-01 | Pemeriksa di Pengesahan "ISO/ISMS Coordinator", Bagian 8 "ISMS Coordinator" | Dipakai "ISMS Coordinator", sama dengan matriks peran SNX-HR-ORG-01 |
| PRO-01 | Label SECRET pada email, label KB hanya tiga nilai, tidak ada target KPI, tidak ada bagian definisi | Tidak menyangkut arsip dokumen keuangan; tidak dibawa. Bagian definisi ada di dokumen ini |
| PRO-01 | (Dari teks Drive) tulisan "komersil" di Bagian 7 | Tidak dibawa; tidak ada kata itu di spec |
| JA-001 (hr audit, bagian 5) | Tidak ada jabatan Finance Lead atau Finance Staff; hanya JA-10 Finance dan JA-11 Accounting & Tax | Nama peran dipakai apa adanya, status "Belum dipetakan (K-13)" di tabel peran, OI-4 |
| JA-001 | Frasa kompetensi janggal (sisa penggantian kata otomatis) | Tidak ada frasa itu yang dipakai. Kutipan Uraian Jabatan di bagian 2 dan 3 di atas dicek bersih |
| JA-001 | Ejaan "Kristianto" dan sebutan CEO | Approval memakai "Samuel Kristanto Utomo / President Director" (template, data_conflicts); badan dokumen tidak menyebut nama dan memakai "Direktur Utama" |
| JA-001 | Batas wewenang tidak berangka dan identik di semua jabatan | Kolom Authority Finance Lead merujuk "delegasi tertulis yang berlaku (SNX-HR-ORG-01)", tanpa angka |
| SOP Billing (fat audit, bagian 5 butir 11) | Persetujuan pemusnahan hanya Finance Lead dan CEO; tidak ada pengganti Finance Lead | Direktur Utama menyetujui bersama Finance Lead (butir 4.9). Pengganti Finance Lead tidak dikarang: OI-15 |
| SOP Billing (butir 12) | Dokumen keuangan berlabel "Rahasia (Confidential)", bukan tingkat PRO-01 | Dipetakan ke RESTRICTED (Internal), (USULAN) di butir 4.2 |
| SOP Billing (butir 13) | Pemetaan klausul 7.5 tidak ada walau ada kontrol arsip dan retensi | Klausul 7.5.3 ditambahkan di bagian 11 (USULAN) |
| SOP Billing (butir 3) | "CEO" dan ejaan nama | "Direktur Utama" sesuai data_conflicts |

## 5. Asumsi

| # | Asumsi | Alasan |
|---|---|---|
| A1 | process_owner = "Finance Lead" | Dokumen ini tidak punya berkas sendiri. "Pemilik dokumen" di kedua sumber menunjuk dokumen lain (PRO-01: ISMS Coordinator; Job Analysis: HR Lead, dengan Aziz = HR Manager menurut data_conflicts). Aturan defaults: dokumen tanpa sumber memakai jabatan reviewer departemen, yaitu Finance Lead. Status USULAN (U-18) |
| A2 | Finance Lead dan Finance Staff dipakai sebagai nama peran | Ada di matriks peran SNX-HR-ORG-01 dengan status belum dipetakan; sama dengan SNX-FAT-SOP-01 dan SNX-FAT-SOP-05 |
| A3 | "CEO" di SOP Billing = Direktur Utama | data_conflicts: sebutan Samuel di badan dokumen "Direktur Utama", termasuk saat sumber menulis CEO |
| A4 | "bukti perpajakan" di SOP Billing 8.2 = dokumen perpajakan dan bukti potong dari klien | Padanan istilah; dokumen perpajakan diatur SNX-FAT-SOP-05 |
| A5 | Dokumen perpajakan diarsipkan Finance Lead | SNX-FAT-SOP-05 menunjuk Finance Lead untuk langkah pengarsipan di butir 6.5 dan menyebut SOP ini sebagai acuan. Dokumen penagihan diarsipkan Finance Staff seperti di SNX-FAT-SOP-01 butir 4.12. Untuk dokumen perpajakan, Finance Lead menjalankan butir 6.1 sampai 6.3, dengan langkah simpan dan catat yang berpelaku Finance Lead di 6.2 dan 6.3; pelaku berbeda menurut jenis dokumen (OI-10) |
| A6 | Ejaan "hardcopy" dan "softcopy" | Mengikuti kata di Description checklist; SOP Billing menulis "hard copy" dan "soft copy" |
| A7 | "folder Google Drive Departemen FAT" disebut "Folder arsip FAT" | Satu istilah di seluruh dokumen, didefinisikan di bagian 3 |
| A8 | Finance Lead bertindak sebagai Pemilik informasi untuk dokumen keuangan | Pemilik informasi menurut PRO-01 = pemilik aset di SNX-ISMS-REG-01; register itu belum memuat aset FAT. USULAN |
| A9 | Financial Document Register ditulis "belum bernomor SNX" dan tidak dinyatakan ada atau tidak ada | Checklist baris 31 kini tanpa tanda ada, worklist tidak memberinya key (OI-5) |

## USULAN

37 kemunculan label (USULAN) di spec sesudah putaran sweep (satu kemunculan adalah baris definisi label itu sendiri), dikelompokkan jadi 19 butir. Pemutus yang disarankan memakai kelompok dari RUNBOOK §11.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U-01 | Dokumen keuangan lain (payment request, bukti pembayaran, laporan kas, laporan keuangan) dan bukti potong dari klien masuk cakupan pengarsipan | Scope; rekaman bagian 11 (baris 1 dan 3) | FAT |
| U-02 | Pengecualian cakupan: pembuatan dan penerbitan dokumen, dokumen non-keuangan (legal), backup Drive. Sumber diam; diturunkan dari kriteria baris | Scope | FAT; Legal untuk dokumen legal |
| U-03 | Definisi Hari = hari kerja (sama dengan SNX-FAT-SOP-05) | Definisi | FAT |
| U-04 | Dokumen kertas juga diarsipkan sebagai hardcopy | Butir 4.1; bagian 6.3 | Legal dan FAT |
| U-05 | Penerapan SNX-ISMS-PRO-01 ke FAT dan tingkat RESTRICTED (Internal) untuk dokumen keuangan; cakupan PRO-01 baru Divisi Operation | Butir 4.2 | owner |
| U-06 | Finance Lead menetapkan struktur folder untuk dokumen perpajakan dan dokumen keuangan lain | Butir 4.4; rekaman baris 2 dan 3 | FAT |
| U-07 | Finance Lead menyetujui penambahan akses ke Folder arsip FAT; Tempat simpan hardcopy hanya dibuka personel FAT | Butir 4.5 | FAT |
| U-08 | Pencatatan hardcopy di Financial Document Register | Butir 4.7; bagian 6.3 langkah 3; Dokumen terkait | FAT |
| U-09 | Retensi 10 tahun diperluas ke dokumen keuangan lain (angka sumber hanya untuk dokumen penagihan dan bukti perpajakan) | Butir 4.8; rekaman baris 3 dan 4 | FAT dan Legal |
| U-10 | Masa retensi dihitung sejak tanggal dokumen | Butir 4.8 | Legal |
| U-11 | Penetapan tugas Finance Staff di butir 4.1 sampai 4.9 dan 6.1 sampai 6.4 (label ada di tabel peran); pemilik rekaman dan Pemilik informasi Finance Lead; pemilik Financial Document Register Finance Staff | Tabel peran (baris Finance Staff dan Finance Lead); butir 4.10; bagian 11 | owner |
| U-12 | Langkah memindai dokumen kertas menjadi PDF | Bagian 6.2 langkah 1 | FAT dan Legal |
| U-13 | Pemeriksaan dokumen yang masa retensinya berakhir setiap tahun | Bagian 6.4 langkah 1; SLA baris 3 | FAT |
| U-14 | SLA 1 hari sejak dokumen diterima atau dibuat untuk dokumen penagihan dan dokumen keuangan lain; titik mulai hitung 1 hari bukti lapor ("sejak bukti lapor terbit"); perluasan 1 hari bukti lapor ke bukti potong | SLA baris 1 dan 2 | FAT |
| U-15 | Cabang dokumen tidak lengkap: Finance Staff meminta dokumen yang kurang dan menunda pengarsipan | Bagian 9 baris 1; keterangan diagram | FAT |
| U-16 | Cara Finance Lead memeriksa kepatuhan (mencocokkan hardcopy dengan register, memeriksa struktur folder) | Kesimpulan | FAT |
| U-17 | Daftar klausul ISO 9001:2015 dan ISO/IEC 27001:2022 (label "(USULAN, perlu konfirmasi konsultan)") | Bagian 11, Acuan standar | konsultan lewat owner |
| U-18 | process_owner Finance Lead | Identity | owner |
| U-19 | Finance Staff sebagai pengaju pengecualian dari aturan SOP ini (PRO-01 hanya menyebut pemilik informasi dan ISMS Coordinator sebagai penyetuju) | Bagian 9 baris 4 | FAT |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-1 | Lokasi, bentuk (lemari atau ruang), pengelola, dan akses Tempat simpan hardcopy FAT tidak ada di sumber. Job Analysis JA-12 menyebut HRGA Officer mengelola fasilitas dan inventaris kantor, tetapi tidak menyebut arsip FAT | FAT; Aziz bila fasilitasnya lewat HRGA |
| OI-2 | Dasar hukum angka 10 tahun: SOP Billing menulis "sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001" tanpa pasal; dasar itu tidak dibawa ke dokumen. Perlu konfirmasi angka dan titik awal hitungan | Legal |
| OI-3 | Cakupan SNX-ISMS-PRO-01 baru Divisi Operation; perlu keputusan menjadikannya berlaku untuk FAT | owner |
| OI-4 | Pemetaan Finance Lead, Finance Staff, dan ISMS Coordinator ke jabatan (K-13 di SNX-HR-ORG-01) | owner |
| OI-5 | Financial Document Register: belum bernomor SNX; checklist baris 31 kini tidak bertanda ada (CONTEXT-PACK menulis "on review"); worklist tidak memberi key; kolom isinya belum diketahui. Butir 4.7, 6.3, 6.4 bergantung padanya | FAT; LEAD untuk penomoran |
| OI-6 | Daftar masa simpan per jenis dokumen FAT. PRO-01 menulis retensi "sesuai master list"; master list yang disebut audit (SNX-OPS-ML-00) milik Divisi Operation | FAT |
| OI-7 | Penindakan pelanggaran penanganan di FAT. PRO-01 menunjuk Head of Operation untuk Divisi Operation; untuk FAT tidak ada. Dokumen ini hanya mencantumkan pelaporan event keamanan | owner |
| OI-8 | Penanganan hardcopy hilang atau rusak, termasuk pemulihan dari softcopy: tidak ada di sumber, tidak dikarang | FAT |
| OI-9 | Pembagian dokumen untuk pemeriksaan DJP atau audit eksternal: PRO-01 mensyaratkan NDA atau kontrak untuk RESTRICTED ke pihak luar; apakah berlaku untuk pemeriksaan DJP tidak dinyatakan | Legal |
| OI-10 | Peran pengarsip dokumen perpajakan: SNX-FAT-SOP-05 menunjuk Finance Lead, sedangkan dokumen penagihan ditangani Finance Staff (SNX-FAT-SOP-01). Konfirmasi pembagian ini atau pilih satu pengarsip | FAT |
| OI-11 | Keabsahan hardcopy asli versus hasil pindai untuk dokumen bertanda tangan basah (BAST, PKS): apakah hardcopy asli wajib tetap disimpan | Legal |
| OI-12 | "CEO" di SOP Billing dipetakan ke Direktur Utama sebagai penyetuju pemusnahan; konfirmasi (data_conflicts: konfirmasi owner atau Samuel) | Samuel atau owner |
| OI-13 | Jadwal backup folder Google Drive FAT: SNX-ISMS-SOP-03 menyebut parameter backup dokumen di Drive ditetapkan Lead NOC (USULAN), belum diputus | Fani |
| OI-14 | Ketidakselarasan SNX-FAT-SOP-01 dan SOP ini: SNX-FAT-SOP-01 mencatat lokasi bukti potong dari klien dan Berita Acara Pemusnahan Dokumen sebagai "belum ditetapkan", sedangkan SOP ini menaruh bukti potong dari klien di Folder arsip FAT (USULAN). Rekaman Berita Acara tetap "belum ditetapkan" di keduanya | FAT |
| OI-15 | Pengganti Finance Lead bila tidak hadir saat persetujuan pemusnahan: tidak ada di sumber | owner |
| OI-16 | Kalimat perintah kepada AI di sumber: nihil | tidak ada |
| OI-17 | Masa simpan Berita Acara Pemusnahan Dokumen dan Financial Document Register belum ditetapkan (kolom Retensi di bagian 11 tertulis "Belum ditetapkan"); lokasinya juga belum ditetapkan (OI-14). Bukti pemusnahan tanpa masa simpan; angka tidak dikarang | FAT dan Legal |

## 6. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI:
1. Pasangan "Finance Staff dan Finance Lead" muncul berulang di butir 4.3, 4.4, 4.6, dan 4.7, sehingga terbaca seperti templat. Pasangan itu dipertahankan karena nama peran wajib sama persis dengan tabel bagian 5 dan kedua peran memang mengarsipkan (OI-10). Penyederhanaan hanya mungkin bila FAT memutus satu pengarsip.
2. Kalimat pembuka Purpose "Hasil yang dijaga:" mengikuti pola RUNBOOK §6a.4 dan juga dipakai di dokumen W3, jadi mudah terbaca sebagai pola. Dibiarkan karena memenuhi §6a.4.
3. Kolom output langkah berpola "X dihancurkan", "X terhapus", "X berlabel" pendek dan seragam. Dibiarkan karena satu langkah wajib punya satu rekaman atau keluaran.
4. Daftar jenis dokumen yang panjang (invoice, e-Faktur Pajak, PKS, PO, BAST, bukti potong) berasal dari sumber, bukan pola tiga yang dipaksakan.

Perbaikan teks yang saya lakukan dalam putaran ini: (a) "yang mengetahuinya melaporkannya" diganti "yang mengetahui pelanggaran itu melaporkannya"; (b) "dari arsip" di bagian 9 diganti "dari Folder arsip FAT atau Tempat simpan hardcopy" karena "arsip" berdiri sendiri tidak didefinisikan; (c) butir 4.10 ditulis ulang agar tiga hal yang berstatus USULAN terbaca sebagai daftar, bukan anak kalimat; (d) langkah 6.2 butir 3 dibatasi ke dokumen keuangan lain supaya sama dengan paragraf pembuka 6.1 yang menyerahkan dokumen perpajakan ke Finance Lead; (e) definisi ISMS Coordinator ditambahkan karena peran itu muncul di bagian 5 dan 9; (f) keterangan diagram menyebut Finance Lead untuk dokumen perpajakan; (g) bukti potong dari klien diberi label (USULAN) di scope dan rekaman karena penempatannya di folder penagihan bukan kutipan sumber; (h) tabel peran Finance Lead dipendekkan.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: 10 tahun (SOP Billing 8.2, untuk dokumen penagihan dan bukti perpajakan; perluasan berlabel); 1 hari (SOP Tax lewat notes/FAT-SOP-05.md, untuk bukti lapor; perluasan berlabel); "1 hari sejak dokumen diterima atau dibuat" dan "setiap tahun" berlabel (USULAN). Tidak ada angka lain.
- Nama: tidak ada nama orang di badan dokumen. Nama sistem (Google Drive) dan nama folder (Departemen FAT) dari SOP Billing 8.2. Kode dokumen SNX dari config/worklist.json dan spec yang sudah ada. Hanya nama Samuel di blok Approval, dari config/defaults.json.
- Tanggal: tidak ada.
- Kalimat tanpa kutipan langsung yang saya turunkan sendiri: definisi "Hapus aman" (diambil dari definisi di specs/ISMS-PRO-01.json; docx PRO-01 hanya menulis "Hapus aman; kertas dihancurkan"), contoh pelanggaran "hardcopy ditinggal di printer" (turunan baris Cetak PRO-01, "tidak ditinggal"), dan contoh "auditor eksternal" (SOP Tax menyebut audit eksternal). Ketiganya contoh atau definisi biasa, bukan klaim fakta baru.
- Item yang memang tidak bersumber ditandai (USULAN) di dokumen dan ada di tabel USULAN di atas.

## Sweep

Putaran sweep atas butir dari orkestrator (verify nonblocking 1, 2, 3, 5, 7, 8). Hanya specs/FAT-SOP-04.json dan notes/FAT-SOP-04.md yang diubah. Cadangan sebelum sweep: /tmp/pen-FAT-SOP-04/spec.before-sweep.json dan /tmp/pen-FAT-SOP-04/notes.before-sweep.md.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1 dan verify nb 1: langkah softcopy dokumen perpajakan | Pembuka 6.1: "Finance Lead menjalankan butir yang sama untuk dokumen perpajakan". Kolom PIC di 6.1 sampai 6.3 hanya Finance Staff; tidak ada langkah simpan softcopy dokumen perpajakan | Pembuka 6.1 tetap seperti sebelum sweep (lihat Pembatalan di bawah). Tambah langkah 6.2 butir 4 (Finance Lead): "Simpan PDF dokumen perpajakan di subfolder yang Finance Lead tetapkan (butir 4.4)." Tambah tiga langkah Finance Lead di 6.3 (butir 4 sampai 6): beri label, simpan, dan catat hardcopy dokumen perpajakan |
| verify nb 2: sel SLA baris 2 | "1 hari. Angka ini berasal dari SNX-FAT-SOP-05 untuk bukti lapor; perluasan ke bukti potong adalah (USULAN)" | "1 hari untuk bukti lapor (SNX-FAT-SOP-05), dihitung sejak bukti lapor terbit (USULAN); 1 hari untuk bukti potong (USULAN)" |
| verify nb 3: kalimat meta status draf | Butir 4.2: "Penerapan SNX-ISMS-PRO-01 ke FAT adalah (USULAN), karena cakupan prosedur itu baru Divisi Operation." Butir 4.10: "Penetapan pelaku pada butir 4.1 sampai 4.9, ... berstatus (USULAN)." | Butir 4.2 satu kalimat: "Dokumen keuangan berklasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01, yang cakupannya baru Divisi Operation (USULAN)." Butir 4.10: "Kepemilikan rekaman. Finance Lead menjadi pemilik rekaman di bagian 11 dan Pemilik informasi untuk dokumen keuangan menurut SNX-ISMS-PRO-01 (USULAN)." Label penugasan Finance Staff dipindah ke tabel peran: "..., menurut butir 6.1 sampai 6.4 (USULAN)" |
| verify nb 5: pengaju pengecualian | "Finance Staff mengajukan pengecualian secara tertulis." | "Finance Staff mengajukan pengecualian secara tertulis (USULAN)." Dicatat di U-19 |
| verify nb 7: rumusan retensi hardcopy | "Minimal 10 tahun; untuk dokumen keuangan lain (USULAN)" | "Minimal 10 tahun (dokumen penagihan dan perpajakan); dokumen keuangan lain minimal 10 tahun (USULAN)" |
| verify nb 8: retensi Berita Acara | Hanya OI-14 (lokasi); retensi tidak punya open item | Tambah OI-17 untuk masa simpan Berita Acara Pemusnahan Dokumen dan Financial Document Register. Sel retensi di dokumen tetap "Belum ditetapkan" |

Tidak diubah karena di luar butir sweep: verify nb 4 (pola "Hasil yang dijaga:" di Purpose, lihat bagian 6 pertanyaan 1 dan 2) dan nb 6 (Annex A 7.10 untuk butir 4.6; Annex A 7.7 disebut pemeriksa lebih langsung, sudah berlabel "(USULAN, perlu konfirmasi konsultan)", jadi bahan untuk konsultan).

Uji sesudah sweep (bukti mentah di /tmp/pen-FAT-SOP-04/lint.out.txt, validate.out.txt, blankscan.out.txt, extra-checks.out.txt): render_sop.py selesai tanpa galat; lint_doc.py sop "pass": true, fails kosong, satu warn "37 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan.py "ok 15"; skrip pemeriksaan tambahan: nol em-dash dan en-dash, nol tanda kutip ganda, nol frasa terlarang, langkah terpanjang 19 kata, semua PIC ada di tabel peran, semua kode SNX di badan ada di tabel Dokumen terkait. Percobaan pertama blankscan gagal membaca PDF (pdfinfo tanpa keluaran, kemungkinan bentrok soffice dengan konversi lain); percobaan kedua tanpa perubahan berkas memberi "ok 15".

Pembatalan (perbaikan sweep r1, qa/FAT-SOP-04.sweep.r1.json, pemblokir): sweep pertama mencabut Finance Lead dari butir 6.1 untuk dokumen perpajakan, dari baris Finance Lead tabel peran, dan dari keterangan Gambar 1, padahal tidak ada butir yang memintanya. Tiga perubahan itu dibatalkan dan teksnya kembali persis seperti sebelum sweep:

| Letak | Teks sweep pertama (dibatalkan) | Teks sekarang (sama dengan sebelum sweep) |
|---|---|---|
| Pembuka 6.1 | "Untuk dokumen perpajakan, Finance Lead menjalankan langkah dengan PIC Finance Lead di butir 6.2 dan 6.3, sesuai butir 6.5 SNX-FAT-SOP-05." | "Finance Lead menjalankan butir yang sama untuk dokumen perpajakan, sesuai butir 6.5 SNX-FAT-SOP-05." |
| Tabel peran, baris Finance Lead | "(butir 4.4, 4.5, 4.9, 6.2 sampai 6.4)" | "(butir 4.4, 4.5, 4.9, 6.1 sampai 6.4)" |
| Keterangan Gambar 1 | "Finance Lead menjalankan langkah dengan PIC Finance Lead di butir 6.2 dan 6.3 untuk dokumen perpajakan." | "Finance Lead menjalankan butir 6.1 sampai 6.3 untuk dokumen perpajakan." |

Dipertahankan dari sweep: langkah 6.2 butir 4 dan 6.3 butir 4 sampai 6 (Finance Lead, dokumen perpajakan). Kolom PIC di 6.1 tetap hanya Finance Staff, seperti sebelum sweep; pelaku 6.1 untuk dokumen perpajakan ditunjuk lewat paragraf pembuka dan tetap bagian OI-10. Butir lain di sweep tidak berubah.

Uji sesudah pembatalan (bukti mentah di /tmp/pen-FAT-SOP-04/lint.out.txt, validate.out.txt, blankscan.out.txt, extra-checks.out.txt): render_sop.py tanpa galat; lint_doc.py sop "pass": true, fails kosong, satu warn "37 butir (USULAN) menunggu ACC" (warn PIC SLA nol); validate.py "All validations PASSED!"; blankscan.py "ok 15".
