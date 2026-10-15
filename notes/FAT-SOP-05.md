# Catatan penyusun FAT-SOP-05: Tax Administration & Reporting

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-SOP-05.json. Mode sop, aksi T1, wave W3, nomor SNX-FAT-SOP-05 (nomor lama dipertahankan), department "Finance, Accounting & Tax", classification "INTERNAL" (worklist), audit_class C2. Approval persis dari config/defaults.json: prepared "Finance Staff", reviewed "Finance Lead", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Finance Lead" (jabatan tanpa nama): sumber tidak punya baris "Pemilik dokumen" (audit: owner_in_doc "tidak dicantumkan"; teks Drive dan docx tidak memuat tabel kontrol dokumen), sehingga dipakai aturan config/defaults.json process_owner: jabatan reviewer departemen.

Hasil uji terakhir (bukti mentah: /tmp/pen-FAT-SOP-05/lint.out.txt dan /tmp/pen-FAT-SOP-05/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-SOP-05.json /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "27 butir (USULAN) menunggu ACC" (setelah putaran perbaikan 2). Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- soffice ke PDF: 13 halaman. Diagram /tmp/pen-FAT-SOP-05/FAT-SOP-05_flow.png dilihat: tujuh simpul, rankdir TB, satu cabang putus-putus, teks terbaca.
- Pemeriksaan tambahan atas spec (skrip python3 -I): nol em-dash dan en-dash; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode SNX yang dirujuk di badan ada di tabel Dokumen terkait; tiap langkah paling banyak 25 kata (terpanjang 18); nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir), nol "komersil", nol "hutang", nol "ID Billing", nol singkatan "SDM".
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control tidak diubah. Berkas yang ditulis hanya specs/FAT-SOP-05.json dan notes/FAT-SOP-05.md; hasil render hanya di /tmp/pen-FAT-SOP-05/. Skrip pembuat spec ada di folder scratchpad sesi, bukan di repo.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 6. SOP Tax Administration & Reporting.docx (127108 byte) | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 | 2026-10-13T11:17:33.562Z (get_file_metadata hari ini, sama dengan prompt; fileSize 127108 sama dengan "bytes" di salinan audit; induk folder 1U4BP2va0dvAez_GhvMutaEf2EuLcyxrj = Dep. FAT) | read_file_content (teks penuh); download_file_content didekode ke /tmp/pen-FAT-SOP-05/src/src.docx dengan python3 -I: tanpa header, footer, comments.xml, maupun footnotes; satu tabel proses (5 baris); gambar word/media/image1.png dibuka dan cocok dengan deskripsi di salinan audit |
| Kriteria penerimaan | config/checklist.json baris 28 | tidak berlaku | Description: "SOP ini menjelaskan proses perhitungan, pembayaran, pelaporan dan pengarsipan dokumen perpajakan". Kolom iso_9001 dan iso_27001 kosong |
| Catatan cacat | context/audit/iso-sinux-supdocs-fat-2026-10-14.md bagian "SOP Tax Process" (dari baris 280, bagian 5 baris 369) dan sintesis baris 81 | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive dan docx |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Matriks Peran memuat "Finance Lead" dan "Finance Staff" dengan status "Belum dipetakan (K-13)"; nama peran dipakai apa adanya |
| Pembanding konsistensi (di luar sumber, dibaca saja) | specs/FAT-SOP-01.json (sibling W3) | repo kerja | Aktor penerbit Faktur Pajak, retensi "Minimal 10 tahun", lokasi "Folder Google Drive Departemen FAT". Retensi asli SOP Billing 8.2 dikutip dari salinan audit baris 166, bukan dibuka ulang di Drive |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Tahap Review & Approval dipegang Lead, 1 hari: rekonsiliasi di akhir Masa Pajak, lalu approval dan pengajuan payment | Tabel IV baris 3, sel Aktivitas: "Review & Approval" / "Rekonsiliasi nilai pajak terhutang di setiap akhir Masa Pajak" / "Proses approval dan pengajuan payment"; sel Waktu: "1 day"; sel PIC: "Lead" (baris dalam sel dipisah "/") | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| 2 | Tahap Pembayaran di tabel hanya membuat kode billing, 1 hari, Staff; tahap Pelaporan mengarsipkan bukti lapor, 1 hari, Lead | Tabel IV baris 4: "Pembayaran" / "Pembuatan kode billing" / "1 day" / "Staff". Baris 5: "Pelaporan" / "Pengarsipan dokumen bukti lapor (BPE, SPT, Kode billing dan bukti bayar)" / "1 day" / "Lead" | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |
| 3 | PPN Pemungut (WAPU/Kode 02) adalah penanganan khusus untuk transaksi dengan Instansi Pemerintah atau BUMN | Bagian III: "Penanganan khusus untuk PPN Pemungut (WAPU/Kode 02) atas transaksi dengan Instansi Pemerintah/BUMN." | 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87 |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan dan risiko yang dihindari | "Standard Operating Procedure (SOP) Tax Process ini disusun secara khusus untuk merinci alur kerja dan proses perpajakan guna memastikan akurasi perhitungan, ketepatan waktu pembayaran, serta kepatuhan pelaporan pajak (tax compliance) agar SINUX dapat terhindar dari risiko sanksi baik berupa denda, bunga administratif, maupun sengketa pajak di kemudian hari." (Latar Belakang) | Purpose kalimat 2 (kalimat tim, disingkat) |
| 2 | Pembagian tanggung jawab FAT dan divisi lain | "Memberikan panduan dan batasan tanggung jawab yang jelas antara tim FAT dan divisi lain yang terkait dalam mengeksekusi transaksi yang memiliki implikasi pajak." (Tujuan 2) | Purpose kalimat 3, peran Unit pengaju (USULAN) |
| 3 | Kewajiban yang dipatuhi | "Menjamin seluruh kewajiban menghitung, memotong/memungut, menyetor, dan melaporkan pajak (PPN, PPh PotPut, dan PPh Badan) dilaksanakan sesuai dengan peraturan perundang-undangan perpajakan yang berlaku." (Tujuan 1) | Kebijakan 4.1 |
| 4 | Ruang lingkup umum | "SOP ini berlaku untuk seluruh kegiatan operasional yang memiliki aspek perpajakan di proses bisnis SINUX. Meliputi namun tidak terbatas pada:" (III) | Scope paragraf 1 ("namun tidak terbatas pada" dibuang, lihat bagian 4 butir E) |
| 5 | PPN | "Penerbitan Faktur Pajak Keluaran atas setiap transaksi penjualan kepada customer;", "Pengkreditan Faktur Pajak Masukan", "Rekonsiliasi PPN setiap Masa Pajak." (III) | Scope paragraf 2 |
| 6 | PPh 21 | "Pemotongan PPh Pasal 21 atas gaji, bonus, dan tunjangan karyawan (termasuk metode Gross-Up dan penyesuaian akhir tahun);" (III) | Scope paragraf 3 |
| 7 | PPh 23/26 dan 4(2) | "Pemotongan/Pemungutan PPh Pasal 23/26 dan PPh Pasal 4 ayat (2) atas transaksi dengan pihak ketiga (vendor jasa, sewa, dan pengadaan infrastruktur);" (III) | Scope paragraf 3 |
| 8 | PPh Badan | "Perhitungan laba komersial dan fiskal, serta penyusunan SPT Tahunan PPh Badan;", "Perhitungan angsuran PPh Pasal 25 (jika ada);", "Rekonsiliasi semua kredit pajak yang bisa digunakan untuk perhitungan PPh Badan." (III) | Scope paragraf 4 |
| 9 | Administrasi | "Pembuatan ID Billing (untuk pembayaran pajak) dan pengelolaan Bukti Penerimaan Negara (BPN/NTPN);", "Pembuatan bukti lapor pajak bagi setiap Masa dan Tahun Pajak berjalan" (III) | Scope paragraf 5, definisi BPN/NTPN dan Kode billing |
| 10 | Pengarsipan untuk audit | "Filing (pengarsipan) dokumen perpajakan yang sistematis untuk persiapan audit (baik audit internal, eksternal, maupun pemeriksaan dari DJP)." (III) | Scope paragraf 5, kebijakan 4.4 |
| 11 | Tahap 1 Identifikasi | Tabel IV baris 1: "Identifikasi Aspek Pajak" / "Kelengkapan dokumen invoice/pengajuan" / "Analisis aspek pajak" / "1 day" / "Staff" | 6.1 langkah 1 dan 2 |
| 12 | Tahap 2 Perhitungan | Tabel IV baris 2: "Perhitungan pajak" / "Input hutang pajak di dokumen tracker" / "Pembuatan bukti potong (PPh PotPut)" / "Pembuatan Faktur Pajak Keluar (PPN)" / "1 day" / "Staff" | 6.2 langkah 1 sampai 4 |
| 13 | Peran di gambar | Gambar: "PIC: Finance Staff" (Identifikasi Aspek Pajak, Perhitungan Pajak, Payment), "PIC: Finance Lead" (Review & Approval, Pelaporan); label "1 Hari" dan "1 hari" | Nama peran tabel bagian 5, SLA bagian 8 |
| 14 | Isi kotak Pelaporan di gambar | Gambar: "Pelaporan:" / "BPE" / "SPT" / "Kode Billing" / "Bukti Bayar" | Definisi Bukti lapor, 6.5 langkah 2 |
| 15 | Tujuan 4 sumber, dibawa pada putaran perbaikan 2 | "Mengelola hak kompensasi pajak (Tax Asset) secara efektif dan memastikan terwujudnya ekualisasi antara Laporan Keuangan Komersial dan Surat Pemberitahuan (SPT) Pajak." (Tujuan 4, judul "Optimalisasi Arus Kas & Ekualisasi") | Kebijakan 4.6; definisi Ekualisasi dan Hak kompensasi pajak (Tax Asset) |
| 20 | Tujuan 3 sumber (mitigasi risiko) | "Mencegah terjadinya keterlambatan penyetoran dan pelaporan pajak, kesalahan penerbitan faktur pajak, serta menghindari potensi kesalahan pada Laporan Keuangan akibat ketidaksesuaian pencatatan utang/piutang pajak." (Tujuan 3, judul "Mitigasi Risiko") | Kebijakan 4.2 |
| 16 | Retensi 10 tahun (bahan USULAN, bukan sumber SOP ini) | "Retensi: minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001/ISO 27001." (SOP Billing 8.2, salinan audit baris 166) | records bagian 11 |
| 17 | Batas wewenang keuangan (bahan kolom Authority) | "Batas wewenang semua jabatan: keputusan keuangan, legal, perubahan kontrak, pengangkatan atau pemutusan hubungan kerja, dan perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." (specs/HR-ORG-01.json, Matriks Peran) | Peran Finance Lead, kolom Authority |
| 18 | Aktor penerbit Faktur Pajak di SOP Billing (bahan open item 7) | "Terbitkan e-Faktur Pajak di CoreTax DJP dengan PPN sesuai DPP transaksi (butir 4.5)." (specs/FAT-SOP-01.json, langkah, PIC Finance Staff) | Open item 7 |
| 19 | Kriteria baris | "SOP ini menjelaskan proses perhitungan, pembayaran, pelaporan dan pengarsipan dokumen perpajakan" (config/checklist.json baris 28) | Pemetaan di bagian 3 |

