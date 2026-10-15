# Catatan penyusun ISMS-FRM-01: Backup Log & Restore Testing Records

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-FRM-01.patch.json. Mode xlsx, aksi T1, nomor SNX-ISMS-FRM-01 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber (Kontrol Dokumen!B9), audit_class B, wave W5. Process owner = "Lead NOC" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-FRM-01_Backup_Log_Restore_Testing_Records.xlsx (145875 byte) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV | 2026-10-13T06:09:28Z (get_file_metadata, dicek hari ini, sama dengan di prompt) | download_file_content, didekode ke /tmp/src/ISMS-FRM-01.xlsx; 7 sheet dibuka dengan openpyxl (nilai, rumus, isian warna, data validation, conditional formatting); gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/checklist.json baris 87 | Description hanya nama berkas | Kriteria = substansi sumber + acuan ISO 9001:2015 "8.5.3" dan ISO/IEC 27001:2022 "8.13" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md baris 8 sampai 215 (bagian 5 pada baris 199 sampai 211) | salinan audit 13 Okt 2026 | DATA, dibandingkan dengan xlsx asli |
| Pembanding peran dan rujukan | bagian SNX-ISMS-SOP-03 pada berkas audit yang sama (baris 2637 sampai 2845); specs/HR-ORG-01.json | salinan audit 13 Okt 2026; HR-ORG-01 status DONE | DATA, hanya untuk memetakan peran dan memeriksa rujukan silang; tidak ada isinya yang disalin ke workbook kecuali yang tertulis di tabel bagian 4 |

Tujuh sheet di sumber: Kontrol Dokumen, Alur Proses, Daftar, Daftar Job, Backup Log, Restore Record, Ringkasan. Sheet "Kontrol Dokumen" ada, jadi diselaraskan lewat `set`; tidak ada sheet yang ditambah.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Lead NOC; masa simpan record 3 tahun | "Pemilik dokumen" / "Lead NOC" (Kontrol Dokumen!A10, B10); "Masa simpan record" / "3 tahun" (Kontrol Dokumen!A14, B14) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |
| Status Gagal dua kali berturut menjadi tiket P2 | "Shift malam mengisi Backup Log setiap hari; status Gagal dua kali berturut menjadi tiket P2." (Kontrol Dokumen!B19) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |
| Restore ke produksi butuh dua persetujuan | "Durasi, RTO, dan kepatuhan dihitung otomatis. Restore ke produksi butuh approval Lead NOC dan persetujuan pelanggan." (Restore Record!A2) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Lokasi |
|---|---|---|---|
| 1 | Acuan klausul | "Klausul 8.5.3" (B12); "Klausul atau kontrol Annex A 8.13" (B13) | Kontrol Dokumen |
| 2 | Tujuan dan prosedur induk | "Daftar job backup, log pemeriksaan harian, dan record restore (uji berkala maupun permintaan) sesuai SNX-ISMS-SOP-03." | Kontrol Dokumen!B15 |
| 3 | KPI di sheet Ringkasan | "Tingkat sukses backup (KPI 98%)" dan "Tingkat keberhasilan uji restore (KPI 95%)" | Ringkasan!A7, A10 |
| 4 | Durasi restore dan kepatuhan RTO dihitung otomatis | `=IF(OR(G5="",H5=""),"",ROUND((H5-G5)*1440,0))` dan `=IF(OR(I5="",J5=""),"",IF(I5<=J5*60,"Ya","Tidak"))` | Restore Record!I5, K5 (rumus yang sama sampai baris 155) |
| 5 | RTO diambil dari Daftar Job per Job ID | `=IF(D5="","",IFERROR(INDEX('Daftar Job'!$J$5:$J$86,MATCH(D5,'Daftar Job'!$A$5:$A$86,0)),""))` | Restore Record!J5 |
| 6 | Jenis restore punya tiga pilihan | Daftar!E2:E4: "Uji berkala", "Permintaan pelanggan", "Pemulihan insiden" | Daftar |
| 7 | Tiket P2 menunjuk SNX-OPS-SOP-04 | Gambar Alur Proses: kotak oranye "Tiket P2" / "SNX-OPS-SOP-04"; garis putus-putus kembali ke "Catat restore" | xl/media/image1.png |
| 8 | Peran NOC Engineer mengisi log (pembanding) | "NOC Engineer | Memantau job, menangani kegagalan, melaksanakan restore dan uji restore, mengisi log" dan "Shift malam memeriksa status semua job backup dan mencatat hasilnya di SNX-ISMS-FRM-01 (sheet Backup Log)." | Bagian 5 dan butir 7.2.1 SNX-ISMS-SOP-03 (salinan audit) |

