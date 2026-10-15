# Catatan penyusun MKT-REG-03: Marketing Lead & Campaign Outcome Register

Status: DRAFTED (spec + notes ada). Spec: specs/MKT-REG-03.json. Mode generic (doc_type_cover REGISTER), aksi T2, wave W7, nomor SNX-MKT-REG-03 (nomor SNX lama dipertahankan), department Marketing, classification INTERNAL, audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Zilly Dwinata / Brand & Marketing", reviewed "Laras Rasmawati / VP Commercial", approved "Samuel Kristanto Utomo / President Director". process_owner "VP Commercial": dokumen T2 tanpa sumber memakai jabatan reviewer departemen (Laras Rasmawati / VP Commercial), tanpa nama (config/defaults.json, medan process_owner). Catatan worklist: kosong.

## 1. Sumber

Sumber dokumen: tidak ada (T2 tanpa sumber). Struktur kolom dan petunjuk pengisian disusun dari kriteria baris 59. Sel data faktual kosong, tanpa baris contoh. Alat Drive hanya dipakai untuk tiga panggilan `get_file_metadata` (baca saja) guna mengukur modifiedTime dokumen yang menjadi dasar peran dan istilah. Nol tulis ke Drive.

| Bahan | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Kriteria: config/checklist.json baris 59 (checked: false, link kosong) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist tim) | 2026-10-14T17:47:13.611Z (tertulis di config/checklist.json, tidak diukur ulang) | `python3 -I` pada berkas repo |
| SALES STANDARD OPERATING PROCEDURE.pdf (dasar hubungan Marketing dan Sales, CRM, qualification) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (`get_file_metadata` hari ini) | Teks dari salinan context/audit/iso-sinux-supdocs-commercial-2026-10-14.md (baris 817, 829, 846). PDF aslinya tidak dibuka di sesi ini (UNMEASURED terhadap lapisan teks PDF) |
| SINUX_Job_Analysis_2026.docx (JA-06 Brand & Marketing) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (`get_file_metadata` hari ini) | Salinan context/audit/iso-sinux-supdocs-hr-2026-10-14.md (baris 445) dan specs/HR-JA-01.json |
| KPI COMMERCIAL & MARKETING.xlsx (KPI Lead Generation dan MQL, KPI individu Brand & Marketing) | 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb | 2026-10-13T06:41:25.963Z (`get_file_metadata` hari ini) | Salinan context/audit/iso-sinux-supdocs-commercial-2026-10-14.md (baris 474, 490, 502). xlsx aslinya tidak dibuka (UNMEASURED terhadap sel aslinya) |
| Pendukung repo (bukan Drive) | tidak berlaku | tidak berlaku | config/defaults.json v21 (approval MKT, process_owner, data_conflicts), specs/HR-ORG-01.json (jabatan JA-03, JA-06, JA-07 dan matriks peran), specs/COM-SOP-01.json (bagian 3, 5, 6, butir 4.3, 4.6, 4.7, 4.13), specs/ISMS-PRO-01.json (butir 4.3), config/worklist.json (nomor dan judul SNX-MKT-REG-02, SNX-MKT-RPT-01, SNX-COM-REG-01). Spec lane lain berstatus Draft, kutipan darinya bisa basi |

