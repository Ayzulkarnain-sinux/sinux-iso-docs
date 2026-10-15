# Catatan penyusun FAT-FRM-02: Financial Information Access Authorization Records

Status: DRAFTED (patch + notes ada). Patch: specs/FAT-FRM-02.patch.json. Mode xlsx, aksi T1 (HOLD-T3 yang dipromosikan di W0 karena berkas tim kini terbaca), wave W7b, nomor SNX-FAT-FRM-02 (nomor SNX lama dipertahankan), department "Finance, Accounting & Tax", klasifikasi "RESTRICTED (Internal)", audit_class kosong. Approval persis dari instruksi baris: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Finance Lead" (jabatan reviewer departemen, tanpa nama; sumber tidak punya baris "Pemilik dokumen", lihat asumsi A1). Catatan worklist: "tim menandai ada; proses hanya bila berkas terlihat di ukur ulang W0"; berkas terlihat dan terbaca, jadi diproses.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 10. Financial Information Access Authorization Records (Google Sheet) | 1UqQ-hYKjAFNhevDwOoF59YQXLHjeFBR7UBHKoSA233k | 2026-10-14T09:11:45.648Z (get_file_metadata hari ini, sama dengan data baris; createdTime 2026-10-14T08:08:22.639Z) | read_file_content (teks, tanpa komentar), download_file_content dengan exportMimeType xlsx (didekode ke /tmp/src/FAT-FRM-02.xlsx), semua sheet dibuka dengan openpyxl |
| Kriteria penerimaan | config/checklist.json baris 32 (checked true, fileId sama dengan sumber, kolom ISO kosong) | ekspor checklist, bukan berkas Drive | Description: "Dokumen berisi list akses dan pemegang akses terhadap data dan informasi departemen Finance" |
| Pembanding: SNX-FAT-SOP-04 (spec repo) | tidak ada fileId (dokumen T2 dalam run ini) | tidak diukur | Dibaca dari specs/FAT-SOP-04.json hanya untuk masa simpan 10 tahun dan nama peran |
| Catatan cacat dan nama | context/audit/iso-sinux-supdocs-fat, -hr, -sintesis (salinan 14 Okt 2026) | salinan audit | DATA. Kutipan nama dari salinan; berkas HR-JA-001 tidak saya buka di Drive |

