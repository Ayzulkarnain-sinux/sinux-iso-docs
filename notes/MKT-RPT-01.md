# Catatan penyusun MKT-RPT-01: Marketing Planning & Performance Review

Status: DRAFTED (spec + notes ada). Spec: specs/MKT-RPT-01.json. Mode generic, aksi T2 tanpa sumber, wave W7, nomor SNX-MKT-RPT-01 (nomor SNX lama dipertahankan), department Marketing, classification INTERNAL, audit_class None. doc_type_cover "REPORT", doc_type_label "Report". Approval persis dari prompt dan config/defaults.json (MKT): prepared Zilly Dwinata / Brand & Marketing, reviewed Laras Rasmawati / VP Commercial, approved Samuel Kristanto Utomo / President Director. status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "VP Commercial" (jabatan, tanpa nama): aturan dokumen tanpa sumber = jabatan reviewer departemen (config/defaults.json, process_owner.rule, status USULAN). Catatan worklist kosong.

Hasil uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-RPT-01.json /tmp/pen-MKT-RPT-01/MKT-RPT-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-RPT-01/MKT-RPT-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "32 butir (USULAN) menunggu ACC" (hasil sesudah putaran sweep). Keluaran tersimpan di /tmp/pen-MKT-RPT-01/lint_final.txt.
- Tata letak: docx dikonversi ke PDF dengan soffice (15 halaman). Seluruh halaman dilihat pada 50 dpi, halaman 9 sampai 14 dilihat lagi pada 70 dpi, dan halaman 12 pada 80 dpi sesudah lebar kolom diperbaiki. Judul kolom tabel B2 sempat terpotong di tengah kata ("Pelaksanaa/n") dan kode AKT-n terbelah; lebar kolom disetel ulang dan sudah terbaca. Kolom retensi di tabel Rekaman sempat sempit dan rata kiri-kanan renggang; dilebarkan. Putaran perbaikan 1: tabel B2 diubah (kolom Aktivitas diganti Rujukan Catatan) dan halaman 12 dilihat lagi pada 80 dpi; judul kolom dan kode AKT-n terbaca penuh. Yang tersisa: tabel A6 dan B4 serta Rekaman terbelah antar halaman di render LibreOffice. Itu tata letak, bukan isi; tampilan di Word perlu dilihat orang (HUMAN-VERDICT).
- Skrip pemindai atas teks spec: tiap kode SNX di badan ada di tabel Dokumen Terkait (7 kode, nol kurang, nol berlebih). Nol em-dash, nol en-dash, nol frasa meta ("draf ini", "dokumen sumber", "sumber tim", kata "penyusun"), nol "belum ada".
- Putaran perbaikan 1: `python3 validate.py /tmp/pen-MKT-RPT-01/MKT-RPT-01.docx` (validator skill docx, /mnt/skills/public/docx/scripts/office) = "All validations PASSED!". `python3 -I reports/orch/blankscan.py /tmp/pen-MKT-RPT-01/MKT-RPT-01.docx` = `ok 15 MKT-RPT-01.docx []`. tools/selftest.sh tidak saya jalankan (menulis ke /tmp/selftest yang dipakai bersama). Lint hanya membuktikan format dan larangan pola; kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.
- spec dibangun dengan skrip Python di scratchpad sesi (di luar repo, tidak ikut dikirim). Berkas yang saya tulis di repo hanya specs/MKT-RPT-01.json dan notes/MKT-RPT-01.md.

## 1. Sumber

Prompt menyatakan sumber: tidak ada (T2 tanpa sumber; config/worklist.json: `"sources": []`). Alat Drive dimuat dan dipakai hanya untuk baca (get_file_metadata, read_file_content, download_file_content); nol tulis ke Drive. Dua berkas Drive dibaca sebagai bahan pendukung karena uraian jabatan dan lembar KPI Brand & Marketing berada di dalamnya.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Kriteria penerimaan: Checklist ISO SINUX - 2026, baris 56, kolom Description | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (get_file_metadata hari ini, sama dengan config/checklist.json) | Dibaca dari config/checklist.json. Baris 56: `checked: false`, `fileId: null`, `link_url: null`, `iso_9001: null`, `iso_27001: null` (tidak ada acuan klausul) |
| SINUX_Job_Analysis_2026.docx (JA-03 dan JA-06) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini) | read_file_content, teks penuh dibaca hari ini. Dipakai untuk tugas Brand & Marketing, tugas VP Commercial, dan batasan umum keputusan keuangan |
| KPI COMMERCIAL & MARKETING.xlsx (lembar "KPI Individu - Zily") | 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb | 2026-10-13T06:41:25.963Z (get_file_metadata hari ini) | download_file_content, hasil besar tersimpan ke berkas, didecode di /tmp/pen-MKT-RPT-01/kpi/ dan dibaca dengan `python3 -I` + openpyxl. Dipakai untuk bentuk tabel KPI, sumber Target KPI, dan kolom pengukuran per kuartal. Tidak ada angka dari lembar ini yang disalin ke dokumen |
| Pendukung repo (bukan Drive) | - | - | config/defaults.json v21; specs/HR-ORG-01.json (nama peran dan JA); specs/COM-SOP-01.json (serah terima inbound lead, CRM); specs/ISMS-PRO-01.json (butir 4.3, 4.8, 4.15); specs/MKT-REG-01.json dan specs/MKT-REG-02.json (batas dokumen, dibaca setelah muncul di repo dan dibaca ulang pada putaran perbaikan 1); keputusan cakupan orkestrator untuk REG-01, REG-02, dan REG-03 (berkas instruksi putaran perbaikan 1, status USULAN, pemutus owner); specs/HR-RPT-01.json dan notes/HR-RPT-01.md (pola dokumen REPORT W7). Dibaca sebagai DATA. Spec lane lain masih Draft; kutipan darinya bisa basi |

Kalimat perintah kepada AI di semua bahan: nihil. Kalimat kewajiban di Job Analysis ("harus dikonfirmasi oleh manajemen") adalah isi dokumen itu, bukan instruksi untuk saya.

Pemetaan kriteria baris 56 ke dokumen:

| Unsur Description | Di dokumen |
|---|---|
| marketing objectives | Tabel A2 Marketing Objective |
| target audience | Tabel A3 Target Audience dan Positioning |
| positioning | Tabel A3 (kolom Positioning, satu per Target Audience) |
| channel | Tabel A5 Rencana Aktivitas (kolom Channel) |
| aktivitas | Tabel A5 (rencana) dan B2 Realisasi Aktivitas (kolom Rujukan Catatan menunjuk catatan pelaksanaan di SNX-MKT-REG-02, butir 4.8) |
| timeline | Tabel A5 (kolom Mulai dan Selesai) dan B2 (kolom Tanggal Pelaksanaan) |
| PIC | Tabel A5 (kolom PIC) dan C1 (kolom PIC) |
| budget jika ada | Tabel A6 Budget (ditulis Tidak Ada Budget bila tanpa dana, butir 4.5), B2 (kolom Realisasi Biaya) |
| KPI | Tabel A4 KPI (rumusan dan satuan, Target, Sumber Data) |
| realisasi | Tabel B2 (biaya dan status pelaksanaan) dan B3 Realisasi KPI |
| evaluasi | Kolom Evaluasi di B2 dan B3 (butir 4.11) |
| corrective action bila target tidak tercapai | Tabel C1 dan C2 (butir 4.12 sampai 4.15), dasar ISO 9001:2015 10.2 |
| Bukti: marketing plan | Tabel A1 sampai A7; baris pertama tabel Rekaman |
| Bukti: monthly performance review | Tabel B1 sampai B4; baris kedua tabel Rekaman |
| Bukti: catatan tindak lanjut | Tabel C1 dan C2; baris ketiga dan keempat tabel Rekaman |

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria penerimaan baris 56 memuat dua belas unsur dan tiga bukti. Karena itu dokumen memuat Marketing Plan, Monthly Performance Review, dan Catatan Tindak Lanjut dengan semua sel isian kosong | "Mencakup marketing objectives, target audience, positioning, channel, aktivitas, timeline, PIC, budget jika ada, KPI, realisasi, evaluasi, dan corrective action bila target tidak tercapai." dan "Bukti: marketing plan, monthly performance review, dan catatan tindak lanjut." | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (Checklist ISO SINUX - 2026, baris 56) |
| Brand & Marketing menyusun kalender kampanye, positioning, dan target audience, dan memantau hasilnya. Karena itu Brand & Marketing menjadi pencatat Marketing Plan, Realisasi, dan Evaluasi (butir 4.3, bagian 5) | "Menyusun kalender kampanye, positioning dan target audience sesuai sales priorities." dan "Memonitor reach, engagement, lead dan efektivitas biaya pemasaran." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 (JA-06, Uraian Jabatan A butir 1 dan 5) |
| VP Commercial meninjau aktivitas tim komersial dan tindakan perbaikan atas kesenjangan target. Karena itu VP Commercial menetapkan Tindakan Perbaikan dan memeriksa laporan (butir 4.13 sampai 4.15, USULAN) | "Melakukan peninjauan aktivitas tim komersial dan tindakan perbaikan terhadap kesenjangan target." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 (JA-03, Uraian Jabatan A butir 7) |

## Fakta penting lain dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber dan posisi |
|---|---|---|---|
| 1 | Jenis Aktivitas: campaign, event, webinar (Ruang Lingkup, definisi Aktivitas dan Channel); konten dikendalikan sebagai materi di SNX-MKT-REG-01 (putaran sweep) | "Mengelola event/webinar/campaign serta koordinasi vendor bila ada." dan "Menyiapkan materi brand, konten digital, company profile dan sales collateral." | 1m91..., JA-06 A butir 4 dan 2 |
| 2 | Prioritas Penjualan berasal dari sales plan VP Commercial (definisi, USULAN) | "Menyusun sales plan, target, pipeline dan proyeksi periodik per account/produk." | 1m91..., JA-03 A butir 1. JA-06 menulis "sales priorities" tanpa menyebut dokumennya; pemetaan ke sales plan adalah tafsir (U2) |
| 3 | Persetujuan Budget mengikuti delegasi keuangan yang berlaku (butir 4.6) | "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 1m91..., Batasan umum di bawah E. Wewenang JA-06 |
| 4 | KPI individu Brand & Marketing ada di lembar sendiri, dengan kolom pengukuran per kuartal; sebagian Target berlaku per kuartal dengan pemantauan bulanan (butir 4.7 dan 4.10) | Sel E24: "Traffic website & social media meningkat secara berkala : ≥30% QoQ, dengan monthly monitoring." Sel E26: "Minimal 2 event/webinar/partner activity setiap quarter". Sel G16, K16, O16, S16: "Q1", "Q2", "Q3", "Q4" | 1TNg..., lembar "KPI Individu - Zily" |
| 5 | Lembar KPI memuat bobot, Balancing, dan Score, yang dikecualikan dari laporan ini | Sel F16: "Bobot". Sel I17: "Balancing". Sel J17: "Score". Sel J18: "E x F = G" | 1TNg..., lembar "KPI Individu - Zily" |
| 6 | Periode lembar KPI: 2026 sampai 2027 (Dokumen Terkait) | Sel A7 dan B7: "Periode" dan ": 2026 - 2027" | 1TNg..., lembar "KPI Individu - Zily". Ditulis "2026 sampai 2027" di dokumen |
| 7 | Sumber Data bisa berupa laporan analitik website (definisi Sumber Data) | Sel E25: "100% SEO baseline (keyword mapping, technical SEO audit, Google Search Console/Analytics tracking, dan content/keyword strategy) established." | 1TNg..., lembar "KPI Individu - Zily". Dokumen hanya menulis "laporan analitik website" tanpa nama produk |
| 8 | Brand & Marketing menyerahkan inbound lead ke Business Development, dan Business Development mencatat lead di CRM (peran, definisi CRM, Dokumen Terkait) | "Menyerahkan inbound lead ke Business Development beserta sumber dan statusnya, serta memberi campaign feedback dan berkolaborasi dalam event." dan "CRM; dikelola Business Development (butir 4.3)" | specs/COM-SOP-01.json, tabel peran dan tabel rekaman (spec lokal, bukan berkas Drive) |
| 9 | INTERNAL disimpan di sistem resmi SINUX; informasi pelanggan minimal RESTRICTED; retensi INTERNAL mengikuti master list (butir 4.17, Rekaman, Acuan Klausul ISO) | "INTERNAL disimpan di sistem resmi SINUX (Drive, Zammad, Service Hub, knowledge base)." dan "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan tingkat yang lebih tinggi." dan "INTERNAL disimpan sesuai master list." | specs/ISMS-PRO-01.json, butir 4.8, 4.3, 4.15 |
| 10 | Persetujuan materi eksternal dan validasi klaim dikecualikan ke SNX-MKT-REG-01 (keputusan cakupan putaran perbaikan 1: baris 57 dan 58 ada di REG-01) | Baris 57: "Mengendalikan materi yang digunakan untuk kebutuhan eksternal, termasuk company profile, website, social media, product brochure, presentation deck, campaign material, dan event collateral." Baris 58: "serta memastikan keakuratan informasi dan validasi klaim produk/layanan sebelum dipublikasikan." | config/checklist.json baris 57 dan 58. Baris 58 bukan salinan baris 57: baris 58 memuat isi baris 57 ditambah validasi klaim dan field klaim dan bukti pendukung |
| 11 | Pencatatan lead yang diteruskan ke Sales dikecualikan ke SNX-MKT-REG-03 | "Mencatat hasil marketing yang diteruskan ke Sales, termasuk sumber lead, campaign asal, tanggal serah terima, status qualification bila tersedia, dan feedback dari Sales." | config/checklist.json baris 59 |
| 12 | SNX-MKT-REG-01 dan SNX-MKT-REG-02 menunjuk dokumen ini untuk rencana, anggaran, target, dan evaluasi | REG-01 (dibaca ulang pada putaran perbaikan 1): "Rencana dan evaluasi kinerja marketing" dengan keterangan "Register ini mencatat materinya, bukan hasil kerjanya. Rencana dan evaluasi ada di SNX-MKT-RPT-01 (USULAN)." REG-02: "Perencanaan, anggaran, target, dan evaluasi hasil marketing" dengan keterangan "Dicatat di SNX-MKT-RPT-01 (USULAN)." | specs/MKT-REG-01.json dan specs/MKT-REG-02.json, Ruang Lingkup |
| 13 | KPI individu, bobot, dan sumber data ditetapkan di dokumen terpisah (dasar butir 4.7: Target tidak ditetapkan di laporan ini) | "KPI dalam dokumen merupakan usulan indikator, target numerik, bobot dan sumber data ditetapkan pada KPI Matrix terpisah." | 1m91..., bagian 2 Pedoman Validasi & Keterkaitan ISO |

