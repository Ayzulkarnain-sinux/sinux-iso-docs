# Catatan penyusun ISMS-REG-01: Information Asset Register

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-REG-01.patch.json. Mode xlsx, aksi T1, nomor SNX-ISMS-REG-01 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber, audit_class C2, wave W5. Process owner = "Head of Operation" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-REG-01_Information_Asset_Register.xlsx (133130 byte) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP | 2026-10-13T06:09:35Z (get_file_metadata, dicek hari ini, sama dengan data baris) | read_file_content (teks), download_file_content (xlsx, didekode ke /tmp/src/ISMS-REG-01.xlsx, 133130 byte), 5 sheet dibuka dengan openpyxl (nilai, rumus, warna isi, data validation, conditional formatting), gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/checklist.json baris 78 | Description hanya nama berkas | Kriteria = substansi sumber + acuan ISO 9001:2015 "7.1.3" dan ISO/IEC 27001:2022 "5.9, 5.10, 5.11, 5.12" |
| Pembanding (bahan): SNX-ISMS-SOP-04_SOP_IT_Asset_Configuration_Management.docx | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg | tidak diukur (hanya dibaca lewat read_file_content hari ini) | Dibaca untuk menutup cacat masa simpan Pemusnahan dan pemetaan 5.10 dan 5.11 |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md baris 1119 sampai 1295 (bagian 5 Catatan kualitas dan celah di baris 1285 sampai 1293) | salinan audit 13 Okt 2026 | DATA, dibandingkan dengan xlsx asli |

Lima sheet di sumber: Kontrol Dokumen, Alur Proses, Daftar, Register Aset, Pemusnahan. Sheet "Kontrol Dokumen" ada, jadi diselaraskan lewat `set`; tidak ada sheet yang ditambah. Sel pengesahan ada di B37 sampai B39 (bukan B36 sampai B38 seperti workbook OPS lain), diperiksa langsung di berkas.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Head of Operation | "Pemilik dokumen" / "Head of Operation" (Kontrol Dokumen!A10, B10) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |
| Nilai aset diambil dari nilai tertinggi C, I, A; kritikalitas tiga tingkat | "Nilai aset = nilai tertinggi dari C, I, A. Kritikalitas: 3 Tinggi, 2 Sedang, 1 Rendah." (Register Aset!A2) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |
| Review aset tiap 6 bulan dan aset baru didaftarkan paling lambat saat mulai dipakai | "Review berikutnya dihitung otomatis 6 bulan setelah review terakhir; baris merah berarti review terlambat." (Kontrol Dokumen!B21) dan "Daftarkan setiap aset baru paling lambat saat mulai dipakai; aset pelanggan wajib sebelum gate G3." (B18) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Lokasi |
|---|---|---|---|
| 1 | Skala C, I, A | "Isi nilai C, I, A dengan skala 1 (rendah) sampai 3 (tinggi); nilai dan kritikalitas aset dihitung otomatis." | Kontrol Dokumen!B19 |
| 2 | Tanda CI | "Tandai CI = Ya untuk aset yang konfigurasinya dikendalikan dan isi acuan baseline." | Kontrol Dokumen!B20 |
| 3 | IP address boleh, kredensial dilarang | "IP address dan detail teknis sensitif boleh dicatat di sini karena register berklasifikasi RESTRICTED; kredensial dilarang." | Kontrol Dokumen!B22 |
| 4 | Rumus nilai, kritikalitas, review berikutnya | `=IF(COUNT(I5:K5)=0,"",MAX(I5:K5))`, `=IF(L5="","",CHOOSE(L5,"Rendah","Sedang","Tinggi"))`, `=IF(T5="","",EDATE(T5,6))` | Register Aset!L5, M5, U5 (baris 5 sampai 216) |
| 5 | Sel Review berikutnya merah hanya bila lewat tanggal dan status Aktif | `AND($U5<>"",$U5<TODAY(),$R5="Aktif")` (conditional formatting U5:U216) | Register Aset |
| 6 | Pemusnahan dicatat di sheet sendiri | "Setiap pemusnahan media atau dekomisi aset dicatat di sini dan status aset di Register Aset diubah menjadi Dimusnahkan." | Pemusnahan!A2 |
| 7 | Metode pemusnahan | "Overwrite atau secure erase,Penghancuran fisik,Crypto erase,Penghapusan VM sesuai kontrak" (data validation E5:E44) | Pemusnahan |
| 8 | Masa simpan berita acara 5 tahun (di dokumen lain) | "Berita acara pemusnahan | Lampiran SNX-ISMS-REG-01 | 5 tahun" | SNX-ISMS-SOP-04 bagian 8, fileId 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |
| 9 | Penggunaan yang dapat diterima (5.10) dan pengembalian aset (5.11) diatur di SOP-04 | "6.2 Penggunaan yang dapat diterima (A 5.10)" dan "6.4 Pengembalian aset (A 5.11)" | SNX-ISMS-SOP-04, fileId 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |

## 3. Hasil uji

Perintah: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-REG-01.xlsx specs/ISMS-REG-01.patch.json /tmp/pen-ISMS-REG-01/out.xlsx`

Hasil: `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 5 sheet, 1 gambar (Alur Proses), data validation 0/0/0/9/1, conditional formatting 0/0/0/3/0, rumus 636 di Register Aset (L, M, U untuk baris 5 sampai 216). Berkas hasil terbuka di LibreOffice (konversi ke PDF berhasil). Pemindaian teks semua sel hasil: tidak ada em-dash, en-dash, kata CONTOH, SKILL_, DOCTRINE, DEC-, HANDOVER, Claude, Altair, kb_anchor. lint_doc.py hanya untuk docx, jadi pemindaian itu saya jalankan manual dengan pola yang sama.

## 4. Isi patch dan alasannya

| Sel atau baris | Sebelum | Sesudah | Alasan |
|---|---|---|---|
| Register Aset baris 5 sampai 16 | 12 aset AST-001 sampai AST-012, semua Catatan "CONTOH", Review terakhir 13 Okt 2026 | dikosongkan (clear_rows); rumus L, M, U tetap; warna isian ikut baris 17 | RUNBOOK §6 buang baris CONTOH; sumber sendiri menyebut pemilik dan status harus diverifikasi |
| Kontrol Dokumen baris 23 | "6. Baris CONTOH (biru muda) adalah aset internal yang teridentifikasi dari knowledge base; verifikasi pemilik dan statusnya." | dikosongkan | baris CONTOH sudah tidak ada; butir 1 sampai 5 tetap berurutan |
| Kontrol Dokumen baris 27 | legenda "Baris CONTOH: hapus atau timpa saat dipakai" | dikosongkan (teks dan warna) | idem |
| Kontrol Dokumen baris 33 | revisi 00 kedua, tanggal sama, menyebut "keselarasan RTO dan target pulih" | dikosongkan | duplikat; frasa RTO tidak berkaitan dengan isi workbook |
| Kontrol Dokumen B11 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by (D2) |
| Kontrol Dokumen B13 | "Klausul atau kontrol Annex A 5.9, 5.10, 5.11, 5.12" | "Kontrol Annex A 5.9, 5.10, 5.11, 5.12" | semua butir adalah kontrol Annex A; angka sama dengan acuan baris |
| Kontrol Dokumen B14 | "Berlaku sampai digantikan" | "Register Aset: berlaku sampai digantikan. Berita acara di sheet Pemusnahan: 5 tahun (SNX-ISMS-SOP-04)." | cacat audit nomor 7; angka dari SNX-ISMS-SOP-04, lihat open item 11 |
| Kontrol Dokumen C32 | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| Kontrol Dokumen B37 | "Head of Operation" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared, dan instruksi baris |
| Kontrol Dokumen B38 | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults reviewed, dan instruksi baris |
| Kontrol Dokumen B39 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |

Tidak diubah, sudah selaras dengan data baris: Nomor SNX-ISMS-REG-01, Judul, Revisi "00 (DRAFT)", Tanggal draft "13 Oktober 2026" (tanggal dari sumber, bukan tanggal efektif), Tanggal efektif "Ditetapkan saat pengesahan", Klasifikasi RESTRICTED (Internal), Pemilik dokumen Head of Operation, Acuan 9001 "Klausul 7.1.3", Tujuan, Cara pakai butir 1 sampai 5, legenda sel input dan sel rumus, kolom Tanda tangan dan Tanggal kosong, Disusun "Divisi Operation" dan Disetujui "Menunggu" pada riwayat revisi. Sheet Daftar, Pemusnahan, dan gambar Alur Proses tidak disentuh. Legenda Alur Proses!A2 cocok dengan gambar (garis putus-putus dari Berita acara kembali ke alur utama), jadi tidak diubah.

Sebutan COO: setelah B11 dan B39 diganti, workbook tidak lagi menyebut COO, jadi aturan "Direktur (COO)" tidak terpakai. Direktur Utama hanya muncul di blok pengesahan sebagai "President Director". Zammad, GLPI, vault, dan PPN tidak tersisa di workbook sesudah baris CONTOH dikosongkan; tidak ada yang ditambahkan.

## 5. Penanganan cacat context/audit (bagian 5, fileId 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Semua 12 baris bertanda CONTOH, belum ada aset terverifikasi | Diperbaiki: baris dikosongkan. Daftar kandidat disimpan di bagian 6 untuk Ops. Lihat open item 1 |
| 2 | Hanya 12 aset; empat jenis di Daftar tidak terpakai; tidak ada aset milik pelanggan sebagai baris sendiri | Hilang bersama data contoh. Daftar jenis tidak diubah: itu pilihan dropdown tim. Pengisian aset pelanggan menjadi bagian open item 1 |
| 3 | Kolom Tanggal masuk kosong di semua baris | Hilang bersama data contoh. Kolom tetap ada sebagai isian |
| 4 | Acuan baseline "Belum ada" pada AST-003, 006, 009 padahal CI = Ya | Hilang bersama data contoh. Dicatat di bagian 6 supaya Ops mengisi acuan baseline saat mendaftar ulang |
| 5 | AST-010 Cloudflare (SECRET, nilai 3) Backup dan CI "Tidak"; AST-011 Google Workspace (nilai 3) Backup dan Monitoring "Tidak" | Hilang bersama data contoh. Dicatat di bagian 6; keputusan isi ada di Ops (open item 1) |
| 6 | Pemilik AST-005 "Tech dan Product" adalah nama fungsi, bukan peran | Hilang bersama data contoh. Open item 2 |
| 7 | Sheet Pemusnahan kosong; SOP-04 bagian 8 menyebut berita acara "5 tahun" sebagai lampiran REG-01, tetapi B14 hanya "Berlaku sampai digantikan" | Diperbaiki di B14 (angka dari SOP-04, konfirmasi di open item 11). Sheet Pemusnahan dibiarkan kosong (isian faktual per kejadian) |
| 8 | Tanda tangan, tanggal pengesahan, status "Menunggu" kosong; penyusun "Head of Operation", pemeriksa "ISO/ISMS Coordinator" dua penamaan berbeda | Tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Nama diisi dari defaults; tiga penanda tangan kini berbeda |
| 9 | Riwayat revisi dua baris rev 00 bertanggal sama | Diperbaiki: satu baris, deskripsi dari data baris |
| 10 | 5.12 Klasifikasi: nilai dropdown "RESTRICTED" dibanding tingkat "RESTRICTED (Internal)" (temuan saya, bukan dari audit) | Tidak diubah, USULAN 2 |

## 6. Daftar kandidat aset dari 12 baris CONTOH (bahan untuk Ops, bukan isi dokumen)

Nilai persis dari sumber. Kolom: ID, nama aset, pemilik, klasifikasi, C/I/A, CI, Backup, Monitoring.