Dua sheet di sumber: "Worksheet" (4 dokumen, kolom Document Name, Details, Access Holder, Doc Link) dan "Platform Access" (3 platform, kolom Login Info, Website, Access Holder). Tidak ada sheet "Kontrol Dokumen" dan tidak ada baris CONTOH atau data dummy, jadi tidak ada baris yang dikosongkan dari sheet tim. Alat Drive yang dipakai hanya baca (read_file_content, download_file_content, get_file_metadata). Nol penulisan, salin, bagi, atau hapus. Kalimat perintah kepada AI di sumber: nihil.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemegang akses BCA Bank Access ditulis per peran dengan nama panggilan. Di Platform Access!C3 "Dipta" ditulis persis seperti sumber; "Bila" dan "Samuel" dilengkapi sesuai data_conflicts; struktur tiga baris dipertahankan | "Maker: Dipta,Bila" / "Maker,Approval,Releaser: Samuel, Bila" / "SysAdmin: Samuel, Bila" (Platform Access!C3) | 1UqQ-hYKjAFNhevDwOoF59YQXLHjeFBR7UBHKoSA233k |
| Worksheet PPh 21 satu-satunya dokumen yang pemegang aksesnya bukan hanya FAT: HR dan Management ikut. Tiga dokumen lain hanya FAT | "Worksheet PPh 21 Masa & Tahunan" / "HR, FAT, Management" (Worksheet!A2, C2); "FAT" (Worksheet!C3, C4, C5) | 1UqQ-hYKjAFNhevDwOoF59YQXLHjeFBR7UBHKoSA233k |
| Coretax dipegang FAT dan Management; Artha Graha Bank Access dipegang FAT dan Samuel | "Coretax" / "FAT & Management" (Platform Access!A2, C2); "FAT & Samuel" (Platform Access!C4) | 1UqQ-hYKjAFNhevDwOoF59YQXLHjeFBR7UBHKoSA233k |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Lokasi |
|---|---|---|---|
| 1 | Empat dokumen keuangan dan pajak terdaftar | "Tax Outstanding SINUX", "AR & AP Aging", "Fixed Asset" (Worksheet!A3, A4, A5) bersama "Worksheet PPh 21 Masa & Tahunan" (A2) | sumber, sheet Worksheet |
| 2 | Isi Tax Outstanding: empat jenis pajak | "Dokumen log sheet outstanding pajak sinux untuk pajak masa dan tahunan: 1. PPh 21/26 2. PPh 23/26 3. PPN 4. PPh Badan" | Worksheet!B3 |
| 3 | AR & AP Aging diperbarui tiap tahun | "Dokumen tracker Hutang & Piutang SINUX selama tahun berjalan. Dokumen akan diperbaharui setiap tahun" | Worksheet!B4 |
| 4 | Tiga platform: Coretax, BCA, Artha Graha; alamat situs login | "https://coretaxdjp.pajak.go.id/identityproviderportal/Account/Login", "https://vpn.klikbca.com/+CSCOE+/logon.html", "https://ibb.ag.co.id/business/login?returnUrl=%2F" | Platform Access!B2, B3, B4 |
| 5 | Dasar dugaan "Dipta" = Pradipta Nugraha (hanya dugaan, tidak dipakai di sel): "Bila" dan "Pradipta Nugraha" adalah dua Supporting PIC departemen FAT | "Dep. FAT \| @Bila Parwasto @Pradipta Nugraha Finance" | context/audit sintesis baris 680 |
| 6 | Bila = Kana Salsabila Putri Koeswologito (owner 14 Okt, konfirmasi "selesai") | "pakai": "Kana Salsabila Putri Koeswologito"; "dasar": "owner 14 Okt: orang yang sama; HR-JA-001 JA-10" | config/defaults.json, data_conflicts "Nama staf Finance" |
| 7 | Jabatan di Job Analysis: Kana = Finance (dipakai di C3); Pradipta = Accounting & Tax (tidak dipakai di sel) | "\| JA-10 \| Finance \| Kana Salsabila Putri Koeswologito \|" dan "\| JA-11 \| Accounting & Tax \| Pradipta Nugraha \|" | context/audit hr baris 77 dan 78 (HR-JA-001) |
| 8 | Peran Finance Lead dan Finance Staff dipakai apa adanya; pemetaan ke orang belum ada | "peran apa adanya di SOP Billing dan Tax" dan konfirmasi "owner (pemetaan peran ke orang)"; matriks peran HR-ORG-01: "Finance Lead" / "Belum dipetakan" | config/defaults.json; specs/HR-ORG-01.json (K-13) |
| 9 | SOP Billing menulis akses FAT dibatasi untuk personel FAT dan CEO, dan 2FA untuk CoreTax dan KlikBCA Bisnis | "Akses folder Google Drive FAT dan Register Penagihan Google Sheets dibatasi ketat hanya untuk personel FAT dan CEO." dan "akun CoreTax DJP dan KlikBCA Bisnis wajib 2FA dan tidak dibagikan" | context/audit fat baris 153 dan 154 (SOP Billing 7.1) |
| 10 | Judul ini di daftar FAT dokumen sumber ditandai berkoordinasi dengan Ops/IT | "10. Financial Information Access Authorization Records (berkoordinasi dengan Ops/IT)." | context/audit sintesis baris 753 |
| 11 | Masa simpan 10 tahun untuk arsip penagihan dan bukti pajak (lingkup lain berlabel USULAN) | "Retensi: minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001/ISO 27001." dan tabel rekaman SNX-FAT-SOP-04: "Minimal 10 tahun (USULAN)" untuk dokumen keuangan lain | context/audit fat baris 166 (SOP Billing 8.2); specs/FAT-SOP-04.json |
| 12 | AR & AP Aging memakai fileId yang sama dengan baris checklist 29 "Billing & Collection Monitoring Register" | Checklist baris 29: "Dokumen tracker untuk semua piutang dari customer", fileId 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ; Worksheet!D4 berisi tautan ke fileId yang sama | config/checklist.json; sumber Worksheet!D4 |