Pemetaan peran ke SNX-HR-ORG-01 (instruksi: nama peran memakai HR-ORG-01, peran lain dipetakan ke jabatan terdekat dan dicatat di sini): Brand & Marketing = JA-06, VP Commercial = JA-03, Business Development = JA-07, Direktur Utama = JA-01, semua persis sesuai nama di daftar jabatan. "Pencatat" dan "Pemeriksa" di tabel pengesahan adalah label baris tanda tangan, bukan jabatan. "PIC" dan "Atasan" tidak dipetakan ke JA tertentu karena PIC diisi per Aktivitas dengan nama jabatan dari HR-ORG-01. JA-06 butir 6 menulis "Menyerahkan qualified leads ke Commercial"; saya memetakan penerimanya ke Business Development (JA-07) mengikuti SNX-COM-SOP-01 (lihat asumsi 4).

## Pemetaan klausul ISO

Checklist tidak memberi acuan klausul untuk baris 56. Bagian Acuan Klausul ISO memuat enam baris dengan satu label "(USULAN, perlu konfirmasi konsultan)". Judul klausul adalah pengetahuan standar, bukan teks sumber tim, kecuali Annex A 5.12 yang disebut SNX-ISMS-PRO-01 butir 4.1.

| Klausul | Alasan | Catatan |
|---|---|---|
| ISO 9001:2015 6.2 Sasaran mutu dan perencanaan untuk mencapainya | Marketing Plan memuat apa yang dikerjakan (Aktivitas), sumber daya (Budget), penanggung jawab (PIC), kapan selesai (jadwal), dan cara hasil dievaluasi (Monthly Performance Review) | Tafsir penyusun: Marketing Objective diperlakukan sebagai sasaran yang terkait mutu layanan dan kepuasan pelanggan |
| ISO 9001:2015 9.1.1 Pemantauan, pengukuran, analisis, dan evaluasi: Umum | Realisasi, Status Capaian, dan Evaluasi tiap bulan | Judul sub-klausul "Umum" ditulis sebagai akhiran agar tidak ambigu dengan 9.1 |
| ISO 9001:2015 10.2 Ketidaksesuaian dan tindakan korektif | Catatan Tindak Lanjut memuat Tindakan Perbaikan, PIC, status, dan Hasil Pemeriksaan | Memperlakukan Target yang tidak tercapai sebagai ketidaksesuaian terhadap rencana adalah tafsir; konsultan menilai |
| ISO 9001:2015 7.5.3 Pengendalian informasi terdokumentasi | Laporan terisi adalah rekaman yang butuh lokasi, pemilik, klasifikasi | Sama dengan pola SNX-HR-RPT-01 |
| ISO/IEC 27001:2022 7.5.3 | Klausul yang sama untuk ISMS | Hubungan tidak langsung: laporan pemasaran bukan dokumen yang diwajibkan ISMS; konsultan menilai perlu tidaknya |
| ISO/IEC 27001:2022 Annex A 5.12 Klasifikasi informasi | Laporan berklasifikasi INTERNAL dan tidak memuat data pelanggan | Dasar: SNX-ISMS-PRO-01 butir 4.1, 4.3, dan 4.5 |

ISO 9001:2015 8.2.1 (komunikasi dengan pelanggan) dan 9.1.2 (kepuasan pelanggan) tidak dimasukkan: materi pemasaran dikendalikan di SNX-MKT-REG-01, dan laporan ini tidak mengukur kepuasan pelanggan. ISO 9001:2015 9.3 (tinjauan manajemen) tidak dimasukkan karena milik lane konsultan. Konsultan dapat menambahkannya.

## Asumsi dan keputusan desain

