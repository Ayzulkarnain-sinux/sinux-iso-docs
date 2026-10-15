# Catatan penyusun FAT-RPT-02: FAT Nonconformity & Corrective Action

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-RPT-02.json. Mode generic, aksi T2, wave W7, nomor SNX-FAT-RPT-02 (nomor lama dipertahankan), department "Finance, Accounting & Tax", classification "RESTRICTED (Internal)", audit_class None. doc_type_cover "REPORT", doc_type_label "Report". Approval persis dari config/defaults.json: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Finance Lead" (jabatan tanpa nama): dokumen tanpa sumber memakai aturan config/defaults.json process_owner, yaitu jabatan reviewer departemen.

Hasil uji terakhir (bukti mentah: /tmp/pen-FAT-RPT-02/lint.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-RPT-02.json /tmp/pen-FAT-RPT-02/FAT-RPT-02.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-RPT-02/FAT-RPT-02.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "15 butir (USULAN) menunggu ACC". Lulus pada putaran render pertama; tiga putaran berikutnya hanya memperbaiki lebar kolom dan kalimat (lihat bagian 8).
- soffice ke PDF: 12 halaman. Tabel 1 sampai 4 dilihat per halaman sebagai gambar; kata header tidak terpotong di tengah sesudah putaran 3 (judul kolom "Ketidaksesuaian" di Tabel 3 diganti "Persyaratan yang Tidak Terpenuhi" supaya muat; "Target Penyelesaian" diganti "Target Selesai").
- Pemeriksaan tambahan atas spec (skrip python3 -I, tidak disimpan di repo): nol em-dash dan en-dash; nol kutip dan tanda tebal; nol frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, hulu ke hilir); nol frasa meta proses (dokumen sumber, sumber tim, penyusun, draf ini); nol kata "tim"; "Lead" selalu "Finance Lead"; semua kode SNX di badan (SNX-FAT-SOP-01, 04, 05, 06, SNX-HR-ORG-01, SNX-ISMS-PRO-01) ada di bagian Dokumen Terkait; nol "hambatan" atau "dukungan" (satu istilah: bottleneck dan support).
- tools/selftest.sh tidak dijalankan. Berkas tools, template, config, control, reference, ledger.json, out, qa tidak diubah. Berkas yang ditulis hanya specs/FAT-RPT-02.json dan notes/FAT-RPT-02.md; hasil render hanya di /tmp/pen-FAT-RPT-02/. Skrip pembuat spec ada di folder scratchpad sesi, bukan di repo.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Tidak ada sumber untuk dokumen ini (T2, checklist tanpa link) | tidak ada | tidak berlaku | Struktur kolom dan petunjuk pengisian saja; sel data faktual kosong; tanpa baris contoh |
| Checklist ISO SINUX - 2026 (kriteria baris 33) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (get_file_metadata hari ini; sama dengan config/checklist.json) | read_file_content (teks penuh): baris "FAT Nonconformity & Corrective Action Records." kolom Checklist FALSE, Description sama dengan config/checklist.json baris 33, kolom Link kosong |
| 1. SOP Billing and Invoicing (satu-satunya sumber tim yang menyebut log ketidaksesuaian) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI | 2026-10-14T08:06:56.942Z (get_file_metadata hari ini; induk folder Dep. FAT 1U4BP2va0dvAez_GhvMutaEf2EuLcyxrj) | read_file_content (teks penuh), dibuka untuk menyalin kutipan verbatim bagian 7.2 dan 7.1 |
| Peran dan matriks peran | specs/HR-ORG-01.json (DONE) | repo kerja | Matriks Peran: Finance Lead dan Finance Staff "Belum dipetakan (K-13)"; Direktur Utama = JA-01 |
| Pembanding konsistensi (dibaca saja, di luar sumber) | specs/FAT-SOP-01.json, FAT-SOP-04.json, FAT-SOP-05.json, LEG-RPT-01.json | repo kerja | Nomor butir yang dirujuk (4.4, 4.8, 4.11, 4.14, 6.1, 4.2, bagian 8), nama peran, dan pola tabel laporan |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kriteria penerimaan: log sheet, proses FAT, bottleneck, dan perlu support | Kolom Description, baris dokumen "FAT Nonconformity & Corrective Action Records.": "Dokumen berisi log sheet proses FAT yang bottleneck dan perlu support" | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| 2 | Log ketidaksesuaian sudah dikenal di SOP Billing, dengan evaluasi bulanan; wadah dan lokasinya tidak ditetapkan | Bagian 7.2: "Seluruh riwayat pembatalan dan revisi wajib dicatat dalam log ketidaksesuaian sebagai bahan evaluasi kendali mutu bulanan." | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| 3 | Contoh support yang bisa menahan tahap: persetujuan tertulis Direktur Utama atas TOP di atas standar (sumber menulis CEO, Samuel Utomo) | Bagian 5.3: "Penetapan TOP di atas 14 hari kalender wajib mendapatkan persetujuan tertulis dari CEO (Samuel Utomo) sebelum PKS atau PO disepakati." | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Akun portal pajak dan internet banking memakai 2FA dan tidak dibagikan | Bagian 7.1 SOP Billing (tanda tebal sumber dibuang): "Akun portal CoreTax DJP dan KlikBCA Bisnis wajib menggunakan Otentikasi Dua Faktor (2FA) dan tidak boleh dibagikan kepada pihak yang tidak berkepentingan." | Ketentuan butir 13 |
| 2 | Project Manager menyediakan dokumen pendukung penagihan | Bagian 6.1 SOP Billing: "Project Manager mengajukan permohonan penagihan ke Tim Finance dengan melampirkan BAST yang sudah ditandatangani, acuan PO, PKS, dan mengonfirmasi bahwa data master klien pada Master Sales Sheet / Google Form sudah terisi lengkap." | Peran, baris Pemberi support (butir 6.1 SNX-FAT-SOP-01) |
| 3 | Data master klien dipasok oleh peran penjualan (di SNX-FAT-SOP-01 dipetakan ke Business Development, USULAN di sana) | Bagian 4.1 SOP Billing: "Mengunggah dan memperbarui detail transaksi, acuan PO/PKS, serta kelengkapan data master klien tersebut ke dalam Master Sales Sheet secara rutin sebagai rujukan Tim Finance." | Peran, baris Pemberi support (butir 4.2 SNX-FAT-SOP-01) |
| 4 | Batas waktu tahap pajak 1 hari per tahap | Kutipan dari catatan FAT-SOP-05 (sumber SOP Tax, fileId 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87, tidak dibuka ulang hari ini): Tabel IV baris 3, sel Waktu "1 day", sel PIC "Lead"; baris lain juga "1 day" | Ketentuan butir 6 (rujukan SNX-FAT-SOP-05 bagian 8) |
| 5 | Tiket: Zammad untuk Ops, GLPI untuk generalist; GLPI = SINUX Service Hub; batas generalist belum dirinci | config/defaults.json ticketing: "Kata owner 14 Okt: \"sistem tiket zammad untuk ops, glpi untuk generalist\". GLPI = SINUX Service Hub. Batas lingkup 'generalist' belum dirinci owner" | Ketentuan butir 4; Istilah GLPI |
| 6 | Pengevaluasi log ketidaksesuaian SOP Billing = Finance Lead, tiap bulan; pencatat = Finance Staff | Dari spec FAT-SOP-01 butir 4.14: "Finance Staff mencatat riwayat pembatalan dan revisi invoice di log ketidaksesuaian. Finance Lead mengevaluasi log itu setiap bulan sebagai bahan kendali mutu." | Ketentuan butir 12 dan 15 (pola pencatat dan penetap) |
| 7 | Batas wewenang keuangan mengikuti delegasi tertulis | specs/HR-ORG-01.json, Matriks Peran: "Batas wewenang semua jabatan: keputusan keuangan, legal, perubahan kontrak, pengangkatan atau pemutusan hubungan kerja, dan perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | Peran, kolom Wewenang Finance Lead |