## 3. Pemetaan kriteria (Description baris 32)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| "list akses" | Sheet Worksheet (4 dokumen dengan tautan) dan sheet Platform Access (3 platform dengan alamat situs) | Sumber, tidak diubah selain ejaan dan nama |
| "pemegang akses" | Kolom Access Holder di kedua sheet; pemegang platform bank ditulis dengan nama lengkap bila tertulis di data_conflicts (Kana Salsabila Putri Koeswologito, Samuel Kristanto Utomo), "Dipta" tetap seperti sumber | Sumber dan data_conflicts |
| "data dan informasi departemen Finance" | Tujuan di Kontrol Dokumen!B15 menyebut dokumen keuangan, platform pajak dan bank | Kriteria baris |

Pemetaan klausul ISO (checklist baris 32 tidak memberi acuan klausul). Satu label "(USULAN, perlu konfirmasi konsultan)" dipakai pada dua sel, B12 dan B13, karena workbook memisah acuan 9001 dan 27001 ke dua sel. Judul klausul adalah pengetahuan standar, bukan teks sumber, dan tidak dicocokkan dengan teks standar (UNMEASURED):

| Klausul | Alasan |
|---|---|
| ISO 9001:2015 7.5.3 | Pengendalian informasi terdokumentasi, termasuk akses ke informasi itu |
| ISO/IEC 27001:2022 Annex A 5.15 | Kontrol akses: aturan siapa boleh mengakses apa |
| ISO/IEC 27001:2022 Annex A 5.18 | Hak akses: pemberian dan pencatatan hak akses per orang |
| ISO/IEC 27001:2022 Annex A 5.3 | Pemisahan tugas; relevan bagi peran Maker, Approval, Releaser, dan SysAdmin di bank |
| ISO/IEC 27001:2022 Annex A 8.3 | Pembatasan akses informasi |

## 4. Hasil uji

Perintah: `python3 -I tools/xlsx_patch.py /tmp/src/FAT-FRM-02.xlsx specs/FAT-FRM-02.patch.json /tmp/pen-FAT-FRM-02/out.xlsx`

Hasil: `"pass": true`, `"fails": []`, putaran ketiga dan terakhir (dua putaran sebelumnya juga pass; putaran ketiga sesudah perbaikan putaran 1 orkestrator: Platform Access!C3 kembali menulis "Dipta"). Fitur sebelum dan sesudah sama: tiga sheet (Kontrol Dokumen ditambah di posisi pertama oleh alat; Worksheet dan Platform Access dari sumber), tanpa gambar, data validation, conditional formatting, atau rumus. Keluaran mentah: /tmp/pen-FAT-FRM-02/xlsx_patch.out.txt. Hasil dibuka di LibreOffice (konversi ke PDF berhasil) dan tiga sheet dilihat sebagai gambar: teks Kontrol Dokumen muat di tinggi baris donor, tautan Doc Link di Worksheet tetap berupa hyperlink. Pemindaian teks semua sel hasil (/tmp/pen-FAT-FRM-02/scan.out.txt): nol em-dash, en-dash, CONTOH, SKILL_, DOCTRINE, DEC-, HANDOVER, Claude, Altair, nama alat KB, "komersil", "diagnosa", "hutang", "diperbaharui", CEO, COO, tebal, dan tanda kutip ganda. Satu kata kredensial muncul (B20) dan itu larangannya sendiri. Tidak ada kata sandi, PIN, atau token di sel mana pun. lint_doc.py hanya untuk docx, jadi pemindaian itu manual dengan pola yang sama.

