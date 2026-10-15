# Catatan penyusun OPS-FRM-05: Testing / UAT & Quality Verification Records

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-05.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-FRM-05 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber, audit_class B. Process owner = "Project Manager" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-05.xlsx specs/OPS-FRM-05.patch.json /tmp/pen-OPS-FRM-05/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 7 sheet, 1 gambar (Alur Proses), 2 data validation di Kasus Uji, 2 di Defect, 1 aturan conditional formatting di Kasus Uji, 1 di Ringkasan dan Persetujuan, 8 rumus di Ringkasan dan Persetujuan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-05_Testing_UAT_Quality_Verification.xlsx (135427 byte) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs | 2026-10-13T06:09:19Z (get_file_metadata, dicek ulang di sesi ini; fileSize 135427 sama dengan hasil decode) | read_file_content (teks), download_file_content (exportMimeType tidak dipakai karena berkas sudah xlsx; didekode ke /tmp/src/OPS-FRM-05.xlsx), 7 sheet dibuka dengan python3 -I + openpyxl (nilai, rumus, warna isian, data validation, conditional formatting), gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris OPS-FRM-05 | Kolom Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.6, 8.7" dan ISO/IEC 27001:2022 "8.29" (cocok dengan checklist.json: iso_9001 "8.6, 8.7", iso_27001 "8.29") |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, berkas ops/SNX-OPS-FRM-05.md mulai baris 1659, bagian 5 Catatan kualitas dan celah baris 1845 sampai 1854 | Salinan audit 13 sampai 14 Okt 2026 | DATA, dibandingkan dengan xlsx asli sel per sel |
| Pendukung | Audit SNX-OPS-FRM-06 (baris 1884) dan FRM-01 (baris 883) di berkas audit yang sama | Salinan audit, bukan Drive terbaru | Dipakai hanya untuk lintas dokumen di open items 6 dan 7; bisa basi bila tim sudah mengubahnya |

Sheet sumber: Kontrol Dokumen (A1:E37), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:D8, nilai dropdown), Rencana Uji (A1:B11), Kasus Uji (A1:K87), Defect (A1:I45), Ringkasan dan Persetujuan (A1:D18). Sheet "Kontrol Dokumen" ada, jadi diselaraskan lewat `set`; tidak ada sheet yang ditambah.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini merekam rencana uji, kasus uji, defect, dan persetujuan UAT, dan menjadi dasar BAST pada gate G2 | "Merekam rencana uji, eksekusi kasus uji, defect, dan persetujuan UAT sebagai dasar BAST (gate G2)." (Kontrol Dokumen B15) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |
| 2 | Rekomendasi UAT dihitung otomatis dari tiga angka (defect berat, kasus Belum, kasus Gagal); petunjuk sumber hanya menyebut defect berat | `=IF(B3=0,"",IF(AND(B9=0,B7=0,B5=0),"SIAP UAT DITANDATANGANI","BELUM SIAP"))` (Ringkasan dan Persetujuan B10) dan "Sheet Ringkasan dan Persetujuan menghitung tingkat kelulusan; UAT ditandatangani bila tidak ada defect Kritis atau Tinggi terbuka." (Kontrol Dokumen B21) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |
| 3 | Pemilik dokumen adalah peran Project Manager; klasifikasi RESTRICTED (Internal); masa simpan durasi kontrak ditambah 3 tahun | "Pemilik dokumen" / "Project Manager" (A10, B10); "Klasifikasi" / "RESTRICTED (Internal)" (A9, B9); "Masa simpan record" / "Durasi kontrak + 3 tahun" (A14, B14) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Isi Kasus Uji dan Defect adalah data contoh | "Baris biru muda = CONTOH." (Kasus Uji A2); "Baris CONTOH: hapus atau timpa saat dipakai" (Kontrol Dokumen B25) | Kasus Uji baris 5 sampai 7 (TC-001 sampai TC-003, penguji "[penguji]", tanggal 18-Nov-2026); Defect baris 5 (DF-001). Baris 8 sampai 87 dan 6 sampai 45 kosong |
| Kriteria lulus di sumber hanya contoh | "Contoh: 100% kasus Kritis lolos, minimal 95% total kasus lolos, tidak ada defect Kritis atau Tinggi terbuka" | Rencana Uji B8 |
| Rumus defect berat menghitung dua status | Empat COUNTIFS dijumlahkan: Kritis dan Tinggi dengan status "Terbuka", lalu Kritis dan Tinggi dengan status "Diperbaiki" (rumus penuh di sel, disingkat di sini) | Ringkasan dan Persetujuan B9 (tidak diubah) |
| Aturan defect di sumber | "Defect berstatus Terbuka dengan severity Kritis atau Tinggi menahan UAT." | Defect A2 |
| Penanda tangan sumber | "Disusun oleh \| Project Manager", "Diperiksa oleh \| ISO/ISMS Coordinator", "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Kontrol Dokumen B35 sampai B37, B11 |
| Riwayat revisi sumber | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" dan "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | Kontrol Dokumen C30, C31 |
| Blok tanda tangan UAT | "Penguji SINUX (Project Manager)", "Perwakilan pelanggan", "Service Delivery Manager" | Ringkasan dan Persetujuan A16 sampai A18 (tidak diubah) |

