# Catatan penyusun OPS-FRM-01: Project Plan, Scope & Timeline Records

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-01.patch.json. Mode xlsx, aksi T1, nomor SNX-OPS-FRM-01 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber, audit_class B, wave W5. Process owner = "Project Manager" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-01_Project_Plan_Scope_Timeline.xlsx (153326 byte) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 | 2026-10-13T06:09:12Z (get_file_metadata, dicek hari ini) | read_file_content (teks), download_file_content (xlsx, didekode ke /tmp/src/OPS-FRM-01.xlsx), 8 sheet dibuka dengan openpyxl (nilai, rumus, isian warna, data validation, conditional formatting), gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/checklist.json baris dengan link_text nama berkas | Description hanya nama berkas | Kriteria = substansi sumber + acuan ISO 9001:2015 "8.1, 8.2.2" dan ISO/IEC 27001:2022 "5.8" |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md baris 743 sampai 984 (bagian 5 Catatan kualitas dan celah) | salinan audit 13 Okt 2026 | DATA, dibandingkan dengan xlsx asli |

Delapan sheet di sumber: Kontrol Dokumen, Alur Proses, Daftar, Checklist G1, Project Charter, WBS dan Timeline, Milestone, Stakeholder. Sheet "Kontrol Dokumen" ada, jadi diselaraskan lewat `set`; tidak ada sheet yang ditambah.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Gate G1 dimiliki Service Delivery Manager dan lolos hanya bila tidak ada butir Belum | "Pemilik gate: Service Delivery Manager. Gate LOLOS bila tidak ada butir berstatus Belum." (Checklist G1!A2) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |
| Pemilik dokumen adalah peran Project Manager | "Pemilik dokumen" / "Project Manager" (Kontrol Dokumen!A10, B10) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |
| Masa simpan record per proyek | "Masa simpan record" / "Durasi kontrak + 3 tahun" (Kontrol Dokumen!A14, B14) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Lokasi |
|---|---|---|---|
| 1 | Satu salinan per proyek | "Salin file ini per proyek; ganti nama menjadi FRM-01_<KodeProyek>.xlsx." | Kontrol Dokumen!B18 |
| 2 | Proyek tidak dimulai bila ada butir Belum | "Isi Checklist G1 sebelum proyek dimulai; proyek tidak dimulai bila ada butir Belum." | Kontrol Dokumen!B19 |
| 3 | Pembaruan progres mingguan | "Perbarui kolom Progres dan Status minimal mingguan (SNX-OPS-SOP-01 Bagian 6.4)." | Kontrol Dokumen!B21 |
| 4 | Acuan klausul | "Klausul 8.1, 8.2.2" (B12); "Klausul atau kontrol Annex A 5.8" (B13) | Kontrol Dokumen |
| 5 | Delapan butir G1, semua default Belum | "Klasifikasi data pelanggan dan kebutuhan keamanan informasi teridentifikasi (SNX-ISMS-PRO-01)." | Checklist G1!B12 |
| 6 | Rumus keputusan G1 | `=IF(COUNTIF(C5:C12,"Belum")=0,"LOLOS","TAHAN")` | Checklist G1!C14 |
| 7 | Progres keseluruhan berbobot | `=IFERROR(SUMPRODUCT('WBS dan Timeline'!I5:I104,'WBS dan Timeline'!J5:J104)/SUM('WBS dan Timeline'!I5:I104),0)` | Project Charter!B22 |
| 8 | Durasi hari kalender | "Kolom Durasi dihitung otomatis (hari kalender)." dan `=IF(AND(E5<>"",F5<>""),F5-E5+1,"")` | WBS dan Timeline!A2, G5 |
| 9 | Kanal komunikasi | "Kanal resmi: email dan grup WhatsApp proyek. Kredensial tidak pernah dikirim melalui kanal ini." | Stakeholder!A2 |
| 10 | SD dan PM = dua peran | "SD dan PM" pada tabel POL-OPS-001: baris "Service Delivery Manager" dan baris "Project Manager" (salinan audit baris 218 dan 219; sumber bukan xlsx ini) | context/audit ops |

## 3. Hasil uji

Perintah: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-01.xlsx specs/OPS-FRM-01.patch.json /tmp/pen-OPS-FRM-01/out.xlsx`

Hasil: `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 8 sheet, 1 gambar (Alur Proses), 3 data validation (Checklist G1, WBS dan Timeline, Milestone), conditional formatting 2/1/1, rumus 1/1/101/20 (Checklist G1, Project Charter, WBS, Milestone). Berkas hasil juga terbuka di LibreOffice (konversi PDF berhasil). Pemindaian teks seluruh sel hasil dengan pola FORBIDDEN dan STYLE dari tools/lint_doc.py: 0 temuan; tidak ada em-dash maupun en-dash. lint_doc.py sendiri hanya untuk docx, jadi pemindaian itu saya jalankan manual.

