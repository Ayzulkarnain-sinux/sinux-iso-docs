# Catatan penyusun OPS-PRC-01: Operations Business Process Flow

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-PRC-01.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-PRC-01 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Process owner "Head of Operation" mengikuti "Pemilik dokumen" di sumber, tanpa nama. Approval persis dari config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revisi 00, effective_date kosong, review YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-PRC-01_Operations_Business_Process_Flow.docx (342402 byte) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 | 2026-10-13T06:09:03Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (teks); download_file_content didekode ke /tmp/pen-OPS-PRC-01/src/ (docx 342402 byte, ukuran sama dengan metadata). Dua gambar rId23.png dan rId28.png dibuka dan cocok dengan deskripsi di context/audit. comments.xml dan footnotes.xml tidak berisi teks |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content. Bahan saja (catatan worklist) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte) | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content. Bahan saja (catatan worklist) |
| Kriteria penerimaan | config/worklist.json baris OPS-PRC-01 | Kolom Description berisi nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "4.4, 8.1, 8.2, 8.5" dan ISO/IEC 27001:2022 "4.4, 8.1" |
| Nama peran | specs/HR-ORG-01.json (DONE) | spec lokal repo, bukan Drive | Daftar jabatan dan matriks peran. Dipakai untuk nama peran di bagian 5, PIC bagian 6 dan 8 |
| Cacat sumber | context/audit/iso-sinux-supdocs-ops-2026-10-14.md (berkas ops/SNX-OPS-PRC-01.md, POL-OPS-001, PRO-OPS-001), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | DATA, dibandingkan dengan docx asli |
| Lintas dokumen (hanya untuk menyamakan istilah) | specs/OPS-FRM-06.json, specs/OPS-FRM-01.patch.json | spec lane lain, bisa basi | Definisi hypercare dan tempat Checklist G1 dan G3 |

Isi sumber diperlakukan sebagai data. Tidak ada kalimat perintah di tiga berkas sumber yang perlu dicatat sebagai open item.