## 5. Isi patch dan alasannya

| Sel atau baris | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| add_control_sheet | sumber tanpa sheet Kontrol Dokumen | sheet disalin dari form donor SNX-OPS-FRM-01 ke posisi pertama (hanya label medan) | instruksi baris; sheet lain tidak ditambah |
| Kontrol Dokumen A1, A2, B4 sampai B15 | kosong | judul, "PT Strategi Integrasi Nusantara (SINUX) · Departemen Finance, Accounting & Tax", nomor, judul, "00 (DRAFT)", tanggal draft, "Ditetapkan saat pengesahan", klasifikasi, pemilik, penyetuju, acuan ISO (USULAN), masa simpan (USULAN), tujuan | medan template; lihat bagian 6 dan 7 untuk asal tiap nilai |
| Kontrol Dokumen A18:B21 | kosong | empat butir Cara pakai | sesuai struktur dua sheet sumber |
| Kontrol Dokumen A31:E31 | kosong | "00", "15 Oktober 2026", "Draft awal untuk review dan pengesahan", "Finance Staff", "Menunggu" | satu baris riwayat revisi; tanda tangan dan tanggal pengesahan tidak diisi (batas keras 3) |
| Kontrol Dokumen B36:B38 | kosong | "Finance Staff", "Finance Lead", "Samuel Kristanto Utomo / President Director" | approval persis dari instruksi baris |
| Kontrol Dokumen baris 25 dan 27 (clear_rows) | kotak warna legenda donor tanpa teks | warna dihapus | legenda sel input dan sel rumus tidak berlaku (tidak ada rumus di sumber) |
| Worksheet!B3 | "outstanding pajak sinux" | "outstanding pajak SINUX" | nama perusahaan |
| Worksheet!B4 | "Hutang & Piutang", "diperbaharui" | "Utang & Piutang", "diperbarui" | ejaan baku; kalimat tim selebihnya dipertahankan |
| Platform Access!C3 | "Maker: Dipta,Bila / Maker,Approval,Releaser: Samuel, Bila / SysAdmin: Samuel, Bila" | "Dipta" dipertahankan persis; Bila menjadi Kana Salsabila Putri Koeswologito (Finance), Samuel menjadi Samuel Kristanto Utomo (Direktur Utama); jabatan hanya pada sebutan pertama dalam sel; peran dan urutan tiga baris tidak diubah | data_conflicts: nilai nama dan jabatan wajib; Samuel di badan dokumen = Direktur Utama |
| Platform Access!C4 | "FAT & Samuel" | "FAT & Samuel Kristanto Utomo (Direktur Utama)" | idem |

Tidak diubah: kata "Dipta" di Platform Access!C3; semua sel A, B, D di Worksheet selain B3 dan B4; kolom Access Holder di Worksheet (HR, FAT, Management); header kedua sheet (termasuk "Login Info"); alamat situs dan tautan; Platform Access!C2.

Zammad, GLPI, vault, PPN, dan COO tidak muncul di workbook, jadi aturan sebutan COO, pembagian tiket, status vault, dan rumusan PPN tidak terpakai dan tidak ada yang ditambahkan. "PPN" di Worksheet!B3 hanya nama jenis pajak tanpa tarif.

## 6. Asumsi

