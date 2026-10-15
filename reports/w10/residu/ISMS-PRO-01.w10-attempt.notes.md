# Catatan penyusun ISMS-PRO-01: Information Classification & Handling Procedure

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-PRO-01.json. Mode sop, aksi T1, nomor SNX-ISMS-PRO-01 (nomor lama dipertahankan), department Operation (label ISMS di defaults; sumber menulis "Information Security"), classification RESTRICTED (Internal) mengikuti label sumber, audit_class B, wave W2. Catatan worklist: "sumber pendukung POL-OPS-001 dan PRO-OPS-001 (bahan saja)".

## Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx (158648 byte) | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io | 2026-10-13T06:09:00Z (get_file_metadata, dicek ulang saat menyusun) | read_file_content (teks); download_file_content (docx didekode di /tmp/pen-ISMS-PRO-01/src/, python3 -I). Diagram rId23.png dibuka dan sama dengan diagram mermaid di context/audit. comments.xml dan footnotes.xml kosong |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan saja | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z | read_file_content dan download_file_content (untuk memeriksa kutipan) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan saja | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z | read_file_content dan download_file_content (untuk memeriksa kutipan) |
| Kriteria penerimaan | config/checklist.json baris 79 | checklist modifiedTime 2026-10-14T17:47:13.611Z | Description hanya nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001:2015 "7.5.3" dan ISO/IEC 27001:2022 "5.12, 5.13, 5.14, 5.33, 7.10, 8.10" |
| Pendukung (DATA, bukan dari Drive): REG-01, SOA-01, ML-00, FRM-02 di context/audit; specs/HR-ORG-01.json | lihat context/audit | salinan audit 13 sampai 14 Okt | Dipakai untuk judul dokumen terkait, pemilik dan retensi record, dan nama peran |

Tidak ada kalimat perintah yang ditujukan ke penyusun atau AI di ketiga sumber (dipindai: abaikan, ignore, assistant, agent). Kalimat imperatif di POL-OPS-001 dan PRO-OPS-001 adalah isi prosedur Ops, bukan instruksi untuk dokumen ini.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Informasi pelanggan minimal RESTRICTED (butir 4.3) | "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan lebih tinggi." | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| 2 | SECRET hanya di password manager (vault) atau sistem khusus ter-encrypt (butir 4.8) | "Hanya password manager internal (vault) atau sistem khusus ter-encrypt; dilarang di dokumen, spreadsheet, chat, tiket, atau email" | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| 3 | Syarat sah pengecualian (bagian 9) | "Pengecualian hanya sah bila tertulis, berbatas waktu, disetujui pemilik informasi dan ISMS Coordinator." | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |

## Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 4 | Tujuan | "Prosedur ini menetapkan tingkat klasifikasi informasi SINUX, cara memberi label, dan aturan penanganan per tingkat (penyimpanan, pengiriman, berbagi, pencetakan, retensi, dan pemusnahan), sehingga informasi dilindungi sesuai nilai dan risikonya." | Bagian 1 (kalimat tim utuh) |
| 5 | Scope | "Berlaku untuk semua informasi yang dibuat, diterima, disimpan, atau diproses oleh personel Divisi Operation dan pihak ketiga yang bekerja atas nama SINUX" | Bagian 2 |
| 6 | Pemilik informasi menetapkan klasifikasi | "Pemilik informasi (pemilik aset pada SNX-ISMS-REG-01) menetapkan klasifikasi saat informasi dibuat atau diterima." | Butir 4.1, 6.1 |
| 7 | Ragu berarti naik; penurunan oleh pemilik dan dicatat | "Bila ragu, gunakan tingkat yang lebih tinggi. Menurunkan klasifikasi hanya boleh oleh pemilik informasi dan dicatat." | Butir 4.1, 4.2, 6.1 |
| 8 | Agregasi | "Kumpulan informasi dapat naik tingkat (agregasi): daftar lengkap IP address server pelanggan beserta versi software minimal RESTRICTED." | Butir 4.4 |
| 9 | Label default | "Informasi PUBLIC dan INTERNAL boleh tanpa label; tanpa label dianggap INTERNAL." | Butir 4.5 |
| 10 | Label email | "Subjek diawali tingkat bila RESTRICTED atau SECRET" | 6.2 langkah 3 |
| 11 | Removable media RESTRICTED | "Hanya ter-encrypt dan dengan persetujuan Lead" | Butir 4.14, 6.3 |
| 12 | Retensi | "Sesuai master list dan kontrak" (RESTRICTED); "Sesingkat mungkin; rotasi berkala" (SECRET) | Butir 4.15 |
| 13 | Pemusnahan SECRET | "Hapus aman dan rotasi; media dihancurkan atau di-wipe sesuai SNX-ISMS-SOP-04" | Butir 4.16 |
| 14 | Kredensial yang ditemukan | "Kredensial yang ditemukan di tempat tersebut segera dihapus, dirotasi, dan dilaporkan sebagai event keamanan sesuai SNX-ISMS-SOP-01." | Butir 4.17, 6.4, SLA |
| 15 | Kredensial pelanggan | "Kredensial pelanggan diterima melalui direct message atau password manager, dipakai seperlunya, dan pelanggan diminta mengganti setelah dipakai." | Butir 4.18, 6.4 |
| 16 | Peran ISMS Coordinator | "Pemilik prosedur; sosialisasi dan pemantauan kepatuhan" | Bagian 5, 6.6 |
| 17 | Peran Head of Operation | "Menegakkan prosedur di Divisi Operation; meninjau pengecualian" | Bagian 5, 6.6, bagian 9 |
| 18 | Pelanggaran | "Pelanggaran penanganan informasi RESTRICTED atau SECRET dilaporkan sebagai event keamanan sesuai SNX-ISMS-SOP-01 dan ditindak sesuai kebijakan disipliner perusahaan." | Bagian 9 |
| 19 | Pemilik dokumen | "Pemilik dokumen | ISMS Coordinator" | meta.process_owner (tanpa nama) |
| 20 | Istilah Lead sub divisi | "Lead sub divisi | Konfirmasi di tiket" (POL-OPS-001 bagian 7, baris change Standar) | Definisi Lead sub divisi |
| 21 | Singkatan NOC dan SOC | "Prosedur NOC (Network Operations Center)" dan "Prosedur SOC (Security Operations Center)" (PRO-OPS-001) | Definisi Lead sub divisi |
| 22 | Contoh label knowledge base | "RESTRICTED (internal, restricted:ops)" (POL-OPS-001 bagian 1) | 6.2 langkah 8 (contoh restricted:ops) |
| 23 | Tiket | Owner 14 Okt (config/defaults.json): "sistem tiket zammad untuk ops, glpi untuk generalist" | Definisi Zammad dan Service Hub; butir 4.8; 6.2 langkah 6 |
| 24 | Status vault | POL-OPS-001 bagian 13: "Password manager: migrasikan kredensial dari dua sumber (Google Sheets dan Excel password-protected) ke vault internal sebelum vault dinyatakan live." | Definisi Password manager (vault): "menunggu konfirmasi Ops" |
| 25 | Dasar frekuensi (USULAN) pemantauan | POL-OPS-001 bagian 12: "Kepatuhan diaudit sampling per triwulan oleh Head of Operation: tiket, change request, dan Shift Log. (USULAN)" | SLA, baris Pemantauan kepatuhan |

## Pemetaan klausul ISO (kriteria)