## 2. Fakta penting dan kutipan sumber

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "Dokumen ini memetakan proses bisnis Divisi Operation SINUX, dari kontrak ditandatangani sampai layanan berjalan, diukur, dan diperbaiki." (PRC-01 Bagian 1) | Bagian 1 (kalimat tim dipertahankan, kata "record" diganti "rekaman") |
| 2 | Scope dan pengecualian | "Di luar ruang lingkup: app-level pelanggan (isi aplikasi, plugin, database aplikasi, kode pelanggan), keputusan harga dan komersial, serta SOC yang menurut kontrak menjadi tanggung jawab pelanggan." (PRC-01 Bagian 2) | Bagian 2, utuh |
| 3 | Gate tertulis | "Setiap deal baru berpindah tangan tiga kali. Tiap perpindahan wajib lolos gate tertulis:" (PRC-01 Bagian 6) | Bagian 4 butir 2 |
| 4 | Penolakan G3 dan hypercare | "Operation berhak menolak serah terima G3 secara tertulis bila checklist belum lengkap. Selama G3 belum lolos, layanan berstatus hypercare dengan pemilik SD dan PM." (PRC-01 Bagian 6) | Bagian 4 butir 3; penanganan di bagian 9 |
| 5 | Pemilik gate dan bukti | "G1 Kick-off \| Commercial \| SD dan PM \| Service Delivery Manager \| Checklist G1 pada SNX-OPS-FRM-01"; "G2 UAT dan BAST \| SD dan PM \| Pelanggan \| Project Manager \| SNX-OPS-FRM-05, BAST pada SNX-OPS-FRM-06"; "G3 Serah terima operasi \| SD dan PM \| NOC dan SOC \| Head of Operation \| Checklist G3 pada SNX-OPS-FRM-06" (tabel Bagian 6) | Bagian 3 (dari dan ke), bagian 6.2 (pemilik dan bukti) |
| 6 | Delapan proses inti, pemilik, input, output, prosedur, rekaman | "\| 4 \| UAT, verifikasi, serah terima \| Service Delivery Manager \| Layanan terpasang, kriteria uji \| UAT lolos, BAST, serah terima ke Operation \| Pelanggan, Operation \| SNX-OPS-SOP-01 \| SNX-OPS-FRM-05, SNX-OPS-FRM-06 \|" (contoh satu baris, tabel Bagian 5) | Bagian 6.1, satu langkah per proses |
| 7 | Perubahan atas proses ini | "Perubahan pada proses ini diajukan ke Head of Operation, dikaji dampaknya terhadap SLA dan keamanan informasi, lalu disahkan COO sebelum dokumen direvisi." (Bagian 9) | Bagian 6.3 langkah 1 sampai 3 |
| 8 | Pengukuran kinerja | "Kinerja proses diukur bulanan melalui SNX-OPS-RPT-01 dan dibahas dalam tinjauan manajemen." (Bagian 9) | Bagian 6.3 langkah 4 dan 5, bagian 8 |
| 9 | Ketidaksesuaian proses | "Ketidaksesuaian proses (gate dilewati, record tidak lengkap, SLA terlewat berulang) ditangani melalui SNX-OPS-FRM-10." (Bagian 9) | Bagian 9 baris 4 |
| 10 | Pemilik dokumen, klasifikasi, acuan | "Pemilik dokumen \| Head of Operation"; "Klasifikasi \| RESTRICTED (Internal)"; "Acuan ISO 9001:2015 \| Klausul 4.4, 8.1, 8.2, 8.5"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 4.4, 8.1" (tabel atribut) | Identity, bagian 11 |
| 11 | Sistem tiket | "Tiket pelanggan Nusagrid \| Zammad (integrasi WhatsApp dan telepon) \| Ticketing system untuk layanan Nusagrid" dan "Tiket GMF dedicated dan permintaan internal \| SINUX Service Hub (GLPI, ticket.sinux.co.id) \| Termasuk change request dan Shift Log" (tabel Bagian 8) | Bagian 3 (definisi), bagian 4 butir 8 |
| 12 | Kredensial, Jumphost, rekaman | "Kredensial tidak pernah di chat, tiket, atau dokumen"; "Rekam sesi untuk audit akses"; "Google Drive SINUX, terkendali sesuai SNX-ISMS-PRO-01"; "Master record mengikuti masa simpan di tiap dokumen" (tabel Bagian 8) | Bagian 4 butir 9 sampai 11 |
| 13 | Masa simpan dokumen ini | "Masa simpan record \| Berlaku sampai digantikan" (tabel atribut) | Bagian 11, tabel rekaman, baris terakhir |
| 14 | Interaksi dengan proses pendukung ISMS | "Backup aktif dan restore teruji adalah syarat G3"; "Aset baru didaftarkan sebelum G3; perubahan konfigurasi melalui SNX-OPS-SOP-02"; "Insiden teknis berindikasi keamanan diserahkan ke SOC" (tabel Bagian 7, sembilan baris) | Bagian 11 tabel Dokumen terkait; syarat G3 di bagian 6.2 langkah 4 |
| 15 | Syarat G1 | "PO atau kontrak, scope final, SLA tertulis, PIC pelanggan, janji lisan tercatat" (POL-OPS-001 Bagian 8, tabel gate) | Bagian 6.2 langkah 2 |
| 16 | Syarat G2 | "UAT lolos, BAST ditandatangani, isu sisa punya pemilik" (POL-OPS-001 Bagian 8) | Bagian 6.2 langkah 3 |
| 17 | Syarat G3 | "Terdaftar di Service Hub, monitoring aktif, backup teruji, as-built, runbook, akses lewat Jumphost" (POL-OPS-001 Bagian 8) dan "Backup aktif dan restore uji pertama berhasil (bila layanan backup ada)." (PRO-OPS-001 Bagian 8.2) | Bagian 6.2 langkah 4 |
| 18 | Pihak penerima tidak menerima sebelum gate lolos | "Pekerjaan tidak boleh diterima sub divisi berikutnya sebelum gate-nya lolos." (POL-OPS-001 Bagian 8) | Bagian 4 butir 2 |
| 19 | Janji lisan | "Janji ke pelanggan yang tidak tercatat di G1 tidak mengikat Operation sampai disetujui Commercial dan COO." (POL-OPS-001 Bagian 8) | Bagian 4 butir 4 (kriteria 8.2) |
| 20 | Hypercare 2 minggu | "Durasi hypercare standar 2 minggu. (USULAN)" (POL-OPS-001 Bagian 8) | Bagian 8, berlabel (USULAN) |
| 21 | Kick-off internal 3 hari kerja | "Kick-off internal (SD dan PM, NOC, SOC bila ada, Tech dan Product) dalam 3 hari kerja sejak PO. (USULAN)" (PRO-OPS-001 SDPM-01) | Bagian 8, berlabel (USULAN) |
| 22 | Laporan bulanan hari kerja ke-5 | "Kirim paling lambat hari kerja ke-5." (PRO-OPS-001 SDPM-04); "Laporan SLA terkirim hari kerja ke-5" (KPI 11 SNX-OPS-RPT-01, salinan audit) | Bagian 8 |
| 23 | G1 tidak lolos | "G1 tidak lolos: paket dikembalikan ke Commercial, onboarding belum dimulai." (PRO-OPS-001 Bagian 8.3) | Bagian 9 baris 1 |
| 24 | G3 tidak lolos | "G3 tidak lolos: Operation menolak serah terima secara tertulis; layanan tetap hypercare dengan pemilik SD dan PM sampai kriteria terpenuhi." dan "Pemilik gate mencatat kriteria yang belum lolos di tiket, beserta pemilik dan tanggal targetnya." (PRO-OPS-001 Bagian 8.3) | Bagian 9 baris 2 |
| 25 | Deal lost | "Deal yang gagal dicatat lost oleh Commercial dengan alasannya. Prospek yang ditunda tetap dipegang Commercial, bukan Operation." (PRO-OPS-001 Bagian 8, teks di bawah gambar) | Bagian 9 baris 3 |
| 26 | Pihak penerima briefing G3 | "Briefing serah terima ke Lead NOC dan Lead SOC, tanda terima tercatat." (PRO-OPS-001 Bagian 8.2) | Bagian 6.2 langkah 5 |
| 27 | Pemimpin tinjauan manajemen | "Penetap kebijakan mutu, sasaran mutu, dan sumber daya; pemimpin tinjauan manajemen \| Direktur Utama (JA-01)" (matriks peran specs/HR-ORG-01.json) | Bagian 5 dan bagian 6.3 langkah 5 |

## 3. Pemetaan klausul ISO (kriteria baris ini)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 4.4 | Ya | Butir 1 (pemilik proses) | 6.1 |
| ISO 9001:2015 8.1 | Ya | Butir 2 (gate tertulis) | 6.2 |
| ISO 9001:2015 8.2 | Ya | Butir 4 (janji pelanggan yang belum tercatat di G1) | 6.2 langkah 1 dan 2 |
| ISO 9001:2015 8.5 | Ya | Butir 5 (BAU hanya setelah G3, perubahan konfigurasi lewat SNX-OPS-SOP-02) | 6.1 langkah 3 sampai 5 |
| ISO/IEC 27001:2022 4.4 | Ya | Butir 1 dan 6 (proses pendukung ISMS) | 6.1 |
| ISO/IEC 27001:2022 8.1 | Ya | Butir 2 dan 6 | 6.2 |
| Tambahan dari bagian Referensi sumber: 9001 8.6, 8.7, 9.1, 10.2; 27001 6.1, 9.1, Annex A 5.37 | Ya, kalimat terpisah | 8.6: butir 3; 9.1: bagian 6.3 langkah 4; 8.7 dan 10.2: bagian 9 baris 4; 6.1: tabel Dokumen terkait (REG-02, REG-03); A 5.37: dokumen ini sendiri | |

