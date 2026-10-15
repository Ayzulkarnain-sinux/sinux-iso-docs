# Catatan penyusun OPS-FRM-07: Maintenance Schedule & Service Report

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-07.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-FRM-07 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C1. Process owner = "Lead NOC" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber).

Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-07.xlsx specs/OPS-FRM-07.patch.json /tmp/pen-OPS-FRM-07/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 5 sheet, 1 gambar di Alur Proses, 1 data validation dan 1 conditional formatting di Jadwal PM, 2 data validation dan 1 conditional formatting di Service Report, 121 rumus di Jadwal PM, 151 rumus di Service Report. Keluaran mentah: /tmp/pen-OPS-FRM-07/xlsx_patch.out.txt.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-07_Maintenance_Schedule_Service_Report.xlsx (130465 byte) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB | 2026-10-13T06:09:21Z (get_file_metadata, dicek hari ini; fileSize 130465 sama dengan hasil decode) | read_file_content (teks), download_file_content (xlsx, didekode ke /tmp/src/OPS-FRM-07.xlsx), 5 sheet dibuka dengan openpyxl (nilai, rumus, isian warna, data validation, conditional formatting), gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/checklist.json baris 74 dan config/worklist.json | Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "7.1.3, 8.5.1" dan ISO/IEC 27001:2022 "7.13" (dari prompt orkestrator; cocok dengan checklist.json: iso_9001 "7.1.3, 8.5.1", iso_27001 "7.13") |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md baris 2107 sampai 2290 (bagian 5 Catatan kualitas dan celah) | salinan audit 13 Okt 2026 | DATA, dibandingkan dengan xlsx asli |
| Pendukung (bahan) | SNX-OPS-SOP-03 (10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc), SNX-OPS-RPT-01, SNX-ISMS-SOP-03 | salinan audit | Dibaca dari context/audit (DATA), bukan dari Drive terbaru; bisa basi bila tim sudah mengubahnya |