Nama kontrol Annex A dan judul klausul 7.5.3 berasal dari standar ISO, bukan dari sumber tim; label (Annex A ...) di bagian 4 memetakan tiap butir ke kontrol.

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 7.5.3 Control of documented information | Ya | Butir 4.5 dan 6.2 (label pada dokumen, spreadsheet, tiket, knowledge base), butir 4.15 (retensi) | 6.2, 6.5 |
| 5.12 Classification of information | Ya | Butir 4.1 sampai 4.4 | 6.1 |
| 5.13 Labelling of information | Ya | Butir 4.5, 4.6 | 6.2 |
| 5.14 Information transfer | Ya | Butir 4.9, 4.10, 4.11 | 6.3, 6.4 |
| 5.33 Protection of records | Ya | Butir 4.15 | 6.5 |
| 7.10 Storage media | Ya | Butir 4.8, 4.12, 4.13, 4.14 | 6.3 |
| 8.10 Information deletion | Ya | Butir 4.16 | 6.5 |
| 8.12 (hanya di Bagian 3 sumber) | Tidak dimasukkan | Tidak | Lihat open item 11 |

## Keputusan data

- Approval: prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo, persis dari config/defaults.json (kunci ISMS). Sumber menulis "Disusun oleh | ISMS Coordinator", "Diperiksa oleh | ISO/ISMS Coordinator", "Disetujui oleh | COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber. Badan dokumen tidak menyebut COO maupun Direktur Utama, jadi aturan "Direktur (COO)" tidak terpakai.
- Process owner "ISMS Coordinator" mengikuti "Pemilik dokumen" di sumber (jabatan, tanpa nama).
- Review period YEARLY dari defaults. Header sumber "Masa simpan record | Berlaku sampai digantikan" tidak punya field di template; hanya tabel rekaman bagian 11 yang berlaku.
- Tanggal draft sumber (13 Oktober 2026) dan "Tanggal efektif | Ditetapkan saat pengesahan" tidak dibawa. Effective Date kosong, tanda tangan kosong. Dua baris riwayat revisi sumber menjadi satu baris template.
- Tiket: Zammad untuk Ops, Service Hub (GLPI) untuk generalist, sesuai owner. Sumber hanya menyebut Service Hub, jadi Zammad ditambahkan pada butir 4.8 (INTERNAL) dan 6.2 langkah 6. Batas "generalist" belum dirinci owner, dan dokumen ini tidak memerlukan batas itu.
- Vault: ditulis "Password manager (vault)" dengan "Status operasional: menunggu konfirmasi Ops", kalimat yang sama dengan SNX-ISMS-SOP-02. Tidak ada klaim aktif atau belum live.
- Ejaan: "komersil" di sumber menjadi "komersial" (butir 4.19). Tingkat ditulis RESTRICTED di badan dokumen; definisi memakai RESTRICTED (Internal) sesuai defaults dan menyatakan singkatannya.
- Definisi RESTRICTED: sumber "peran atau tim yang membutuhkan" ditulis "peran atau divisi yang membutuhkan" agar tidak ada "tim" tanpa keterangan. Penyusun menafsirkan "tim" sebagai divisi karena RESTRICTED dipecah per domain (ops, commercial, legal, hr, finance).
- Kolom Definisi, Contoh, dan Dampak bila bocor dari tabel Tingkat klasifikasi sumber dipindah ke bagian 3 (arti istilah); aturannya di bagian 4. Tabel pelabelan menjadi 6.2; matriks aktivitas x tingkat menjadi butir 4.7 sampai 4.16 (dipecah per aktivitas karena template bagian 4 hanya berisi paragraf).
- Nama peran (padanan di specs/HR-ORG-01.json):

