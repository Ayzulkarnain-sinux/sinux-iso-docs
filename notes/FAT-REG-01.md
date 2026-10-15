# Catatan penyusun FAT-REG-01: Billing & Collection Monitoring Register

Status: DRAFTED (patch + notes ada). Patch: specs/FAT-REG-01.patch.json. Mode xlsx, aksi T1 (HOLD-T3 yang dipromosikan di W0, berkas tim terbaca), nomor SNX-FAT-REG-01 (nomor lama dipertahankan), department Finance, Accounting & Tax, classification RESTRICTED (Internal), audit_class None, wave W7b. Uji terakhir, dijalankan dari /home/claude/iso-run: `python3 -I tools/xlsx_patch.py /tmp/src/FAT-REG-01.xlsx specs/FAT-REG-01.patch.json /tmp/pen-FAT-REG-01/out.xlsx` hasilnya `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: sheet AR Aging (2 data validation, 0 rumus), AP Aging (2 data validation, 8 rumus), ditambah sheet Kontrol Dokumen di posisi pertama.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 7. Billing & Collection Monitoring Register (Google Sheet) | 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ | 2026-10-14T08:07:21.851Z (get_file_metadata hari ini, cocok dengan prompt) | read_file_content dengan komentar (hasil: "No anchored comments"); download_file_content dengan exportMimeType xlsx, didekode ke /tmp/src/FAT-REG-01.xlsx (zip valid, 9088 byte); semua sheet dibaca dengan openpyxl (python3 -I) |
| Kriteria penerimaan | config/checklist.json baris 29 (checked true) | berkas ekspor checklist | Description: "Dokumen tracker untuk semua piutang dari customer". Kolom iso_9001 dan iso_27001 kosong, jadi klausul berstatus USULAN |
| Catatan cacat | context/audit/*.md | salinan audit 13 sampai 14 Okt | `grep -n 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ context/audit/*.md` tidak menemukan apa pun; lihat bagian 3 |
| Pendukung konsistensi | specs/FAT-SOP-01.json, specs/HR-ORG-01.json, config/defaults.json v21, audit FAT bagian SOP Billing dan Invoicing (fileId 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI) | | Dibaca sebagai DATA untuk nama peran, PPN, masa simpan, dan istilah |

Sheet di sumber: AR Aging (A1:M6), AP Aging (A1:N7). Tidak ada sheet Kontrol Dokumen, maka patch memakai `add_control_sheet` dari form SNX donor (out/07_Ops/SNX-OPS-FRM-01 ...xlsx) sesuai RUNBOOK §7. Tidak ada gambar, komentar sel, tautan, atau format bersyarat di sumber.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Piutang klien dicatat per invoice di sheet AR Aging dengan 13 kolom, dari Client sampai Action / notes | AR Aging A1: "Accounts Receivable Aging"; A4 sampai M4: "Client", "Invoice Number", "Invoice date", "Due date", "Date Paid ", "DPP", "PPN ", "PPh 23/22", "Amount (IDR)", "Days overdue", "Client type", "Status", "Action / notes" | 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ |
| 2 | Sheet kedua adalah utang usaha (vendor), bukan piutang klien, jadi di luar kriteria baris 29 | AP Aging A1: "Accounts Payable Aging"; L6: "Vendor"; A2: "Watch government / SOE slow-payers [tanda pisah panjang di sumber] the main cash risk at your stage. All amounts IDR." (penanda dalam kurung siku menggantikan karakter em-dash asli karena larangan em-dash) | 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ |
| 3 | Sampel AR Aging menulis dua rumus Amount per jenis klien (Enterprise menambah PPN, Gov / SOE mengurangkan PPN) dan PPN 11%; SOP Billing menulis 12% | AR Aging G5: "DPP x 11%"; I5: "DPP + PPN - PPh 23"; I6: "DPP - PPN - PPh 22". SOP Billing bagian 5.2 (salinan audit FAT, baris 119): "PPN 12%: seluruh penyerahan JKP dikenakan PPN 12%" | 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ (sheet); 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI (SOP Billing) |

Fakta lain dari berkas yang sama: AR Aging E5 dan E6 "ddmmyyy", F5 dan F6 "xxxx" (placeholder); validasi K5:K6 "Gov / SOE,Enterprise"; validasi L5:L6 "On track,At risk,Overdue,Escalate,Paid,Partially Paid"; AP Aging M6:M7 validasi "On Track,Overdue,Paid"; AP Aging B3 `=SUMIF(M6:M1000, "Paid", I6:I1000)`; AP Aging L7 "Gov / SOE" berfont putih (tidak terlihat di layar).

## 2. Isi patch (yang berubah dan alasannya)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| AR Aging baris 5 dan 6 (clear_rows) | Dua baris sampel (klien Enterprise dan Gov / SOE) dengan "ddmmyyy", "xxxx", teks rumus | Dikosongkan; header, validasi data, dan lebar kolom tetap | Data dummy; RUNBOOK §6 buang baris CONTOH |
| AR Aging!A2 | "All amounts IDR." | "Dalam IDR. Finance Staff memantau klien Gov / SOE yang lambat membayar. PPN = DPP x 12% (USULAN). Amount (IDR): Enterprise = DPP + PPN - PPh 23; Gov / SOE = DPP - PPN - PPh 22 (menunggu konfirmasi FAT)." | Menyimpan aturan dari sampel yang dikosongkan: dua rumus Amount per jenis klien dibawa persis dari I5 dan I6 dan rumus Gov / SOE diberi penanda menunggu konfirmasi (USULAN 4, Open item 13); PPN satu rumusan (USULAN 3); kalimat slow-payers dipindah dari AP, ditulis ulang dalam satu bahasa dengan pelaku Finance Staff (USULAN 8) |
| AP Aging baris 6 (clear_rows) | Nama vendor, dua tanggal, "xxxx", "DPP x 11%", "DPP x 2%", nilai 0, "Vendor" | Dikosongkan; rumus J, K, M tetap | Placeholder xxxx dan teks rumus di kolom angka; USULAN 9 |
| AP Aging!A2 | "Watch government / SOE slow-payers [em-dash] the main cash risk at your stage. All amounts IDR." | "All amounts IDR." | Kalimat itu tentang piutang, bukan utang; "at your stage" tidak menyebut apa pun tentang SINUX dan bisa ditempel ke perusahaan mana pun (RUNBOOK §6a.3) |
| Kontrol Dokumen (sheet baru, add_control_sheet) | Tidak ada | Tata letak donor; label medan tetap | RUNBOOK §7 mode xlsx |
| Kontrol Dokumen!A1, A2 | kosong | Judul; "PT Strategi Integrasi Nusantara (SINUX) · Departemen Finance, Accounting & Tax" | Instruksi penyusunan |
| B4, B5, B6 | kosong | SNX-FAT-REG-01; Billing & Collection Monitoring Register; 00 (DRAFT) | Data baris |
| B7, B31 | kosong | 15 Oktober 2026 | Tanggal penyusunan, lihat Asumsi 3 |
| B8 | kosong | Ditetapkan saat pengesahan | Tanggal efektif tidak diisi (batas keras 3) |
| B9 | kosong | RESTRICTED (Internal) | Data baris; keuangan dan pelanggan = RESTRICTED menurut defaults |
| B10 | kosong | Finance Lead | Sumber tidak punya medan "Pemilik dokumen"; aturan defaults: jabatan reviewer departemen tanpa nama (USULAN 5) |
| B11, B38 | kosong | Samuel Kristanto Utomo / President Director | defaults approved_by (USULAN 6) |
| B12, B13 | kosong | "Klausul 7.5.3, 9.1.1 (USULAN, perlu konfirmasi konsultan)"; "Annex A 5.12, 5.15, 5.33 (USULAN, perlu konfirmasi konsultan)" | USULAN 1 |
| B14 | kosong | "Minimal 10 tahun (USULAN, sama dengan berkas penagihan)" | USULAN 2 |
| B15 | kosong | "Mencatat semua piutang usaha dari klien SINUX di sheet AR Aging. Utang usaha di sheet AP Aging tidak termasuk." | Kriteria baris 29; pengecualian dari fakta 2 |
| A18 sampai B21 | kosong | Empat langkah Cara pakai, pelaku Finance Staff | Dasar tiap langkah ada di bagian 4 butir 4 |
| C31, D31, E31 | kosong | "Draft awal untuk review dan pengesahan"; Finance Staff; Menunggu | revision_desc; Disusun = prepared |
| B36, B37 | kosong | Finance Staff; Finance Lead | defaults prepared_reviewed.FAT (USULAN 5) |
| Kontrol Dokumen baris 25 dan 27 (clear_rows) | Swatch warna legenda donor (input kuning, rumus abu-abu) | Warna dikosongkan | Legenda tidak dipakai karena sheet tim tidak punya konvensi warna; teks legenda memang tidak disalin alat |

Tidak diubah: nama sheet, header kolom (termasuk spasi akhir di "Date Paid " dan "PPN "), validasi data, rumus AP Aging (J, K, M, B3, B4), AP Aging baris 7 (PPN August, nilai dipertahankan). Kolom Tanda tangan dan Tanggal di Pengesahan (C36 sampai D38) kosong. Tidak ada rujukan internal AI, kredensial, atau kode dokumen SNX lain di sel mana pun.

## 3. Penanganan cacat context/audit

grep fileId sumber ke context/audit/*.md: nol baris. Tidak ada catatan cacat khusus untuk berkas ini, jadi tidak ada bagian 5 "Catatan kualitas dan celah" untuknya. Yang saya lakukan: membaca bagian SOP Billing dan Invoicing (audit FAT) karena SOP itu menyebut register ini sebagai Lampiran 4, lalu mencocokkan butirnya ke berkas xlsx.

| # | Cacat di audit SOP Billing | Hubungan ke register | Penanganan |
|---|---|---|---|
| 4 | Tarif PPN 11% di satu bagian, 12% di bagian lain | Sampel AR memakai 11% | Sampel dikosongkan; A2 AR menulis 12% (USULAN), sejalan dengan SNX-FAT-SOP-01 butir 4.5. Konfirmasi tarif ada di Open item 5 |
| 5 | Titik awal hitungan TOP tidak konsisten (tanggal invoice, tanggal kirim, tanggal terima) | Kolom Due date tidak punya aturan hitung | Tidak diperbaiki; menentukan titik awal adalah keputusan substantif, Open item 7 |
| 8 | Tidak ada prosedur Overdue rinci dan tindak lanjut collection | Kolom Action / notes kosong tanpa petunjuk | Tidak diperbaiki; prosedurnya ada di SOP Account Receivable & Collection yang dalam peninjauan, Open item 6 dan USULAN 12 |
| 11 | Finance Lead dan Finance Staff tidak ada sebagai jabatan di HR-JA-001 | Pemilik dan pelaku langkah memakai dua peran itu | Nama peran dipakai persis seperti Matriks Peran SNX-HR-ORG-01 (status "Belum dipetakan", butir K-13). Jabatan terdekat Finance Staff adalah JA-10 Finance; Finance Lead tidak punya padanan. Tidak dipetakan sendiri, Open item 8 |
| 12 | Klasifikasi dokumen keuangan disebut Rahasia (Confidential) tetapi dokumen tidak berlabel | Sheet sumber tanpa label klasifikasi | B9 diisi RESTRICTED (Internal) sesuai defaults |
| 2, 3 | Penyusun, pemeriksa, penyetuju orang yang sama; ejaan nama Direktur Utama | Blok Pengesahan | Tiga peran berbeda (Finance Staff, Finance Lead, Samuel Kristanto Utomo / President Director); ejaan "Kristanto" |
| 1, 6, 7, 9, 10, 13, 14 | Kontrol dokumen kosong, definisi dokumen pendukung, urutan proses, lampiran hilang, lingkup, klausul, sisa LaTeX | Tidak berlaku untuk isi register | Tidak ada tindakan |

Perbaikan lintas dokumen yang berlaku: baris sampel dibuang (AR 5 dan 6, AP 6); tiga penanda tangan berbeda; PPN satu rumusan; ejaan Samuel. Tidak berlaku di berkas ini karena istilahnya tidak muncul di sheet: tiket Zammad dan GLPI, vault, kunci backup, sebutan COO, nama Fani. Tidak ada rujukan internal AI di sumber.

## 4. Asumsi

1. Register di sumber diperlakukan sebagai Format Register Penagihan dan Penjualan yang disebut sebagai Lampiran 4 di SOP Billing ("Lembar Google Sheets status tagihan, jatuh tempo (TOP 14 hari), rekonsiliasi piutang (AR)"). Kesamaan ini tidak tertulis di sumber mana pun; dasarnya hanya isi dan penomoran "7." pada nama berkas. Lihat USULAN 7.
2. Hanya sheet AR Aging yang memenuhi kriteria baris 29. AP Aging dipertahankan karena alat melarang jumlah sheet berkurang dan RUNBOOK §6 T1 meminta substansi tim dipertahankan, tetapi dikecualikan secara tertulis di Tujuan (B15).
3. Tanggal draft 15 Oktober 2026 adalah tanggal hari penyusunan (tanggal sesi), bukan tanggal dari Drive, dan bukan tanggal efektif. Tidak ada tanggal mundur.
4. Dasar tiap langkah Cara pakai (semua dari SOP Billing lewat salinan audit, pelaku Finance Staff mengikuti peran Maker di SOP itu): (1) "Update Register Penagihan: catat transaksi ke Register Penagihan dan Penjualan (AR Tracker)"; (2) "Staff Finance memperbarui Google Sheets Register Penagihan dan Penjualan secara real-time setiap perubahan status invoice"; (3) "pemantauan harian arus kas masuk via KlikBCA Bisnis" dan "memperbarui status menjadi LUNAS"; kata "mengisi Date Paid" adalah kesimpulan saya dari nama kolom, bukan kutipan; (4) "mencatat estimasi pemotongan di Register Penagihan dan merekonsiliasi saat Bukti Potong (Bupot) diterima dari klien". Langkah 4 sengaja hanya menyebut PPh 23 karena SOP tidak menyebut PPh 22.
5. Kalimat di sumber yang berbunyi perintah ("Watch government / SOE slow-payers.") adalah isi sheet untuk pengguna, bukan arahan ke penyusun. Tidak dijalankan sebagai instruksi; isinya dibawa ke AR Aging A2 sebagai kalimat Indonesia dengan pelaku Finance Staff, peran yang memantau kas masuk di SOP Billing (USULAN 8). Tidak ada kalimat lain di sumber yang ditujukan ke penyusun atau alat.
6. Baris AP Aging 7 ("PPN August") berisi nilai uang nyata, jadi dipertahankan walau berada di luar kriteria. Isinya tidak disalin ke notes ini.

## USULAN

| # | Butir | Status di berkas | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Klausul ISO 9001:2015 7.5.3 (pengendalian informasi terdokumentasi, untuk penyimpanan dan akses register) dan 9.1.1 (pemantauan dan pengukuran, untuk pemantauan piutang); ISO/IEC 27001:2022 Annex A 5.12 (klasifikasi informasi), 5.15 (kontrol akses), 5.33 (perlindungan rekaman). Checklist tidak memberi acuan. Annex A 5.33 dan pembatasan akses ke register ada di SOP Billing bagian 1.1 dan 7.1; sisanya dari praktik ISO. Label ditulis di B12 dan B13 karena tiap sel dibaca sendiri. | Diterapkan (B12, B13) | owner (meneruskan ke konsultan) |
| 2 | Masa simpan register minimal 10 tahun. Angka 10 tahun di SOP Billing bagian 8.2 berlaku untuk berkas penagihan; register tidak disebut di kalimat itu. | Diterapkan (B14) | FAT |
| 3 | PPN = DPP x 12%, mengganti 11% di sampel. | Diterapkan (AR Aging!A2) | FAT |
| 4 | Aturan Amount (IDR) per jenis klien ditulis di A2 dari sampel tim agar tidak hilang saat baris sampel dikosongkan: Enterprise = DPP + PPN - PPh 23 (I5); Gov / SOE = DPP - PPN - PPh 22 (I6). Rumus dibawa persis dari sumber dan rumus Gov / SOE diberi penanda "(menunggu konfirmasi FAT)" karena hitungannya tidak terbukti cocok dengan SNX-FAT-SOP-05 (Open item 13). | Diterapkan (AR Aging!A2) | FAT |
| 5 | Pemilik dokumen Finance Lead; Disusun Finance Staff; Diperiksa Finance Lead. | Diterapkan (B10, B36, B37, D31) | owner |
| 6 | Penyetuju Samuel Kristanto Utomo / President Director (defaults D2; pembalik: disetujui COO bila owner memutus). | Diterapkan (B11, B38) | owner atau Samuel |
| 7 | Register ini sama dengan "Register Penagihan dan Penjualan" di SNX-FAT-SOP-01, sehingga SOP itu merujuk SNX-FAT-REG-01 pada tabel rekamannya. | Diterapkan secara tersirat di Cara pakai; SOP tidak diubah (di luar bidang tulis) | FAT |
| 8 | Kalimat tim "Watch government / SOE slow-payers." dipindah dari AP Aging ke AR Aging dan ditulis ulang menjadi "Finance Staff memantau klien Gov / SOE yang lambat membayar." Pelaku Finance Staff mengikuti peran pemantau kas masuk di SOP Billing; sumber tidak menyebut pelaku kalimat itu. Bagian "the main cash risk at your stage" dibuang karena tidak bersumber. | Diterapkan (AR Aging!A2, AP Aging!A2) | FAT |
| 9 | AP Aging baris 6 dikosongkan karena memuat placeholder "xxxx". Bila baris itu data nyata, pulihkan dari Drive. | Diterapkan (clear_rows) | FAT |
| 10 | Rumus untuk Days overdue dan Status di AR Aging, seperti rumus di AP Aging. AR Aging tidak punya rumus sama sekali. | Hanya diusulkan | FAT |
| 11 | Perluas validasi data Client type dan Status di AR Aging dari K5:L6 ke baris 5 sampai 1000 (AP memakai rentang sampai 1000). | Hanya diusulkan (alat tidak menambah validasi) | FAT |
| 12 | Pindahkan sheet AP Aging ke register utang usaha tersendiri, atau hapus bila bukan bagian SINUX. | Hanya diusulkan (alat tidak menghapus sheet) | FAT |
| 13 | Petunjuk pengisian Action / notes untuk tindak lanjut invoice Overdue, ditulis setelah SOP Account Receivable & Collection selesai ditinjau. | Hanya diusulkan | FAT |
| 14 | Satu daftar Status beserta ambangnya: AR Aging "On track, At risk, Overdue, Escalate, Paid, Partially Paid"; AP Aging "On Track, Overdue, Paid"; SNX-FAT-SOP-01 butir 4.13 "Draf, Terkirim, Lunas, atau Cancel". | Hanya diusulkan | FAT |

Jumlah USULAN: 14 (sembilan diterapkan di berkas, lima hanya diusulkan).

## Open items

1. Identitas register: apakah berkas ini Lampiran 4 SOP Billing atau register berbeda dari "Register Penagihan dan Penjualan" yang dipakai SNX-FAT-SOP-01. SOP itu menyebut register dengan nama lain dan "Belum bernomor". Pemutus: FAT.
2. Sheet AP Aging (utang usaha) ada di berkas, di luar kriteria "piutang dari customer". Dipertahankan; baris 7 berisi nilai nyata. Di sumber, teks "Gov / SOE" pada L7 berfont putih sehingga tidak terlihat. Rumus aging AP menghitung usia sejak Invoice date dan terus bertambah walau baris sudah Paid. Label A3 "TOTAL" hanya menjumlahkan baris Paid. Pemutus: FAT.
3. Validasi data AR Aging hanya menutup K5:K6 dan L5:L6; baris 7 ke bawah tidak punya dropdown, padahal register harus memuat semua piutang. Days overdue dan Status di AR tanpa rumus. Alat patch tidak menambah validasi atau rumus. Format sel input (border) juga hanya ada di baris 5 dan 6. Pemutus: FAT; perbaikan alat: LEAD.
4. Tiga kosakata status (USULAN 14) dan ambang yang tidak tertulis untuk AR. Ambang AP (30, 60, 90 hari) dihitung sejak Invoice date, bukan sejak Due date, dan tidak cocok dengan TOP 14 hari di SOP Billing. Pemutus: FAT.
5. Tarif PPN 12% (USULAN) menggantikan 11% di sampel; SOP Billing sendiri menulis 11% di satu bagian dan 12% di bagian lain. Perlu konfirmasi tarif dan dasar hitungnya. Rumus Amount klien Gov / SOE dibawa seperti sumber (PPN dikurangkan); apakah itu perlakuan PPN Pemungut yang berlaku, dan apakah 11% di sampel adalah tarif efektif dengan DPP Nilai Lain atau tarif lama, perlu diputus. Pemutus: FAT.
6. Tindak lanjut invoice Overdue: SOP Account Receivable & Collection dalam peninjauan, jadi kolom Action / notes tidak diberi petunjuk dan pelakunya tidak ditulis. Pemutus: FAT.
7. Titik awal hitungan Due date (tanggal invoice, tanggal kirim, atau tanggal terima) tidak konsisten di SOP Billing dan tidak diatur di kolom Due date. Pemutus: FAT.
8. Finance Lead dan Finance Staff belum dipetakan ke jabatan di SNX-HR-ORG-01 (butir K-13); nama peran dipakai apa adanya. Pemutus: owner.
9. Batasan alat di luar bidang tulis saya: clear_rows menghapus isi dan warna tetapi tidak border, sehingga Kontrol Dokumen A25 sampai A27 tampil sebagai tiga kotak kosong bergaris (sisa swatch legenda donor), dan baris sampel AR 5 dan 6 kehilangan warna biru muda dan kuning. Fungsi tidak berubah. Keputusan LEAD: tech_fix alat atau terima.
10. Template Kontrol Dokumen tidak punya blok Dokumen terkait, jadi hubungan ke SNX-FAT-SOP-01 dan SOP Account Receivable & Collection tercatat di notes ini saja, bukan di sel. Pemutus: LEAD.
11. Tanggal draft 15 Oktober 2026 diisi penyusun dari tanggal sesi; ganti bila owner ingin tanggal lain. Pemutus: owner.
12. Nama berkas keluaran: orkestrator yang menentukan nama akhir; patch tidak memuatnya.
13. Selisih rumus Gov / SOE dengan SNX-FAT-SOP-05: rumus sampel tim "DPP - PPN - PPh 22" mengurangkan PPN dari DPP. SNX-FAT-SOP-05 (specs/FAT-SOP-05.json, baris 27 dan butir pengecualian "Transaksi dengan Instansi Pemerintah atau BUMN") hanya menyebut "PPN Pemungut (WAPU/Kode 02) atas transaksi dengan Instansi Pemerintah atau BUMN" dan penanganan khusus pada Faktur Pajak Keluaran; SOP itu tidak memuat hitungan dan tidak menyebut PPh 22. Pemeriksa membaca hitungan WAPU sebagai kas diterima = DPP - PPh 22 (invoice = DPP + PPN, PPN dipungut instansi), yang menghasilkan piutang lebih besar sebesar PPN daripada rumus sampel. Rumus sampel dipertahankan apa adanya sampai FAT memutus. Pemutus: FAT.

## Jawaban dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya tiga cacat, lalu putaran perbaikan 1 menemukan dua lagi di AR Aging A2. Cara pakai 2 berisi dua kalimat dan terpotong di sel setinggi satu baris (terlihat di hasil render LibreOffice); saya pangkas jadi satu kalimat dan kalimat tentang Overdue saya buang karena aturan status AR memang tidak ada di sumber. Langkah 4 awalnya menyebut "PPh 23/22" dengan Bukti Potong, padahal SOP hanya mengaitkan PPh 23 dengan Bukti Potong; saya persempit ke PPh 23. Tujuan awalnya memakai "hutang", yang tidak baku; saya ganti "utang" mengikuti ejaan di specs lain. Dua cacat putaran 1: A2 menyatukan rumus Amount menjadi "DPP + PPN - PPh 23/22" untuk semua klien, yang membalik perlakuan PPN klien Gov / SOE dari sumber, dan itu saya tulis seolah rumus sumber "jelas salah" padahal tanpa dasar; kini dua rumus dibawa persis dari sumber. A2 juga mencampur bahasa dan memuat kalimat perintah tanpa pelaku; kini satu bahasa dengan pelaku Finance Staff. Yang masih tersisa: nama kolom dan istilah teknis tetap berbahasa Inggris dari sumber (Amount (IDR), Gov / SOE, Enterprise), serta kata "Status" dan "status" yang berulang di Cara pakai 2 karena nama kolom dan istilah SOP sama. Tidak ada kelompok tiga, penutup positif, ekor penegas, atau kata kerja manusia untuk benda di sel yang saya tulis.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Satu tanggal: 15 Oktober 2026 (tanggal penyusunan, Asumsi 3). Angka 12% bersumber dari SOP Billing bagian 5.2 dan berlabel USULAN karena sampel sheet menulis 11%. Dua rumus Amount di A2 berasal dari sel I5 dan I6 sumber, tanpa perubahan. Pelaku Finance Staff pada kalimat pemantauan klien Gov / SOE diambil dari peran pemantau kas masuk di SOP Billing, bukan dari kalimat sumber (USULAN 8). Angka 10 tahun bersumber dari SOP Billing bagian 8.2 untuk berkas penagihan; perluasan ke register berlabel USULAN. Nomor klausul ISO berlabel USULAN; hanya Annex A 5.33 yang juga tertulis di SOP Billing bagian 1.1, yang lain dari praktik ISO. Nama peran dan penanda tangan dari config/defaults.json dan SNX-HR-ORG-01. Kesimpulan "mengisi Date Paid" di Cara pakai 3 adalah turunan dari nama kolom dan dua langkah SOP, bukan kutipan. Tidak ada nama orang, nomor izin, nilai kontrak, atau kredensial yang ditambahkan.


## Sweep

Butir 1 (AR Aging!A2): bunyi SNX-FAT-SOP-05 saya cek di specs/FAT-SOP-05.json (grep WAPU, PPh 22, DPP). Bunyinya "PPN Pemungut (WAPU/Kode 02) atas transaksi dengan Instansi Pemerintah atau BUMN" tanpa hitungan, jadi kalimat "hitungan WAPU di SNX-FAT-SOP-05 adalah DPP - PPh 22" tidak saya tulis; itu bacaan pemeriksa, bukan bunyi SOP. Rumus sumber dipertahankan dan diberi penanda "(menunggu konfirmasi FAT)". Penanda pendek karena sel A2 yang digabung berkapasitas sekitar 205 karakter (hasil render LibreOffice: 230 karakter terpotong di "lih"), dan tinggi baris tidak bisa diubah oleh alat. Agar muat, "Nilai dalam IDR." dipendekkan menjadi "Dalam IDR." (202 karakter, terlihat utuh di render). Rujukan ke SNX-FAT-SOP-05 dan bunyinya ada di Open item 13.

Butir 2 (notes): pernyataan USULAN 4 bahwa rumus itu selaras dengan PPN Pemungut di SNX-FAT-SOP-05 dibuang karena tidak terbukti. Selisihnya dicatat sebagai Open item 13 (pemutus FAT). Hal lain tidak diubah.

Uji: `python3 -I tools/xlsx_patch.py /tmp/src/FAT-REG-01.xlsx specs/FAT-REG-01.patch.json /tmp/pen-FAT-REG-01/out.xlsx` hasilnya `"pass": true`, `"fails": []`.