| ID | Nama aset | Pemilik | Klas. | C/I/A | CI | Backup | Mon. |
|---|---|---|---|---|---|---|---|
| AST-001 | Password manager internal (vault.sinux.co.id) | Head of Operation | SECRET | 3/3/3 | Ya | Ya | Ya |
| AST-002 | SINUX Service Hub GLPI (ticket.sinux.co.id) | Head of Operation | RESTRICTED | 2/2/2 | Ya | Ya | Ya |
| AST-003 | Helpdesk Zammad Nusagrid | Lead NOC | RESTRICTED | 2/2/3 | Ya | Ya | Ya |
| AST-004 | Jumphost multi-customer | Head of Operation | SECRET | 3/3/3 | Ya | Ya | Ya |
| AST-005 | AegisWAF edge | Tech dan Product | RESTRICTED | 2/3/3 | Ya | Ya | Ya |
| AST-006 | Monitoring Nusametric dan Overseer | Lead NOC | RESTRICTED | 2/2/3 | Ya | Ya | Ya |
| AST-007 | Acronis Cyber Protect (console dan repository) | Lead NOC | SECRET | 3/3/3 | Ya | Ya | Ya |
| AST-008 | Knowledge base SINUX dan database pendukung | COO | RESTRICTED | 3/3/2 | Ya | Ya | Ya |
| AST-009 | Server email mail.nusagrid.co.id | Lead NOC | RESTRICTED | 3/2/2 | Ya | Ya | Ya |
| AST-010 | Akun Cloudflare | Head of Operation | SECRET | 3/3/3 | Tidak | Tidak | Ya |
| AST-011 | Google Workspace sinux.co.id | COO | RESTRICTED | 3/2/2 | Tidak | Tidak | Tidak |
| AST-012 | Laptop kerja personel Operation | Head of Operation | RESTRICTED | 2/2/2 | Tidak | Tidak | Tidak |

Kolom Acuan baseline di sumber untuk AST-002, 005, dan 007 berisi nama berkas internal AI (huruf besar dengan garis bawah dan awalan SKILL). Nama itu terlarang di dokumen (RUNBOOK §0 butir 6) dan sengaja tidak disalin ke sini; Ops mengisi acuan baseline dengan nama runbook yang benar.

## USULAN

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Kata "baris merah" di Kontrol Dokumen!B21 dan di gambar Alur Proses tidak cocok dengan aturan warna: yang merah hanya sel Review berikutnya, dan hanya bila status Aktif. Usulan ganti jadi "sel Review berikutnya berwarna merah bila tanggalnya lewat dan status Aktif". Tidak saya ubah karena gambar tidak bisa disunting alat dan teks sel akan berbeda dari gambar | Fani |
| 2 | Dropdown Klasifikasi (Daftar!B4) berisi "RESTRICTED", sedangkan tingkat SNX-ISMS-PRO-01 dan label dokumen berbunyi "RESTRICTED (Internal)". Usulan samakan nilainya sekaligus aturan warna kolom H (yang mencocokkan teks "RESTRICTED"), supaya warna kuning tidak hilang | Fani |

## Open items