| Peran di dokumen | Padanan HR-ORG-01 | Catatan |
|---|---|---|
| ISMS Coordinator | Matriks Peran: "Belum ditetapkan (K-13)" | Dipakai apa adanya; peran ada, pemegang belum |
| Head of Operation | Matriks Peran: "(USULAN), belum ada pemegang (K-10, K-11)" | Dipakai apa adanya |
| Lead sub divisi | Lead NOC, Lead SOC, Service Delivery Manager (baris "Peran lain di NOC, SOC, serta SD dan PM") | Sumber menulis "Lead" saja. Dipetakan ke istilah "Lead sub divisi" dari POL-OPS-001 bagian 7. Service Delivery Manager untuk SD dan PM adalah (USULAN) |
| Pemilik informasi | Tidak ada; peran fungsi, bukan jabatan | Kolom Pemilik SNX-ISMS-REG-01 memuat peran berbeda per aset (Head of Operation, Lead NOC, COO), jadi tidak bisa dipetakan ke satu jabatan |
| Seluruh personel | Tidak ada; semua pemegang jabatan ditambah pihak ketiga | Definisi diambil dari kalimat scope sumber |

## Penanganan cacat context/audit (bagian 5, fileId 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Scope hanya "personel Divisi Operation dan pihak ketiga", padahal judul dan Bagian 1 berbicara tentang informasi SINUX | Tidak diperluas diam-diam. Scope sumber dipertahankan, ditambah pengecualian eksplisit untuk divisi lain dan satu kalimat (USULAN) untuk perluasan ke seluruh SINUX. Open item 3 |
| 2 | Header memuat 5.12, 5.13, 5.14, 5.33, 7.10, 8.10; Bagian 3 menambah 8.12 (SoA: "Data leakage prevention", usulan "Perlu keputusan"); 5.33 tanpa bagian isi eksplisit | 8.12 tidak dimasukkan karena kriteria baris dan master list hanya enam kontrol dan SoA belum memetakannya (open item 11). 5.33 diperbaiki: butir 4.15 memakai tag 5.33, prosedur 6.5 dibuat, dan SoA menunjuk dokumen ini |
| 3 | Label knowledge base hanya tiga nilai, tanpa SECRET | Dipertahankan di 6.2 langkah 8. Larangan SECRET masuk paket knowledge base ada di butir 4.17. Bahwa larangan itu alasan tidak adanya label SECRET tidak dinyatakan sumber, jadi tidak ditulis (open item 12) |
| 4 | Rujukan keluar (REG-01, FRM-02, SOP-01, SOP-04) konsisten | Semua dicantumkan di bagian 11 dengan judul dari korpus |
| 5 | "master list" di baris Retensi tanpa nomor | "Master list" didefinisikan sebagai SNX-OPS-ML-00 (kolom Masa simpan record) dan dicantumkan di bagian 11. Dasarnya SoA: "SNX-ISMS-PRO-01, master list SNX-OPS-ML-00 (masa simpan)". Ini tafsir; open item 6 |
| 6 | Label SECRET di subjek email bertentangan dengan larangan SECRET di email | Kalimat sumber dipertahankan di 6.2 langkah 3. Butir 4.6 (USULAN): label SECRET menandai email yang terlanjur memuat SECRET dan dilaporkan sebagai pelanggaran. Keputusan di Fani (open item 4) |
| 7 | Pengesahan kosong, dua baris riwayat revisi bertanggal sama, "ISMS Coordinator" lawan "ISO/ISMS Coordinator" | Template: satu baris Revision 00, Effective Date dan Signature kosong. Penyusun dan pemeriksa dari defaults. Di badan hanya "ISMS Coordinator" |
| 8 | Tidak ada KPI, bagian definisi, atau RACI | Bagian 3 (definisi) ditambahkan. KPI dan RACI tidak ditambahkan: kriteria baris tidak menuntutnya dan angkanya tidak punya sumber. SLA memuat batas waktu dari sumber ("segera", "saat informasi dibuat atau diterima", "setelah pakai") dan satu (USULAN) |