## 3. Pemetaan kriteria (Description baris 33)

| Unsur kriteria | Di dokumen |
|---|---|
| log sheet | Bagian Isi Log: Tabel 1 (log), Tabel 2 (tindak lanjut dan status), Tabel 3 (ketidaksesuaian dan tindakan korektif), Tabel 4 (tinjauan bulanan); satu catatan = baris bernomor sama di Tabel 1 sampai 3 |
| proses FAT | Ruang Lingkup: enam proses FAT dari checklist baris 23 sampai 28 (Billing & Invoicing, Account Receivable & Collection, Payment and Disbursement Approval, Financial Document Control & Retention, Accounting and Financial Report, Tax Administration & Reporting); kolom Proses FAT di Tabel 1 |
| bottleneck | Istilah Bottleneck; Ketentuan butir 1; kolom Tahap yang Tertahan, Uraian Bottleneck, Tanggal Dicatat, Tanggal Tahap Berlanjut |
| perlu support | Istilah Support; kolom Support yang Diperlukan, Diminta kepada (Tabel 1), Tanggal Support Diminta dan Diterima (Tabel 2); peran Pemberi support; pengecualian bottleneck yang selesai tanpa support |
| judul "Nonconformity & Corrective Action" (di luar Description, dari judul baris) | Tabel 3 dan Tabel 4, dibatasi ke ketidaksesuaian yang timbul dari bottleneck (open item 2) |

