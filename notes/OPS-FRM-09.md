# Catatan penyusun OPS-FRM-09: SLA Performance Monitoring Report

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-09.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-FRM-09 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; isinya parameter SLA per pelanggan), audit_class B. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-09.xlsx specs/OPS-FRM-09.patch.json /tmp/pen-OPS-FRM-09/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), 2 data validation dan 1 aturan conditional formatting di Downtime Log, 202 rumus di Downtime Log, 2 aturan conditional formatting dan 362 rumus di Laporan Bulanan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-09_SLA_Performance_Monitoring_Report.xlsx (134604 byte, berkas xlsx di Drive) | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF | 2026-10-13T06:09:25Z (dari prompt tugas; tidak dicek ulang lewat metadata Drive, tetapi ukuran hasil dekode 134604 byte sama dengan "bytes: 134604" di salinan audit) | read_file_content (teks), download_file_content (didekode ke /tmp/src/OPS-FRM-09.xlsx; kerja di /tmp/pen-OPS-FRM-09/; semua 6 sheet dibaca dengan python3 -I + openpyxl; gambar xl/media/image1.png dibuka) |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris OPS-FRM-09 (row 76) | berkas ekspor checklist W0 | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "9.1.1, 9.1.2, 9.1.3" dan ISO/IEC 27001:2022 "8.16" (cocok dengan iso_9001 dan iso_27001 di checklist.json) |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, bagian SNX-OPS-FRM-09 (baris 2546 sampai 2748), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir dicocokkan ulang ke berkas xlsx dengan openpyxl |
| Pendukung | SNX-OPS-SOP-05 (Bagian 4, 5, 6.2, 6.4, 6.5, 6.6, 7) dan SNX-OPS-FRM-08 | salinan audit (SOP-05 baris 4489 dst.) | Dibaca dari context/audit, bukan dari Drive terbaru; kutipan bisa basi bila tim sudah mengubah dokumen itu. Nomor butir SOP-05 hanya dipakai di notes ini, tidak di sel mana pun, karena SOP-05 akan disusun ulang ke 11 bagian |

Sheet sumber: Kontrol Dokumen (A1:E38), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:B8), Parameter SLA (A1:I46, baris data 5 sampai 44), Downtime Log (A1:K206, baris data 5 sampai 206), Laporan Bulanan (A1:L50, rumus baris 8 sampai 47). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Workbook ini adalah tempat parameter SLA, log downtime, dan laporan availability bulanan; dasar prosedurnya SNX-OPS-SOP-05 | Kontrol Dokumen B15: "Parameter SLA per pelanggan, log downtime, dan laporan availability bulanan sesuai SNX-OPS-SOP-05." | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |
| 2 | Semua downtime dicatat; yang dikeluarkan dari hitungan hanya yang punya bukti notifikasi maintenance atau pengecualian kontrak. Availability = 1 dikurangi downtime dihitung dibagi menit kalender dalam bulan | Kontrol Dokumen B19: "Catat setiap downtime di Downtime Log; kolom Dihitung = Tidak hanya bila ada bukti notifikasi maintenance atau pengecualian kontrak." Laporan Bulanan B5: `=DAY(B4)*1440`; E8: `=IF(A8="","",1-D8/$B$5)` | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |
| 3 | Laporan dikirim ke pelanggan paling lambat hari kerja ke-5; pemilik dokumen Service Delivery Manager; masa simpan 3 tahun | Kontrol Dokumen B22: "Laporan dikirim ke pelanggan paling lambat hari kerja ke-5." B10: "Service Delivery Manager". B14: "3 tahun" | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |

Fakta pendukung yang tidak diubah: B9 "RESTRICTED (Internal)"; B12 "Klausul 9.1.1, 9.1.2, 9.1.3"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; Laporan Bulanan A49 "Disusun (Service Delivery Manager)" dan A50 "Diperiksa (Head of Operation)"; status Tercapai atau Breach di F8 `=IF(A8="","",IF(E8>=C8,"Tercapai","Breach"))`; anggaran downtime G8 `=IF(A8="","",ROUND($B$5*(1-C8),1))`. Hasil pemindaian rumus: rumus di seluruh workbook hanya merujuk kolom B, C, D sheet Parameter SLA dan kolom B, C, D, F, G sheet Downtime Log.

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (script openpyxl, python3 -I). Selain sel di bawah ini tidak ada sel yang berubah.

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Parameter SLA baris 5 dan 6 (A sampai I) | SLA-001 dan SLA-002, `[pelanggan A]`, `[pelanggan B]`, `[PIC pelanggan]`, Nusagrid IaaS 0.999, Managed backup 0.995, kolom Catatan "CONTOH" | Dikosongkan lewat clear_rows; warna isi ikut baris input baris 7 (kuning muda) | RUNBOOK §6 (buang baris CONTOH, bukan hapus baris). Target 99.9% dan 99.5% di sumber adalah data contoh, bukan target kontrak nyata, jadi tidak dipindah ke baris lain |
| Downtime Log baris 5 dan 6 (kecuali kolom F) | Dua downtime 10 dan 14 November 2026, `[pelanggan A]`, TKT-2026-0001, CR-2026-0001, "CONTOH" | Dikosongkan; rumus F5 dan F6 tetap | Sama; tanggal contoh lebih akhir dari tanggal draft |
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt; penulisan Draft sama dengan form OPS lain |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by; USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 8.16" | "Kontrol Annex A 8.16" | 8.16 adalah kontrol Annex A, bukan klausul; "klausul atau kontrol" ragu-ragu. Angka sama dengan acuan checklist |
| B22 Cara pakai 5 | "Laporan dikirim ke pelanggan paling lambat hari kerja ke-5." | "Kirim laporan ke pelanggan paling lambat hari kerja ke-5." | Pasif diganti kalimat perintah seperti butir 1 sampai 4. Pelaku tidak ditulis karena baris B22 setinggi satu baris dan alat tidak bisa mengubah tinggi baris (nama peran membuat teks terpotong, dicek di render LibreOffice). Pelakunya Service Delivery Manager menurut SOP-05 Bagian 5 ("menyusun dan mengirim laporan SLA") |
| B26 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Legenda lama menyuruh menghapus baris yang sudah kosong. Kotak A26 tetap biru (alat tidak mengubah warna di luar clear_rows). Kalimat sama dengan FRM-04, FRM-05, FRM-07, FRM-08 |
| C31 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A32 sampai E32 | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; topik RTO tidak ada di form ini (pencarian di sheet: nol kemunculan). USULAN 2 |
| B36, B37, B38 | "Service Delivery Manager", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 1 |
| Parameter SLA A2 | "Target availability dalam persen (0.999 = 99.9%). Kombinasi Pelanggan dan Layanan harus unik." | Kalimat lama utuh + "Availability dihitung dari menit kalender penuh; Jam layanan dan Pengecualian kontrak tidak masuk rumus." | Cacat audit butir 3. Kalimat baru menyatakan perilaku rumus yang terukur (B5 `=DAY(B4)*1440`, pemindaian rumus di atas), bukan aturan baru |
| Downtime Log A2 | "Durasi dihitung otomatis dalam menit." | Kalimat lama utuh + "Pelanggan dan Layanan ditulis persis seperti di Parameter SLA; bila berbeda, downtime tidak terhitung di Laporan Bulanan. Downtime lintas bulan masuk seluruhnya ke bulan Mulai." | Cacat audit butir 4 dan 5. Turunan rumus Laporan Bulanan D8 (SUMIFS dengan kriteria Pelanggan dan Layanan sama, dan Mulai di antara B3 dan B4+1) |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen yang diminta prompt; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama |
| Tidak diubah | | | B7 dan B8 bukan tanggal efektif. Tanda tangan dan tanggal (C36 sampai D38) tetap kosong. Alur Proses (gambar dan legenda), Daftar, Laporan Bulanan (termasuk B3 dan blok A49, A50), data validation dan format kondisional tidak disentuh |