| # | Asumsi | Dasar | Pengaruh bila salah |
|---|---|---|---|
| A1 | Pemilik dokumen = Finance Lead | Sumber tidak punya baris "Pemilik dokumen"; aturan defaults.json: jabatan reviewed departemen, tanpa nama | Kontrol Dokumen!B10 diganti |
| A2 | Dihapus pada putaran perbaikan 1: pemetaan "Dipta" ke Pradipta Nugraha tidak tertulis di sumber, HR-JA-001, HR-ORG-01, maupun data_conflicts, jadi tidak dipakai di sel | Platform Access!C3 menulis "Dipta" persis seperti sumber | Dugaan dicatat di open item 13 |
| A3 | "Bila" = Kana Salsabila Putri Koeswologito | defaults.json data_conflicts, konfirmasi "selesai" | nihil (sudah dikonfirmasi owner) |
| A4 | Tanggal draft "15 Oktober 2026" | Tanggal hari penyusunan; sumber memberi tanggal modifikasi 14 Oktober 2026, bukan tanggal draft; bukan tanggal efektif | Kontrol Dokumen!B7 dan B31 diganti |
| A5 | "Management" di Worksheet!C2 dan Platform Access!C2 tidak dirinci dan dibiarkan | Sumber tidak mendefinisikan | Lihat open item 3 |

## 7. Penanganan cacat context/audit

`grep -n 1UqQ-hYKjAFNhevDwOoF59YQXLHjeFBR7UBHKoSA233k context/audit/*.md` tidak menemukan baris (keluaran kosong). Berkas ini tidak punya bagian 5 "Catatan kualitas dan celah" sendiri, sama dengan catatan README context/audit untuk berkas yang muncul sesudah audit. Cacat yang relevan saya ambil dari tetangganya: daftar FAT di sintesis (baris 753) dan SOP Billing (context/audit fat, bagian 5 dan 7.1). Cacat di berkas itu sendiri saya periksa langsung dari xlsx.

| Berkas | Cacat atau catatan | Penanganan |
|---|---|---|
| sintesis baris 753 | Dokumen ini ditandai berkoordinasi dengan Ops/IT | Open item 9: izin sebenarnya di Google Drive dan di bank belum dibandingkan dengan daftar; pemutus Fani |
| fat bagian 5 butir 2 dan 11 | Pemisahan peran penyusun, pemeriksa, penyetuju lemah; satu peran tunggal sebagai pemeriksa; peran Finance Lead dan Staff Finance tidak ada di HR-JA-001 | Pola yang sama tampak di Platform Access!C3 (open item 1). Peran Finance Lead dan Finance Staff dipakai apa adanya, pemetaan ke orang open item 2 |
| fat bagian 5 butir 3 | Ejaan Samuel dan sebutan CEO versus Direktur Utama | Diperbaiki: "Samuel Kristanto Utomo", "Direktur Utama" di Platform Access!C3 dan C4 |
| fat 7.1 | Akses ke Folder Google Drive FAT dan Register Penagihan dibatasi untuk personel FAT dan CEO | Open item 5 dan 6: daftar tidak memuat folder itu dan menulis AR & AP Aging hanya FAT |
| xlsx sumber | Ejaan "Hutang", "diperbaharui", "sinux" | Diperbaiki di Worksheet!B3 dan B4 |
| xlsx sumber | Nama panggilan (Dipta, Bila, Samuel) di kolom pemegang akses bank | Bila dan Samuel diperbaiki ke nama lengkap sesuai data_conflicts. "Dipta" dibiarkan seperti sumber karena pemetaannya tidak tertulis (open item 13) |
| xlsx sumber | Tidak ada sheet Kontrol Dokumen, nomor, revisi, status, penyetuju | Diperbaiki: add_control_sheet dan set |
| xlsx sumber | Kolom Access Holder memakai "FAT", "HR", "Management" tanpa nama orang | Tidak diubah, open item 3 dan 4 |