## 4. Klausul ISO (checklist tidak memberi acuan; satu label di bagian Acuan ISO: "(USULAN, perlu konfirmasi konsultan)")

| Standar | Klausul | Dasar pemilihan |
|---|---|---|
| ISO 9001:2015 | 10.2 Ketidaksesuaian dan tindakan korektif | Isi Tabel 3 (ketidaksesuaian, penyebab, tindakan, hasil verifikasi) |
| ISO 9001:2015 | 7.1.1 Sumber daya, umum | Tabel 1 dan 2 mencatat support yang diperlukan agar proses berjalan |
| ISO 9001:2015 | 7.5.3 Pengendalian informasi terdokumentasi | Lokasi, pemilik, retensi dokumen terisi |
| ISO/IEC 27001:2022 | 10.2 Ketidaksesuaian dan tindakan korektif | Tabel 3, termasuk tindakan yang menyangkut kontrol keamanan informasi |
| ISO/IEC 27001:2022 | Annex A 5.33 Perlindungan rekaman | Retensi dan perlindungan dokumen terisi |
| ISO/IEC 27001:2022 | Annex A 5.12 Klasifikasi informasi | Klasifikasi RESTRICTED (Internal) |

Nomor dan nama klausul berasal dari standar, ditulis dari ingatan penyusun tanpa membuka teks standar; tidak diukur ulang. Konsultan perlu mengonfirmasi (open item 8).

## 5. Penanganan cacat context/audit

Perintah: `grep -n "FAT Nonconformity & Corrective" context/audit/*.md`. Hasil: satu baris saja, di context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 756 ("13. FAT Nonconformity & Corrective Action Records."), yaitu butir daftar permintaan konsultan departemen FAT. Tidak ada bagian dokumen, fileId, maupun bagian 5 "Catatan kualitas dan celah" untuk dokumen ini, karena belum ada berkas sumbernya. Cacat tercatat pada dokumen FAT terdekat (SOP Billing dan SOP Tax, context/audit/iso-sinux-supdocs-fat-2026-10-14.md bagian 5) dinilai satu per satu terhadap dokumen ini:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Billing butir 1: kontrol dokumen kosong | Tidak berlaku ke dokumen ini; nomor SNX-FAT-RPT-02, Draft, revisi 00, tanggal dan tanda tangan kosong |
| 2 | Billing butir 3: sebutan CEO lawan Direktur Utama, ejaan Samuel | Badan dokumen memakai "Direktur Utama"; blok Approval "Samuel Kristanto Utomo / President Director" dari defaults; kutipan sumber yang memakai "CEO" hanya ada di notes ini |
| 3 | Billing butir 4: PPN 11% lawan 12% | Dokumen tidak menulis tarif PPN, jadi tidak ada rumusan PPN |
| 4 | Billing butir 5: titik awal TOP tidak konsisten | Dokumen tidak menyatakan titik awal TOP; Istilah TOP merujuk SNX-FAT-SOP-01 butir 4.8 |
| 5 | Billing butir 8: tanpa SLA waktu per tahap dan tanpa prosedur Overdue rinci | Tidak ada angka karangan: dokumen tidak menetapkan batas waktu pemberian support (open item 5). Tindak lanjut Overdue masuk proses Account Receivable & Collection, yang tercantum di Ruang Lingkup sebagai salah satu enam proses |
| 6 | Billing butir 11 dan Tax butir 6: Finance Lead tunggal tanpa pengganti; Finance Lead dan Finance Staff bukan jabatan di Job Analysis | Nama peran dipakai apa adanya dan dicatat "Belum dipetakan (K-13)" di Peran dan Dokumen Terkait. Kontrol pengganti tidak ditulis karena sumber diam (open item 4) |
| 7 | Billing butir 12: klasifikasi dokumen tidak berlabel | Dokumen ini berlabel RESTRICTED (Internal) (Ketentuan butir 14, USULAN) dan footer otomatis |
| 8 | Billing 7.2: log ketidaksesuaian disebut tanpa lokasi, form, atau pemilik | Dicatat sebagai open item 1: hubungan dokumen ini dengan log itu. Dokumen mengecualikan riwayat pembatalan dan revisi invoice sementara (USULAN) |
| 9 | Butir lain (lampiran tak ada, ruang lingkup transaksi, "Klausa" untuk ISO, LaTeX tersisa) | Tidak relevan ke dokumen T2 ini |