Nama klausul dalam tanda kurung di bagian 11 berasal dari standar, bukan dari sumber tim. Perlakuan cacat label: sumber menulis "Klausul atau kontrol Annex A 4.4, 8.1". Di bagian 11 dokumen ini 4.4 dan 8.1 ditulis sebagai klausul utama ISO/IEC 27001:2022 dan dinyatakan bukan kontrol Annex A (Annex A memuat kontrol bernomor 5.x sampai 8.x, dan 8.1 di sana berarti kontrol lain).

## 4. Keputusan data

- Approval: persis dari config/defaults.json (D2). Sumber menulis "Disusun oleh Head of Operation", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber. Akibatnya bagian 6.3 langkah 3 tetap memuat COO sebagai pengesah perubahan proses (kalimat sumber), sedangkan blok Approved By memuat Direktur Utama. Dicatat sebagai open item 1.
- Sebutan: "Direktur (COO)" pada sebutan pertama di badan dokumen (bagian 3), sesudahnya "COO". Direktur Utama dipakai di badan dokumen (bagian 5 dan 6.3). Tidak ada nama orang di badan dokumen.
- Nama peran bagian 5: dari specs/HR-ORG-01.json. Delapan peran dipakai: Direktur Utama (JA-01), COO (JA-02, sebutan Direktur), VP Commercial (JA-03), Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager, Project Manager. Peran sumber yang tidak ada di sana dipetakan: "Commercial (VP Commercial)" jadi VP Commercial; "Tim implementasi" (pelanggan proses 2) jadi NOC dan SOC (asumsi 6); "ISO/ISMS Coordinator" tidak dipakai di badan dokumen (pemeriksa diganti Fani oleh defaults; HR-ORG-01 K-13 mencatat peran itu belum punya pemegang). Peran "Pemilik proses" ditambahkan karena sumber memakainya sebagai peran generik (Bagian 9 butir 1) dan PIC langkah pengajuan perubahan butuh peran.
- Tiket: Zammad untuk tiket pelanggan Nusagrid, Service Hub (GLPI) untuk tiket GMF dedicated dan permintaan internal (kedua baris dari tabel sumber, cocok dengan kata owner "zammad untuk ops, glpi untuk generalist"). Penempatan change request dan Shift Log di Service Hub berasal dari sumber, tetapi pekerjaan itu milik Operation, sehingga batas dengan Zammad belum jelas. Ditulis (USULAN) dan masuk open item 5. Batas "generalist" belum dirinci owner.
- Vault: ditulis "Password manager (vault)" dengan status "menunggu konfirmasi Ops" (defaults). Sumber menulis vault tanpa status. Tidak ada klaim aktif atau belum live.
- PPN dan rumusan keuangan: tidak relevan untuk dokumen ini.
- Department "Operation".
- Klasifikasi RESTRICTED (Internal): label sumber; footer berlabel otomatis oleh renderer.
- Masa simpan: template tidak punya field masa simpan di Identity. Sumber menulis "Berlaku sampai digantikan" untuk dokumen ini dan "mengikuti masa simpan di tiap dokumen" untuk rekaman; keduanya masuk tabel rekaman bagian 11 tanpa angka baru.

## 5. Penanganan cacat context/audit

Perintah yang dijalankan: `grep -n 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 context/audit/*.md`, `grep -n 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv context/audit/*.md`, `grep -n 1U8CAdibwBk9x_-Aic2lbev144d6WReTz context/audit/*.md`. Hasil: semuanya di context/audit/iso-sinux-supdocs-ops-2026-10-14.md (PRC-01 mulai baris 3159, POL-OPS-001 baris 15, PRO-OPS-001 baris 342) dan baris indeks di iso-sinux-supdocs-sintesis-2026-10-14.md.

PRC-01 (bagian 5 Catatan kualitas dan celah, 10 butir):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | DRAFT, Disetujui "Menunggu", dua baris riwayat revisi sama-sama 00 | Teratasi oleh template: satu baris Revision 00, Effective Date kosong, Signature kosong, status Draft |
| 2 | Label ISO 27001 "Klausul atau kontrol Annex A 4.4, 8.1" bertentangan dengan Bagian 3 | Diperbaiki: 4.4 dan 8.1 ditulis sebagai klausul utama, bukan Annex A. Klausul 6.1, 9.1, dan Annex A 5.37 dari Bagian 3 sumber dibawa sebagai kalimat terpisah |
| 3 | Proses 1 kolom Prosedur "Prosedur Commercial" tanpa kode | Diperbaiki sebagian: ditulis SNX-COM-SOP-01 (SOP Sales Process, ada di worklist wave W3) berlabel (USULAN). Tidak ada bukti sumber bahwa itu prosedur yang dimaksud. Open item 4 |
| 4 | Proses 5 memetakan SNX-OPS-SOP-03 (Preventive & Corrective Maintenance) walau proses bernama operasi layanan 24/7 | Dipertahankan. Output sumber proses 5 menyebut "maintenance terlaksana", jadi pemetaan masuk akal. Langkah proses 5 menyebut maintenance secara eksplisit |
| 5 | Kode PRO-OPS-001 (SHF-01, NOC-0x, CHG-01, SVC-01) tidak dirujuk; dua skema kode paralel | Tidak diperbaiki diam-diam: kode prosedur PRO-OPS-001 tidak dikutip, hanya PRO-OPS-001 bagian 8.2 sebagai dasar checklist gate. Kedua dokumen POL dan PRO ada di tabel Dokumen terkait dengan keterangan penomoran berstatus usulan. Open item 11 |
| 6 | Zammad di PRC-01, POL-OPS-001 P-08 menulis semua tiket di GLPI | Diperbaiki mengikuti defaults dan tabel PRC-01 (bagian 4 butir 8). P-08 POL tidak diikuti karena bertentangan dengan kata owner. Open item 5 |
| 7 | Pemilik proses 4 (Service Delivery Manager) berbeda dari pemilik gate G2 (Project Manager) dan G3 (Head of Operation) | Tidak diubah, karena konsisten dengan POL-OPS-001. Perbedaan diterangkan: definisi "Pemilik proses" dan "Pemilik gate", dan satu kalimat di intro bagian 6.1. Open item 6 |
| 8 | Frasa "keselarasan RTO dan target pulih" di riwayat revisi tanpa isi | Tidak dibawa (riwayat revisi diganti satu baris template). Target pemulihan ditunjuk ke SNX-ISMS-PLN-01 di tabel Dokumen terkait, tanpa angka. Matriks severity SNX-OPS-SOP-04 yang memuat target pulih berada di luar dokumen ini |
| 9 | Hypercare: teks menaruhnya selama G3 belum lolos, gambar menaruhnya sesudah G3 ("2 minggu, usulan") | Diputuskan mengikuti teks: sama dengan POL-OPS-001 Bagian 8, PRO-OPS-001 Bagian 8.3, dan definisi di SNX-OPS-FRM-06. Diagram bagian 7 menggambar hypercare sebagai cabang dari G3 yang tidak lolos. Angka 2 minggu dibawa di bagian 8 berlabel (USULAN). POL-OPS-001 Bagian 9.2 dan PRO-OPS-001 tabel 8.1 (Lead NOC sebagai pemilik hypercare) tidak diikuti. Open item 3 |
| 10 | Label klasifikasi PRC-01 "RESTRICTED (Internal)" berbeda dari POL dan PRO "RESTRICTED (internal, restricted:ops)" | Dipakai label PRC-01, sama dengan tingkat SNX-ISMS-PRO-01. Label "restricted:ops" tidak dibawa |

