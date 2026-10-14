# REVIEW-W3 (2026-10-14T23:06:13Z)

## SNX-FAT-SOP-01 Billing & Invoicing
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 2; OOXML: PASSED
- Berkas: out/03_FAT/SNX-FAT-SOP-01 Billing & Invoicing (Rev00 DRAFT).docx
- Sumber: 1. SOP Billing and Invoicing (1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI, modifiedTime 2026-10-14T08:06:56.942Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tujuan utama: nominal invoice mengikuti PKS, PO, dan BAST yang sah (Purpose dan butir 4.1) | "Memastikan seluruh tagihan (invoice) diterbitkan dengan nominal yang 100% akurat berdasarkan Perjanjian Kerja Sama (PKS), Purchase Order (PO), dan Berita Acara Serah Terima (BAST) yang sah." (1.2 butir 1) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| Validasi tiga arah sebelum e-Faktur Pajak (butir 4.3 dan 6.2) | "Setiap draf invoice wajib melalui proses validasi 3 arah (3-way matching) antara nominal PKS, acuan PO, dan bukti penyerahan BAST sebelum e-Faktur Pajak diterbitkan." (7.2) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| Pemisahan pembuat dan penyetuju: Finance Staff tidak mengirim invoice tanpa persetujuan Finance Lead (butir 4.4) | "Staff Finance dilarang keras menerbitkan atau mengirimkan invoice kepada klien tanpa persetujuan (approval) tertulis dari Finance Lead." (4.2) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |

Fakta penting lain (kutipan tanpa penanda tebal; sumber memakai tebal di beberapa tempat):

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi |
|---|---|---|---|
| 1 | Cakupan transaksi | "SOP ini mencakup seluruh proses penagihan atas penjualan jasa dan pekerjaan proyek perusahaan, meliputi:" lalu "Proyek Pengembangan Sistem & Layanan IT (IT Service Development)." dan "Layanan Konsultasi dan Pekerjaan Berbasis Retainer/Kontrak Periodik" | 2.2, Scope |
| 2 | Syarat dokumen pendukung | "Tagihan hanya dapat diproses dan diterbitkan apabila 4 dokumen pendukung utama telah lengkap dan tervalidasi:" (PKS, PO/SPK, BAST, NPWP Klien) | 5.1, definisi dan butir 4.1 |
| 3 | Data master klien dan Google Form | "Sebelum permohonan penagihan diproses, Tim Sales wajib memastikan klien te

### USULAN
Enam butir bertanda "(USULAN)" di dokumen (lint menghitung enam, termasuk baris definisi label itu sendiri) ditambah label klausul ISO dan process_owner. Total tujuh butir keputusan.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Rumusan tunggal PPN 12% menggantikan 11% di satu tempat sumber | Butir 4.5 | FAT (dengan konsultan pajak) |
| 2 | Titik awal TOP = tanggal invoice | Butir 4.8 | FAT |
| 3 | Data keuangan, daftar harga, data penagihan klien, dan rekening bank = RESTRICTED (Internal) menggantikan "Rahasia (Confidential)" | Butir 4.10 | Fani (pemilik skema SNX-ISMS-PRO-01 di sisi Operation dan ISMS) |
| 4 | Penetapan pelaku pada butir 4.3, 4.9, 4.11, 4.12, 4.14, 4.16, pemantauan Overdue (bagian 9), dan Finance Lead sebagai pemilik rekaman | Butir 4.15 dan tabel rekaman | FAT, dikukuhkan owner |
| 5 | Tim Sales dipetakan ke Business Development | Tabel peran bagian 5 | owner |
| 6 | Daftar klausul ISO 9001:2015 (7.5.3, 8.2, 8.5, 8.6) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.15, 5.33, 8.5), label "(USULAN, dikonfirmasi konsultan)" | Bagian 11, Acuan standar | owner, diteruskan ke konsultan |
| 7 | Process owner = Finance Lead (sumber tanpa "Pemilik dokumen") | Identity Document | owner |

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Rumusan tarif PPN: 12% atau 11%, dan dasar pengenaannya. Sumber menulis keduanya. Perlu keputusan tertulis agar USULAN 1 bisa dicabut | FAT |
| 2 | e-Faktur Pajak terbit sebelum approval Finance Lead (butir 6.2 lalu 6.3), padahal Finance Staff dilarang menerbitkan invoice tanpa approval (butir 4.4) dan koreksi butuh Faktur Pajak Pengganti. Apakah approval dipindah sebelum e-Faktur | FAT |
| 3 | Titik awal TOP (USULAN 2) dan lokasi pencatatan tanggal penerimaan (butir 6.4.6): sumber tidak menyebut tempatnya | FAT |
| 4 | Tidak ada target waktu per tahap penerbitan invoice (pengajuan, e-Faktur, pemeriksaan, pengiriman). SOP Tax di folder yang sama memakai 1 hari per langkah; angka itu tidak saya pakai di sini karena lingkupnya lain | FAT |
| 5 | Finance Lead berhalangan: pengganti tidak diatur. Finance Lead dan Finance Staff belum dipetakan ke jabatan (HR-ORG-01 K-13) | owner |
| 6 | Tindak lanjut invoice Overdue: "prosedur pemantauan piutang" di sumber adalah SOP Account Receivable & Collection (checklist baris 24), status on review dan belum bernomor. Dokumen menyebutnya dengan judul; kode SNX perlu ditambahkan ke bagian 2, 9, dan 11 setelah terbit | FAT |
| 7 | Penjualan perangkat atau lisensi tidak disebut di scope sumber. Masuk SOP ini atau tidak | FAT |
| 8 | Permohonan penagihan yang tidak lengkap: sumber hanya melarang memproses, tanpa menyebut siapa memberi tahu Project Manager dan dalam berapa lama | FAT |
| 9 | Persetujuan Direktur Utama atas TOP lebih dari standar: sebelum PKS atau PO disepakati (5.3) atau saat draf invoice (6.3). Keduanya dipertahankan | FAT dan Samuel |
| 10 | Staff Finance menandatangani dan menstempel invoice cetak (sumber 6.4). Apakah itu sesuai Authority Matrix yang belum be

