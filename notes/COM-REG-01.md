# Catatan penyusun COM-REG-01: Customer Feedback & Complaint Register

Status: DRAFTED (spec + notes ada). Spec: specs/COM-REG-01.json. Mode generic (doc_type_cover REGISTER), aksi T2, wave W7, nomor SNX-COM-REG-01 (nomor SNX lama dipertahankan), department Commercial, classification INTERNAL (worklist), audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Laras Rasmawati / VP Commercial", reviewed "Amirull Yusuf Zulkarnain / Direktur", approved "Samuel Kristanto Utomo / President Director". process_owner "Direktur": dokumen T2 tanpa sumber, jadi jabatan reviewer departemen tanpa nama (config/defaults.json process_owner, status USULAN). Catatan worklist: kosong.

## 1. Sumber

Sumber dokumen: tidak ada (T2 tanpa sumber). Struktur kolom dan petunjuk pengisian disusun dari kriteria baris; sel data faktual dikosongkan; tanpa baris contoh. Alat Drive hanya dipakai untuk satu panggilan baca, `get_file_metadata`, guna mengukur modifiedTime dokumen yang menjadi dasar eskalasi. Tidak ada tulis ke Drive.

| Bahan | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Kriteria: config/checklist.json baris 54 (checked: false, link kosong) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist tim) | 2026-10-14T17:47:13.611Z (tertulis di config/checklist.json, tidak diukur ulang) | `sed`/`python3` pada berkas repo |
| SALES STANDARD OPERATING PROCEDURE.pdf (dasar eskalasi keluhan kritis dan tanggung jawab customer satisfaction) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 | 2026-10-05T07:08:41.814Z (`get_file_metadata` hari ini; sama dengan notes/COM-SOP-02.md) | Teks dibaca dari salinan context/audit/iso-sinux-supdocs-commercial-2026-10-14.md (baris 826 dan 882). PDF aslinya tidak dibuka di sesi ini (UNMEASURED terhadap lapisan teks PDF) |
| SINUX_Job_Analysis_2026.docx (JA-07) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (dikutip dari notes/COM-SOP-02.md, tidak diukur ulang) | Salinan context/audit/iso-sinux-supdocs-hr-2026-10-14.md. Sejak sweep tidak lagi menjadi dasar kalimat di dokumen; dibaca hanya sebagai konteks |
| Pendukung repo (bukan Drive) | tidak berlaku | tidak berlaku | config/defaults.json v21 (ticketing, data_conflicts, process_owner), specs/HR-ORG-01.json (jabatan dan matriks peran), specs/COM-SOP-01.json (butir 4.10, 4.17, bagian 8 dan 9), specs/ISMS-PRO-01.json (butir 4.3), specs/OPS-SOP-04.json, specs/OPS-FRM-10.json, context/audit sintesis. Spec lane lain berstatus Draft, kutipan darinya bisa basi |