Aturan lintas dokumen RUNBOOK §6 dan defaults: rujukan internal AI (tidak ada), baris CONTOH (tidak ada), tiket Zammad Ops dan GLPI generalist (GLPI di Ketentuan butir 4, USULAN; Zammad tidak muncul karena FAT bukan Ops), Fani (tidak muncul), tiga penanda tangan berbeda (Finance Staff, Finance Lead, Samuel), vault dan kunci backup (tidak muncul), PPN (tidak ditulis), sebutan "Direktur (COO)" (tidak terpicu karena COO tidak disebut di badan), Samuel di badan = "Direktur Utama" (dipakai).

Peran dari specs/HR-ORG-01.json: Finance Lead dan Finance Staff dipakai apa adanya; Direktur Utama = JA-01. Peran Pemberi support dan Penanggung Jawab adalah peran khusus dokumen ini, bukan jabatan di HR-ORG-01. Contoh Project Manager (peran Divisi Operation, USULAN tanpa pemegang di HR-ORG-01, butir K-10) dan Business Development (JA-07) berasal dari SNX-FAT-SOP-01 dan hanya disebut sebagai contoh Pemberi support.

## 6. Asumsi dan tafsir

1. Kriteria dibaca sebagai: dokumen log (per baris satu bottleneck) untuk proses FAT yang tertahan dan memerlukan support. Judul baris menambah "Nonconformity & Corrective Action", jadi Tabel 3 memuat ketidaksesuaian dan tindakan korektif, dibatasi ke yang timbul dari bottleneck (pembatasan ini dari Description, bukan dari judul).
2. "Proses FAT" ditafsir sebagai enam proses SOP FAT di checklist baris 23 sampai 28. Baris Register, Form, dan Report FAT bukan proses.
3. Kolom, nilai Status, lima baris awal per tabel, dan Tabel 4 (tinjauan bulanan) adalah rancangan struktur. Checklist tidak merinci kolom. Tabel 4 dibuat karena evaluasi bulanan (butir 12) perlu tempat rekaman.
4. Pola pencatat (Finance Staff) dan penetap (Finance Lead) diambil dari pola log ketidaksesuaian di SNX-FAT-SOP-01 butir 4.14. Penerapan ke dokumen ini diberi label (USULAN).
5. Tabel 3 hanya diisi bila Tabel 2 berisi Ya. Penetapan Ya atau Tidak oleh Finance Lead, dengan contoh persyaratan yang sudah tertulis (batas waktu tahap pajak di SNX-FAT-SOP-05 bagian 8 dan TOP standar di SNX-FAT-SOP-01 butir 4.8). Tahap non-pajak tidak punya batas waktu tertulis, sehingga penetapan bergantung pada persyaratan kontrak atau peraturan.
6. SNX-FAT-SOP-06 dipakai untuk SOP Accounting and Financial Report karena nomor itu ada di config/worklist.json dan kini DONE di ledger.json (wave W7b); tanpa keterangan status (sweep, butir 1). Dua SOP lain (AR dan Payment) masih HOLD tanpa nomor di ledger dan checklist menandainya on review, sehingga ditulis "belum bernomor, dalam peninjauan" mengikuti pola SNX-FAT-SOP-01.
7. Definisi Istilah (Bottleneck, Support, Ketidaksesuaian, Tindakan korektif, Verifikasi efektivitas) adalah rumusan penyusun, bukan kutipan sumber; Ketidaksesuaian dan Tindakan korektif mengikuti pengertian umum ISO, ditulis dari ingatan.
8. Tidak ada diagram: dokumen berbentuk log, urutan langkah sudah di Ketentuan butir 1 sampai 12.
9. Daftar pemutus di bawah memakai peran dari daftar yang diizinkan prompt (owner, Samuel, Aziz, FAT, Legal, Fani). Pemetaan peran ke orang menurut data_conflicts adalah keputusan owner.

## USULAN

Hitungan: 11 butir. Di dokumen ada 15 label "(USULAN)" (satu di antaranya baris definisi di Istilah, yaitu pengertian label itu sendiri; sama dengan warn lint "15 butir") ditambah satu label "(USULAN, perlu konfirmasi konsultan)" di Acuan ISO.