## 2. Isi patch (apa yang diubah dan kenapa)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Kasus Uji baris 5, 6, 7 (A sampai K) | TC-001, TC-002, TC-003 | Dikosongkan lewat clear_rows; warna isian mengikuti baris 8 (kuning input, diperiksa di out.xlsx); data validation Kategori dan Status serta conditional formatting Status tetap | Aturan baris CONTOH (RUNBOOK §6, prompt) |
| Defect baris 5 (A sampai I) | DF-001 | Dikosongkan lewat clear_rows; validation Severity dan Status tetap | Idem |
| Rencana Uji B8 | "Contoh: 100% kasus Kritis lolos, ..." | Dikosongkan lewat set null (clear_rows akan ikut menghapus label A8) | Contoh bukan kriteria resmi; lihat USULAN 1 |
| Kasus Uji A2 | "Baris biru muda = CONTOH." | "Kasus berstatus Gagal wajib punya Defect ID di sheet Defect. Rekomendasi SIAP mensyaratkan tidak ada kasus Gagal atau Belum. Kasus yang lolos retest diubah menjadi Lolos (USULAN)." | Kalimat CONTOH tidak berlaku sesudah baris dikosongkan; alat menolak teks CONTOH di luar Kontrol Dokumen. Kalimat pertama dari Kontrol Dokumen B20; kalimat kedua dari rumus B10; kalimat ketiga USULAN 2 |
| Defect A2 | "Defect berstatus Terbuka dengan severity Kritis atau Tinggi menahan UAT." | "Defect Kritis atau Tinggi berstatus Terbuka atau Diperbaiki menahan UAT." | Selaras dengan rumus B9 yang menghitung Terbuka dan Diperbaiki; USULAN 5 |
| Ringkasan dan Persetujuan A9 | "Defect Kritis atau Tinggi masih terbuka" | "Defect Kritis atau Tinggi menahan UAT" | Label lama tidak sama dengan rumus B9 (menghitung Terbuka dan Diperbaiki). Label baru memakai kata "menahan UAT" dari aturan di Defect A2 dan cukup pendek untuk kolom A (lebar 40; versi yang lebih rinci terpotong di render LibreOffice). Rumus tidak diubah; USULAN 5 |
| Kontrol Dokumen B21 | "Sheet Ringkasan dan Persetujuan menghitung tingkat kelulusan; UAT ditandatangani bila tidak ada defect Kritis atau Tinggi terbuka." | "Sheet Ringkasan dan Persetujuan menghitung tingkat kelulusan dan memberi rekomendasi; UAT ditandatangani bila rekomendasinya SIAP." | Kalimat lama hanya menyebut satu dari tiga syarat rumus B10. Panjang dijaga di dua baris karena tinggi baris 21 (23,85) tidak bisa diubah alat. USULAN 5 |
| Kontrol Dokumen B25 | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" | Legenda lama menyuruh menghapus baris yang sudah kosong. Kotak A25 tetap biru karena alat tidak mengubah warna di luar clear_rows. Kalimat sama dengan yang dipakai di FRM-04 agar seri konsisten |
| B6 Revisi | "00 (DRAFT)" | "00 (Draft)" | Revisi 00 dan status Draft sesuai prompt; sheet tidak punya baris Status terpisah. Huruf besar penuh diganti ejaan template |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by (D2); USULAN 3 |
| B35 Disusun oleh | "Project Manager" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed.OPS; USULAN 3 |
| B36 Diperiksa oleh | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed.OPS; USULAN 3 |
| B37 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by; USULAN 3 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 8.29" | "Kontrol Annex A 8.29" | 8.29 adalah kontrol Annex A, bukan klausul; "klausul atau kontrol" ragu-ragu. Sama dengan perlakuan di FRM-04 |
| C30 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A31 sampai E31 | Baris riwayat kedua, juga Revisi 00 bertanggal sama | Dikosongkan; teks asli dicatat di tabel Fakta pendukung | USULAN 4 |
| B12, B7, B8, B9, B10, B14, B15, B18 sampai B20, B26, B30, E30, A2 sampai A13 pada Kontrol Dokumen | | Tidak diubah | B12 "Klausul 8.6, 8.7" sudah memuat acuan ISO 9001. B7 dan B30 tanggal draft tim. B8 "Ditetapkan saat pengesahan" bukan tanggal. B9 mengikuti label sumber. B10 mengikuti "Pemilik dokumen" sumber tanpa nama. B14 mengikuti sumber. Kalimat tim yang sudah jelas tidak diganti (T1). Tanda tangan dan tanggal di C35 sampai D37 tetap kosong |

