# Catatan penyusun OPS-FRM-08: Technical Ticket / Incident Register

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-08.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-FRM-08 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-08.xlsx specs/OPS-FRM-08.patch.json /tmp/pen-OPS-FRM-08/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), 5 data validation dan 2 aturan conditional formatting di Register, 1505 rumus di Register, 25 rumus di Ringkasan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-08_Technical_Ticket_Incident_Register.xlsx (150836 byte, berkas xlsx di Drive, bukan Google Sheet) | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz | 2026-10-13T06:09:23Z (get_file_metadata, dicek ulang hari ini, cocok dengan prompt; fileSize 150836 cocok dengan hasil dekode) | read_file_content (teks), download_file_content (didekode ke /tmp/src/OPS-FRM-08.xlsx; kerja di /tmp/pen-OPS-FRM-08/; semua 6 sheet dibaca dengan python3 -I + openpyxl; gambar xl/media/image1.png dibuka) |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris OPS-FRM-08 (row 75) | berkas ekspor checklist W0 | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.5.1, 8.7, 9.1.1" dan ISO/IEC 27001:2022 "5.25, 5.26" (cocok dengan iso_9001 dan iso_27001 di checklist.json) |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, bagian SNX-OPS-FRM-08 (baris 2294 sampai 2545) | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir bagian 5 dicocokkan ulang ke berkas xlsx |
| Pendukung (bahan) | SNX-OPS-SOP-04 (Bagian 7.1, 7.2, 7.5), SNX-ISMS-SOP-01 (Bagian 8), SNX-OPS-ML-00 (riwayat review no. 5 dan 10), judul SNX-ISMS-FRM-02 | salinan audit | Dibaca dari context/audit, bukan dari Drive terbaru; kutipan bisa basi bila tim sudah mengubah dokumen itu |

Sheet sumber: Kontrol Dokumen (A1:E37), Alur Proses (judul, legenda, 1 gambar), Target Severity (A1:D8), Daftar (5 daftar dropdown), Register (A1:W305, kapasitas baris data 5 sampai 305), Ringkasan (A1:G11). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Register adalah rekap audit untuk semua tiket teknis dan insiden; tiket hidup di sistem ticketing, ekspornya boleh ditempel | Kontrol Dokumen B15: "Register seluruh tiket teknis dan insiden dengan waktu Ack dan pemulihan, status SLA, dan tautan RCA sesuai SNX-OPS-SOP-04." dan B18: "Tiket operasional hidup di Zammad (Nusagrid) atau Service Hub GLPI (GMF dan internal). Register ini adalah rekap audit; ekspor dari ticketing system boleh ditempel di sheet Register dengan kolom yang sama." | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |
| 2 | Target Ack dan update per severity berasal dari SOP-04; target pulih berlabel USULAN; jam kerja dihitung sebagai jam kalender | Target Severity A2: "Ack dan update dari SNX-OPS-SOP-04. Target pemulihan = USULAN internal; komitmen ke pelanggan mengikuti kontrak. Jam kerja dihitung sebagai jam kalender untuk penyederhanaan." Nilai B5:B8 (Ack menit) 15, 30, 120, 1440; C5:C8 (update menit) 60, 180, 1440, "Saat selesai"; D4 "Target pulih (jam), USULAN" dengan D5:D8 4, 8, 24, 72 | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |
| 3 | RCA wajib untuk P1 dan P2 dengan nomor dari FRM-10; ambang KPI 95% hanya untuk Ack P1 dan P2 | Kontrol Dokumen B21: "Kolom RCA wajib otomatis Ya untuk P1 dan P2; isi nomor RCA dari SNX-OPS-FRM-10." Ringkasan A11: "P1 dan P2 di-ack sesuai target (KPI 95%)" | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |

Fakta pendukung yang tidak diubah: Kontrol Dokumen B9 "RESTRICTED (Internal)"; B10 "Lead NOC"; B12 "Klausul 8.5.1, 8.7, 9.1.1"; B14 "3 tahun"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan". Rumus Register (identik tiap baris 5 sampai 305, tidak diubah): P `=IF(G5="","",IF(OR(G5="P1",G5="P2"),"Ya","Tidak"))`; S `=IF(OR(I5="",J5=""),"",ROUND((J5-I5)*1440,0))`; T `=IF(OR(I5="",K5=""),"",ROUND((K5-I5)*24,1))`.