1. Satu laporan terisi = satu Periode Rencana. Isinya tiga bukti dari kriteria: Marketing Plan (tabel A1 sampai A7), Monthly Performance Review (B1 sampai B4, disalin tiap bulan), Catatan Tindak Lanjut (C1 dan C2). Kriteria hanya menyebut "monthly", jadi siklus review = bulanan; panjang Periode Rencana tidak ditulis karena tidak ada sumbernya (U4).
2. Semua sel faktual kosong. Terisi hanya judul kolom, kode baris (OBJ-1 sampai OBJ-3, TA-1 sampai TA-3, KPI-1 sampai KPI-5, AKT-1 sampai AKT-5), nomor urut C1 dan C2, dan peran di tabel pengesahan. Tanpa baris contoh. Jumlah baris kosong adalah kapasitas tata letak, bukan klaim jumlah KPI atau Aktivitas; butir 7 memberi izin menambah baris.
3. Tidak ada angka Target, Budget, tenggat hari, atau jangka retensi di dokumen. Target KPI diisi per periode dari lembar KPI Brand & Marketing atau ditetapkan VP Commercial (butir 4.7, U8). Arti Efektif dan Belum Efektif ditulis terhadap Status Capaian KPI yang sama, bukan terhadap persentase.
4. Penerima lead: JA-06 menulis "Commercial"; SNX-COM-SOP-01 menulis Business Development sebagai penerima inbound lead dan pengelola CRM. Peran Business Development ditulis mengikuti SNX-COM-SOP-01 dan hanya menyediakan status lead sebagai Sumber Data (USULAN).
5. Kolom "Rumusan dan Satuan" ada di tabel KPI karena lembar KPI Brand & Marketing tidak memuat definisi operasional KPI (lihat penanganan cacat). Tanpa kolom itu, Status Capaian bisa dihitung berbeda tiap bulan.
6. Nilai "Tidak Dinilai" ada karena lembar KPI mengukur per kuartal sedangkan kriteria meminta review bulanan. KPI per kuartal dicatat Realisasinya tiap bulan, tetapi dinilai pada akhir rentang Target (butir 4.10, U9).
7. Pembagian peran: Brand & Marketing mencatat dan mengusulkan; VP Commercial menetapkan, memeriksa, dan memiliki laporan. Penetapan dan pencatatan dibedakan konsisten di butir 4.5 sampai 4.16, bagian 5, dan langkah 6.1 sampai 6.21. Label baris pengesahan memakai "Pencatat" dan "Pemeriksa", bukan kata yang memuat "penyusun".
8. Bagian 3 hanya arti istilah dan arti nilai kolom; aturan di bagian 4. Definisi dicek tidak melingkar: draf pertama menulis KPI memakai Target dan Target memakai KPI, dan Tindakan Perbaikan didefinisikan dengan "tindakan"; keduanya sudah dibenahi (KPI dihitung dengan rumusan dan satuan; Tindakan Perbaikan = langkah).
9. Satu istilah untuk satu hal: Marketing Plan, Monthly Performance Review, Catatan Tindak Lanjut, Tindakan Perbaikan (corrective action disebut sekali di definisi), Realisasi, Target, Budget, Channel, Aktivitas, PIC. Tidak ada "rencana pemasaran", "anggaran", "kegiatan", atau "corrective action" di badan selain definisi.
10. Sebutan COO tidak muncul di badan, jadi aturan "Direktur (COO)" tidak terpakai. Samuel ditulis "Direktur Utama" di badan dan "President Director" hanya di blok Approved By. Tidak ada nama orang di badan dokumen. Zammad, GLPI, vault, dan PPN tidak relevan dan tidak disebut. Satu-satunya sistem yang disebut: CRM, Google Drive, dan laporan analitik website.
11. Setiap kode dokumen di badan ada di tabel Dokumen Terkait: SNX-HR-ORG-01, SNX-HR-JA-01, SNX-COM-SOP-01, SNX-MKT-REG-01, SNX-MKT-REG-02, SNX-MKT-REG-03, SNX-ISMS-PRO-01, dan KPI COMMERCIAL & MARKETING.xlsx (belum bernomor, dirujuk dengan nama berkas).
12. Frasa "belum ada" tidak dipakai. Baris checklist 56 sampai 59 semuanya `checked: false`; SNX-MKT-REG-01 sampai 03 ditulis dengan judul dan fungsinya saja, menurut keputusan cakupan putaran perbaikan 1.
13. Diagram: tidak ada. Dokumen berupa laporan isian, dan kriteria baris 56 tidak memintanya.

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Pembukuan biaya pemasaran dikecualikan; laporan hanya memuat Budget dan Realisasi Biaya | Ruang Lingkup | FAT |
| U2 | Prioritas Penjualan = sales plan VP Commercial | Definisi | Owner |
| U3 | Daftar nilai Status Pelaksanaan (sama dengan kolom Status di SNX-MKT-REG-02), Status Capaian, Status pada Catatan Tindak Lanjut, dan Hasil Pemeriksaan beserta artinya | Bagian 3, Nilai pada Kolom Status dan Hasil | Owner |
| U4 | Panjang Periode Rencana belum ditetapkan; Brand & Marketing memilihnya per rencana | Butir 4.1 | Owner |
| U5 | Marketing Plan diisi sebelum Aktivitas pertama dijalankan | Butir 4.2 | Owner |
| U6 | Rujukan Prioritas Penjualan ditulis di tiap Marketing Objective | Butir 4.3, tabel A2 | Owner |
| U7 | Tiap Marketing Objective punya KPI; tiap Aktivitas merujuk satu Marketing Objective dan punya Channel, jadwal, PIC | Butir 4.4 | Owner |
| U8 | Target KPI disalin dari lembar KPI Brand & Marketing; VP Commercial menetapkan Target di luar lembar itu | Butir 4.7, Dokumen Terkait | Owner |
| U9 | KPI dengan Target per kuartal dinilai pada akhir rentang Target dan ditulis Tidak Dinilai pada bulan lain | Butir 4.10 | Owner |
| U10 | VP Commercial menetapkan Tindakan Perbaikan, PIC, dan Target Selesai | Butir 4.13, bagian 5 | Owner |
| U11 | VP Commercial meninjau Tindakan Perbaikan berstatus Terbuka tiap Monthly Performance Review | Butir 4.14 | Owner |
| U12 | Hasil Pemeriksaan ditulis pada Monthly Performance Review pertama yang menilai KPI itu; hasil Belum Efektif memicu Tindakan Perbaikan baru | Butir 4.15 | Owner |
| U13 | Perubahan Marketing Plan ditulis sebagai versi baru dan diperiksa lagi oleh VP Commercial | Butir 4.16 | Owner |
| U14 | Data lead tetap di CRM dan SNX-MKT-REG-03; laporan terisi tidak memuat data pelanggan | Butir 4.17 | Fani (reviewer SNX-ISMS-PRO-01) |
| U15 | Pembagian tugas Brand & Marketing, VP Commercial, Business Development, dan Direktur Utama | Bagian 5 | Owner; Samuel untuk peran penyetuju |
| U16 | Lokasi rekaman (folder Google Drive departemen Marketing), pencatat Brand & Marketing, pemilik VP Commercial, bukti disimpan bersama | Rekaman | Owner |
| U17 | Jangka retensi laporan terisi dan bukti | Rekaman | Legal |
| U18 | Enam klausul ISO 9001:2015 dan ISO/IEC 27001:2022 | Acuan Klausul ISO | Owner; konsultan menilai |
| U19 | SNX-MKT-REG-03 sebagai tempat Realisasi KPI lead dibaca | Dokumen Terkait | Owner |
| U21 | Batas dengan SNX-MKT-REG-02: laporan ini memuat rencana Aktivitas dan jadwal; REG-02 mencatat pelaksanaan nyata tiap campaign dan Aktivitas; tabel B2 merujuk catatan REG-02 lewat kolom Rujukan Catatan (nomor baris Tabel 1) dan Status Pelaksanaan sama dengan kolom Status Tabel 2 | Ruang Lingkup, butir 4.8, tabel B2, Dokumen Terkait | Owner |
| U22 | Validasi klaim produk dan layanan berada di SNX-MKT-REG-01 (Description baris 58 memuat validasi klaim, sedangkan judul baris 58 adalah Campaign & Activity Register) | Ruang Lingkup, Dokumen Terkait | Owner |
| U23 | Satu Aktivitas sama dengan satu baris Tabel 1 SNX-MKT-REG-02 (campaign, atau kegiatan di luar campaign seperti event atau webinar) | Definisi | Owner |
| U20 | Nama penanda tangan Prepared By dan Reviewed By, dan process_owner "VP Commercial" (status USULAN di config/defaults.json) | Blok Identity dan Approval | Owner; Samuel untuk Approved By |

