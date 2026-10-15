# Catatan penyusun OPS-FRM-04: Change Request & Approval Log

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-04.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-FRM-04 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber, audit_class C1. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-04.xlsx specs/OPS-FRM-04.patch.json /tmp/pen-OPS-FRM-04/out.xlsx` memberi `"pass": true`, `"fails": []`, fitur sebelum dan sesudah sama (5 sheet, 1 gambar di Alur Proses, 4 data validation dan 2 aturan conditional formatting di Change Log, 302 rumus di Change Log, 31 rumus di Ringkasan).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-04_Change_Request_Approval_Log.xlsx (155160 byte) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ | 2026-10-13T06:09:17Z (get_file_metadata, dicek ulang; fileSize 155160 sama dengan hasil decode) | read_file_content (teks), download_file_content (didekode ke /tmp/src/OPS-FRM-04.xlsx, python3 -I + openpyxl atas 5 sheet; gambar xl/media/image1.png dibuka) |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris OPS-FRM-04 | checklist modifiedTime tidak diukur ulang di sesi ini | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan klausul ISO 9001:2015 "8.5.6" dan ISO/IEC 27001:2022 "8.32" (dari prompt orkestrator, cocok dengan entri checklist.json row 71: iso_9001 "8.5.6", iso_27001 "8.32") |
| Pendukung (bahan) | SNX-OPS-SOP-02 (15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63) dan tabel KPI Ops | salinan audit 13 sampai 14 Okt | Dibaca dari context/audit (DATA), bukan dari Drive terbaru; kutipan SOP-02 di bawah bisa basi bila tim sudah mengubahnya |

Sheet sumber: Kontrol Dokumen (A1:E37), Alur Proses (judul, legenda, 1 gambar), Daftar (4 daftar dropdown), Change Log (A1:U155), Ringkasan (A1:F13).

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini adalah rekap audit untuk semua change request; CR juga dibuat sebagai tiket di sistem lain | "Satu nomor CR per perubahan: CR-YYYY-NNNN. CR juga dibuat di Service Hub; log ini menjadi rekap audit." (Kontrol Dokumen B18) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |
| 2 | Go-gate dan PIR dihitung otomatis; PIR ditinjau dalam 5 hari kerja | "Kolom Go-gate otomatis CEK bila backup, rollback, atau approval belum lengkap (kecuali Emergency)." dan "Kolom PIR otomatis Ya untuk change Major atau yang berakhir rollback; tinjau dalam 5 hari kerja." (B19, B20) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |
| 3 | Masa simpan 3 tahun, klasifikasi RESTRICTED (Internal), pemilik dokumen Head of Operation, acuan ISO 8.5.6 dan 8.32 | "Masa simpan record \| 3 tahun"; "Klasifikasi \| RESTRICTED (Internal)"; "Pemilik dokumen \| Head of Operation"; "Acuan ISO 9001:2015 \| Klausul 8.5.6"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 8.32" (B14, B9, B10, B12, B13) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Baris CONTOH satu-satunya | "Baris CONTOH: hapus atau timpa saat dipakai" (Kontrol Dokumen B25); "Approver sesuai SNX-OPS-SOP-02 Bagian 5. Baris biru muda = CONTOH." (Change Log A2); U5 = "CONTOH" | Change Log baris 5 (CR-2026-0001); baris 6 sampai 155 hanya rumus S dan T |
| Penanda tangan sumber | "Disusun oleh \| Head of Operation", "Diperiksa oleh \| ISO/ISMS Coordinator", "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Kontrol Dokumen B35 sampai B37, B11 |
| Riwayat revisi sumber | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" dan "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | Kontrol Dokumen C30, C31 |
| Rumus Go-gate | `=IF(A5="","",IF(F5="Emergency","Emergency",IF(AND(I5<>"",J5<>"",L5="Disetujui"),"OK","CEK")))` | Change Log S5 sampai S155 (tidak diubah) |
| Rumus persentase | `=IF(B7=0,"",1-D7/B7)` | Ringkasan F7 sampai F12 (tidak diubah) |
| SOP-02 mensyaratkan ack pelanggan | "Approval tertulis dari approver yang berwenang plus ack pelanggan bila menyentuh layanan pelanggan." | SOP-02 sumber, Bagian 4 butir 1 (salinan audit) |

## 2. Isi patch (apa yang diubah dan kenapa)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Change Log baris 5 (A sampai R, U) | Baris CONTOH CR-2026-0001 | Dikosongkan lewat clear_rows; rumus S5 dan T5 tetap | Aturan baris CONTOH (RUNBOOK §6, WO) |
| Change Log A2 | "...Bagian 5. Baris biru muda = CONTOH." | "Approver sesuai SNX-OPS-SOP-02 Bagian 5." | Kalimat CONTOH tidak berlaku sesudah baris dikosongkan; alat menolak teks CONTOH di luar Kontrol Dokumen |
| Kontrol Dokumen B25 | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Legenda lama menyuruh menghapus baris yang sudah kosong. Kotak warna A25 tetap biru karena alat tidak mengubah warna sel di luar clear_rows |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by (D2) |
| B35 Disusun oleh | "Head of Operation" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed.OPS |
| B36 Diperiksa oleh | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed.OPS |
| B37 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 8.32" | "Kontrol Annex A 8.32" | 8.32 adalah kontrol Annex A, bukan klausul; "klausul atau kontrol" ragu-ragu |
| B12 Acuan ISO 9001:2015 | "Klausul 8.5.6" | Tidak diubah | Sudah memuat "8.5.6" |
| B18 Cara pakai 1 | "CR juga dibuat di Service Hub" | "CR juga dibuat sebagai tiket di Zammad (USULAN)" | Owner 14 Okt: Zammad untuk Ops. Lihat USULAN 1 |
| C30 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A31 sampai E31 | Baris riwayat kedua, juga Revisi 00 | Dikosongkan | Lihat USULAN 4 |
| B6, B7, B8, B9, B10, B14, B15, B19 sampai B21, B26, E30 | | Tidak diubah | B6 "00 (DRAFT)" memuat revisi 00 dan status Draft (sheet tidak punya baris Status). B7 dan B30 tanggal 13 Oktober 2026 adalah tanggal draft tim. B8 "Ditetapkan saat pengesahan" bukan tanggal. E30 "Menunggu" tetap. Tanda tangan dan tanggal di C35 sampai D37 tetap kosong. B9 mengikuti label sumber. B10 mengikuti "Pemilik dokumen" sumber, tanpa nama |

Tidak ada em-dash atau en-dash di nilai `set` (dicek dengan pencarian karakter pada out.xlsx).

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status 00 (DRAFT), kolom Disetujui "Menunggu", tanda tangan kosong, tanggal efektif "Ditetapkan saat pengesahan" | Dipertahankan: memang keadaan yang benar untuk Draft (batas keras 3). Tidak ada yang diisi |
| 2 | Satu baris CONTOH dengan placeholder dan tanggal November 2026 yang lebih akhir dari tanggal draft | Diperbaiki: baris 5 dikosongkan (clear_rows), A2 dan legenda B25 dibersihkan. Periode default Ringkasan B3 dan B4 (1 sampai 30 Nov 2026) dibiarkan: itu sel input, bukan data contoh. Sesudah baris dikosongkan, hitung ulang LibreOffice atas out.xlsx memberi Ringkasan semua nol dan B13 = 0 |
| 3 | Baris contoh ikut terhitung di Ringkasan (Total 1) | Teratasi oleh butir 2 |
| 4 | Label F Ringkasan "Tanpa rollback darurat (%)" tapi rumus `1-D/B` untuk semua jenis | Tidak diubah: nama itu juga tertulis sebagai KPI "Change tanpa rollback darurat" di SOP-02 dan tabel KPI Ops. Mengganti label hanya di form ini membuat tiga dokumen tidak sama. Open item 2, USULAN 6 |
| 5 | Jumlah (B) menghitung semua hasil, C+D+E bisa lebih kecil karena Dibatalkan atau Hasil kosong | Tidak diubah. Memperbaikinya butuh kolom atau rumus baru. Open item 4 |
| 6 | Approver per jenis tidak ada di form; A2 menunjuk SOP-02 Bagian 5 | Dipertahankan: SOP-02 sumber Bagian 5 memang memuat kolom Approver untuk lima jenis yang sama dengan Daftar. Penomoran bisa bergeser setelah SOP-02 dirender ke 11 bagian template. Open item 6 |
| 7 | Go-gate tidak memeriksa Ack pelanggan | Tidak diubah: menambah syarat ke rumus adalah keputusan kontrol, dan legenda sumber menyebut sel rumus "jangan diubah". Rumus usulan di USULAN 5. Open item 1 |
| 8 | Rumus PIR tidak menghitung batas 5 hari kerja; tidak ada kolom tanggal atau status PIR | Tidak diubah: kolom baru menambah struktur yang tidak ada di sumber. USULAN 7, open item 5 |
| 9 | Tidak ada kredensial atau data pribadi sensitif | Dikonfirmasi ulang atas out.xlsx: nama orang hanya di blok Disetujui dan Pengesahan dari defaults |

Cacat tambahan yang saya temukan (di luar bagian 5 audit):

| # | Temuan | Penanganan |
|---|---|---|
| A | Ringkasan A13 berbunyi "CR dieksekusi tanpa go-gate lengkap (status CEK)", tetapi B13 menghitung semua CR berstatus CEK pada periode, termasuk yang masih Menunggu approval dan belum dieksekusi | Tidak diubah. Dua jalan: ganti label menjadi "CR berstatus Go-gate CEK" atau tambahkan syarat Hasil terisi di rumus B13. Keduanya mengubah arti metrik. Open item 3 |
| B | Riwayat revisi punya dua baris Revisi 00 bertanggal sama; baris kedua menyebut "keselarasan RTO dan target pulih", topik yang tidak ada di form ini | Baris kedua dikosongkan dan teks aslinya dicatat di sini. USULAN 4 |
| C | Diagram di sheet Alur Proses: cabang "Ditolak atau revisi" tidak punya panah lanjutan; di SOP-02 sumber cabang yang sama kembali ke pengaju | Tidak bisa diperbaiki lewat xlsx_patch (gambar tetap). Open item 8 |
| D | Judul sheet Change Log "Change request and approval log" tidak sama persis dengan judul form "Change Request & Approval Log" | Tidak diubah (kalimat tim jelas, T1). Tidak masuk open item |

## 4. Asumsi dan tafsir

- "Approval persis" dari prompt mengalahkan sumber di blok Disusun, Diperiksa, Disetujui, mengikuti defaults.json (D2) yang menyebut nilai dipakai persis tanpa substitusi penyusun.
- Sheet "Kontrol Dokumen" tidak punya baris "Status" atau "Klasifikasi PRO-01" terpisah; B6 "00 (DRAFT)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber FRM-04 maupun di patch; dicari dengan pola atas patch dan seluruh teks out.xlsx. Rujukan semacam itu hanya ada di salinan audit SOP-02 dan tidak dibawa.
- Kalimat bernada perintah di sumber: "Isi periode di B3 dan B4", "hapus atau timpa saat dipakai", "jangan diubah", "Ganti..." ditujukan ke pengguna form, bukan ke penyusun. Satu-satunya yang dijalankan adalah "hapus atau timpa" atas baris contoh, karena brief memerintahkan clear_rows yang sama. Tidak ada instruksi lain yang dituruti.
- Fakta tentang SOP-02 diambil dari salinan audit, tidak dibuka di Drive.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | CR dibuat sebagai tiket di Zammad (bukan Service Hub/GLPI) karena CR adalah pekerjaan Ops. Sumber menulis Service Hub, ditulis sebelum keputusan owner 14 Okt. Batas "generalist" belum dirinci owner | Kontrol Dokumen B18, berlabel (USULAN) di sel | Owner, dengan Fani |
| 2 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, COO. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 3 | Pemilik dokumen tetap "Head of Operation" sesuai sumber. Peran ini tidak sama dengan jabatan Fani (VP Tech Operation and Services); pemetaan peran ke orang belum diputus | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Go-gate memeriksa Ack pelanggan. Rumus: `=IF(A5="","",IF(F5="Emergency","Emergency",IF(AND(I5<>"",J5<>"",L5="Disetujui",OR(N5="Ya",N5="Tidak perlu")),"OK","CEK")))`, diterapkan ke S5 sampai S155 | Change Log kolom S (belum diterapkan) | Fani |
| 6 | Samakan label dan rumus persentase: ganti F6 menjadi "Tanpa rollback (%)" bersama KPI di SOP-02 dan tabel KPI Ops, atau batasi rumus ke jenis Emergency. Samakan juga A13 dengan B13 (temuan A) | Ringkasan F6, A13, B13 (belum diterapkan) | Fani |
| 7 | Tambah kolom Tgl PIR dan Status PIR agar batas 5 hari kerja bisa diukur | Change Log (belum diterapkan) | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Go-gate OK tidak berarti Ack pelanggan sudah ada, padahal SOP-02 sumber mensyaratkannya bila menyentuh layanan pelanggan. Putuskan rumus USULAN 5 atau terima celah | Fani |
| 2 | Label "Tanpa rollback darurat (%)" tidak sepadan dengan rumus; nama yang sama dipakai sebagai KPI di SOP-02 dan tabel KPI Ops. Selaraskan ketiganya serentak (USULAN 6) | Fani |
| 3 | Ringkasan A13 vs B13 (temuan A di bagian 3) | Fani |
| 4 | Jumlah vs Berhasil+Rollback+Gagal: CR berhasil Dibatalkan atau tanpa Hasil hanya masuk Jumlah | Fani |
| 5 | Tidak ada kolom tanggal atau status PIR (USULAN 7) | Fani |
| 6 | A2 menunjuk "SNX-OPS-SOP-02 Bagian 5". Cocokkan nomor bagian dan isi kolom Approver setelah SOP-02 selesai dirender; SOP-02 dan FRM-04 harus sama soal sistem tiket (Zammad atau Service Hub) | Orkestrator (lane OPS-SOP-02) |
| 7 | Peran "Head of Operation" sebagai pemilik dokumen dan "ISO/ISMS Coordinator" sebagai pemeriksa di sumber belum dipetakan ke orang; Fani dipakai sebagai pemeriksa karena defaults | Fani, owner |
| 8 | Gambar di Alur Proses tidak bisa diubah lewat xlsx_patch; cabang "Ditolak atau revisi" tanpa lanjutan tetap ada di diagram (ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah) | Orkestrator (butuh entri LEAD bila gambar harus diganti) |
| 9 | Keterbatasan alat: clear_rows menghapus warna isi baris 5, sehingga A5 sampai R5 dan U5 tanpa warna sedangkan baris 6 sampai 155 berwarna kuning input. Kotak legenda A25 tetap biru. Nilai rumus belum tersimpan di out.xlsx (openpyxl); Excel dan LibreOffice menghitung ulang saat dibuka (diverifikasi LibreOffice: Ringkasan nol). Putuskan terima atau tech_fix alat | Orkestrator |
| 10 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti agar tidak ada tanggal karangan. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas 14 entri `set` di patch (9 berisi teks, 5 pengosongan A31 sampai E31) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Label "(USULAN)" di sel B18 bisa terbaca sebagai catatan penyusun di dokumen resmi | Dipertahankan: RUNBOOK §0 butir 4 mewajibkan label untuk hal tanpa sumber; alasannya ada di USULAN 1 |
| Legenda B25 terdengar telegrafis ("Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai") | Dipertahankan: satu kalimat pendek yang menjelaskan kotak biru yang tetap ada; tidak ada lindung nilai atau pengisi |
| Notes mengulang alasan Ack, label, dan baris riwayat di bagian 3, USULAN, dan open items | Dibiarkan karena tiga judul itu wajib berdiri sendiri; xlsx tidak terpengaruh |
| Em-dash, en-dash, tebal di dalam sel, kelompok tiga paksaan, penutup positif | Tidak ada di nilai patch (pencarian karakter atas out.xlsx dan baca ulang). Notes ini tidak memakai em-dash atau en-dash (dicek dengan pola) |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt orkestrator |
| "Draft awal untuk review dan pengesahan" | revision_desc di prompt dan defaults.json |
| "8.5.6" dan "8.32" | Prompt orkestrator, checklist.json baris 854 dan 855, dan sel B12, B13 sumber |
| "Zammad" untuk tiket CR | Owner 14 Okt di defaults.json ("sistem tiket zammad untuk ops, glpi untuk generalist"); penerapan ke CR adalah tafsir, berlabel USULAN |
| "3 tahun", "5 hari kerja", "RESTRICTED (Internal)", "Head of Operation", "13 Oktober 2026" | Sumber FRM-04, tidak diubah |
| Rumus usulan di USULAN 5 | Turunan rumus sumber S5 ditambah syarat kolom N; berlabel USULAN, belum diterapkan |
| Pernyataan isi SOP-02 (Bagian 4 butir 1, Bagian 5) | Salinan audit context/audit, bukan Drive terbaru; ditandai di bagian 1 |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.

## ISO-W9

Spec dan patch tidak diubah di putaran ini (G-3 A9).

| Butir | Sebelum | Sesudah |
|---|---|---|
| Open item gambar Alur Proses | Terbuka, menunggu gambar baru lewat LEAD | Status diubah; teks open item lama tetap |

Open item yang ditutup atau diubah:

- Open item 8 (gambar Alur Proses: cabang Ditolak atau revisi tanpa lanjutan): ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan" (kolom Pelanggan / layanan dan Ack pelanggan; header tidak disunting).
Cara pakai 1: label (USULAN) dipindah ke akhir butir; arti tetap (CR sebagai ticket Zammad masih usulan).
Cara pakai 3: "tinjau dalam 5 hari kerja" menjadi "Lakukan PIR dalam 5 hari kerja"; PIR adalah review pasca-implementasi itu sendiri.