Pemeriksaan keluaran: out.xlsx tidak memuat em-dash atau en-dash di sel mana pun; tidak ada "Amirull" atau "COO" tersisa di sheet mana pun (sebutan COO hanya ada di B11 dan B37 sumber, keduanya sudah diganti, jadi aturan sebutan "Direktur (COO)" tidak terpakai di dokumen ini); pemindaian 146 sel teks dengan pola FORBIDDEN dan STYLE dari tools/lint_doc.py: 0 temuan (lint_doc.py hanya untuk docx, jadi pemindaian dijalankan manual). Hitung ulang LibreOffice atas out.xlsx: Ringkasan dan Persetujuan B3 sampai B7 dan B9 bernilai 0, B8 dan B10 kosong (rumus mengembalikan "" bila Total = 0). Render PDF LibreOffice dibuka halaman Kontrol Dokumen: semua teks terbaca.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, pengesahan dan tanda tangan kosong, tanggal efektif "Ditetapkan saat pengesahan" | Dipertahankan: keadaan yang benar untuk Draft (batas keras 3). Tidak ada tanda tangan, tanggal efektif, atau tanggal baru yang diisi |
| 2 | Seluruh isi contoh: 3 kasus uji, 1 defect, penguji "[penguji]", tanggal 2026-11-18 yang lebih akhir dari tanggal draft | Diperbaiki: clear_rows atas Kasus Uji 5 sampai 7 dan Defect 5. Sesudah itu Ringkasan dan Persetujuan menghitung nol |
| 3 | Kriteria lulus Rencana Uji B8 berlabel "Contoh:" dan belum resmi; rumus rekomendasi tidak memakai ambang 95% dan 100% Kritis | Sel B8 dikosongkan. Rumus tidak diubah (sel rumus "jangan diubah" menurut legenda sumber dan menambah ambang adalah keputusan kontrol). USULAN 1, open item 2 |
| 4 | Label A9 "masih terbuka" tetapi rumus B9 juga menghitung "Diperbaiki" | Diperbaiki di teks: label A9 dan aturan Defect A2 disamakan dengan rumus. Rumus tetap. USULAN 5 |
| 5 | Kasus uji tidak punya kolom Severity, jadi "100% kasus Kritis lolos" tidak bisa dihitung | Tidak diubah: kolom baru menambah struktur yang tidak ada di sumber. Sel contoh yang menyebutnya sudah dikosongkan, jadi tidak ada lagi klaim yang tak bisa dihitung di form. Open item 2 |
| 6 | SIAP mensyaratkan Gagal = 0 walau defect sudah Lolos retest; status kasus harus diubah ke Lolos | Dituliskan di Kasus Uji A2 (syarat dari rumus) dan langkah "ubah menjadi Lolos" berlabel (USULAN 2) |
| 7 | Contoh DF-001 menyebut "Perbaikan melalui CR"; CR berada di log FRM-04 (inferensi); FRM-05 tidak menyebut FRM-04 | Baris contoh dikosongkan, jadi frasa itu hilang. Rujukan ke FRM-04 tidak ditambah ke form (belum diputus). USULAN 7 |
| 8 | Kolom "Tanggal retest" kosong pada contoh; tidak ada kredensial atau data pribadi | Tidak ada tindakan. Dicek ulang atas out.xlsx: nama orang hanya di blok Disetujui oleh dan Pengesahan (dari defaults) |