| # | Butir USULAN | Posisi di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Pembagian pelaku: Finance Staff mencatat, Finance Lead menetapkan dan menjadi pemilik dokumen; Pemberi support dan Penanggung Jawab sebagai peran | Ketentuan butir 15; Peran | owner (pemetaan peran ke orang) |
| U2 | Catatan dibuat pada hari tahap diketahui tertahan | Ketentuan butir 1 | FAT |
| U3 | Permintaan support lewat tiket GLPI; FAT termasuk generalist | Ketentuan butir 4 | owner (batas lingkup generalist) |
| U4 | Finance Lead meninjau catatan terbuka setiap bulan, hasilnya di Tabel 4 | Ketentuan butir 12; Tabel 4 | FAT |
| U5 | Pengecualian riwayat pembatalan dan revisi invoice dari dokumen ini | Ruang Lingkup | FAT |
| U6 | Pengecualian bottleneck departemen lain dan bottleneck yang Finance Staff selesaikan sendiri | Ruang Lingkup | FAT |
| U7 | Tiga nilai Status: Terbuka, Menunggu Verifikasi, Ditutup | Istilah, Nilai Status | FAT |
| U8 | Penyimpanan di Folder arsip FAT (Google Drive) dan pemilik rekaman Finance Lead | Ketentuan butir 14; Rekaman | FAT |
| U9 | Klasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 (cakupan prosedur itu baru Divisi Operation) | Ketentuan butir 14; Rekaman | owner |
| U10 | Retensi minimal 10 tahun (angka dari SOP Billing hanya untuk arsip penagihan; diperluas ke dokumen ini) | Rekaman | FAT |
| U11 | Enam klausul ISO 9001:2015 dan ISO/IEC 27001:2022 | Acuan ISO | owner (meneruskan ke konsultan) |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Hubungan dokumen ini dengan log ketidaksesuaian di SNX-FAT-SOP-01 butir 4.14: sama atau terpisah. Sumber menyebut log itu tanpa form, lokasi, atau pemilik. Saat ini diperlakukan terpisah (U5). Bila sama, pengecualian di Ruang Lingkup dihapus dan Tabel 3 diperluas ke semua ketidaksesuaian FAT | FAT |
| 2 | Judul baris checklist ("Nonconformity & Corrective Action Records") lebih luas daripada Description (bottleneck dan support). Dokumen mengikuti Description; ketidaksesuaian di luar bottleneck belum punya tempat | owner |
| 3 | Finance Lead dan Finance Staff belum dipetakan ke orang atau jabatan (K-13 di SNX-HR-ORG-01) (diubah W9: G-3 A6, Finance Lead dijalankan Direktur sampai jabatannya terisi dan Finance Staff oleh JA-10 dan JA-11, keduanya USULAN) | owner |
| 4 | Persetujuan dan verifikasi bertumpu pada satu Finance Lead tanpa pengganti (catatan audit Billing butir 11). Ini calon bottleneck; dokumen tidak menulis kontrol pengganti karena sumber diam | FAT |
| 5 | Batas waktu permintaan support sampai support diterima tidak ada di sumber; dokumen tidak mengisinya | FAT |
| 6 | Batas lingkup generalist untuk GLPI belum dirinci owner (defaults.json ticketing) | owner |
| 7 | Dua proses masih dalam peninjauan di Drive dan belum bernomor (AR & Collection, Payment and Disbursement Approval). Daftar enam proses dan keterangan keduanya perlu disesuaikan bila tim menerbitkan nomor atau nama lain | FAT |
| 8 | Nomor dan nama klausul ISO belum dicocokkan dengan teks standar | owner (meneruskan ke konsultan) |
| 9 | Kolom, nilai Status, dan jumlah baris awal adalah rancangan; FAT dapat mengubahnya sebelum pengesahan | FAT |
| 10 | Wewenang menutup catatan oleh Finance Lead berada di bawah delegasi tertulis yang berlaku, yang isinya belum ada di HR-ORG-01 selain kalimat umum | Samuel |

## 7. Jawaban dua pertanyaan sebelum selesai

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