## 2. Isi patch (apa yang diubah dan kenapa)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Register baris 5 (A sampai R, W) | Baris CONTOH TKT-2026-0001 dengan placeholder `[pelanggan]` dan `[engineer]` | Dikosongkan lewat clear_rows; rumus P5, S5, T5, U5, V5 tetap | RUNBOOK §6 (buang baris CONTOH, bukan hapus baris) |
| Register A2 | "Kolom abu-abu dihitung otomatis. Baris biru muda = CONTOH." | "Kolom abu-abu dihitung otomatis. Tiket kelas Keamanan (ke SOC) diserahkan ke SOC; insidennya dicatat di SNX-ISMS-FRM-02. Tiket tanpa waktu Ack atau Pulih belum masuk persentase di sheet Ringkasan." | Kalimat CONTOH tidak berlaku sesudah baris dikosongkan dan alat menolak teks CONTOH di luar Kontrol Dokumen. Dua kalimat baru menjawab cacat audit butir 5 dan 7 (bagian 3) |
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt; penulisan Draft sama dengan FRM-02 |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by; USULAN 2 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 5.25, 5.26" | "Kontrol Annex A 5.25, 5.26" | 5.25 dan 5.26 adalah kontrol Annex A, bukan klausul; "klausul atau kontrol" ragu-ragu. Angka sama dengan acuan checklist |
| B18 Cara pakai 1 | "Tiket operasional hidup di Zammad (Nusagrid) atau Service Hub GLPI (GMF dan internal). Register ini adalah rekap audit; ..." | "Tiket Ops dibuat di Zammad (Nusagrid), tiket generalist di Service Hub GLPI (USULAN, batas menunggu owner). Register ini adalah rekap audit; ekspor dari ticketing system boleh ditempel di sheet Register dengan kolom yang sama." | Premis owner: Zammad untuk Ops, GLPI untuk generalist (defaults.json ticketing). Kalimat kedua tim dipertahankan utuh. USULAN 1 |
| B19 Cara pakai 2 | "Isi waktu dalam format tanggal dan jam (WIB)." | "Isi Severity dulu, lalu waktu dalam format tanggal dan jam (WIB)." | Rumus U dan V memberi #N/A bila Severity kosong tetapi waktu terisi (cacat audit butir 6) |
| B20 Cara pakai 3 | "Respon, durasi pulih, dan status SLA dihitung otomatis memakai sheet Target Severity." | "Respon (Dilaporkan sampai Ack), durasi pulih (Dilaporkan sampai Pulih), dan status SLA dihitung otomatis memakai sheet Target Severity." | Titik mulai waktu tidak tertulis di sumber; diambil dari rumus S dan T (cacat audit butir 4) |
| B25 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Legenda lama menyuruh menghapus baris yang sudah kosong. Kotak A25 tetap biru (alat tidak mengubah warna di luar clear_rows). Kalimat sama dengan FRM-04 |
| C30 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A31 sampai E31 | Baris riwayat kedua: Revisi 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; topik RTO tidak ada di form ini. USULAN 4 |
| B35, B36, B37 | "Lead NOC", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 2 |
| B4, B5, B7, B8, B9, B10, B12, B14, B15, B21, E30, sheet lain | | Tidak diubah | B4 nomor, B5 judul, B9 klasifikasi, B12 acuan 9001 sudah sama dengan nilai yang diminta. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama. B14 masa simpan dari sumber. B7 dan B8 bukan tanggal efektif. Tanda tangan dan tanggal di C35 sampai D37 tetap kosong. Target Severity, Daftar, Alur Proses (gambar), Ringkasan tidak disentuh |