Catatan cacat sumber pendukung yang tidak disalin: POL-OPS-001 dan PRO-OPS-001 memuat rujukan internal AI (DOCTRINE, DEC-, HANDOVER, SKILL_, SINUX_SERVICE_HUB, CORE, "packet setor", "jalur staging"); tidak ada yang masuk ke dokumen ini. POL-OPS-001 P-08 menulis semua tiket di GLPI; diganti keputusan owner (Zammad untuk Ops). POL-OPS-001 bagian 3 menulis Fani Fatullah sebagai komisaris dan advisor; dokumen ini tidak menyebut jabatan itu (reviewer di blok Reviewed By = VP Tech Operation and Services dari defaults). POL-OPS-001 menyebut POLRI untuk dokumen tanpa harga dan roadmap; butir 4.19 tetap memakai "pelanggan pemerintah" seperti sumber PRO-01. Istilah "data-safe" di PRO-OPS-001 bagian 5 tidak jelas artinya dan tidak dipakai.

## Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Pencatatan klasifikasi di kolom Klasifikasi SNX-ISMS-REG-01 oleh Pemilik informasi (6.1). Sumber hanya menulis pemilik aset menetapkan, "dicatat" tanpa pelaku, dan REG-01 punya kolom Klasifikasi.
2. Lokasi catatan penurunan klasifikasi = SNX-ISMS-REG-01. Sumber tidak menyebut lokasinya.
3. Rotasi kredensial yang ditemukan di tempat terlarang dilakukan Pemilik informasi (pemilik aset kredensial). Sumber pasif ("dirotasi"). SNX-ISMS-SOP-02 memakai Administrator sistem untuk rotasi kredensial terpapar; peran itu tidak dipakai di sini karena bukan peran sumber PRO-01 dan tidak ada di HR-ORG-01.
4. Penghapusan temuan kredensial dan pelaporannya oleh Seluruh personel (penemu). Sumber pasif.
5. "penerima rotate setelah pakai" ditulis sebagai kewajiban penerima, dengan PIC Seluruh personel.
6. Permintaan penggantian kredensial ke pelanggan oleh Seluruh personel yang memakai kredensial itu. Sumber: "pelanggan diminta mengganti".
7. Head of Operation menindak pelanggaran "sesuai kebijakan disipliner perusahaan". Sumber pasif; peran Head of Operation "Menegakkan prosedur di Divisi Operation".
8. Pemusnahan dan penyimpanan sampai masa simpan berakhir oleh Pemilik informasi. Sumber tidak menyebut pelaku.
9. Persetujuan izin akses folder Drive oleh Pemilik informasi, dari peran sumber "menyetujui akses dan berbagi".
10. Kolom Authority tabel peran tidak ada di sumber; diturunkan dari kalimat peran dan aturan sumber.
11. Definisi Agregasi, Event keamanan, Hapus aman, dan NDA adalah penjelasan penyusun, bukan kalimat tim. Definisi Removable media dari tanda kurung di sumber.
12. Lokasi "Google Drive" untuk SNX-ISMS-REG-01 dan SNX-ISMS-FRM-02: keduanya berkas Drive menurut config/checklist.json. Retensi "Berlaku sampai digantikan" (REG-01) dan "5 tahun" (FRM-02) diambil dari tabel kontrol dokumen masing-masing di salinan audit, bukan dari tiga sumber baris ini.
13. Nama kontrol Annex A dan judul klausul 7.5.3 dari standar ISO.
14. Butir 4.1 sampai 4.21 adalah penomoran penyusun untuk rujukan silang; sumber tidak bernomor.

## USULAN