Kalimat perintah kepada AI di bahan mana pun: nihil. Kalimat kewajiban untuk karyawan ("Segera eskalasikan ...") adalah isi SOP, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria register: enam unsur yang harus tercatat (feedback/keluhan, PIC, tindakan, status penyelesaian, konfirmasi kepada customer, eskalasi bila diperlukan). Dasar Tabel 1 sampai 4 | "Mencatat feedback/keluhan, PIC, tindakan, status penyelesaian, konfirmasi kepada customer, dan eskalasi bila diperlukan." (config/checklist.json baris 54, kolom Description) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Komplain kritis wajib segera dieskalasi ke VP Commercial. Dasar butir 4.9 dan kolom Dieskalasi ke | "Segera eskalasikan kepada VP Commercial apabila terjadi: opportunity bernilai strategis; permintaan diskon di luar kewenangan; risiko kehilangan customer; konflik kontrak; isu legal; komplain kritis; kompetitor melakukan displacement; potensi churn." (Sales SOP 14 Escalation Matrix, hal. 17; teks dari salinan context/audit baris 882) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Customer satisfaction sesudah implementasi menjadi tanggung jawab sales (di SINUX dipetakan ke Business Development oleh SNX-COM-SOP-01 butir 4.17). Dasar penunjukan Business Development sebagai pencatat | "Setelah implementasi, sales tetap bertanggung jawab untuk:" lalu "Relationship Management; Upselling; Cross-selling; Renewal; Customer Satisfaction." (Sales SOP Stage 10 Account Management, hal. 12; baris 826 salinan context/audit) | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Posisi |
|---|---|---|---|
| 1 | Konteks, bukan dasar kalimat di dokumen: JA-07 Business Development memuat tugas dalam konteks negosiasi. Sejak sweep tidak dikutip di Peran maupun Dokumen Terkait | "Menjaga dokumentasi komunikasi, keberatan pelanggan dan status negosiasi." | JA-07 Business Development, Uraian Jabatan nomor 6; fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Informasi customer minimal RESTRICTED, sehingga register terisi berklasifikasi RESTRICTED (Internal) (butir 4.12) | "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan tingkat yang lebih tinggi." | specs/ISMS-PRO-01.json butir 4.3 (repo, Draft); fileId sumber 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| 3 | Tiket Zammad untuk Ops, GLPI untuk generalist; batas generalist belum dirinci (butir 4.8) | "Kata owner 14 Okt: \"sistem tiket zammad untuk ops, glpi untuk generalist\". GLPI = SINUX Service Hub. Batas lingkup 'generalist' belum dirinci owner" | config/defaults.json, medan ticketing |
| 4 | Batas respons ke customer yang dirujuk butir 4.6 (angkanya tidak disalin ke dokumen) | "Balasan email customer", "Business Development", "Maksimal 1 hari kerja"; "Balasan WhatsApp customer", "Business Development", "Maksimal 2 jam kerja" | specs/COM-SOP-01.json bagian 8 (SLA); asal Sales SOP 07 Customer Communication Standard, hal. 14 (salinan context/audit baris 831 sampai 836) |
| 5 | Eskalasi keluhan kritis dari Business Development ke VP Commercial | "Terjadi opportunity bernilai strategis, risiko kehilangan customer, konflik kontrak, isu legal, komplain kritis, kompetitor melakukan displacement, atau potensi churn" / "Business Development segera mengeskalasi kepada VP Commercial." | specs/COM-SOP-01.json bagian 9 |
| 6 | Komunikasi insiden P1 dan P2 ke customer ada di Operation, bukan di register (Ruang Lingkup) | "Komunikasi formal ke pelanggan untuk P1 dan P2; memastikan RCA terkirim." | specs/OPS-SOP-04.json, peran Service Delivery Manager |
| 7 | Keluhan pelanggan adalah salah satu pilihan sumber di form RCA, tanpa kewajiban RCA | "Pilihan Keluhan pelanggan dan Lainnya di bagian Identitas juga tidak mewajibkan RCA (USULAN)." | specs/OPS-FRM-10.json, Tujuan dan Lingkup |
| 8 | Register keluhan dan register NC/CA pernah digabung dalam usulan sintesis | "Satu register NC/CA (sumber audit, keluhan, insiden; FRM-10 untuk RCA rinci)" dengan butir "Com 12, 16"; "keluhan sebagai jenis tiket" | context/audit sintesis, bagian 3 (baris 444 dan 450) |
| 9 | Nama jabatan: VP Commercial (JA-03), Business Development (JA-07), Direktur (JA-02) | Daftar Jabatan HR-ORG-01 | specs/HR-ORG-01.json |

## 3. Pemetaan kriteria (Description baris 54)

| Unsur kriteria | Di dokumen |
|---|---|
| Mencatat feedback/keluhan | Tabel 1 (tanggal, customer, jenis, saluran, isi); butir 4.1 sampai 4.2; langkah 6.2 sampai 6.7 |
| PIC | Tabel 2 kolom PIC; butir 4.3; langkah 6.8; peran VP Commercial dan PIC |
| Tindakan | Tabel 2 kolom Tindakan; butir 4.4; langkah 6.10 |
| Status penyelesaian | Tabel 2 kolom Status dan Tanggal Selesai; tiga status di Definisi; butir 4.7; langkah 6.11 dan 6.12 |
| Konfirmasi kepada customer | Tabel 3 (tanggal, saluran, isi, tanggapan customer); butir 4.5 dan 4.6; langkah 6.13 sampai 6.15 |
| Eskalasi bila diperlukan | Tabel 4; butir 4.9 sampai 4.11; langkah 6.16 sampai 6.18 |
| Klausul ISO (checklist tidak memberi acuan) | Acuan ISO: ISO 9001:2015 8.2.1, 9.1.2, 10.2, 7.5.3; ISO/IEC 27001:2022 Annex A 5.12; satu label "(USULAN, perlu konfirmasi konsultan)" |

## 4. Hasil uji

- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/COM-REG-01.json /tmp/pen-COM-REG-01/COM-REG-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-COM-REG-01/COM-REG-01.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "17 butir (USULAN) menunggu ACC" (keluaran di /tmp/pen-COM-REG-01/lint_final.json). Lulus sejak putaran pertama; perbaikan bahasa dari dua pertanyaan di bagian 7 dan putaran perbaikan 1 (di bawah) diuji ulang dengan hasil sama.
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-COM-REG-01/COM-REG-01.docx` memberi "All validations PASSED!".
- Pratinjau soffice ke PDF, 12 halaman; lembar kontak 50 dpi dilihat: Identity, Approval, TOC, sepuluh bagian, dan empat tabel register (10 baris kosong tiap tabel) tampil; judul kolom tidak terpotong; pdftotext menemukan semua judul kolom. Halaman tidak dibaca satu per satu pada resolusi penuh (UNMEASURED).
- Skrip kecil: kode SNX di badan (SNX-COM-SOP-01, SNX-HR-ORG-01, SNX-ISMS-PRO-01, SNX-OPS-FRM-10, SNX-OPS-SOP-04; SNX-HR-JA-01 dibuang pada sweep) sama persis dengan tabel Dokumen Terkait: nol kurang, nol lebih. Em-dash dan en-dash di badan: nol. Pencarian "pelanggan", "tim", "penyusun", "dokumen sumber", "draf ini", "Lead", nama orang di badan: nol (satu kemunculan "komplain" sengaja, di arti istilah Keluhan kritis, sebagai nama istilah di SNX-COM-SOP-01). "Direktur (COO)" hanya di tabel Definisi sebagai penyebutan pertama; sesudahnya "COO". Samuel di badan = "Direktur Utama".
- Lint dan validator hanya membuktikan format dan larangan pola. Kebenaran isi terhadap bahan diperiksa lewat tabel di atas.

## 4a. Putaran perbaikan 1

Temuan verifikator (qa/COM-REG-01.verify.r1.json) dan perubahannya:

| Temuan | Perubahan | Letak |
|---|---|---|
| Pemilik register bertentangan (Peran: COO; Rekaman: VP Commercial) | Rekaman baris 1 kini "Pemilik: COO. Pengelola: VP Commercial. Pencatat: Business Development", sama dengan Peran dan Process Owner "Direktur" (= COO menurut data_conflicts). Beda dengan SNX-COM-SOP-01 dan 02 tetap di OI-4 | Rekaman; OI-4; U-10; U-11 |
| Butir 4.6 tanpa pelaku dan rancu dengan kolom Status | "Business Development membalas feedback dan keluhan yang customer kirim lewat email atau WhatsApp dalam batas respons SNX-COM-SOP-01 bagian 8 (USULAN)." | Butir 4.6; U-04 |
| Kalimat pasif atau benda sebagai pelaku | Pengecualian baris 2 dan 3 dan pembuka Isi Register kini bersubjek Business Development | Ruang Lingkup; Isi Register |
| Sinonim | "keberatan customer" diganti Keluhan; "customer satisfaction" diganti "kepuasan customer" di badan (kutipan di notes tetap asli). Rujukan JA-07 kemudian dibuang pada sweep | Peran; Dokumen Terkait |
| Langkah 6.7 rancu | "menulis ringkasan isi feedback atau keluhan" (dipilih ringkasan, sejalan dengan 6.14) | Langkah 6.7 |

Uji ulang: render tanpa galat; lint generic `"pass": true`, `"fails": []`; validator OOXML "All validations PASSED!"; PDF 12 halaman, halaman 5 sampai 12 berisi teks badan (221 sampai 335 kata per halaman, halaman 12 berisi Kesimpulan 27 kata; halaman 1 sampai 4 sampul, Identity, Revision, TOC). Kode SNX di badan sama persis dengan tabel Dokumen Terkait. Pencarian "satisfaction", "keberatan", em-dash, en-dash di badan: nol.

## 5. Keputusan data dan pemetaan peran

- Tiket: Zammad untuk keluhan yang ditangani Operation, GLPI untuk lainnya; berlabel USULAN karena batas generalist belum dirinci owner. Nomor tiket ditulis hanya bila tiket ada; dokumen tidak mewajibkan tiket per keluhan (open item OI-6).
- Vault: tidak relevan, tidak disebut. PPN: tidak relevan, tidak disebut. Tarif, nilai kontrak, dan angka lain: tidak ada di badan.
- Klasifikasi header INTERNAL (prompt dan worklist). Register terisi memuat data customer, jadi butir 4.12 menetapkan RESTRICTED (Internal) sebagai USULAN dan Rekaman merujuk butir itu (OI-5).
- Istilah tunggal: customer (bukan pelanggan atau klien), feedback, keluhan (bukan komplain atau keberatan, kecuali nama istilah sumber di Definisi), kepuasan customer (bukan "customer satisfaction" di badan), konfirmasi kepada customer, tindakan, PIC, eskalasi, Selesai.
- Peran dibedakan: Penerima meneruskan; Business Development mencatat dan menyampaikan konfirmasi; VP Commercial (pengelola register) menunjuk PIC, menetapkan Selesai, menetapkan keluhan kritis, dan mengeskalasi ke COO; PIC bertindak; COO pemilik register (satu pemilik di Peran dan Rekaman, selaras Process Owner "Direktur") dan tujuan eskalasi tingkat berikut. Menurut data_conflicts, "Direktur" di blok tanda tangan adalah orang yang sama dengan COO.

Pemetaan peran sumber ke nama peran di bagian 5 (basis: specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| sales, Sales Executive | Business Development | JA-07; sama dengan COM-SOP-01 dan COM-SOP-02 (tafsir di sana berlabel USULAN) |
| VP of Commercial | VP Commercial | JA-03 |
| Direktur, COO | COO (sesudah "Direktur (COO)") | JA-02, aturan data_conflicts; pemilik register |
| Penerima, PIC | tidak ada di HR-ORG-01 | Peran per kasus yang dibuat dokumen ini; pemegangnya karyawan yang menjabat menurut HR-ORG-01 (USULAN) |
| Service Delivery Manager | tidak dipakai di badan | Hanya muncul lewat rujukan SNX-OPS-SOP-04 |

## 6. Penanganan cacat context/audit

Perintah: `grep -n "Customer Feedback & Complaint " context/audit/*.md`. Hasil: 0 baris. Tidak ada bagian dokumen dan tidak ada bagian 5 yang bernama itu, karena register ini T2 tanpa sumber. Saya mencari cacat yang bersinggungan lewat `grep -n -i "complaint\|komplain\|keluhan\|feedback\|keberatan" context/audit/*.md` dan membaca bagian 5 Sales SOP (fileId 19Hex8...), bagian 5 SNX-OPS-FRM-10, dan bagian sintesis 3 dan 5.

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Sales SOP: "Tidak ada tenggat untuk follow-up lead, approval internal, atau handover; hanya CRM 24 jam (hal. 13) dan batas respons komunikasi (hal. 14)" | Tidak ada tenggat penanganan, konfirmasi, atau eskalasi keluhan yang dikarang. Dokumen hanya merujuk batas respons email dan WhatsApp di SNX-COM-SOP-01 bagian 8 (butir 4.6, USULAN). Open item OI-2 |
| 2 | Sales SOP: matriks eskalasi menyebut "komplain kritis" tanpa kriteria (definisi serupa, "strategis", dicatat tidak ada) | Definisi Keluhan kritis menunjuk matriks sumber; butir 4.10 memberi penilaian sementara (USULAN). Open item OI-1 |
| 3 | Sales SOP: "tidak ada mekanisme verifikasi atau rekaman bukti kepatuhan selain CRM" | Register ini menjadi rekaman untuk keluhan dan konfirmasi kepada customer. Hubungannya dengan CRM tidak diputuskan: OI-8 |
| 4 | Sales SOP: alat hanya "CRM" tanpa nama produk | Dokumen tidak menyebut CRM. Nama produk tidak dikarang |
| 5 | Sales SOP: KPI Customer Satisfaction tanpa bobot atau target | Di luar scope register; register tidak memuat KPI atau angka kepuasan |
| 6 | SNX-OPS-FRM-10: Sumber RCA mencakup "Keluhan pelanggan" padahal petunjuk hanya menyebut empat pemicu; di spec repo keluhan tidak mewajibkan RCA | Dokumen tidak menyatakan keluhan wajib RCA. Rujukan ke SNX-OPS-FRM-10 hanya untuk keluhan yang berasal dari insiden layanan, berlabel USULAN (U-13) |
| 7 | Sintesis: register keluhan digabung ke satu register NC/CA ("Com 12, 16") dan "keluhan sebagai jenis tiket" | Register dibuat sesuai checklist baris 54 (berdiri sendiri). Penggabungan dicatat sebagai open item OI-7. "Keluhan sebagai jenis tiket" dipakai lewat kolom Nomor Tiket (butir 4.8) |
| 8 | Sales SOP: komposisi tim tidak konsisten (hanya "Business Development" di Scope, isi menyebut Sales Executive) | Dipakai nama peran HR-ORG-01 (Business Development, JA-07); tanpa nama orang |

## Asumsi

- A1. "Konfirmasi kepada customer" dibaca sebagai pemberitahuan dari SINUX kepada customer tentang tindakan atau hasil penanganan. Kolom Tanggapan Customer ditambahkan agar tanggapan customer atas konfirmasi itu tercatat; kolom ini tidak diminta kriteria (U-12).
- A2. "Status penyelesaian" dibaca sebagai tiga nilai: Baru, Dalam Penanganan, Selesai. Nilai itu tidak bersumber (U-05).
- A3. "PIC" dibaca sebagai jabatan, bukan nama orang, selaras dokumen lain dan aturan nama di badan dokumen.
- A4. "Eskalasi bila diperlukan" dibaca sebagai dua tingkat: keluhan kritis ke VP Commercial (bersumber), VP Commercial ke COO (USULAN). Tabel 4 kosong untuk keluhan yang tidak dieskalasi.
- A5. Feedback dan keluhan memakai register yang sama dan kolom yang sama; kolom Jenis membedakannya. Feedback yang tidak memerlukan tindakan boleh berstatus Selesai bila VP Commercial memutuskan tidak ada tindakan (arti Selesai).
- A6. Sepuluh baris per tabel adalah ukuran tata letak, bukan klaim volume.
- A7. Sumber tidak ada, jadi register berupa docx dengan baris kosong. Bentuk pakai harian (docx atau spreadsheet) tidak diputuskan: OI-9.
- A8. Rujukan JA-07 ("keberatan pelanggan" dalam konteks negosiasi) tidak dipakai sebagai dasar. Dasar penunjukan Business Development sebagai pencatat hanya SNX-COM-SOP-01 butir 4.17 (kepuasan customer).

## USULAN

19 kemunculan label "(USULAN" di spec (17 berbentuk "(USULAN)" persis, dihitung lint; dua berbentuk "(USULAN, perlu konfirmasi konsultan)" dan "(USULAN; batas ...)"), dikelompokkan jadi 16 butir. Satu butir (U-15) dan satu butir (U-16) tanpa label di badan. Pemutus yang disarankan memakai kelompok: owner, Samuel, Aziz, FAT, Legal, Fani.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U-01 | Penerima meneruskan, Business Development mencatat di Tabel 1 (tanggung jawab customer satisfaction di Business Development bersumber; penunjukan pencatat register tidak) | Butir 4.2; Peran | owner |
| U-02 | VP Commercial menunjuk PIC; PIC ditulis jabatan; Business Development menulis tindakan | Butir 4.3 dan 4.4 | owner |
| U-03 | Business Development menyampaikan konfirmasi kepada customer dan mencatatnya di Tabel 3 | Butir 4.5 | owner |
| U-04 | Business Development membalas feedback dan keluhan dalam batas respons email (1 hari kerja) dan WhatsApp (2 jam kerja) di SNX-COM-SOP-01 bagian 8; angka dirujuk, tidak disalin | Butir 4.6 | owner |
| U-05 | VP Commercial menetapkan status Selesai; tiga nilai status dan arti Selesai | Butir 4.7; Definisi Status Penyelesaian | owner |
| U-06 | Zammad untuk tiket yang ditangani Operation, GLPI untuk lainnya; batas generalist | Butir 4.8; Rekaman baris 2 | owner |
| U-07 | Penilaian sementara keluhan kritis oleh Business Development dan VP Commercial sampai kriteria ada | Butir 4.10 | owner |
| U-08 | VP Commercial mengeskalasi ke COO bila keputusan melewati wewenang menurut delegasi tertulis | Butir 4.11; Peran | owner dan Samuel |
| U-09 | Register terisi berklasifikasi RESTRICTED (Internal) | Butir 4.12; Rekaman | Fani (pemilik SNX-ISMS-PRO-01) dan owner |
| U-10 | Folder Google Drive departemen Commercial; pemilik register COO, pengelola VP Commercial, pencatat Business Development; pemilik tiket PIC; penyimpanan oleh Business Development; diubah W9: pemilik register kini VP Commercial, juga pengelola (A7); pencatat Business Development tetap | Butir 4.13; Rekaman | owner |
| U-11 | COO sebagai pemilik register dan peninjau tahunan (process_owner "Direktur"); sama di Peran dan Rekaman; diubah W9: peninjau tahunan dan pemilik register kini VP Commercial, bukan COO (A7); process_owner "VP Commercial" | Peran; Rekaman; Kesimpulan; Identity | owner |
| U-12 | Struktur kolom Tabel 1 sampai 4, termasuk kolom Tanggapan Customer dan 10 baris | Isi Register | owner |
| U-13 | SNX-OPS-FRM-10 sebagai wadah analisis akar masalah untuk keluhan dari insiden layanan | Ruang Lingkup baris 2; Dokumen Terkait | Fani |
| U-14 | Klausul ISO 9001:2015 8.2.1, 9.1.2, 10.2, 7.5.3 dan ISO/IEC 27001:2022 Annex A 5.12, label "(USULAN, perlu konfirmasi konsultan)" | Acuan ISO | konsultan lewat owner |
| U-15 | Pengecualian cakupan (empat baris) diturunkan dari kriteria baris karena sumber diam | Ruang Lingkup tabel dikecualikan | owner |
| U-16 | Arti istilah Feedback, Keluhan, Eskalasi, Konfirmasi kepada customer, Penerima, PIC, Tindakan (arti umum, bukan definisi SINUX) | Definisi | owner |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| OI-1 | Kriteria "komplain kritis" tidak ada di Sales SOP maupun SNX-COM-SOP-01. Butir 4.10 memakai penilaian sementara; kriteria tertulis (dampak, nilai kontrak, kaitan dengan SLA) perlu ditetapkan | owner |
| OI-2 | Tidak ada tenggat penanganan, konfirmasi kepada customer, atau eskalasi keluhan di sumber mana pun. Hanya batas respons email dan WhatsApp umum yang bersumber. Dokumen tidak punya baris SLA | owner |
| OI-3 | Retensi register dan tiket keluhan ("Belum ditetapkan" di Rekaman), serta lokasi folder Google Drive Commercial (U-10) | Legal dan owner |
| OI-4 | process_owner "Direktur" (= COO) mengikuti aturan dokumen tanpa sumber, sedangkan SNX-COM-SOP-01 dan SNX-COM-SOP-02 memakai VP Commercial dari sumber. Di dokumen ini COO pemilik register dan VP Commercial pengelola; apakah pemilik disamakan dengan dokumen Commercial lain; ditutup W9: Process Owner diputus VP Commercial (A7) | owner |
| OI-5 | Header INTERNAL (worklist) berbeda dengan butir 4.12 (register terisi RESTRICTED (Internal)). Bila header diubah ke RESTRICTED (Internal), footer akan berlabel otomatis | owner dan Fani |
| OI-6 | Siapa membuat tiket keluhan, apakah tiket wajib per keluhan, dan apakah Business Development punya akses ke Zammad; batas generalist di GLPI | owner |
| OI-7 | Sintesis audit menggabungkan register keluhan dan register NC/CA (Com 12 dan 16); checklist memuat register ini terpisah dan tidak memuat dokumen NC/CA Commercial. Register dibuat sesuai checklist. Perlu keputusan apakah keluhan yang berujung tindakan korektif rinci punya wadah tersendiri | owner |
| OI-8 | Hubungan dengan CRM: SNX-COM-SOP-01 butir 4.3 mewajibkan Business Development mencatat customer engagement di CRM. Apakah feedback dan keluhan juga dicatat di CRM, atau register ini jadi satu-satunya catatan | owner |
| OI-9 | Bentuk pakai harian: register berformat docx dengan 10 baris per tabel, padahal register lazimnya lembar kerja. Apakah Tabel 1 sampai 4 dipindah ke spreadsheet dan di mana | owner |
| OI-10 | Batas wewenang VP Commercial untuk memutus keluhan dan kapan perlu ke COO tergantung delegasi tertulis (Authority Matrix belum bernomor di Job Analysis) | Samuel dan owner |
| OI-11 | Cara Penerima di luar Commercial (misalnya Operation) meneruskan keluhan ke Business Development tidak diatur; butir 4.2 hanya menyebut "meneruskan" tanpa saluran internal | owner |
| OI-12 | Survei kepuasan customer dan laporan evaluasinya (sintesis, butir Commercial 11) tidak ada di checklist 88 baris; dikecualikan dari register ini dan tidak dibuat | owner |
| OI-13 | Judul dan klausul ISO belum dicocokkan dengan teks standar (tidak ada salinan di repo); konsultan menetapkan klausul final | konsultan lewat owner |
| OI-14 | Kalimat perintah kepada AI di bahan dan di berkas context/audit: nihil | tidak ada |

## 7. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI:

1. Draf pertama: tabel Ruang Lingkup membuka tiga baris berturut-turut dengan "Register ini mencatat/hanya"; diperbaiki jadi "Tindakan dicatat secara ringkas", "Yang dicatat adalah feedback dan keluhan per kasus", dan "Register hanya untuk customer".
2. Draf pertama: langkah 6.5 memakai dua pasang koma berlapis ("memilih satu Jenis, Feedback atau Keluhan, sesuai arti"); diganti kurung. Butir 4.10 "Sampai ada" ambigu; diganti "Sampai kriteria itu ada". Definisi Keluhan kritis menyalin kalimat "kriterianya belum ditetapkan" yang juga ada di butir 4.10; kalimat di Definisi dihapus supaya satu fakta disebut sekali. Kalimat dasar di baris Business Development (tabel Peran) semula membuat satu sel memuat tiga rujukan butir; diurutkan ulang. Rujukan JA-07 yang sempat ditambahkan dibuang pada sweep karena JA-07 menulis "keberatan pelanggan" dalam konteks negosiasi, bukan keluhan.
3. Dibiarkan: 14 dari 18 langkah Cara Mengisi diawali "Business Development menulis". Alasan: satu langkah satu pelaku satu tindakan (RUNBOOK §6a.2) dan nama peran wajib persis sama dengan tabel Peran. Penyederhanaan hanya mungkin bila owner memutus pencatat lain.
4. Dibiarkan: butir 4.2 sampai 4.8, 4.10 sampai 4.13 hampir semuanya berakhir "(USULAN)". Alasan: tiap butir memuat keputusan yang berbeda dan tabel USULAN memetakannya satu per satu; butir 4.1 dan 4.9 sengaja tanpa label karena struktural atau bersumber (SNX-COM-SOP-01 bagian 9). Konsolidasi satu label di kepala bagian 4 akan menutupi butir bersumber.
5. Dibiarkan: kalimat Definisi pendek dan seragam, karena bagian itu hanya memuat arti istilah.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:

- Angka: "10" baris per tabel (ukuran tata letak, bukan klaim). "1 hari kerja" dan "2 jam kerja" tidak ada di badan, hanya dirujuk lewat SNX-COM-SOP-01 bagian 8 (asal Sales SOP). "P1 dan P2" dari SNX-OPS-SOP-04. Nomor butir, tabel, dan bagian adalah penomoran dokumen. Tidak ada angka lain.
- Nama: tidak ada nama orang di badan. Nama Laras, Amirull, dan Samuel hanya di blok Approval (dari prompt dan config/defaults.json). Sistem: Zammad dan GLPI (config/defaults.json ticketing), Google Drive (folder departemen Commercial: USULAN, tidak bersumber), WhatsApp dan email (SNX-COM-SOP-01 daftar sistem). Kode dokumen dan nama jabatan dari spec repo (Draft, bisa basi).
- Tanggal: tidak ada; Effective Date kosong.
- Klausul ISO dan judulnya dari pengetahuan standar, UNMEASURED terhadap teks standar; ditandai USULAN (U-14, OI-13).
- Tanpa kutipan langsung: seluruh alur butir 4.2 sampai 4.13 dan langkah 6.1 sampai 6.18 (berlabel USULAN per butir), tiga nilai status, kolom Tanggapan Customer, empat pengecualian cakupan, dan arti istilah umum (U-15, U-16). Semuanya ada di tabel USULAN di atas.

## Sweep

Putaran sweep dari orkestrator (satu butir). Uji ulang: render tanpa galat; lint generic `"pass": true`, `"fails": []`; validator OOXML "All validations PASSED!"; `python3 -I reports/orch/blankscan.py /tmp/pen-COM-REG-01/COM-REG-01.docx` memberi `ok 12 COM-REG-01.docx []`. Kode SNX di badan sama persis dengan tabel Dokumen Terkait (lima kode).

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Rujukan JA-07 (Peran dan Dokumen Terkait) | Peran, baris Business Development: "SNX-COM-SOP-01 butir 4.17 menempatkan kepuasan customer pada Business Development, dan uraian JA-07 di SNX-HR-JA-01 memuat tugas menjaga dokumentasi keluhan customer." Dokumen Terkait: baris SNX-HR-JA-01 "Uraian JA-07 Business Development memuat tugas menjaga dokumentasi keluhan customer." | Peran: "SNX-COM-SOP-01 butir 4.17 menempatkan kepuasan customer pada Business Development." Baris SNX-HR-JA-01 dibuang dari Dokumen Terkait. JA-07 dilepas sebagai dasar karena kutipan aslinya "keberatan pelanggan" dalam konteks negosiasi, bukan keluhan |

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A7 Identity | Process Owner "Direktur" | Process Owner "VP Commercial" |
| A7 Peran, baris VP Commercial | "Pengelola register." | "Pemilik dan pengelola register." |
| A7 Peran, baris COO | "Pemilik register ini. Memutuskan keluhan ..." | "Memutuskan keluhan ..." |
| A7 Rekaman, baris register | "Pemilik: COO. Pengelola: VP Commercial." | "Pemilik dan pengelola: VP Commercial." |
| A7 Kesimpulan | "COO meninjau register ini setiap tahun (USULAN)." | "VP Commercial meninjau register ini setiap tahun (USULAN)." |

Butir 3 (A3): tidak ada atasan atau garis lapor JA-03/JA-04 di dokumen ini; tidak diubah. Eskalasi VP Commercial ke COO (butir 4.11) tetap.

Open item ditutup atau diubah:
- OI-4 (pemilik register COO vs VP Commercial) dan U-10, U-11 (pemilik COO): ditutup W9 (A7).

R2: tidak ada perubahan spec untuk dokumen ini; hanya baris open item dan USULAN yang ditandai ditutup atau diubah W9 (butir 3).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil (label "(USULAN)" di butir 4.8, 4.10, Peran, dan Isi Register dipindah ke akhir butir; jumlah tetap 19).
### W10 kalimat dihapus atau dipindah
- Definisi, Keluhan kritis: "Penilaiannya diatur di butir 4.10." dihapus (kalimat penunjuk).
- Peran, rujukan penunjuk dihapus: "(butir 4.2)", "(butir 4.2 sampai 4.6, 4.8 sampai 4.11, dan 4.13)", "(butir 4.3, 4.7, 4.9 sampai 4.11)", "(butir 4.4)", "(butir 4.11)". Tugasnya tetap tertulis lengkap di sel.
- Cara Mengisi, rujukan penunjuk dihapus: "(butir 4.2)" di 6.1, "(butir 4.1)" di 6.2, "(butir 4.3)" di 6.8, "(butir 4.8)" di 6.9, "(butir 4.4)" di 6.10, "(butir 4.7)" di 6.11, "(butir 4.5)" di 6.13, "(butir 4.9 sampai 4.11)" di 6.16.
- Isi Register: "Business Development mengisi sel data yang kosong menurut bagian Cara Mengisi." dihapus (penunjuk).
- Butir 4.7: "Status Selesai berlaku hanya bila arti Selesai pada bagian Definisi terpenuhi" ditulis ulang merujuk tabel Status Penyelesaian (nama heading yang ada di dokumen).
- Butir 4.13: "di lokasi yang tertulis pada tabel Record" diganti faktanya: folder Google Drive departemen Commercial.
- Rekaman: "Klasifikasi menurut butir 4.12." dan "Zammad atau GLPI menurut butir 4.8." diganti faktanya. Acuan ISO 5.12: "menurut butir 4.12" dihapus.
### W10 selisih angka
nihil (subst_diff build kosong).
### W10 catatan
- Sebutan pihak luar: customer (sama dengan semua dokumen Commercial).
- Cara Mengisi ditulis sebagai kalimat perintah untuk Business Development (pengisi utama di Peran); butir 6.1 tetap menyebut Penerima karena dikerjakan peran lain.
- Tabel 1 sampai Tabel 4 dilebarkan ke 16 cm (kolom isi paling lebar, Status 2,2 cm) dan diberi min_row_cm 0,8. Halaman tetap 12, ISI mulai halaman 8 (sebelumnya 9).

### W10 koreksi worker (temuan nonblocking qa/COM-REG-01.w10.json)
- Tabel Rekaman dan tabel Acuan ISO (Annex A 5.12): fakta pengganti rujukan butir 4.12 membawa label butir asal (USULAN).