## 4. Isi patch dan alasannya

| Sel atau baris | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| WBS dan Timeline baris 5 sampai 9 | 5 baris bertanda "CONTOH" (kick-off, provisioning, migrasi, UAT, BAST) | dikosongkan (clear_rows); rumus Durasi tetap | RUNBOOK §6 buang baris CONTOH; tanggal contoh November 2026 |
| Milestone baris 5 | "Go-live layanan", bertanda "CONTOH" | dikosongkan; rumus Deviasi tetap | idem |
| Stakeholder baris 5 | "[nama PIC]", "[pelanggan]", "[email kerja]" | dikosongkan | placeholder = data dummy |
| Kontrol Dokumen B11 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by (D2) |
| Kontrol Dokumen B13 | "Klausul atau kontrol Annex A 5.8" | "Kontrol Annex A 5.8" | 5.8 adalah kontrol Annex A; kata "Klausul atau" meragukan jenis acuannya |
| Kontrol Dokumen B36 | "Project Manager" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed OPS |
| Kontrol Dokumen B37 | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed OPS |
| Kontrol Dokumen B38 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |
| Kontrol Dokumen C31 | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| Kontrol Dokumen baris 32 | revisi 00 kedua, tanggal sama, menyebut "keselarasan RTO dan target pulih" | dikosongkan | duplikat; frasa RTO tidak berkaitan dengan isi workbook |
| Kontrol Dokumen baris 22 | "5. Hapus baris CONTOH (biru muda) sebelum dipakai." | dikosongkan | baris CONTOH sudah tidak ada |
| Kontrol Dokumen baris 26 | legenda "Baris CONTOH: hapus atau timpa saat dipakai" | dikosongkan (teks dan warna) | idem |
| Alur Proses!A2 | "... · garis putus-putus = kembali ke alur utama" | "Kotak biru = output akhir · kotak oranye = cabang ke tindakan atau prosedur lain" | gambar tidak punya garis putus-putus, legenda menjanjikan yang tidak ada |
| Checklist G1!A1 | "... ke SD dan PM" | "... ke Service Delivery Manager dan Project Manager" | singkatan tanpa definisi; satu istilah untuk satu peran, sama dengan A2 dan sheet Project Charter |

Tidak diubah, sudah selaras dengan data baris: Nomor SNX-OPS-FRM-01, Judul, Klasifikasi RESTRICTED (Internal), Pemilik dokumen Project Manager, Acuan 9001 "Klausul 8.1, 8.2.2", Masa simpan "Durasi kontrak + 3 tahun", Tujuan, tanggal efektif "Ditetapkan saat pengesahan" (bukan tanggal), kolom Tanda tangan dan Tanggal kosong, E31 "Menunggu".

Sebutan COO: setelah B11 dan B38 diganti, workbook tidak lagi menyebut COO, jadi aturan "Direktur (COO)" tidak terpakai. Direktur Utama hanya muncul di blok pengesahan sebagai "President Director". Zammad, GLPI, vault, dan PPN tidak ada di sumber dan tidak ditambahkan.

## 5. Penanganan cacat context/audit (bagian 5, fileId 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Data terisi adalah contoh (WBS M5:M9, Milestone G5, Stakeholder placeholder, tanggal Nov 2026) | Diperbaiki: baris dikosongkan, lihat tabel bagian 4 |
| 2 | Checklist G1 semua "Belum" (TAHAN) padahal WBS contoh menandai tugas Selesai dan Berjalan | Hilang bersama data contoh. Default "Belum" di Checklist G1 dipertahankan karena itu keadaan awal form |
| 3 | Go-live contoh 17 Nov sama dengan selesai migrasi dan mendahului UAT | Hilang bersama data contoh |
| 4 | Daftar G1 memuat Belum, Lolos, Tidak berlaku, tetapi rumus C14 hanya memeriksa "Belum"; sel kosong tidak menahan gate | Tidak diubah: rumus adalah substansi tim dan legenda menulis "Sel rumus: jangan diubah". Usulan perbaikan ada di bagian USULAN (butir 3) |
| 5 | Rumus Durasi F-E+1 hari kalender | Tidak ada cacat; A2 sheet WBS sudah menyatakan hari kalender |
| 6 | Total bobot 100 hanya tampil di J2, tidak ada validasi | Tidak diperbaiki: alat tidak menambah validasi. Usulan di bagian USULAN (butir 4) |
| 7 | Kolom Bukti, PIC, Tanggal Checklist G1 kosong; tidak ada nama orang selain COO di Pengesahan | Kolom kosong adalah isian per proyek, dibiarkan. Nama COO diganti sesuai defaults, tiga penanda tangan kini berbeda |
| 8 | Lintas dokumen: B21 merujuk "SNX-OPS-SOP-01 Bagian 6.4"; checklist G1 di PRO-OPS-001 8.2 memuat 7 butir tanpa klasifikasi data, FRM-01 memuat 8 | Rujukan dipertahankan; menjadi open item 4 dan 5. PRO-OPS-001 berstatus bahan saja, bukan dokumen yang saya ubah |
| 9 | Riwayat revisi: dua baris rev 00 bertanggal sama; frasa RTO tidak relevan | Diperbaiki: satu baris, deskripsi dari data baris |
| 10 | Pengesahan tanpa tanda tangan atau tanggal | Dibiarkan kosong (batas keras 3); nama diisi dari defaults |
| 11 | Diagram: kotak "Kembalikan ke Commercial" tanpa panah kembali | Tidak bisa diperbaiki dari patch (gambar tertanam). Legenda disesuaikan dengan gambar; masalah diagram menjadi USULAN butir 5 dan open item 2 |