Hitung ulang LibreOffice atas out.xlsx (konversi xlsx ke xlsx lalu dibaca data_only): Laporan Bulanan B3 sampai B5 = 01-Nov-2026, 30-Nov-2026, 43200; baris 8 sampai 47 kosong; tidak ada sel galat; Parameter SLA dan Downtime Log baris 5 sampai 7 kosong. Render PDF LibreOffice: Kontrol Dokumen B22 satu baris, catatan A2 di Parameter SLA dan Downtime Log terbaca utuh di satu baris, baris yang dikosongkan berwarna sama dengan baris input di bawahnya. Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas 118 sel teks out.xlsx: nol temuan. Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter).

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, pengesahan kosong; "Diperiksa (Head of Operation)" di Laporan Bulanan berbeda dari "ISO/ISMS Coordinator" di Kontrol Dokumen | Pengesahan dokumen diisi tiga penanda tangan dari defaults.json, tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Blok A49 dan A50 di Laporan Bulanan adalah pengesahan laporan bulanan, konteks lain dari pengesahan dokumen, jadi tidak diubah. Open item 1 |
| 2 | Seluruh isi CONTOH; tanggal contoh setelah tanggal draft | Diperbaiki: empat baris contoh dikosongkan (Parameter SLA 5 dan 6, Downtime Log 5 dan 6), legenda B26 dibersihkan. Laporan Bulanan baris 8 sampai 47 kosong lewat rumusnya sendiri |
| 3 | Availability memakai menit kalender penuh, kolom Jam layanan dan Pengecualian kontrak tidak dipakai rumus | Diberi keterangan di Parameter SLA A2. Rumus tidak diubah: legenda sumber menyebut sel rumus "jangan diubah" dan mengubah penyebut adalah perubahan substansi. USULAN 4 |
| 4 | Kombinasi Pelanggan dan Layanan unik tidak ditegakkan; SUMIFS memakai pencocokan teks | Diberi keterangan di Downtime Log A2 (ejaan harus sama). Validasi data tidak ditambah (alat tidak menambah data validation). USULAN 5 |
| 5 | Downtime lintas bulan tidak dipecah | Diberi keterangan di Downtime Log A2. Pemecahan butuh aturan baru, tidak ada di sumber. Open item 5 |
| 6 | Alasan pengecualian tidak divalidasi terhadap Pengecualian kontrak; satu-satunya kontrol adalah format kondisional sel kosong dan Cara pakai butir 2 | Tidak diubah: Cara pakai butir 2 sudah memuat syaratnya dan format kondisional I5:I206 tetap. USULAN 6 |
| 7 | Tiket P1 dan P2 dan Di-ack sesuai target diisi manual; Response SLA hanya rasio J/I tanpa status target | Tidak diubah: Cara pakai butir 4 sudah menyatakan pengisian dari ringkasan SNX-OPS-FRM-08, kalimat tim jelas. Ambang 95% ada di FRM-08, bukan di form ini. USULAN 7 |
| 8 | Gambar menyebut keputusan Breach menuju RCA FRM-10 dan info Commercial, tanpa rumus atau pemicu | Gambar tidak bisa diubah lewat xlsx_patch dan isinya cocok dengan SOP-05 Bagian 6.6 (RCA dengan FRM-10, Commercial menangani konsekuensi kontraktual). Tidak ada kolom untuk mencatat pemberitahuan ke Commercial; kolom "Catatan dan tindakan" (L) yang ada tetap. Open item 2 |
| 9 | Penyebab "Upstream atau supplier" bisa diberi Dihitung = Ya atau Tidak; contoh upstream tetap "Ya" | Tidak diubah: aturan butir 2 (Tidak hanya dengan bukti notifikasi maintenance atau pengecualian kontrak) tetap berlaku; baris contoh hilang bersama clear_rows. Open item 3 |
| 10 | Early warning 50% anggaran (SOP-05 Bagian 6.4) tanpa rumus atau penanda; format kondisional H hanya untuk nilai kurang dari 0 | Tidak diubah: alat tidak mengubah format kondisional dan penanda baru menambah mekanisme. USULAN 3 |
| 11 | Tidak ada kredensial atau data pribadi, hanya placeholder | Dikonfirmasi ulang atas out.xlsx: nama orang hanya di blok Pengesahan dan Disetujui dari defaults.json. Placeholder `[pelanggan A]`, `[pelanggan B]`, `[PIC pelanggan]` hilang bersama baris contoh |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B13 "Klausul atau kontrol Annex A 8.16" | Diganti "Kontrol Annex A 8.16" |
| B | B22 pasif tanpa pelaku | Diganti kalimat perintah (lihat bagian 2) |
| C | Legenda B26 menyuruh menghapus baris CONTOH yang sudah dikosongkan | Diganti kalimat yang benar sesudah patch |
| D | Riwayat revisi punya dua baris Revisi 00 bertanggal sama; baris kedua menyebut RTO | Baris kedua dikosongkan; teks asli dicatat di bagian 2. USULAN 2 |
| E | Laporan Bulanan B3 berisi 01-Nov-2026 (sel input), lebih akhir dari tanggal draft | Tidak diubah: sel input yang dibutuhkan rumus B4 dan B5 (keduanya bergantung pada B3). Open item 4 |