| # | Butir | Pemutus atau pelaksana |
|---|---|---|
| 1 | Register Aset kini kosong: 12 aset kandidat (bagian 6) dihapus karena bertanda CONTOH. Ops memverifikasi pemilik, klasifikasi, C/I/A, CI, Backup, Monitoring, lalu mengisi ulang. Sebelum dipakai audit, isi harus ada; kandidat AST-010 dan AST-011 bernilai 3 tetapi Backup "Tidak". Aset pelanggan belum ada satu baris pun (Cara pakai butir 1: wajib sebelum gate G3) | Fani (Ops mengisi) |
| 2 | Pemilik aset AST-005 ditulis "Tech dan Product" (nama fungsi). Saat diisi ulang, pakai nama peran dari Struktur Organisasi (HR-ORG-01); peran yang sudah ada di sana antara lain Head of Operation dan Lead NOC | Fani |
| 3 | Vault: kandidat AST-001 menulis vault.sinux.co.id. Sesuai aturan vault, statusnya "menunggu konfirmasi Ops"; tidak ada baris vault di dokumen sekarang | Ops (Fani) |
| 4 | Tiket: kandidat AST-002 (GLPI, "Tiket GMF dedicated dan permintaan internal") dan AST-003 (Zammad, "Tiket pelanggan Nusagrid (WhatsApp, telepon)"). Batas "generalist" untuk GLPI belum dirinci owner, jadi pembagian dua sistem ini belum bisa dipastikan dari sumber | owner |
| 5 | Pemetaan acuan 5.10 dan 5.11: workbook ini tidak punya kolom pemakaian wajar atau pengembalian aset. Di SNX-ISMS-SOP-04 kedua kontrol itu ada (6.2 dan 6.4). Konfirmasi bahwa acuan 5.10 dan 5.11 di Kontrol Dokumen REG-01 cukup lewat SOP-04, atau tambah kolom (alat xlsx tidak bisa menambah kolom) | Fani, konsultan SoA |
| 6 | Hubungan Head of Operation (pemilik dokumen dan pemilik banyak aset) dengan VP Tech Operation and Services belum ditetapkan di Struktur Organisasi (butir K-09 di spec HR-ORG-01). Pemilik dokumen tetap "Head of Operation" mengikuti sumber | owner |
| 7 | Tidak ada sel untuk masa tinjau dokumen (YEARLY) di Kontrol Dokumen, jadi nilai itu tidak tercetak. Review aset 6 bulan (aturan tim, formula EDATE) dipertahankan; SOP-04 6.6 menyebut review pemilik aset minimal semester, sejalan | Fani |
| 8 | "gate G3" tidak dijelaskan di workbook (Checklist G3 ada di SNX-OPS-FRM-06). Kode itu tidak saya tambahkan ke B18 supaya kalimat tim utuh dan tidak muncul rujukan baru tanpa tabel dokumen terkait | Fani |
| 9 | Kosmetik: legenda warna sekarang punya satu kotak abu tanpa label (baris 27, hasil clear_rows menyalin warna baris 28). Menyatu dengan kotak abu berlabel "Sel rumus" di bawahnya | tech_fix alat bila dianggap mengganggu |
| 10 | Tidak ada kalimat di sumber yang ditujukan ke agen. Kalimat "hapus atau timpa" dan "verifikasi pemilik dan statusnya" adalah petunjuk untuk pengguna workbook, ditangani lewat pengosongan baris CONTOH | nihil |
| 11 | Kontrol Dokumen!B14 memuat "5 tahun" untuk berita acara di sheet Pemusnahan. Angka itu bersumber dari SNX-ISMS-SOP-04 bagian 8 (dibaca di Drive), bukan dari REG-01 sendiri. Lingkupnya sama (berita acara pemusnahan), jadi dipakai tanpa label USULAN. Ops mengonfirmasi bahwa 5 tahun berlaku untuk sheet ini, lalu SOP-04 dan REG-01 tetap seragam saat SOP-04 dirender | Fani |

## Jawaban dua pertanyaan pemeriksaan

1. Apa yang membuat teks ini terdengar buatan AI. Teks yang saya tulis hanya tujuh nilai sel dan satu kalimat baru (B14). Kalimat B14 memakai pola "X: Y. Z: W." yang agak mekanis, tetapi isinya dua fakta dengan satu rujukan dan tidak ada kata pengisi, penegasan, atau penutup. Asal angka 5 tahun tidak dijelaskan di sel; cukup di open item 11. Kalimat Cara pakai, legenda, dan label tim tidak saya sentuh (T1). Tidak ada em-dash atau en-dash di patch; tanda "·" di subjudul adalah penyekat milik tim.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber. Erik, Fani, dan Samuel dari config/defaults.json. "5 tahun" dari SNX-ISMS-SOP-04 bagian 8, dibaca dari Drive hari ini (fileId di atas); angka itu bukan dari REG-01 sendiri, jadi konfirmasinya dicatat di open item 11. "13 Oktober 2026" dan "00 (DRAFT)" tetap dari sumber. Tidak ada nama, tanggal, atau angka baru lain. Tidak ada perbaikan teks yang diperlukan setelah pemeriksaan ini.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan".
Disunting: Tujuan, Cara pakai 1 sampai 5, dan catatan Pemusnahan A2. Catatan Register Aset A2 dipertahankan (T1).
Cara pakai 5: "kredensial dilarang" menjadi "Kredensial tidak boleh dicatat"; arti tetap.