## USULAN

| # | Butir | Status di berkas | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga nama di blok Pengesahan dan B11: Erik Dwi Yanto (Disusun), Fani Fatullah (Diperiksa), Samuel Kristanto Utomo (Disetujui). Sumber menulis peran saja ("Project Manager", "ISO/ISMS Coordinator") dan COO sebagai penyetuju. Defaults menandai semua baris ini USULAN, dengan pembalik "form operasional disetujui COO bila owner memutus" | Diterapkan | owner (nama penyetuju: owner atau Samuel) |
| 2 | Pemilik dokumen ditulis sebagai peran "Project Manager" (jabatan tanpa nama, sesuai sumber). Pemetaan peran itu ke jabatan nyata belum ada | Diterapkan apa adanya | Fani |
| 3 | Rumus C14 Checklist G1 dibuat menahan gate bila ada butir kosong: `=IF(COUNTIF(C5:C12,"Lolos")+COUNTIF(C5:C12,"Tidak berlaku")=8,"LOLOS","TAHAN")` | Tidak diterapkan | Fani |
| 4 | Penanda bila total bobot WBS (J2) bukan 100, mis. conditional formatting pada J2 | Tidak diterapkan | Fani |
| 5 | Garis putus-putus dari "Kembalikan ke Commercial" kembali ke "Isi Checklist G1" pada gambar Alur Proses. Sumber tidak menyebut apa yang terjadi sesudah paket dikembalikan; tujuan panah itu tafsir | Tidak diterapkan | Fani |

Tidak ada angka baru dari saya di berkas hasil. Angka 8 di butir 3 adalah jumlah butir G1 di sumber.

## Open items