Hitung ulang LibreOffice atas out.xlsx: Ringkasan P1 sampai P4 semuanya 0, KPI kosong, tidak ada sel galat, Register baris 5 kosong semua. Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter). Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas 145 sel teks out.xlsx: nol temuan.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, pengesahan dan tanda tangan kosong | Dipertahankan: keadaan yang benar untuk Draft (batas keras 3). Tanda tangan dan tanggal tidak diisi |
| 2 | Target pulih seluruhnya USULAN; Ack dan update dari SOP-04; nilai cocok dengan Bagian 6 SOP-04 | Tidak diubah. Label USULAN dan kalimat "komitmen ke pelanggan mengikuti kontrak" tetap |
| 3 | Jam kerja dihitung sebagai jam kalender; SOP-04 menulis Ack P3 "2 jam kerja" dan P4 "1 hari kerja"; ML-00 no. 10 Terbuka | Tidak diubah: kalimat tim di Target Severity A2 sudah jelas dan keputusannya butuh kalender kerja. Open item 2 |
| 4 | Durasi pulih dihitung dari Dilaporkan, Cara pakai tidak menyebut titik mulai | Diperbaiki di B20 (titik mulai Respon dan Durasi pulih ditulis) |
| 5 | Tiket tanpa waktu Ack atau Pulih menghasilkan kosong dan tidak tercatat sebagai pelanggaran | Diberi keterangan di Register A2 (belum masuk persentase Ringkasan). Rumus tidak diubah karena legenda sumber menyebut sel rumus "jangan diubah". USULAN 5 dan 6 |
| 6 | #N/A pada U dan V bila Severity kosong tetapi waktu terisi | Dicegah lewat urutan isi di B19 (Severity dulu). Rumus tidak diubah. USULAN 5 |
| 7 | Kelas "Keamanan (ke SOC)" tanpa tautan ke SNX-ISMS-FRM-02 atau SNX-ISMS-SOP-01; kolom N teks bebas | Register A2 menautkan tiket kelas Keamanan ke SOC dan ke SNX-ISMS-FRM-02. Dasar: SOP-04 Bagian 7.2 butir 4 "Berindikasi keamanan: serahkan ke SOC (SNX-ISMS-SOP-01)." dan ISMS-SOP-01 Bagian 8 butir 3 "Satu insiden = satu parent ticket; alert terkait ditautkan. Insiden dicatat di SNX-ISMS-FRM-02." Pelaku pencatat tidak tertulis di sumber, jadi kalimat dibiarkan tanpa pelaku. Kolom N tetap teks bebas (menambah validasi mengubah struktur). Open item 5 |
| 8 | Satu baris CONTOH; tanggal November 2026 lebih akhir dari tanggal draft; ikut terhitung di periode default Ringkasan | Diperbaiki: baris 5 dikosongkan, A2 dan legenda B25 dibersihkan. Ringkasan jadi nol (hitung ulang LibreOffice). Periode B3 dan B4 (1 sampai 30 November 2026) adalah sel input, dibiarkan. Open item 8 |
| 9 | KPI 95% hanya untuk Ack P1 dan P2, tanpa padanan pemulihan | Tidak diubah: baris KPI baru menambah metrik yang ambangnya belum diputus. USULAN 7 |
| 10 | Tidak ada kredensial atau data pribadi sensitif; hanya placeholder | Dikonfirmasi ulang atas out.xlsx: nama orang hanya di blok Disetujui dan Pengesahan dari defaults.json. Placeholder `[pelanggan]` dan `[engineer]` ikut hilang bersama baris contoh |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B18 menulis "Service Hub GLPI (GMF dan internal)", sedangkan premis owner 14 Okt memberi Zammad untuk Ops dan GLPI untuk generalist | B18 ditulis ulang berlabel USULAN. Penyebutan GMF dan internal dilepas dari sel karena batas "generalist" belum dirinci owner. USULAN 1, open item 1 |
| B | B13 "Klausul atau kontrol Annex A" | Diganti "Kontrol Annex A" |
| C | Riwayat revisi punya dua baris Revisi 00 bertanggal sama; baris kedua menyebut RTO | Baris kedua dikosongkan; teks asli dicatat di bagian 2. USULAN 4 |
| D | Gambar Alur Proses: tidak ada cabang untuk tiket kelas Keamanan; kotak pertama "Zammad atau Service Hub" | Tidak bisa diubah lewat xlsx_patch (gambar tetap). Open item 4 |
| E | Rujukan RCA: KPI no. 14 di RPT-01 butuh tanggal kirim RCA, register ini hanya punya "RCA wajib" dan "No RCA" | Tidak diubah (kolom baru). USULAN 8, open item 3 |

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiket Ops dibuat di Zammad dan tiket generalist di Service Hub GLPI. Sumber tim menyebut GMF dan internal sebagai cakupan Service Hub; batas "generalist" belum dirinci owner | Kontrol Dokumen B18 (berlabel USULAN di sel) | Owner, dengan Fani |
| 2 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Lead NOC, ISO/ISMS Coordinator, COO. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 3 | Pemilik dokumen tetap "Lead NOC" sesuai sumber. Peran ini belum dipetakan ke jabatan; Fani dipakai sebagai pemeriksa karena defaults | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Penjaga rumus agar Severity kosong tidak memberi #N/A. U5 menjadi `=IF(OR(S5="",G5=""),"",IF(S5<=INDEX('Target Severity'!$B$5:$B$8,MATCH(G5,'Target Severity'!$A$5:$A$8,0)),"Ya","Tidak"))`; V5 dengan T5 dan kolom D analog; berlaku baris 5 sampai 305 | Register kolom U dan V (belum diterapkan) | Fani |
| 6 | Penanda tiket yang belum di-ack atau belum pulih melewati target, supaya tidak lolos dari hitungan pelanggaran | Register, kolom baru (belum diterapkan) | Fani |
| 7 | Baris KPI "Pulih sesuai target" di Ringkasan, padanan baris 11; angka ambang tidak diusulkan karena tidak ada sumber | Ringkasan (belum diterapkan) | Fani |
| 8 | Kolom "Tgl kirim RCA" di Register agar KPI "RCA P1 dan P2 terkirim dalam 2 hari kerja" (RPT-01) bisa dihitung dari register ini | Register, kolom baru (belum diterapkan) | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Pembagian Zammad dan Service Hub GLPI untuk tiket GMF dan internal. SOP-04 sumber menulis "Service Hub untuk GMF dan internal" (7.1 butir 1), FRM-08 sumber sama; premis owner memberi Zammad untuk Ops. SOP-04, FRM-09, dan form ini harus sama | Owner, Fani, lane OPS-SOP-04 |
| 2 | Target Ack P3 dan P4 dihitung sebagai jam kalender sedangkan SOP-04 menulis jam kerja; ML-00 no. 10 masih Terbuka karena kalender kerja belum ditetapkan | Fani |
| 3 | RPT-01 KPI no. 14 butuh tanggal kirim RCA; register tidak punya kolomnya (USULAN 8) | Fani |
| 4 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch: tidak ada cabang tiket Keamanan, dan kotak pertama masih "Zammad atau Service Hub". Butuh entri LEAD bila gambar harus diganti (ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah) | Orkestrator |
| 5 | Register A2 menautkan tiket Keamanan ke SNX-ISMS-FRM-02 berdasarkan SOP-04 7.2 dan ISMS-SOP-01 Bagian 8. Pelaku pencatat di FRM-02 tidak tertulis di sumber; cocokkan setelah ISMS-SOP-01 dirender | Orkestrator (lane ISMS-SOP-01) |
| 6 | Peran "Lead NOC" sebagai pemilik dokumen belum dipetakan ke jabatan (matriks peran dan SK penunjukan belum ada) | Fani, owner |
| 7 | Keterbatasan alat: kotak legenda A25 tetap biru; nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka. Tinggi baris B18 tetap, teks 3 baris pas di render LibreOffice; HUMAN-VERDICT: lihat di Excel apakah baris B18 terpotong | Orkestrator, owner |
| 8 | Periode default Ringkasan 1 sampai 30 November 2026 (B3 dan B4) lebih akhir dari tanggal draft; sel input, perlu diisi ulang tiap periode | Fani |
| 9 | Masa simpan 3 tahun (sumber) berbeda dari 5 tahun untuk SNX-OPS-FRM-10 dan SNX-ISMS-FRM-02 yang ditautkan; tidak diubah | Fani |
| 10 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: "Baris CONTOH: hapus atau timpa saat dipakai", "Isi waktu dalam format tanggal dan jam (WIB).", "isi nomor RCA dari SNX-OPS-FRM-10", "Sel rumus: jangan diubah". Satu-satunya yang dijalankan adalah pengosongan baris contoh, karena prompt memerintahkan clear_rows yang sama | Orkestrator |
| 11 | Tanggal draft 13 Oktober 2026 (B7, C30 lama) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |

## Asumsi dan tafsir

- "Approval persis" dari prompt mengalahkan sumber di blok Disusun, Diperiksa, Disetujui, mengikuti defaults.json.
- Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber FRM-08 maupun di patch; dicek dengan pola lint_doc atas semua sel teks out.xlsx.
- Fakta tentang SOP-04, ISMS-SOP-01, dan ML-00 diambil dari salinan audit, tidak dibuka di Drive.
- Satu-satunya kalimat baru yang berisi isi proses adalah dua kalimat di Register A2. Keduanya turunan dari rumus sumber (kalimat tentang Ringkasan) dan dari SOP-04 7.2 dan ISMS-SOP-01 Bagian 8 (kalimat tentang Keamanan), bukan proses baru.

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas 12 entri `set` berisi teks dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| B18 dan "(USULAN, batas menunggu owner)": penanda penyusun di dokumen resmi terdengar seperti catatan rapat | Dipertahankan: RUNBOOK §0 butir 4 mewajibkan label untuk hal tanpa sumber; alasannya ada di USULAN 1. Kata "generalist" tidak diganti karena itu kata owner |
| Register A2 memuat tiga kalimat berurutan dengan pola sama (subjek tiket, lalu keterangan) | Dibiarkan: tiap kalimat membawa fakta berbeda (warna, Keamanan, Ringkasan). Tidak ada kelompok tiga yang dipaksakan, tidak ada penutup positif |
| B20 memakai tanda kurung ganda | Dipertahankan: satu kalimat tim diberi dua keterangan titik mulai; alternatif dua kalimat lebih panjang dari tinggi baris |
| B25 telegrafis | Dipertahankan: kalimat sama dengan FRM-04, satu fakta |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust) | Tidak ada di nilai patch (pencarian karakter dan lint). Notes ini tidak memakai em-dash atau en-dash |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di prompt dan defaults.json |
| "Kontrol Annex A 5.25, 5.26" dan "Klausul 8.5.1, 8.7, 9.1.1" | Prompt, checklist.json row 75, sel B12 dan B13 sumber |
| Zammad untuk Ops, Service Hub GLPI untuk generalist | Premis owner 14 Okt (defaults.json ticketing); penerapan ke form ini berlabel USULAN di sel B18 |
| Titik mulai Respon dan Durasi pulih (Dilaporkan) | Rumus sumber S5 dan T5 |
| Kalimat Ringkasan di Register A2 | Rumus sumber D7 sampai D10 (penyebut = jumlah "Ya" dan "Tidak") |
| Tautan Keamanan ke SNX-ISMS-FRM-02 | SOP-04 7.2 butir 4 dan ISMS-SOP-01 Bagian 8 butir 3 (salinan audit), kode SNX-ISMS-FRM-02 berjudul Security Incident & Investigation Records |
| "3 tahun", "RESTRICTED (Internal)", "Lead NOC", "13 Oktober 2026", "KPI 95%", angka Target Severity | Sumber FRM-08, tidak diubah |
| Rumus di USULAN 5 | Turunan rumus sumber U5 ditambah syarat G5; berlabel USULAN, belum diterapkan |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.

## ISO-W9

Spec dan patch tidak diubah di putaran ini (G-3 A9).

| Butir | Sebelum | Sesudah |
|---|---|---|
| Open item gambar Alur Proses | Terbuka, menunggu gambar baru lewat LEAD | Status diubah; teks open item lama tetap |

Open item yang ditutup atau diubah:

- Open item 4 (gambar Alur Proses: tanpa cabang tiket Keamanan, kotak pertama Zammad atau Service Hub): ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan".
Cara pakai 1: "(USULAN, batas menunggu owner)" ditulis "pembagian ini masih menunggu keputusan owner (USULAN)"; label tetap satu, di akhir kalimat itu.
Register A2: "(ke SOC)" dihapus karena sudah tersirat di "diserahkan ke SOC"; arti tetap.
Target Severity A2: "Target pemulihan = USULAN internal" ditulis sebagai kalimat; kata USULAN tetap.
