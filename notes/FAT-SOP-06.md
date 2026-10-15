# Catatan penyusun FAT-SOP-06: Accounting and Financial Report

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-SOP-06.json. Mode sop, aksi T1 (HOLD-T3 yang dipromosikan di W0, wave W7b, diperlakukan sebagai improve existing), nomor SNX-FAT-SOP-06 (nomor lama dipertahankan), department "Finance, Accounting & Tax", classification "INTERNAL", audit_class None. Approval persis: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Process owner "Finance Lead" (jabatan tanpa nama). Sumber tidak punya baris "Pemilik dokumen" (isinya langsung dari Latar Belakang; tidak ada tabel kontrol dokumen, header, atau footer di teks Drive), sehingga dipakai aturan config/defaults.json process_owner: jabatan reviewer departemen.

Hasil uji terakhir (bukti mentah: /tmp/pen-FAT-SOP-06/lint.out.txt, /tmp/pen-FAT-SOP-06/validate.out.txt, /tmp/pen-FAT-SOP-06/grep-audit.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-SOP-06.json /tmp/pen-FAT-SOP-06/FAT-SOP-06.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-SOP-06/FAT-SOP-06.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "21 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- soffice ke PDF: 12 halaman. Diagram /tmp/pen-FAT-SOP-06/FAT-SOP-06_flow.png dilihat: tujuh simpul, rankdir TB, teks terbaca.
- Pemeriksaan tambahan atas spec (skrip python3 -I, tidak disimpan di repo): nol em-dash dan en-dash; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode SNX yang dirujuk di badan ada di tabel Dokumen terkait; tiap langkah paling banyak 18 kata; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir), nol "komersil", nol "hutang", nol frasa meta ("dokumen sumber", "sumber tim", "draf ini"). Kata "penyusunan" muncul hanya sebagai istilah proses (judul butir 6.5, kriteria checklist).
- tools/selftest.sh tidak dijalankan. Berkas tools, template, config, control tidak diubah. Berkas yang ditulis hanya specs/FAT-SOP-06.json dan notes/FAT-SOP-06.md; hasil render hanya di /tmp/pen-FAT-SOP-06/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 5. SOP Accounting & Financial Report (Google Doc, fileSize 5629) | 18OGetq0EsAFGDMlU2kK4-BX5-9uIGeTxWi8HWB5TPYs | 2026-10-14T10:51:01.134Z (get_file_metadata hari ini, sama dengan prompt; induk folder 1U4BP2va0dvAez_GhvMutaEf2EuLcyxrj = Dep. FAT) | read_file_content (teks penuh) dan get_file_metadata (contentSnippet untuk kutipan teks polos). Dokumen pendek: Latar Belakang, Tujuan (4 butir), Ruang Lingkup (5 kelompok), dan satu tabel proses IV (5 baris). download_file_content tidak dipakai karena struktur terbaca penuh di read_file_content dan tidak ada gambar yang disebut di teks |
| Kriteria penerimaan | config/checklist.json baris 27 | tidak berlaku | Description: "SOP ini menjelaskan proses pencatatan hingga penyusunan laporan keuangan". Kolom iso_9001 dan iso_27001 kosong |
| Catatan cacat | context/audit/*.md | salinan audit 13 sampai 14 Okt | `grep -n 18OGetq0EsAFGDMlU2kK4-BX5-9uIGeTxWi8HWB5TPYs context/audit/*.md` memberi nol baris (exit 1). Sesuai context/audit/README.md, fileId yang tidak ada di sana tidak punya catatan cacat; cacat di bagian 4 dicari sendiri dari teks Drive |
| Peran | specs/HR-ORG-01.json (DONE), config/defaults.json | repo kerja | Matriks Peran memuat "Finance Lead" dan "Finance Staff" dengan status "Belum dipetakan (K-13)"; nama peran dipakai apa adanya |
| Pembanding konsistensi (dibaca saja) | specs/FAT-SOP-01.json, FAT-SOP-04.json, FAT-SOP-05.json | repo kerja | Pola lokasi "Folder Google Drive Departemen FAT", retensi "Minimal 10 tahun", pembagian scope antar SOP FAT, definisi Piutang usaha |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Finance Staff menginput jurnal dan merekonsiliasi bank mingguan, masing-masing 1 hari dan 3 hari | Tabel IV baris 1: "Input Jurnal" / "Weekly (setiap awal minggu)" / "1 days" / "Staff". Baris 3: "Rekonsiliasi Bank" / "Weekly (setiap awal minggu)" / "3 days" / "Staff" | 18OGetq0EsAFGDMlU2kK4-BX5-9uIGeTxWi8HWB5TPYs |
| 2 | Finance Lead mereview (jurnal, rekonsiliasi bank, jurnal penyesuaian atau reklas) 2 hari, lalu tutup buku bulanan dan penyusunan Laporan Keuangan 2 hari | Tabel IV baris 4: "Review Laporan" / "Review jurnal" / "Review rekon bank statement" / "Jurnal Penyesuaian/Reklas" / "2 days" / "Lead". Baris 5: "Closing Bulanan" / "Penyusunan Laporan Keuangan" / "2 days" / "Lead" | 18OGetq0EsAFGDMlU2kK4-BX5-9uIGeTxWi8HWB5TPYs |
| 3 | Laporan Keuangan terdiri dari empat laporan dan dipakai pihak internal dan eksternal | Tujuan 4: "Menghasilkan Laporan Keuangan (Neraca, Laba Rugi, Arus Kas, dan Perubahan Ekuitas) yang valid, akuntabel, dan audit-ready, baik untuk keperluan internal (Manajemen/Pemegang Saham) maupun eksternal (Pihak Bank, Panitia Tender BUMN, dan DJP)." | 18OGetq0EsAFGDMlU2kK4-BX5-9uIGeTxWi8HWB5TPYs |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Dasar pencatatan | "SOP ini mengadopsi pencatatan accrual basis untuk memastikan bahwa setiap transaksi keuangan direkam secara real-time dan sesuai dengan Standar Akuntansi Keuangan (SAK) yang berlaku." (Latar Belakang) | Kebijakan 4.1; definisi Accrual basis, SAK. Kata "real-time" tidak dibawa, lihat bagian 4 butir D2 |
| 2 | Kebutuhan sistem pencatatan | "membutuhkan sistem pencatatan keuangan yang terstruktur, akurat, dan akuntabel" (Latar Belakang) | Bagian 11 baris rekaman 1 dan 3 ("Sistem pencatatan keuangan SINUX", nama sistem tidak disebut sumber) |
| 3 | Risiko yang dikurangi | "perbedaan interpretasi dalam penjurnalan, kesalahan input, maupun keterlambatan dalam proses tutup buku (closing) dapat diminimalisir" (Latar Belakang) | Purpose kalimat 2 (disingkat, tanpa "perbedaan interpretasi" karena tidak punya langkah pengendali) |
| 4 | Pencatatan pada CoA, nominal aktual | "dicatat pada Chart of Accounts (CoA) yang tepat dan presisi sesuai nominal aktual untuk menghindari selisih (unbalance) pada Buku Besar dan Neraca" (Tujuan 1) | Kebijakan 4.2 |
| 5 | Jadwal tutup buku | "Menetapkan jadwal dan tenggat waktu (timeline) yang tegas untuk proses rekonsiliasi dan month-end closing (tutup buku bulanan) serta year-end closing (tutup buku tahunan)." (Tujuan 2) | Kebijakan 4.3 dan 4.6; definisi Tutup buku |
| 6 | Jurnal penyesuaian | "pencatatan jurnal akrual di akhir periode, seperti pengakuan beban gaji yang masih harus dibayar, penyusutan aset tetap (server/hardware), amortisasi software, dan utang/piutang pajak" (Tujuan 3) | Kebijakan 4.5 |
| 7 | Siklus akuntansi dan batasnya | "SOP ini mencakup seluruh siklus akuntansi di PT SINUX dari awal mula terjadinya transaksi hingga terbitnya Laporan Keuangan, yang meliputi namun tidak terbatas pada:" (III) | Scope kalimat 1 ("namun tidak terbatas pada" dibuang, lihat D5) |
| 8 | Data master | "Pengelolaan dan pembaruan Chart of Accounts (CoA)." (III.1) | Scope baris 2 |
| 9 | Transaksi harian | "Pencatatan Jurnal Penerimaan dan Pengeluaran Kas/Bank (Cash Management).", "Pencatatan Pengakuan Pendapatan dan Piutang Usaha (Account Receivable).", "Pencatatan Pembelian, Biaya Operasional, dan Utang Usaha (Account Payable)." (III.2) | Scope baris 3; langkah 6.1 |
| 10 | Aset tetap | "Registrasi (Fixed Asset Register), kapitalisasi, dan perhitungan beban penyusutan aset fisik (server, kendaraan, dsb) serta amortisasi software/lisensi." (III.3) | Scope baris 4; rekaman Fixed Asset Register |
| 11 | Tutup buku | "Rekonsiliasi Bank .", "Pencatatan Jurnal Penyesuaian (Accrual, Prepaid Expense, Deferred Revenue).", "Rekonsiliasi/Ekualisasi akun komersial dengan akun perpajakan (PPN, PPh 21, PPh 22, dsb)." (III.4) | Scope baris 5; definisi Ekualisasi |
| 12 | Laporan | "Penerbitan Laporan Posisi Keuangan (Neraca).", "Penerbitan Laporan Laba Rugi.", "Penerbitan Laporan Arus Kas (Cash Flow)." (III.5) | Scope baris 6 (ditambah Perubahan Ekuitas dari Tujuan 4, lihat D3) |
| 13 | Langkah 2 | Tabel IV baris 2: "Kategorisasi" / "Klasifikasi dan Pengelolaan Chart of Account" / "1 day" / "Staff" | 6.2; SLA |
| 14 | Pengecualian pembanding (bahan USULAN, bukan sumber SOP ini) | Deskripsi checklist baris 24: "SOP ini menjelaskan proses penagihan invoice kepada customer dan pendataan piutang"; baris 25: "SOP ini menjelaskan proses pengajuan pembayaran invoice, reimbursement dan cash advance"; baris 29: "Dokumen tracker untuk semua piutang dari customer" (config/checklist.json) | Scope baris pengecualian; Dokumen terkait |
| 15 | Retensi 10 tahun (bahan USULAN, bukan sumber SOP ini) | "Retensi: minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001/ISO 27001." (SOP Billing 8.2, salinan audit FAT baris 166) | Bagian 11 tabel rekaman, semua baris (USULAN) |
| 16 | Peran | Tabel IV kolom PIC: "Staff" (baris 1 sampai 3), "Lead" (baris 4 dan 5) | Peran Finance Staff dan Finance Lead (bagian 3 ringkasan di bawah) |

## 3. Pemetaan kriteria (Description baris 27)

| Unsur kriteria | Di dokumen | Sumber |
|---|---|---|
| pencatatan | Butir 6.1 (input jurnal), 6.2 (klasifikasi pada CoA, pengelolaan CoA), 6.3 (rekonsiliasi bank); kebijakan 4.1 sampai 4.3 | Tabel IV baris 1 sampai 3; Tujuan 1; scope III.1 sampai III.2 |
| hingga penyusunan | Butir 6.4 (review dan jurnal penyesuaian) dan 6.5 langkah 1 (tutup buku bulanan) sebagai jalan ke penyusunan | Tabel IV baris 4 dan 5 |
| laporan keuangan | Butir 6.5 langkah 2 (susun Laporan Keuangan); definisi Laporan Keuangan; scope baris 6 | Tabel IV baris 5; Tujuan 4; scope III.5 |

Peta peran sumber ke HR-ORG-01 (instruksi: peran sumber yang tidak ada di sana dipetakan ke jabatan terdekat dan dicatat):

| Peran sumber | Nama di dokumen | Alasan |
|---|---|---|
| "Staff" (PIC baris 1 sampai 3) | Finance Staff | Peran departemen FAT; HR-ORG-01 Matriks Peran memuat "Finance Staff", status "Belum dipetakan (K-13)". Tidak dipetakan ke JA-10 atau JA-11 karena HR-ORG-01 sendiri tidak memetakannya |
| "Lead" (PIC baris 4 dan 5) | Finance Lead | Sama; HR-ORG-01 memuat "Finance Lead", "Belum dipetakan (K-13)". Tidak ada "Lead" tanpa keterangan di badan dokumen |
| "Manajemen" (penerima laporan, Tujuan 4) | Manajemen (istilah sumber, hanya di Purpose) | Bukan peran proses, tidak masuk bagian 5 |

Klausul ISO (checklist tidak memberi acuan, semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur |
|---|---|---|
| ISO 9001:2015 5.3 | 4.4: peran Finance Lead mereview pekerjaan Finance Staff | Bagian 5; 6.4 |
| ISO 9001:2015 7.5.3 | 4.7: arsip Laporan Keuangan, lokasi, pemilik, retensi | Tabel rekaman; 6.5 |
| ISO 9001:2015 8.1 | 4.2 dan 4.3: pencatatan pada CoA dan jadwal | 6.1 sampai 6.5; bagian 8 |
| ISO/IEC 27001:2022 Annex A 5.3 | 4.4: pembuat jurnal dan peninjau jurnal berbeda peran | 6.1 sampai 6.4 |
| ISO/IEC 27001:2022 Annex A 5.12 | 4.9: klasifikasi rekaman | Tabel rekaman |
| ISO/IEC 27001:2022 Annex A 5.15 | 4.8: pemegang akses data akuntansi | SNX-FAT-FRM-02 |
| ISO/IEC 27001:2022 Annex A 5.33 | 4.7: perlindungan rekaman | Tabel rekaman |

Nomor dan nama klausul ditulis dari ingatan penyusun tanpa membuka teks standar (tidak diukur ulang di sesi ini).

## 4. Penanganan cacat sumber

context/audit tidak punya catatan untuk fileId ini (bagian 1). Cacat berikut dicari sendiri dari teks Drive; tiap butir diperbaiki atau diberi alasan.

| # | Cacat di sumber | Penanganan |
|---|---|---|
| D1 | Penomoran judul tidak urut ("1.", "1.", "III", "IV"), sisa tanda bintang markup, kalimat "Tujuannya untuk menyediakan informasi keuangan..." di bagian IV tanpa subjek | Dipindah ke 11 bagian template; kalimat bagian IV dibuang karena mengulang Tujuan 4 |
| D2 | Latar Belakang menyebut transaksi "direkam secara real-time", tetapi tabel IV menetapkan input jurnal mingguan | Mengikuti tabel (mingguan, setiap awal minggu); "real-time" tidak dibawa; open item 4 |
| D3 | Tujuan 4 menyebut empat laporan (Neraca, Laba Rugi, Arus Kas, Perubahan Ekuitas); Ruang Lingkup III.5 hanya tiga | Empat laporan dipakai di definisi dan scope (Tujuan 4 adalah kalimat sumber); open item 5 |
| D4 | Tujuan 2 menjanjikan jadwal tutup buku tahunan, tabel IV hanya memuat tutup buku bulanan | Tidak dikarang. Kebijakan 4.6 memberi label (USULAN) dengan pelaku Finance Lead; open item 1 |
| D5 | Scope "meliputi namun tidak terbatas pada" membuka cakupan tanpa batas dan tidak menyebut pengecualian | Frasa dibuang; daftar tertutup; pengecualian ditulis dari kriteria baris dan checklist baris 24, 25, 28, 26 berlabel (USULAN); open item 8 |
| D6 | Scope III.2 diberi judul "Daily Bookkeeping" tetapi input jurnal mingguan | Judul diganti "Pencatatan transaksi" |
| D7 | Baris tabel IV "Review Laporan" berisi review jurnal dan review rekon bank, bukan review Laporan Keuangan; butir "Jurnal Penyesuaian/Reklas" tanpa kata kerja | Butir 6.4 diberi judul "Review dan jurnal penyesuaian". Kata kerja "Catat" dan pelaku Finance Lead berlabel (USULAN); open item 2 |
| D8 | "Waktu" ditulis "1 days" dan "1 day" tanpa kejelasan hari kerja atau kalender; titik awal hitung untuk baris 4 dan 5 tidak ada | "Hari" didefinisikan hari kerja (USULAN); open item 3 |
| D9 | PIC "Staff" dan "Lead" tanpa nama jabatan | "Finance Staff" dan "Finance Lead" (peta di bagian 3) |
| D10 | Kontrol dokumen kosong (nomor, versi, tanggal, pemilik, klasifikasi, pengesahan) | Diisi dari config/defaults.json dan template |
| D11 | Ejaan: "hutang", "diminimalisir", "Standardisasi", "PT SINUX" (nama badan hukum di template: PT Strategi Integrasi Nusantara) | "utang", "berkurang", "SINUX" di badan dokumen |
| D12 | Tidak ada pemisahan peninjau untuk jurnal penyesuaian bila Finance Lead yang mencatatnya (pencatat dan peninjau sama, pola yang sama dengan catatan "Disusun, Diperiksa, Disetujui oleh orang yang sama" di audit SOP Billing) | Tidak ada kontrol pengganti di sumber, jadi tidak ditulis; open item 2 |
| D13 | PPh 22 muncul di III.4 tetapi SNX-FAT-SOP-05 tidak mencantumkan PPh 22 di scope-nya | Dibawa apa adanya dari sumber; open item 6 |

Butir lintas dokumen di config/defaults.json yang tidak berlaku di dokumen ini: tiket Zammad atau GLPI, vault, rumusan PPN (dokumen ini hanya menyebut PPN sebagai nama akun pajak untuk ekualisasi), sebutan COO (tidak muncul), nama Direktur Utama (hanya di blok Approved By). Nama peran Finance Lead dan Finance Staff mengikuti data_conflicts.

## 5. Asumsi

1. Pemilik rekaman di bagian 11 = PIC langkah yang menghasilkan rekaman itu (Finance Staff untuk baris 1 dan 2, Finance Lead untuk baris 3 dan 4, dari kolom PIC tabel IV). Lokasi dan retensi seluruhnya (USULAN).
2. Tutup buku bulanan dan penyusunan Laporan Keuangan dua langkah terpisah dengan satu batas 2 hari (satu baris di tabel IV, dua kata kerja di sumber: "Closing Bulanan" dan "Penyusunan Laporan Keuangan"). Angka 2 hari ditulis di baris SLA gabungan, tidak dipecah.
3. Batas waktu butir 6.2 ditulis 1 hari, tanpa kata "setiap awal minggu" karena sumber hanya menulisnya pada baris 1 dan 3.
4. Frekuensi review (butir 6.4) tidak disebut sumber; dokumen hanya menyebut urutannya (sebelum tutup buku bulanan).
5. Diagram tanpa simpul keputusan: sumber tidak memuat cabang. Cabang selisih ada di bagian 9 sebagai (USULAN), bukan di diagram.
6. Klasifikasi dokumen INTERNAL (worklist), sedangkan rekaman berklasifikasi RESTRICTED (Internal) (USULAN, aturan keuangan = RESTRICTED di config/defaults.json), pola yang sama dengan SNX-FAT-SOP-05.

## USULAN

Dua belas butir di badan dokumen (lint menghitung 21 penanda "(USULAN)" karena sebagian butir muncul di lebih dari satu bagian).

| # | Butir USULAN | Letak | Pemutus yang disarankan |
|---|---|---|---|
| U1 | "Hari" dihitung sebagai hari kerja | Definisi; bagian 8 | FAT |
| U2 | Pengecualian scope: penerbitan invoice (SNX-FAT-SOP-01), penagihan invoice dan pendataan piutang (SOP Account Receivable & Collection, dengan tracker piutang di SNX-FAT-REG-01), persetujuan pengajuan pembayaran, pajak (SNX-FAT-SOP-05), pengarsipan dokumen keuangan (SNX-FAT-SOP-04) | Scope baris terakhir | FAT |
| U3 | Finance Lead mencatat jurnal penyesuaian dan jurnal reklasifikasi | Kebijakan 4.5; bagian 5; langkah 3 butir 6.4; diagram | FAT |
| U4 | Finance Lead menetapkan langkah, pelaku, dan batas waktu untuk tutup buku tahunan, ekualisasi pajak, dan aset tetap sebelum SOP disahkan | Kebijakan 4.6 | FAT |
| U5 | Arsip Laporan Keuangan menurut SNX-FAT-SOP-04 | Kebijakan 4.7; Dokumen terkait; rekaman | FAT |
| U6 | Pemegang akses data akuntansi dicatat di SNX-FAT-FRM-02 | Kebijakan 4.8; Dokumen terkait | FAT (akses sistem: Fani) |
| U7 | Rekaman berklasifikasi RESTRICTED (Internal) | Kebijakan 4.9 | owner |
| U8 | Finance Lead mengembalikan selisih yang belum bisa dijelaskan ke Finance Staff sebelum tutup buku bulanan | Bagian 9 baris 2 | FAT |
| U9 | Finance Lead memeriksa kepatuhan dengan membandingkan rekaman bagian 11 dengan batas waktu bagian 8 | Kesimpulan | FAT |
| U10 | Lokasi rekaman (sistem pencatatan keuangan, Folder Google Drive Departemen FAT, folder arsip FAT), pemilik, dan retensi minimal 10 tahun | Bagian 11 tabel rekaman | FAT (retensi: Legal) |
| U11 | Dua rujukan "Belum bernomor" (SOP Account Receivable & Collection, SOP Payment and Disbursement Approval) dan SNX-FAT-REG-01 sebagai batas scope | Dokumen terkait | FAT |
| U12 | Semua acuan klausul ISO 9001:2015 dan ISO/IEC 27001:2022 | Bagian 11 acuan standar; judul kebijakan 4.2 sampai 4.9 | owner (lewat konsultan) |

Di luar badan dokumen, berlabel USULAN di config/defaults.json: process_owner "Finance Lead" dan nilai prepared dan reviewed departemen FAT; pemutus: owner.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Tutup buku tahunan, ekualisasi akun komersial dengan akun perpajakan, pencatatan aset tetap dan penyusutan (kapitalisasi, ambang kapitalisasi, Fixed Asset Register) tercantum di scope tetapi tidak punya langkah atau batas waktu di sumber | FAT |
| 2 | Kata kerja dan pelaku butir "Jurnal Penyesuaian/Reklas" di tabel IV; bila Finance Lead yang mencatat, tidak ada peninjau lain atas jurnal itu | FAT; Samuel bila perlu peninjau di luar FAT |
| 3 | Titik awal hitung hari untuk baris 4 dan 5 (mis. dari akhir bulan atau dari selesainya langkah sebelumnya) dan hari kerja atau kalender | FAT |
| 4 | Input jurnal mingguan (tabel IV) versus pencatatan "real-time" (Latar Belakang): mana yang berlaku | FAT |
| 5 | Laporan Perubahan Ekuitas: ada di Tujuan 4, tidak ada di Ruang Lingkup III.5, dan tidak jelas disusun bulanan atau tahunan | FAT |
| 6 | Ekualisasi muncul di dua SOP: scope dokumen ini dan kebijakan 4.6 SNX-FAT-SOP-05 (keduanya tanpa langkah); PPh 22 hanya muncul di sini | FAT |
| 7 | Nama sistem pencatatan keuangan, persetujuan perubahan CoA, dan lokasi arsip tidak disebut sumber | FAT |
| 8 | Pengecualian scope bersifat usulan (sumber diam); belum ada keputusan tertulis apakah penagihan, persetujuan pembayaran, dan pengarsipan tetap di SOP lain | FAT |
| 9 | Pemetaan Finance Lead dan Finance Staff ke jabatan (K-13 di SNX-HR-ORG-01) | owner |
| 10 | Siapa menyetujui dan mendistribusikan Laporan Keuangan ke Manajemen, Pemegang Saham, Pihak Bank, Panitia Tender BUMN, dan DJP tidak ada di sumber; tidak ditulis | Samuel; FAT |
| 11 | Hubungan piutang yang dijurnal (butir 6.1) dengan SNX-FAT-REG-01 (tracker piutang) tidak ada di sumber; SNX-FAT-REG-01 hanya dirujuk sebagai tracker piutang di luar scope (USULAN), cakupan SOP Account Receivable & Collection tidak diubah, rekonsiliasi jurnal dengan tracker tidak ditulis | FAT |
| 12 | Acuan klausul ISO belum dicocokkan dengan teks standar | konsultan |
| 13 | Pemilik dokumen tidak tertulis di sumber; dipakai aturan jabatan reviewer departemen | owner |

## 6. Jawaban dua pertanyaan penutup

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Purpose kalimat kedua mengulang aturan kebijakan 4.2. Diperbaiki: Purpose memuat hasil yang dijaga, aturan hanya di bagian 4.
- Kebijakan 4.4 menyatakan "Finance Staff tidak mereview hasil kerjanya sendiri", kontrol yang tidak ada di sumber dan terdengar seperti kalimat audit generik. Kalimat dibuang; yang tersisa hanya pembagian review dari tabel IV.
- Judul scope "Pencatatan transaksi harian" bertentangan dengan jadwal mingguan di tabel. Diganti "Pencatatan transaksi".
- Frasa "belum punya langkah" memberi benda kata kerja manusia. Diganti "bagian 6 belum memuat langkah untuk ...".
- Kolom wewenang peran mengulang isi kebijakan 4.4. Diganti rujukan butir.

Sisa yang masih terdengar seragam: awalan "(ISO ... )" di judul kebijakan dan penanda "(USULAN)" yang berulang. Keduanya dipertahankan karena RUNBOOK §6 mewajibkan label USULAN dan pemetaan klausul di bagian 4, serta pola yang sama dipakai SNX-FAT-SOP-04 dan SNX-FAT-SOP-05. Daftar empat butir jurnal penyesuaian di 4.5 berasal dari sumber, bukan kelompok tiga yang dipaksakan. Tidak ada penutup positif generik di Kesimpulan.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Isi di dokumen | Sumber | Status |
|---|---|---|
| 1, 1, 3, 2, 2 hari; "setiap awal minggu" (baris 1 dan 3) | Tabel IV | Bersumber |
| "hari kerja" | Tidak ada | (USULAN) U1 |
| Samuel Kristanto Utomo / President Director; Finance Staff; Finance Lead | config/defaults.json | Bersumber |
| Laporan Keuangan empat jenis; penerima laporan | Tujuan 4 | Bersumber |
| PPN, PPh 21, PPh 22, server, kendaraan, hardware, software | Scope III.4, III.3, Tujuan 3 | Bersumber |
| Minimal 10 tahun | SOP Billing 8.2 (audit FAT baris 166); dipakai untuk rekaman akuntansi, lingkup yang berbeda | (USULAN) U10 |
| Folder Google Drive Departemen FAT, folder arsip FAT | SOP Billing lewat SNX-FAT-SOP-01 dan SNX-FAT-SOP-04 | (USULAN) U10 |
| "Sistem pencatatan keuangan SINUX" | Latar Belakang menyebut kebutuhan sistem pencatatan keuangan; tidak ada nama sistem | (USULAN) U10, open item 7 |
| Definisi istilah umum (Accrual, Prepaid expense, Deferred revenue, Utang usaha, Bank statement, Buku Besar, Jurnal, Jurnal reklasifikasi, Ekualisasi, Fixed Asset Register, Tutup buku) | Pengertian akuntansi umum, bukan fakta SINUX; Piutang usaha disalin dari SNX-FAT-SOP-01 | Tidak berlabel; bukan klaim tentang SINUX |
| Pemilik rekaman | PIC langkah di tabel IV | Asumsi 1 |
| Baris pengecualian di Exception: reklasifikasi oleh Finance Lead | Baris "Jurnal Penyesuaian/Reklas" di baris Lead | Bersumber, dengan pelaku berlabel U3 |
| Nomor klausul ISO | Ingatan penyusun | (USULAN) U12 |
| Tanggal | Tidak ada; Effective Date kosong | Tidak ada klaim |

## Sweep

Putaran sweep atas FAT-SOP-06 dari orkestrator WORKER-ISO-01. Yang diubah hanya dua butir di bawah; fakta, angka, nama, dan struktur lain tetap. Temuan nonblocking lain di qa/FAT-SOP-06.verify.json (judul 6.2 "Kategorisasi" dan langkah "Klasifikasikan", kata kerja langkah 6.3, titik awal hitung SLA, baris Fixed Asset Register) tidak termasuk butir sweep dan tidak diubah; titik awal hitung SLA tetap open item 3 dan Fixed Asset Register tetap dalam open item 1.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Definisi "Jurnal penyesuaian" lebih sempit dari butir 4.5 (bagian 3) | "Jurnal akhir periode untuk accrual, prepaid expense, dan deferred revenue." | "Jurnal akhir periode yang menyesuaikan saldo akun supaya beban dan pendapatan tercatat pada periode yang tepat." Daftar jenis tetap di scope dan butir 4.5, tidak disalin ke definisi |
| 1 | Scope menyebut aset tetap, ekualisasi, dan tutup buku tahunan tanpa prosedur | Butir 4.6 berlabel (USULAN), Finance Lead menetapkan langkah | Tidak diubah: gap dari sumber, sudah (USULAN) di butir 4.6, pemutus FAT (U4, open item 1) |
| 2 | Dokumen FAT yang sudah bernomor (SNX-FAT-SOP-06, SNX-FAT-REG-01, SNX-FAT-FRM-02) | Scope: "penagihan invoice dan pendataan piutang (SOP Account Receivable & Collection)"; Dokumen terkait: SOP Account Receivable & Collection "dalam peninjauan", "penagihan invoice kepada customer dan pendataan piutang"; SNX-FAT-REG-01 tidak dirujuk | Rumusan SOP Account Receivable & Collection dipertahankan persis (cakupan checklist baris 24: penagihan invoice dan pendataan piutang; tetap belum bernomor). Ditambah rujukan SNX-FAT-REG-01 sebagai tracker piutang: Scope "..., dengan tracker piutang di SNX-FAT-REG-01" dan baris Dokumen terkait baru "tracker semua piutang dari customer, rekaman pelacak piutang di luar scope SOP ini (USULAN)". SNX-FAT-FRM-02 sudah dirujuk dengan nomor (butir 4.8, Dokumen terkait). SNX-FAT-SOP-06 tidak dirujuk di badan dokumen ini |

Dua rujukan "Belum bernomor" yang tersisa (SOP Account Receivable & Collection, SOP Payment and Disbursement Approval) tidak ada di daftar dokumen yang kini bernomor, tetap "dalam peninjauan" menurut checklist baris 24 dan 25.

Perbaikan sweep (temuan pemblokir qa/FAT-SOP-06.sweep.r1.json): versi sweep pertama memindahkan "pendataan piutang" dari SOP Account Receivable & Collection ke SNX-FAT-REG-01 dan memangkas deskripsi SOP itu. Itu salah: checklist baris 24 menyebut SOP itu mencakup penagihan invoice dan pendataan piutang, dan SOP itu bukan salah satu dari tiga dokumen yang dinomori. Baris pengecualian Scope dan baris Dokumen terkait SOP Account Receivable & Collection dikembalikan ke rumusan sebelum sweep; SNX-FAT-REG-01 tinggal sebagai rujukan tracker piutang (USULAN, pemutus FAT) tanpa mencabut cakupan SOP itu. Catatan gaya nonblocking pada definisi "Jurnal penyesuaian" tidak diubah karena di luar butir perbaikan.

Hasil uji sweep setelah perbaikan (bukti: /tmp/pen-FAT-SOP-06/lint.out.txt, validate.out.txt, blankscan.out.txt): render tanpa galat; lint_doc sop `"pass": true`, fails kosong, warn "21 butir (USULAN) menunggu ACC"; validator OOXML "All validations PASSED!"; blankscan `ok`.