| Temuan | Perbaikan |
|---|---|
| Kalimat petunjuk kolom hampir semuanya berpola "Kolom X memuat Y" | Sudah diubah pada Petunjuk Pengisian butir 2, 3, 4, 7, dan 8 menjadi campuran "Finance Staff menulis X di kolom Y" dan "kolom X berisi Y". Butir 5 dan 6 tetap memakai "memuat" karena menjelaskan nilai, bukan tindakan |
| Rumus pembuka "Hasil yang dijaga:" muncul di semua dokumen laporan | Dipertahankan: itu pola 6a.4 RUNBOOK (hasil yang dijaga), bukan hiasan |
| Semua butir Ketentuan diawali "Finance Staff" atau "Finance Lead" dan berpanjang mirip | Dipertahankan: RUNBOOK 6a.1 mewajibkan pelaku berupa peran dan satu tindakan per butir. Butir 6, 12, dan 15 sengaja lebih panjang karena membawa rujukan |
| Istilah berurutan abjad dan semua baris Peran berformat sama | Dipertahankan: tabel rujukan memang dibaca per baris oleh auditor |
| Definisi Istilah berbunyi rapi dan simetris | Definisi Penanggung Jawab dipangkas dari "ditulis dengan nama dan jabatan" menjadi arti saja, karena aturan pengisian sudah ada di Petunjuk butir 7 |
| Kalimat penutup | Kesimpulan hanya dua kalimat tentang status dan peninjauan tahunan; tidak ada pujian atau ajakan |

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir di dokumen | Status |
|---|---|
| Kriteria log sheet, proses FAT, bottleneck, support | Sumber: checklist live, dibuka hari ini |
| Enam proses FAT | Sumber: checklist baris 23 sampai 28 |
| SNX-FAT-SOP-06 | Sumber: config/worklist.json dan ledger.json (DONE, W7b) (asumsi 6) |
| "1 hari" per tahap pajak | Sumber: SOP Tax lewat SNX-FAT-SOP-05; kutipan dari catatan FAT-SOP-05, tidak dibuka ulang hari ini |
| Nomor butir 4.4, 4.8, 4.11, 4.14, 4.2, 6.1 SNX-FAT-SOP-01 dan 4.4 SNX-FAT-SOP-04 | Dicocokkan ke spec saudara (specs/FAT-SOP-01.json, FAT-SOP-04.json) |
| Project Manager dan Business Development sebagai contoh Pemberi support | Sumber: SOP Billing 6.1 dan 4.1 lewat SNX-FAT-SOP-01 |
| JA-01 untuk Direktur Utama, butir K-13 | Sumber: specs/HR-ORG-01.json |
| Minimal 10 tahun, bulanan, hari diketahui, nilai Status, klasifikasi, folder | Tidak bersumber untuk dokumen ini; semua berlabel (USULAN) |
| Nomor dan nama klausul ISO | Dari ingatan, berlabel (USULAN, perlu konfirmasi konsultan), open item 8 |
| Nama orang | Hanya Samuel Kristanto Utomo di blok Approval (defaults.json); badan dokumen tidak memuat nama orang |
| Tanggal | Nol tanggal; tanggal efektif dan tanda tangan kosong |
| Kredensial | Nol; Ketentuan butir 13 justru melarang menuliskannya |
| Lima baris awal per tabel | Struktur, bukan fakta; baris tambahan diizinkan di Petunjuk butir 1 |

Tidak ada butir tanpa sumber dan tanpa label yang tersisa.

## 8. Riwayat putaran

1. Putaran 1: render pertama lulus lint generic. Pemeriksaan tambahan menemukan kalimat pengantar Nilai Status dan definisi Penanggung Jawab di Istilah memuat aturan pengisian (bagian 3 hanya boleh berisi arti), dan beberapa fakta SOP-01 dan SOP-05 diulang di Dokumen Terkait: aturan dipindah ke Ketentuan dan Petunjuk, fakta diganti rujukan nomor butir.
2. Putaran 2 dan 3: lebar kolom Tabel 1 sampai 4 diperbaiki karena kata header terpotong di tengah (dilihat dari PDF); header "Ketidaksesuaian" di Tabel 3 diganti "Persyaratan yang Tidak Terpenuhi" dan "Target Penyelesaian" diganti "Target Selesai".
3. Putaran 4: variasi kalimat di Petunjuk Pengisian; uji terakhir `pass: true` (lihat bagian atas).

## Sweep

Putaran sweep sesudah DONE (instruksi orkestrator, berkas FAT-RPT-02.sweep.txt). Hanya dua baris di spec yang berubah; fakta, angka, nama, dan struktur lain tetap. Temuan nonblocking lain di qa/FAT-RPT-02.verify.json tidak diubah karena di luar butir sweep.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1. Ruang Lingkup, tabel enam proses, baris Accounting and Financial Report | "SNX-FAT-SOP-06, dalam peninjauan" | "SNX-FAT-SOP-06" |
| 1. Dokumen Terkait, baris SNX-FAT-SOP-06 | "Accounting and Financial Report. Dalam peninjauan. Salah satu dari enam proses FAT di bagian Ruang Lingkup." | "Accounting and Financial Report. Salah satu dari enam proses FAT di bagian Ruang Lingkup." |
| 2. SNX-FAT-REG-01 dan SNX-FAT-FRM-02 | Tidak disebut di dokumen | Tidak ada perubahan: dokumen tidak merujuk keduanya. Hanya SNX-FAT-SOP-06 yang disebut dan sudah memakai nomor. AR & Collection dan Payment and Disbursement Approval tetap "belum bernomor, dalam peninjauan" karena masih HOLD tanpa nomor di ledger.json |