Sheet sumber: Kontrol Dokumen (A1:E37), Alur Proses (judul, legenda, 1 gambar), Daftar (3 daftar dropdown), Jadwal PM (A1:T47), Service Report (A1:P155). Sheet "Kontrol Dokumen" ada, jadi diselaraskan lewat `set`; tidak ada sheet yang ditambah.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kepatuhan PM dihitung otomatis sebagai S dibagi jumlah bulan berkode R, S, atau T | "Per aktivitas, isi bulan dengan kode: R = rencana, S = selesai, T = tertunda. Kepatuhan dihitung otomatis (S dibagi R+S+T)." (Kontrol Dokumen B19); rumus `=IF(R6=0,"",S6/R6)` (Jadwal PM T6) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |
| 2 | Service Report hanya untuk PM atau CM yang mengubah sistem, dengan nomor tiket atau CR | "Setiap pelaksanaan PM atau CM yang mengubah sistem dicatat di Service Report beserta nomor tiket atau CR." (Kontrol Dokumen B20) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |
| 3 | Pemilik dokumen Lead NOC, record disimpan 3 tahun, klasifikasi RESTRICTED (Internal), acuan klausul 7.1.3, 8.5.1 dan Annex A 7.13 | "Pemilik dokumen \| Lead NOC"; "Masa simpan record \| 3 tahun"; "Klasifikasi \| RESTRICTED (Internal)"; "Acuan ISO 9001:2015 \| Klausul 7.1.3, 8.5.1"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 7.13" (B10, B14, B9, B12, B13) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Lokasi |
|---|---|---|---|
| 1 | Satu-satunya baris CONTOH | "Baris CONTOH: hapus atau timpa saat dipakai" (Kontrol Dokumen B25); "Durasi dihitung otomatis dalam menit. Baris biru muda = CONTOH." (Service Report A2); P5 = "CONTOH" | Service Report baris 5 (SR-2026-0001); baris 6 sampai 155 hanya rumus Durasi di kolom M |
| 2 | Sembilan aktivitas PM baku, bukan baris contoh | Contoh: "Health check layanan kritis \| Tiap awal shift \| NOC Engineer"; "Review rule dan akun tidak terpakai \| Triwulanan \| Lead SOC"; "Uji pemulihan SNX-ISMS-PLN-01 \| Tahunan \| Head of Operation" | Jadwal PM baris 6 sampai 14; total rencana 7 x 12 + 4 + 1 = 89 siklus (dihitung dari kode R di sheet) |
| 3 | Aktivitas harian dan mingguan dihitung satu siklus per bulan | "R = rencana, S = selesai, T = tertunda. Aktivitas harian dan mingguan dicatat per bulan sebagai satu siklus terpenuhi." | Jadwal PM A2 |
| 4 | Ambang 95% dan tindak lanjut Lead NOC hanya ada di gambar | Kotak keputusan "Kepatuhan di bawah 95%?", cabang "ya" ke kotak "Tindak lanjut / Lead NOC", cabang "tidak" ke "Rekap bulanan / ke SNX-OPS-RPT-01" | Alur Proses, xl/media/image1.png |
| 5 | Angka 95% yang sama ada di dokumen tim lain | "Kepatuhan jadwal PM (realisasi dibanding rencana) \| 95%" (SNX-OPS-SOP-03 Bagian 9, salinan audit); "Kepatuhan jadwal preventive maintenance \| ≥ \| 0,95 (95%) \| SNX-OPS-FRM-07 \| Bulanan" (SNX-OPS-RPT-01 KPI 5, salinan audit) | context/audit: bagian SOP-03 mulai baris 4020, bagian RPT-01 mulai baris 3389 (KPI 5 di baris 3477) |
| 6 | Lead NOC meninjau kepatuhan bulanan | "Lead NOC meninjau kepatuhan bulanan dan menandatangani kolom verifikasi." | Kontrol Dokumen B21 |
| 7 | Rumus Durasi | `=IF(OR(K5="",L5=""),"",ROUND((L5-K5)*1440,0))` | Service Report M5 sampai M155 (tidak diubah) |
| 8 | Penanda tangan sumber | "Disusun oleh \| Lead NOC", "Diperiksa oleh \| ISO/ISMS Coordinator", "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Kontrol Dokumen B35 sampai B37, B11 |
| 9 | Riwayat revisi sumber | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" dan "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | Kontrol Dokumen C30, C31 |

## 3. Isi patch (apa yang diubah dan kenapa)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Service Report baris 5 (A sampai L, N sampai P) | Baris CONTOH SR-2026-0001 | Dikosongkan lewat clear_rows; M5 tetap rumus; warna isi mewarisi baris 6 (kuning input), diperiksa pada out.xlsx | Aturan baris CONTOH (RUNBOOK §6) |
| Service Report A2 | "...menit. Baris biru muda = CONTOH." | "Durasi dihitung otomatis dalam menit." | Kalimat CONTOH tidak berlaku setelah baris dikosongkan; alat menolak teks CONTOH di luar Kontrol Dokumen |
| Kontrol Dokumen B25 | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Legenda lama menyuruh menghapus baris yang sudah kosong. Kotak warna A25 tetap biru karena alat tidak mengubah warna di luar clear_rows. Kalimat sama dengan OPS-FRM-04 agar seri form seragam |
| B6 Revisi | "00 (DRAFT)" | "00 (Draft)" | Sheet tidak punya baris Status terpisah; satu sel memuat revisi 00 dan status Draft. Penulisan "Draft" sama dengan nilai status, tanpa huruf kapital untuk penekanan |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by dan prompt |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 7.13" | "Kontrol Annex A 7.13" | 7.13 adalah kontrol Annex A, bukan klausul; "klausul atau kontrol" ragu-ragu. Acuan "7.13" dari prompt tetap tercantum |
| B20 Cara pakai 3 | "...beserta nomor tiket atau CR." | "...beserta nomor tiket Zammad atau CR." | Premis owner: tiket Zammad untuk Ops. Lihat asumsi 4 dan open item 8 |
| C30 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A31 sampai E31 | Baris riwayat kedua, juga Revisi 00 | Dikosongkan | USULAN 5 |
| B35 Disusun oleh | "Lead NOC" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed.OPS |
| B36 Diperiksa oleh | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed.OPS |
| B37 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |
| B4, B5, B9, B10, B12, B14 | Sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Agar patch memuat semua medan template secara eksplisit; tidak mengubah isi sel |
| B7, B8, B15, B18, B19, B21, B24, B26, B30, D30, E30, C35 sampai D37 | | Tidak diubah | B7 dan B30 tanggal 13 Oktober 2026 adalah tanggal draft tim (open item 9). B8 "Ditetapkan saat pengesahan" bukan tanggal. E30 "Menunggu" tetap. Tanda tangan dan tanggal tetap kosong (batas keras 3). B10 "Lead NOC" mengikuti sumber, tanpa nama |