## 3. Pemetaan kriteria (Description baris 28)

| Unsur kriteria | Di dokumen | Sumber |
|---|---|---|
| perhitungan | Butir 6.1 (identifikasi aspek pajak), 6.2 (perhitungan, bukti potong, Faktur Pajak Keluaran), 6.3 langkah 1 (rekonsiliasi) | Tabel IV baris 1 sampai 3 |
| pembayaran | Butir 6.3 langkah 3 (pengajuan pembayaran), 6.4 (kode billing; penyetoran dan BPN/NTPN berlabel USULAN) | Tabel IV baris 3 dan 4; scope III.4 |
| pelaporan | Butir 6.5 langkah 1 (SPT dan BPE) | Tabel IV baris 5; gambar |
| pengarsipan | Butir 6.5 langkah 2 (bukti lapor) dan 3 (bukti potong dan Faktur Pajak Keluaran, USULAN); kebijakan 4.4; tabel rekaman | Tabel IV baris 5; scope III.4 |

Pengarsipan tidak dibuat sub-proses 6.x sendiri karena sumber menaruhnya di tahap Pelaporan dengan satu batas 1 hari; memecahnya menambah angka yang tidak ada di sumber.

Klausul ISO (checklist tidak memberi acuan, semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur dan SLA |
|---|---|---|---|
| ISO 9001:2015 5.3 | Ya, "5.3 (Peran, tanggung jawab, dan wewenang organisasi)" | 4.3: Finance Lead menyetujui utang pajak yang dihitung Finance Staff | 6.3; tabel peran |
| ISO 9001:2015 7.5.3 | Ya, "7.5.3 (Pengendalian informasi terdokumentasi)" | 4.4: arsip dokumen perpajakan, lokasi, pemilik, retensi | 6.5 langkah 2 dan 3; tabel rekaman |
| ISO 9001:2015 8.1 | Ya, "8.1 (Perencanaan dan pengendalian operasional)" | 4.2: lima tahap berurutan, batas waktu di bagian 8 | 6.1 sampai 6.5; bagian 8 |
| ISO/IEC 27001:2022 Annex A 5.31 | Ya, "Annex A 5.31 (Persyaratan hukum, undang-undang, regulasi, dan kontrak)" | 4.1: kepatuhan terhadap peraturan perpajakan, termasuk batas waktu setor dan lapor | 6.2 sampai 6.5 |
| ISO/IEC 27001:2022 Annex A 5.33 | Ya, "5.33 (Perlindungan rekaman)" | 4.4 dan 4.5: arsip dan klasifikasi rekaman | 6.5; tabel rekaman |

Nomor dan nama klausul berasal dari standar, bukan dari dokumen tim, dan ditulis dari ingatan penyusun tanpa membuka teks standar (tidak diukur ulang di sesi ini). Klausul SOP Billing yang lain (8.2, 8.5, A.5.12, A.5.15, A.8.5) tidak dibawa karena tidak relevan ke proses pajak.

## 4. Penanganan cacat context/audit

Bagian 5 "SOP Tax Process" di context/audit/iso-sinux-supdocs-fat-2026-10-14.md (fileId 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tanpa nomor, revisi, tanggal, pemilik, penyetuju, klasifikasi, riwayat revisi; nama berkas "Tax Administration & Reporting" berbeda dari judul isi "Tax Process" | Teratasi template dan defaults: nomor SNX-FAT-SOP-05, Rev 00, Draft, tanggal dan tanda tangan kosong, pemilik Finance Lead, klasifikasi INTERNAL. Judul dokumen mengikuti checklist dan worklist ("Tax Administration & Reporting"); badan dokumen tidak memakai "Tax Process" dan menyebut diri "SOP ini". Open item 14 |
| 2 | Penomoran bagian campuran | Teratasi template 11 bagian dan 6.x |
| 3 | Ruang lingkup luas, proses 5 langkah generik, tanpa pembeda per jenis pajak, tanpa tenggat statutori, tanpa portal atau bank | Diperbaiki sebagian: butir 6.1 menyatakan lima tahap berlaku untuk semua jenis pajak dan menyebut bagian yang belum punya alur sendiri (USULAN). Kebijakan 4.1 mewajibkan batas waktu setor dan lapor menurut peraturan tanpa menyalin tanggalnya. Tenggat, nama portal, dan bank tidak ditulis karena tidak ada di sumber. Open item 3, 5, 7 |
| 4 | Langkah Pembayaran hanya kode billing; NTPN tidak di tabel; approval tanpa form dan batas wewenang | Diperbaiki sebagian: langkah penyetoran dan pencatatan BPN/NTPN ditambahkan di 6.4 dengan Finance Staff sebagai pelaku (USULAN, dasar scope III.4 dan "Bukti Bayar" di gambar). Persetujuan dicatat di SNX-FAT-FRM-01 (USULAN, dasar checklist baris 30). Batas wewenang mengikuti delegasi tertulis (kalimat Matriks Peran HR-ORG-01). Open item 2 |
| 5 | Gambar dan tabel memakai label berbeda ("Payment" lawan "Pembayaran"; "Pelaporan" tanpa kata pengarsipan; "Finance Staff/Lead" lawan "Staff/Lead") | Diperbaiki: satu istilah per hal ("Pembayaran", "Pelaporan dan pengarsipan", "Finance Staff", "Finance Lead"); gambar digambar ulang sebagai diagram alir tujuh simpul dengan panah |
| 6 | "Finance Staff" dan "Finance Lead" bukan jabatan di Job Analysis | Tidak dipetakan ke orang: config/defaults.json data_conflicts memutus "peran apa adanya di SOP Billing dan Tax", dan HR-ORG-01 K-13 mencatat belum dipetakan. Jabatan terdekat yang tercatat untuk catatan ini: JA-10 Finance dan JA-11 Accounting & Tax; tidak ditulis di dokumen. Open item 1 |
| 7 | Tanpa rujukan ISO, klasifikasi, masa retensi | Diperbaiki: klausul bagian 3 di atas (USULAN), klasifikasi INTERNAL untuk SOP dan RESTRICTED (Internal) untuk rekaman (USULAN 4.5), retensi minimal 10 tahun (USULAN, dari SOP Billing 8.2). Open item 12 |
| 8 | "Dokumen tracker" tanpa nama dan lokasi | Istilah sumber dipertahankan ("dokumen tracker"); lokasi diusulkan "Folder Google Drive Departemen FAT" (USULAN). Open item 10 |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | "Faktur Pajak Keluar" (tabel) lawan "Faktur Pajak Keluaran" (scope) | Satu istilah: "Faktur Pajak Keluaran" |
| B | "ID Billing" (scope) lawan "kode billing" (tabel dan gambar) untuk hal yang sama | Satu istilah: "kode billing" |
| C | "BuPot", "PPh PotPut" lawan "bukti potong", "PPh Potong dan Pungut" | Satu istilah: "bukti potong", "PPh Potong dan Pungut" |
| D | "hutang pajak" dan "pajak terhutang" untuk hal yang sama; ejaan baku "utang" | Satu istilah baku: "utang pajak" |
| E | "Meliputi namun tidak terbatas pada" membuat scope terbuka | Dibuang; diganti daftar pengecualian berlabel USULAN karena sumber diam |
| F | Dua butir "Rekonsiliasi PPh Potong dan Pungut" tanpa tanda baca akhir, satu per masa dan satu per akhir tahun | Digabung dalam satu kalimat Scope paragraf 3 |
| G | "1 day" (Inggris) dan "1 Hari", "1 hari" | Satu bentuk "1 hari"; satuan hari kerja diusulkan di definisi "Hari" (USULAN) |
| H | Bagian Latar Belakang sumber (profil SINUX: IT Services, customer swasta dan Instansi Pemerintah, vendor) tidak punya padanan di 11 bagian template | Profil tidak dibawa; kalimat sasaran risiko dipakai di Purpose. Instansi Pemerintah dan BUMN tetap muncul di scope dan pengecualian |
| I | Singkatan BPE, WAPU, Kode 02 tanpa uraian di sumber | BPE diuraikan berlabel USULAN; WAPU dan Kode 02 dipakai sebagai nama penanganan, tanpa uraian singkatan. Open item 9 |
| J | Tarif PPN: SOP Billing sumber menulis 12% dan satu kali 11% (audit Billing butir 4) | Tarif tidak ditulis di SOP ini sama sekali, sehingga tidak ada rumusan PPN kedua. Open item 8 |

Aturan lintas dokumen dari RUNBOOK §6 yang tidak terpakai: sumber tidak menyebut tiket, Zammad, GLPI, vault, COO, maupun Samuel di badan (Samuel hanya di blok Approved By sebagai "President Director"), sehingga aturan sebutan "Direktur (COO)" dan "Direktur Utama" tidak terpicu. Sumber tidak memuat rujukan internal AI; tidak ada yang dibuang.

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Pelaku "Pelaporan" (6.5 langkah 1) adalah Finance Lead: tabel dan gambar memberi PIC Lead pada tahap Pelaporan, sedangkan kalimat sumber hanya menulis pengarsipan.
2. "Review" pada tahap Review & Approval diwujudkan lewat rekonsiliasi (6.3 langkah 1); sumber tidak menulis langkah memeriksa hasil hitung Staff secara terpisah dan saya tidak menambahkannya.
3. "Approval dan pengajuan payment" dipecah jadi dua langkah (setujui, ajukan) agar satu langkah satu tindakan. Penerima pengajuan tidak ditulis karena tidak ada di sumber (open item 2).
4. "Pembuatan bukti lapor" (scope III.4) dipetakan ke keluaran "SPT dan BPE" di 6.5 langkah 1, karena BPE dan SPT adalah bukti lapor menurut tahap Pelaporan.
5. Pemilik rekaman: tracker ke Finance Staff (pencatat, 6.2 langkah 2), semua arsip ke Finance Lead (pelaku pengarsipan 6.5). Pemisahan menetapkan (Finance Lead) lawan mencatat (Finance Staff) mengikuti tabel sumber.
6. Definisi Aspek pajak, Ekualisasi, Hak kompensasi pajak (Tax Asset), Faktur Pajak Masukan, Masa Pajak, Tahun Pajak, Utang pajak, PPh Badan, DJP adalah penjelasan penyusun yang diturunkan dari kata sumber atau pengetahuan umum perpajakan, bukan kutipan sumber. "Surat Pemberitahuan pajak" dan "Bukti Penerimaan Negara" datang dari sumber (Tujuan 4 dan scope III.4). Rincian tarif, tenggat, dan prosedur pajak tidak dimasukkan ke definisi.
7. Klasifikasi: worklist memberi INTERNAL untuk SOP, dipakai persis. Aturan config/defaults.json menyebut data keuangan RESTRICTED (Internal) bila worklist null; karena worklist terisi, SOP tetap INTERNAL dan hanya rekaman perpajakan diusulkan RESTRICTED (Internal) di kebijakan 4.5.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Acuan klausul ISO 9001:2015 5.3, 7.5.3, 8.1 dan ISO/IEC 27001:2022 Annex A 5.31, 5.33 (label "USULAN, perlu konfirmasi konsultan") | Bagian 4 (judul butir) dan bagian 11 | owner |
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
| 14 | Retensi minimal 10 tahun untuk rekaman perpajakan (disamakan dengan SOP Billing) | Bagian 11, tabel rekaman | FAT dan Legal |
| 15 | Cara Finance Lead memeriksa kepatuhan (bandingkan rekaman bagian 11 dengan batas waktu bagian 8) | Bagian 10 kalimat 1 | FAT |
| 16 | Finance Lead sebagai pelaku pengelolaan hak kompensasi pajak (Tax Asset) dan ekualisasi; langkah rinci belum ada | Kebijakan 4.6; bagian 5 baris Finance Lead; definisi Ekualisasi dan Hak kompensasi pajak | FAT |
| 17 | Arti "pengajuan" = permintaan agar sebuah pembayaran diproses, dipakai untuk kiriman Unit pengaju dan untuk permintaan bayar pajak oleh Finance Lead | Bagian 3, baris Pengajuan | FAT |

Jumlah: 17 USULAN. Di dokumen ada 27 penanda "(USULAN)" yang dihitung lint (sesudah putaran perbaikan 2): 8 di tabel rekaman (butir 13 dan 14, empat baris masing-masing), 1 baris definisi "(USULAN)" itu sendiri, dan 1 tiap di Scope (butir 8), definisi BPE (11), definisi Hari (10), definisi Pengajuan (17), kebijakan 4.5 (12), peran Finance Lead (16), peran Unit pengaju (9), peran Finance Staff kolom Responsibilities dan kolom Authority (butir 3, dua penanda), intro 6.1 (2), 6.3 langkah 2 dan Dokumen terkait FRM-01 (5, dua penanda), 6.4 langkah 2 dan 3 (3, dua penanda), 6.5 langkah 3 (4), bagian 9 baris 2 (7), Dokumen terkait SOP-04 (6), dan Kesimpulan (15). Di luar hitungan lint: satu kata USULAN di keterangan gambar dan di simpul diagram "Setor pajak, catat BPN/NTPN", serta penanda "(USULAN: Finance Lead sebagai pelaku)" di kebijakan 4.6 dan label ISO "(USULAN, perlu konfirmasi konsultan)". Label ISO memakai bunyi sweep, yang terbaca sebagai menunggu konfirmasi. Process owner "Finance Lead" dan tiga nama di blok approval berstatus USULAN di config/defaults.json, tidak diberi label di dokumen karena Master List yang memuatnya.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Finance Lead dan Finance Staff belum dipetakan ke jabatan atau orang (HR-ORG-01 K-13; jabatan terdekat JA-10 Finance dan JA-11 Accounting & Tax, tidak berlevel). Tanpa pemetaan, auditor tidak bisa menunjuk siapa memegang peran; ditutup W9: dipetakan lewat definisi bagian 3 sebagai USULAN sampai jabatan Finance Lead terisi | owner |
| 2 | Pengajuan pembayaran: sumber tidak menyebut penerima pengajuan, siapa yang melepas dana, siapa yang menyetor, batas wewenang approval, maupun form yang dipakai. Dokumen memakai Finance Lead untuk menyetujui dan mengajukan, Finance Staff untuk menyetor (USULAN) | FAT dan Samuel |
| 3 | Tenggat statutori setor dan lapor per jenis pajak tidak ada di sumber maupun di dokumen ini; tidak ada penanganan untuk keterlambatan, denda, atau SPT pembetulan. Tahap 1 hari tidak menjamin tenggat peraturan | FAT |
| 4 | Arti "1 day": hari kerja atau hari kalender, titik mulai (sesudah tahap sebelumnya selesai atau sejak dokumen diterima), dan apakah 1 hari masuk akal untuk SPT Tahunan PPh Badan, laba fiskal, dan PPh Pasal 21 akhir tahun | FAT |
| 5 | Alur per jenis pajak: PPh Pasal 21 (Gross-Up, penyesuaian akhir tahun), pengkreditan Faktur Pajak Masukan, angsuran PPh Pasal 25, laba komersial dan fiskal, rekonsiliasi kredit pajak punya butir scope tetapi tidak punya langkah sendiri | FAT |
| 6 | Tujuan 4 sumber (hak kompensasi pajak atau Tax Asset, ekualisasi) kini ada di kebijakan 4.6 dengan Finance Lead sebagai pelaku (USULAN), tetapi bagian 6 belum punya langkah yang menghasilkannya dan tabel rekaman belum memuat dokumen ekualisasi. Perlu langkah dan rekaman baru | FAT |
| 7 | Tumpang tindih penerbitan Faktur Pajak Keluaran: SNX-FAT-SOP-01 menulis Finance Staff menerbitkan e-Faktur Pajak di CoreTax DJP pada penagihan, sedangkan 6.2 langkah 4 SOP ini memuatnya di tahap perhitungan. Perlu satu pemilik langkah dan satu waktu terbit. Nama portal pajak dan bank tidak ada di sumber SOP ini | FAT |
| 8 | Tarif PPN tidak ditulis di SOP ini. SOP Billing sumber memuat 12% dan satu kali 11%; satu rumusan PPN menunggu keputusan FAT | FAT |
| 9 | Arti "pengajuan" di "invoice/pengajuan" tidak ada di sumber; dokumen memakai satu arti "permintaan agar sebuah pembayaran diproses" (USULAN, sejalan dengan checklist baris 25 "pengajuan pembayaran invoice, reimbursement dan cash advance"), identitas "divisi lain yang terkait", dan uraian singkatan WAPU, Kode 02, BPE tidak ada di sumber | FAT |
| 10 | Nama dan lokasi "dokumen tracker" tidak ada di sumber. Perlu diputus apakah memakai Register Penagihan dan Penjualan milik SOP Billing atau dokumen terpisah | FAT |
| 11 | Pengarsipan hardcopy (bukti potong asli, faktur cetak), pemusnahan arsip pajak setelah retensi, dan siapa yang menyetujui pemusnahan tidak ada di sumber. SOP Billing menulis Berita Acara Pemusnahan Dokumen disetujui Finance Lead dan CEO | FAT dan Samuel |
| 12 | Klasifikasi: SOP berlabel INTERNAL (worklist) sedangkan rekaman perpajakan diusulkan RESTRICTED (Internal). Perlu konfirmasi bahwa pemisahan itu yang dikehendaki | owner |
| 13 | Tiket: sumber tidak memakai tiket. Jalur Unit pengaju menyerahkan invoice atau pengajuan (email, Google Form, atau tiket GLPI untuk generalist) tidak ada; batas "generalist" belum dirinci owner | owner |
| 14 | Judul: berkas Drive bernama "SOP Tax Administration & Reporting", isi sumber menyebut "SOP Tax Process". Dokumen memakai judul checklist; perlu konfirmasi tim FAT | FAT |
| 15 | Penanganan yang tidak ada di sumber dan tidak dikarang: selisih hasil rekonsiliasi, penolakan pengajuan pembayaran oleh Finance Lead, kesalahan faktur pajak, dan pemeriksaan DJP. Bagian 9 hanya memuat dua kondisi | FAT |
| 16 | Hubungan kebijakan 4.3 (Finance Lead menyetujui) dengan kewenangan Direktur Utama atas pembayaran: sumber tidak menyebutnya, dokumen tidak menyebut Direktur Utama atau COO di badan | Samuel |

## 6. Dua pertanyaan penutup

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI, dan perbaikannya.

| Temuan pada draf awal | Perbaikan |
|---|---|
| Kebijakan 4.3 menyalin isi tabel peran (siapa melakukan apa) dalam tiga kalimat pendek berpola sama | Ditulis ulang jadi satu fakta (Finance Lead menyetujui utang pajak yang dihitung Finance Staff) dan satu rujukan ke bagian 5 |
| Pembuka kalimat 2 Purpose memakai "dengan akurat" dan tiga anak kalimat berurutan | Dipendekkan menjadi "dihitung akurat, dibayar tepat waktu, dan dilaporkan sesuai peraturan" |
| Intro tentang "lima tahap berlaku untuk semua jenis pajak" ada di 6.2, jauh dari awal prosedur | Dipindah ke intro 6.1 supaya aturan berlaku dibaca sebelum langkah pertama |
| Ejaan "unit pengaju" huruf kecil di Purpose lawan "Unit pengaju" sebagai nama peran | Disamakan menjadi nama peran "Unit pengaju" |
| Kata "sumber" dan "sumber tim" bergantian untuk satu hal | Dihapus dari badan dokumen pada putaran perbaikan 1 (bagian 7); asal-usul hanya ada di notes |
| Kesimpulan awal meringkas ulang isi dokumen | Diganti dua kalimat tentang pemeriksaan kepatuhan dan peninjauan tahunan, tanpa ringkasan |
| Retensi ditulis "10 tahun" padahal kalimat sumber SOP Billing "minimal 10 (sepuluh) tahun" | Diganti "Minimal 10 tahun (USULAN)" dan lokasi disamakan dengan sibling |

Sisa yang disengaja: dua kelompok tiga di Purpose ("akurat, tepat waktu, sesuai peraturan"; "denda, bunga administratif, dan sengketa pajak") berasal dari kalimat tim dan dipertahankan sesuai aturan T1. Scope panjang karena butir tim dibawa utuh. Label "(USULAN)" sering muncul karena sumber memang tidak memuat penyetoran, arsip bukti potong, klausul ISO, retensi, dan lokasi simpan; menghapus label akan menyamarkan tambahan penyusun.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber, dan perbaikannya.

| Butir | Asal | Status |
|---|---|---|
| "1 hari" per tahap, PIC Staff dan Lead | Tabel IV dan gambar | Bersumber |
| "Minimal 10 tahun" | SOP Billing 8.2 (salinan audit), bukan sumber SOP ini | Berlabel USULAN di dokumen; basis di notes |
| Nomor dan nama klausul ISO | Standar, bukan dokumen tim; ditulis dari ingatan penyusun | Berlabel "USULAN, perlu konfirmasi konsultan"; tidak diukur ulang |
| Nomor Pasal 21, 23/26, 4(2), 25; Kode 02 | Scope III | Bersumber |
| "Folder Google Drive Departemen FAT" | Pola di specs/FAT-SOP-01.json | Berlabel USULAN |
| Kode SNX-FAT-SOP-01, -04, FRM-01, ISMS-PRO-01, HR-ORG-01 | config/worklist.json dan checklist baris 23, 26, 30 | Nama dokumen cocok worklist; FRM-01 dan SOP-04 belum selesai disusun, isinya tidak dikutip selain judul checklist |
| Uraian BPE | Pengetahuan umum | Berlabel USULAN |
| Uraian DJP, Masa Pajak, Tahun Pajak, Faktur Pajak Masukan, Utang pajak, PPh Badan, Aspek pajak | Pengetahuan umum dan kata sumber | Tidak berlabel; dicatat di asumsi 6 sebagai penjelasan penyusun tanpa angka, tarif, atau tanggal |
| Nama orang | Hanya Samuel Kristanto Utomo di blok approval, dari config/defaults.json | Bersumber |
| Tanggal, tarif PPN, tenggat, nama portal, nama bank | Tidak ada | Tidak ditulis. Pemindaian angka di spec: hanya nomor butir, "1 hari", "10 tahun", Pasal, nomor klausul, dan Kode 02 |

Tidak ada butir tanpa sumber yang tersisa tanpa label atau catatan.

## 7. Putaran perbaikan 1 (dari orkestrator, verifikasi PASS)

Temuan terberat: badan dokumen memuat catatan asal-usul draf. Semua frasa itu dikeluarkan dari spec; isi catatannya sudah ada di notes (bagian 4, USULAN, Open items) dan tidak diubah.

| Lokasi di dokumen | Sebelum | Sesudah | Catatan asal-usul ada di |
|---|---|---|---|
| Bagian 2, pengecualian | "... Sumber tim tidak memuat pengecualian; daftar ini diturunkan dari batas SOP perpajakan (USULAN)." | Daftar pengecualian diakhiri "(USULAN)" | Bagian 4 butir E; USULAN 8 |
| Intro 6.1 | "Sumber tim hanya merinci PPN keluaran dan PPh Potong dan Pungut. Alur tersendiri ... belum ada, sehingga langkah yang sama dipakai ..." | "Tahap 6.1 sampai 6.5 berlaku untuk semua jenis pajak di bagian 2 dengan langkah yang sama; alur terpisah per jenis pajak belum ada (USULAN)." | Bagian 4 butir 3; USULAN 2; open item 5 |
| Intro 6.4 | "Sumber tim hanya menyebut pembuatan kode billing ... ditambahkan dari ruang lingkup dan gambar alur sumber tim ..." | "Finance Staff menyetor pajak dan mencatat BPN/NTPN sesudah membuat kode billing (USULAN)." | Bagian 4 butir 4; USULAN 3; open item 2 |
| Definisi BPE, definisi Hari, peran Unit pengaju, bagian 9 baris 2 | Tanda kurung "(USULAN: sumber tim menulis ...)" | "(USULAN)" polos | Bagian 4 butir G dan I; USULAN 7, 9, 10, 11; open item 4, 9, 15 |

Nonblocking dari qa/FAT-SOP-05.verify.r1.json yang dirapikan:

| Temuan | Tindakan |
|---|---|
| 4.2 "untuk tiap transaksi" bertentangan dengan 6.3 (per akhir Masa Pajak) dan 6.5 (per Masa dan Tahun Pajak) | Frasa "untuk tiap transaksi yang punya aspek pajak" dibuang; 4.2 hanya menyebut lima tahap berurutan. Titik mulai dan satuan hari tetap open item 4 |
| Sinonim "masa simpan" lawan "Retensi" | 4.4 memakai "retensi" |
| Sinonim "menetapkan/penetapan" lawan "menyetujui" | Kolom Authority Unit pengaju: "Tidak menyetujui utang pajak; persetujuan ada pada Finance Lead (butir 6.3)" |
| Sinonim "Divisi" (definisi Unit pengaju) lawan "departemen" (definisi FAT) | Definisi Unit pengaju: "Departemen SINUX di luar FAT ..." |
| Finance Staff menyetor tanpa wewenang menyetor di kolom Authority | Ditambah "menyetor pajak sesudah Finance Lead mengajukan pembayaran (USULAN)". Siapa berwenang melepas dana tetap open item 2 |
| Label "Hasil yang dijaga:" terbaca seperti isian | Diganti "Dengan SOP ini pajak dihitung akurat, ..."; dua kelompok tiga tetap karena kalimat tim (T1) |
| Tumpang tindih Faktur Pajak Keluaran dengan SNX-FAT-SOP-01 | Tidak diubah di dokumen; open item 7 (butuh keputusan pemilik langkah) |
| Klasifikasi INTERNAL lawan saran audit restricted:finance | Tidak diubah (worklist menetapkan INTERNAL); open item 12 |

Uji ulang: render_sop.py tanpa galat; lint_doc.py sop "pass": true, fails kosong, warns hanya "23 butir (USULAN)", warn PIC SLA nol; validator OOXML "All validations PASSED!". Bukti: /tmp/pen-FAT-SOP-05/lint.out.txt dan /tmp/pen-FAT-SOP-05/validate.out.txt. Pemeriksaan spec: nol "sumber tim", nol "penyusun" sebagai pelaku, nol em-dash dan en-dash, tiap langkah paling banyak 25 kata, semua PIC ada di tabel peran.

## 8. Putaran perbaikan 2 (dari orkestrator, verifikasi PASS)

| Temuan | Tindakan |
|---|---|
| Tujuan 4 sumber (Tax Asset, ekualisasi) tidak terbawa; T1 mewajibkan substansi tim | Kebijakan 4.6 baru: "Finance Lead mengelola hak kompensasi pajak (Tax Asset) dan memastikan ekualisasi antara Laporan Keuangan Komersial dan SPT. Langkah rincinya belum ada di bagian 6 (USULAN)." Definisi Ekualisasi dan Hak kompensasi pajak (Tax Asset) ditambah. Kutipan sumber: bagian 2 baris 15 notes. Pelaku Finance Lead adalah USULAN karena sumber tidak menyebut pelaku. Open item 6 diperbarui |
| Butir Tujuan 3 (keterlambatan setor dan lapor, salah faktur, salah catat utang/piutang pajak) tidak terbawa | Kebijakan 4.2 memuat tiga hal itu sebagai tujuan pengendalian proses. "Piutang pajak" tidak ditulis karena tidak didefinisikan di sumber; hanya "utang pajak". Kutipan: bagian 2 baris 20 notes |
| Simpul diagram "setor pajak, catat BPN/NTPN" tanpa label USULAN | Simpul dipecah: "Buat kode billing (butir 6.4)" bersumber, "Setor pajak, catat BPN/NTPN (butir 6.4, USULAN)" berlabel. Keterangan gambar menyebut dua cabang USULAN. Diagram kini delapan simpul, rankdir TB. Langkah 2 dan 3 di 6.4 serta kolom Responsibilities Finance Staff berlabel (USULAN); intro 6.4 dibuang karena mengulang langkah di bawahnya |
| Kata "pengajuan" dipakai untuk dua hal | Satu arti dipilih dan didefinisikan: "Permintaan agar sebuah pembayaran diproses (USULAN)". Kiriman Unit pengaju ("invoice atau pengajuan") dan permintaan bayar pajak oleh Finance Lead memakai arti itu; yang berbeda hanya penerbitnya. Dasar: checklist baris 25 memakai "pengajuan pembayaran" untuk permintaan bayar. Open item 9 diperbarui |
| Purpose kalimat 2 pasif | Ditulis aktif dengan pelaku: "Finance Staff dan Finance Lead menghitung pajak dengan akurat, membayarnya tepat waktu, dan melaporkannya sesuai peraturan, ..." Dua kelompok tiga tetap karena kalimat tim (T1) |
| Pengulangan isi (intro 6.4; pengecualian WAPU menyalin langkah 6.2.4) | Intro 6.4 dibuang. WAPU/Kode 02 hanya ada di bagian 9 (kondisi khusus) dan di definisi; langkah 4 di 6.2 tidak lagi memuatnya |
| "di luar Faktur Pajak Keluaran" ambigu; tanda baca memisahkan label | Diganti "kecuali Faktur Pajak Keluaran"; label menempel di kalimat: "... dokumen perpajakan (USULAN)." |
| Register "punya"; "aspek perpajakan" lawan "aspek pajak" | Semua "punya" menjadi "memiliki"; "aspek perpajakan" menjadi "aspek pajak" (istilah yang didefinisikan) |
| Tumpang tindih Faktur Pajak Keluaran dengan SNX-FAT-SOP-01 | Tidak diubah di dokumen; open item 7 |
| "(USULAN, dikonfirmasi konsultan)" terbaca seolah sudah dikonfirmasi | Tidak diubah: label itu ditetapkan verbatim oleh prompt tugas; koreksi serentak antar-spec adalah keputusan orkestrator |
| Konfirmasi data_conflicts, approval, cacat audit | Tidak ada tindakan; dicatat |

Uji ulang: render_sop.py tanpa galat; lint_doc.py sop "pass": true, fails kosong, warns hanya "27 butir (USULAN)", warn PIC SLA nol; validator OOXML "All validations PASSED!". Bukti: /tmp/pen-FAT-SOP-05/lint.out.txt dan /tmp/pen-FAT-SOP-05/validate.out.txt. Pemeriksaan spec: nol "punya", nol "aspek perpajakan", nol "sumber tim", nol em-dash dan en-dash, tiap langkah paling banyak 25 kata, semua PIC ada di tabel peran, diagram dilihat (delapan simpul, TB).

## Sweep

Putaran sweep dari orkestrator (berkas /tmp/claude-0/prompts/FAT-SOP-05.sweep.txt). Dua butir diubah; diff spec sebelum lawan sesudah hanya tiga baris. Fakta, angka, nama, dan struktur lain tetap.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1. Pelaku Finance Lead di 4.6, kebijakan | "4.6 ... Finance Lead mengelola hak kompensasi pajak (Tax Asset) dan memastikan ekualisasi antara Laporan Keuangan Komersial dan SPT. Langkah rincinya belum ada di bagian 6 (USULAN)." Label hanya menempel di kalimat langkah, bukan di pelaku | "4.6 ... Finance Lead mengelola hak kompensasi pajak (Tax Asset) dan memastikan ekualisasi antara Laporan Keuangan Komersial dan SPT (USULAN: Finance Lead sebagai pelaku). Bagian 6 belum memuat langkah rinci untuk butir ini." |
| 1. Selaras dengan bagian 5, baris Finance Lead kolom Responsibilities | "... mengarsipkan dokumen perpajakan (butir 6.3 dan 6.5)." Tanpa tugas Tax Asset dan ekualisasi, sehingga 4.6 menyebut pelaku yang tidak tercatat di tabel peran | "... mengarsipkan dokumen perpajakan (butir 6.3 dan 6.5). Mengelola hak kompensasi pajak (Tax Asset) dan memastikan ekualisasi menurut butir 4.6 (USULAN)." Kolom Authority tidak diubah |
| 2. Label ISO, bagian 11 baris "Status acuan klausul" | "(USULAN, dikonfirmasi konsultan)" | "(USULAN, perlu konfirmasi konsultan)". Hanya satu kemunculan di spec; rujukan hidup di notes ikut diubah, riwayat putaran 1 dan 2 dibiarkan apa adanya |

Pemutus USULAN pelaku Finance Lead tetap FAT (USULAN 16). Jumlah penanda "(USULAN)" yang dihitung lint tetap 27: kebijakan 4.6 tidak lagi dihitung (berbentuk "USULAN:" bukan "(USULAN)"), baris Finance Lead di bagian 5 menambah satu.

Uji (bukti: /tmp/pen-FAT-SOP-05/lint.out.txt, validate.out.txt, blankscan.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-SOP-05.json /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx`: tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx sop`: "pass": true, fails kosong, warns hanya "27 butir (USULAN) menunggu ACC"; warn PIC SLA nol.
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx`: "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-FAT-SOP-05/FAT-SOP-05.docx`: "ok 13 FAT-SOP-05.docx []".


## ISO-W9

Round perbaikan ISO-W9 (LEAD G-3 A6). Fakta, angka, dan struktur lain tetap. Rujukan silang yang diubah: hanya baris SNX-HR-ORG-01 di bagian 11 FAT-SOP-01 (di atas).

| Butir | Sebelum | Sesudah |
|---|---|---|
| Blok Reviewed (meta.approval.reviewed) | Finance Lead | Amirull Yusuf Zulkarnain / Direktur |
| Bagian 3 Definisi | Tanpa istilah Finance Lead dan Finance Staff | Dua baris baru, isi persis LEAD G-3 A6 (lihat teks di FAT-SOP-01 W9). Tidak ada kalimat pemetaan lain yang perlu diselaraskan |
| R2: Open item 1 (baris notes) | Tanpa catatan W9 di baris | Ditambah "ditutup W9: dipetakan lewat definisi bagian 3 sebagai USULAN sampai jabatan Finance Lead terisi" |

Open item:

- K-13 (Finance Lead dan Finance Staff belum dipetakan ke jabatan): ditutup W9: dipetakan lewat definisi bagian 3 sesuai keputusan owner 15 Okt ("finance lead belum ada"), berlabel USULAN; baris lama tidak dihapus.
- Pemetaan Finance Lead dan Finance Staff ke jabatan: status berubah W9: berlaku sebagai USULAN sampai jabatan Finance Lead terisi.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Label butir 4.6 dipindah ke akhir butir dan ditulis sebagai kalimat (asli: "4.6 Hak kompensasi pajak dan ekualisasi: Finance Lead mengelola hak kompensasi pajak (Tax Asset) dan memastikan ekualisasi antara Laporan Keuangan Komersial dan SPT (USULAN: Finance Lead sebagai pelaku). Bagian 6 belum memuat langkah rinci untuk butir ini."); arti tetap: Finance Lead sebagai pelaku berstatus USULAN. Jumlah label tetap 31.

### W10 kalimat dihapus atau dipindah
- 4.2: "Batas waktu tiap tahap ada di bagian 8." ditulis ulang "Setiap tahap diselesaikan dalam batas waktu sesuai bagian 8." (rujukan batas waktu dipertahankan).
- 4.3: "Pembagian tanggung jawab lainnya ada di bagian 5." menjadi "... sesuai bagian 5." (rujukan dipertahankan).
- 4.4: "Lokasi, pemilik, dan retensi tiap record ada di tabel bagian 11." menjadi "... mengikuti tabel bagian 11." (rujukan dipertahankan).

### W10 selisih angka
nihil

### W10 catatan
- Sebutan pihak luar: "customer" (satu-satunya sebutan di dokumen ini, 5 kali).
- "Dikecualikan dari SOP ini" menjadi "Di luar scope SOP ini", sama dengan SNX-FAT-SOP-04; definisi (USULAN), Finance Lead, dan Finance Staff diselaraskan dengan SNX-FAT-SOP-01.
- Langkah 6.2 butir 2 "Input utang pajak" menjadi "Catat utang pajak" (kata kerja Indonesia, STYLE §1.3).

### W10 audit cakupan label
- .policy[5]: diperbaiki (label digeser kembali ke kalimat Finance Lead sebagai pelaku; kalimat keterangan bagian 6 tanpa label seperti bed1bb6)