Cacat tambahan yang saya temukan (di luar bagian 5 audit):

| # | Temuan | Penanganan |
|---|---|---|
| A | Kontrol Dokumen B21 hanya menyebut satu dari tiga syarat rekomendasi SIAP (defect berat, kasus Belum, kasus Gagal) | Diperbaiki di teks, lihat tabel bagian 2 dan USULAN 5 |
| B | Riwayat revisi punya dua baris Revisi 00 bertanggal sama; baris kedua menyebut "keselarasan RTO dan target pulih", topik yang tidak ada di form ini | Baris kedua dikosongkan, teks asli dicatat di bagian 1. USULAN 4 |
| C | Status defect "Diterima sebagai isu sisa" tidak dihitung rumus B9, jadi defect Kritis atau Tinggi yang diterima sebagai isu sisa tidak lagi menahan UAT. Sumber tidak menyebut siapa yang boleh menerima | Tidak diubah. Open item 3 |
| D | Rencana Uji memakai "Penguji pelanggan"; blok tanda tangan UAT memakai "Perwakilan pelanggan" | Tidak diubah; belum jelas satu peran atau dua. Open item 5 |
| E | Gambar di Alur Proses: cabang "Belum siap" tidak punya panah lanjutan, padahal teks gambar menyebut "tunggu defect ditutup" | Tidak bisa diperbaiki lewat xlsx_patch (gambar tetap). Open item 1 |
| F | Format ID (TC-nnn, DF-nnn) hanya tampak di baris contoh; tidak ada petunjuk format di judul kolom atau Cara pakai | Tidak dikarang ulang. Setelah baris contoh dikosongkan, pengguna tidak punya contoh format. Open item 8 |
| G | Legenda Alur Proses A2 menyebut garis putus-putus; gambar memang punya satu (dari "Catat defect" kembali ke alur utama) | Dipertahankan, cocok dengan gambar |

## 4. Asumsi dan tafsir