Kalimat perintah kepada AI di bahan mana pun: nihil. Kalimat kewajiban untuk karyawan di Sales SOP ("Sales wajib memastikan ...") adalah isi SOP, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria register: lima unsur yang harus tercatat (hasil marketing yang diteruskan ke Sales, sumber lead, campaign asal, tanggal serah terima, status qualification bila tersedia, feedback dari Sales) dan tiga bukti. Dasar Tabel 1 sampai Tabel 4 | "Mencatat hasil marketing yang diteruskan ke Sales, termasuk sumber lead, campaign asal, tanggal serah terima, status qualification bila tersedia, dan feedback dari Sales." dan "Bukti: lead handover, laporan lead generation, dan evaluasi kualitas lead." (config/checklist.json baris 59, kolom Description) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Brand & Marketing (JA-06) menyerahkan lead beserta sumber dan statusnya. Dasar butir 4.2, peran Brand & Marketing sebagai pencatat, dan kolom Sumber Lead | "Menyerahkan qualified leads ke Commercial beserta sumber dan statusnya." (Job Analysis, JA-06 Brand & Marketing, Uraian Jabatan nomor 6) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Marketing mengirim inbound lead ke Sales, dan kolaborasi Marketing dengan Sales mencakup lead generation dan campaign feedback. Dasar penerima lead (Business Development) dan kolom Feedback dari Business Development | "mengelola inbound leads dari Marketing." (Sales SOP, Stage 1 Prospecting, hal. 6) dan "Marketing | Lead generation; Campaign feedback; Event collaboration" (Sales SOP, 09 Internal Collaboration, hal. 15) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Posisi |
|---|---|---|---|
| 1 | Brand & Marketing menyerahkan inbound lead ke Business Development beserta sumber dan statusnya (butir 4.2; Peran) | "Menyerahkan inbound lead ke Business Development beserta sumber dan statusnya, serta memberi campaign feedback dan berkolaborasi dalam event." | specs/COM-SOP-01.json, tabel Peran, baris Brand & Marketing; prosedur Lead Generation langkah 1 |
| 2 | Business Development mencatat lead di CRM (butir 4.4) | "Business Development mencatat seluruh aktivitas penjualan, opportunity, forecast, dan customer engagement di CRM. Catatan wajib meliputi Lead, Opportunity, ..." | specs/COM-SOP-01.json butir 4.3; asal Sales SOP 06 CRM Policy, hal. 13: "Seluruh aktivitas penjualan wajib dicatat di CRM." |
| 3 | Qualification dan Sales Stage dijalankan Business Development di CRM; daftar status berlabel USULAN di sana (Definisi Qualification dan Sales Stage; butir 4.5) | "Sebelum opportunity masuk ke tahap proposal, Business Development memastikan opportunity memenuhi lima kriteria qualification (Business Need, Budget, Decision Maker, Timeline, dan Technical Fit) ..." dan "Business Development mengubah Sales Stage di CRM: status Leads saat lead tercatat, status Qualified sesudah qualification, ... dan status Future Nurture untuk lead yang belum layak sekarang tetapi akan ditindaklanjuti nanti. Pemetaan tahap ke status ini berstatus (USULAN)." | specs/COM-SOP-01.json butir 4.6 dan 4.7 |
| 4 | Brand & Marketing memonitor lead dan efektivitas biaya pemasaran (dasar evaluasi di Tabel 4, tanpa kriteria angka) | "Memonitor reach, engagement, lead dan efektivitas biaya pemasaran." | Job Analysis, JA-06 nomor 5; fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 5 | KPI Brand & Marketing memuat Lead Generation dan MQL bersatuan per bulan (dasar periode satu bulan, butir 4.12; angkanya tidak disalin) | "Lead Generation & Marketing Qualified Leads (MQL) | Jumlah | Minimal 2 Leads/bulan dan 1 MQL/bulan" | KPI COMMERCIAL & MARKETING.xlsx, blok Zilly; salinan context/audit baris 474; fileId 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb |
| 6 | Informasi customer minimal RESTRICTED, sehingga register terisi berklasifikasi RESTRICTED (Internal) (butir 4.14) | "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan tingkat yang lebih tinggi." | specs/ISMS-PRO-01.json butir 4.3 (repo, Draft) |
| 7 | JA-06 dan JA-07 melapor ke VP Commercial; nama jabatan dipakai persis | "JA-06 | Brand & Marketing | Zilly Dwinata | Commercial | VP Commercial (JA-03)" dan "JA-07 | Business Development | ... | Commercial | VP Commercial (JA-03)" | specs/HR-ORG-01.json, Daftar Jabatan |
| 8 | Handover Sales ke Delivery adalah proses lain (Definisi Serah terima lead) | "Sales wajib melakukan handover kepada Delivery." | Sales SOP, Stage 9 Project Handover, hal. 11; specs/COM-SOP-01.json bagian 6 Handover |

## 3. Pemetaan kriteria (Description baris 59)

| Unsur kriteria | Di dokumen |
|---|---|
| Mencatat hasil marketing yang diteruskan ke Sales | Tabel 1 (serah terima lead); Tujuan; Ruang Lingkup; butir 4.1 sampai 4.4; langkah 6.1 sampai 6.6 |
| Sumber lead | Tabel 1 kolom Sumber Lead; Definisi Sumber Lead; langkah 6.4 |
| Campaign asal | Tabel 1 kolom Campaign Asal; butir 4.13; langkah 6.5; acuan nama ke SNX-MKT-REG-02 (USULAN) |
| Tanggal serah terima | Tabel 1 kolom Tanggal Serah Terima; langkah 6.2 |
| Status qualification bila tersedia | Tabel 2 kolom Status Qualification dan Tanggal Status; butir 4.5 sampai 4.7; kolom dibiarkan kosong bila belum tersedia |
| Feedback dari Sales | Tabel 2 kolom Feedback dari Business Development dan Tanggal Feedback; butir 4.8; langkah 6.9 dan 6.10. Sales dipetakan ke Business Development (Definisi Sales, USULAN) |
| Bukti: lead handover | Tabel 1 dan Tabel 2; tabel Rekaman baris 1 |
| Bukti: laporan lead generation | Tabel 3; butir 4.9; langkah 6.11 dan 6.12; tabel Rekaman baris 2 |
| Bukti: evaluasi kualitas lead | Tabel 4; butir 4.10 dan 4.11; langkah 6.13 sampai 6.17; tabel Rekaman baris 3 |
| Klausul ISO (checklist tidak memberi acuan) | Acuan ISO: ISO 9001:2015 9.1.1, 9.1.3, 10.3, 7.5.3; ISO/IEC 27001:2022 Annex A 5.12; satu label "(USULAN, perlu konfirmasi konsultan)" |

## 4. Hasil uji

- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-REG-03.json /tmp/pen-MKT-REG-03/MKT-REG-03.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-03/MKT-REG-03.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "24 butir (USULAN) menunggu ACC" (keluaran di /tmp/pen-MKT-REG-03/lint_final.json). Lulus sejak putaran pertama; putaran berikutnya hanya perbaikan bahasa, istilah, dan lebar kolom.
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-MKT-REG-03/MKT-REG-03.docx` memberi "All validations PASSED!".
- Pratinjau soffice ke PDF, 12 halaman. Lembar kontak 45 dpi dan halaman 10 pada 80 dpi dilihat: Identity, Approval, TOC, sepuluh bagian, dan empat tabel (10 baris kosong tiap tabel) tampil. Draf pertama memotong kata di judul kolom Tabel 4 ("Diserahka n", "Qualificatio n"); kolom itu dikurangi satu dan lebarnya disesuaikan, dan pratinjau ulang menunjukkan judul utuh. Halaman lain tidak dibaca satu per satu pada resolusi penuh (UNMEASURED). Judul kolom Istilah | Arti di Definisi jatuh sendirian di dasar halaman 5 pada pratinjau soffice; itu perilaku renderer, bukan isi, dan tidak diubah.
- Skrip kecil: kode SNX di badan (SNX-COM-REG-01, SNX-COM-SOP-01, SNX-HR-JA-01, SNX-HR-ORG-01, SNX-ISMS-PRO-01, SNX-MKT-REG-01, SNX-MKT-REG-02, SNX-MKT-RPT-01) sama persis dengan tabel Dokumen Terkait: nol kurang, nol lebih. Em-dash dan en-dash di badan: nol. Pencarian "tim", "penyusun", "dokumen sumber", "draf ini", "pelanggan", "belum ada", "memastikan", "secara" (satu kemunculan sah: "secara tertulis" di arti USULAN), tanda kutip dan tanda tebal: nol. Langkah di Cara Mengisi: paling panjang 26 kata.
- Lint dan validator hanya membuktikan format dan larangan pola. Kebenaran isi terhadap bahan diperiksa lewat tabel di atas.

## 5. Keputusan data dan pemetaan peran

- Nama dan jabatan di blok Approval persis dari prompt. Di badan hanya nama jabatan, tanpa nama orang. Samuel di badan = "Direktur Utama". COO tidak disebut di badan, jadi aturan "Direktur (COO)" tidak terpakai. Tiket Zammad dan GLPI, vault, dan PPN tidak relevan dan tidak disebut.
- Klasifikasi header INTERNAL (prompt). Register terisi memuat nama lead (customer sasaran penjualan), jadi butir 4.14 menetapkan RESTRICTED (Internal) sebagai USULAN, selaras dengan SNX-COM-SOP-01 butir 4.13 (OI-8).
- Istilah tunggal: lead, serah terima lead (dengan padanan "lead handover" di Definisi), laporan lead generation, evaluasi kualitas lead, Sales Stage, Status Qualification, feedback, campaign. "Ringkasan" hanya dipakai untuk kolom Ringkasan Feedback.
- Peran dibedakan: Brand & Marketing menyerahkan dan mencatat; Business Development mencatat di CRM, menilai, dan menyampaikan status dan feedback; VP Commercial pemilik, menetapkan kriteria kualitas, dan meninjau.
- Angka dari sumber: tidak ada yang disalin. Target 2 dan 3 leads per bulan di KPI tidak dipakai; hanya satuan per bulan yang dirujuk sebagai dasar periode (USULAN). Jumlah 10 baris per tabel adalah ukuran tata letak, bukan klaim volume.

Pemetaan peran sumber ke nama peran di bagian Peran (basis: specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Marketing, Brand & Marketing (JA-06) | Brand & Marketing | JA-06; sama dengan HR-ORG-01 dan COM-SOP-01 |
| Sales, Sales Executive, "Commercial" sebagai penerima di JA-06 | Business Development | JA-07; sama dengan COM-SOP-01 (tafsir berlabel USULAN di sana dan di Definisi Sales) |
| VP of Commercial | VP Commercial | JA-03 |
| Delivery | tidak dipakai di badan selain kata "handover proyek ke Delivery" di pengecualian | Hanya untuk membedakan dari serah terima lead |

## 6. Penanganan cacat context/audit

Perintah: `grep -n "Marketing Lead & Campaign Outc" context/audit/*.md`. Hasil: 0 baris. Tidak ada bagian dokumen dan tidak ada bagian 5 yang bernama itu, karena register ini T2 tanpa sumber. Saya mencari cacat yang bersinggungan lewat `grep -n -i "marketing\|MKT" context/audit/*.md` dan `grep -n -i "lead\b" context/audit/*.md`, lalu membaca bagian 5 Catatan kualitas dan celah Sales SOP (fileId 19Hex8...), bagian KPI COMMERCIAL & MARKETING (fileId 1TNg8M...), dan baris JA-06 di Job Analysis.

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Sales SOP: "Tidak ada tenggat untuk follow-up lead, approval internal, atau handover; hanya CRM 24 jam (hal. 13) dan batas respons komunikasi (hal. 14)." (audit baris 997) | Tidak ada tenggat serah terima, penyampaian status, atau feedback yang dikarang. Dokumen tidak punya baris SLA. Open item OI-6 |
| 2 | Sales SOP: "Alat yang dirujuk SOP hanya "CRM" (hal. 13), tanpa nama produk CRM." (audit baris 1000) | Dokumen menulis "CRM" saja. Format nomor atau nama catatan di CRM tidak dikarang: kolom Rujukan CRM. Open item OI-5 |
| 3 | KPI: "Lead Generation / MQL | Minimal 3 Leads/bulan dan 1 MQL/bulan (bobot 0.1) | Minimal 2 Leads/bulan dan 1 MQL/bulan (bobot 0.05)" (audit baris 502): dua blok KPI bertarget berbeda | Tidak ada angka KPI di dokumen. Target dikecualikan dari scope dan menunjuk berkas KPI. Hanya satuan per bulan yang dirujuk (butir 4.12, USULAN). Open item OI-3 |
| 4 | KPI: nama "Zilly" (B15) vs "Zily" (nama sheet, blok OLD) (audit baris 543) | Dipakai "Zilly Dwinata" sesuai config/defaults.json dan JA-06. Tidak ada nama orang di badan |
| 5 | Sales SOP: komposisi tim tidak konsisten ("tim Commercial yang saat ini terdiri dari: Business Development" vs isi yang menyebut Sales Executive) (audit baris 992) | Dipakai nama peran HR-ORG-01: Business Development, Brand & Marketing, VP Commercial |
| 6 | Sales SOP: Stage 1 menyebut "inbound leads dari Marketing" tetapi tidak ada form atau rekaman serah terima, dan "Tidak ada form handover bernomor" untuk handover ke Delivery (audit baris 817 dan bagian 4) | Register ini menjadi rekaman serah terima lead (Tabel 1 dan 2). Serah terima ke Delivery dikecualikan dan dibedakan di Definisi |
| 7 | JA-06 nomor 6 menulis penerima "Commercial" dan menyerahkan "qualified leads", sedangkan SNX-COM-SOP-01 menempatkan qualification di Business Development dan penerima Business Development | Penerima = Business Development; Status Qualification diambil dari Sales Stage CRM yang Business Development sampaikan (USULAN). Open item OI-1 dan OI-2 |
| 8 | Sales SOP: KPI SOP (9 butir) tidak identik dengan KPI deck dan KPI individu, tanpa bobot atau target | Di luar scope register; tidak ada KPI di badan selain rujukan nama berkas pada butir 4.12 |

## Asumsi

- A1. "Sales" di kriteria dibaca sebagai fungsi penjualan Commercial, dijalankan Business Development (Definisi Sales, USULAN). Tidak ada jabatan bernama Sales di SNX-HR-ORG-01.
- A2. "Hasil marketing yang diteruskan ke Sales" dibaca sebagai lead yang Brand & Marketing serahkan. Lead yang Business Development peroleh sendiri lewat prospecting dikecualikan karena bukan hasil marketing (baris 1 tabel pengecualian).
- A3. "Status qualification bila tersedia" dibaca sebagai Sales Stage lead di CRM yang Business Development sampaikan. Kolom dibiarkan kosong bila belum ada. Nilai status bersumber dari SNX-COM-SOP-01 butir 4.7 yang sendiri berlabel USULAN.
- A4. "Feedback dari Sales" dibaca sebagai tanggapan tertulis Business Development kepada Brand & Marketing tentang lead yang diserahkan. Arah ini mengikuti checklist, bukan kalimat "memberi campaign feedback" di tabel peran SNX-COM-SOP-01 (OI-2).
- A5. "Laporan lead generation" dibaca sebagai hitungan lead per periode, sumber lead, dan campaign asal (Tabel 3). "Evaluasi kualitas lead" dibaca sebagai hitungan lead per Sales Stage, ringkasan feedback, tindak lanjut, dan tinjauan VP Commercial (Tabel 4). Kriteria kualitas tidak dikarang; sampai VP Commercial menetapkannya, evaluasi hanya memakai Status Qualification dan feedback.
- A6. Tabel 2 menyimpan Sales Stage terbaru, bukan riwayat. Riwayat perubahan tidak dirancang (OI-9).
- A7. Register berupa docx dengan 10 baris kosong per tabel, mengikuti pola SNX-COM-REG-01. Bentuk pakai harian tidak diputuskan (OI-8).
- A8. Kolom Rujukan CRM dan butir 4.4 mengasumsikan Brand & Marketing dapat membaca nomor atau nama catatan lead dari Business Development. Akses Brand & Marketing ke CRM tidak diketahui (OI-5).

## USULAN

Diubah W9: hitungan lint sesudah W9 = 21 butir USULAN (angka di paragraf ini dari sebelum W9). 28 kemunculan "(USULAN)" di spec sesudah sweep (dihitung `grep -o`; 24 sebelum sweep), ditambah satu "(USULAN, perlu konfirmasi konsultan)" di Acuan ISO. Dikelompokkan jadi 18 butir. Pemutus yang disarankan memakai kelompok: owner, Samuel, Aziz, FAT, Legal, Fani.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U-01 | Business Development menjalankan fungsi Sales (pemetaan dari "Sales" di checklist dan Sales SOP) | Definisi Sales; Peran | owner |
| U-02 | Pembagian tugas pada tabel Peran: Brand & Marketing pencatat, Business Development penyampai status dan feedback, VP Commercial pemilik | Peran | owner |
| U-03 | Brand & Marketing mencatat lead di Tabel 1 saat menyerahkannya | Butir 4.3 | owner |
| U-04 | Brand & Marketing menulis rujukan catatan CRM di Tabel 1 | Butir 4.4; kolom Rujukan CRM | owner |
| U-05 | Business Development menyampaikan Sales Stage kepada Brand & Marketing, yang menulisnya di Tabel 2; status terbaru menggantikan nilai lama | Butir 4.6 dan 4.7 | owner |
| U-06 | Daftar nilai Sales Stage (Leads, Qualified, Opportunity, Bid, Win, Lost, Future Nurture) dipakai sebagai nilai Status Qualification; daftar itu berlabel USULAN di SNX-COM-SOP-01 | Definisi Sales Stage | owner |
| U-07 | Business Development menyampaikan feedback kepada Brand & Marketing, yang menulisnya di Tabel 2 | Butir 4.8 | owner |
| U-08 | Laporan lead generation di Tabel 3 disusun Brand & Marketing dari Tabel 1 | Butir 4.9 | owner |
| U-09 | Evaluasi kualitas lead di Tabel 4 dari Status Qualification dan feedback; VP Commercial menetapkan kriteria kualitas; sampai itu hanya dua isian Tabel 2 | Butir 4.10 | owner |
| U-10 | Tindak lanjut di Tabel 4 oleh Brand & Marketing; tinjauan Tabel 3 dan 4 oleh VP Commercial | Butir 4.11 | owner |
| U-11 | Periode Tabel 3 dan 4 satu bulan kalender, mengikuti satuan per bulan pada KPI | Butir 4.12 | owner |
| U-12 | Lead tanpa campaign diisi Tanpa campaign | Butir 4.13 | owner ; diubah W9 R2: kolom Campaign Asal memuat nama Aktivitas di SNX-MKT-REG-02; nilai Tanpa campaign tetap untuk lead tanpa Aktivitas |
| U-13 | Register terisi berklasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 butir 4.3 | Butir 4.14; Rekaman; Acuan ISO | Fani (pemilik SNX-ISMS-PRO-01) dan owner |
| U-14 | Register hanya memuat nama perusahaan atau institusi lead; kontak orang tetap di CRM | Butir 4.15; Ruang Lingkup baris 7 | Legal (pelindungan data pribadi) dan owner |
| U-15 | Folder Google Drive departemen Marketing sebagai lokasi, pemilik VP Commercial, pencatat Brand & Marketing; retensi belum ditetapkan | Butir 4.16; Rekaman | owner dan Legal (retensi) |
| U-16 | Struktur kolom Tabel 1 sampai Tabel 4 dan 10 baris per tabel | Isi Register | owner |
| U-17 | Batas cakupan empat dokumen Marketing: SNX-MKT-RPT-01 = rencana pemasaran dan tinjauan kinerja; SNX-MKT-REG-01 = persetujuan materi eksternal dan validasi klaim; SNX-MKT-REG-02 = pelaksanaan campaign dan aktivitas, dengan materi tertaut ke ID persetujuan di SNX-MKT-REG-01; register ini = hasil lead dan serah terima ke Sales, merujuk nama campaign di SNX-MKT-REG-02. Tabel 3 dan 4 sebagai data masukan SNX-MKT-RPT-01 | Ruang Lingkup (kalimat pengantar dan baris 3 sampai 5); Dokumen Terkait | owner ; diubah W9: batas sudah diputus owner (A8), label USULAN pada batas dihapus; REG-01 satu-satunya register materi, konten, dan persetujuan klaim; REG-02 merujuk Aktivitas, bukan campaign saja |
| U-18 | Klausul ISO 9001:2015 9.1.1, 9.1.3, 10.3, 7.5.3 dan ISO/IEC 27001:2022 Annex A 5.12, label "(USULAN, perlu konfirmasi konsultan)"; peninjauan register tahunan oleh VP Commercial | Acuan ISO; Kesimpulan | owner (meneruskan ke konsultan) |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-1 | JA-06 nomor 6 menulis Brand & Marketing menyerahkan "qualified leads ke Commercial beserta sumber dan statusnya", artinya status mungkin ditetapkan Brand & Marketing (MQL) saat serah terima. SNX-COM-SOP-01 butir 4.6 menempatkan qualification di Business Development. Register memakai Sales Stage dari Business Development dan tidak punya kolom status MQL dari Brand & Marketing. Perlu diputus siapa menetapkan status pada serah terima | owner |
| OI-2 | Arah campaign feedback ambigu: Sales SOP 09 menulis "Marketing | Lead generation; Campaign feedback; Event collaboration" sebagai lingkup kolaborasi Sales, sedangkan tabel peran SNX-COM-SOP-01 menulis Brand & Marketing "memberi campaign feedback". Register mengikuti checklist (feedback dari Sales ke Brand & Marketing) | owner |
| OI-3 | Definisi MQL dan padanannya dengan Sales Stage Qualified belum ada. KPI Lead Generation dan MQL di KPI COMMERCIAL & MARKETING.xlsx punya dua blok bertarget berbeda (3 dan 2 leads per bulan). Register tidak memuat angka target | owner |
| OI-4 | Daftar nilai Sumber Lead tidak ada. Brand & Marketing menulis nama saluran apa adanya (langkah 6.4); nama yang tidak seragam mengacaukan hitungan Tabel 3 | owner |
| OI-5 | Nama produk CRM, format nomor atau nama catatan lead, dan akses Brand & Marketing ke CRM tidak disebut di bahan mana pun. Kolom Rujukan CRM bergantung pada ketiganya | owner |
| OI-6 | Tenggat serah terima lead, penyampaian Sales Stage, dan feedback tidak ada di bahan mana pun (Sales SOP hanya memuat batas CRM dan respons komunikasi). Dokumen tidak punya baris SLA | owner |
| OI-7 | Retensi register dan lokasi folder Google Drive departemen Marketing (U-15) | Legal dan owner |
| OI-8 | Header INTERNAL (worklist) berbeda dengan butir 4.14 (register terisi RESTRICTED (Internal)). Bila header diubah, footer berlabel otomatis. Bentuk pakai harian (docx dengan 10 baris per tabel atau lembar kerja) juga belum diputus | owner dan Fani |
| OI-9 | Tabel 2 hanya menyimpan Sales Stage terbaru. Perlu keputusan apakah riwayat perubahan status dicatat di register atau cukup di CRM | owner |
| OI-10 | Isi SNX-MKT-REG-02 (acuan nama campaign) dan SNX-MKT-RPT-01 (review kinerja) belum dikonfirmasi saat register ini disusun. Kolom Campaign Asal dan pembagian lingkup dengan RPT-01 perlu dicocokkan setelah kedua dokumen selesai. Batas cakupan empat dokumen Marketing berstatus USULAN (U-17); checklist baris 58 memuat seluruh isi Description baris 57 ditambah validasi klaim dan kolom produk/layanan, klaim, sumber/bukti, sehingga isinya cocok dengan judul baris 57 sementara judul baris 58 adalah Campaign & Activity Register | owner ; diubah W9: owner memutus A8; batas empat dokumen sudah diputus (label USULAN pada batas dihapus) dan REG-02 sudah memakai nama Aktivitas; kolom Campaign Asal cocok dengan Nama Aktivitas di Tabel 1 REG-02. Temuan baris 58 pindah ke OI-13 |
| OI-11 | Klausul ISO belum dicocokkan dengan teks standar (tidak ada salinan di repo); konsultan menetapkan klausul final | owner (meneruskan ke konsultan) |
| OI-12 | Kalimat perintah kepada AI di bahan dan di berkas context/audit: nihil | tidak ada |

## 7. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI, dan perbaikannya:

1. Draf pertama menyebut hasil yang sama dengan dua nama: "ringkasan lead generation" di badan dan "laporan lead generation" di Rekaman. Disatukan jadi "laporan lead generation"; "ringkasan" hanya tersisa di nama kolom Ringkasan Feedback.
2. Draf pertama memakai "penyerahan lead" di langkah 6.2 dan "serah terima lead" di tempat lain. Disatukan jadi "serah terima lead", dengan "lead handover" hanya di Definisi sebagai padanan kata checklist.
3. Tiga baris tabel pengecualian dibuka dengan "Dicatat di" dan "Ditetapkan di" (pasif tanpa pelaku). Diganti "Menjadi lingkup", "Ada di", dan "Target ada di".
4. Tabel Peran mengulang butir 4.x kalimat demi kalimat. Baris Brand & Marketing dipadatkan jadi satu kalimat plus rujukan nomor butir; Business Development dan VP Commercial tetap pendek.
5. Kontak orang di lead disebut penuh dua kali (Ruang Lingkup dan butir 4.15). Ruang Lingkup kini hanya merujuk butir 4.15.
6. Tabel 4 draf pertama punya kolom Jumlah Lead Diserahkan yang mengulang Tabel 3 dan memaksa langkah sinkronisasi. Kolom dan langkahnya dibuang; jumlah lead per periode cukup di Tabel 3.
7. Label (USULAN) sempat dipasang tiga kali dalam satu butir 4.10 dan satu kali pada baris Business Development di Peran, padahal kalimat pengantar tabel Peran sudah berlabel. Dikurangi jadi dua label pada butir 4.10 dan nol pada baris itu.
8. Sisa pola yang saya terima: kalimat berawal "Brand & Marketing menulis ..." berulang di Cara Mengisi. Itu mengikuti aturan satu langkah, satu pelaku, dan sengaja tidak diganti sinonim.

Adakah fakta, angka, nama, atau tanggal tanpa sumber, dan hasilnya:

1. Fakta bersumber dan berkutip di tabel Fakta kunci dan Fakta pendukung: nama jabatan (HR-ORG-01), tugas JA-06, peran Brand & Marketing dan CRM (COM-SOP-01), lima kriteria qualification dan nilai Sales Stage (COM-SOP-01 butir 4.6 dan 4.7), RESTRICTED untuk informasi customer (PRO-01 butir 4.3), satuan per bulan KPI.
2. Tanpa sumber dan berlabel (USULAN) atau "Belum ditetapkan": seluruh U-01 sampai U-18, termasuk lokasi folder, pencatat, periode satu bulan kalender, jumlah 10 baris (ukuran tata letak), dan klausul ISO.
3. Angka: nol angka tanpa sumber di badan. Angka "lima kriteria" bersumber COM-SOP-01 butir 4.6. Angka KPI (2 dan 3 leads per bulan) sengaja tidak disalin.
4. Nama orang di badan: nol. Nama di blok Approval persis dari prompt. Tanggal: nol; Effective Date kosong.
5. Klausul ISO dikutip dari ingatan tanpa salinan standar; judul dan nomornya berlabel (USULAN, perlu konfirmasi konsultan) dan tercatat di OI-11.

## Sweep

Putaran penghalusan sesudah DONE (instruksi /tmp/claude-0/prompts/MKT-REG-03.sweep.txt). Dua butir diubah, semuanya di Ruang Lingkup dan Dokumen Terkait. Fakta, angka, nama, dan struktur lain tetap. Temuan nonblocking lain di qa/MKT-REG-03.verify.json tidak diubah karena di luar butir sweep.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Pengecualian Ruang Lingkup baris 3 menaruh perencanaan campaign di MKT-REG-02 sekaligus MKT-RPT-01 | Baris "Perencanaan dan pelaksanaan campaign dan aktivitas marketing | Menjadi lingkup SNX-MKT-REG-02 ..." dan baris "Perencanaan dan review kinerja marketing | Menjadi lingkup SNX-MKT-RPT-01 ..." | Baris menjadi "Pelaksanaan campaign dan aktivitas marketing | Menjadi lingkup SNX-MKT-REG-02 ... (USULAN)"; perencanaan hanya di baris SNX-MKT-RPT-01 |
| 2a | Batas cakupan dokumen Marketing (USULAN, pemutus owner), tabel pengecualian | Tabel tanpa baris untuk SNX-MKT-REG-01; kalimat pengantar "Butir berikut dikecualikan dari register ini:" | Kalimat pengantar menambah "Pembagian isi antara SNX-MKT-REG-01, SNX-MKT-REG-02, SNX-MKT-RPT-01, dan register ini berstatus (USULAN)." Baris baru "Persetujuan materi eksternal dan validasi klaim | Menjadi lingkup SNX-MKT-REG-01 (USULAN)." Baris SNX-MKT-RPT-01 menjadi "Rencana pemasaran dan tinjauan kinerja marketing: sasaran, audiens, positioning, channel, rencana aktivitas, KPI, realisasi, evaluasi, dan tindakan korektif | Menjadi lingkup SNX-MKT-RPT-01 ... (USULAN)" |
| 2b | Batas cakupan, tabel Dokumen Terkait | SNX-MKT-REG-02 "Tempat nama campaign dicatat ..."; SNX-MKT-RPT-01 "Review kinerja marketing yang berada di luar register ini."; tanpa baris SNX-MKT-REG-01 | Baris SNX-MKT-REG-01 ditambah ("Persetujuan materi eksternal dan validasi klaim (USULAN)"); SNX-MKT-REG-02 menjadi "Pelaksanaan campaign dan aktivitas marketing, dengan materi yang dipakai tertaut ke ID persetujuan di SNX-MKT-REG-01. Kolom Campaign Asal merujuk nama campaign di register itu (USULAN)"; SNX-MKT-RPT-01 menjadi "Rencana pemasaran dan tinjauan kinerja marketing (USULAN)" |
| 2c | Isi register ini tidak ditaruh di register lain | Lingkup register ini: lead yang diserahkan, laporan lead generation, evaluasi kualitas lead | Tidak berubah. Register ini tetap hanya memuat hasil lead dan serah terima ke Sales dan merujuk nama campaign di SNX-MKT-REG-02; rencana, realisasi KPI, dan evaluasi kinerja pemasaran umum ada di SNX-MKT-RPT-01, dan Tabel 3 dan 4 hanya menjadi data masukannya (USULAN) |

Catatan USULAN: label (USULAN) naik dari 24 ke 28 kemunculan; butir U-17 dan OI-10 di atas diperbarui. Tidak ada fakta atau angka baru; batas cakupan berasal dari instruksi orkestrator dan berstatus USULAN dengan pemutus owner.

Hasil uji sweep:
- `python3 -I tools/render_sop.py ...` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-03/MKT-REG-03.docx generic`: `"pass": true`, `"fails": []`, satu warn (28 butir USULAN).
- `python3 /mnt/skills/public/docx/scripts/office/validate.py`: All validations PASSED.
- `python3 -I reports/orch/blankscan.py`: ok, 12 halaman, daftar halaman kosong `[]`.
- Skrip kecil: kode SNX di badan (delapan kode, termasuk SNX-MKT-REG-01) sama persis dengan tabel Dokumen Terkait; em-dash dan en-dash nol.

## ISO-W9

Putaran ISO-W9 (LEAD G-3 A8; owner GO). REG-03 tetap untuk lead dan hasil; struktur tabel tidak berubah. Batas tulis: specs/MKT-REG-03.json dan notes/MKT-REG-03.md. Meta dan blok approval tidak berubah (sama dengan defaults v22 MKT). Tujuan rujukan (REG-02 Tabel 1, REG-01, RPT-01) ada dan cocok isinya.

| Butir | Sebelum | Sesudah |
|---|---|---|
| Ruang Lingkup pengantar pengecualian | "Pembagian isi antara REG-01, REG-02, RPT-01, dan register ini berstatus (USULAN)" | kalimat dihapus (batas diputus) |
| Pengecualian baris REG-02 | "Pelaksanaan campaign dan aktivitas marketing ... nama campaign di sana (USULAN)" | "Pelaksanaan Aktivitas pemasaran ... hanya merujuk nama Aktivitas di sana lewat kolom Campaign Asal" |
| Pengecualian baris REG-01 | "(USULAN)" | "satu-satunya register materi, konten, dan persetujuan klaim"; label dihapus |
| Pengecualian baris RPT-01 | "Tabel 3 dan Tabel 4 dapat menjadi data masukan tinjauan itu (USULAN)" | Brand & Marketing mengisi RPT-01 dari register ini dan REG-02; Tabel 3 dan Tabel 4 menjadi data masukan |
| Dokumen Terkait REG-01 | persetujuan materi dan validasi klaim (USULAN) | satu-satunya register materi, konten, dan persetujuan klaim, termasuk validasi klaim |
| Dokumen Terkait REG-02 | materi tertaut ke ID persetujuan; nama campaign (USULAN) | kolom yang dicatat REG-02 (nama, tujuan, Channel, jadwal, PIC, Budget, status, ID materi, hasil singkat); nama Aktivitas; label dihapus |
| Dokumen Terkait RPT-01 | (USULAN) | label dihapus; Brand & Marketing mengisi RPT-01 dari register ini dan REG-02 |

Open item yang ditutup atau diubah W9: lihat kolom Pemutus pada tabel Open items. Open item baru:

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-13 | Description checklist baris 58 berisi pengendalian materi baris 57 yang diperluas dengan validasi klaim, bukan pelaksanaan campaign sesuai judulnya (Marketing Campaign & Activity Register); perlu dibetulkan Brand & Marketing. Pengukuran: teks baris 58 tidak identik dengan baris 57. | Brand & Marketing |
| OI-14 | REG-02 tidak lagi punya kolom Jenis, jadi kolom Campaign Asal di sini menerima nama Aktivitas apa pun (campaign, event, atau webinar). Istilah Campaign di Definisi tetap "kegiatan marketing yang tercatat dengan nama di SNX-MKT-REG-02" | owner ; diubah R2: Definisi Campaign kini "Aktivitas pemasaran SINUX yang tercatat dengan nama Aktivitas di SNX-MKT-REG-02" dan Campaign Asal ditulis dengan nama Aktivitasnya |
| OI-15 | A3: dokumen ini tidak menyebut JA-03 atau JA-04 dan tidak menyebut atasan atau garis lapor keduanya; tidak ada yang diselaraskan | - |

Uji (spec W9): render, `lint_doc.py ... generic`: pass true, fails kosong, 21 butir USULAN; `validate.py`: All validations PASSED; `blankscan.py`: ok 12 halaman []; `w9diff.py MKT-REG-03`: diff hanya baris di tabel di atas.

### ISO-W9 R2

| Butir | Sebelum | Sesudah |
|---|---|---|
| R2 butir 3, Definisi Campaign | "Kegiatan marketing SINUX yang tercatat dengan nama di SNX-MKT-REG-02." | "Aktivitas pemasaran SINUX yang tercatat dengan nama Aktivitas di SNX-MKT-REG-02." |
| R2 butir 3, Definisi Campaign Asal | "Campaign yang menghasilkan sebuah lead." | "Campaign di SNX-MKT-REG-02 yang menghasilkan sebuah lead, ditulis dengan nama Aktivitasnya." |
| R2 butir 3, butir 4.13 | "Lead yang tidak berasal dari campaign diisi Tanpa campaign ..." | "Lead yang tidak berasal dari Aktivitas di SNX-MKT-REG-02 diisi Tanpa campaign ..."; aturan dan nilai isian tidak berubah |
| R2 butir 3, Cara Mengisi 6.5 | "menulis nama campaign di kolom Campaign Asal ... bila lead tidak berasal dari campaign" | "menulis nama Aktivitas di kolom Campaign Asal ... bila lead tidak berasal dari Aktivitas di register itu" |

Hygiene R2 butir 4: USULAN U-12, U-17 dan OI-14 kini memuat "diubah W9" di barisnya sendiri; hitungan label USULAN dikoreksi.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Butir 4.10 asli: "4.10 Brand & Marketing menyusun evaluasi kualitas lead di Tabel 4 dari Status Qualification terbaru dan feedback di Tabel 2 (USULAN). VP Commercial menetapkan kriteria kualitas lead. Kriteria itu belum ditetapkan. Sampai ada penetapan, evaluasi hanya memakai dua isian Tabel 2 tersebut (USULAN)." Dua label digabung jadi satu di akhir butir (STYLE §3.5); kalimat disusun ulang sehingga label tetap meliputi evaluasi Tabel 4 dan aturan sementaranya. Butir 4.10 tetap berstatus USULAN.
### W10 kalimat dihapus atau dipindah
- Ruang Lingkup, baris Kontak orang di lead: "Aturannya ada di butir 4.15." diganti faktanya: "Register ini hanya memuat nama perusahaan atau institusi lead."
- Ruang Lingkup, baris Target: "Target ada di KPI COMMERCIAL & MARKETING.xlsx." ditulis "Target ditetapkan di ...". Baris Feedback customer: "Ada di SNX-COM-REG-01." ditulis "Dicatat di SNX-COM-REG-01."
- Tabel Peran: rujukan "(butir 4.2 sampai 4.4, 4.6 sampai 4.13, 4.15, dan 4.16)", "(butir 4.4 sampai 4.6 dan 4.8)", "(butir 4.10 dan 4.11)" dihapus. Paragraf pembuka: "Pembagian tugas berikut berstatus (USULAN)." dipindah ke akhir paragraf.
- Cara Mengisi: "(butir 4.1 dan 4.3)" di 6.1 diganti faktanya (pada saat lead diserahkan); "(butir 4.13)" di 6.5, "(butir 4.4)" di 6.6, "(butir 4.8)" di 6.9, "(butir 4.11)" di 6.16 dan 6.17 dihapus; 6.7 "(butir 4.6 dan 4.7)" jadi "(butir 4.7)"; 6.11 "(butir 4.9 dan 4.12)" jadi "(butir 4.12)"; 6.13 "(butir 4.10 dan 4.12)" jadi "(butir 4.10)".
- Rekaman, paragraf pembuka: "Lokasi, pemilik, dan retensi berikut berstatus (USULAN). Retensi belum ditetapkan." ditulis satu kalimat.
### W10 selisih angka
nihil (subst_diff kosong).
### W10 catatan
- Pihak luar: "customer" (satu-satunya sebutan di dokumen ini).
- Definisi CRM: "aktivitas penjualan" ditulis "kegiatan penjualan" agar "Aktivitas" hanya berarti Aktivitas di SNX-MKT-REG-02; "rencana aktivitas" ditulis "rencana Aktivitas".
- Istilah Marketing English: lead, campaign, claim (jembatan "claim (klaim)" di Ruang Lingkup), content; "record (rekaman)" di butir 4.16.
- Tabel isian min_row_cm 0.7 (0.8 menaikkan halaman jadi 13); lebar kolom tabel Record, Acuan ISO, dan Dokumen Terkait diatur ulang agar halaman tetap 12.

### W10 putaran perbaikan 1 (worker, temuan qa/MKT-REG-03.w10.r1.json)
- "6.1 Tulis satu baris di Tabel 1 untuk setiap lead pada saat lead diserahkan kepada Business Development." ditambah label (USULAN) di akhir: fakta ini menggantikan rujukan ke butir berlabel (USULAN) (usul_butir 6.1).
- "Menjadi isi CRM. Register ini hanya memuat nama perusahaan atau institusi lead." ditambah label (USULAN) di akhir: fakta ini menggantikan rujukan ke butir berlabel (USULAN) (usul_butir -).