Butir POL-OPS-001 dan PRO-OPS-001 yang relevan:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| POL 3 | Pemilik POL: COO di tabel kontrol, Head of Operation di Bagian 9.1 | Tidak berdampak langsung. Pemilik dokumen ini = Head of Operation (sumber PRC-01) |
| POL 6, PRO 7 | Sistem tiket dan hubungannya dengan Zammad | Lihat PRC-01 butir 6 |
| POL 7, PRO 8 | Rujukan AI internal (DOCTRINE, DEC-, HANDOVER, SKILL_, CLAIM_CLASS_POLICY, SINUX_LEGAL, SINUX_SERVICE_HUB, "packet setor", "jalur staging", "blok ukur", "blok ubah") | Tidak ada yang dibawa. Lint "terlarang" lulus |
| POL 8 | P1 memuat tuntutan komersial dan hal legal | Di luar scope dokumen ini (dokumen ini tidak memuat definisi P1; hanya menyebut tingkat severity P1 dan P2 di definisi) |
| POL 11 | RACI Change Major dengan dua R | Tidak dibawa, di luar scope |
| PRO 2 | Langkah berlabel USULAN (kick-off 3 hari kerja, hypercare 2 minggu, dan lainnya) | Hanya dua yang dipakai, keduanya tetap berlabel (USULAN): kick-off dan hypercare. RCA 2 hari kerja, uji restore bulanan, laporan IR 24 jam, dan lainnya milik SOP lain dan tidak dibawa |
| PRO 5 | Dua urutan dan dua pemilik hypercare | Lihat PRC-01 butir 9 |
| PRO 6 | Teks "lost" tanpa kotak lost di gambar | Dibawa sebagai baris pengecualian bagian 9 dengan pelaku VP Commercial. Sumber PRC-01 sendiri tidak memuat cabang lost |
| PRO 9 | Tidak ada klausul ISO dan tidak ada masa simpan | Klausul dari sumber PRC-01 dan baris acuan worklist. Masa simpan ditulis di tabel rekaman bagian 11 |
| PRO 7, 10, 11 | NOC-06 3 hari kerja vs H-2 dan H-5; SOC-04 dasar kebijakan; tiket 10 menit | Di luar scope dokumen ini, tidak dibawa |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber PRC-01)