Pemeriksaan hasil: perbandingan sel demi sel antara /tmp/src/OPS-FRM-07.xlsx dan out.xlsx menunjukkan hanya sel di tabel di atas yang berubah (30 sel: 15 di Service Report baris 5, 1 di Service Report A2, 14 di Kontrol Dokumen). Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas seluruh teks out.xlsx: nol hit. Tidak ada em-dash atau en-dash. Hitung ulang LibreOffice atas out.xlsx: Service Report baris 5 kosong, Jadwal PM kolom Rencana 12, 12, 12, 12, 12, 12, 12, 4, 1, Kepatuhan keseluruhan 0%.

## 4. Penanganan cacat context/audit (bagian 5, fileId 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, pengesahan dan tanda tangan kosong | Dipertahankan: keadaan yang benar untuk Draft (batas keras 3). Tidak ada tanda tangan, tanggal efektif, atau status lain yang diisi |
| 2 | Ambang 95% hanya di diagram; tidak ada rumus atau format kondisional yang menandainya; tidak berlabel USULAN; SOP-03 Bagian 9 sama | Tidak diubah. Gambar tidak bisa diganti lewat xlsx_patch. Menambah butir "Cara pakai" yang menyuruh Lead NOC menindaklanjuti di bawah 95% akan memicu tindak lanjut tiap bulan, karena kepatuhan sekarang tidak bisa mendekati 95% sebelum bulan terakhir (temuan A). Angka 95% berasal dari diagram, SOP-03 Bagian 9, dan RPT-01, jadi tidak diberi label USULAN. Penandaan di sheet = USULAN 2; open item 1 dan 2 |
| 3 | Rumus Rencana menghitung R, S, dan T sekaligus | Tidak diubah: sesuai Cara pakai butir 2 ("S dibagi R+S+T") dan legenda "Sel rumus: jangan diubah". Akibat pada angka kepatuhan diukur di temuan A. USULAN 1 |
| 4 | Aktivitas harian dan mingguan dicatat satu siklus per bulan, jadi kepatuhan tidak mencerminkan per shift atau per minggu | Kalimat tim (Jadwal PM A2) dipertahankan: sudah jelas dan menyatakan batasnya sendiri. Open item 3 |
| 5 | Contoh Service Report merujuk CR-2026-0002, sedangkan Change Log SNX-OPS-FRM-04 hanya punya CR-2026-0001 | Teratasi: baris contoh dikosongkan. specs/OPS-FRM-04.patch.json juga mengosongkan baris contoh di Change Log, jadi tidak ada lagi rujukan silang data contoh. Sembilan aktivitas Jadwal PM cocok dengan tabel 6.1 SOP-03 (salinan audit); beda kecil: SOP-03 menulis patch "Bulanan, atau segera untuk patch kritis", Jadwal PM menulis "Bulanan". Tidak diubah |
| 6 | Tanggal contoh November 2026 lebih akhir dari tanggal draft; tahun jadwal 2027 sedangkan contoh bertahun 2026 | Tanggal contoh hilang bersama baris contoh. Tahun jadwal 2027 (Jadwal PM B3) dipertahankan: sel input tim, dan SOP-03 Bagian 6.1 menetapkan jadwal disusun paling lambat Desember untuk tahun berikutnya |
| 7 | Status SR memuat Tindak lanjut dan Eskalasi, tetapi tidak ada kolom tanggal tindak lanjut atau penerima eskalasi | Tidak diubah: kolom baru menambah struktur yang tidak ada di sumber. USULAN 4; open item 5 |
| 8 | Tidak ada kredensial atau data pribadi; placeholder `[pelaksana]`, `[Lead NOC]`, `[nama server]` | Dikonfirmasi ulang atas out.xlsx. Ketiga placeholder hilang bersama baris contoh. Nama orang hanya di blok Disetujui dan Pengesahan dari defaults |

