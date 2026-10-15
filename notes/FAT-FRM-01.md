# Catatan penyusun FAT-FRM-01: Financial Transaction Approval Records

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-FRM-01.json. Mode generic (FORM), aksi T2, wave W7, nomor SNX-FAT-FRM-01 (nomor SNX lama dipertahankan), department "Finance, Accounting & Tax", classification "RESTRICTED (Internal)", audit_class kosong. Approval persis dari config/defaults.json: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Finance Lead" (jabatan reviewer departemen, tanpa nama; asumsi A1). Catatan worklist: kosong.

Hasil uji terakhir (bukti mentah: /tmp/pen-FAT-FRM-01/lint.out.txt, /tmp/pen-FAT-FRM-01/validate.out.txt, /tmp/pen-FAT-FRM-01/extra-checks.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-FRM-01.json /tmp/pen-FAT-FRM-01/FAT-FRM-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-FRM-01/FAT-FRM-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "13 butir (USULAN) menunggu ACC" (hasil sesudah sweep; sebelum sweep 12).
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-FAT-FRM-01/FAT-FRM-01.docx` (sesudah sweep): `ok 11 FAT-FRM-01.docx []`, bukti /tmp/pen-FAT-FRM-01/blankscan.out.txt.
- soffice ke PDF: 11 halaman. Halaman 8 dan 9 (tiga tabel log, tabel Rekaman, tabel Acuan ISO) dilihat sebagai gambar. Putaran pertama memperlihatkan header "No", "Pemohon", dan "Penyetuju" terpotong di kolom sempit; lebar kolom diperbaiki (widths_cm) dan dicek ulang, kini terbaca utuh.
- Pemeriksaan tambahan atas spec (skrip python3 -I di folder scratchpad sesi, bukan di repo; keluaran di extra-checks.out.txt): nol em-dash dan en-dash; nol tanda kutip ganda; nol tebal; nol frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir, hal ini); nol frasa meta proses (dokumen sumber, sumber tim, penyusun, draf ini, versi tim); nol "komersil", "diagnosa", "hutang", "CEO", "COO", "HR Lead"; nol "Lead" tanpa "Finance" di depannya dan nol "tim"; langkah 6.x terpanjang 25 kata (batas 25); semua kode SNX di badan dan semua nama dokumen tanpa nomor ada di bagian Dokumen Terkait; semua sel data di tiga tabel log kosong kecuali kolom No.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas config, control, tools, template, reference, ledger.json, out, qa tidak diubah oleh saya (git status memperlihatkan ledger.json berubah, itu oleh proses lain). Berkas yang saya tulis hanya specs/FAT-FRM-01.json dan notes/FAT-FRM-01.md; hasil render hanya di /tmp/pen-FAT-FRM-01/.

## 1. Sumber

Baris ini tidak punya berkas sumber (checklist baris 30: tanpa link, tanpa fileId). Bahan yang dipakai:

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist tim, baris 30 (kriteria) dan baris 24, 25, 27, 29 (dokumen tetangga) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (ekspor 2026-10-14T19:05:35Z, dari config/checklist.json) | Dibaca dari config/checklist.json; Drive tidak dibuka |
| SINUX_Job_Analysis_2026.docx (51426 byte), HR-JA-001 | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini) | read_file_content, teks penuh; kutipan JA-10 dicocokkan dengan salinan context/audit |
| 6. SOP Tax Administration & Reporting.docx (127108 byte) | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 | 2026-10-13T11:17:33.562Z (get_file_metadata hari ini) | read_file_content, teks penuh; kutipan Tabel IV baris 3 |
| SOP Billing and Invoicing (Google Doc) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI | tidak diukur oleh saya; notes/FAT-SOP-04.md mencatat 2026-10-14T08:06:56.942Z | TIDAK saya buka. Kutipannya saya ambil dari salinan context/audit/iso-sinux-supdocs-fat-2026-10-14.md dan notes/FAT-SOP-04.md; bisa basi bila berkas Drive berubah |
| Catatan cacat dan verdict | context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md (baris 434, 446, 751), iso-sinux-supdocs-fat (bagian 5), iso-sinux-supdocs-hr (bagian 5) | salinan audit 13 sampai 14 Okt | DATA, tidak ada fileId tunggal |
| Peran dan nama jabatan | specs/HR-ORG-01.json (DONE): matriks peran, butir K-13 | repo kerja | Dibaca; nama peran Finance Lead dan Finance Staff dipakai persis |
| Dokumen FAT tetangga | specs/FAT-SOP-01.json, specs/FAT-SOP-04.json, specs/FAT-SOP-05.json, notes/FAT-SOP-04.md | repo kerja | Dibaca sebagai DATA untuk menyelaraskan istilah, lokasi, dan retensi. Kutipan dari spec lain bisa basi bila dokumen itu berubah |

Alat Drive yang dipakai hanya baca (get_file_metadata, read_file_content). Nol penulisan, salin, bagi, atau hapus. Kalimat perintah kepada AI di sumber: nihil. Kalimat kewajiban di sumber (misalnya "wajib") adalah isi SOP untuk karyawan, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemeriksaan kelengkapan permintaan pembayaran dan kewenangan menahan pembayaran yang belum lengkap sudah ada di uraian jabatan Finance (JA-10). Dasar butir 4.3; pelaku Finance Lead berstatus USULAN karena Finance Lead belum dipetakan ke jabatan (K-13) | "Memeriksa kelengkapan payment request dan kesesuaian dengan persetujuan." (A.4) dan "Memverifikasi/menahan pembayaran yang belum lengkap" (E.1) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Persetujuan pembayaran pajak dilakukan peran Lead (Finance Lead), 1 hari. Dasar pembayaran pajak masuk Ruang Lingkup dan jenis transaksi "Pembayaran pajak" | Tabel IV baris 3: "Review & Approval" ... "Proses approval dan pengajuan payment" / "1 day" / "Lead" (teks sel berurutan tanpa spasi di hasil baca: "Review & ApprovalRekonsiliasi nilai pajak terhutang di setiap akhir Masa PajakProses approval dan pengajuan payment") | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| Jenis transaksi pembayaran FAT: pembayaran invoice, reimbursement, cash advance (daftar jenis di kolom Jenis Transaksi). Sumbernya deskripsi checklist untuk SOP tetangga, bukan berkas tim | "SOP ini menjelaskan proses pengajuan pembayaran invoice, reimbursement dan cash advance" (config/checklist.json baris 25, SOP Payment and Disbursement Approval, checked true, tanpa fileId baris sendiri) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (berkas checklist) |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | Kriteria penerimaan baris 30 | "Dokumen log sheet approval untuk setiap transaksi pembayaran finance" | config/checklist.json baris 30 (checked false, tanpa link, tanpa kolom ISO) |
| 2 | Hak tanda tangan dan otorisasi keuangan dibatasi Authority Matrix; dasar jabatan Penyetuju tidak ditulis di form (butir 4.4, Definisi Delegasi tertulis) | "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." | 1m91W..., bagian 2 Pedoman Validasi |
| 3 | Keputusan keuangan mengikuti delegasi dan persetujuan tertulis (butir 4.4) | "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 1m91W..., JA-10 bagian E |
| 4 | Sumber menyebut "approver" tanpa jabatan (Penyetuju belum ditetapkan) | "Mengusulkan prioritas cash flow kepada approver" | 1m91W..., JA-10 E.3 |
| 5 | Prinsip pembuat dan pemeriksa di FAT: Staff tidak bertindak tanpa persetujuan tertulis Finance Lead (dasar analogi butir 4.7 dan 4.8, berlabel USULAN) | "Batas Kewenangan Pembuatan: Staff Finance dilarang keras menerbitkan atau mengirim invoice kepada klien tanpa approval tertulis Finance Lead." | context/audit fat, SOP Billing bagian 4.2 (baris 108); fileId 1sZfT..., tidak dibuka di Drive |
| 6 | Verdict audit: FAT 8 (judul ini) bertier G | "FAT 8 tetap G: DoA keuangan tertulis + jejak approval yang ada, bukan register baru." | context/audit sintesis baris 434 |
| 7 | Cacat maker = checker = approver menjadi syarat sebelum SOP Billing dan Tax masuk master list (dasar butir 4.7 dan Annex A 5.3) | "SOP Billing/Tax jangan masuk master list sebelum cacat maker = checker = approver (A 5.3) dan PPN diperbaiki (Opus)." | context/audit sintesis baris 434 |
| 8 | SNX-FAT-SOP-05 menaruh persetujuan utang pajak di form ini (berlabel USULAN di sana) | "Persetujuan utang pajak, dicatat di SNX-FAT-FRM-01 (USULAN)" dan baris rekaman "Persetujuan utang pajak dan pengajuan pembayaran (SNX-FAT-FRM-01)", lokasi "Folder Google Drive Departemen FAT (USULAN). Pemilik: Finance Lead.", retensi "Minimal 10 tahun (USULAN)" | specs/FAT-SOP-05.json (langkah 6.3 dan tabel rekaman) |
| 9 | Retensi 10 tahun untuk dokumen penagihan dan bukti perpajakan (angka dipakai pada lingkupnya; perluasan ke log ini USULAN) | "Seluruh arsip dokumen penagihan dan bukti perpajakan wajib disimpan selama minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001." | 1sZfT..., 8.2, dikutip dari notes/FAT-SOP-04.md (penanda tebal dibuang) |
| 10 | SNX-FAT-SOP-04 memuat "payment request, bukti pembayaran" sebagai dokumen keuangan lain dengan retensi USULAN (dasar baris rekaman 2) | "Softcopy dokumen keuangan lain (payment request, bukti pembayaran, laporan kas, laporan keuangan)" | specs/FAT-SOP-04.json, tabel rekaman |
| 11 | Dokumen tetangga: sesudah sweep, baris 27 dan 29 dirujuk dengan nomor SNX-FAT-SOP-06 dan SNX-FAT-REG-01; baris 24 dan 25 tetap ditulis "dalam peninjauan" (bukan "belum ada") | checklist baris 24, 25, 27, 29: checked true; CONTEXT-PACK: `"on review": SOP AR & Collection, SOP Payment & Disbursement Approval, SOP Accounting & Financial Report, Billing & Collection Monitoring Register` | config/checklist.json; context/CONTEXT-PACK-v19.md baris 74 |
| 12 | Finance Lead dan Finance Staff belum dipetakan ke jabatan; Authority Matrix belum bernomor | "Belum dipetakan (K-13)" (baris Finance Lead dan Finance Staff, matriks peran) dan "Belum bernomor" / "Authority Matrix, tempat hak tanda tangan kontrak dan otorisasi keuangan ditetapkan." | specs/HR-ORG-01.json |
| 13 | Peran Penyetuju (Approver) sudah dikenal di FAT untuk persetujuan invoice (bukan pembayaran) | "Penyetuju (Approver / CEO - Samuel Utomo)" / "Keputusan dan persetujuan tertulis atas perubahan Term of Payment di luar standar 14 hari kalender" | context/audit fat, SOP Billing 4.1 (baris 106); fileId 1sZfT..., tidak dibuka di Drive |

## 3. Pemetaan kriteria (Description baris 30)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| "Dokumen" | Form SNX-FAT-FRM-01, 10 bagian, format template (mode generic, FORM) | Perintah baris dan RUNBOOK §7 |
| "log sheet" | Bagian Log Sheet Approval: Tabel 1, 2, 3 dengan nomor baris sama (butir 4.1); satu baris satu transaksi; sel data kosong, tanpa baris contoh | RUNBOOK §6 (form baru: struktur kolom dan petunjuk pengisian saja) |
| "approval" | Tabel 2 (Keputusan Finance Lead, Keputusan Penyetuju, tanggal, alasan); butir 4.3 sampai 4.8; Tabel 3 (lokasi bukti persetujuan) | JA-10 A.4 dan E.1; SOP Tax Tabel IV baris 3; selebihnya USULAN (butir 4.9) |
| "untuk setiap transaksi pembayaran" | Ruang Lingkup: "setiap transaksi pembayaran yang dikelola FAT" dengan empat jenis bernama dan jenis lain; butir 4.1; tabel Dikecualikan | Checklist baris 25 (tiga jenis), SOP Tax (pajak); "setiap" dibaca mencakup semua jenis (A4) |
| "finance" | Dikelola FAT; pelaku Finance Staff dan Finance Lead | defaults.json (prepared, reviewed) dan HR-ORG-01 |

Pemetaan klausul ISO (bagian Rekaman dan Acuan ISO, satu label "(USULAN, perlu konfirmasi konsultan)"; checklist tidak memberi acuan klausul untuk baris ini). Judul klausul adalah pengetahuan standar, bukan teks sumber, dan tidak dicocokkan dengan teks standar (UNMEASURED):

| Klausul | Butir | Alasan |
|---|---|---|
| ISO 9001:2015 5.3 | 4.4 | Wewenang memutuskan atas pembayaran ditunjukkan per jabatan |
| ISO 9001:2015 7.5.3 | rekaman, 4.8 | Log dan bukti persetujuan dikendalikan: lokasi, pemilik, retensi |
| ISO/IEC 27001:2022 Annex A 5.3 | 4.7 | Pemisahan tugas; verdict sintesis menyebut "A 5.3" untuk cacat maker = checker = approver |
| ISO/IEC 27001:2022 Annex A 5.33 | rekaman | Perlindungan rekaman; SNX-FAT-SOP-01 dan SNX-FAT-SOP-05 memakainya untuk rekaman FAT |

## 4. Penanganan cacat context/audit

`grep -n "Financial Transaction Approval" context/audit/*.md` hanya menemukan satu baris: context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 751, butir 8 daftar FAT ("8. Financial Transaction Approval Records."). Dokumen ini tidak punya bagian 5 Catatan kualitas sendiri (T2 tanpa sumber). Cacat yang relevan diambil dari verdict sintesis dan dari dokumen FAT dan HR yang menjadi tetangganya:

| Berkas sumber | Cacat tercatat | Penanganan |
|---|---|---|
| sintesis baris 434 dan 446 | Verdict FAT 8 = G: isi wajib ada di dokumen induk (DoA keuangan tertulis plus jejak approval yang ada), bukan register baru | Checklist baris 30 tetap meminta dokumen log sheet dan worklist menetapkan T2, jadi form dibuat. Ketegangan dengan verdict G dicatat sebagai OI-11; form menunjuk delegasi tertulis (Authority Matrix) sebagai penentu jabatan Penyetuju dan tidak menetapkannya |
| SOP Billing (fat audit, bagian 5 butir 2) | Disusun, diperiksa, dan disetujui orang yang sama; tidak ada pemisahan peran | Butir 4.7: Finance Staff mencatat dan tidak memutuskan; satu orang tidak memutuskan pengajuannya sendiri. Berlabel USULAN. Blok Approval memakai tiga penanda tangan berbeda sesuai defaults.json |
| SOP Billing (butir 11) | Finance Lead tunggal; tidak ada pengganti bila tidak hadir; Finance Lead dan Staff Finance tidak ada sebagai jabatan di HR-JA-001 | Pengganti Finance Lead tidak dikarang (OI-6). Finance Lead dan Finance Staff ditulis apa adanya dengan status "belum dipetakan (butir K-13)" di Peran |
| SOP Billing (butir 3) | "CEO", "Samuel Utomo", ejaan Kristanto lawan Kristianto | Badan dokumen menulis "Direktur Utama" (data_conflicts); nama hanya di blok Approval ("Samuel Kristanto Utomo / President Director") |
| SOP Tax (fat audit, bagian 5 butir 4) | Langkah 3 memuat "Proses approval dan pengajuan payment" tanpa rujukan form atau batas wewenang approval | Form ini menjadi rujukan form untuk persetujuan itu (berlabel USULAN, sama dengan SNX-FAT-SOP-05). Batas wewenang tidak dikarang; ditunjuk ke delegasi tertulis (OI-1) |
| SOP Tax (fat audit, bagian 5 butir 4) | Langkah 4 tidak menyebut siapa yang menyetor pajak | Form tidak menyebut pelaku pembayaran; Finance Staff hanya mencatat tanggal dan bukti pembayaran. Pelaku pembayaran jadi OI-5 |
| HR-JA-001 (hr audit, bagian 5 butir 4 dan 10) | Frasa kompetensi janggal ("Risk pemahaman karyawan" dan "pihak terkait coordination" di JA-10); tidak ada jabatan Finance Lead atau Finance Staff | Tidak ada frasa janggal yang dipakai; hanya A.4, E.1, dan E.3 JA-10 yang dikutip dan semuanya bersih. Peran dipetakan seperti baris di atas |
| HR-JA-001 | Authority dibatasi Authority Matrix; belum ada | Tidak ada jabatan Penyetuju yang ditulis. Authority Matrix tercantum "Belum bernomor" di Dokumen Terkait |

## 5. Asumsi

| # | Asumsi | Alasan |
|---|---|---|
| A1 | process_owner = "Finance Lead" | Dokumen tanpa sumber; aturan defaults: jabatan pada kolom reviewed departemen, tanpa nama. Status USULAN (U-14) |
| A2 | Pemetaan peran ke HR-ORG-01: Finance Lead dan Finance Staff ada di matriks peran (belum dipetakan, K-13) dan dipakai persis. "Penyetuju" dan "Pemohon" tidak ada di HR-ORG-01. Jabatan terdekat untuk Penyetuju adalah Direktur Utama (JA-01) dan Direktur (JA-02), pemegang keputusan keuangan menurut batasan umum Job Analysis, tetapi saya tidak menuliskannya di dokumen karena sumber hanya menyebut "approver" (E.3) dan "Authority Matrix". "Pemohon" bukan jabatan; ia jabatan atau departemen mana pun yang meminta pembayaran | Instruksi pemetaan peran; mengarang jabatan Penyetuju melanggar RUNBOOK §0 butir 4. Istilah "Penyetuju" sama dengan nama peran "Penyetuju (Approver / CEO - Samuel Utomo)" di SOP Billing 4.1 (fakta 5 dan 13), yang di sana hanya menyetujui Term of Payment di luar standar |
| A3 | "finance" di kriteria = FAT (Finance, Accounting & Tax) | Nama departemen di defaults.json |
| A4 | "Setiap transaksi pembayaran" dibaca mencakup semua jenis pembayaran yang FAT kelola, bukan hanya tiga jenis di checklist baris 25; jenis lain ditulis di kolom Jenis Transaksi | Kata "setiap" di kriteria |
| A5 | Pembayaran pajak masuk lingkup | SNX-FAT-SOP-05 menunjuk form ini sebagai tempat persetujuan utang pajak dan pengajuan pembayaran pajak (USULAN di sana) |
| A6 | "10 baris" per tabel adalah ukuran tata letak, bukan klaim kapasitas atau volume | Kalimat di dokumen: "Baris tersedia untuk 10 transaksi. Finance Staff menambah baris bila perlu." |
| A7 | Rujukan "tugas nomor 4 JA-10" dan "baris Wewenang JA-10" di SNX-HR-JA-01 sama dengan A.4 dan E.1 di Job Analysis Drive | specs/HR-JA-01.json memuat tugas nomor 4 dan wewenang yang kalimatnya sama dengan kutipan Drive |
| A8 | Satu istilah tiap hal: "Penyetuju" untuk peran, "keputusan" untuk hasil, "bukti persetujuan" untuk berkas persetujuan, "bukti pembayaran" untuk berkas bayar; "approval" hanya dipakai sebagai nama form, nama blok, dan sebutan kerja di Tujuan | RUNBOOK §6a butir 7 |
| A9 | Bentuk fisik form: docx berformat template (mode generic). Pemakaian harian sebagai lembar Google Sheets tidak diputuskan | OI-9 |
| A10 | Samuel di badan dokumen = "Direktur Utama"; COO tidak disebut, jadi aturan "Direktur (COO)" tidak terpicu | defaults.json data_conflicts |

## USULAN

13 kemunculan label "(USULAN)" di spec (sebelum sweep 12; sweep menambah satu di baris rekaman bukti) (satu adalah baris definisi label itu sendiri) ditambah satu label klausul "(USULAN, perlu konfirmasi konsultan)"; dikelompokkan jadi 14 butir, termasuk butir yang dicakup label di butir 4.9 dan satu butir tanpa label di badan (U-13, pengecualian cakupan). Pemutus yang disarankan memakai kelompok: owner, Samuel, Aziz, FAT, Legal, Fani. Diubah W9: hitungan di atas basi; sesudah W9 spec memuat dua label (USULAN) lagi dari dua definisi baru A6 (Finance Lead dan Finance Staff), jadi lint mencatat 15 kemunculan. Dua label itu tercakup OI-2, tidak membuat butir USULAN baru.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U-01 | Struktur kolom Tabel 1 sampai 3 dan tiga nilai Keputusan (Disetujui, Ditolak, Ditahan; "Ditahan" dari JA-10 E.1, dua lainnya tidak bersumber) | Butir 4.9; bagian Log Sheet Approval; Definisi Keputusan | FAT |
| U-02 | Penunjukan pelaku: Pemohon menyampaikan, Finance Staff mencatat, Finance Lead memeriksa dan memutuskan, Penyetuju memutuskan; butir 4.2 sampai 4.8 | Butir 4.9; intro Peran; tabel Peran | owner |
| U-03 | Penyetuju sebagai tingkat persetujuan kedua yang bergantung delegasi tertulis; kolom dikosongkan bila delegasi tidak mensyaratkan; jabatan dan batas nilai tidak ditulis | Butir 4.4; Peran | Samuel (pemilik delegasi keuangan) dan owner |
| U-04 | Alasan tertulis untuk keputusan Ditolak atau Ditahan; Tabel 3 hanya terisi untuk baris yang semua keputusannya Disetujui | Butir 4.5 dan 4.6 | FAT |
| U-05 | Pemisahan peran: Finance Staff tidak memutuskan; tidak ada yang memutuskan pengajuannya sendiri; bila Finance Lead adalah Pemohon, Penyetuju memutuskan. Dasar sintesis dan Annex A 5.3 | Butir 4.7 | owner, setelah konfirmasi konsultan |
| U-06 | Bukti persetujuan tertulis untuk tiap keputusan Disetujui dan pencatatan lokasinya di Tabel 3 | Butir 4.8 | FAT |
| U-07 | Definisi Reimbursement dan Cash advance (dua label; definisi umum, bukan definisi SINUX) | Definisi | FAT |
| U-08 | Lokasi rekaman Folder Google Drive Departemen FAT dan pemilik Finance Lead (dua baris rekaman) | Rekaman baris 1 dan 2 | FAT |
| U-09 | Retensi minimal 10 tahun untuk log dan bukti (angka sumber hanya untuk dokumen penagihan dan bukti perpajakan; dua baris rekaman) | Rekaman kolom Retensi | FAT dan Legal |
| U-10 | Finance Lead meninjau form setiap tahun (review_period YEARLY dari defaults, pelaku USULAN) | Kesimpulan | owner |
| U-11 | Daftar klausul ISO 9001:2015 (5.3, 7.5.3) dan ISO/IEC 27001:2022 (Annex A 5.3, 5.33), label "(USULAN, perlu konfirmasi konsultan)" | Acuan ISO | konsultan lewat owner |
| U-12 | Form ini sebagai tempat mencatat persetujuan utang pajak dan pengajuan pembayaran pajak (label di Dokumen Terkait mengikuti SNX-FAT-SOP-05; diubah W9: kalimat Dokumen Terkait kini merujuk butir 6.3 langkah 2 untuk persetujuan utang pajak dan tabel rekaman bagian 11 untuk pengajuan pembayaran, cakupan butir tidak berubah) | Dokumen Terkait baris SNX-FAT-SOP-05; Ruang Lingkup | FAT |
| U-13 | Aturan arsip SNX-FAT-SOP-04 dipakai untuk lokasi dan retensi form ini; pengecualian cakupan (tujuh butir) diturunkan dari kriteria baris karena sumber diam | Dokumen Terkait baris SNX-FAT-SOP-04; Ruang Lingkup tabel dikecualikan | FAT |
| U-14 | process_owner = Finance Lead | Identity | owner |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-1 | Jabatan Penyetuju, batas nilai, dan tingkat persetujuan per jenis transaksi tidak ada di sumber. Authority Matrix belum bernomor; Job Analysis hanya menyebut "approver" (E.3). Kolom Penyetuju di Tabel 2 kosong sampai delegasi tertulis ada | Samuel dan owner |
| OI-2 | Pemetaan Finance Lead dan Finance Staff ke jabatan di SNX-HR-ORG-01 (butir K-13); sampai itu diputus, tidak ada nama orang di kolom keputusan (diubah W9: G-3 A6, Finance Lead dijalankan Direktur sampai jabatannya terisi dan Finance Staff oleh JA-10 dan JA-11, keduanya USULAN; tetap tidak ada nama orang di kolom keputusan) | owner |
| OI-3 | Apakah dua tingkat (Finance Lead lalu Penyetuju) berlaku untuk semua jenis, atau Finance Lead cukup untuk jenis tertentu. Form menaruh keduanya dan membiarkan kolom Penyetuju kosong bila delegasi tidak mensyaratkan | FAT |
| OI-4 | Konflik dengan SNX-FAT-SOP-05 butir 6.3: dokumen itu menaruh persetujuan utang pajak dan pengajuan pembayaran pajak pada Finance Lead yang sama. Butir 4.7 form ini meminta Penyetuju memutuskan pengajuan yang Finance Lead ajukan sendiri. FAT perlu memutus: pemisahan di form ini, atau perubahan di SOP Tax | FAT dan owner |
| OI-5 | Siapa yang menjalankan pembayaran (transfer bank) dan apakah ada kontrol yang menahan pembayaran tanpa keputusan Disetujui. Sumber hanya menyebut Finance Staff menyetor pajak di SNX-FAT-SOP-05 (USULAN di sana). Form hanya mencatat tanggal dan bukti pembayaran | FAT |
| OI-6 | Pengganti Finance Lead atau Penyetuju bila tidak hadir, dan pembayaran mendesak sebelum persetujuan tertulis: tidak ada di sumber, tidak dikarang. Form belum punya penanganan pengecualian | Samuel dan FAT |
| OI-7 | Apakah jenis pembayaran lain (gaji dan input payroll dari HR, pembayaran vendor selain pembayaran invoice) tercakup. Form membaca "setiap" sebagai mencakup semuanya (A4) | FAT |
| OI-8 | Bentuk bukti persetujuan tertulis yang sah (surat, pesan, tanda tangan basah, atau sistem tiket); sumber tidak menyebutnya, jadi form hanya menyebut "tertulis" | FAT |
| OI-9 | Bentuk pakai harian: form ini berformat docx, sedangkan log harian lazimnya lembar kerja. Apakah Tabel 1 sampai 3 dipindah ke Google Sheets dan di mana | FAT dan owner |
| OI-10 | SOP Payment and Disbursement Approval belum bernomor di kolom kode Dokumen Terkait; kalimat Ruang Lingkup kini hanya "dalam peninjauan". Setelah terbit, rujukan di Ruang Lingkup, Dokumen Terkait, dan butir 4.2 sampai 4.5 perlu disesuaikan; diubah W9: penyeragaman status di Ruang Lingkup (G-3 B4), item tetap terbuka | FAT |
| OI-11 | Verdict audit menempatkan butir ini di tier G (isi wajib di dokumen induk: DoA keuangan tertulis plus jejak approval, bukan register baru), sedangkan checklist baris 30 meminta dokumen log sheet. Form dibuat sesuai checklist. Keputusan apakah form ini berdiri sendiri atau menjadi lampiran DoA keuangan | owner |
| OI-12 | Retensi dan lokasi log: angka 10 tahun hanya bersumber untuk dokumen penagihan dan bukti perpajakan; dasar hukum angka itu tidak dibawa (sumber menulis "sesuai ketentuan perpajakan dan audit ISO" tanpa pasal). Perlu konfirmasi angka dan titik awal hitungan | Legal dan FAT |
| OI-13 | Definisi Reimbursement dan Cash advance (U-07) belum diputus; SOP Payment and Disbursement Approval akan memuat definisi sebenarnya | FAT |
| OI-14 | Kalimat perintah kepada AI di sumber dan di berkas context/audit: nihil | tidak ada |

## 6. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI:
1. Awalan "Finance Staff" muncul di 12 dari 13 langkah Cara Mengisi (9 di antaranya "menulis"), dan tabel Peran memakai pasangan "Finance Staff" dan "Finance Lead" berulang. Dibiarkan karena satu langkah wajib satu pelaku dan satu tindakan (RUNBOOK §6a.2) dan nama peran wajib persis sama dengan tabel Peran. Penyederhanaan hanya mungkin bila FAT memutus satu pelaku pencatat.
2. Paragraf kedua Tujuan membuka dengan "Hasil yang dijaga adalah", pola yang sama dengan dokumen W-lain. Dibiarkan karena RUNBOOK §6a.4 meminta hasil yang dijaga.
3. Definisi berkalimat pendek dan seragam. Dibiarkan karena bagian itu hanya memuat arti istilah.
4. Dua baris tabel Rekaman memakai "(USULAN)" berturut-turut dan Dokumen Terkait memakainya dua kali. Dibiarkan karena tiap label menunjuk keputusan yang berbeda (lokasi, pemilik, retensi, rujukan).

Perbaikan teks yang saya lakukan dalam putaran ini: (a) "pemohon" huruf kecil di Tujuan diganti "Pemohon" agar sama dengan nama peran; (b) "transaksi pembayaran Finance" diganti "transaksi pembayaran yang dikelola FAT" supaya satu nama departemen; (c) "Rekaman approval" di tabel Acuan ISO diganti "Rekaman keputusan dan bukti persetujuan" supaya satu istilah per hal; (d) kalimat "Meninjau form ini setiap tahun" dihapus dari tabel Peran karena sudah ada di Kesimpulan; (e) langkah 6.1 dipendekkan dan klausa "memakai nomor yang sama di Tabel 2 dan Tabel 3" dihapus karena sudah ada di butir 4.1; (f) rujukan JA-10 diganti dari "butir A.4 dan E.1" (nomor berkas Drive) ke "tugas nomor 4 dan baris Wewenang" supaya cocok dengan SNX-HR-JA-01 yang dibaca pegawai; (g) definisi Bukti pembayaran ditambahkan karena istilah itu dipakai di Tabel 3 dan butir 6.12; (h) kalimat retensi dipendekkan dan lebar kolom tabel Rekaman, Dokumen Terkait, dan tiga tabel log diperbaiki agar kolom tidak terlalu sempit.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: "10 tahun" (SOP Billing 8.2, untuk dokumen penagihan dan bukti perpajakan; perluasan berlabel USULAN). "10 transaksi" adalah ukuran tata letak (A6), bukan klaim. Tidak ada angka lain di badan; nomor butir dan nomor tabel adalah penomoran dokumen.
- Nama: tidak ada nama orang di badan dokumen. Nama Samuel hanya di blok Approval, dari config/defaults.json. Nama sistem "Google Drive" dan folder "Departemen FAT" dari SOP Billing 8.2 lewat SNX-FAT-SOP-05; "Authority Matrix" dari HR-JA-001 bagian 2.
- Tanggal: tidak ada; Effective Date kosong.
- Kalimat turunan tanpa kutipan langsung: definisi Transaksi pembayaran, Pengajuan, Dokumen dasar, Bukti persetujuan, Bukti pembayaran (arti umum, bukan klaim tentang SINUX); definisi Reimbursement dan Cash advance (berlabel USULAN); nilai Keputusan "Disetujui" dan "Ditolak" (hanya "Ditahan" dari JA-10 E.1); seluruh alur butir 4.2 sampai 4.8 dan langkah 6.1 sampai 6.13 (berlabel USULAN lewat butir 4.9 dan intro Peran); tujuh butir pengecualian cakupan (diturunkan dari kriteria baris, U-13); judul klausul ISO (pengetahuan standar, UNMEASURED).
- Item yang memang tidak bersumber ditandai (USULAN) di dokumen dan ada di tabel USULAN di atas.

## Sweep

Putaran sweep atas permintaan orkestrator (butir 1 dan 2). Hanya dua hal diubah; fakta, angka, nama, dan struktur lain tetap. Salinan spec sebelum sweep: /tmp/pen-FAT-FRM-01/FAT-FRM-01.spec.before-sweep.json.

| Butir | Letak | Sebelum | Sesudah |
|---|---|---|---|
| 1 dan 2 | Ruang Lingkup, baris "Penerimaan uang dari pelanggan" | "...ada di SOP Account Receivable & Collection dan Billing & Collection Monitoring Register, keduanya dalam peninjauan dan belum bernomor." | "...ada di SOP Account Receivable & Collection (dalam peninjauan dan belum bernomor) dan SNX-FAT-REG-01." |
| 1 dan 2 | Ruang Lingkup, baris "Pencatatan akuntansi" | "Ada di SOP Accounting and Financial Report, dalam peninjauan dan belum bernomor." | "Ada di SNX-FAT-SOP-06." |
| 1 dan 2 | Dokumen Terkait, baris SOP Accounting and Financial Report | "Belum bernomor | SOP Accounting and Financial Report: dalam peninjauan. Pencatatan akuntansi, dikecualikan dari form ini." | "SNX-FAT-SOP-06 | Accounting and Financial Report: pencatatan akuntansi, dikecualikan dari form ini." (ditaruh sesudah SNX-FAT-SOP-05) |
| 1 dan 2 | Dokumen Terkait, baris Billing & Collection Monitoring Register | Digabung di baris "Belum bernomor | SOP Account Receivable & Collection dan Billing & Collection Monitoring Register: dalam peninjauan..." | Baris sendiri "SNX-FAT-REG-01 | Billing & Collection Monitoring Register: pencatatan piutang usaha dari klien, dikecualikan dari form ini."; baris "Belum bernomor" tersisa hanya untuk SOP Account Receivable & Collection (dalam peninjauan) |
| 1 | Langkah 6.11 | "Finance Staff menulis lokasi bukti persetujuan di Tabel 3, sesuai lokasi di tabel Rekaman (butir 4.8)." | "Finance Staff menulis lokasi berkas bukti persetujuan di Tabel 3, di dalam folder yang tercantum di tabel Rekaman (butir 4.8)." |
| 1 | Tabel Rekaman, baris 2, kolom Lokasi dan pemilik | "Lokasi tertulis di Tabel 3. Pemilik: Finance Lead (USULAN). Aturan arsip mengikuti SNX-FAT-SOP-04." | "Folder Google Drive Departemen FAT (USULAN); lokasi berkas tiap baris ditulis di Tabel 3 (butir 6.11). Pemilik: Finance Lead (USULAN). Aturan arsip mengikuti SNX-FAT-SOP-04." |

Catatan sweep:
- Rujukan melingkar 6.11 dan tabel Rekaman selesai: 6.11 menunjuk folder di tabel Rekaman, tabel Rekaman menyebut folder dan menunjuk balik ke 6.11 untuk lokasi berkas per baris. Folder sama dengan baris 1 tabel Rekaman, jadi tidak ada lokasi baru; label (USULAN) mengikuti baris 1 (U-08).
- SNX-FAT-FRM-02 (Financial Information Access Authorization Records): form ini tidak pernah menyebutnya, jadi tidak ada rujukan yang diganti. Tidak ditambahkan karena sweep hanya mengubah dua butir itu. Bila FAT ingin akses ke folder log dicatat di FRM-02, itu perlu keputusan baru (pemutus: FAT).
- Judul dokumen bernomor diambil dari specs/FAT-SOP-06.json (title "Accounting and Financial Report") dan specs/FAT-REG-01.patch.json (Kontrol Dokumen B5 "Billing & Collection Monitoring Register"; B15 "Mencatat semua piutang usaha dari klien SINUX di sheet AR Aging"). Keduanya berstatus Draft; kutipan bisa basi bila dokumen itu berubah.
- Temuan pemeriksa lain di qa/FAT-FRM-01.verify.json (penunjuk butir SOP-01 4.8, kalimat pasif tanpa pelaku, istilah approval lawan persetujuan, setelah lawan sesudah, label pada kalimat pengecualian, ketegangan JA-10 dengan data_conflicts) tidak disentuh karena di luar dua butir sweep. Ketegangan JA-10 dan K-13 sudah tercakup OI-2 dan OI-4.
- Uji sesudah sweep: render tanpa galat; lint generic pass true (warn 13 butir USULAN); validator OOXML PASSED; blankscan ok 11 halaman; pemeriksaan tambahan (dash, kutipan, frasa terlarang, kode SNX di badan lawan Dokumen Terkait, panjang langkah) nihil temuan, bukti /tmp/pen-FAT-FRM-01/extra-checks.out.txt.

## ISO-W9

Dasar: control/LEAD-GUIDE.md G-3 A6 dan B4, serta temuan makna R400 dan S03. Hanya specs/FAT-FRM-01.json dan notes/FAT-FRM-01.md yang diubah.

| Butir | Sebelum | Sesudah |
|---|---|---|
| A6 blok Reviewed | Finance Lead | Amirull Yusuf Zulkarnain / Direktur (Prepared tetap Finance Staff) |
| A6 definisi (bagian 3), dua baris baru setelah FAT | tidak ada | "Finance Lead: peran pemeriksa dan penyetuju FAT; jabatannya belum terisi, dan sampai terisi peran ini dijalankan Direktur (USULAN)." dan "Finance Staff: peran pelaksana yang dijalankan pemegang jabatan Finance (JA-10) dan Accounting & Tax (JA-11) (USULAN)." (kata pertama arti diberi huruf kapital) |
| A6 tabel peran (bagian 5), baris Finance Staff dan Finance Lead | "Belum dipetakan ke jabatan di SNX-HR-ORG-01 (butir K-13)." | "Pemetaan ke jabatan mengikuti definisi di bagian 3 (butir K-13)." |
| A6 dokumen terkait, baris SNX-HR-ORG-01 | "sumber nama peran Finance Lead dan Finance Staff, yang belum dipetakan ke jabatan (butir K-13)." | "sumber nama jabatan. Pemetaan Finance Lead dan Finance Staff ke jabatan mengikuti definisi di bagian 3 (butir K-13)." |
| R400 dokumen terkait, baris SNX-FAT-SOP-05 | "butir 6.3 menyebut form ini sebagai tempat mencatat persetujuan utang pajak dan pengajuan pembayaran pajak (USULAN)." | "butir 6.3 langkah 2 menyebut form ini sebagai tempat mencatat persetujuan utang pajak, dan tabel rekaman di bagian 11 menyebutnya untuk persetujuan utang pajak dan pengajuan pembayaran (USULAN)." |
| S03 ruang lingkup, baris Penerimaan uang dari pelanggan | "SOP Account Receivable & Collection (dalam peninjauan dan belum bernomor)" | "SOP Account Receivable & Collection (dalam peninjauan)" |
| B4 ruang lingkup, baris Tata cara pengajuan pembayaran | "SOP Payment and Disbursement Approval, dalam peninjauan dan belum bernomor." | "SOP Payment and Disbursement Approval, dalam peninjauan." (pola status yang sama dengan S03, ikut diseragamkan) |
| R2 butir 1, rujukan K-13 (tabel peran dua baris, dokumen terkait baris SNX-HR-ORG-01) | "... bagian 3 (butir K-13)" (3 tempat) | "... bagian 3 (SNX-HR-ORG-01 butir K-13)" (3 tempat) |
| R2 butir 2, notes | U-12, OI-10, dan hitungan USULAN tanpa penanda W9; kalimat OI-10 "dalam peninjauan dan belum bernomor" tidak akurat bagi kalimat Ruang Lingkup | Penanda "diubah W9" ditambahkan di baris U-12, OI-10, dan kalimat hitungan; OI-10 menyebut kalimat Ruang Lingkup kini "dalam peninjauan" saja dan kolom kode tetap "Belum bernomor" |
| Putaran perbaikan 1, R2 butir 2 (pemblokir) | Baris U-12, OI-10, dan paragraf hitungan USULAN tanpa penanda W9; hitungan menyebut 13 label | Penanda "diubah W9: <alasan>" ditambahkan di baris U-12, OI-10, dan paragraf hitungan (15 label sesudah dua definisi A6); OI-10 kini menyebut kolom kode "belum bernomor" dan Ruang Lingkup "dalam peninjauan" |

Rujukan silang yang diubah: dua, yaitu baris SNX-FAT-SOP-05 di dokumen terkait (butir 6.3 langkah 2 dan bagian 11 tabel rekaman, keduanya terbukti ada di SNX-FAT-SOP-05) dan rujukan bagian 3 pada pemetaan peran.

Tidak diubah: kolom kode "Belum bernomor" pada tiga baris dokumen terkait dan "Authority Matrix, belum bernomor" di ruang lingkup dan definisi, karena butir kerja hanya menyeragamkan status dokumen checklist (SOP Account Receivable & Collection dan SOP Payment and Disbursement Approval) di kalimat, dan Authority Matrix bukan baris checklist.

GAP: butir 4.3 dan baris SNX-HR-JA-01 menaruh pemeriksaan dokumen dasar pada tugas nomor 4 JA-10 (Finance). Dengan definisi baru, Finance Lead dijalankan Direktur sampai jabatannya terisi, sehingga kaitan tugas JA-10 ke peran pemeriksa perlu ditegaskan oleh LEAD atau FAT. Tidak diubah karena di luar butir kerja.

Open item: OI-2 diubah W9 (pemetaan peran mengikuti G-3 A6, berlabel USULAN). OI-10 tetap terbuka.

Uji: render_sop.py rc 0; lint_doc.py generic "pass": true (warn 15 butir USULAN); validate.py "All validations PASSED!"; blankscan ok 11; w9diff.py: 7 baris lama, 9 baris baru, hanya perubahan di atas.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
- Tabel Peran, baris Finance Staff dan Finance Lead: "Pemetaan ke jabatan mengikuti definisi di bagian 3 (SNX-HR-ORG-01 butir K-13)." Kalimat penunjuk; pemetaannya sudah tertulis di tabel Definisi dan di baris SNX-HR-ORG-01 Dokumen Terkait (butir K-13).
- Tabel Record, Retensi baris 1: "Angka berasal dari retensi dokumen penagihan dan perpajakan (SNX-FAT-SOP-01, SNX-FAT-SOP-05); perluasan ke log ini belum diputus." Catatan sumber angka; faktanya dipadatkan menjadi "mengikuti retensi dokumen penagihan dan perpajakan (USULAN)". Sumber angka 10 tahun: SNX-FAT-SOP-01 dan SNX-FAT-SOP-05; perluasan ke log ini belum diputus FAT.
- Rujukan butir yang tidak perlu dibuka pengisi: "(butir 4.1)" di 6.1, "sesuai butir 4.5" di 6.10 dan "sesuai butir 4.6" di 6.12 (diganti faktanya), "(butir 4.8)" di 6.11, "(butir 6.11)" di tabel Record.
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "klien" (paling sering di dokumen ini); satu "pelanggan" di Ruang Lingkup diganti "klien".
Cara Mengisi ditulis sebagai kalimat perintah untuk Finance Staff (pengisi utama di tabel Peran); 6.7 tetap diawali Finance Lead karena langkahnya milik peran lain.
Tabel isian: kolom Alasan Ditolak atau Ditahan diperlebar, min_row_cm 0.8 di Tabel 1 sampai 3.

### W10 koreksi worker (temuan nonblocking qa/FAT-FRM-01.w10.json)
- Tabel Record, Retensi baris 1: sumber angka (SNX-FAT-SOP-01, SNX-FAT-SOP-05) dan "perluasan ke log ini belum diputus" dikembalikan; sempat hilang saat kalimat dipadatkan.
- 6.11: "tabel Record (rekaman)" pada kemunculan pertama, menjembatani heading beku "Rekaman".
### W10 audit pointer
- .sections[4].blocks[1].table.rows[1][1]: lengkap; kalimat penunjuk "Pemetaan ke jabatan mengikuti definisi di bagian 3 (SNX-HR-ORG-01 butir K-13)" dibuang; pemetaan tetap di bagian 3 Definisi dan di Dokumen Terkait baris SNX-HR-ORG-01 (butir K-13); rujukan butir 4.2, 4.7, 4.8 tetap.
- .sections[4].blocks[1].table.rows[2][1]: lengkap; kalimat penunjuk yang sama dibuang; rujukan butir 4.3 tetap.
- .sections[5].blocks[0].p: lengkap; penunjuk "(butir 4.1)" dibuang; langkah satu baris per pengajuan tetap tertulis.
- .sections[5].blocks[9].p: lengkap; "sesuai butir 4.5" diganti isi butir 4.5 (setiap keputusan Ditolak atau Ditahan memuat alasan tertulis).
- .sections[5].blocks[10].p: lengkap; penunjuk "(butir 4.8)" dibuang; langkah menulis lokasi bukti di Tabel 3 dan folder di tabel Record tetap.
- .sections[5].blocks[11].p: lengkap; "sesuai butir 4.6" diganti isi butir 4.6 (Tabel 3 hanya untuk baris yang semua keputusannya Disetujui).
- .sections[7].blocks[1].table.rows[1][1]: lengkap; penunjuk "(butir 6.11)" dibuang; folder, lokasi di Tabel 3, pemilik (USULAN), dan aturan arsip tetap.
- .sections[8].blocks[0].table.rows[0][1]: lengkap; "mengikuti definisi di bagian 3" dibuang, rujukan "(butir K-13)" SNX-HR-ORG-01 tetap.
- .sections[8].blocks[0].table.rows[4][1]: lengkap; rujukan "Butir 6.3 langkah 2" dan "bagian 11" SOP itu tetap (huruf kapital di awal kalimat; pemindai hanya mengenali huruf kecil); label (USULAN) tetap.