Jumlah USULAN: 23 butir. Teks dokumen memuat 32 label "(USULAN)" karena beberapa butir diberi label di lebih dari satu kalimat, ditambah satu label "(USULAN, perlu konfirmasi konsultan)" di bagian Acuan Klausul ISO; lint menghitung 32. Tidak ada angka bisnis tanpa sumber di dokumen.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Selisih Description checklist: baris 58 (Marketing Campaign & Activity Register) tidak identik dengan baris 57. Baris 58 memuat isi baris 57 (materi dan konten eksternal) ditambah validasi klaim dan field klaim yang perlu diverifikasi serta sumber atau bukti pendukung; tidak ada kalimat di baris 58 tentang pelaksanaan campaign atau aktivitas, padahal judulnya campaign dan aktivitas. Keputusan cakupan orkestrator (USULAN, pemutus owner): SNX-MKT-REG-01 = persetujuan materi eksternal dan validasi klaim (field baris 57 dan 58); SNX-MKT-REG-02 = pencatatan pelaksanaan nyata tiap campaign dan aktivitas, dengan materi ditautkan ke ID persetujuan di REG-01; SNX-MKT-REG-03 = hasil lead dan serah terima ke Sales; dokumen ini = rencana dan tinjauan kinerja. Dokumen ini mengikuti keputusan itu (Ruang Lingkup, butir 4.8, tabel B2, Dokumen Terkait; U21). Spec SNX-MKT-REG-02 di repo saya baca ulang sesudah keputusan: Tujuan dan Ruang Lingkupnya sudah mencatat pelaksanaan campaign dan aktivitas dan menautkan materi ke ID Persetujuan Materi di REG-01, jadi cocok dengan kalimat di dokumen ini. Periksa ulang bila REG-02 berubah lagi | Owner ; diubah W9: owner memutus A8; batas empat dokumen sudah diputus (label USULAN pada batas dihapus). Temuan baris 58 pindah ke open item 14 |
| 2 | Panjang Periode Rencana dan tenggat pengisian Monthly Performance Review (tanggal berapa tiap bulan) tidak ada di sumber. Dokumen tidak menulis angka | Owner |
| 3 | Lembar KPI Brand & Marketing mengukur per kuartal (kolom Q1 sampai Q4), semua kolom Actual, Realisasi, Balancing, dan Score kosong, dan tidak memuat rumusan KPI. Hubungan KPI di laporan ini dengan lembar KPI dan dengan KPI Matrix terpisah (Job Analysis bagian 2) belum diputus: satu daftar KPI atau dua | Owner |
| 4 | Lembar KPI memuat keterangan "No. 1 & 2 = KPI Perusahaan & departement yang di tetapkan Direktur". Siapa menetapkan Target KPI pemasaran untuk laporan ini (VP Commercial menurut butir 4.7, atau Direktur untuk KPI no. 1 dan 2) belum jelas | Owner |
| 5 | Siapa menyetujui Budget pemasaran dan siapa memverifikasi Realisasi Biaya terhadap bukti pengeluaran. Dokumen hanya menulis "mengikuti delegasi dan persetujuan tertulis yang berlaku" (butir 4.6) | FAT; owner |
| 6 | Apakah Marketing Plan terisi perlu persetujuan Direktur Utama (misalnya bila memuat Budget), atau cukup diperiksa VP Commercial. Dokumen memberi Direktur Utama hanya peran penyetuju laporan ini lewat blok Approved By | Samuel |
| 7 | Lokasi folder, hak akses, dan jangka retensi laporan terisi belum ditetapkan. SNX-ISMS-PRO-01 butir 4.15 hanya menulis "sesuai master list"; master list yang disebut SNX-ISMS-PRO-01 adalah milik Divisi Operation | Owner untuk lokasi; Legal untuk retensi |
| 8 | Nama di lembar KPI ditulis "Zilly" (sel B15) dan "Zily" (nama lembar dan blok OLD). Tidak ada nama orang di badan dokumen ini, jadi tidak berdampak; dicatat untuk pemilik lembar | Aziz |
| 9 | Sistem tempat Realisasi tiap KPI dibaca (CRM, laporan analitik website) disebut sebagai contoh. Daftar Sumber Data resmi per KPI belum ada dan diisi per Periode Rencana di tabel A4 | Owner |
| 10 | SNX-MKT-REG-01, REG-02, dan REG-03 ditulis paralel. REG-03 baru muncul di repo sesudah dokumen ini pertama ditulis; Tujuan dan Ruang Lingkupnya saya baca ulang pada putaran perbaikan 1 dan cocok (REG-03 menyebut tabel datanya dapat menjadi masukan review di dokumen ini). Periksa ulang butir yang menyebut REG-03 (Ruang Lingkup, butir 4.17, Dokumen Terkait, U14, U19) bila REG-03 berubah | LEAD ; ditutup W9: REG-02 diubah lewat A8 (Aktivitas satu arti, Dibatalkan terpisah, kolom Kode Aktivitas dihapus), rujukan di dokumen ini dicocokkan ulang |
| 11 | Tabel A6, B4, dan Rekaman terbelah antar halaman di render LibreOffice. Perlu dilihat di Word oleh orang; bukan hasil yang bisa dipastikan mesin | HUMAN-VERDICT, owner atau LEAD ; ditutup W9: tiap tabel diberi repeat_header dan cant_split (B4); tampilan di Word tetap bisa dilihat manusia |
| 12 | data_conflicts yang konfirmasinya belum selesai dan relevan: ejaan "Samuel Kristanto Utomo" (konfirmasi: owner atau Samuel) dan sebutan "Direktur Utama" di badan. Dipakai sesuai kolom "pakai" | Owner |
| 13 | Kalimat perintah di DATA yang saya baca (checklist, Job Analysis, lembar KPI, spec lane lain): nihil | - |