Lint menghitung 13 label (USULAN) di dokumen; satu di antaranya baris definisi label itu sendiri. Sisanya 6 keputusan.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Perluasan cakupan prosedur ke seluruh SINUX | Bagian 2 | Judul dan tujuan sumber berbicara tentang informasi SINUX, scope hanya Divisi Operation | Owner |
| U2 | Service Delivery Manager sebagai "Lead" bagi sub divisi Service Delivery dan PM | Definisi Lead sub divisi | Sumber menulis "Lead" tanpa nama jabatan; POL-OPS-001 hanya menyebut Lead NOC dan Lead SOC | Fani |
| U3 | Label SECRET pada subjek email menandai email yang terlanjur memuat SECRET | Butir 4.6 | Menutup pertentangan label email (RESTRICTED atau SECRET) dengan larangan SECRET di email | Fani |
| U4 | Catatan sosialisasi dan catatan pemantauan kepatuhan: lokasi Google Drive, pemilik ISMS Coordinator, retensi 3 tahun | 6.6 langkah 1 dan 2; bagian 11 | Sumber memberi peran sosialisasi dan pemantauan tanpa rekaman. 3 tahun disamakan dengan retensi SNX-ISMS-REG-04 di SNX-ISMS-SOP-02 | Fani |
| U5 | Pemantauan kepatuhan setiap triwulan | Bagian 8 | Sumber tanpa frekuensi; angka mengikuti audit sampling triwulanan di POL-OPS-001 bagian 12 (itu pun USULAN) | Fani |
| U6 | Rekaman persetujuan tertulis (berbagi RESTRICTED ke pihak luar, removable media, pengecualian): lokasi Zammad atau Service Hub, pemilik ISMS Coordinator, retensi 3 tahun | Bagian 11 | Sumber mensyaratkan persetujuan dan pengecualian tertulis tanpa menyebut tempat dan masa simpannya | Fani |

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju: sumber menulis COO (Amirull Yusuf Zulkarnain), template dan defaults Samuel Kristanto Utomo / President Director. Defaults dipakai. Penyusun dan pemeriksa juga diganti dari "ISMS Coordinator" dan "ISO/ISMS Coordinator" ke defaults | Owner atau Samuel |
| 2 | ISMS Coordinator (pemilik prosedur) belum punya pemegang jabatan (HR-ORG-01 K-13). Head of Operation berstatus usulan tanpa pemegang (K-10, K-11) | Owner, Fani |
| 3 | Scope hanya Divisi Operation; keputusan memperluas ke seluruh SINUX (U1). Label klasifikasi dokumen departemen lain sudah memakai skema empat tingkat dokumen ini (config/defaults.json, blok classification) | Owner |
| 4 | Label SECRET pada email (U3), dan peran yang menangani email SECRET | Fani |
| 5 | Password manager (vault): status "menunggu konfirmasi Ops". Aturan SECRET hanya di vault belum bisa dipenuhi penuh selama kredensial masih di Google Sheets dan Excel password-protected (SNX-ISMS-REG-02 ISR-001: "Kredensial masih tersimpan di Google Sheets dan Excel password-protected sebelum migrasi ke vault"; POL-OPS-001 bagian 13 menunggu keputusan migrasi). Tidak ada kontrol pengganti di sumber, jadi tidak ditulis | Ops, Fani |
| 6 | "Master list" dibaca sebagai SNX-OPS-ML-00. Itu tafsir (didukung SoA), dan ML-00 hanya mencakup dokumen Divisi Operation; master list lintas divisi belum ada | Fani |
| 7 | Batas Zammad (Ops) lawan Service Hub GLPI (generalist) belum dirinci owner. Sumber PRO-01 hanya menyebut Service Hub; POL-OPS-001 P-08 masih menulis "Semua permintaan dan insiden tercatat sebagai tiket di SINUX Service Hub" | Owner |
| 8 | "Lead" di sumber dipetakan ke Lead sub divisi (Lead NOC atau Lead SOC); pemetaan untuk SD dan PM (U2) | Fani |
| 9 | Pelaku tidak disebut sumber, ditulis tafsir: rotasi kredensial temuan (Pemilik informasi), penghapusan temuan (Seluruh personel), pemusnahan (Pemilik informasi), penindakan pelanggaran (Head of Operation), pencatatan klasifikasi (Pemilik informasi). SNX-ISMS-SOP-02 memakai Administrator sistem untuk rotasi; selaraskan | Fani |
| 10 | "Kebijakan disipliner perusahaan" tidak punya kode dokumen, jadi tidak ada di tabel Dokumen terkait | Aziz |
| 11 | Annex A 8.12 (Data leakage prevention) hanya ada di Bagian 3 sumber, tidak di header, checklist, dan master list; SoA menandainya "Perlu keputusan" dan belum memetakannya ke PRO-01. Tidak dimasukkan | Konsultan SoA, Fani |
| 12 | Label sensitivity knowledge base tanpa SECRET: sumber tidak menyatakan alasannya | Fani |
| 13 | Layanan AI atau pihak ketiga yang "disetujui SINUX" (butir 4.21): daftar dan penyetujunya tidak ada di sumber | Fani |
| 14 | "Rotasi berkala" dan retensi "sesingkat mungkin" untuk SECRET tanpa angka; "Seperlunya" untuk cetak tanpa ukuran. Dipertahankan sebagai kalimat tim | Fani |
| 15 | Lokasi catatan penurunan klasifikasi: SNX-ISMS-REG-01 punya kolom Klasifikasi dan kolom Catatan bebas, tetapi belum ada kolom atau sheet khusus untuk mencatat penurunan | Pemilik REG-01 |
| 16 | "Pelanggan pemerintah" (PRO-01 bagian 7) lawan POLRI (POL-OPS-001): cakupan istilah belum dirinci | Fani |
| 17 | Header sumber "Masa simpan record | Berlaku sampai digantikan" untuk dokumen ini; template tidak punya field itu, jadi tidak tampil | Aziz |