Uji sweep (bukti mentah di /tmp/pen-FAT-RPT-02/lint.out.txt, validate.out.txt, blankscan.out.txt): render_sop.py selesai tanpa galat; lint_doc.py generic `"pass": true`, `"fails": []`, satu warn "15 butir (USULAN) menunggu ACC" (jumlah sama dengan sebelum sweep); validate.py "All validations PASSED!"; blankscan.py "ok". Lulus pada putaran pertama sweep. Notes yang ikut diperbarui: asumsi 6, open item 7, dan baris SNX-FAT-SOP-06 di jawaban pertanyaan 2.

## ISO-W9

Dasar: control/LEAD-GUIDE.md G-3 A6. Hanya specs/FAT-RPT-02.json dan notes/FAT-RPT-02.md yang diubah.

| Butir | Sebelum | Sesudah |
|---|---|---|
| A6 blok Reviewed | Finance Lead | Amirull Yusuf Zulkarnain / Direktur (Prepared tetap Finance Staff) |
| A6 Istilah (bagian 2.1), dua baris baru setelah CoreTax DJP | tidak ada | "Finance Lead: peran pemeriksa dan penyetuju FAT; jabatannya belum terisi, dan sampai terisi peran ini dijalankan Direktur (USULAN)." dan "Finance Staff: peran pelaksana yang dijalankan pemegang jabatan Finance (JA-10) dan Accounting & Tax (JA-11) (USULAN)." (kata pertama arti diberi huruf kapital) |
| A6 tabel peran (bagian 4), baris Finance Staff dan Finance Lead | "Belum dipetakan ke jabatan di SNX-HR-ORG-01 (butir K-13)." | "Pemetaan ke jabatan mengikuti definisi di bagian 2.1 (butir K-13)." |
| A6 dokumen terkait, baris SNX-HR-ORG-01 | "Finance Lead dan Finance Staff belum dipetakan ke jabatan (butir K-13)." | "Pemetaan Finance Lead dan Finance Staff ke jabatan mengikuti definisi di bagian 2.1 (butir K-13)." |
| R2 butir 1, rujukan K-13 (tabel peran dua baris, dokumen terkait baris SNX-HR-ORG-01) | "... bagian 2.1 (butir K-13)" (3 tempat) | "... bagian 2.1 (SNX-HR-ORG-01 butir K-13)" (3 tempat) |
| R2 butir 2, notes | Hitungan USULAN tanpa penanda W9; open item 3 sudah bertanda | Kalimat hitungan USULAN ditandai "diubah W9" (15 menjadi 17 kemunculan); tidak ada baris open item atau USULAN lain yang berubah di W9 |

Rujukan silang yang diubah: rujukan ke definisi di bagian 2.1 (heading Istilah bernomor 2.1 di kerangka). Butir B4, R400, dan S03 tidak menyangkut dokumen ini.

Open item: nomor 3 diubah W9 (pemetaan peran mengikuti G-3 A6, berlabel USULAN). Tidak ada yang ditutup penuh.