## USULAN

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Acuan ISO 9001:2015 klausul 7.5.3 (Kontrol Dokumen!B12) | owner, diteruskan ke konsultan |
| 2 | Acuan ISO/IEC 27001:2022 Annex A 5.3, 5.15, 5.18, 8.3 (Kontrol Dokumen!B13) | owner, diteruskan ke konsultan; Fani untuk sisi ISMS |
| 3 | Masa simpan "berlaku sampai digantikan; versi lama minimal 10 tahun" (B14). Angka 10 tahun dari SOP Billing 8.2 untuk arsip penagihan dan bukti pajak; perluasan ke daftar akses ini adalah usulan | FAT, Legal untuk ketentuan pajak |
| 4 | Larangan menulis kata sandi, PIN, atau token di berkas ini (Cara pakai butir 3, kini dengan pelaku Finance Staff). Tidak ada di sumber | Fani |
| 5 | Finance Lead (pemilik dokumen) meninjau isi berkas setiap tahun (Cara pakai butir 4, kini berlabel). Masa tinjau YEARLY dari data baris; penunjukan Finance Lead sebagai peninjau adalah usulan | FAT |
| 6 | Mengganti header "Login Info" di Platform Access!A1 dengan "Platform", karena "Login Info" bisa terbaca sebagai tempat menyimpan data login. Tidak saya ubah (T1, suara tim) | FAT |
| 7 | Mengganti nama sheet "Worksheet" dengan "Daftar Dokumen". Alat tidak mengganti nama sheet | FAT |
| 8 | Finance Staff mengisi dan memperbarui kedua sheet (Cara pakai butir 1 sampai 3). Sumber tidak menyebut siapa pengisinya; Finance Staff dipilih karena menjadi penyusun di blok Pengesahan | FAT |

## Open items

| # | Butir | Pemutus atau pelaksana |
|---|---|---|
| 1 | Platform Access!C3 (BCA): sebagaimana ditulis tim, nama Bila (Kana Salsabila Putri Koeswologito) muncul di baris Maker, baris Maker, Approval, Releaser, dan baris SysAdmin; Samuel di dua baris terakhir. Dibaca harfiah, satu orang memegang peran pembuat, penyetuju, pelepas, dan administrator sekaligus. Sumber tidak menjelaskan apakah baris kedua berarti tiga peran sekaligus untuk dua orang itu atau penulisan yang tidak lengkap. Teks tidak saya tafsirkan ulang; kontrol Annex A 5.3 sudah dicantumkan di acuan. Perlu konfirmasi pembagian peran sebenarnya di KlikBCA Bisnis | Samuel dan FAT |
| 2 | Finance Lead (pemilik dokumen, pemeriksa) dan Finance Staff (penyusun) belum dipetakan ke orang atau jabatan di Struktur Organisasi (K-13). Daftar ini menulis pemegang akses dengan jabatan JA-10 dan JA-11, bukan Finance Lead atau Finance Staff (diubah W9: definisi kedua peran ditambahkan di Kontrol Dokumen (USULAN); pemetaan ke orang atau jabatan tetap menunggu) | owner |
| 3 | "Management" di Worksheet!C2 (PPh 21) dan Platform Access!C2 (Coretax) tidak dirinci: siapa saja yang memegang akses. Hal yang sama untuk "FAT" dan "HR" (tidak ada nama per orang) | FAT |
| 4 | Worksheet PPh 21 berisi data gaji karyawan menurut uraiannya ("perhitungan PPh 21 karyawan") dan pemegang aksesnya mencakup HR dan Management. Perlu keputusan siapa di HR yang boleh melihat, dan apakah perluasan itu sesuai klasifikasi RESTRICTED (Internal) | Aziz dan FAT |
| 5 | Cakupan daftar hanya 4 dokumen dan 3 platform. SOP Billing menyebut data keuangan lain yang aksesnya dibatasi (Folder Google Drive FAT, Register Penagihan dan Penjualan, Master Sales Sheet, Google Form Data Subskripsi Klien) dan SNX-FAT-SOP-04 menyebut Folder arsip FAT dan Financial Document Register. Tidak ada di daftar. Belum ditambahkan karena T1 tidak boleh menambah isi tanpa sumber | FAT |
| 6 | AR & AP Aging (fileId 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ) adalah berkas yang sama dengan baris checklist 29 Billing & Collection Monitoring Register (HOLD-T3). Daftar ini menulis pemegang akses "FAT" saja, sedangkan SOP Billing 7.1 menyebut Register Penagihan terbuka untuk personel FAT dan CEO. Perlu keputusan apakah dua baris checklist itu satu dokumen dan apakah Direktur Utama termasuk pemegang | FAT dan Samuel |
| 7 | Tempat penyimpanan kredensial dan perangkat 2FA untuk Coretax, BCA, dan Artha Graha tidak ada di sumber. Auditor kemungkinan menanyakannya. Bila jawabannya vault, statusnya "menunggu konfirmasi Ops" | Fani |
| 8 | Peran di bank untuk Artha Graha ("FAT & Samuel") tidak dirinci menjadi Maker, Approval, Releaser, atau SysAdmin seperti BCA | FAT |
| 9 | Daftar mencatat pemegang akses menurut tim. Izin sebenarnya di Google Drive untuk empat tautan Doc Link (semuanya tautan "usp=sharing"), dan di Coretax dan dua bank, tidak saya bandingkan (UNMEASURED). Sintesis menandai dokumen ini berkoordinasi dengan Ops/IT | Fani |
| 10 | Kontrol Dokumen tidak punya sel masa tinjau, jadi nilai YEARLY hanya muncul di Cara pakai butir 4 (USULAN 5) | FAT |
| 11 | Kosmetik: tiga kotak berbingkai kosong tersisa di Kontrol Dokumen baris 25 sampai 27 (bekas legenda donor; warna sudah dihapus, bingkai tidak bisa dihapus clear_rows). Kolom A dan B di Platform Access terlalu sempit sehingga "BCA Bank Access" dan alamat situs terpotong di tampilan; alat tidak mengubah lebar kolom sheet tim | tech_fix alat bila dianggap mengganggu |
| 12 | Kalimat perintah kepada AI di sumber: nihil. Kalimat "Dokumen akan diperbaharui setiap tahun" adalah uraian tim untuk isi AR & AP Aging, bukan instruksi | nihil |
| 13 | "Dipta" di Platform Access!C3 (peran Maker BCA) tidak punya nama lengkap tertulis. Dugaan: Pradipta Nugraha (JA-11, Accounting & Tax), karena Dep. FAT hanya punya dua Supporting PIC, Bila dan Pradipta (sintesis baris 680). Dugaan itu tidak ditulis di sel. Perlu konfirmasi nama lengkap dan jabatan | FAT |