1. Format sumber: tabel SIPOC delapan kolom dipadatkan ke tabel langkah tiga kolom template. Nama proses ada di awal kalimat langkah, pemilik di kolom PIC, input dan output di kalimat, prosedur di akhir kalimat, rekaman dan pelanggan proses di kolom Output / Rekaman. Nomor langkah sama dengan nomor proses.
2. Kolom "Pemilik" proses 5 di sumber berbunyi "Head of Operation (Lead NOC, Lead SOC)". Dibaca: Head of Operation pemilik, Lead NOC dan Lead SOC menjalankan operasi harian (POL-OPS-001 Bagian 9.1 menyebut Head of Operation membawahi keduanya).
3. Sembilan baris proses pendukung di sumber (Bagian 7) diubah jadi keterangan tabel Dokumen terkait, bukan langkah prosedur, karena sumber menulis kalimat pasif tanpa pelaku ("Aset baru didaftarkan sebelum G3"). Pelaku tidak ditebak. Tiga di antaranya jadi syarat Checklist G3 (aset terdaftar, backup dan restore teruji) di bagian 6.2.
4. Pelaku pengisi Checklist G3 (Project Manager), penerima briefing (Lead NOC dan Lead SOC), dan penyatu keputusan (Head of Operation) dari PRO-OPS-001 tabel 8.1 baris 9 ("SD dan PM (R), Lead NOC dan Lead SOC (R)") dan specs/OPS-FRM-06.json. Sumber PRC-01 hanya menyebut pemilik gate.
5. Syarat tiap gate (bagian 6.2) diambil dari POL-OPS-001 Bagian 8 dan PRO-OPS-001 Bagian 8.2. Sumber PRC-01 hanya menyebut bukti ("Checklist G1 pada SNX-OPS-FRM-01"). Daftar butir checklist di FRM-01 dan FRM-06 belum tentu sama dengan daftar ini; keduanya disusun lane lain.
6. "Tim implementasi" (pelanggan proses 2) diganti "NOC dan SOC". Dasarnya PRO-OPS-001 tabel 8.1 tahap 7 ("NOC dan SOC (R lewat change request)"). Alasan penggantian: aturan "tidak ada tim tanpa keterangan".
7. Pemilik rekaman di bagian 11 = pemilik proses di baris SIPOC yang sama. Lokasi "Google Drive SINUX" dari baris "Dokumen dan record" di Bagian 8 sumber. Retensi tiap rekaman "mengikuti masa simpan di dokumennya" dari kalimat sumber yang sama; angka tiap dokumen tidak disalin karena beda antardokumen (mis. FRM-02 "Durasi kontrak + 3 tahun", FRM-07 "3 tahun") dan itu milik dokumen masing-masing.
8. Direktur Utama sebagai pemimpin tinjauan manajemen (bagian 6.3 langkah 5): dari matriks peran HR-ORG-01. Sumber PRC-01 hanya menulis "dibahas dalam tinjauan manajemen".
9. Pengaju perubahan proses = pemilik proses (bagian 6.3 langkah 1). Sumber menulis pasif ("diajukan ke Head of Operation").
10. Service Delivery Manager sebagai pelaksana kewajiban "SD dan PM" untuk hypercare dan sebagai PIC SLA hypercare: tafsir, karena Service Delivery Manager membawahi sub divisi SD dan PM (POL-OPS-001 Bagian 9.4, HR-ORG-01).
11. Kalimat "Proses 1 ... dipetakan di sini hanya sampai paket handover G1" di Scope adalah tafsir penyusun untuk menyelaraskan proses 1 (dimiliki VP Commercial) dengan pengecualian "keputusan harga dan komersial". Sumber tidak menjelaskan.
12. Definisi umum (UAT, BAST, RCA, BAU, Deal, Commercial, Gate, P1 dan P2, Shift Log) adalah penjelasan penyusun, bukan kalimat tim. Singkatan NOC dan SOC dari judul bagian PRO-OPS-001. P1 dan P2 dari skala di POL-OPS-001 Bagian 6.
13. Nama klausul ISO di bagian 11: dari standar, bukan dari sumber.
14. Review tahunan (bagian 8 baris terakhir): dari config/defaults.json review_period YEARLY, bukan dari sumber (POL dan PRO menulis review 6 bulan untuk dokumen mereka sendiri; tidak diikuti untuk dokumen ini).
15. Tenggat "hari kerja ke-5 bulan berikutnya" laporan SLA: dari PRO-OPS-001 SDPM-04 (laporan bulanan) dan KPI 11 RPT-01 (laporan SLA); kedua dibaca sebagai laporan yang sama dengan "Laporan SLA bulanan" proses 6.
16. Jalur G2 tidak lolos tidak ada di sumber mana pun; bagian 9 tidak memuat baris G2.

## 7. Diagram

Satu diagram di bagian 7, rankdir TB, 11 simpul: delapan proses inti, gate G1 dan G3 (belah ketupat), dan hypercare. Nama pemilik ada di baris bawah tiap kotak, tanpa lane, karena lane dengan node berjauhan membuat kluster saling tindih (percobaan pertama, dibuang). Dua garis putus-putus meniru siklus perbaikan sumber (kembali ke proses 5 dan ke proses 1). Diagram Sales sampai Operation (gambar kedua sumber, empat jalur) tidak digambar ulang karena spec sop hanya menerima satu diagram. Isinya sebagian ada di diagram ini (G1, G2, G3, hypercare) dan sebagian di bagian 6.2. Langkah Lead, Discovery, Proposal dan quote, serta cabang "tidak: nego ulang" di gambar kedua sumber tidak ada di dokumen ini. Open item 12.

## USULAN

Daftar USULAN berlabel (lint menghitung 5 butir).

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | SNX-COM-SOP-01 sebagai prosedur proses 1 (sumber menulis "Prosedur Commercial" tanpa kode) | Bagian 6.1 langkah 1; baris Dokumen terkait SNX-COM-SOP-01 | owner |
| U2 | Kick-off internal 3 hari kerja sejak PO (label USULAN di PRO-OPS-001 SDPM-01) | Bagian 8 baris 1 | Fani |
| U3 | Durasi hypercare standar 2 minggu (label USULAN di POL-OPS-001 Bagian 8) | Bagian 8 baris 2 | Fani |
| U4 | Change request dan Shift Log dicatat di Service Hub; batas dengan Zammad belum diputus | Bagian 4 butir 8 | owner |
| U5 | Status lima jabatan Divisi Operation (Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager, Project Manager) tetap usulan dan belum ada pemegang bernama (label dari POL-OPS-001 dan HR-ORG-01 K-10) | Bagian 3, baris Jabatan Divisi Operation | owner, Fani |

Tidak diberi label tetapi bersumber dari bahan dan patut dikonfirmasi: pemilik rekaman = pemilik proses (asumsi 7), pelaku Checklist G3 (asumsi 4), syarat gate dari POL dan PRO (asumsi 5), hari kerja ke-5 laporan SLA (asumsi 15). Semuanya masuk open items.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Operation berhak menolak serah terima G3 secara tertulis; selama G3 belum lolos layanan berstatus hypercare dengan pemilik SD dan PM | "Operation berhak menolak serah terima G3 secara tertulis bila checklist belum lengkap. Selama G3 belum lolos, layanan berstatus hypercare dengan pemilik SD dan PM." (Bagian 6) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |
| 2 | Perubahan atas proses ini diajukan ke Head of Operation, dikaji dampaknya terhadap SLA dan keamanan informasi, lalu disahkan COO | "Perubahan pada proses ini diajukan ke Head of Operation, dikaji dampaknya terhadap SLA dan keamanan informasi, lalu disahkan COO sebelum dokumen direvisi." (Bagian 9) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |
| 3 | Setiap deal baru berpindah tangan tiga kali dan tiap perpindahan wajib lolos gate tertulis; pemilik gate G1 Service Delivery Manager, G2 Project Manager, G3 Head of Operation | "Setiap deal baru berpindah tangan tiga kali. Tiap perpindahan wajib lolos gate tertulis:" dan "G3 Serah terima operasi \| SD dan PM \| NOC dan SOC \| Head of Operation \| Checklist G3 pada SNX-OPS-FRM-06" (Bagian 6) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |

## Open items

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis COO (Amirull), defaults dan template menulis Samuel (President Director). Defaults dipakai di blok Approved By, tetapi bagian 6.3 langkah 3 memuat COO sebagai pengesah perubahan proses sesuai kalimat sumber. Selaraskan peran pengesah perubahan dan penanda tangan dokumen | owner, Samuel |
| 2 | Pemeriksa dan penyusun: sumber menulis Head of Operation dan ISO/ISMS Coordinator, defaults menulis Erik dan Fani. ISMS Coordinator belum dipetakan ke jabatan (HR-ORG-01 K-13). Sebutan "Direktur (COO)" menunggu konfirmasi owner | owner, Fani |
| 3 | Hypercare: teks sumber (selama G3 belum lolos, pemilik SD dan PM) berbeda dari gambar sumber (sesudah G3, 2 minggu usulan) dan dari POL-OPS-001 Bagian 9.2 dan PRO-OPS-001 tabel 8.1 (Lead NOC pemilik). Dokumen mengikuti teks. Konfirmasi urutan, pemilik, dan apakah 2 minggu berlaku sebelum atau sesudah G3 | Fani |
| 4 | SNX-COM-SOP-01 dipilih sebagai prosedur proses 1 (menutup cacat "Prosedur Commercial" tanpa kode). Belum ada konfirmasi bahwa itu prosedur yang dimaksud | owner |
| 5 | Zammad lawan Service Hub: sumber menaruh change request dan Shift Log di Service Hub, kata owner Zammad untuk Ops. POL-OPS-001 P-08 menulis semua tiket di GLPI. Batas "generalist" belum dirinci. Singkatan GMF pada "tiket GMF dedicated" tidak dijelaskan di sumber | owner |
| 6 | Proses 4 dimiliki Service Delivery Manager, tetapi G2 dimiliki Project Manager dan G3 Head of Operation. Dokumen membedakan pemilik proses dan pemilik gate; konfirmasi pembedaan ini | Fani |
| 7 | Lima jabatan Divisi Operation berstatus usulan tanpa pemegang (HR-ORG-01 K-10); pemilik dokumen ini Head of Operation. Hubungan Head of Operation dengan VP Tech Operation and Services belum ditetapkan (K-09) | owner, Fani |
| 8 | Pelaku Checklist G3 (Project Manager), penerima briefing (Lead NOC, Lead SOC), dan "tim implementasi" yang diganti NOC dan SOC berasal dari PRO-OPS-001 dan SNX-OPS-FRM-06, bukan dari sumber PRC-01. Daftar butir Checklist G1 dan G3 mengikuti POL dan PRO; cocokkan dengan FRM-01 dan FRM-06 sesudah keduanya final | Fani |
| 9 | Retensi kontrak dan paket handover G1 belum ditetapkan di sumber mana pun (kolom retensi baris pertama tabel rekaman berisi "Belum ditetapkan"). Retensi rekaman lain "mengikuti dokumen" dan angkanya beda antardokumen | Legal |
| 10 | Pengajuan perubahan proses dan tinjauan manajemen tidak punya nama rekaman atau lokasi di sumber. Pelaku pengajuan (pemilik proses) adalah tafsir | Fani |
| 11 | Dua skema kode berjalan paralel: SNX-OPS-SOP/FRM dan kode prosedur PRO-OPS-001 (SHF-01, NOC-01 dan seterusnya). POL-OPS-001 dan PRO-OPS-001 masih DRAFT v0.1 dengan penomoran berstatus usulan; ganti kode bila terbit | Fani |
| 12 | Diagram kedua sumber (Sales sampai Operation, empat jalur dengan Tech dan Product) tidak digambar ulang karena format spec hanya satu diagram. Putuskan apakah cukup | owner |
| 13 | Jalur G2 tidak lolos (UAT gagal atau BAST ditolak) tidak ada di sumber mana pun; bagian 9 tidak memuat baris G2 | Fani |
| 14 | Status password manager (vault): "menunggu konfirmasi Ops" menurut defaults; sumber PRC-01 menulisnya tanpa status | Fani |
| 15 | Nama klausul ISO di bagian 11 dan klausul tambahan dari Referensi sumber (9001 8.6, 8.7, 9.1, 10.2; 27001 6.1, 9.1, Annex A 5.37) berasal dari standar dan sumber, belum dikonfirmasi konsultan | owner (konsultan) |
| 16 | Tenggat "hari kerja ke-5 bulan berikutnya" berasal dari PRO-OPS-001 dan KPI 11 RPT-01; sumber PRC-01 tidak memuat tenggat | Fani |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan dan yang saya lakukan:
- Scope di draf pertama berupa satu kalimat sepanjang 70 kata dengan enam titik koma. Saya pecah menjadi satu kalimat pengantar dan enam baris pendek, mengikuti daftar tim.
- Kolom Output / Rekaman bagian 6.1 berpola sama delapan kali ("Rekaman: ... Pelanggan proses: ..."). Terdengar mekanis, tetapi itu satu tabel dengan kolom tetap, dan polanya memang cara membaca SIPOC. Saya biarkan, tanpa menambah kata pengisi.
- Label klausul "(ISO 9001:2015 8.1; ISO/IEC 27001:2022 8.1)" di akhir butir kebijakan bisa terbaca seperti tempelan. Dipertahankan karena kriteria meminta kontrol tercermin di bagian 4. Saya batasi pada butir yang memang menjadi kontrol klausul itu, dan butir tanpa kontrol jelas (mis. data SLA, rekaman) tidak diberi label.
- Sumber menulis "Kredensial tidak pernah di chat, tiket, atau dokumen". Saya tidak memakai ekor penegas itu dan menulis "dilarang ditulis di chat, tiket, atau dokumen".
- Kolom Authority di tabel peran bukan dari sumber. Saya batasi satu klausa dari kalimat sumber atau POL, tanpa kalimat berbunga.
- Pembuka generik, penutup positif, "sangat penting", em-dash, en-dash, tebal atau huruf kapital untuk penekanan: tidak ada. Lint lulus. Daftar enam unsur pada intro bagian 6.1 ("memuat pemilik proses, input, output, ...") sama dengan kolom tabel sumber, bukan kelompok yang dipaksakan, jadi dipertahankan.
- Kalimat Tujuan, gate, hypercare, dan pengendalian proses adalah kalimat tim, dipertahankan hampir utuh (T1).
- Diagram di percobaan pertama memakai lane per peran. Hasilnya kluster Service Delivery Manager melebar melewati simpul lain dan dua label garis bertabrakan. Saya buang lane dan menaruh nama pemilik di dalam kotak.
- Istilah: "record" di sumber diseragamkan menjadi "rekaman"; "Checklist G1" dan "Checklist G3" selalu berhuruf kapital C sebagai nama rekaman; "Operation" dipakai untuk divisi, peran selalu dari tabel bagian 5.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: hanya tiga, semuanya berasal dari POL-OPS-001 atau PRO-OPS-001. 3 hari kerja (kick-off) dan 2 minggu (hypercare) berlabel (USULAN) mengikuti label asal. Hari kerja ke-5 laporan SLA tidak berlabel di PRO-OPS-001 dan dibawa tanpa label, dicatat sebagai open item 16. Setahun sekali untuk review dari config/defaults.json. Tidak ada angka lain.
- Nama orang: hanya tiga penanda tangan, dari defaults. Tidak ada nama di badan dokumen. Tidak ada tanggal; Effective Date kosong.
- Sistem: semua dari sumber PRC-01 (Zammad, Service Hub GLPI, Nusametric, Overseer, console Nusagrid, Wazuh, AegisWAF, Cloudflare, EDR, Acronis Cyber Protect, Jumphost, vault, Google Drive, WHM, cPanel, SIEM). Satu alamat portal (ticket.sinux.co.id), dari sumber.
- Tidak bersumber tim dan sudah dicatat di bagian 6: nama klausul ISO, definisi umum (UAT, BAST, RCA, BAU, Deal, Commercial, Shift Log, P1 dan P2), syarat tiap gate dari POL dan PRO, pelaku Checklist G3 dari PRO dan FRM-06, pelaku langkah tinjauan manajemen dari HR-ORG-01, pemilik rekaman, lokasi rekaman, baris pengecualian "deal lost" dari PRO-OPS-001, SNX-COM-SOP-01 (USULAN).
- Hal yang saya ubah sesudah memeriksa: label USULAN pada butir tiket semula "(USULAN, batas ...)" dan tidak terhitung lint, kini "(USULAN)" polos sehingga hitungan lint sama dengan jumlah butir (5); lane diagram dibuang; scope dipecah.
- Satu hal yang saya tidak yakin dan tidak saya klaim: apakah Checklist G1 di SNX-OPS-FRM-01 memuat tepat lima butir syarat G1 yang ditulis di bagian 6.2. Syaratnya saya ambil dari POL, bukan dari FRM-01 (open item 8).