- "Approval persis" dari prompt mengalahkan sumber di blok Disusun, Diperiksa, Disetujui, mengikuti defaults.json yang menyebut nilai dipakai persis tanpa substitusi penyusun.
- Sheet "Kontrol Dokumen" tidak punya baris "Status" atau "Klasifikasi PRO-01" terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
- Rencana Uji B8 dikosongkan, bukan diganti petunjuk, karena sel masih bisa diisi per proyek dan petunjuk pengisian tidak ada di sumber. Angka 100% dan 95% dari sumber tetap tercatat di sini (bagian 1) agar tidak hilang.
- Rekomendasi "SIAP" di teks form dipakai sebagai singkatan dari nilai rumus "SIAP UAT DITANDATANGANI"; nilai penuh tertulis di Ringkasan dan Persetujuan B10.
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber FRM-05 maupun di patch; dicari dengan pola atas patch dan seluruh teks out.xlsx.
- Kalimat bernada perintah di sumber ("ganti nama menjadi FRM-05_<KodeProyek>.xlsx", "Isi Rencana Uji, lalu kasus uji ...", "hapus atau timpa saat dipakai", "jangan diubah") ditujukan ke pengguna form, bukan ke penyusun. Satu-satunya yang dijalankan adalah "hapus" atas baris contoh, karena prompt memerintahkan clear_rows yang sama. Tidak ada instruksi lain yang dituruti.
- Fakta tentang FRM-06 dan FRM-01 diambil dari salinan audit, tidak dibuka di Drive.
- Sheet Daftar (nilai dropdown) tidak diubah: kategori, status uji, severity, dan status defect adalah istilah kerja tim dan dipakai persis oleh rumus.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tetapkan kriteria lulus baku. Sumber hanya punya contoh "100% kasus Kritis lolos, minimal 95% total kasus lolos, tidak ada defect Kritis atau Tinggi terbuka"; sel dikosongkan. Bila ambang itu mau dipakai, form butuh kolom Severity di Kasus Uji dan rumus tambahan | Rencana Uji B8 (dikosongkan), Kasus Uji dan Ringkasan (belum diubah) | Fani |
| 2 | Tambah langkah: kasus yang lolos retest diubah statusnya dari Gagal menjadi Lolos, agar rekomendasi bisa menjadi SIAP. Ditulis di sel dengan label (USULAN) | Kasus Uji A2 | Fani |
| 3 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Project Manager, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Teks mengikuti rumus, bukan sebaliknya: label A9, aturan Defect A2, dan petunjuk B21 disamakan dengan perilaku rumus B9 dan B10 (Terbuka atau Diperbaiki; tiga syarat SIAP). Pilihan lain: ubah rumus agar sesuai teks lama | Ringkasan dan Persetujuan A9, Defect A2, Kontrol Dokumen B21 (sudah diterapkan di teks) | Fani |
| 6 | Pemilik dokumen tetap "Project Manager" sesuai sumber. Peran ini belum dipetakan ke orang; Erik Dwi Yanto tercantum sebagai penyusun dari defaults | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 7 | Tambahkan rujukan ke SNX-OPS-FRM-04 untuk defect yang diperbaiki lewat change request (sumber contoh: "Perbaikan melalui CR") | Cara pakai atau judul kolom Catatan di Defect (belum diterapkan) | Fani |
| 8 | Samakan masa simpan dengan FRM-06 (durasi kontrak + 5 tahun) atau pertahankan durasi kontrak + 3 tahun di FRM-05 | Kontrol Dokumen B14 (tidak diubah, sumber 3 tahun) | Fani, dengan Legal |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Gambar di Alur Proses tidak bisa diubah lewat xlsx_patch: cabang "Belum siap (tunggu defect ditutup)" tetap tanpa panah kembali ke alur. Butuh entri LEAD bila gambar harus diganti (ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah) | Orkestrator |
| 2 | Rumus rekomendasi tidak memakai ambang 95% dan 100% Kritis, dan Kasus Uji tidak punya kolom Severity. Putuskan USULAN 1 atau terima bahwa kriteria lulus hanya ditulis per proyek di Rencana Uji B8 tanpa dihitung form | Fani |
| 3 | Defect Kritis atau Tinggi berstatus "Diterima sebagai isu sisa" tidak menahan UAT dan sumber tidak menyebut siapa yang boleh menerimanya. Tetapkan peran penerima | Fani |
| 4 | Blok Keputusan UAT (tiga kotak centang) dan tiga baris tanda tangan tidak menyebut siapa yang memutus. Sumber hanya menyebut tiga peran penanda tangan | Fani |
| 5 | Istilah "Penguji pelanggan" (Rencana Uji A10) dan "Perwakilan pelanggan" (Ringkasan A17): satu peran atau dua? Samakan bila satu | Fani |
| 6 | Masa simpan FRM-05 (durasi kontrak + 3 tahun) berbeda dari FRM-06 (durasi kontrak + 5 tahun, salinan audit). FRM-05 adalah prasyarat BAST di FRM-06, jadi dua angka itu dilihat auditor berdampingan (USULAN 8) | Fani, dengan Legal |
| 7 | Rujukan "project charter (SNX-OPS-FRM-01)" di B19 dan kolom kriteria penerimaan di FRM-01 (audit baris 883, "Kriteria penerimaan (dasar UAT)"): cocokkan nama sheet dan sel setelah FRM-01 final | Orkestrator (lane OPS-FRM-01) |
| 8 | Format ID kasus uji dan defect tidak tertulis di form setelah baris contoh dikosongkan. Tambah petunjuk format hanya bila tim memutus polanya | Fani |
| 9 | Keterbatasan alat: tinggi baris tidak bisa diubah, kotak legenda A25 tetap biru walau tidak ada baris biru lagi, dan nilai rumus belum tersimpan di out.xlsx (openpyxl); Excel dan LibreOffice menghitung ulang saat dibuka (diverifikasi LibreOffice: Ringkasan nol). Putuskan terima atau tech_fix alat | Orkestrator |
| 10 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti agar tidak ada tanggal karangan. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |
| 11 | Peran "ISO/ISMS Coordinator" sebagai pemeriksa di sumber belum dipetakan ke orang; Fani dipakai sebagai pemeriksa karena defaults (USULAN 3) | Fani, owner |

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas 18 entri `set` di patch (12 berisi teks, 6 pengosongan: A31 sampai E31 dan Rencana Uji B8) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Draf pertama B21 berbunyi "UAT ditandatangani bila rekomendasinya SIAP UAT DITANDATANGANI": kata yang sama diulang dalam satu kalimat dan memakai huruf kapital | Diganti "... dan memberi rekomendasi; UAT ditandatangani bila rekomendasinya SIAP." Nilai penuh rumus tetap di B10 |
| Draf pertama label A9 ("Defect Kritis atau Tinggi, Terbuka atau Diperbaiki") terpotong di kolom A dan terbaca seperti daftar status | Diganti "Defect Kritis atau Tinggi menahan UAT", memakai kata dari aturan tim di Defect A2 |
| Draf pertama Kasus Uji A2 memakai "butuh nol kasus ... nol kasus" (kasar dan kembar) | Diganti "mensyaratkan tidak ada kasus Gagal atau Belum" |
| Label "(USULAN)" di Kasus Uji A2 bisa terbaca sebagai catatan penyusun di dokumen resmi | Dipertahankan: RUNBOOK §0 butir 4 mewajibkan label untuk hal tanpa sumber; alasannya ada di USULAN 2 |
| Legenda B25 terdengar telegrafis | Dipertahankan: satu kalimat pendek yang menjelaskan kotak biru yang tetap ada; sama dengan FRM-04 |
| Notes mengulang alasan perubahan di bagian 2, 3, USULAN, dan open items | Dibiarkan karena tiga judul wajib berdiri sendiri; xlsx tidak terpengaruh |
| Em-dash, en-dash, tebal di dalam sel, kelompok tiga paksaan, penutup positif, atribusi kabur | Tidak ada di nilai patch (pencarian karakter dan lint atas out.xlsx, baca ulang). Notes ini tidak memakai em-dash atau en-dash |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt orkestrator |
| "Draft awal untuk review dan pengesahan", "00 (Draft)" | revision_desc, revision, dan status di prompt dan defaults.json |
| "Klausul 8.6, 8.7" dan "Kontrol Annex A 8.29" | Prompt orkestrator, checklist.json (iso_9001 "8.6, 8.7", iso_27001 "8.29"), dan sel B12, B13 sumber |
| "Project Manager", "RESTRICTED (Internal)", "Durasi kontrak + 3 tahun", "13 Oktober 2026" | Sumber FRM-05, tidak diubah |
| Kalimat "Rekomendasi SIAP mensyaratkan tidak ada kasus Gagal atau Belum" dan "Terbuka atau Diperbaiki" | Rumus sumber Ringkasan dan Persetujuan B10 dan B9, tidak diubah |
| "Kasus yang lolos retest diubah menjadi Lolos" | Tidak ada di sumber; turunan perilaku rumus B10; berlabel USULAN di sel dan di USULAN 2 |
| 100%, 95%, tanggal 18-Nov-2026, TC-001 sampai TC-003, DF-001 (hanya di notes) | Sumber FRM-05 (Rencana Uji B8, Kasus Uji, Defect), semuanya sudah dikosongkan dari form |
| Masa simpan FRM-06 durasi kontrak + 5 tahun; kolom kriteria penerimaan di FRM-01 | Salinan audit context/audit baris 1884 dan 883, bukan Drive terbaru; ditandai di bagian 1 |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.

## ISO-W9

Spec dan patch tidak diubah di putaran ini (G-3 A9).

| Butir | Sebelum | Sesudah |
|---|---|---|
| Open item gambar Alur Proses | Terbuka, menunggu gambar baru lewat LEAD | Status diubah; teks open item lama tetap |

Open item yang ditutup atau diubah:

- Open item 1 (gambar Alur Proses: cabang Belum siap tanpa panah kembali): ditutup W9: diputus owner 15 Okt; gambar alur di xlsx sudah diganti tim dengan gambar png buatan sendiri, tidak diubah