# Catatan penyusun LEG-SOP-02: Contract Review & Legal Approval

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-SOP-02.json. Mode sop, aksi T1, wave W3, nomor SNX-LEG-SOP-02 (nomor lama dipertahankan), department Legal, classification INTERNAL (worklist), audit_class null. Process owner "Line Manager Legal" (jabatan tanpa nama; lihat USULAN 7). Approval persis dari config/defaults.json: prepared Staff Legal, reviewed Line Manager Legal, approved Samuel Kristanto Utomo / President Director. Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Hasil uji terakhir (bukti mentah: /tmp/pen-LEG-SOP-02/render.out.txt, /tmp/pen-LEG-SOP-02/lint.out.txt, /tmp/pen-LEG-SOP-02/validate.out.txt, /tmp/pen-LEG-SOP-02/blankscan.out.txt; diulang sesudah sweep 15 Okt, hasil sama):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-SOP-02.json /tmp/pen-LEG-SOP-02/LEG-SOP-02.docx` selesai tanpa galat (exit 0).
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-SOP-02/LEG-SOP-02.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "16 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`, tanpa -I karena skrip itu mengimpor modul sebelahnya): "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-SOP-02/LEG-SOP-02.docx`: `ok 24 LEG-SOP-02.docx []` (nol halaman kosong).
- soffice ke PDF: 24 halaman. Diagram (/tmp/pen-LEG-SOP-02/LEG-SOP-02_flow.png) dilihat: 18 simpul, rankdir TB, teks terbaca, tiga loop (permintaan tidak lengkap, revisi, perubahan material) tergambar.
- Pemeriksaan tambahan atas spec (skrip python3 -I): nol em-dash dan en-dash; tiap langkah paling banyak 25 kata; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode dokumen yang dirujuk di badan ada di tabel Dokumen terkait; nol kalimat identik di dua bagian; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, tanpa terkecuali, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, dari hulu ke hilir, sesegera mungkin) dan untuk "Lead", "tim" tanpa keterangan, Direksi, COO, TBD, [ISI, CONTOH.
- tools/selftest.sh tidak dijalankan. Berkas tools, template, config, control tidak diubah. Berkas yang ditulis hanya specs/LEG-SOP-02.json dan notes/LEG-SOP-02.md; hasil render hanya di /tmp/pen-LEG-SOP-02/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SOP Contract Review & Legal Approval (Google Doc, fileSize 13285), sumber utama, draf tim sedang ditulis | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE | 2026-10-14T09:08:19.129Z (get_file_metadata sesi ini, sama dengan prompt; diukur ulang di akhir penyusunan, hasil sama, bagian 6) | read_file_content dengan includeComments=true: teks penuh, tidak ada penanda komentar. Tidak ada catatan audit untuk berkas ini (grep context/audit nol hasil) |
| SOP Divisi Legal – SINUX.docx (fileSize 16407), bahan | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (get_file_metadata sesi ini, sama dengan prompt; fileSize sama dengan "bytes" di salinan audit) | read_file_content (teks penuh, cocok dengan salinan context/audit baris 1055 dan seterusnya). download_file_content tidak dipakai karena struktur docx sudah tercatat di audit (tanpa header, footer, gambar) |
| Kriteria penerimaan | config/checklist.json baris 37 | tidak berlaku | Description: "Prosedur standar untuk proses peninjauan, revisi, dan persetujuan kontrak oleh Divisi Legal sebelum penandatanganan." Klausul ISO: kosong di checklist |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md bagian "legal/LEG-SOP-Divisi-Legal.md" (dari baris 1055, bagian 5 "Catatan kualitas dan celah" sebelum "## 6. Kata kunci retrieval") | salinan audit 13 sampai 14 Okt | DATA. `grep -n 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE context/audit/*.md`: nol hasil. `grep -n 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb context/audit/*.md`: baris 1055 (legal) dan baris 88 (sintesis) |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Matriks peran: Line Manager Legal = Legal & Compliance (JA-08), Staff Legal = Legal & Compliance (JA-09), keduanya "(USULAN), menunggu konfirmasi (K-13)" |
| Nomor dokumen rujukan | config/worklist.json | repo kerja | SNX-LEG-SOP-01 (Legal Operational), SNX-LEG-SOP-03 (Legal Document Control & Retention), SNX-LEG-FRM-01 dan SNX-LEG-FRM-02 (checklist review kontrak pelanggan dan vendor/pemasok) |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat imperatif di kedua sumber adalah langkah prosedur dan diperlakukan sebagai isi.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Penandatanganan baru boleh sesudah semua persetujuan yang diwajibkan diperoleh (gerbang "sebelum penandatanganan" dari kriteria baris) | "Penandatanganan hanya dapat dilaksanakan setelah persetujuan yang diwajibkan telah diperoleh." (Prosedur Pelaksanaan, Pemeriksaan Akhir dan Penandatanganan, butir 6) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |
| 2 | Persetujuan Legal bukan pengganti persetujuan lain | "Persetujuan Legal tidak dengan sendirinya menggantikan persetujuan bisnis, keuangan, keamanan informasi, atau kewenangan penandatanganan yang dipersyaratkan." (Definisi, Persetujuan Legal) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |
| 3 | Target waktu berstatus usulan awal dan dihitung sejak informasi lengkap | "Target berikut merupakan usulan awal berdasarkan SOP Divisi Legal dan dihitung sejak informasi serta dokumen minimum telah diterima secara lengkap." (Prosedur Pelaksanaan, Prioritas dan Target Waktu) | 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di spec |
|---|---|---|---|
| 1 | Tujuan | "SOP ini bertujuan untuk menetapkan prosedur penelaahan, penyusunan, negosiasi, persetujuan, dan penandatanganan kontrak agar setiap kontrak yang melibatkan PT Strategi Integrasi Nusantara (“Perusahaan” atau “SINUX”) telah ditelaah secara memadai" (Tujuan butir 1) | purpose |
| 2 | Pemilik dokumen | "Pemilik Dokumen \| Departemen Legal" (Identitas Dokumen, 1E_8...); "Pemilik SOP: Line Manager Legal." (Kontrol Dokumen SOP, 19pe...); "Line Manager Legal bertanggung jawab memantau penerapan SOP ini." (Pemantauan dan Peninjauan SOP, 1E_8...) | meta.process_owner, conclusion |
| 3 | Scope: sembilan proses dan jenis kontrak | "Pemeriksaan akhir dan penandatanganan." dan "Pencatatan serta pengarsipan kontrak yang telah ditandatangani." (Ruang Lingkup butir 8 dan 9); "Jenis dokumen yang dapat ditangani meliputi NDA, IaaS Contract, Technology Services Contract, Hardware Sale and Purchase Agreement, PKS, Subcontract, addendum, dan dokumen kontraktual lainnya yang relevan." | scope |
| 4 | Kanal permintaan belum ada | "melalui kanal resmi Perusahaan, yaitu [TBD: email/formulir/sistem tiket]." (Pengajuan Permintaan butir 1) | scope butir 4, 6.1 langkah 1 |
| 5 | Data minimal permintaan | "nama dan identitas para pihak; jenis dan tujuan kontrak; ruang lingkup transaksi atau layanan; nilai dan mekanisme pembayaran; jangka waktu yang direncanakan; tenggat waktu yang diminta beserta alasannya; PIC Bisnis; dan draft, term sheet, proposal, atau dokumen pendukung lainnya yang tersedia." (Pengajuan Permintaan butir 2, daftar bernomor digabung) | 6.1 intro |
| 6 | Pencatatan, kelengkapan, penugasan | "Staff Legal mencatat permintaan dalam register permintaan Legal dan memberikan nomor referensi." dan "Setelah informasi memadai, Line Manager Legal menetapkan penugasan kepada Staff Legal dan mengonfirmasi prioritas serta target penyelesaian." | 6.1 langkah 2 sampai 6 |
| 7 | Target waktu per jenis | "NDA \| 1 hari \| 2 hari"; "Review Kontrak atau PKS \| 1 hari \| 3-5 hari"; "Penyusunan Kontrak Baru \| 1 hari \| 5 hari"; "Dokumen Korporasi/Perizinan \| 2 hari \| Sesuai kompleksitas dan proses pihak ketiga"; "Permintaan Mendesak \| Hari yang sama (jika memungkinkan) \| Berdasarkan konfirmasi prioritas dan kesepakatan tenggat". Satuan "hari kerja": "NDA standar \| 1 hari kerja \| 2 hari kerja" (19pe...) | bagian 8 |
| 8 | Target proses internal, bisa disesuaikan | "Target penyelesaian merupakan target proses internal, bukan jaminan bahwa negosiasi dengan pihak lawan atau penandatanganan akan selesai dalam jangka waktu tersebut." dan "Perubahan target harus dikomunikasikan kepada pemohon dengan alasan yang relevan." | 4.5, 4.6 |
| 9 | Pemeriksaan awal pihak lawan | "Apabila terdapat ketidaksesuaian identitas, kewenangan penandatangan, atau informasi material lainnya, Staff Legal meminta klarifikasi atau dokumen tambahan sebelum proses dilanjutkan." dan "Temuan yang berpotensi menimbulkan risiko material disampaikan kepada Line Manager Legal untuk ditentukan tindak lanjutnya." | 6.2 |
| 10 | Aspek review (16 baris) | Tabel "Aspek \| Hal yang Diperiksa", dari "Identitas dan kewenangan" sampai "Konsistensi dokumen". Tambahan dari 19pe...: "(termasuk apakah pembayaran bergantung pada pembayaran klien akhir)", "hak penangguhan pembayaran atau layanan", "potensi tumpang tindih wilayah/produk/pihak dengan kontrak lain" | 6.3 intro |
| 11 | Klasifikasi dan penanganan risiko | "Proses persetujuan ditahan pada isu terkait dan dieskalasi kepada Line Manager Legal serta manajemen/pejabat berwenang sesuai kebutuhan." (Tinggi); "Keputusan penerimaan risiko harus dibuat oleh pihak yang memiliki kewenangan dan didokumentasikan." | 4.8 sampai 4.12, 6.4 |
| 12 | Review dan Persetujuan Legal | "Line Manager Legal dapat: menyetujui hasil review untuk dilanjutkan; meminta revisi atau analisis tambahan; atau mengeskalasi isu kepada manajemen atau unit kerja terkait." (daftar bernomor digabung) dan "Persetujuan Legal harus dapat ditelusuri melalui catatan tertulis, komentar pada dokumen, email resmi, atau media persetujuan internal yang ditetapkan." | 6.5, 4.13 |
| 13 | Revisi dan perubahan material | "Apabila terdapat perubahan material setelah persetujuan Legal, dokumen harus ditelaah kembali sebelum dilanjutkan ke persetujuan final." dan "Apabila terdapat perubahan pada versi final setelah persetujuan, kontrak dikembalikan untuk ditelaah sesuai tingkat materialitas perubahannya." | 4.14, 6.6 langkah 5 |
| 14 | Persetujuan DoA belum bisa jalan | "Batas persetujuan berdasarkan jenis dan nilai transaksi mengacu pada matriks DoA Perusahaan, yaitu [TBD]." dan "Apabila DoA belum tersedia atau kewenangan tidak jelas, Staff Legal mengeskalasi kepada Line Manager Legal untuk memperoleh konfirmasi tertulis dari pihak berwenang sebelum kontrak ditandatangani." | 6.7 intro, langkah 4 sampai 7 |
| 15 | Kewajiban Pemohon (bahan, sumber lama) | "Melibatkan Legal sejak tahap negosiasi komersial, sebelum ada komitmen tertulis kepada pihak luar."; "Menjawab pertanyaan Legal dalam 2 hari kerja; tenggat Legal bergeser sebesar keterlambatan jawaban."; "Tidak mengubah isi dokumen yang sudah direview tanpa melalui Legal." (19pe..., Kewajiban Divisi Pemohon) | 4.3, 4.4, bagian 8 |
| 16 | Penamaan versi | "Dokumen diberi nama secara konsisten, misalnya: “JenisDokumen_NamaPihak_Versi_Tanggal”. Contoh: IaaSContract_Arkana_v02_20261014." | 4.15 (nama pihak di contoh diganti NamaPihak) |
| 17 | Arsip dan register | "Dalam waktu paling lambat 2 (dua) hari kerja setelah kontrak ditandatangani lengkap oleh para pihak, Staff Legal mengunggah salinan final ke repositori resmi Perusahaan, yaitu [TBD]." dan "Dokumen asli disimpan pada tempat yang aman dengan kontrol akses sesuai SOP Legal Document Control & Retention." Register 9 isian, dari "nomor dan jenis kontrak" sampai "lokasi penyimpanan dokumen" | 6.9 |
| 18 | Pemantauan kontrak berjalan | "Staff Legal meninjau register kontrak sekurang-kurangnya satu kali setiap bulan." dan "Kontrak yang akan berakhir atau memiliki batas pemberitahuan perpanjangan/terminasi dalam 90 (sembilan puluh), 60 (enam puluh), dan 30 (tiga puluh) hari ditandai untuk ditindaklanjuti." | 6.10, bagian 8 |
| 19 | Peninjauan SOP | "SOP ditinjau sekurang-kurangnya satu kali dalam setahun atau ketika terdapat perubahan regulasi, struktur organisasi, kewenangan persetujuan, proses bisnis, atau kebutuhan pengendalian internal." | conclusion |
| 20 | Referensi sumber | "SOP Legal Operational."; "Jobdesc Line Manager Legal."; "Jobdesc Legal Staff."; "Contract Review Checklist" (Referensi dan Dokumen Terkait) | related_documents |
| 21 | Tiket Zammad untuk Ops, GLPI untuk generalist | config/defaults.json ticketing: "sistem tiket zammad untuk ops, glpi untuk generalist". Sumber tidak menyebut sistem tiket selain placeholder di baris 4 | scope butir 4, 6.1, definisi GLPI |

## 3. Pemetaan klausul ISO (kriteria baris)

Checklist tidak memberi acuan klausul untuk baris ini. Semua klausul di bagian 11 spec berstatus "(USULAN, perlu konfirmasi konsultan)", satu label di key "Status daftar klausul".

| Klausul | Alasan | Di spec |
|---|---|---|
| ISO 9001:2015 8.2.3 (Peninjauan persyaratan produk dan jasa) | Review kontrak pelanggan sebelum komitmen penandatanganan | iso_refs, butir 6.3 sampai 6.5 |
| ISO 9001:2015 8.2.4 (Perubahan persyaratan produk dan jasa) | Addendum, perpanjangan, perubahan material | butir 6.6 dan 6.10 |
| ISO 9001:2015 8.4.3 (Informasi untuk penyedia eksternal) | Kontrak vendor, pemasok, subkontraktor | butir 6.3 |
| ISO 9001:2015 7.5.3 (Pengendalian informasi terdokumentasi) | Penamaan versi, pengarsipan, register kontrak | butir 6.6 dan 6.9 |
| ISO/IEC 27001:2022 Annex A 5.31 (Persyaratan legal, statutori, regulasi, dan kontraktual) | Review kesesuaian hukum kontrak; audit legal menyebut kaitan ke kontrol 5.31 sebagai inferensi | butir 6.3 dan 6.4 |
| ISO/IEC 27001:2022 Annex A 5.20 (Penanganan keamanan informasi dalam perjanjian pemasok) | Aspek "Keamanan informasi" pada kontrak vendor | butir 6.3 |
| ISO/IEC 27001:2022 Annex A 5.34 (Privasi dan pelindungan data pribadi) | Aspek "Pelindungan data pribadi" | butir 6.3 |
| ISO/IEC 27001:2022 Annex A 6.6 (Perjanjian kerahasiaan) | NDA dan aspek "Kerahasiaan" | butir 6.3 |

Nama klausul berasal dari standar, bukan dari dokumen tim. Pilihan klausul dan nama Indonesianya belum diperiksa konsultan.

## 4. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" untuk SOP Divisi Legal (19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb), dinilai terhadap dokumen ini. Sumber utama 1E_8... tidak punya catatan audit; cacat yang saya temukan sendiri ada di tabel kedua.

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status v0.1, tanpa nomor, tanggal hanya "Oktober 2026", penyetuju belum ditetapkan | Diperbaiki: nomor SNX-LEG-SOP-02, status Draft revision 00, tanggal efektif kosong, penyetuju Samuel Kristanto Utomo / President Director sesuai defaults |
| 2 | Delapan placeholder [ISI] | Dijawab sebagian. (1) atasan Line Manager Legal: tidak dipakai di dokumen ini, ada di SNX-HR-ORG-01 (K-03). (2) kanal permintaan: tiket GLPI (USULAN 1). (3) DoA: matriks belum ada, diatur langkah eskalasi sumber (6.7), open item 2. (4) kontrol akses dokumen asli: diarahkan ke SNX-LEG-SOP-03 sesuai sumber utama. (5) LKPM: di luar scope, tidak dibawa. (6) repositori: open item 3. (7) retensi: open item 3. (8) penyetuju SOP: blok Approved By template |
| 3 | Rujukan menggantung "alur 5.2 dan 5.3" (bagian 4.3 sumber lama) | Diperbaiki: sumber utama menulis "prosedur penelaahan dan persetujuan dalam SOP ini"; spec merujuk butir 6.1 sampai 6.9 (6.10 langkah 5) |
| 4 | Tiga sumber berbeda untuk atasan Line Manager Legal | Tidak dibawa ke dokumen ini. SNX-HR-ORG-01 sudah memutus penempatan sementara di bawah Direktur dengan konfirmasi K-03; dokumen ini tidak menyebut atasan dan tidak menyebut CEO atau COO |
| 5 | Target waktu berlabel usulan; KPI Jobdesk "90% tepat waktu" bergantung padanya | Dipertahankan sebagai (USULAN) di tiap baris bagian 8. KPI 90% tidak disalin ke dokumen ini karena bukan isi sumber utama; open item 11 |
| 6 | Lampiran belum disusun (template, playbook, redline, register, DoA) | Dicatat di Dokumen terkait sebagai "Belum bernomor": matriks DoA, template kontrak, format register. Playbook klausul tidak dirujuk karena sumber utama tidak menyebutnya |
| 7 | Tidak ada retensi, lokasi repositori; SLA korporasi dan urgent "Sesuai"/"Disepakati" | Retensi dan lokasi: "Belum ditetapkan" di tabel rekaman, open item 3. SLA korporasi dan urgent memakai rumusan sumber utama (kompleksitas dan proses pihak ketiga; konfirmasi prioritas dan kesepakatan tenggat) |
| 8 | "Legal memberi opini" bertentangan dengan "Hentikan proses" dan "menahan kontrak" | Diperbaiki mengikuti sumber utama: Line Manager Legal menahan Persetujuan Legal pada isu risiko Tinggi, Pejabat Berwenang memutuskan penerimaan risiko (4.8, 4.12), dan Persetujuan Legal tidak menggantikan persetujuan lain (4.2). Kalimat "opini" tidak dibawa |
| 9 | Tidak ada klausul ISO; tidak ada klasifikasi dokumen | Diperbaiki: iso_refs (USULAN, perlu konfirmasi konsultan); klasifikasi SOP INTERNAL dari worklist |
| 10 | Rujukan PP No. 5 Tahun 2021 dan UU No. 27 Tahun 2022 | Tidak dibawa: sumber utama tidak menyebut peraturan itu. PP 5/2021 ada di bagian 4.4 sumber lama (pengurusan NIB melalui OSS, di luar scope); UU 27/2022 ada di bagian 4.5 sumber lama (kepatuhan, bukan review kontrak). Aspek pelindungan data pribadi tetap ada di 6.3 tanpa kutipan peraturan |
| 11 | "Staff Legal (Senior/Junior)" dan sel batas wewenang advokat kosong di Jobdesk | Tidak dibawa: sumber utama hanya menyebut Staff Legal; penunjukan advokat di luar scope |
| 12 | Label klasifikasi Rahasia/Internal/Publik, SOP tidak merujuk SNX-ISMS-PRO-01 | Diperbaiki: butir 4.17 merujuk SNX-ISMS-PRO-01; label Indonesia tidak dipakai |

Cacat tambahan di sumber utama (tidak ada di audit):

| # | Cacat | Penanganan |
|---|---|---|
| a | Tiga placeholder [TBD]: kanal permintaan, matriks DoA, repositori | Lihat baris 2 tabel di atas; tidak ada [TBD] di dokumen (lint menembak) |
| b | Istilah berganti: "Legal Staff" dan "Staff Legal"; "Pemohon/Unit Bisnis" dan "pemohon"; "Pihak Berwenang", "Pejabat Berwenang", "pihak berwenang"; "PIC" dan "PIC Bisnis"; "penelaahan", "review", "Contract Review", "ditelaah" | Disatukan: Staff Legal, Pemohon, Pejabat Berwenang, PIC Bisnis (langkah 6.7.1 sumber menulis "PIC" saja), "review kontrak" |
| c | Baris tabel Tanggung Jawab mengulang judul ("Unit Kerja Terkait Memberikan masukan", "Pejabat Berwenang Memberikan persetujuan") | Dirapikan di tabel peran |
| d | Tabel "Catatan Pemeriksaan dan Persetujuan" di akhir sumber (Disusun, Diperiksa, Disetujui, semua kosong) | Tidak dibawa: digantikan blok Approval template; tanda tangan dan tanggal kosong |
| e | Baris "Dokumen Korporasi/Perizinan" di tabel target waktu berada di luar daftar jenis kontrak pada Ruang Lingkup sumber | Baris dipertahankan di bagian 8 dan dijelaskan di scope; open item 5 |
| f | Sumber utama menulis target "hari", sumber lama "hari kerja" | Dipakai "hari kerja" (asumsi 1) |
| g | Contoh nama berkas memuat nama pihak (Arkana) | Diganti NamaPihak di 4.15 (nama pihak luar tidak dibawa ke dokumen) |
| h | Daftar Ruang Lingkup tidak memuat pemantauan kontrak berjalan, padahal prosedur 5 butir 11 mengaturnya | Pemantauan kontrak berjalan ditambahkan ke daftar proses di scope |
| i | Klausul kritis sumber lama (pembayaran bergantung klien akhir, penangguhan, tumpang tindih kontrak) tidak ada di tabel aspek sumber utama | Digabung ke baris "Nilai dan pembayaran" dan "Konsistensi dokumen" (6.3 intro) agar substansi tim tidak hilang |

## 5. Asumsi

1. Satuan target waktu "hari kerja": sumber utama menulis "hari", sumber lama (yang menjadi dasar tabel menurut sumber utama) menulis "hari kerja".
2. Pemohon menjawab pertanyaan Legal dalam 2 hari kerja diambil dari sumber lama (19pe..., Kewajiban Divisi Pemohon). Pelakunya PIC Bisnis karena tabel Tanggung Jawab sumber utama: "mengoordinasikan jawaban atas pertanyaan Legal".
3. Dasar kewenangan "Pejabat Berwenang" tidak diberi nama jabatan. Jabatan terdekat di SNX-HR-ORG-01 adalah Direktur Utama (JA-01) dan Direktur (JA-02), tetapi SNX-HR-ORG-01 menyerahkan hak tanda tangan kontrak ke Authority Matrix yang belum bernomor. Dokumen tidak memetakan, sehingga aturan sebutan "Direktur (COO)" tidak terpicu (tidak ada sebutan COO atau Direktur Utama di badan).
4. Peran sumber di luar matriks peran SNX-HR-ORG-01: Pemohon (unit, bukan jabatan), PIC Bisnis (penunjukan oleh Pemohon), Unit Kerja Terkait (Finance, Accounting & Tax, IT, fungsi keamanan informasi; sumber menulis "Finance, Accounting, and Tax" dan "tim keamanan informasi"), Pejabat Berwenang (asumsi 3). Line Manager Legal dan Staff Legal memakai nama peran matriks SNX-HR-ORG-01.
5. Sumber menyatakan Line Manager Legal menyetujui Persetujuan Legal ("memberikan persetujuan internal Legal sesuai kewenangannya"), maka definisi Persetujuan Legal menyebut Line Manager Legal.
6. Pengecualian scope (sumber diam): keputusan bisnis dan sejenisnya diturunkan dari "Persetujuan Legal tidak dengan sendirinya menggantikan ..."; korporasi, perizinan, somasi, klaim, dan sengketa diturunkan dari kriteria baris (kontrak sebelum penandatanganan) dan dari pembagian SOP Divisi Legal (sumber SNX-LEG-SOP-01); retensi arsip diturunkan dari judul SNX-LEG-SOP-03. Isi SNX-LEG-SOP-01 dan -03 belum ada di specs/ saat disusun.
7. Definisi umum yang bukan dari sumber: NDA (Non-Disclosure Agreement, perjanjian kerahasiaan), PKS (Perjanjian Kerja Sama), Term sheet, Wanprestasi, Pihak lawan. Definisi DoA ("Delegasi wewenang") diambil dari sumber lama, lampiran "Matriks delegasi wewenang (DoA) penandatanganan kontrak".
8. Langkah 6.6.1: sumber menulis "Staff Legal berkoordinasi dengan PIC Bisnis untuk menyampaikan usulan perubahan kepada pihak lawan"; siapa yang menyampaikan tidak disebut, maka langkah dibatasi pada koordinasi oleh Staff Legal.
9. Butir 4.17: sumber menulis "klasifikasi kerahasiaan dokumen" tanpa skema; skema SNX-ISMS-PRO-01 dipakai sesuai perbaikan lintas dokumen RUNBOOK §6. Tingkat tiap jenis kontrak tidak ditetapkan (aturan defaults: dokumen hukum = RESTRICTED (Internal); itu keputusan Legal, bukan penyusun).
10. Tidak ada angka, tanggal, atau nama di spec selain yang tercatat di tabel kutipan dan di tabel USULAN. Tanggal "20261014" hanya bagian dari contoh nama berkas sumber.

## USULAN

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

## Open items

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Kanal resmi permintaan dan batas "generalist" GLPI belum diputus; sumber utama masih [TBD]. Apakah nomor referensi register permintaan Legal sama dengan nomor tiket GLPI belum jelas | owner |
| 2 | Matriks DoA belum disusun, jabatan Pejabat Berwenang belum ditetapkan, dan belum dipastikan apakah "matriks DoA" sama dengan Authority Matrix di SNX-HR-ORG-01. Sampai terbit, langkah 6.7.5 sampai 6.7.7 berlaku untuk semua kontrak | owner dan Samuel |
| 3 | Lokasi repositori resmi, lokasi register permintaan Legal, register kontrak, dan rekaman lain; retensi semua rekaman bagian 11 belum ditetapkan. SNX-LEG-SOP-03 belum ada saat disusun | Legal |
| 4 | Pelaku pemberian akses ke kontrak (butir 4.17, sumber pasif) dan tingkat klasifikasi tiap jenis kontrak menurut SNX-ISMS-PRO-01 | Legal |
| 5 | Baris "Dokumen Korporasi/Perizinan" ada di tabel target waktu sumber tetapi di luar daftar jenis kontrak pada scope sumber. Dipertahankan di bagian 8; Legal memutus apakah dipindah ke SNX-LEG-SOP-01 | Legal |
| 6 | "Media persetujuan internal yang ditetapkan" (butir 4.13) dan "metodologi risiko Perusahaan, apabila telah ditetapkan" (butir 4.11) belum ada | Legal |
| 7 | Atasan Line Manager Legal: sumber lama [ISI], Jobdesk "CEO", HR-JA-001 "Management / Direktur"; SNX-HR-ORG-01 K-03. Dokumen ini netral | owner |
| 8 | Pengecualian scope dan baris Dokumen terkait untuk SNX-LEG-SOP-01 dan -03 bergantung pada isi dokumen itu. Spec LEG-SOP-01 (draf paralel, dibaca saja di akhir) memuat korporasi, perizinan, sengketa, somasi, dan klaim di scope-nya, sesuai pengecualian di sini, dan memakai GLPI untuk permintaan; spec LEG-SOP-03 belum ada. Bila isinya berubah, perbarui scope butir 5 dan tabel Dokumen terkait | Legal (setelah spec LEG-SOP-03 ada) |
| 9 | Lampiran sumber lama yang belum disusun: template kontrak, playbook klausul, format redline dan ringkasan risiko, format register. Playbook dan format redline tidak dirujuk dokumen ini | Legal |
| 10 | Sumber utama adalah draf tim yang sedang ditulis. Bila modifiedTime berubah sesudah 2026-10-14T09:08:19.129Z, spec perlu dicocokkan ulang | LEAD ISO [ditutup W9] |
| 11 | KPI Jobdesk "Review kontrak sesuai SLA 90% tepat waktu" bergantung pada target usulan bagian 8; tidak disalin ke sini | Legal |
| 12 | Penamaan unit: dokumen ini memakai "Divisi Legal" (kata kriteria baris); sumber utama memakai "Departemen Legal" hanya di Pemilik Dokumen; spec LEG-SOP-01 memakai "Departemen Legal". Satu sebutan untuk seluruh dokumen Legal perlu diputus | LEAD ISO, lalu owner bila perlu [ditutup W9] |

## 6. Pengukuran ulang modifiedTime

Sumber utama adalah draf tim yang sedang ditulis (catatan worklist), maka modifiedTime diukur dua kali.

Pengukuran akhir (get_file_metadata, sesudah spec dan notes selesai): 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE modifiedTime 2026-10-14T09:08:19.129Z, fileSize 13285, tidak berubah sejak awal penyusunan. 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb tidak diukur ulang di akhir (terakhir 2026-10-13T10:54:39.480Z).

## 7. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI, dan apa yang saya perbaiki:
- Butir 4.19 pada draf pertama berbunyi seperti catatan proses ("dokumen sumber memakai kalimat pasif"). Sudah ditulis ulang dua kali; bentuk akhir (sesudah sweep) hanya menyebut pelaku dan labelnya, alasan ada di notes ini (USULAN 3). Tiga kalimat meta lain di scope dan Dokumen terkait dibersihkan di sweep.
- Pola "Hasil yang dijaga:" di Purpose dipakai dokumen saudara (FAT-SOP-01) dan RUNBOOK §6a.4; dipertahankan, tetapi kalimatnya saya pecah menjadi satu klausa utama dan satu klausa pendukung, tanpa tiga serangkai.
- Daftar bertitik koma di scope dan di intro 6.1, 6.2, 6.5, 6.9 mirip daftar mesin. Daftar itu menyalin urutan dan isi tabel atau butir sumber (kata tim dipertahankan, T1), jadi tidak diganti.
- Frasa lindung nilai "sesuai kebutuhan", "sesuai relevansi transaksi", "tanpa dasar yang memadai" muncul beberapa kali. Semuanya kata sumber utama; saya menghapus yang bukan kata sumber dan membiarkan yang bunyi aslinya demikian. Penajamannya butuh keputusan Legal (kapan eskalasi ke Pejabat Berwenang diperlukan), bukan penyusun.
- Kata kerja berulang "Periksa", "Pastikan", "Simpan" di 6.8 dan 6.9 sengaja dibiarkan: tiap langkah satu tindakan, dan kata kerjanya memang berbeda objeknya.
- Frasa AI yang dicek dan tidak ada: pembuka generik, penegasan kosong, atribusi kabur, kata kerja manusia untuk benda ("sistem memutuskan"), ekor penegas, rentang palsu, penutup positif. Tanda kutip, huruf kapital, dan tebal untuk penekanan tidak dipakai (tebal hanya subjudul template).

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: semua dari sumber (1, 2, 3 sampai 5, 5 hari kerja; 2 hari kerja; 90, 60, 30 hari; sebulan sekali; setahun sekali; 25 kata adalah batas RUNBOOK, bukan isi dokumen). Satuan "hari kerja" dari sumber lama (asumsi 1).
- Nama: nama orang hanya Samuel Kristanto Utomo di blok Approved By (defaults). Nama pihak luar (Arkana) dihapus dari contoh. Nama sistem: GLPI (defaults), Service Hub (defaults). Kode dokumen dari worklist dan HR-ORG-01.
- Tanggal: tidak ada selain "20261014" di contoh nama berkas (dari sumber).
- Tanpa sumber tetapi diberi label atau dicatat: kanal GLPI, pelaku langkah pasif, pemilik rekaman, pemetaan checklist, klausul ISO, process owner (USULAN 1 sampai 7). Definisi umum NDA, PKS, Term sheet, Wanprestasi, Pihak lawan tidak berlabel karena arti istilah baku; dicatat di asumsi 7.
- Nomor langkah yang dirujuk butir 4.19 dan butir lain (6.4 langkah 9; 6.7 langkah 3 dan 8; 6.10 langkah 3 dan 6; butir 4.6 sampai 4.17) dicek ulang terhadap spec final dan cocok.

## Sweep

Sweep 15 Okt dari orkestrator WORKER-ISO-01 (instruksi /tmp/claude-0/prompts/LEG-SOP-02.sweep.txt). Berkas yang ditulis: specs/LEG-SOP-02.json dan notes/LEG-SOP-02.md. Perubahan spec diterapkan lewat skrip pembangun di luar repo, lalu dibandingkan dengan salinan sebelum sweep: selisihnya hanya baris di bawah.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1. Butir 4.19 | "4.19 Dokumen sumber memakai kalimat pasif untuk beberapa langkah. Pelaku yang SOP ini tetapkan untuk langkah itu berstatus (USULAN): butir 4.6 dan 4.11, 6.4 langkah 9, 6.7 langkah 3 dan 8, serta 6.10 langkah 3 dan 6. Line Manager Legal sebagai pemilik rekaman di bagian 11 juga berstatus (USULAN)." | "4.19 Pelaku pada butir 4.6 dan 4.11, 6.4 langkah 9, 6.7 langkah 3 dan 8, serta 6.10 langkah 3 dan 6 berstatus (USULAN). Line Manager Legal sebagai pemilik rekaman di bagian 11, sama dengan SNX-LEG-SOP-03, juga berstatus (USULAN)." Catatan proses ("sumber memakai kalimat pasif") pindah ke notes, USULAN 3 |
| 1 (kalimat setara, scope) | "... tetap dimuat di bagian 8 karena tabel target waktu sumber memuatnya." | "... tetap dimuat di bagian 8." Alasan ada di notes, tabel cacat 4 baris e dan open item 5 |
| 1 (kalimat setara, Dokumen terkait SNX-LEG-SOP-01) | "Legal Operational. Sumber dokumennya, SOP Divisi Legal, memuat korporasi, perizinan, somasi, klaim, dan sengketa yang di luar scope SOP ini." | "Legal Operational. Memuat korporasi, perizinan, somasi, klaim, dan sengketa, yang di luar scope SOP ini." Isi scope specs/LEG-SOP-01.json dicek: memuat kelima topik itu |
| 1 (kalimat setara, SNX-HR-JA-01) | "... (JA-08 dan JA-09). Sumber SOP ini menyebutnya Jobdesc Line Manager Legal dan Jobdesc Legal Staff." | "... (JA-08 dan JA-09), tempat peran Line Manager Legal dan Staff Legal dipetakan." Rujukan Jobdesc di sumber tetap tercatat di bagian 2 baris 20 |
| 1 (kalimat setara, SNX-LEG-FRM-01) | "Customer Contract Review Checklist; checklist review untuk kontrak pelanggan (USULAN). Sumber SOP ini menyebutnya Contract Review Checklist." | "Customer Contract Review Checklist; dipakai sebagai checklist review untuk kontrak pelanggan (USULAN)." Rujukan sumber tetap di bagian 2 baris 20 dan USULAN 5 |
| 2. Label klausul ISO (iso_refs, "Status daftar klausul") | "Klausul di bawah berstatus (USULAN, dikonfirmasi konsultan)." | "Klausul di bawah berstatus (USULAN, perlu konfirmasi konsultan)." Hanya satu kemunculan di spec; notes diselaraskan |
| 3. Peran Staff Legal dan Line Manager Legal (tabel peran) | "Dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." dan versi JA-08 | "Peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." dan versi JA-08 |
| 3. Dokumen terkait SNX-HR-ORG-01 | "... Line Manager Legal dan Staff Legal dipetakan ke JA-08 dan JA-09, menunggu konfirmasi (K-13)." | "... Peran Line Manager Legal dan Staff Legal dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09) (USULAN, butir K-13)." |
| 3. Pemilik rekaman | "Line Manager Legal sebagai pemilik rekaman di bagian 11 juga berstatus (USULAN)." | Ditambah "sama dengan SNX-LEG-SOP-03". Dicek terhadap specs/LEG-SOP-03.json: pemilik rekaman Line Manager Legal dan pencatat Staff Legal (butir 4.26, USULAN di sana). Kolom pemilik dan pencatat di tabel rekaman bagian 11 sudah sama, tidak berubah |

Penjelasan kalimat yang dipindah dari badan dokumen: butir 4.19 melabeli sebagai USULAN pelaku yang sumber utama tidak sebut (kalimat pasif), dan pemilik rekaman; scope menaruh target respons korporasi dan perizinan di bagian 8 karena baris itu ada di tabel target waktu sumber utama; SNX-HR-JA-01 dan SNX-LEG-FRM-01 menggantikan nama Jobdesc dan Contract Review Checklist yang dipakai sumber.

Temuan di luar butir sweep (tidak diubah, menunggu instruksi):
- SNX-LEG-SOP-03 (draf paralel) sudah menetapkan lokasi (folder Google Drive departemen Legal, butir 4.8) dan retensi per kategori (USULAN di sana). Tabel rekaman dan scope dokumen ini masih menulis "Lokasi belum ditetapkan" dan retensi "Belum ditetapkan". Perlu keputusan LEAD apakah diselaraskan; bila ya, open item 3 ikut gugur.
- Baris Dokumen terkait "Template kontrak SINUX (NDA, PKS, addendum); belum disusun" dan prompt_addendum ("jangan menyatakan belum ada bila checklist menandai baris itu ada"): checklist baris 43 "NDA / Confidentiality Agreement Template" bertanda true. PKS dan addendum tidak punya baris checklist. Perlu keputusan LEAD untuk rumusan.

Hasil uji sesudah sweep: render exit 0; lint `"pass": true`, `"fails": []`, warn 16 (USULAN), warn PIC SLA nol; validator "All validations PASSED!"; blankscan "ok 24".

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A5 approval Prepared By | Staff Legal | Alif Altamziz / Staff Legal |
| A5 approval Reviewed By | Line Manager Legal | Ester Febe Utomo / Line Manager Legal |
| A5 bagian 5, Staff Legal (JA-09) | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| A5 bagian 5, Line Manager Legal (JA-08) | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| A5 bagian 11, baris SNX-HR-ORG-01 (rujukan silang) | ... (JA-08 dan JA-09) (USULAN, butir K-13). | ... (JA-08 dan JA-09). |
| A5 nama unit, Purpose | cara Divisi Legal PT Strategi ... | cara Departemen Legal PT Strategi ... |
| A5 nama unit, bagian 3 Register permintaan Legal | diterima Divisi Legal | diterima Departemen Legal |
| A5 nama unit, bagian 3 Review kontrak | oleh Divisi Legal | oleh Departemen Legal |
| A5 nama unit, caption Gambar 1 | oleh Divisi Legal | oleh Departemen Legal |
| A5 nama unit, bagian 11 template kontrak | menurut SOP Divisi Legal | menurut SOP Departemen Legal |
| A5 nama unit, bagian 11 format register | menurut SOP Divisi Legal | menurut SOP Departemen Legal |

Open item:

- Open item 10 (sumber utama draf tim yang sedang ditulis): ditutup W9: LEAD mengukur modifiedTime sumber tidak berubah (G-2).
- Open item 12 (penamaan unit): ditutup W9: A5, seluruh dokumen Legal memakai Departemen Legal.
- USULAN 4 (pemetaan JA-08 dan JA-09): ditutup W9: diputus owner (G-3 A5).
- Open item 7 (atasan Line Manager Legal, K-03): tetap terbuka (A4).
- A3: tidak ada perubahan; dokumen ini tidak menyebut atasan atau garis lapor JA-03 atau JA-04.