## Hasil uji sendiri

- `python3 -m json.tool specs/OPS-PRC-01.json`: valid.
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-PRC-01.json /tmp/pen-OPS-PRC-01/OPS-PRC-01.docx`: sukses; 16 halaman (LibreOffice), diagram TB 11 simpul.
- `python3 -I tools/lint_doc.py /tmp/pen-OPS-PRC-01/OPS-PRC-01.docx sop`: "pass": true, "fails": kosong, warns hanya "5 butir (USULAN) menunggu ACC" (nol warns PIC SLA).
- Validasi OOXML (/mnt/skills/public/docx/scripts/office/validate.py): "All validations PASSED!".
- Panjang langkah prosedur: 19 langkah, terpanjang 23 kata (batas sekitar 25).
- Berkas keluaran uji: /tmp/pen-OPS-PRC-01/OPS-PRC-01.docx (bukan hasil final, render final oleh orkestrator ke out/07_Ops).

## Sweep

Putaran sweep (penghalusan sesudah DONE), butir 1: frasa proses penyusunan di badan dokumen. Dua perubahan, keduanya di bagian 11 (Acuan standar). Catatan proses dipindah ke notes: klausul tambahan dari bagian Referensi sumber PRC-01 sudah tercatat di bagian 3 dan open item 15 di atas. Fakta, angka, nama, dan struktur lain tidak berubah.

| # | Letak | Sebelum | Sesudah |
|---|---|---|---|
| 1a | Bagian 11, Acuan standar, ISO 9001:2015 | "klausul 4.4 (Sistem manajemen mutu dan prosesnya), 8.1 (Perencanaan dan pengendalian operasional), 8.2 (Persyaratan untuk produk dan jasa), dan 8.5 (Produksi dan penyediaan jasa). Referensi dokumen sumber menambah klausul 8.6 (Pelepasan produk dan jasa), 8.7 (Pengendalian keluaran yang tidak sesuai), 9.1 (Pemantauan, pengukuran, analisis, dan evaluasi), dan 10.2 (Ketidaksesuaian dan tindakan korektif)." | "klausul 4.4 (Sistem manajemen mutu dan prosesnya), 8.1 (Perencanaan dan pengendalian operasional), 8.2 (Persyaratan untuk produk dan jasa), dan 8.5 (Produksi dan penyediaan jasa). Klausul 8.6 (Pelepasan produk dan jasa) juga berlaku pada gate G3, klausul 8.7 (Pengendalian keluaran yang tidak sesuai) dan 10.2 (Ketidaksesuaian dan tindakan korektif) pada penanganan ketidaksesuaian proses, dan klausul 9.1 (Pemantauan, pengukuran, analisis, dan evaluasi) pada pengukuran kinerja proses." |
| 1b | Bagian 11, Acuan standar, ISO/IEC 27001:2022 | "klausul 4.4 (Sistem manajemen keamanan informasi dan prosesnya) dan klausul 8.1 (Perencanaan dan pengendalian operasional); keduanya klausul utama standar, bukan kontrol Annex A. Referensi dokumen sumber menambah klausul 6.1 (Tindakan untuk menangani risiko dan peluang) dan 9.1 (Pemantauan, pengukuran, analisis, dan evaluasi), serta Annex A 5.37 (Documented operating procedures)." | "klausul 4.4 (Sistem manajemen keamanan informasi dan prosesnya) dan klausul 8.1 (Perencanaan dan pengendalian operasional); keduanya klausul utama standar, bukan kontrol Annex A. Klausul 6.1 (Tindakan untuk menangani risiko dan peluang) juga berlaku pada risiko proyek berat dan temuan RCA yang dinaikkan ke register risiko ISMS, klausul 9.1 (Pemantauan, pengukuran, analisis, dan evaluasi) pada pengukuran kinerja proses, dan Annex A 5.37 (Documented operating procedures) pada dokumen ini." |

Dasar tiap klausul tambahan pada kalimat baru: 8.6 pada gate G3 (bagian 4 butir 3), 8.7 dan 10.2 pada penanganan ketidaksesuaian proses (bagian 9 baris 4), 9.1 pada pengukuran kinerja proses (bagian 6.3 langkah 4), 6.1 pada risiko proyek berat dan temuan RCA yang dinaikkan ke register risiko ISMS (tabel Dokumen terkait, SNX-ISMS-REG-02), Annex A 5.37 pada dokumen ini. Pemetaan itu sama dengan tabel di bagian 3 notes ini; tidak ada klausul atau fakta baru. Nama klausul tetap berasal dari standar (asumsi 13).

Uji sesudah sweep: render_sop.py sukses; lint_doc.py sop "pass": true, fails kosong, warns hanya "5 butir (USULAN)"; validate.py "All validations PASSED!"; blankscan.py "ok" (16 halaman, tanpa temuan). Pencarian "dokumen sumber", "penyusun", "sumber tim", "draf" di teks docx: nol temuan.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Definisi Jabatan Divisi Operation, asli: "Status kelimanya (USULAN) di POL-OPS-001 dan SNX-HR-ORG-01, dan belum ada pemegang bernama." Label dipindah ke akhir sel. Kebijakan butir 4.8, asli: "Change request dan Shift Log dicatat di Service Hub (USULAN). Batas pemakaian dengan Zammad belum diputus." Label dipindah ke akhir butir. Dokumen terkait SNX-COM-SOP-01 mendapat (USULAN) sebagai pengganti kalimat penunjuk.

### W10 kalimat dihapus atau dipindah
- Ruang lingkup: "Sistem pendukung yang dipakai proses ini disebut di bagian 4." diganti daftar sistemnya.
- Definisi Proses pendukung: "Daftarnya ada di tabel Dokumen terkait." (penunjuk).
- Kebijakan butir 4.1: "Pemilik tiap proses tercantum di butir 6.1" (penunjuk).
- Peran Pemilik proses: "(butir 6.1)".
- Intro 6.1: "pemilik gate G2 dan G3 ada di butir 6.2." diganti faktanya (G2 Project Manager, G3 Head of Operation).
- Dokumen terkait SNX-COM-SOP-01: "penunjukan ini diusulkan di butir 6.1." diganti label (USULAN).
- Bagian 9 baris Checklist G3: pengulangan pelaku "lalu Head of Operation memeriksa ulang G3" disatukan ke kalimat pertama.

### W10 selisih angka
- 6.2: hilang karena penunjuk "ada di butir 6.2" di intro 6.1 diganti faktanya; prosedur 6.2 tetap ada.

### W10 catatan
- Pihak luar: "pelanggan" (dokumen induk OPS).
- "review manajemen" ditulis "Management Review"; "bila" di syarat gate diganti "jika".

### W10 putaran perbaikan 1 (qa/OPS-PRC-01.w10.r1.json)
- Intro 6.1: "kolom Output / Record" dikembalikan ke judul kolom renderer persis, "kolom Output / Rekaman".
- 6.3 langkah 5, output: "Record Management Review" menjadi "Record hasil Management Review".
- Scope, daftar sistem pengganti rujukan bagian 4: Google Drive SINUX ditambahkan agar sama lengkap dengan bagian 4.
- Definisi Proses pendukung: contoh "kontrol akses, backup, dan manajemen risiko" dibuang; rujukan "Daftarnya tercantum di tabel Dokumen terkait." dikembalikan (penghapusan pointer di bagian kalimat dihapus di atas dibatalkan).
- Pointer lain yang diganti fakta diperiksa ulang terhadap bed1bb6: intro 6.1 (pemilik G2 dan G3) sama dengan PIC 6.2 langkah 3 dan 6; tidak ada fakta yang menyempit.
### W10 audit pointer
- .scope[9]: lengkap; "disebut di bagian 4" diganti daftar 13 sistem, dicek satu per satu terhadap butir 4.7 sampai 4.11 (Nusametric, Overseer, console Nusagrid, Wazuh, AegisWAF, Cloudflare, EDR, Acronis Cyber Protect, Zammad, Service Hub, password manager (vault), Jumphost, Google Drive SINUX), tidak ada yang hilang atau bertambah.
- .policy[0]: lengkap; kalimat penunjuk "Pemilik tiap proses tercantum di butir 6.1" dibuang (STYLE §3.2), pemilik proses tetap di kolom PIC butir 6.1.
- .roles[8][1]: lengkap; penunjuk "(butir 6.1)" dibuang, tanggung jawab tidak berubah.
- .procedures[0].intro[1]: lengkap; "pemilik gate G2 dan G3 ada di butir 6.2" diganti fakta dari kolom PIC butir 6.2 (G2 dinyatakan lolos oleh Project Manager, G3 oleh Head of Operation).
- .related_documents[5][1]: lengkap; "penunjukan ini diusulkan di butir 6.1" diganti label (USULAN), status usulan tetap terbawa.

### W10 audit cakupan label
- .policy[7]: diperbaiki (dipisah lagi; batas pemakaian dengan Zammad yang belum diputus tanpa label seperti bed1bb6)
- .related_documents[5][1]: OK (kalimat penunjuk usulan butir 6.1 diganti label)