## SNX-FAT-SOP-05 Tax Administration & Reporting
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 2; OOXML: PASSED
- Berkas: out/03_FAT/SNX-FAT-SOP-05 Tax Administration & Reporting (Rev00 DRAFT).docx
- Sumber: 6. SOP Tax Administration & Reporting.docx (1iMKby6u4X8MYyGlrC5qz73D0y2anOv87, modifiedTime 2026-10-13T11:17:33.562Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Tahap Review & Approval dipegang Lead, 1 hari: rekonsiliasi di akhir Masa Pajak, lalu approval dan pengajuan payment | Tabel IV baris 3, sel Aktivitas: "Review & Approval" / "Rekonsiliasi nilai pajak terhutang di setiap akhir Masa Pajak" / "Proses approval dan pengajuan payment"; sel Waktu: "1 day"; sel PIC: "Lead" (baris dalam sel dipisah "/") | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| 2 | Tahap Pembayaran di tabel hanya membuat kode billing, 1 hari, Staff; tahap Pelaporan mengarsipkan bukti lapor, 1 hari, Lead | Tabel IV baris 4: "Pembayaran" / "Pembuatan kode billing" / "1 day" / "Staff". Baris 5: "Pelaporan" / "Pengarsipan dokumen bukti lapor (BPE, SPT, Kode billing dan bukti bayar)" / "1 day" / "Lead" | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| 3 | PPN Pemungut (WAPU/Kode 02) adalah penanganan khusus untuk transaksi dengan Instansi Pemerintah atau BUMN | Bagian III: "Penanganan khusus untuk PPN Pemungut (WAPU/Kode 02) atas transaksi dengan Instansi Pemerintah/BUMN." | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Acuan klausul ISO 9001:2015 5.3, 7.5.3, 8.1 dan ISO/IEC 27001:2022 Annex A 5.31, 5.33 (label "USULAN, dikonfirmasi konsultan") | Bagian 4 (judul butir) dan bagian 11 | owner |
| 2 | Lima tahap berlaku untuk semua jenis pajak sampai alur per jenis pajak dirinci | 6.1 intro | FAT |
| 3 | Penyetoran pajak dan pencatatan BPN/NTPN oleh Finance Staff | 6.4 intro dan langkah 2 dan 3; peran Finance Staff | FAT |
| 4 | Pengarsipan bukti potong dan Faktur Pajak Keluaran oleh Finance Lead | 6.5 langkah 3; tabel rekaman baris 2 | FAT |
| 5 | Persetujuan utang pajak dicatat di SNX-FAT-FRM-01 | 6.3 langkah 2; Dokumen terkait; tabel rekaman baris 4 | FAT |
| 6 | SNX-FAT-SOP-04 sebagai acuan pengarsipan | Dokumen terkait | FAT |
| 7 | Penanganan dokumen invoice atau pengajuan yang belum lengkap (Finance Staff meminta ke Unit pengaju dan menahan perhitungan), termasuk cabang di diagram | Bagian 9 baris 2; diagram bagian 7 | FAT |
| 8 | Daftar pengecualian scope (invoice di luar Faktur Pajak Keluaran, pembayaran selain pajak, pencatatan akuntansi dan laporan keuangan, arsip dokumen keuangan selain perpajakan) | Bagian 2 paragraf terakhir | FAT |
| 9 | Peran "Unit pengaju" dan tanggung jawabnya menyerahkan invoice atau pengajuan | Bagian 5 baris 3; 6.1 | owner |
| 10 | Satuan "Hari" = hari kerja | Bagian 3, baris Hari | FAT |
| 11 | BPE = Bukti Penerimaan Elektronik | Bagian 3, baris BPE | FAT |
| 12 | Klasifikasi rekaman perpajakan RESTRICTED (Internal) | Kebijakan 4.5 | owner |
| 13 | Lokasi simpan "Folder Google Drive Departemen FAT" untuk empat rekaman | Bagian 11, tabel rekaman | FAT |
| 14 | Retensi minimal 10 tahun untuk rekaman perpajakan (disamakan dengan SOP Billing) | Bagian 11, tabel rekaman | FAT dan L

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Finance Lead dan Finance Staff belum dipetakan ke jabatan atau orang (HR-ORG-01 K-13; jabatan terdekat JA-10 Finance dan JA-11 Accounting & Tax, tidak berlevel). Tanpa pemetaan, auditor tidak bisa menunjuk siapa memegang peran | owner |
| 2 | Pengajuan pembayaran: sumber tidak menyebut penerima pengajuan, siapa yang melepas dana, siapa yang menyetor, batas wewenang approval, maupun form yang dipakai. Dokumen memakai Finance Lead untuk menyetujui dan mengajukan, Finance Staff untuk menyetor (USULAN) | FAT dan Samuel |
| 3 | Tenggat statutori setor dan lapor per jenis pajak tidak ada di sumber maupun di dokumen ini; tidak ada penanganan untuk keterlambatan, denda, atau SPT pembetulan. Tahap 1 hari tidak menjamin tenggat peraturan | FAT |
| 4 | Arti "1 day": hari kerja atau hari kalender, titik mulai (sesudah tahap sebelumnya selesai atau sejak dokumen diterima), dan apakah 1 hari masuk akal untuk SPT Tahunan PPh Badan, laba fiskal, dan PPh Pasal 21 akhir tahun | FAT |
| 5 | Alur per jenis pajak: PPh Pasal 21 (Gross-Up, penyesuaian akhir tahun), pengkreditan Faktur Pajak Masukan, angsuran PPh Pasal 25, laba komersial dan fiskal, rekonsiliasi kredit pajak punya butir scope tetapi tidak punya langkah sendiri | FAT |
| 6 | Tujuan 4 sumber (hak kompensasi pajak atau Tax Asset, ekualisasi) kini ada di kebijakan 4.6 dengan Finance Lead sebagai pelaku (USULAN), tetapi bagian 6 belum punya langkah yang menghasilkannya dan tabel rekaman belum memuat dokumen ekualisasi. Perlu langkah dan rekaman baru | FAT |
| 7 | Tumpang tindih penerbitan Faktur Pajak Keluaran: SNX-FAT-SOP-01 menulis Finance Staff menerbitkan e-Faktur Pajak di CoreTax DJP pada penagihan, sedangkan 6.2 langkah 4 SOP ini memuatnya di tahap perhitungan. P

## SNX-LEG-SOP-01 Legal Operational
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-SOP-01 Legal Operational (Rev00 DRAFT).docx
- Sumber: SOP Divisi Legal – SINUX.docx (19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb, modifiedTime 2026-10-13T10:54:39.480Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Pengguna SOP: Line Manager Legal, Staff Legal, dan unit bisnis pemohon, termasuk entitas afiliasi. Di dokumen menjadi Scope, dengan "Pemohon" = departemen SINUX yang mengajukan permintaan | "Berlaku bagi Line Manager Legal dan seluruh Staff Legal, serta unit bisnis SINUX yang mengajukan permintaan legal. Mencakup juga entitas afiliasi atau turunan (misalnya rencana pendirian PT Nusagrid) sepanjang ditugaskan kepada Divisi Legal SINUX." (1. Tujuan, Ruang Lingkup, dan Prinsip) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 2 | Pembagian kerja Line Manager dan Staf: Staff menyiapkan, Line Manager mereview dan menyetujui atau mengembalikan. Di dokumen menjadi butir 4.6 dan prosedur 6.2 langkah 7 dan 8 | "Bagian ini mengatur alur kerja di dalam Divisi Legal: Staff Legal menyiapkan, Line Manager Legal mereview dan menyetujui." (4. SOP Internal Tim Legal) dan "Review Line Manager. Staff menyerahkan draf, tabel redline, dan ringkasan risiko; Line Manager menyetujui atau mengembalikan dengan catatan." (4.1 butir 6) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 3 | Koordinasi dengan departemen lain: kewajiban Pemohon dan batas waktu jawab. Di dokumen menjadi butir 4.7 sampai 4.15, bagian 8, dan prosedur 6.1 | "Melibatkan Legal sejak tahap negosiasi komersial, sebelum ada komitmen tertulis kepada pihak luar." dan "Menjawab pertanyaan Legal dalam 2 hari kerja; tenggat Legal bergeser sebesar keterlambatan jawaban." dan "Tidak menandatangani, menjanjikan, atau mengirim dokumen final sebelum persetujuan Legal dan pejabat berwenang sesuai DoA." (3.2 Kewajiban Divisi Pemohon, butir 1, 4, 5) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |

### USULAN
Delapan placeholder [ISI] tercakup (butir 1 sampai 8). Lint menghitung 18 kemunculan "(USULAN)" termasuk baris definisi label dan lima baris SLA. Total 17 butir keputusan.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Atasan Line Manager Legal = COO (ganti placeholder 1; tiga sumber berbeda) | Bagian 5 baris Line Manager Legal | owner, dikukuhkan Samuel (HR-ORG-01 K-03) |
| 2 | Kanal permintaan = tiket GLPI (ganti placeholder 2) | Butir 4.7, 6.1 | owner (batas "generalist") |
| 3 | Sampai DoA terbit, Manajemen memutuskan persetujuan tiap kontrak (ganti placeholder 3) | Butir 4.20 | Samuel |
| 4 | Dokumen asli di tempat aman dengan akses terbatas pada Line Manager Legal dan Staff Legal (ganti placeholder 4) | Butir 4.25, tabel rekaman | Legal |
| 5 | Pemantauan pelaporan berkala (LKPM) oleh Staff Legal bersama Finance; penanggung jawab dan jadwal di register perizinan; "Finance/Compliance" dipetakan ke Finance (ganti placeholder 5) | 6.6 langkah 10 dan 11, bagian 5 | FAT |
| 6 | Repositori resmi = folder Google Drive departemen Legal (ganti placeholder 6) | Butir 4.24, tabel rekaman | Legal |
| 7 | Periode retensi belum ditetapkan, penetapan di SNX-LEG-SOP-03 (ganti placeholder 7) | Butir 4.27, kolom Retensi | Legal |
| 8 | Penyetuju SOP = Samuel Kristanto Utomo / President Director (ganti placeholder 8; defaults D2, bukan label di badan dokumen) | Blok Approved By | Samuel |
| 9 | Pelaku langkah pasif dan pemilik rekaman ditetapkan dari pembagian peran dan HR-JA-01 | Butir 4.6, tabel rekaman | Legal |
| 10 | Label Rahasia di sumber setara RESTRICTED (Internal) dan SECRET | Butir 4.23 | Fani (pemilik skema SNX-ISMS-PRO-01 di sisi Operation dan ISMS) |
| 11 | "tim keamanan/IT" dipetakan ke VP Tech Operation and Services | Bagian 5, 6

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Batas "generalist" untuk tiket GLPI belum dirinci owner. Apakah semua permintaan layanan legal masuk GLPI, atau ada yang lewat Zammad | owner |
| 2 | Atasan Line Manager Legal berbeda di sumber ("Direksi/COO"), Jobdesk ("CEO"), dan HR-JA-001 ("Management / Direktur"); HR-ORG-01 K-03 masih menunggu | owner, Samuel |
| 3 | DoA (Authority Matrix) belum terbit: pejabat penyetuju, batas nilai, dan jenis kontrak kosong. Butir 4.20 hanya jembatan sementara | Samuel |
| 4 | Batas wewenang Line Manager Legal menunjuk notaris, konsultan, advokat kosong di Jobdesk dan "Belum ditetapkan" di SNX-HR-JA-01; butir 4.29 dan 6.8 langkah 7 bergantung padanya | Legal, Samuel |
| 5 | Konfirmasi tafsir pertentangan "memberi opini" dan "hentikan proses": Line Manager Legal menghentikan proses di Departemen Legal, keputusan di Manajemen. Jobdesk memakai kata "menahan kontrak" | Legal |
| 6 | Periode retensi dan lokasi arsip (termasuk dokumen asli) belum ada; SNX-LEG-SOP-03 harus memutus dan dokumen ini diselaraskan | Legal |
| 7 | Tanpa angka di sumber: penyelesaian dokumen korporasi dan urgent; waktu lapor pelanggaran atau wanprestasi kontrak ("segera"); penanganan surat regulator dan perubahan fakta yang dilaporkan Pemohon (sumber hanya mewajibkan laporan) | Legal |
| 8 | Pemohon yang menandatangani, menjanjikan, mengirim, atau mengubah dokumen tanpa review: sumber melarang tanpa menetapkan penanganan, maka tidak ada baris di bagian 9 | Legal, Samuel |
| 9 | Register permintaan tidak punya format lampiran dan tidak ada dokumen bernomor di checklist; register kontrak juga tidak ada. Menambah baris checklist di luar 88 baris hanya bila konsultan meminta | Legal, owner |
| 10 | Tumpang tindih dengan SNX-LEG-SOP-02 (Contract Review 

## SNX-LEG-SOP-02 Contract Review & Legal Approval
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/04_Legal/SNX-LEG-SOP-02 Contract Review & Legal Approval (Rev00 DRAFT).docx
- Sumber: SOP Contract Review & Legal Approval (1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE, modifiedTime 2026-10-14T09:08:19.129Z); SOP Divisi Legal – SINUX.docx (19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb, modifiedTime 2026-10-13T10:54:39.480Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Penandatanganan baru boleh sesudah semua persetujuan yang diwajibkan diperoleh (gerbang "sebelum penandatanganan" dari kriteria baris) | "Penandatanganan hanya dapat dilaksanakan setelah persetujuan yang diwajibkan telah diperoleh." (Prosedur Pelaksanaan, Pemeriksaan Akhir dan Penandatanganan, butir 6) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |
| 2 | Persetujuan Legal bukan pengganti persetujuan lain | "Persetujuan Legal tidak dengan sendirinya menggantikan persetujuan bisnis, keuangan, keamanan informasi, atau kewenangan penandatanganan yang dipersyaratkan." (Definisi, Persetujuan Legal) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |
| 3 | Target waktu berstatus usulan awal dan dihitung sejak informasi lengkap | "Target berikut merupakan usulan awal berdasarkan SOP Divisi Legal dan dihitung sejak informasi serta dokumen minimum telah diterima secara lengkap." (Prosedur Pelaksanaan, Prioritas dan Target Waktu) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |

### USULAN
| # | Butir | Letak di spec | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Kanal permintaan = tiket GLPI (SINUX Service Hub). Sumber hanya punya placeholder; owner memutus GLPI untuk generalist, batas "generalist" belum dirinci | scope butir 4, 6.1 intro dan langkah 1 | owner |
| 2 | Semua target waktu di bagian 8 (NDA 1 dan 2 hari kerja, review kontrak atau PKS 1 dan 3 sampai 5, kontrak baru 1 dan 5, korporasi 2, mendesak, jawaban Pemohon 2 hari kerja). Sumber sendiri menyebutnya "usulan awal"; satuan hari kerja (asumsi 1) | bagian 8 | Legal (Line Manager Legal) |
| 3 | Pelaku yang SOP tetapkan untuk langkah berkalimat pasif di sumber (butir 4.6, 4.11; 6.4 langkah 9; 6.7 langkah 3 dan 8; 6.10 langkah 3 dan 6) dan Line Manager Legal sebagai pemilik rekaman di bagian 11 | butir 4.19, bagian 11 | Legal |
| 4 | Pemetaan Line Manager Legal ke Legal & Compliance (JA-08) dan Staff Legal ke JA-09 (berasal dari SNX-HR-ORG-01, K-13, sudah USULAN di sana) | tabel peran | owner |
| 5 | Checklist review: SNX-LEG-FRM-01 untuk kontrak pelanggan, SNX-LEG-FRM-02 untuk kontrak vendor atau pemasok. Sumber hanya menulis "Contract Review Checklist" | Dokumen terkait | Legal |
| 6 | Daftar klausul ISO (bagian 3 notes ini): 9001 8.2.3, 8.2.4, 8.4.3, 7.5.3; 27001 Annex A 5.31, 5.20, 5.34, 6.6 | iso_refs | owner (meneruskan ke konsultan) |
| 7 | Process owner = Line Manager Legal. Sumber utama menulis "Departemen Legal" (unit, bukan jabatan); sumber lama menulis "Pemilik SOP: Line Manager Legal"; defaults (fallback reviewer departemen) memberi hasil yang sama. Tidak diberi label di dokumen karena medan identitas satu baris | meta.process_owner | owner |

Jumlah USULAN: 7 butir (16 kemunculan label "(USULAN)" di dokumen, menurut warn lint).

### Open items
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Kanal resmi permintaan dan batas "generalist" GLPI belum diputus; sumber utama masih [TBD]. Apakah nomor referensi register permintaan Legal sama dengan nomor tiket GLPI belum jelas | owner |
| 2 | Matriks DoA belum disusun, jabatan Pejabat Berwenang belum ditetapkan, dan belum dipastikan apakah "matriks DoA" sama dengan Authority Matrix di SNX-HR-ORG-01. Sampai terbit, langkah 6.7.5 sampai 6.7.7 berlaku untuk semua kontrak | owner dan Samuel |
| 3 | Lokasi repositori resmi, lokasi register permintaan Legal, register kontrak, dan rekaman lain; retensi semua rekaman bagian 11 belum ditetapkan. SNX-LEG-SOP-03 belum ada saat disusun | Legal |
| 4 | Pelaku pemberian akses ke kontrak (butir 4.17, sumber pasif) dan tingkat klasifikasi tiap jenis kontrak menurut SNX-ISMS-PRO-01 | Legal |
| 5 | Baris "Dokumen Korporasi/Perizinan" ada di tabel target waktu sumber tetapi di luar daftar jenis kontrak pada scope sumber. Dipertahankan di bagian 8; Legal memutus apakah dipindah ke SNX-LEG-SOP-01 | Legal |
| 6 | "Media persetujuan internal yang ditetapkan" (butir 4.13) dan "metodologi risiko Perusahaan, apabila telah ditetapkan" (butir 4.11) belum ada | Legal |
| 7 | Atasan Line Manager Legal: sumber lama [ISI], Jobdesk "CEO", HR-JA-001 "Management / Direktur"; SNX-HR-ORG-01 K-03. Dokumen ini netral | owner |
| 8 | Pengecualian scope dan baris Dokumen terkait untuk SNX-LEG-SOP-01 dan -03 bergantung pada isi dokumen itu. Spec LEG-SOP-01 (draf paralel, dibaca saja di akhir) memuat korporasi, perizinan, sengketa, somasi, dan klaim di scope-nya, sesuai pengecualian di sini, dan memakai GLPI untuk permintaan; spec LEG-SOP-03 belum ada. Bila isinya berubah, perbarui scope butir 5 dan tabel Dokumen terkait | Legal (setelah spec LEG-
- Langkah persetujuan ulang Line Manager Legal sesudah revisi tidak ada di 6.6 (nonblocking verifikator); Legal konfirmasi.

## SNX-COM-SOP-01 Sales Process
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/05_Commercial/SNX-COM-SOP-01 Sales Process (Rev00 DRAFT).docx
- Sumber: SALES STANDARD OPERATING PROCEDURE.pdf (19Hex8udn1JDG4NKY7hZaODjroHeHwMM0, modifiedTime 2026-10-05T07:08:41.814Z); Commercial Onboarding. Jul 2026.pdf (16TIN9Tsv_sBXMrL4KHeO8f6Ao0F-KsAS, modifiedTime 2026-10-05T07:10:01.246Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Proposal hanya dibuat setelah discovery selesai, dan sebelum dikirim ke customer harus melewati tiga pemeriksaan berurutan: review internal, approval harga, approval diskon (jika ada). Dasar butir 4.6, 4.9, dan langkah 6.4 | "Proposal hanya dibuat setelah Discovery selesai. Demo dilakukan bersama Presales apabila diperlukan." dan "Sebelum dikirim ke customer:" lalu "Review internal." "Approval harga." "Approval diskon (jika ada)." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| CRM wajib memuat seluruh aktivitas penjualan dan diperbarui paling lambat 24 jam. Dasar butir 4.3 dan baris SLA | "Seluruh aktivitas penjualan wajib dicatat di CRM." dan "CRM harus diperbarui maksimal 24 jam setelah aktivitas dilakukan." | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |
| Handover wajib, dengan handover meeting sebelum implementasi dan enam butir minimal. Dasar butir 4.16 dan 6.8 | "Sales wajib melakukan handover kepada Delivery." lalu "Handover meeting wajib dilakukan sebelum implementasi dimulai." dengan butir "Customer Background", "Scope", "Timeline", "Risks", "Commitment", "Contact Person" | 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0 |

Fakta penting lain:

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi |
|---|---|---|---|
| 1 | Pemilik dokumen = VP Commercial (process_owner) | "Commercial Department Document Owner: VP of Commercial" | Sampul SOP; SOP sumber, fileId 19Hex8... |
| 2 | Siklus tinjau sumber 6 bulan; dokumen ini YEARLY menurut defaults | "Review Cycle: Every 6 Months" | Sampul SOP |
| 3 | Lima kriteria qualification dan metode | "Sebelum opportunity masuk ke tahap Proposal, Sales harus memastikan opportunity telah memenuhi kriteria qualification menggunakan BANT atau MEDDICC, serta telah melakukan discovery melalui pend

### USULAN
Sembilan butir keputusan; dokumen memuat 14 label "(USULAN" (12 persis "(USULAN)", ditambah satu pada butir 4.13 dan satu pada label klausul ISO).

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Pemetaan tahap proses ke Sales Stage CRM (Leads, Qualified, Opportunity, Bid, Win atau Lost, Future Nurture) | Butir 4.7 | owner |
| 2 | Wewenang harga: VP Commercial merekomendasikan harga dan diskon, COO menyetujui dan menetapkan margin final, setiap diskon butuh persetujuan COO sampai ambang ditetapkan. Margin final = owner (catatan worklist) | Butir 4.10, langkah 6.4.4 sampai 6.4.6, 6.6.3 sampai 6.6.5 | owner |
| 3 | Data customer, kontrak, dan harga = RESTRICTED (Internal) untuk Commercial (SNX-ISMS-PRO-01 belum mencakup Commercial) | Butir 4.13 | Fani |
| 4 | Titik waktu keterlibatan Legal: review draf kontrak sebelum tanda tangan, NDA sebelum informasi RESTRICTED dibagikan, dukungan negosiasi kontrak (catatan worklist "tambah langkah Legal") | Butir 4.14, langkah 6.3.1 dan 6.3.2, 6.6.6, 6.7.1 dan 6.7.2 | Legal |
| 5 | Project kick-off dimulai sesudah Service Delivery Manager menerima paket handover, dan tidak lagi masuk syarat closing | Butir 4.15 | owner |
| 6 | Penetapan pelaku yang tidak disebut sumber (VP Commercial: review internal, tinjauan mingguan dan bulanan, penerima laporan, penyerahan paket, penyimpan rekaman persetujuan; Legal & Compliance: penyimpan NDA dan hasil review kontrak; Business Development: perbaikan paket ditolak) | Butir 4.19, bagian 8, bagian 11 | owner |
| 7 | Pemetaan peran: Sales dan Sales Executive ke Business Development; Presales ke Manager of Product Tech; Delivery ke Service Delivery Manager (jabatan usulan tanpa pemegang) | Tabel peran bagian 5 | owner (dengan Fani untuk Service Delivery Manager dan 

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Ambang diskon, batas margin minimum, dan tenggat approval harga tidak ada di sumber. Penetapan COO sebagai penyetuju (USULAN 2) belum diputus tertulis, dan Authority Matrix belum bernomor | owner |
| 2 | Siklus tinjau: sumber 6 bulan, dokumen ini YEARLY (defaults). Konfirmasi bahwa VP Commercial menerima YEARLY | owner |
| 3 | Kriteria qualification: Technical Fit (SOP) atau Project Scope (deck); BANT atau MEDDICC (SOP) atau MEDDICC saja (deck). Skala Opportunity Score, arti "strategis" pada negosiasi dan eskalasi, dan "pihak yang berwenang" untuk penyimpangan prosedur tidak didefinisikan | owner |
| 4 | Status lead yang tidak lolos qualification: sumber tidak mengatur (Future Nurture atau Lost). Bagian 9 hanya melarang proposal | owner |
| 5 | Penerima dan format laporan harian, mingguan, dan bulanan; peminta laporan harian ("jika diminta"); pelaku tinjauan pipeline dan forecast | owner |
| 6 | Arti "Internal Request" (4 jam kerja), titik awal hitung respons email dan WhatsApp, dan apakah respons internal lewat tiket GLPI (generalist). Deck juga menyebut alat "Pre-sales Request" dan "Proposal & Quotation Template" tanpa bentuk, nomor, atau kanal | owner |
| 7 | Siapa memberi persetujuan internal (syarat closing) dan siapa menandatangani kontrak atas nama SINUX; Authority Matrix belum bernomor | Samuel |
| 8 | Syarat closing: apakah kick-off tetap masuk (versi sumber) atau sesudah handover (USULAN 5) | owner |
| 9 | Siapa yang menyerahkan paket handover (Business Development di sumber, VP Commercial di dokumen Operation) dan selisih isi enam butir paket handover dengan Checklist G1 di SNX-OPS-FRM-01 (SLA tertulis ada di G1, Customer Background, Timeline, dan Risks ada di sumber) | Fani |
| 10 | Nama produk 

## SNX-HR-SOP-08 Company Leaves
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/02_HR/SNX-HR-SOP-08 Company Leaves (Rev00 DRAFT).docx
- Sumber: PP - Cuti.docx (1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z, modifiedTime 2026-10-13T11:34:27.275Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Semua jenis cuti diajukan lewat sistem HR dengan persetujuan atasan langsung, paling lambat 7 hari kerja sebelumnya | Pasal 32 ayat (1): "Prosedur pengambilan semua jenis cuti baik cuti tahunan maupun izin cuti kerja dengan dibayar, dilakukan atas persetujuan atasan langsung serta dengan mengajukan permohonan melalui sistem HR yang digunakan oleh Perusahaan;" dan ayat (2): "Permohonan cuti diajukan selambat-lambatnya tujuh 7 (tujuh) hari kerja sebelumnya dan/atau apabila dalam kondisi tertentu akan menyesuaikan dengan ketentuan dan keputusan dari atasan langsung dan Pimpinan Perusahaan;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |
| 2 | Cuti tahunan 12 hari per tahun, 14 hari kerja bila masa kerja di atas 3 tahun | Pasal 23 ayat (2) huruf a: "Karyawan berhak mendapatkan cuti tahunan sebanyak 12 (dua belas) hari selama satu tahun;" dan huruf h: "Karyawan dengan masa kerja diatas 3 (tiga) tahun berhak cuti selama 14 (empat belas) hari kerja;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |
| 3 | Sakit wajib diberitahukan ke atasan dan HR paling lambat pukul 10:00 WIB hari yang sama | Pasal 24 ayat (1): "Karyawan yang tidak dapat bekerja karena sakit atau dalam kondisi tidak sehat yang bukan disebabkan oleh kecelakaan kerja diharuskan untuk memberitahu atasannya dan HR selambat-lambatnya pukul 10:00 WIB di hari yang sama;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |

### USULAN
| # | Butir USULAN di spec | Pemutus yang disarankan |
|---|---|---|
| U1 | Enam klausul ISO di bagian 11 (9001 5.3, 7.5.3, 8.1; 27001 Annex A 6.2, 5.33, 5.34), label "(USULAN, dikonfirmasi konsultan)" | Konsultan, lalu owner |
| U2 | Pemetaan istilah sumber ke jabatan: Pimpinan Perusahaan = Direktur Utama; HR = HRGA Officer; keputusan atas nama Perusahaan = HR Manager (definisi bagian 3, tabel peran) | Samuel (Pimpinan Perusahaan), Aziz (HR dan Perusahaan) |
| U3 | Pelaku pemanggilan kembali karyawan yang sedang cuti: Atasan langsung (6.7) | Aziz |
| U4 | Pelaku pencatatan HRGA Officer: alfa sakit tanpa surat (6.3), cuti haid (6.5), pembatalan cuti (6.7); penerima surat keterangan dokter dan penerima pemberitahuan haid (6.3, 6.5) | Aziz |
| U5 | Pengecualian scope: hari libur resmi dan upah lembur (Pasal 22 ayat (1) sampai (3)), izin Pasal 29, pemutusan hubungan kerja (WFH berasal dari sumber) | Aziz |
| U6 | Pasal 26 ayat (6) dan Pasal 27 huruf e dibaca satu hak 2 hari (4.21) | Aziz, dengan Legal |
| U7 | Penerapan alur 6.1 (Pasal 32 ayat (1)) ke cuti melahirkan, pendampingan, cuti ibadah, dan cuti tanpa dibayar | Aziz |
| U8 | Label subjek Pasal 34 ayat (2) huruf a = karyawan di luar masa percobaan (4.34) | Aziz, dengan Legal |
| U9 | Urutan cuti mendesak: ajukan di sistem HR sesudah persetujuan atasan langsung (6.2 langkah 4) | Aziz |
| U10 | Penanggung jawab pengganti dicatat pada permohonan (6.1 langkah 3) | Aziz |
| U11 | Akibat penolakan cuti: karyawan tidak mengambil cuti (bagian 9) | Aziz |
| U12 | HR Manager menentukan sanksi alfa, surat peringatan, dan pemotongan cuti tahunan (bagian 9, tabel peran) | Aziz, dengan Samuel |
| U13 | Klasifikasi RESTRICTED (Internal) untuk permohonan cuti, surat dokter, dan HPL (4.37) | Aziz, dikonfirmasi owner |
| U14 | Lokasi

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Nama sistem HR yang dipakai Perusahaan untuk pengajuan cuti tidak tertulis di sumber | Aziz |
| 2 | Satuan hari: cuti tahunan "12 hari" tanpa kata kerja, "14 hari kerja", cuti khusus dan lainnya tanpa satuan. Hari kerja atau hari kalender belum diputus; definisi hari kerja belum ada | Aziz |
| 3 | Rumus prorata tidak ada; "penuh" bersanding "prorata" (Pasal 23 ayat (2) huruf c) | Aziz |
| 4 | Sisa cuti: batas 6 hari (huruf f) dan batas 30 Juni (huruf g) berurutan atau berdiri sendiri; perlakuan sisa di atas 6 hari tidak ada | Aziz |
| 5 | Cuti ulang tahun termasuk dalam 12 hari atau tambahan; kapan 14 hari mulai diberikan | Aziz |
| 6 | Pasal 26 ayat (6) dan Pasal 27 huruf e: satu hak 2 hari atau dua hak (4 hari) | Aziz, Legal |
| 7 | Pasal 34: tidak ada sanksi SP untuk alfa 1 hari karyawan di luar masa percobaan dan untuk alfa lebih dari 5 hari; rentang "SP Pertama sampai Kedua" tanpa penentu; penerbit SP dan pelaku pemotongan gaji tidak disebut | Aziz, Legal |
| 8 | Ambang sakit berkepanjangan (4 bulan berturut-turut atau "waktu yang lama" di Pasal 24 ayat (3), "terus-menerus" di Pasal 33 ayat (1)); "dan/atau" di Pasal 23 ayat (2) huruf b dan c (masa percobaan selesai atau 3 bulan, mana yang berlaku) | Aziz, Legal |
| 9 | Rujukan UU No. 13 Tahun 2003 Pasal 93 ayat (3) dikutip apa adanya dan belum dicek terhadap perubahan regulasi | Legal |
| 10 | Pasal 28: batas hari untuk ibadah kerohanian selain haji tidak ada (ayat (4) hanya "sesuai jangka waktu"); ayat (2) khusus karyawan beragama Islam | Aziz |
| 11 | Pasal 30: cuti tanpa dibayar tanpa batas maksimum hari | Aziz |
| 12 | Saluran pemberitahuan sakit, haid, dan kelahiran bayi (sistem HR, chat, atau email) tidak disebut; batas waktu keputusan atasan lan