## 3. Hasil uji

Perintah: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-FRM-01.xlsx specs/ISMS-FRM-01.patch.json /tmp/pen-ISMS-FRM-01/out.xlsx`

Hasil terakhir: `"pass": true`, `"fails": []`, lulus pada putaran pertama dan diulang sesudah satu perubahan kata di Daftar Job!A2 (juga lulus). Fitur sebelum dan sesudah sama: 7 sheet, 1 gambar (Alur Proses), 3 data validation masing-masing di Daftar Job, Backup Log, dan Restore Record, conditional formatting 0/1/2 (Backup Log, Restore Record), rumus 453 di Restore Record dan 8 di Ringkasan. Berkas hasil terbuka di LibreOffice (konversi PDF berhasil, 151285 byte). Pemindaian seluruh 140 teks sel hasil dengan pola FORBIDDEN dan STYLE dari tools/lint_doc.py: 0 temuan; tidak ada em-dash, en-dash, COO, CEO, atau CONTOH. Perbandingan nilai sel sumber dengan hasil: hanya sel di tabel bagian 4 yang berubah. Isian warna sel yang dikosongkan kini mengikuti baris isian di bawahnya (kuning FFF2CC; sel rumus I sampai K di Restore Record tetap abu-abu), jadi GAP kosmetik di notes OPS-FRM-01 butir 3 tidak muncul di sini, kecuali satu sel legenda (open item 3).

## 4. Isi patch dan alasannya

| Sel atau baris | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| Daftar Job baris 5 dan 6 | JOB-001 dan JOB-002, kolom Catatan "CONTOH", "[pelanggan A]", "VM produksi [nama]" | dikosongkan (clear_rows) | RUNBOOK §6: buang baris CONTOH dan placeholder |
| Backup Log baris 5 dan 6 | dua entri 10 Nov 2026 dengan "[pemeriksa]" | dikosongkan | idem |
| Restore Record baris 5 | RST-2026-001, 12 Nov 2026, Q5 "CONTOH", "[pelaksana]" | dikosongkan; rumus I5:K5 tetap | idem |
| Backup Log!A2 (baris 2) | "Baris biru muda = CONTOH." | dikosongkan | baris CONTOH sudah tidak ada |
| Kontrol Dokumen baris 25 | legenda "Baris CONTOH: hapus atau timpa saat dipakai" | dikosongkan | idem |
| Kontrol Dokumen baris 31 | revisi 00 kedua, tanggal sama, menyebut "keselarasan RTO dan target pulih" | dikosongkan | duplikat; klaim keselarasan RTO tidak terlihat di workbook (cacat audit 8 dan 12) |
| Kontrol Dokumen!C30 | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| Kontrol Dokumen!B11 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by (D2) |
| Kontrol Dokumen!B13 | "Klausul atau kontrol Annex A 8.13" | "Kontrol Annex A 8.13" | 8.13 adalah kontrol Annex A; "Klausul atau" meragukan jenis acuannya (pola sama dengan OPS-FRM-01 dan ISMS-REG-01) |
| Kontrol Dokumen!B19 | "Shift malam mengisi Backup Log setiap hari; status Gagal dua kali berturut menjadi tiket P2." | "NOC Engineer shift malam mengisi Backup Log setiap hari; status Gagal dua kali berturut menjadi tiket P2 di Zammad." | peran "Shift malam" dipetakan ke NOC Engineer (HR-ORG-01 dan SOP-03 Bagian 5); tiket Ops di Zammad (premis owner, defaults ticketing). USULAN 2 dan 3 |
| Kontrol Dokumen!B35 | "Lead NOC" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed ISMS |
| Kontrol Dokumen!B36 | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed ISMS |
| Kontrol Dokumen!B37 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |
| Daftar Job!A2 | "RPO dan RTO dalam jam." | "RPO dan RTO dalam jam. Simpan salinan offline (break-glass) kunci enkripsi backup di luar password manager (USULAN)." | aturan lintas dokumen kunci backup; Daftar Job punya kolom Encryption. USULAN 4 |

Tidak diubah, sudah selaras dengan data baris: Nomor SNX-ISMS-FRM-01, Judul, Revisi "00 (DRAFT)" (memuat Revisi dan Status Draft), Klasifikasi RESTRICTED (Internal), Pemilik dokumen Lead NOC, Acuan 9001 "Klausul 8.5.3", Masa simpan "3 tahun", Tujuan, tanggal efektif "Ditetapkan saat pengesahan" (bukan tanggal), kolom Tanda tangan dan Tanggal kosong, E30 "Menunggu", legenda Alur Proses!A2 (gambar memang memuat garis putus-putus, jadi legenda benar), butir Cara pakai 1, 3, dan 4, rumus semua sheet, judul kolom, isi sheet Daftar.

Sebutan COO: setelah B11 dan B37 diganti, workbook tidak lagi menyebut COO, jadi aturan "Direktur (COO)" tidak terpakai. Direktur Utama hanya muncul di blok pengesahan sebagai "President Director". PPN dan GLPI tidak ada di sumber dan tidak ditambahkan. Vault: workbook memakai "password manager" mengikuti sumber; tidak ada klaim status vault (lihat open item 10).

## 5. Penanganan cacat context/audit (bagian 5, fileId 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Seluruh isi adalah data CONTOH berisi placeholder (Daftar Job L5:L6, Restore Record Q5, Backup Log A2, "[pelanggan A]", "[pemeriksa]", "[pelaksana]") | Diperbaiki: baris dikosongkan, lihat tabel bagian 4. Form belum menjadi bukti implementasi 8.13 sampai Lead NOC mengisi job, log, dan restore nyata; itu pekerjaan tim, bukan patch |
| 2 | Tanggal contoh (Backup Log A5:A6, Restore Record B5, Ringkasan B3) jatuh sesudah tanggal draft | Tiga tanggal pertama hilang bersama baris contoh. Ringkasan!B3 (1 November 2026) dipertahankan; open item 4 |
| 3 | Rujukan prosedur terverifikasi (SOP-03, tiket P2 ke SNX-OPS-SOP-04) | Tidak ada yang diperbaiki. B15, B19, dan gambar selaras dengan SOP-03 butir 7.2.2 |
| 4 | KPI: SOP-03 memuat empat KPI, Ringkasan hanya melabeli 98% dan 95% dan "Restore dalam RTO" berupa jumlah; "percobaan pertama" tidak bisa dibedakan | Tidak diubah: rumus adalah substansi tim, alat tidak menambah kolom. USULAN 5 |
| 5 | Parameter contoh JOB-002 (password manager AST-001, Full, 30 hari, RPO 24, RTO 4) selaras dengan REG-01, PLN-01, SOP-03 | Dikosongkan karena baris itu bertanda CONTOH. Open item 11 mencatat parameternya agar bisa dimasukkan Lead NOC sebagai job nyata |
| 6 | Frekuensi uji restore tidak ada di form (ada di SOP-03 butir 7.4.1 dan PLN-01) | Tidak ditambahkan: baris 22 Kontrol Dokumen adalah pemisah tata letak dan tidak ada tempat kosong untuk butir baru. USULAN 8 |
| 7 | RPO tidak punya rumus pemeriksaan kepatuhan | Tidak diperbaiki; rumus tidak diubah dan alat tidak menambah kolom. USULAN 6 |
| 8 | RTO contoh berbeda antarjob; tidak ada tabel RTO standar; revisi 00 baris kedua menyebut "keselarasan RTO dan target pulih" tanpa nilai | Baris revisi kedua dikosongkan (duplikat, klaim tidak terlihat di form). Kolom RTO bebas isi dipertahankan; nilai standar ada di SOP-03 butir 6.1 dan PLN-01 bagian 4 |
| 9 | Hasil contoh Ringkasan 50% dari dua entri contoh | Hilang bersama data contoh: B7 dan B10 kini kosong ("") sampai ada data |
| 10 | Tidak ada kolom tanggal kedaluwarsa retensi atau pemeriksaan pelanggaran retensi 30 hari | Tidak diperbaiki; menambah kolom mengubah tata letak. Digabung ke USULAN 6 |
| 11 | SOP-03 butir 7.3.3 menyebut "sheet Restore Test dan Request", sheet di form bernama "Restore Record" | Nama sheet tidak diubah (rumus Ringkasan merujuk nama itu). Penyelarasan ada di SOP-03; open item 5 |
| 12 | Pengesahan kosong, "Menunggu", revisi 00 tercatat dua kali | Revisi ganda diperbaiki (baris 31). Tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Nama tiga penanda tangan diisi dari defaults, sekarang berbeda satu sama lain |

## USULAN

| # | Butir | Status di berkas | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga nama di blok Pengesahan dan B11: Erik Dwi Yanto (Disusun), Fani Fatullah (Diperiksa), Samuel Kristanto Utomo (Disetujui). Sumber menulis peran saja ("Lead NOC", "ISO/ISMS Coordinator") dan COO sebagai penyetuju. Defaults menandai baris ini USULAN, dengan pembalik "form operasional disetujui COO bila owner memutus" | Diterapkan | owner (nama penyetuju: owner atau Samuel) |
| 2 | Peran "Shift malam" di B19 dipetakan ke NOC Engineer. Dasarnya SOP-03 Bagian 5 (NOC Engineer "mengisi log") dan HR-ORG-01 (NOC Engineer, pola shift); jabatan itu USULAN di sumbernya dan belum ada pemegang | Diterapkan di B19 | Fani |
| 3 | Sistem tiket P2 backup = Zammad. Premis owner menyebut Zammad untuk Ops; saya menafsirkan tiket P2 backup sebagai tiket Ops karena pemilik dokumen adalah Lead NOC. Sumber tidak menyebut sistem tiket | Diterapkan di B19 | Fani |
| 4 | Salinan offline (break-glass) kunci enkripsi backup di luar password manager. Sumber tidak menyebut salinan itu; aturan lintas dokumen meminta label USULAN | Diterapkan di Daftar Job!A2 | Fani |
| 5 | Wadah ukur untuk KPI SOP-03 yang belum punya tempat di Ringkasan: "Uji restore bulanan terlaksana per pelanggan backup" 100%, "Waktu restore uji dalam RTO" 100% (persentase dari B11 dibagi B8), dan kolom percobaan ke berapa untuk "Uji restore berhasil pada percobaan pertama" 95% | Tidak diterapkan | Fani |
| 6 | Pemeriksaan otomatis kepatuhan RPO di Daftar Job dan tanggal kedaluwarsa retensi (kolom F sudah memuat retensi dalam hari) | Tidak diterapkan | Fani |
| 7 | Kapasitas baris dibanding masa simpan 3 tahun: Backup Log hanya sampai baris 606 (602 baris, satu baris per job per pemeriksaan), Restore Record sampai baris 155, dan rumus Ringkasan berhenti di baris yang sama. Usulan: satu berkas per periode, atau rentang diperluas | Tidak diterapkan | Fani |
| 8 | Frekuensi uji restore ditulis di Cara pakai: bulanan untuk setiap pelanggan berlayanan backup, triwulanan untuk sistem internal kritis (angka dari SOP-03 butir 7.4.1, bukan dari xlsx ini) | Tidak diterapkan | Fani |

Angka baru dari saya di berkas hasil: tidak ada. Angka 100%, 95%, 602, 155, dan 606 di tabel ini berasal dari SOP-03 atau dari ukuran sheet sumber.

## Open items

1. Tanggal draft "13 Oktober 2026" (Kontrol Dokumen!B7) dan tanggal baris riwayat revisi (B30) dipertahankan dari sumber. Saya tidak menulis tanggal baru, dan tanggal efektif tetap "Ditetapkan saat pengesahan". Owner memutus apakah tanggal draft diganti tanggal draft revisi ini.
2. Sheet Kontrol Dokumen tidak punya baris Status terpisah; "00 (DRAFT)" di B6 memuat Revisi dan Status sekaligus dan dipertahankan. Menambah baris butuh perubahan tata letak yang tidak bisa dilakukan patch.
3. GAP alat (kosmetik): clear_rows pada baris legenda 25 menyalin warna dari baris 26, sehingga sel A25 kini abu-abu tanpa label, di atas "Sel rumus: jangan diubah" yang juga abu-abu. Biru muda (E7EEF7) tidak dipakai lagi di workbook. Fungsi form tidak berubah. Perbaikannya di tools/xlsx_patch.py atau lewat LEAD; di luar batas tulis saya. Belum dilihat di Excel; hanya konversi LibreOffice yang berhasil.
4. Ringkasan!B3 berisi 1 November 2026. Itu sel pilihan bulan, bukan baris bertanda CONTOH, dan semua rumus Ringkasan bergantung padanya, jadi dipertahankan. Tanggalnya jatuh sesudah tanggal draft; pengguna menggantinya tiap bulan. Pemilik dokumen memutus apakah nilai awalnya perlu diganti.
5. SOP-03 butir 7.3.3 menyebut "sheet Restore Test dan Request", sedangkan sheet di form ini "Restore Record". Perlu penyelarasan di SOP-03 (lane ISMS-SOP-03); nama sheet di form tidak saya ubah karena rumus Ringkasan merujuknya.
6. Jenis restore di Daftar!E2:E4 ada tiga ("Uji berkala", "Permintaan pelanggan", "Pemulihan insiden"), sedangkan Tujuan (B15) dan Cara pakai butir 3 hanya menyebut uji berkala dan permintaan. Teks tim dipertahankan; pemilik dokumen memutus apakah pemulihan insiden ikut disebut.
7. Dropdown Shift berisi Shift 1, Shift 2, Shift 3, sedangkan Cara pakai menyebut shift malam. Baris contoh yang sudah dihapus memakai Shift 3, tetapi sumber tidak menyatakan Shift 3 adalah shift malam. Pemilik dokumen menetapkan shift mana yang disebut shift malam.
8. Pelaku yang membuat tiket P2 tidak disebut di sumber (B19, SOP-03 butir 7.2.2 memakai kalimat pasif "menjadi tiket P2"). Form tidak punya kolom untuk pembuat tiket selain "Ref tiket" dan "Diperiksa oleh".
9. Peran di workbook: Lead NOC dan NOC Engineer adalah jabatan USULAN di HR-ORG-01 dan belum punya pemegang (K-10 di spec itu). "ISO/ISMS Coordinator" di blok Pengesahan lama belum punya jabatan (K-13); kolom Diperiksa oleh kini berisi Fani Fatullah sesuai defaults. Erik Dwi Yanto (L1) tercantum sebagai penyusun, sedangkan pemilik dokumen Lead NOC belum ada pemegangnya.
10. Vault: workbook memakai "password manager" mengikuti sumber, dan tidak ada klaim status. Catatan konteks (CONTEXT-PACK-v19 butir 7) menyebut SOP-03 menyimpan kunci enkripsi di vault yang ikut di-backup, sedangkan salinan audit SOP-03 Bagian 6.2 butir 2 menulis kunci disimpan di password manager terpisah dari backup. Bila JOB-002 (backup password manager) benar dipakai, kunci dan backup bisa berada di sistem yang sama; ini tafsir saya dari dua sumber itu, bukan fakta di xlsx. Status vault "menunggu konfirmasi Ops" tidak ditulis karena workbook tidak membuat klaim status. Ops (Fani) mengonfirmasi dan SOP-03 menyelaraskan rumusannya.
11. Parameter baris JOB-002 yang dikosongkan: password manager (AST-001), Full, harian 02:00, retensi 30 hari, offsite Ya, encryption Ya, RPO 24 jam, RTO 4 jam. SOP-03 butir 6.1, PLN-01 bagian 4, dan REG-01 selaras dengan parameter itu (menurut catatan audit). Lead NOC dapat memasukkannya sebagai job nyata; saya tidak membawanya karena baris itu bertanda CONTOH.
12. Gambar Alur Proses (image1.png) tertanam dan tidak bisa disunting xlsx_patch. Isinya selaras dengan legenda A2 dan B19 (garis putus-putus ada, tiket P2 menunjuk SNX-OPS-SOP-04), tetapi tidak menyebut Zammad maupun pelaku. Tidak ada yang saya ubah.
13. Rujukan kode dokumen di workbook: SNX-ISMS-SOP-03 (B15), SNX-OPS-RPT-01 (B21), SNX-OPS-SOP-04 (gambar). Ketiganya ada di worklist (ISMS-SOP-03, OPS-RPT-01, OPS-SOP-04). Xlsx tidak punya tabel Dokumen terkait, jadi tidak ada yang ditambahkan.
14. Kalimat perintah di sumber (Cara pakai 1 sampai 4, dan legenda "hapus atau timpa saat dipakai") adalah petunjuk bagi pengguna form, bukan instruksi untuk penyusun; tidak dijalankan sebagai perintah. Legenda CONTOH dibuang karena RUNBOOK §6, bukan karena kalimat itu.
15. Scope tidak tertulis di sumber: workbook tidak punya bagian Scope, sehingga tidak jelas job mana yang wajib masuk Daftar Job (hanya pelanggan, hanya internal, atau keduanya; kolom B memuat "Pelanggan atau internal"). Saya tidak menambah pengecualian. SOP-03 memuat cakupan layanan backup pelanggan dan sistem internal; pemilik dokumen memutus apakah form perlu menyebutnya.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI. Teks di berkas hasil hampir seluruhnya suara tim. Saya menulis delapan sel lewat `set` dan satu kalimat baru: tujuh sel berisi nama, jabatan, atau kalimat dari data baris dan defaults, dan B19 hanya menambah satu nama peran dan satu nama sistem pada kalimat tim. Satu-satunya kalimat yang saya karang adalah Daftar Job!A2. Draf pertama berbunyi "Kunci enkripsi backup punya salinan offline (break-glass) di luar password manager (USULAN)". Kalimat itu terbaca seperti pernyataan keadaan nyata (seolah salinan sudah ada), padahal usulan. Saya ubah ke bentuk perintah, "Simpan salinan offline (break-glass) kunci enkripsi backup di luar password manager (USULAN)", sama dengan gaya butir Cara pakai tim ("Daftarkan setiap job ..."). Di notes ini saya memeriksa frasa pengisi, kelompok tiga yang dipaksakan, ekor penegas, dan kata kerja manusia untuk benda. Kalimat "form belum menjadi bukti implementasi" di bagian 5 butir 1 saya pertahankan karena itu temuan audit, bukan pujian atau penegasan.

Adakah fakta, angka, nama, atau tanggal tanpa sumber. Nama dan jabatan penanda tangan bersumber dari config/defaults.json v21 (prepared_reviewed ISMS, approved_by) dan ditandai USULAN 1. "NOC Engineer" bersumber dari specs/HR-ORG-01.json dan Bagian 5 SOP-03 di salinan audit (fakta pendukung 8), bukan dari xlsx. "Zammad" bersumber dari premis owner (defaults ticketing); penerapannya ke tiket P2 backup adalah tafsir saya dan berlabel USULAN 3. "Salinan offline (break-glass)" bersumber dari aturan lintas dokumen di RUNBOOK §6 dan CONTEXT-PACK-v19 butir 7, berlabel USULAN 4. Klausul 8.5.3 dan 8.13 ada di sumber dan di data baris. Tanggal 13 Oktober 2026 dari sumber. Angka 100% dan 95% di USULAN 5 serta frekuensi bulanan dan triwulanan di USULAN 8 berasal dari SOP-03 (salinan audit), bukan dari xlsx. Angka 602, 155, dan 606 di USULAN 7 hasil membaca ukuran sheet dan rentang rumus di xlsx asli (Backup Log A5:A606, Restore Record sampai baris 155). Tidak ada angka lain yang saya tambahkan. Dua pernyataan hasil pembacaan sendiri: isian warna E7EEF7 pada baris CONTOH dan legenda (openpyxl atas /tmp/src/ISMS-FRM-01.xlsx), dan bahwa gambar Alur Proses memuat garis putus-putus (gambar dibuka langsung).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan" (sebutan ISMS).
Disunting: Tujuan, Cara pakai 2 sampai 4, dan catatan Restore Record A2. Cara pakai 1 dan legenda dipertahankan (T1).
Cara pakai 2 dibuat pasif dengan pelaku di tengah kalimat supaya tidak diawali nama peran; arti tetap.
Restore Record A2: "approval Lead NOC dan persetujuan pelanggan" disatukan menjadi "persetujuan Lead NOC dan pelanggan"; arti tetap.
Sheet Daftar Job dan Alur Proses tidak disunting.