## Sweep

Putaran sweep atas butir 1 dan 2 dari orkestrator. Yang diubah hanya teks di bawah; fakta, angka, nama, dan struktur lain tetap. Temuan pemeriksa di qa/MKT-RPT-01.verify.json dibaca sebagai data; yang di luar butir 1 dan 2 tidak diubah (nonblocking lain: pasif tanpa pelaku di butir 4.3, 4.10, 4.16, pengantar bagian 7; "Target Selesai" dan kata "rencana" huruf kecil; "Legal" dan "PIC" di tabel Peran; judul SNX-ISMS-PRO-01; hubungan ISO/IEC 27001:2022 7.5.3).

| Butir | Letak | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Definisi, Aktivitas | "Satu pekerjaan pemasaran yang punya Channel, jadwal mulai, jadwal selesai, dan PIC sendiri, misalnya campaign, konten, event, atau webinar." | "Satu campaign, atau satu kegiatan pemasaran di luar campaign seperti event atau webinar, yang punya Channel, jadwal mulai, jadwal selesai, dan PIC sendiri. Satu Aktivitas sama dengan satu baris Tabel 1 SNX-MKT-REG-02 (USULAN)." |
| 1 | Definisi, Channel | "Saluran yang dipakai sebuah Aktivitas untuk menjangkau Target Audience, misalnya website, media sosial, event, atau webinar." | "Tempat sebuah Aktivitas menampilkan atau membagikan materi kepada pihak di luar SINUX, misalnya website, akun social media, atau acara." (disamakan dengan arti Channel di SNX-MKT-REG-02) |
| 1 | Nilai Status Pelaksanaan | Tiga nilai: Terlaksana, Tertunda, Dibatalkan | Empat nilai sama dengan SNX-MKT-REG-02: Direncanakan, Berjalan, Selesai, Dibatalkan, dengan arti yang sejalan. Pengantar tabel menambah kalimat "Nilai Status Pelaksanaan sama dengan nilai kolom Status di SNX-MKT-REG-02." Aktivitas lintas bulan kini punya padanan (Berjalan) |
| 1 | Butir 4.8 | "... dan Aktivitas yang tertunda dari bulan sebelumnya, dan Brand & Marketing mengisinya dengan merujuk pencatatan pelaksanaan tiap campaign di SNX-MKT-REG-02 (USULAN)." | "... dan Aktivitas yang belum Selesai dari bulan sebelumnya. Brand & Marketing mengisinya dari pencatatan pelaksanaan di SNX-MKT-REG-02: kolom Rujukan Catatan memuat nomor baris Tabel 1 untuk Aktivitas itu, dan Status Pelaksanaan sama dengan kolom Status di Tabel 2 di sana (USULAN)." (sekaligus menjawab temuan pemeriksa tentang isi kolom Rujukan Catatan) |
| 1 | Ruang Lingkup, kalimat pertama | "... untuk Aktivitas pemasaran SINUX berupa campaign, konten, event, dan webinar." | "... berupa campaign, event, dan webinar." (konten adalah materi yang dikendalikan di SNX-MKT-REG-01; JA-06 butir 4 menyebut event, webinar, dan campaign) |
| 1 | Ruang Lingkup, pengecualian REG-01 | "Ada di SNX-MKT-REG-01: persetujuan materi eksternal seperti company profile, website, dan media sosial, serta validasi klaim produk dan layanan." | Kalimat sama dengan tambahan "(USULAN)" di akhir |
| 1 | Dokumen Terkait, SNX-MKT-REG-01 | "... persetujuan materi eksternal dan validasi klaim produk dan layanan sebelum publikasi. Dikecualikan dari laporan ini." | "... sebelum publikasi (USULAN). Dikecualikan dari laporan ini." |
| 2 | Ruang Lingkup, pengecualian REG-02 | "Ada di SNX-MKT-REG-02. Laporan ini memuat rencana Aktivitas dan jadwalnya, dan Realisasi di tabel B2 merujuk catatan di SNX-MKT-REG-02 (USULAN)." | "Ada di SNX-MKT-REG-02, yang juga menautkan materi yang dipakai ke ID persetujuan di SNX-MKT-REG-01. Laporan ini memuat rencana Aktivitas dan jadwalnya, dan tabel B2 merujuk catatan di SNX-MKT-REG-02 (USULAN)." |
| 2 | Dokumen Terkait, SNX-MKT-REG-02 | "... mencatat pelaksanaan nyata tiap campaign dan Aktivitas, dan menautkan materi ke ID persetujuan di SNX-MKT-REG-01. Laporan ini memuat rencana Aktivitas dan jadwalnya, dan kolom Rujukan Catatan di tabel B2 menunjuk catatan itu (USULAN)." | "... menautkan materi yang dipakai ke ID persetujuan di SNX-MKT-REG-01. Laporan ini memuat rencana Aktivitas dan jadwalnya. Kolom Rujukan Catatan di tabel B2 menunjuk nomor baris catatan itu, dan kolom Kode Aktivitas di sana menunjuk kode Aktivitas di laporan ini (USULAN)." (kolom Kode Aktivitas (SNX-MKT-RPT-01) memang ada di Tabel 2 SNX-MKT-REG-02) |
| 2 | Dokumen Terkait, SNX-MKT-REG-03 | "... hasil marketing yang diteruskan ke Sales. Tempat Realisasi KPI lead dapat dibaca (USULAN)." | "... hasil lead dan serah terimanya ke Sales, dengan campaign asal yang merujuk nama campaign di SNX-MKT-REG-02. Tempat Realisasi KPI lead dapat dibaca (USULAN)." |

Batas empat dokumen sesudah sweep (USULAN, pemutus owner): SNX-MKT-RPT-01 = rencana pemasaran dan tinjauan kinerja; SNX-MKT-REG-01 = persetujuan materi eksternal dan validasi klaim; SNX-MKT-REG-02 = pencatatan pelaksanaan campaign dan aktivitas yang menautkan materi ke ID persetujuan REG-01; SNX-MKT-REG-03 = hasil lead dan serah terima ke Sales yang merujuk nama campaign di REG-02. Tidak ada isi yang ditaruh di dua register di dokumen ini: dokumen ini tidak memuat persetujuan materi, klaim, maupun data lead per lead. Yang tetap muncul di dua tempat adalah status dan nomor baris pelaksanaan di tabel B2; keduanya salinan rujukan bulanan dari Tabel 1 dan Tabel 2 SNX-MKT-REG-02 dan ditandai USULAN di butir 4.8 (U21).