## Uji

- python3 -m json.tool specs/ISMS-PRO-01.json: valid.
- python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-PRO-01.json /tmp/pen-ISMS-PRO-01/ISMS-PRO-01.docx: berhasil.
- python3 -I tools/lint_doc.py /tmp/pen-ISMS-PRO-01/ISMS-PRO-01.docx sop: "pass": true, fails kosong, warns hanya "13 butir (USULAN) menunggu ACC" (PIC SLA: nol warn).
- Validator OOXML (/mnt/skills/public/docx/scripts/office/validate.py): PASSED.
- Pratinjau PDF (soffice): 17 halaman, tabel dan diagram TB terbaca; hasil dilihat sebagai montase.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI, dan perbaikannya:

1. Matriks sumber menjadi sembilan paragraf berpola sama (INTERNAL ..., RESTRICTED ..., SECRET ...). Pola itu isi matriks tim, jadi dipertahankan; kata kerja dibuat sesuai aktivitas (disimpan, dikirim, dibagikan, dicetak, ditangani, dimusnahkan) dan PUBLIC dipadatkan jadi satu butir 4.7 supaya kata "bebas" tidak diulang sembilan kali.
2. Tag "(Annex A ...)" di judul butir terdengar mekanis. Dipertahankan karena melayani pemetaan kriteria ke kontrol; tag tidak masuk ke kalimat isi.
3. "Seluruh personel" berulang sebagai PIC. Itu peran sumber; mengganti dengan peran yang tidak ada di sumber akan menambah fakta. Dibiarkan.
4. Dua baris yang saya hapus karena mengulang butir lain atau memuat nama rekaman karangan: baris pengecualian "Kredensial ... ditemukan" (sudah di butir 4.17 dan 6.4, kini dirujuk dari baris pelanggaran) dan langkah "Tinjau pengecualian" dengan output "Hasil tinjauan pengecualian".
5. Output "Cetakan sesuai butir 4.12" diganti "Cetakan hanya untuk tingkat yang mengizinkan". Tidak ada pembuka generik, penutup positif, em-dash, atau tebal untuk penekanan di badan dokumen.

Adakah fakta, angka, nama, atau tanggal tanpa sumber, dan perbaikannya:

1. Angka "3 tahun" dan "setiap triwulan" tidak punya sumber tim; keduanya berlabel (USULAN) dengan dasar tertulis di bagian USULAN. Angka "5 tahun" (FRM-02) berasal dari tabel kontrol FRM-02 di salinan audit.
2. Nama kontrol Annex A dan judul 7.5.3 berasal dari standar ISO; dicatat di bagian Pemetaan klausul ISO.
3. Singkatan NOC dan SOC dari judul bagian PRO-OPS-001; "restricted:ops" dari POL-OPS-001; NDA dan "Hapus aman" adalah penjelasan umum penyusun (asumsi 11).
4. Nama orang dan jabatan hanya di blok Prepared, Reviewed, Approved, persis dari config/defaults.json. Tidak ada tanggal di dokumen.
5. Pelaku yang sumbernya pasif (rotasi, hapus, pemusnahan, penindakan, pencatatan) tercatat sebagai tafsir di Asumsi dan open item 9, tidak disajikan sebagai kalimat tim.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Butir 4.6: label dipindah dari awal ke akhir butir (asli: "4.6 (USULAN) Label SECRET pada subjek email menandai email yang terlanjur memuat informasi SECRET."); cakupan label tetap seluruh butir 4.6. Jumlah label tetap 13.

### W10 kalimat dihapus atau dipindah
- 4.5: "Cara memberi label pada tiap media ada di butir 6.2." (penunjuk; langkahnya ada di butir 6.2 Pelabelan).
- 6.1 langkah 1: "menurut definisi di bagian 3 dan butir 4.1 sampai 4.4" menjadi "sesuai butir 4.1 sampai 4.4" (satu rujukan per sel).
- SLA pengecualian: "(bagian 9)" dihapus; faktanya (batas tertulis pada persetujuan) tetap.
- Bagian 9 pelanggaran: "Seluruh personel dan Pemilik informasi menangani temuan kredensial menurut butir 6.4." diringkas; "Head of Operation menindak pelanggaran menurut butir 6.6." diganti fakta butir 6.6 ("sesuai kebijakan disipliner perusahaan").

### W10 selisih angka
- 6.2: hilang karena penunjuk di butir 4.5 dihapus; butir 6.2 (Pelabelan) tetap ada.
- 6.6: hilang karena rujukan "menurut butir 6.6" di bagian 9 diganti faktanya; butir 6.6 tetap ada.

### W10 catatan
- Sebutan pihak luar: "pelanggan" (keputusan lintas dokumen ISMS).
- Tingkat PUBLIC, INTERNAL, RESTRICTED (Internal), SECRET dipertahankan sebagai istilah resmi.
- Policy 4.17, 4.18, 4.20, 4.21 ditulis pasif atau dengan "personel" (STYLE §2.1); peran Seluruh personel di Roles dan PIC tidak berubah.
- Calque "yang SINUX kelola" diganti "yang dikelola SINUX".

### W10 putaran perbaikan 1 (qa/ISMS-PRO-01.w10.r1.json)
- Bagian 9 pelanggaran: pelaku dikembalikan (Seluruh personel menghapus dan melaporkan temuan kredensial sesuai butir 6.4; Pemilik informasi merotasinya).
- 4.21: arti asli dikembalikan; yang dibatasi adalah layanan AI atau pihak ketiga yang boleh dipakai untuk RESTRICTED.
- 4.14: "Pemakaian removable media untuk INTERNAL dihindari" (cakupan semua pemakaian, sama dengan "INTERNAL dihindari").
- Rujukan dikembalikan: 4.5 "sesuai butir 6.2", 6.1 langkah 1 "definisi tingkat di bagian 3", SLA pengecualian "(bagian 9)". Akibatnya "6.2" tidak lagi hilang; catatan selisih angka "6.2" di atas tidak berlaku lagi.
- Bagian 9 pengecualian dipecah lagi menjadi kalimat dengan satu pelaku; Scope: label tidak lagi menjadi predikat.

### W10 audit pointer
- .exceptions[0][1]: lengkap (butir 6.6 langkah 3: Head of Operation menindak pelanggaran sesuai kebijakan disipliner perusahaan; tanpa label; langkah 1 dan 2 butir 6.6 milik ISMS Coordinator bukan bagian penanganan pelanggaran).