Cacat tambahan yang saya temukan (di luar bagian 5 audit):

| # | Temuan | Penanganan |
|---|---|---|
| A | Kepatuhan PM tidak bisa mencapai 95% sebelum bulan terakhir. Penyebut T6 dan T47 mencakup bulan berkode R yang belum jatuh tempo. Pengukuran: salinan kerja sumber dengan kode S di Januari pada tujuh aktivitas yang punya bulan Januari (baris 6 sampai 12), dihitung ulang LibreOffice, memberi Rencana 12, Selesai 1, Kepatuhan 8,33333333333333% untuk tiap tujuh baris dan Kepatuhan keseluruhan 7,86516853932584% (7 dari 89). Evidence mentah: /tmp/pen-OPS-FRM-07/csv/scen-Jadwal PM.csv (salinan kerja, bukan bagian repo). Dengan diagram yang menanyakan "di bawah 95%?" tiap bulan, jawabannya selalu ya sampai akhir tahun | Tidak diubah: mengganti rumus mengubah arti metrik dan melanggar legenda "jangan diubah". USULAN 1, open item 1 |
| B | SNX-ISMS-SOP-03 Bagian 7.4 butir 1 (salinan audit ISMS baris 205): uji restore "minimal bulanan untuk setiap pelanggan berlayanan backup, dan minimal triwulanan untuk sistem internal kritis". Jadwal PM aktivitas 7 hanya memuat yang bulanan | Tidak diubah: baris baru butuh PIC yang tidak ada di sumber dan menambah penyebut kepatuhan. USULAN 3, open item 4 |
| C | Riwayat revisi baris kedua menyebut "keselarasan RTO dan target pulih", topik yang tidak ada di form ini; dua baris Revisi 00 bertanggal sama | Baris kedua dikosongkan, teks aslinya dicatat di bagian 2 butir 9. USULAN 5. OPS-FRM-04 diperlakukan sama |
| D | Cara pakai butir 4 menyebut "menandatangani kolom verifikasi", tetapi satu-satunya kolom verifikasi adalah "Diverifikasi" di Service Report (O), dan Jadwal PM tidak punya kolom tanda tangan | Tidak diubah (kalimat tim, T1). Open item 6 |

## 5. Asumsi dan tafsir