Uji sesudah sweep: `python3 -I tools/render_sop.py ...` sukses; `python3 -I tools/lint_doc.py /tmp/pen-MKT-RPT-01/MKT-RPT-01.docx generic` = "pass": true, fails kosong, warn "32 butir (USULAN) menunggu ACC"; `python3 /mnt/skills/public/docx/scripts/office/validate.py` = "All validations PASSED!"; `python3 -I reports/orch/blankscan.py` = `ok 15 MKT-RPT-01.docx []`. Tiap kode SNX di badan ada di Dokumen Terkait (nol kurang). Nol em-dash, nol en-dash, nol frasa meta.

## Penanganan cacat context/audit

Perintah: `grep -n "Marketing Planning & Performan" context/audit/*.md`. Hasil: nol baris (exit code 1). Baris ini T2 tanpa sumber dan tidak punya fileId, jadi tidak ada bagian dokumen sendiri dan tidak ada "Catatan kualitas dan celah" untuk baris ini. Saya membaca bagian lembar KPI di context/audit/iso-sinux-supdocs-commercial-2026-10-14.md (baris 353 sampai 547, termasuk bagian 5 Catatan kualitas dan celah), karena lembar itu dirujuk sebagai sumber Target KPI, dan membandingkannya dengan lembar asli hari ini (download_file_content, openpyxl).

| Cacat atau catatan | Relevansi | Penanganan |
|---|---|---|
| Kolom Q1 sampai Q4 (Actual, Realisasi, Balancing, Score) kosong pada semua baris KPI; realisasi UNMEASURED | Langsung | Dokumen tidak menyalin Target maupun realisasi dari lembar itu dan tidak mengklaim ada realisasi. Tabel B3 kosong sampai Brand & Marketing mengisinya dari Sumber Data. Open item 3 |
| Sheet Zily tidak memuat definisi formula KPI; definisi hanya ada di kolom X sheet lain | Langsung | Tabel A4 punya kolom "Rumusan dan Satuan" dan butir 4.11 memakai rumusan itu untuk Status Capaian (asumsi 5) |
| Rumus Score Rata-Rata berupa ArrayFormula yang tidak terbaca | Langsung | Bobot, Balancing, dan Score dikecualikan dari laporan ini (Ruang Lingkup); laporan hanya memuat Target dan Realisasi |
| Target per kuartal bercampur dengan target bulanan di lembar yang sama ("setiap quarter", "QoQ", "/bulan") | Langsung | Nilai Tidak Dinilai dan butir 4.10 (asumsi 6, U9). Open item 3 |
| Penulisan nama "Zilly" vs "Zily" | Tidak langsung | Tidak ada nama orang di badan dokumen. Open item 8 |
| Sel C30 Zily memuat sisa penanda markup ("**" dan "<br><br>") | Tidak relevan | Tidak disalin; dokumen tidak menyalin isi sel itu |
| Satuan "M" pada target revenue tidak didefinisikan; kolom No berformat campuran; rumus W55 blok OLD Laras | Tidak relevan | Tidak dipakai. Dokumen tidak memuat target revenue |
| KPI individu tidak sama dengan daftar KPI di Sales SOP dan deck onboarding | Tidak langsung | Dokumen tidak memuat daftar KPI; KPI diisi per Periode Rencana. Open item 3 |
| Paket konsultan dan Eranyacloud | Tidak relevan | Tidak ada isi yang disalin; tidak ada nama perusahaan lain |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Benda memakai kata kerja manusia atau jadi pelaku. Draf pertama menulis "Panjang periode tidak dibatasi dokumen ini" (butir 4.1) dan "Monthly Performance Review dibuat sekali tiap bulan" tanpa pelaku (butir 4.8). Keduanya saya tulis ulang dengan pelaku Brand & Marketing. Kalimat dengan subjek "Marketing Plan", "Catatan Tindak Lanjut", "Tabel", dan "Laporan" yang tersisa memuat sesuatu, atau berstatus ("Laporan ini berstatus Draft"). Tidak ada kalimat "laporan menetapkan", "tabel menentukan", atau "dokumen memastikan".
- Definisi melingkar: KPI memakai Target dan Target memakai KPI, dan Tindakan Perbaikan didefinisikan dengan kata "tindakan". Sudah diganti (lihat asumsi 8).
- Kata "Positioning-nya" di langkah 6.3 terbaca seperti salinan terjemahan; saya ganti "menulis Positioning untuk tiap Target Audience". Langkah yang memuat dua tindakan (menyalin lalu mengisi tabel; menyerahkan bukti lalu mengisi status) saya pecah supaya satu langkah satu tindakan.
- Kata meta penyusunan: draf pertama memakai kolom "Tanggal Penyusunan" dan baris pengesahan "Penyusun". Diganti "Tanggal Rencana Dibuat" dan "Pencatat". Pemindai atas teks spec menemukan nol kata "penyusun" (satu kecocokan "menyusun" adalah kata kerja dari uraian jabatan JA-06 butir 1, bukan frasa meta).
- Ekor penegas dan pengisi: tidak ada "tanpa terkecuali", "perlu dicatat bahwa", "dalam rangka", "adapun", "pada intinya", "secara fundamental". Kesimpulan dua kalimat tanpa pujian. Tidak ada em-dash, en-dash, tebal, atau tanda kutip penekanan.
- Langkah 6.1 sampai 6.21 hampir semuanya diawali "Brand & Marketing" atau "VP Commercial". Terbaca seragam, tetapi tiap langkah satu tindakan dan satu pelaku (RUNBOOK §6a.2). Saya biarkan.
- Huruf kapital pada istilah terdefinisi (Marketing Plan, Target, Realisasi, Aktivitas) bisa terbaca sebagai kapital penekanan. Saya pertahankan karena auditor perlu mencocokkan istilah dengan tabel Definisi, sama dengan SNX-HR-RPT-01; kata umum seperti "rencana", "jadwal", dan "bulan" tetap huruf kecil. Verifikator perlu menilai.
- Pembuka Tujuan "Hasil yang dijaga:" sama dengan dokumen W7 lain. Saya biarkan karena RUNBOOK §6a.4 meminta "hasil yang dijaga" dan frasa itu bukan ekor penegas.
- Kelompok tiga yang tersisa: "campaign, event, dan webinar" (tiga jenis Aktivitas dari JA-06 butir 4), "Realisasi, Status Capaian, dan Evaluasi" (nama tiga kolom nyata di tabel B2 dan B3). Keduanya isi nyata, bukan tiga yang dipaksakan.
- Banyak butir bertanda (USULAN) berurutan di bagian 4. Terbaca penuh label, tetapi tiap butir memang belum diputus pimpinan; menghapus label akan menyembunyikan status. Saya biarkan dan daftarkan di bagian USULAN.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Nama orang: nol di badan dokumen. Nama di blok Approval berasal dari prompt dan config/defaults.json.
- Angka: nol angka bisnis (Target, Budget, tenggat, retensi, jumlah KPI). Yang ada: nomor butir (4.1 sampai 4.17, 6.1 sampai 6.21), kode tabel (A1 sampai C2), kode baris (OBJ, TA, KPI, AKT), dan jumlah baris kosong (3 atau 5) sebagai kapasitas tata letak. "JA-06 butir 1 dan 5", "JA-03 butir 1 dan 7" sudah dicocokkan dengan teks Job Analysis yang dibaca hari ini. Nomor butir 4.3, 4.8, dan 4.15 SNX-ISMS-PRO-01 dicocokkan dengan specs/ISMS-PRO-01.json.
- Tanggal: satu rentang, "2026 sampai 2027", dari sel B7 lembar KPI. Tidak ada tanggal rekaman.
- Sistem: CRM (SNX-COM-SOP-01), Google Drive (SNX-ISMS-PRO-01 butir 4.8), laporan analitik website (lembar KPI sel E25). Ketiganya disebut sebagai contoh atau lokasi dengan sumber, atau berlabel USULAN (folder departemen Marketing).
- Pembagian peran, alur pemeriksaan, arti Efektif dan Belum Efektif, versi Marketing Plan, dan nilai status adalah rancangan penyusun dan berlabel USULAN (U3 sampai U13, U15). Kalimat di bagian 5 dan butir 4.3, 4.13 menunjuk uraian jabatan JA-06 dan JA-03 sebagai dasar, tetapi uraian itu tidak menyebut Marketing Plan atau Monthly Performance Review.
- Judul klausul ISO bukan dari sumber tim; berlabel USULAN dan perlu konfirmasi konsultan (U18).
- Satu hal yang saya tandai karena dekat dengan fakta: batas dengan SNX-MKT-REG-01, REG-02, dan REG-03 mengikuti keputusan cakupan orkestrator (USULAN, U21) dan deskripsi checklist baris 57 sampai 59, bukan isi final ketiga register (open item 1 dan 10). Kalimat "REG-02 mencatat pelaksanaan nyata tiap campaign" cocok dengan spec REG-02 yang saya baca ulang pada putaran perbaikan 1.