Uji: render_sop.py rc 0; lint_doc.py generic "pass": true (warn 17 butir USULAN); validate.py "All validations PASSED!"; blankscan ok 12; w9diff.py: 4 baris lama, 6 baris baru, hanya perubahan di atas.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
- Istilah TOP: "Lama dan titik awalnya ada di SNX-FAT-SOP-01 butir 4.8." Kalimat penunjuk (STYLE §3.2); definisi ditulis ulang sesuai contoh STYLE §6.
- Tabel Peran, baris Finance Staff dan Finance Lead: "Pemetaan ke jabatan mengikuti definisi di bagian 2.1 (SNX-HR-ORG-01 butir K-13)." Kalimat penunjuk; pemetaan sudah tertulis di tabel Istilah dan di baris SNX-HR-ORG-01 Dokumen Terkait (butir K-13 tetap).
- Dokumen Terkait: ", yang dirujuk di Ruang Lingkup dan Ketentuan Penggunaan." (SNX-FAT-SOP-01), ", dirujuk di Ketentuan butir 14." (SNX-FAT-SOP-04), ", dirujuk di Ketentuan butir 6 dan Petunjuk Pengisian butir 2." (SNX-FAT-SOP-05), dan "Pemetaan Finance Lead dan Finance Staff ke jabatan mengikuti definisi di bagian 2.1" (SNX-HR-ORG-01, dipadatkan). Kalimat penunjuk balik.
- Rujukan butir yang tidak perlu dibuka pengisi: "(Ketentuan butir 4)" di Petunjuk 3, "(Ketentuan butir 7)" dan "(Ketentuan butir 11)" di Petunjuk 5, "pada butir 6" di Ketentuan 7 (diganti "hasil penetapan itu"), "(Ketentuan butir 14)" dan "(Ketentuan butir 10)" di tabel Record.
### W10 selisih angka
- "2.1" hilang: hanya muncul di kalimat penunjuk "definisi di bagian 2.1" (tabel Peran dan Dokumen Terkait) yang dihapus; nomor bagian Istilah tidak berubah.
### W10 catatan
Pihak luar: "klien" (satu-satunya sebutan di dokumen ini).
Petunjuk Pengisian ditulis sebagai kalimat perintah untuk Finance Staff (pencatat di tabel Peran). Ketentuan Penggunaan tetap menyebut pelaku per butir karena pembagian pelakunya sendiri adalah USULAN butir 15.
Label (USULAN) di Ketentuan 1 dan 12 dipindah ke akhir butir (STYLE §3.5), cakupannya tetap butir itu. "Corrective action (tindakan korektif)" di tabel Istilah mengikuti heading Tabel 3.
Tabel isian Isi Log diberi min_row_cm 1.0.
Lebar kolom Tabel 1 (Uraian Bottleneck) dan Tabel 3 (Corrective Action, Hasil Verifikasi Efektivitas) disesuaikan agar judul tidak terpotong.

### W10 rujukan USULAN dicek (adjudikasi worker, gerbang rujukan USULAN)
- .sections[4].blocks[2].p (butir 3): label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[6].blocks[0].table.rows[1][1]: tanpa label; deskripsi dokumen terkait (SNX-FAT-SOP-04), bukan aturan form ini.

### W10 audit pointer
- .sections[1].blocks[1].table.rows[14][1]: lengkap (definisi; lama dan titik awal TOP standar tetap dirujuk ke SNX-FAT-SOP-01 butir 4.8 di Ketentuan butir 6 dan tabel Dokumen Terkait)
- .sections[2].blocks[6].p: lengkap (pelaku Finance Staff, nilai Ya atau Tidak, kolom Ketidaksesuaian Tabel 2; "penetapan itu" menunjuk butir 6 tepat di atasnya)
- .sections[3].blocks[0].table.rows[0][1]: lengkap (kalimat penunjuk ke definisi dibuang; pemetaan jabatan Finance Staff tetap ada di tabel Istilah, rujukan Ketentuan tetap)
- .sections[3].blocks[0].table.rows[1][1]: lengkap (kalimat penunjuk ke definisi dibuang; pemetaan Finance Lead dan label USULAN tetap ada di tabel Istilah, rujukan Ketentuan tetap)
- .sections[4].blocks[2].p: lengkap (alternatif nomor ticket GLPI di kolom Diminta kepada dan label USULAN; catatan batas generalist tetap di Ketentuan butir 4)
- .sections[4].blocks[4].p: lengkap (Ya atau Tidak menurut penetapan Finance Lead, nilai dari tabel Nilai Status, Tanggal Ditutup = tanggal Finance Lead menetapkan Ditutup; syarat penutupan milik Finance Lead tetap di Ketentuan butir 11)
- .sections[6].blocks[0].table.rows[1][1]: lengkap (penunjuk balik "dirujuk di Ketentuan butir 14" dibuang; Ketentuan butir 14 tetap merujuk SNX-FAT-SOP-04 butir 4.4)
- .sections[6].blocks[0].table.rows[2][1]: lengkap (penunjuk balik dibuang; Ketentuan butir 6 tetap memuat batas 1 hari dengan rujukan SNX-FAT-SOP-05 bagian 8)
- .sections[6].blocks[0].table.rows[6][1]: lengkap (pemetaan Finance Lead dan Finance Staff butir K-13 tetap disebut; definisinya ada di tabel Istilah)
- .sections[7].blocks[1].table.rows[0][1]: lengkap (lokasi Folder arsip FAT, pencatat, pemilik, klasifikasi, label USULAN; langkah simpan sesuai SNX-FAT-SOP-04 butir 4.4 tetap di Ketentuan butir 14)
- .sections[7].blocks[1].table.rows[1][1]: lengkap (lokasi bukti, penulis Finance Staff, kolom Hasil Verifikasi Efektivitas, pemilik, label USULAN)

### W10 audit cakupan label
- .sections[4].blocks[2].p: OK (rujukan Ketentuan butir 4 berlabel diganti label pada kalimat nomor ticket GLPI)