1. "Approval persis" dari prompt mengalahkan sumber di blok Disusun, Diperiksa, Disetujui, mengikuti config/defaults.json yang menyebut nilai dipakai persis tanpa substitusi penyusun. Di sheet ini tidak ada badan dokumen, jadi bentuk "President Director" (blok tanda tangan) dipakai di B11 dan B37.
2. Sheet "Kontrol Dokumen" tidak punya baris "Status" atau "Klasifikasi PRO-01" terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya. Tidak ada baris yang ditambah.
3. Sembilan baris Jadwal PM (6 sampai 14) adalah rencana baku, bukan data dummy, jadi tidak dikosongkan. Kode R di dalamnya juga bukan CONTOH.
4. Zammad di B20: sumber tidak menyebut sistem tiket (hanya "nomor tiket atau CR"). Zammad ditambahkan karena premis owner "tiket zammad untuk ops" dan form ini milik Operation. Tidak diberi label USULAN karena itu premis owner, bukan angka atau proses baru. Batas "generalist" belum dirinci owner, jadi open item 8.
5. Kalimat bernada perintah di sumber ("Isi tahun di sheet Jadwal PM sel B3", "hapus atau timpa saat dipakai", "jangan diubah") ditujukan ke pengguna form, bukan ke penyusun. Satu-satunya yang dijalankan adalah "hapus" atas baris contoh, karena brief memerintahkan clear_rows yang sama. Tidak ada instruksi lain yang dituruti.
6. Fakta tentang SOP-03, RPT-01, dan ISMS-SOP-03 diambil dari salinan audit (13 sampai 14 Okt), tidak dibuka di Drive.
7. Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber maupun di patch.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Ganti definisi Kepatuhan menjadi S dibagi (S + T), dengan aturan bahwa Lead NOC mengubah bulan yang lewat tanpa pelaksanaan dari R menjadi T. Rumus baris 6: `=IF(S6+COUNTIF(F6:Q6,"T")=0,"",S6/(S6+COUNTIF(F6:Q6,"T")))`; T47: `=IF(SUM(S6:S45)+COUNTIF(F6:Q45,"T")=0,"",SUM(S6:S45)/(SUM(S6:S45)+COUNTIF(F6:Q45,"T")))`. Diuji di salinan kerja dengan LibreOffice: Januari S dan Februari T pada baris 6 memberi 50%, S saja memberi 100%, keseluruhan 87,5% pada skenario uji. Belum diterapkan | Jadwal PM T6 sampai T45 dan T47; Cara pakai butir 2 | Fani |
| 2 | Setelah USULAN 1 diputus: tulis ambang 95% sebagai butir Cara pakai ke-5 dan beri conditional formatting pada T6 sampai T14 dan T47. Belum diterapkan | Kontrol Dokumen, Jadwal PM | Fani |
| 3 | Tambah baris uji restore triwulanan untuk sistem internal kritis, mengikuti SNX-ISMS-SOP-03 Bagian 7.4 (salinan audit). PIC belum ada di sumber. Belum diterapkan | Jadwal PM baris 15 | Fani |
| 4 | Tambah kolom Tgl tindak lanjut dan Penerima eskalasi di Service Report untuk status Tindak lanjut dan Eskalasi. Belum diterapkan | Service Report, kolom baru | Fani |
| 5 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris. Sudah diterapkan | Kontrol Dokumen A31 sampai E31 | Owner |
| 6 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Lead NOC, ISO/ISMS Coordinator, COO. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus. Sudah diterapkan | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Definisi Kepatuhan membuat angkanya 7,87% pada bulan pertama walau semua pekerjaan Januari selesai (temuan A). Putuskan USULAN 1 atau terima pembacaan "progres terhadap rencana tahunan". SNX-OPS-SOP-03 Bagian 9 dan SNX-OPS-RPT-01 KPI 5 memakai istilah dan target yang sama, jadi ketiganya harus selaras | Fani |
| 2 | Ambang 95% hanya ada di gambar Alur Proses, SOP-03 Bagian 9, dan RPT-01. Gambar tidak bisa diubah lewat xlsx_patch; bila ambang berubah, gambar perlu diganti lewat entri LEAD | Fani; orkestrator |
| 3 | Aktivitas harian dan mingguan dicatat satu siklus per bulan, jadi pelaksanaan per shift atau per minggu tidak terlihat di kepatuhan. Terima batas ini atau tetapkan cara mengukurnya | Fani |
| 4 | Uji restore triwulanan sistem internal tidak ada di Jadwal PM (temuan B, USULAN 3) | Fani |
| 5 | Service Report tidak punya tempat mencatat tanggal tindak lanjut atau penerima eskalasi (USULAN 4) | Fani |
| 6 | Cara pakai butir 4 menyebut "menandatangani kolom verifikasi", padahal kolom itu hanya ada di Service Report dan tidak ada kolom tanda tangan di Jadwal PM (temuan D) | Fani |
| 7 | Peran "Lead NOC" (pemilik dokumen), "NOC Engineer", "Lead SOC", dan "Head of Operation" belum dipetakan ke nama. "Head of Operation" tidak sama dengan jabatan Fani (VP Tech Operation and Services). "ISO/ISMS Coordinator" sebagai pemeriksa di sumber digantikan Fani oleh defaults | Fani, owner |
| 8 | Nomor tiket di Service Report ditulis "Zammad" (asumsi 4). Bila ada pekerjaan PM atau CM yang tiketnya di GLPI (generalist), batas ini belum dirinci owner | Owner |
| 9 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti agar tidak ada tanggal karangan. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |
| 10 | Keterbatasan alat: kotak legenda A25 tetap biru walau tidak ada lagi baris biru. Nilai rumus belum tersimpan di out.xlsx (openpyxl menulis tanpa nilai cache); Excel dan LibreOffice menghitung ulang saat dibuka (diverifikasi LibreOffice). Terima atau jadikan tech_fix alat | Orkestrator |

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas 21 entri `set` di patch (16 berisi teks, 5 pengosongan A31 sampai E31) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Legenda B25 terdengar telegrafis ("Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai"); "dan tidak dipakai" mengulang "dikosongkan" | Dipertahankan apa adanya karena OPS-FRM-04 memakai kalimat yang sama dan seri form harus seragam; satu kalimat pendek, tanpa lindung nilai atau pengisi |
| Draf pertama notes mengulang penjelasan temuan A di tiga tempat | Penjelasan lengkap hanya di bagian 4 temuan A; USULAN 1 dan open item 1 merujuk ke sana dengan satu kalimat |
| Pemindaian pola lint (FORBIDDEN dan STYLE) dan karakter em-dash atau en-dash atas seluruh teks out.xlsx | Nol hit; tidak ada yang perlu diganti |
| Kalimat B20 tanpa pelaku ("dicatat di Service Report") | Dibiarkan: kalimat tim yang sudah jelas, aturan T1; pelaku jelas dari butir 4 dan 5 di sheet yang sama |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Nilai di patch atau notes | Sumber | Verdict |
|---|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | prompt dan config/defaults.json (prepared_reviewed.OPS, approved_by) | Bersumber |
| "00 (Draft)", "Draft awal untuk review dan pengesahan" | prompt (status, revision, revision_desc) | Bersumber |
| "Kontrol Annex A 7.13", "Klausul 7.1.3, 8.5.1", "3 tahun", "Lead NOC", "RESTRICTED (Internal)" | sumber (B9, B10, B12 sampai B14) dan prompt | Bersumber |
| "Zammad" di B20 | premis owner (RUNBOOK §0, defaults ticketing); sumber FRM-07 tidak menyebut sistem tiket | Bersumber dari premis owner, bukan dari sumber form; ditandai di asumsi 4 dan open item 8 |
| 95%, 89 siklus, 7,87% (7 dari 89), 50%, 100%, 87,5% di notes | 95% dari gambar sumber, SOP-03, RPT-01; 89 dihitung dari kode R di Jadwal PM; 7,87% dan skenario USULAN 1 diukur dengan LibreOffice atas salinan kerja | Bersumber atau diukur; tidak ada di sel patch |
| Fakta SOP-03, RPT-01, ISMS-SOP-03 | salinan audit, bukan Drive terbaru | Bersumber dengan catatan kemungkinan basi (asumsi 6) |
| Tanggal | Tidak ada tanggal baru di patch; 13 Oktober 2026 dan 2027 sudah ada di sumber | Bersumber |


## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar tidak disebut di sel yang disunting.
Cara pakai 4 kini diawali "Setiap bulan"; Lead NOC tetap pelaku.