## Sweep

Putaran sweep orkestrator, satu butir (Cara pakai tanpa pelaku; B20 tidak cocok dengan isi kolom Access Holder; B21 tanpa label USULAN). Perubahan hanya di specs/FAT-FRM-02.patch.json (empat sel) dan notes ini. Pelaku diambil dari dua peran yang sudah ada di blok Pengesahan (Finance Staff, Finance Lead); pilihan itu keputusan, jadi tiap butir berlabel (USULAN) dan dicatat di USULAN 4, 5, dan 8.

| Sel | Sebelum | Sesudah |
|---|---|---|
| Kontrol Dokumen!B18 | "Sheet Worksheet: satu baris untuk satu dokumen keuangan." | "Finance Staff mengisi sheet Worksheet, satu baris per dokumen (USULAN)." |
| Kontrol Dokumen!B19 | "Sheet Platform Access: satu baris untuk satu platform pajak atau bank." | "Finance Staff mengisi sheet Platform Access, satu baris per platform (USULAN)." |
| Kontrol Dokumen!B20 | "Tulis pemegang akses dengan nama dan jabatan. Jangan tulis kata sandi, PIN, atau token (USULAN)." | "Finance Staff menulis pemegang akses sebagai kelompok atau sebagai nama dan jabatan, tanpa kata sandi, PIN, atau token (USULAN)." |
| Kontrol Dokumen!B21 | "Pemilik dokumen meninjau isi berkas ini setiap tahun." | "Finance Lead meninjau isi berkas ini setiap tahun (USULAN)." |