## USULAN

Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Service Delivery Manager, ISO/ISMS Coordinator, COO. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | Owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | Owner |
| 3 | Penanda peringatan dini di Laporan Bulanan: tandai baris bila downtime dihitung melewati 50% anggaran (ambang dari SOP-05, nilai menit tidak ada di sumber). Belum diterapkan | Laporan Bulanan kolom H, format kondisional baru | Fani |
| 4 | Availability memperhitungkan kolom Jam layanan, atau dokumen menyatakan bahwa semua SLA diukur 24x7. Selama belum diputus, Parameter SLA A2 hanya menyatakan perilaku rumus yang ada. Belum diterapkan | Laporan Bulanan kolom D dan E, Parameter SLA kolom E | Fani |
| 5 | Daftar pilihan Pelanggan dan Layanan di Downtime Log yang mengambil dari Parameter SLA, dan pemeriksaan kombinasi unik. Belum diterapkan | Downtime Log kolom B dan C, Parameter SLA kolom B dan C | Fani |
| 6 | Alasan pengecualian dipilih dari kolom Pengecualian kontrak di Parameter SLA, bukan teks bebas. Belum diterapkan | Downtime Log kolom I | Fani |
| 7 | Status Response SLA terhadap ambang; ambang 95% sudah ada di SNX-OPS-FRM-08, angka baru tidak diusulkan. Belum diterapkan | Laporan Bulanan kolom K | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Pemilik dokumen "Service Delivery Manager" (B10), "Disusun (Service Delivery Manager)" dan "Diperiksa (Head of Operation)" (Laporan Bulanan A49 dan A50) belum dipetakan ke jabatan atau orang; peran ini berbeda dari penanda tangan Kontrol Dokumen (Erik, Fani). Matriks peran dan SK penunjukan belum ada | Fani, owner |
| 2 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Isinya tidak salah terhadap SOP-05, tetapi form tidak punya kolom pencatat "info Commercial" dan tidak ada pemicu otomatis dari status Breach ke RCA | Orkestrator, Fani |
| 3 | Penyebab "Upstream atau supplier" (Daftar B3): SOP-05 Bagian 4 mengecualikan "gangguan di luar tanggung jawab SINUX sesuai kontrak". Belum tertulis kapan gangguan upstream dihitung dan kapan dikecualikan; contoh sumber memberi "Ya" | Fani, Legal |
| 4 | Laporan Bulanan B3 (periode, sel input) berisi 01-Nov-2026 dan perlu diisi ulang tiap periode. Bila owner ingin sel kosong, B4 dan B5 perlu penjaga rumus | Fani |
| 5 | Downtime yang melintasi pergantian bulan dihitung seluruhnya di bulan Mulai (rumus sumber); aturan pemecahan belum ada di sumber | Fani |
| 6 | SOP-05 (salinan audit) Bagian 6.2 butir 2 menulis "Zammad untuk Nusagrid, Service Hub untuk GMF dan internal", sedangkan premis owner memberi Zammad untuk Ops dan GLPI untuk generalist. FRM-09 tidak menyebut sistem tiket (hanya kolom "Ref tiket atau CR" dan rujukan ke FRM-08), jadi tidak ada yang diubah di sini; SOP-05, FRM-08, dan form ini harus sama | Owner, lane OPS-SOP-05 dan OPS-FRM-08 |
| 7 | Format xlsx tidak punya bagian Dokumen terkait, tabel rekaman (lokasi, pemilik), ataupun scope. Kode yang dirujuk di sel: SNX-OPS-SOP-05, SNX-OPS-FRM-08; di gambar: FRM-10. Lokasi simpan dan pemilik rekaman tidak ada di sumber; masa simpan 3 tahun dari sumber (sama dengan SOP-05 Bagian 7, salinan audit) | Orkestrator, Fani |
| 8 | Keterbatasan alat: nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka; kotak legenda A26 tetap biru; tinggi baris Kontrol Dokumen tidak bisa diubah. HUMAN-VERDICT: buka di Excel dan lihat apakah baris B22 dan catatan A2 di Parameter SLA dan Downtime Log tidak terpotong; di render LibreOffice semuanya terbaca | Orkestrator, owner |
| 9 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: "Baris CONTOH: hapus atau timpa saat dipakai", "Sel rumus: jangan diubah", Cara pakai butir 1 sampai 5. Satu-satunya yang dijalankan adalah pengosongan baris contoh, karena prompt memerintahkan clear_rows yang sama | Orkestrator |
| 10 | Tanggal draft 13 Oktober 2026 (B7 dan B31) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |

## Asumsi dan tafsir

- "Approval persis" dari prompt mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json. Sebutan COO dan "Direktur (COO)" tidak muncul lagi di dokumen karena satu-satunya penyebutnya (B11 dan B38) diganti.
- Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber maupun di patch; dicek dengan pola lint_doc atas semua sel teks out.xlsx.
- Fakta tentang SOP-05 dan FRM-08 diambil dari salinan audit, tidak dibuka di Drive.
- Penulisan "0.999 = 99.9%" di Parameter SLA A2 memakai titik desimal seperti sumber; kalimat tim dipertahankan.
- Satu-satunya kalimat baru yang berisi isi proses adalah dua catatan A2. Keduanya menyatakan perilaku rumus yang sudah ada, bukan proses baru.

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas 17 entri `set` berisi teks dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Draf awal B22 memuat nama peran panjang yang membuat kalimat dua baris dan terpotong; terdengar seperti kalimat prosedur yang dipaksakan masuk sel | Diganti kalimat perintah satu baris, selaras dengan butir 1 sampai 4 |
| Downtime Log A2 dan Parameter SLA A2 memakai dua klausa dengan titik koma | Dipertahankan: tiap klausa membawa satu fakta berbeda dan tidak ada kelompok tiga yang dipaksakan, tidak ada penutup positif |
| Teks "persis seperti" dan "penuh" di dua catatan A2 bisa terbaca sebagai penekanan | Dipertahankan: "persis" menggambarkan pencocokan teks rumus (ejaan beda berarti tidak cocok) dan "penuh" menggambarkan 1440 menit per hari; tidak ada kata penegas lain |
| Legenda B26 telegrafis | Dipertahankan: kalimat sama dengan form OPS lain, satu fakta |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust) | Tidak ada di nilai patch (pencarian karakter dan lint). Notes ini tidak memakai em-dash atau en-dash |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di prompt dan defaults.json |
| "Kontrol Annex A 8.16" dan "Klausul 9.1.1, 9.1.2, 9.1.3" | Prompt, checklist.json row 76, sel B12 dan B13 sumber |
| "menit kalender penuh", "Jam layanan dan Pengecualian kontrak tidak masuk rumus" | Rumus sumber Laporan Bulanan B5 dan E8; pemindaian rumus (hanya kolom B, C, D Parameter SLA yang dirujuk) |
| "ditulis persis seperti di Parameter SLA", "downtime lintas bulan masuk seluruhnya ke bulan Mulai" | Rumus sumber Laporan Bulanan D8 (SUMIFS dengan kriteria Pelanggan dan Layanan, dan Mulai di antara B3 dan B4+1) |
| "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Kalimat yang sama dipakai di patch FRM-04, FRM-05, FRM-07, FRM-08; warna E7EEF7 dari sel A26 sumber |
| "3 tahun", "RESTRICTED (Internal)", "Service Delivery Manager", "13 Oktober 2026", "hari kerja ke-5" | Sumber FRM-09, tidak diubah |
| Rujukan SOP-05 dan FRM-08 di notes (50%, "gangguan di luar tanggung jawab SINUX sesuai kontrak", 95%) | Salinan audit; hanya di notes, tidak di sel |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.


## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan" (sebutan seluruh workbook).
Butir 4 dan 5 Cara pakai serta Tujuan dipertahankan (T1).

### W10 koreksi worker (07:33Z, temuan pemeriksa buta r1)
- Kontrol Dokumen B19: nilai pilihan ditulis "Tidak" dalam tanda kutip agar tidak terbaca sebagai "tidak hanya".
- Kontrol Dokumen B21: "respon" menjadi "respons" (ejaan baku).
- Tata letak (rubrik d): op format worker (fit_rows sheet data, lebar kolom minimal sesuai kata judul terpanjang, A3 untuk sheet 16 kolom atau lebih).