## ISO-W9

Putaran ISO-W9 (LEAD G-3 A8, B2, B4; owner GO). Batas tulis: specs/MKT-RPT-01.json dan notes/MKT-RPT-01.md. Meta dan blok approval tidak berubah (sama dengan defaults v22 MKT). Rujukan silang yang diubah ada di baris tabel; tujuan rujukan (REG-02 Tabel 1, kolom Status, kolom Rujukan Catatan; REG-03) ada dan cocok isinya.

| Butir | Sebelum | Sesudah |
|---|---|---|
| Ruang Lingkup paragraf 1 | tidak menyebut sumber isian | tambah: Brand & Marketing mengisi laporan dari REG-02 (pelaksanaan Aktivitas) dan REG-03 (hasil lead) |
| Pengecualian baris REG-01 | "Ada di SNX-MKT-REG-01: ... (USULAN)" | "satu-satunya register materi, konten, dan persetujuan klaim"; label dihapus |
| Pengecualian baris REG-02 | "pelaksanaan nyata tiap campaign dan Aktivitas ... menautkan materi ... (USULAN)" | "pelaksanaan tiap Aktivitas": nama, tujuan, Channel, jadwal, PIC, Budget, status, ID Persetujuan Materi, hasil singkat; label dihapus |
| Definisi Aktivitas | "... sama dengan satu baris Tabel 1 SNX-MKT-REG-02 (USULAN)" | label dihapus; arti sama dengan Definisi Aktivitas di REG-02 |
| 3.1 intro | nilai Status Pelaksanaan sama dengan REG-02 | tambah: Direncanakan atau Berjalan = belum Selesai; Dibatalkan dihitung terpisah |
| 4.8 | "Aktivitas yang belum Selesai dari bulan sebelumnya" (mencakup Dibatalkan) | "Aktivitas berstatus Direncanakan atau Berjalan dari bulan sebelumnya"; Dibatalkan dihitung terpisah, dicatat sekali pada Bulan Review pembatalan, tidak dibawa ke bulan berikutnya (USULAN) |
| Dokumen Terkait REG-01 | persetujuan materi dan validasi klaim (USULAN) | satu-satunya register materi, konten, dan persetujuan klaim, termasuk validasi klaim; label dihapus |
| Dokumen Terkait REG-02 | menautkan materi; kolom Kode Aktivitas menunjuk kode laporan ini (USULAN) | kolom yang dicatat REG-02; kolom Rujukan Catatan di B2 menunjuk nomor baris Tabel 1; rujukan Kode Aktivitas dihapus |
| Dokumen Terkait REG-03 | "Tempat Realisasi KPI lead dapat dibaca (USULAN)"; nama campaign | Brand & Marketing mengisi laporan dari register itu untuk hasil lead; nama Aktivitas; label dihapus |
| Semua 20 blok table | tanpa flag | "repeat_header": true dan "cant_split": true (B4) |

Open item yang ditutup atau diubah W9: lihat kolom Pemutus pada tabel Open items. Open item baru:

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 14 | Description checklist baris 58 berisi pengendalian materi baris 57 yang diperluas dengan validasi klaim, bukan pelaksanaan campaign sesuai judulnya (Marketing Campaign & Activity Register); perlu dibetulkan Brand & Marketing. Pengukuran: teks baris 58 tidak identik dengan baris 57. | Brand & Marketing |
| 15 | Kode AKT di tabel A5 tidak lagi dirujuk dari REG-02 (kolom Kode Aktivitas dihapus). Hubungan hanya lewat kolom Rujukan Catatan di tabel B2 | owner |
| 16 | A3: dokumen ini menyebut JA-03 dan JA-04 hanya sebagai rujukan uraian jabatan (VP Commercial JA-03), tanpa atasan atau garis lapor; tidak ada yang diselaraskan dan tidak ada label menunggu konfirmasi pada garis itu | - |

Uji (spec W9): render, `lint_doc.py ... generic`: pass true, fails kosong, 27 butir USULAN; `validate.py`: All validations PASSED; `blankscan.py`: ok 16 halaman []; `w9diff.py MKT-RPT-01`: diff teks hanya baris di tabel di atas (flag tabel tidak tampak di teks).