Alasan B20: kolom Access Holder di sumber berisi kelompok ("HR, FAT, Management", "FAT", "FAT & Management") di Worksheet dan nama di baris bank Platform Access, jadi petunjuk "nama dan jabatan" saja tidak cocok dengan isi. Rumusan baru mengakui kedua bentuk; pemecahan kelompok menjadi nama tetap open item 3.

Uji: `python3 -I tools/xlsx_patch.py /tmp/src/FAT-FRM-02.xlsx specs/FAT-FRM-02.patch.json /tmp/pen-FAT-FRM-02/out.xlsx` memberi `"pass": true`, `"fails": []` pada putaran pertama sweep (keluaran mentah /tmp/pen-FAT-FRM-02/xlsx_patch.out.txt). Teks keempat butir muat di tinggi baris donor (dilihat sebagai gambar hasil LibreOffice). Fakta, angka, nama, dan sel lain tidak diubah.

## Jawaban dua pertanyaan pemeriksaan

1. Apa yang membuat teks ini terdengar buatan AI. Sesudah dibaca ulang, kalimat Tujuan versi pertama memakai pola "X: Y." dan mengulang "akses dan pemegang akses" dua kali; sudah diganti menjadi satu kalimat dengan kurung ("Mencatat akses ke data dan informasi departemen Finance (dokumen keuangan, platform pajak dan bank) beserta pemegang aksesnya.") dan patch diuji ulang. Butir Cara pakai 1 dan 2 berpola sama ("satu baris untuk satu ..."); itu pola isian form (satu baris satu objek), jadi dipertahankan. Label "(USULAN, perlu konfirmasi konsultan)" muncul dua kali karena dua sel, itu perintah baris. Kalimat tim di sheet data tidak saya sentuh selain ejaan dan nama (T1). Tidak ada em-dash atau en-dash, tebal, tanda kutip penekanan, frasa pengisi, atau penutup generik di patch.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber. Nomor, judul, klasifikasi, revisi, status, dan tiga nama approval dari instruksi baris dan config/defaults.json. "Kana Salsabila Putri Koeswologito" dari data_conflicts (konfirmasi "selesai") dan jabatan "Finance" dari HR-JA-001 JA-10 (salinan audit); "Samuel Kristanto Utomo" dan "Direktur Utama" dari data_conflicts. "Dipta" ditulis persis seperti sumber; versi pertama menulis "Pradipta Nugraha (Accounting & Tax)", itu tafsir tanpa sumber tertulis dan sudah dicabut (open item 13). "15 Oktober 2026" adalah tanggal hari penyusunan (A4). "10 tahun" bersumber dari SOP Billing 8.2 dan SNX-FAT-SOP-04 tetapi diperluas ke daftar ini, jadi berlabel (USULAN). Nomor klausul ISO dari pengetahuan standar, berlabel USULAN dan belum dicocokkan dengan teks standar (UNMEASURED). "Finance Lead" sebagai pemilik dokumen dan peninjau tahunan adalah asumsi A1 dan USULAN 5. Kalimat Cara pakai butir 1 sampai 4 (B18 sampai B21) menunjuk pelaku Finance Staff atau Finance Lead dan larangan kata sandi, PIN, token; semuanya tidak di sumber, jadi berlabel (USULAN 4, 5, 8). Tidak ada nama, angka, atau tanggal lain.


## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| Kontrol Dokumen!B37 (Diperiksa oleh) | Finance Lead | Amirull Yusuf Zulkarnain / Direktur (A6, defaults v22) |
| Kontrol Dokumen!B16 (baru) | kosong | Definisi Finance Lead (USULAN), teks persis G-3 A6 |
| Kontrol Dokumen!B23 (baru) | kosong | Definisi Finance Staff (USULAN), teks persis G-3 A6 |

Sel B16 dan B23 tidak dibungkus teks; teks satu baris meluber ke kolom C sampai E yang kosong.

Open item: 2 diubah W9 (definisi peran ditambahkan, pemetaan tetap menunggu owner). Rujukan silang diubah: nihil.