1. Tanggal draft "13 Oktober 2026" (B7) dan tanggal baris riwayat revisi (B31) dipertahankan dari sumber. Tidak ada tanggal baru yang saya tulis dan tanggal efektif tetap "Ditetapkan saat pengesahan". Owner memutus apakah tanggal draft perlu diganti tanggal draft revisi ini.
2. Gambar Alur Proses (image1.png) tidak bisa disunting xlsx_patch. Kotak "Kembalikan ke Commercial" tidak punya jalan kembali, dan teks gambar tidak menyebut siapa yang menindaklanjuti. Perlu keputusan pemilik dokumen (USULAN 5) lalu gambar baru lewat LEAD atau tim.
3. GAP alat (kosmetik): clear_rows menghapus isian warna sel yang dikosongkan, sehingga baris 5 sampai 9 WBS, baris 5 Milestone, dan baris 5 Stakeholder berwarna polos, sedangkan baris kosong lain di sheet yang sama berwarna kuning input (FFF2CC). Sel rumus tidak terpengaruh. Perbaikannya di tools/xlsx_patch.py (memulihkan FFF2CC pada sel input yang dikosongkan), di luar batas tulis saya. Conditional formatting membaca nilai sel, bukan isian warna, jadi fungsi form tidak berubah. Belum dilihat di Excel; hanya konversi LibreOffice yang berhasil.
4. Rujukan "SNX-OPS-SOP-01 Bagian 6.4" (B21) benar terhadap sumber SOP-01. SOP-01 akan dirender ulang ke 11 bagian template (W2); orkestrator perlu memeriksa bahwa pembaruan progres mingguan tetap ada di butir 6.4 spec OPS-SOP-01, atau mengubah rujukan ini.
5. Checklist G1 di FRM-01 memuat 8 butir, G1 di PRO-OPS-001 8.2 memuat 7 butir tanpa butir klasifikasi data (catatan audit). Pemilik dokumen memutus daftar mana yang berlaku. Dokumen ini memakai 8 butir karena butir 8 menjadi dasar acuan 27001 5.8.
6. Nama peran Project Manager, Service Delivery Manager, dan Commercial (di gambar) belum dicocokkan dengan HR-ORG-01 (status IN_PROGRESS di ledger saat saya menyusun). Cocokkan setelah HR-ORG-01 DONE. "NOC Engineer" hanya muncul di baris contoh yang sudah dikosongkan.
7. Sheet Kontrol Dokumen tidak punya baris Status terpisah; "00 (DRAFT)" di B6 memuat Revisi dan Status sekaligus dan dipertahankan. Menambah baris butuh perubahan tata letak yang tidak bisa dilakukan patch.
8. Warna biru muda dipakai dua arti di sumber: baris CONTOH dan kolom No butir Checklist G1 (A5:A12). Legenda CONTOH sudah dihapus, jadi biru di Checklist G1 kini tanpa keterangan. Fungsi form tidak berubah; pemilik dokumen boleh menambah legenda.
9. Ruang lingkup dokumen (proyek apa yang wajib memakai FRM-01, apakah proyek tanpa paket handover Commercial dikecualikan) tidak tertulis di sumber. Workbook tidak punya bagian Scope, jadi tidak ada pengecualian yang saya tambahkan.
10. Kalimat perintah di sumber (butir Cara pakai 1 sampai 5) adalah petunjuk pengisian untuk pengguna form, bukan instruksi untuk penyusun, dan tidak saya jalankan sebagai perintah. Pembuangan baris CONTOH saya kerjakan karena RUNBOOK §6, bukan karena butir 5 itu. Butir 5 dan legenda CONTOH ikut dibuang karena sudah tidak punya objek.
11. Rujukan kode dokumen di workbook: SNX-OPS-SOP-01, SNX-OPS-FRM-02 (Project Charter!A21), SNX-ISMS-PRO-01 (Checklist G1!B12, Project Charter!A19). Ketiganya ada di worklist (OPS-SOP-01, OPS-FRM-02, ISMS-PRO-01). Xlsx tidak punya tabel Dokumen terkait.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI. Teks di berkas hasil hampir seluruhnya suara tim. Saya menulis ulang delapan sel lewat `set` (B11, B13, C31, B36, B37, B38 di Kontrol Dokumen, Alur Proses!A2, Checklist G1!A1) dan mengosongkan baris. Enam sel pertama berisi nama, jabatan, atau kalimat dari data baris dan defaults, jadi tidak ada kalimat bebas buatan saya. Dua sel lain (Alur Proses!A2 dan Checklist G1!A1) hanya memotong atau menguraikan singkatan. Di notes ini saya memeriksa frasa pengisi, kelompok tiga yang dipaksakan, ekor penegas, dan tanda kutip untuk penekanan, lalu satu kalimat saya koreksi: klaim lama bahwa tidak ada rumus atau validasi yang menyangkut warna salah, karena conditional formatting ada (Checklist G1, WBS dan Timeline, Milestone). Yang benar: conditional formatting membaca nilai sel, bukan isian warna, dan isian warna yang dihapus clear_rows tidak mengubah hasilnya. Butir open items 3 dan 8 sudah memakai rumusan itu.

Adakah fakta, angka, nama, atau tanggal tanpa sumber. Nama dan jabatan penanda tangan bersumber dari config/defaults.json v21 (prepared_reviewed OPS, approved_by) dan ditandai USULAN butir 1. Perluasan "SD dan PM" menjadi Service Delivery Manager dan Project Manager bersumber dari tabel POL-OPS-001 di salinan audit (baris 218 dan 219), bukan dari xlsx; sudah dicatat di fakta pendukung 10. Klausul 8.1, 8.2.2, dan 5.8 ada di sumber dan di data baris. Tanggal 13 Oktober 2026 dari sumber. Rumus di USULAN 3 adalah usulan saya dan berlabel; angka 8 di dalamnya adalah jumlah butir G1 di sumber. Tidak ada angka lain yang saya tambahkan. Dua pernyataan hasil pembacaan sendiri: tanggal contoh November 2026 (WBS E5:F9, Milestone C5:D5 di xlsx asli) dan isian biru muda E7EEF7 pada baris CONTOH serta kolom No Checklist G1 (openpyxl atas /tmp/src/OPS-FRM-01.xlsx).
