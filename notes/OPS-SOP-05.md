# Catatan penyusun OPS-SOP-05: Service Level Agreement (SLA) Monitoring

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-SOP-05.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-SOP-05 (nomor lama dipertahankan), department Operation, classification "RESTRICTED (Internal)" mengikuti label sumber (worklist null), audit_class C1. Process owner "Service Delivery Manager" (jabatan tanpa nama, dari "Pemilik dokumen | Service Delivery Manager" di sumber). Approval persis dari config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Hasil uji terakhir (bukti mentah: /tmp/pen-OPS-SOP-05/lint.out.txt dan /tmp/pen-OPS-SOP-05/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-SOP-05.json /tmp/pen-OPS-SOP-05/OPS-SOP-05.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-OPS-SOP-05/OPS-SOP-05.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "8 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`, tanpa -I karena skrip itu mengimpor modul sebelahnya): "All validations PASSED!".
- soffice ke PDF: 16 halaman. Diagram (/tmp/pen-OPS-SOP-05/OPS-SOP-05_flow.png) dilihat; sepuluh simpul, rankdir TB, teks terbaca.
- Pemeriksaan tambahan atas spec (skrip python3 -I): nol em-dash dan en-dash; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode dokumen yang dirujuk di badan ada di tabel Dokumen terkait; tiap langkah paling banyak 25 kata; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, tanpa terkecuali, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli) dan singkatan SDM.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control tidak diubah. Berkas yang ditulis hanya specs/OPS-SOP-05.json dan notes/OPS-SOP-05.md; hasil render hanya di /tmp/pen-OPS-SOP-05/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-SOP-05_SOP_SLA_Monitoring.docx (165510 byte) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- | 2026-10-13T06:09:05Z (get_file_metadata hari ini, sama dengan prompt; fileSize 165510 sama dengan "bytes" di salinan audit) | read_file_content (teks penuh); download_file_content didekode ke /tmp/pen-OPS-SOP-05/src/src.docx dengan python3 -I: comments.xml dan footnotes.xml kosong, header dan footer hanya label dan nomor halaman, gambar word/media/rId25.png dibuka dan cocok dengan mermaid di salinan audit |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| Pembanding kolom dan sheet: SNX-OPS-FRM-09 (di luar daftar sumber prompt, dibaca saja) | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF | 2026-10-13T06:09:25Z (dari notes/OPS-FRM-09.md, tidak diukur ulang di sesi ini) | read_file_content (teks; nama sheet, kolom, dan nilai "Menit dalam periode" 43200 terbaca). Rumus `=DAY(B4)*1440` dikutip dari notes/OPS-FRM-09.md, tidak dibuka ulang |
| Pembanding peran penyusun RCA: SNX-OPS-FRM-10 | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS | tidak diukur ulang; dikutip dari specs/OPS-FRM-10.json dan notes/OPS-FRM-10.md | Dibaca dari spec dan notes sibling, bukan dari Drive |
| Kriteria penerimaan | config/checklist.json baris 67 | Description hanya nama berkas "SNX-OPS-SOP-05_SOP_SLA_Monitoring.docx" | Kriteria = substansi sumber tim + ISO 9001:2015 "8.2.3, 9.1.1, 9.1.2" dan ISO/IEC 27001:2022 "5.22, 8.16" |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md: bagian SNX-OPS-SOP-05 (dari baris 4489, bagian 5 mulai baris 4703), POL-OPS-001 (bagian 5 mulai baris 317), PRO-OPS-001 (bagian 5 mulai baris 720); catatan ML-00 baris 3088; legal-2026-10-14.md baris 367 | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Nama peran: Service Delivery Manager, Lead NOC, Lead SOC, Head of Operation (daftar jabatan Divisi Operation); VP Commercial (JA-03) |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat imperatif di POL dan PRO adalah langkah prosedur dan diperlakukan sebagai isi.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Peringatan dini: bila downtime yang dihitung melewati 50% anggaran sebelum akhir bulan, Lead NOC memberi tahu dua peran dan change non-darurat ditinjau ulang | "Bila downtime yang dihitung melewati 50% anggaran sebelum akhir bulan, Lead NOC memberi tahu Service Delivery Manager dan Head of Operation, dan change non-darurat pada layanan itu ditinjau ulang." (Bagian 6.4 butir 2) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |
| 2 | Siklus bulanan: data dikumpulkan paling lambat hari kerja ke-3, laporan SLA dikirim paling lambat hari kerja ke-5 | "Data dikumpulkan paling lambat hari kerja ke-3 bulan berikutnya." (Bagian 6.2 butir 4) dan "Laporan SLA bulanan dikirim ke pelanggan paling lambat hari kerja ke-5." (Bagian 6.5 butir 1) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |
| 3 | Target standar availability 99.9% per bulan, dengan anggaran downtime sekitar 43 menit untuk bulan 30 hari | "Target standar availability yang dikomunikasikan adalah 99.9% per bulan." (Bagian 4) dan "Untuk 99.9%, anggaran sekitar 43 menit per bulan 30 hari." (Bagian 6.4 butir 1) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "SOP ini menetapkan cara SINUX mengukur, memantau, melaporkan, dan menindaklanjuti pencapaian Service Level Agreement (SLA) kepada pelanggan, sehingga komitmen layanan dapat dibuktikan dengan data dan penyimpangan ditangani sebelum menjadi masalah kontrak." (Bagian 1) | Purpose, kalimat tim utuh |
| 2 | Scope | "Berlaku untuk semua layanan dengan SLA tertulis di kontrak, PKS, atau perjanjian layanan, termasuk SLA yang SINUX terima dari supplier (upstream infrastruktur, partner SOC, penyedia platform) karena memengaruhi SLA ke pelanggan." (Bagian 2) | Scope paragraf 1 |
| 3 | Pemilik, klasifikasi, acuan ISO | "Pemilik dokumen \| Service Delivery Manager"; "Klasifikasi \| RESTRICTED (Internal)"; "Acuan ISO 9001:2015 \| Klausul 8.2.3, 9.1.1, 9.1.2"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 5.22, 8.16" | meta.process_owner, meta.classification, iso_refs |
| 4 | Definisi availability, downtime, response, resolution, breach | "Availability \| (Menit dalam periode dikurangi menit downtime yang dihitung) dibagi menit dalam periode, dalam persen"; "Downtime yang dihitung \| Waktu layanan tidak tersedia, tidak termasuk window maintenance yang sudah dinotifikasi dan gangguan di luar tanggung jawab SINUX sesuai kontrak"; "Response SLA \| Persentase tiket yang di-ack dalam target per severity"; "Resolution SLA \| Persentase tiket yang dipulihkan dalam target pemulihan kontrak"; "Breach \| Pencapaian di bawah target kontrak dalam satu periode" | Definition |
| 5 | Kompensasi hanya di dokumen kontraktual | "Bahasa kompensasi atau service credit hanya ada di dokumen kontraktual, tidak di materi pemasaran atau proposal." (Bagian 4) | Policy 4.1 |
| 6 | Peran | "Service Delivery Manager \| Pemilik SOP; menyusun dan mengirim laporan SLA; memimpin review layanan"; "Lead NOC \| Menyediakan data availability dan tiket; validasi downtime"; "Lead SOC \| Menyediakan data SLA layanan SOC"; "Head of Operation \| Meninjau breach dan tindakan perbaikan"; "Commercial \| Menangani konsekuensi kontraktual dari breach" (Bagian 5) | Roles bagian 5 |
| 7 | Registrasi SLA saat G1, termasuk SLA supplier | "Saat onboarding (gate G1), Service Delivery Manager mencatat parameter SLA tiap pelanggan pada SNX-OPS-FRM-09 (sheet Parameter SLA): layanan, target availability, target response dan resolution, jam layanan, pengecualian, dan periode laporan." dan "SLA dari supplier yang menopang layanan pelanggan dicatat juga, untuk melihat apakah SLA ke pelanggan didukung SLA dari hulu." (6.1) | 6.1 langkah 1 dan 2 |
| 8 | Sumber data | "Data availability diambil dari Nusametric, Overseer, dan console Nusagrid." dan "Data tiket diambil dari SNX-OPS-FRM-08 (Zammad untuk Nusagrid, Service Hub untuk GMF dan internal)." (6.2) | 6.2 langkah 1 sampai 2 dan intro |
| 9 | Pencatatan downtime | "Setiap downtime dicatat dengan waktu mulai, waktu pulih, penyebab, dan apakah dihitung atau dikecualikan beserta alasannya." (6.2 butir 3) | 6.2 langkah 3 |
| 10 | Validasi pengecualian | "Lead NOC memvalidasi pengecualian downtime; pengecualian tanpa bukti notifikasi maintenance tidak boleh dikecualikan." (6.3 butir 2). Pelengkap dari form: "Catat setiap downtime di Downtime Log; kolom Dihitung = Tidak hanya bila ada bukti notifikasi maintenance atau pengecualian kontrak." (SNX-OPS-FRM-09, Cara pakai 2, fileId 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF) | 6.3 langkah 1, exceptions baris 1 (lihat asumsi 5) |
| 11 | Isi laporan, pelanggan pemerintah, review triwulanan | "Laporan berisi availability, daftar downtime, response dan resolution SLA, insiden P1 dan P2 beserta status RCA, serta rekomendasi teknis."; "Review layanan triwulanan dilaksanakan bersama pelanggan enterprise utama; masukan kepuasan pelanggan dicatat."; "Untuk pelanggan pemerintah, laporan teknis tanpa harga, diskon, tier, maupun roadmap komersil." (6.5 butir 2 sampai 4) | 6.5 langkah 1, 2, 4, 5 |
| 12 | Penanganan breach | "Breach dicatat di SNX-OPS-FRM-09 dan dianalisis dengan SNX-OPS-FRM-10."; "Head of Operation menetapkan tindakan perbaikan beserta pemilik dan tenggat."; "Konsekuensi kontraktual ditangani Commercial."; "Breach yang disebabkan supplier dicatat pada SNX-ISMS-FRM-03 sebagai bahan evaluasi supplier." (6.6) | 6.6 langkah 1 sampai 7 |
| 13 | Retensi record | "SLA Performance Monitoring Report \| SNX-OPS-FRM-09 \| 3 tahun"; "Technical Ticket / Incident Register \| SNX-OPS-FRM-08 \| 3 tahun"; "RCA untuk breach \| SNX-OPS-FRM-10 \| 5 tahun"; "Evaluasi supplier \| SNX-ISMS-FRM-03 \| Durasi kontrak + 3 tahun" (Bagian 7) | Records bagian 11 |
| 14 | Indikator kinerja | "Laporan SLA terkirim hari kerja ke-5 \| 100%"; "Layanan dengan availability sesuai target kontrak \| 100%"; "Breach dengan RCA dan tindakan perbaikan \| 100%" (Bagian 8) | SLA bagian 8, baris indikator |
| 15 | Penyusun RCA di form (SNX-OPS-FRM-10) | "Disusun (Lead NOC atau Lead SOC)", "Disetujui (Head of Operation)" (dikutip dari notes/OPS-FRM-10.md, fileId 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS) | 6.6 langkah 2 dan 3 |
| 16 | Kolom Parameter SLA dan Laporan Bulanan di FRM-09 | "ID,Pelanggan,Layanan,Target availability,Jam layanan,Pengecualian kontrak,Periode laporan,PIC penerima laporan,Catatan" (Parameter SLA); "Pelanggan,Layanan,Target,Downtime dihitung (menit),Availability,Status,Anggaran downtime (menit),Sisa anggaran (menit),Tiket P1 dan P2,Di-ack sesuai target,Response SLA,Catatan dan tindakan" (Laporan Bulanan); "Isi data respon tiket dari ringkasan SNX-OPS-FRM-08." (Cara pakai 4) | 6.1 intro, 6.3 langkah 2 dan 3, 6.4 langkah 1 |
| 17 | Zammad untuk Ops, GLPI (Service Hub) untuk generalist | config/defaults.json ticketing: "sistem tiket zammad untuk ops, glpi untuk generalist" | 6.2 intro, definisi Zammad dan Service Hub |
| 18 | Pengecualian lingkup divisi (bahan) | "Di luar ruang lingkup: app-level pelanggan (isi WordPress, plugin, DB aplikasi, kode pelanggan), keputusan harga dan komersial, serta SOC POLRI (tanggung jawab POLRI)." (POL-OPS-001 Bagian 2, fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv) | Scope paragraf 3 (hanya "keputusan harga dan komersial") |
| 19 | Riwayat revisi dan pengesahan sumber | Baris kedua: "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih"; "Diperiksa oleh \| ISO/ISMS Coordinator"; "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Tidak dibawa (diganti defaults; lihat bagian 4) |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur dan SLA |
|---|---|---|---|
| ISO 9001:2015 8.2.3 | Ya, "8.2.3 (Peninjauan persyaratan produk dan jasa)" | 4.1: parameter SLA pelanggan dicatat saat onboarding; target standar dan aturan bahasa kompensasi | 6.1; baris SLA availability |
| ISO 9001:2015 9.1.1 | Ya, "9.1.1 (Pemantauan, pengukuran, analisis, dan evaluasi: umum)" | 4.2: availability, response SLA, resolution SLA diukur tiap bulan | 6.2, 6.3; baris SLA anggaran, pengumpulan data, response, resolution, laporan |
| ISO 9001:2015 9.1.2 | Ya, "9.1.2 (Kepuasan pelanggan)" | 4.4: masukan kepuasan pelanggan dicatat dari review triwulanan | 6.5 langkah 4 dan 5; baris SLA review layanan; rekaman baru di bagian 11 |
| ISO/IEC 27001:2022 Annex A 5.22 | Ya, "5.22 (Pemantauan layanan supplier)" | 4.5: SLA supplier dicatat dan breach supplier jadi bahan evaluasi | 6.1 langkah 2; 6.6 langkah 7; exceptions baris 4 |
| ISO/IEC 27001:2022 Annex A 8.16 | Ya, "8.16 (Aktivitas pemantauan)" | 4.3: anggaran downtime dipantau selama bulan berjalan, peringatan dini | 6.4; baris SLA peringatan dini |

Nama klausul 8.2.3, 9.1.1, dan 8.16 berasal dari standar, bukan dari dokumen tim. "5.22 (pemantauan layanan supplier)" dan "9.1.2 (kepuasan pelanggan)" ada di sumber Bagian 3. Klausul 9.1.3 ada di sumber Bagian 3 tetapi tidak di baris checklist maupun atribut sumber; tidak dibawa (open item 14).

## 4. Penanganan cacat context/audit

Bagian 5 SNX-OPS-SOP-05 (fileId 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9-):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tidak ada angka target response dan resolution per severity | Diperbaiki sebagian: baris SLA Response SLA merujuk target response di Parameter SLA dan target Ack per severity di SNX-OPS-SOP-04 bagian 8 (angka tidak disalin, satu tempat); baris Resolution SLA menyatakan angka mengikuti kontrak dan tidak ditetapkan di SOP ini. Tidak ada angka baru. Open item 1 dan 2 |
| 2 | Anggaran 43 menit hanya untuk bulan 30 hari | Diperbaiki: definisi "Anggaran downtime" memuat rumus (menit dalam periode dikali 100% dikurangi target availability), yang sama dengan rumus anggaran di Laporan Bulanan FRM-09, sehingga bulan 31 hari punya cara hitung. Angka bulan 31 hari tidak ditulis karena tidak ada di sumber |
| 3 | Target pulih P1 di SNX-OPS-SOP-04 (4 jam) melebihi anggaran downtime bulanan 43 menit, hubungan tidak dijelaskan | Tidak diperbaiki dan tidak disalin: angka 4 jam tidak dibawa ke dokumen ini. Menjelaskan hubungan keduanya butuh keputusan. Open item 2 |
| 4 | Nilai menit ambang 50% (sekitar 21,5 menit) tidak ada di sumber, hanya hasil hitungan | Nilai menit tidak ditulis. Dokumen hanya memuat "50% anggaran" seperti sumber |
| 5 | FRM-09 dan FRM-08 ada dan nama sheet cocok | Nama sheet dipakai persis: Parameter SLA, Downtime Log, Laporan Bulanan. Temuan baru dari pembacaan FRM-09: Parameter SLA tidak punya kolom target response dan resolution, dan Laporan Bulanan tidak punya kolom resolution SLA (hanya Response SLA untuk tiket P1 dan P2). Diperbaiki sebagian dengan USULAN 2 (catat di kolom Catatan). Open item 1 |
| 6 | Klausul 9.1.3 di Bagian 3 tetapi tidak di atribut Acuan | Diselaraskan ke baris checklist dan atribut sumber (8.2.3, 9.1.1, 9.1.2). Open item 14 |
| 7 | Gambar: kotak "Peringatan dini" bertulis "Lead NOC ke SD Manager" saja, sedangkan teks 6.4 butir 2 menyebut Service Delivery Manager dan Head of Operation; validasi pengecualian tidak tergambar terpisah | Diperbaiki: simpul peringatan dini menyebut kedua penerima; simpul validasi ditulis "Validasi pengecualian dan hitung SLA". Gambar digambar ulang dengan 10 simpul dan referensi butir. Singkatan "SDM" tidak dipakai di mana pun karena catatan ML-00 (baris 3088) menandainya ambigu |
| 8 | Dua baris riwayat revisi Revisi 00 bertanggal sama, kolom Disetujui "Menunggu", tanda tangan kosong | Teratasi template: satu baris Revision 00 "Draft awal untuk review dan pengesahan", Effective Date kosong, Signature kosong. Tidak ada tanda tangan atau tanggal yang diisi |
| 9 | "keselarasan RTO dan target pulih" di riwayat revisi tanpa padanan | Kalimat tidak dibawa. SOP ini tidak memuat RTO atau RPO |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Bagian 6.3 sumber menghitung dulu lalu memvalidasi pengecualian, padahal perhitungan bergantung pada pengecualian yang sudah valid | Urutan dibalik: validasi (Lead NOC) lebih dulu, lalu hitung (Service Delivery Manager). Substansi tidak berubah. Asumsi 4 |
| B | Kalimat 6.3 butir 2 sumber, "pengecualian tanpa bukti notifikasi maintenance tidak boleh dikecualikan", kalau dibaca harfiah juga melarang pengecualian kontrak ("gangguan di luar tanggung jawab SINUX sesuai kontrak" di definisi) | Langkah dan exceptions memakai rumusan form FRM-09 (bukti notifikasi maintenance atau pengecualian kontrak di Parameter SLA). Asumsi 5. Open item 3 |
| C | Kalimat pasif tanpa pelaku: 6.2 butir 3, 6.3 butir 1, 6.4 butir 2 (peninjauan change), 6.6 butir 1, 2, dan 4 | Diberi pelaku dari tabel peran dan dari form FRM-09 dan FRM-10; lihat asumsi 1 sampai 3. Open item 5 |
| D | Judul 6.4 sumber "Pemantauan berjalan (early warning)" memakai dua istilah untuk satu hal | Judul jadi "Pemantauan berjalan dan peringatan dini"; satu istilah "peringatan dini" di seluruh dokumen |
| E | Sumber 6.5 butir 4 menulis "komersil" | Ditulis "komersial" |
| F | Sumber 6.2 butir 2 menulis "Zammad untuk Nusagrid, Service Hub untuk GMF dan internal"; premis owner "zammad untuk ops, glpi untuk generalist" | Dokumen memakai premis owner: tiket Ops (termasuk layanan Nusagrid) di Zammad, tiket GMF dan internal di Service Hub, batas generalist berlabel USULAN 1 |
| G | "Pelanggan enterprise utama" dan "hari kerja" tanpa definisi di sumber | Tidak didefinisikan (tidak ada sumber). Open item 8 |

Bagian 5 POL-OPS-001 (fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv) dan PRO-OPS-001 (fileId 1U8CAdibwBk9x_-Aic2lbev144d6WReTz), butir yang menyentuh dokumen ini:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| POL 2 dan 4 | Target KPI berlabel USULAN dan baseline belum diukur; KPI "Laporan bulanan terkirim hari kerja ke-5 100%" ada di POL bagian 11 | Tiga indikator SOP-05 dipertahankan tanpa label (T1, SOP-05 sumber utama), kalimat tim. Status berbeda di POL masuk open item 6 |
| PRO 2 | SDPM-04 butir 1 ("Kumpulkan data NOC dan SOC paling lambat hari kerja ke-3 bulan berikutnya. (USULAN)") dan butir 4 ("Review layanan triwulanan dengan pelanggan enterprise utama. (USULAN)") berlabel USULAN; butir 3 ("Kirim paling lambat hari kerja ke-5.") tanpa label | Sama: SOP-05 menulisnya sebagai aturan tim tanpa label; open item 6 |
| POL 6 | P-08 menetapkan semua tiket di GLPI; Bagian 13 butir 6 menunda GLPI sebagai sistem resmi | Dokumen memakai premis owner (temuan F di atas). Open item 7 |
| POL 7, PRO 8 | Rujukan internal (DOCTRINE, DEC, HANDOVER, CORE, SKILL_, SINUX_SERVICE_HUB, "packet setor", "jalur staging") | Tidak ada yang dibawa; lint lolos |
| POL 5, 11 | Nama pemegang jabatan kosong; RACI tidak selaras dengan approver change | Peran ditulis tanpa nama. Peninjauan change non-darurat di 6.4 memakai Lead NOC (asumsi 3); RACI POL tidak dipakai. Open item 5 |
| POL 13 | Matriks severity POL tidak memuat target pulih; target pulih hanya di SOP-04 | Sama dengan cacat SOP-05 nomor 3. Open item 2 |

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber SOP-05)

1. Pelaku kalimat pasif: pencatatan downtime (6.2 butir 3) oleh Lead NOC, karena peran sumber "Menyediakan data availability dan tiket; validasi downtime". Pencatatan parameter SLA dan breach di FRM-09 oleh Service Delivery Manager, pemilik FRM-09 menurut sumber FRM-09 ("Pemilik dokumen | Service Delivery Manager"). Perhitungan di Laporan Bulanan dan pengisian data respon tiket oleh Service Delivery Manager, karena ia menyusun laporan. Penyerahan breach ke VP Commercial oleh Service Delivery Manager (alur gambar sumber "info Commercial"; peran sumber tanpa pelaku).
2. RCA breach disusun Lead NOC (layanan NOC) atau Lead SOC (layanan SOC) mengikuti form SNX-OPS-FRM-10 ("Disusun (Lead NOC atau Lead SOC)"), dan dipecah jadi dua langkah supaya satu langkah satu pelaku. Pencatatan breach supplier di SNX-ISMS-FRM-03 oleh Head of Operation, pemilik dokumen FRM-03 menurut notes/ISMS-FRM-03.md.
3. Peninjauan ulang change non-darurat (6.4 butir 2 sumber, pasif) oleh Lead NOC: kalimat sumber bersubjek tunggal Lead NOC untuk seluruh butir. Bisa jadi Head of Operation; open item 5.
4. Urutan 6.3 dibalik (cacat tambahan A). Langkah mengisi data respon tiket dari ringkasan FRM-08 ditambahkan dari "Cara pakai 4" FRM-09, karena Laporan Bulanan memintanya dan SOP sumber tidak menyebut langkah itu.
5. Rumusan pengecualian downtime di 6.3 langkah 1 menggabungkan kalimat sumber 6.3 butir 2 dengan "bukti notifikasi maintenance atau pengecualian kontrak" dari Cara pakai 2 FRM-09 dan kolom "Pengecualian kontrak" di Parameter SLA. Tanpa penggabungan itu, pengecualian kontrak (yang ada di definisi sumber) tidak punya jalur sah.
6. "Hari kerja ke-5" ditulis "bulan berikutnya": sumber 6.2 menetapkan data selesai hari kerja ke-3 bulan berikutnya dan PRO-OPS-001 SDPM-04 menulis "Kirim paling lambat hari kerja ke-5" sesudah pengumpulan data bulan berikutnya.
7. PIC tiga indikator di bagian 8 (Service Delivery Manager untuk dua indikator pertama, Head of Operation untuk breach dengan RCA dan tindakan perbaikan) adalah tafsir: sumber Bagian 8 tidak memuat kolom PIC. Dasarnya peran sumber Bagian 5.
8. Definisi Ack dan Severity disamakan dengan SNX-OPS-SOP-04 (spec sibling); definisi NOC dan SOC dengan SNX-HR-ORG-01; definisi Window maintenance dipersingkat dari SNX-OPS-SOP-03 tanpa jam Shift 3 karena SOP ini tidak memakai jam itu. Definisi SLA, SLA supplier, Supplier, Tindakan perbaikan, RCA, Gate G1, Peringatan dini, dan Menit dalam periode adalah penjelasan penyusun yang diturunkan dari kalimat sumber (Bagian 1, 2, 6.1, 6.4, 6.6) dan FRM-09.
9. Scope pengecualian (SOP-04 untuk penanganan insiden, harga dan komersial ke VP Commercial) diturunkan dari rujukan SOP-05 ke SNX-OPS-SOP-04 (Bagian 3 sumber), 6.6 butir 3, dan POL-OPS-001 Bagian 2. Sumber SOP-05 sendiri tidak memuat pengecualian lingkup. Open item 9.
10. Tabel peran: "VP Commercial" untuk peran sumber "Commercial" (jabatan terdekat di HR-ORG-01, JA-03), sama dengan pemetaan di SNX-OPS-SOP-04. Peran lain memakai nama dari Daftar Jabatan Divisi Operation HR-ORG-01. "ISO/ISMS Coordinator" tidak dipakai di badan dokumen (HR-ORG-01 K-13: belum ditetapkan). Badan dokumen tidak menyebut COO maupun Direktur Utama, jadi aturan sebutan "Direktur (COO)" tidak terpakai.
11. Lokasi simpan rekaman (Folder Drive Operation) dan pemilik rekaman FRM-08 (Lead NOC) dan FRM-10 (Head of Operation) mengikuti SNX-OPS-SOP-04; pemilik FRM-09 dari sumber FRM-09; pemilik FRM-03 dari notes/ISMS-FRM-03.md. Sumber SOP-05 hanya memberi nomor dan masa simpan.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiket GMF dan internal di Service Hub, tiket Ops di Zammad; batas "generalist" belum dirinci owner | 6.2 intro | owner |
| 2 | Target response dan resolution per pelanggan dicatat di kolom Catatan sheet Parameter SLA, sampai FRM-09 punya kolomnya | 6.1 intro | Fani |
| 3 | Jabatan "VP Commercial" untuk peran sumber "Commercial" | Bagian 5, langkah 6.6 | owner |
| 4 | Batas hari kerja ke-3 untuk penyerahan data SLA layanan SOC oleh Lead SOC (sumber hanya menyebut batas itu untuk pengumpulan data) | Bagian 8, baris Lead SOC | Fani |
| 5 | Lokasi simpan "Folder Drive Operation" untuk lima rekaman di bagian 11 | Bagian 11, tabel rekaman | Fani |
| 6 | Rekaman baru "Catatan review layanan triwulanan dan masukan kepuasan pelanggan", pemilik Service Delivery Manager, retensi 3 tahun (disamakan dengan FRM-09); diminta klausul 9.1.2, sumber hanya menyebut "masukan kepuasan pelanggan dicatat" tanpa tempat | Bagian 11, tabel rekaman; 6.5 langkah 5 | Fani |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Ketidakcocokan SOP dan FRM-09: 6.1 meminta target response dan resolution dicatat di Parameter SLA, 6.3 meminta resolution SLA dihitung, tetapi Parameter SLA tidak punya kolom target itu dan Laporan Bulanan tidak punya kolom resolution SLA. Response SLA di Laporan Bulanan hanya untuk tiket P1 dan P2 (kolom "Tiket P1 dan P2", "Di-ack sesuai target"), sedangkan definisi sumber untuk semua tiket per severity. Perlu tambah kolom di FRM-09 atau ubah SOP | Fani |
| 2 | Target pulih internal P1 di SNX-OPS-SOP-04 (4 jam, USULAN) lebih panjang dari anggaran downtime bulanan 43 menit; tidak ada dokumen yang menjelaskan hubungannya. Angka resolution SLA kontrak tidak ada di dokumen mana pun | Fani |
| 3 | Pengecualian downtime: sumber menulis bukti notifikasi maintenance saja, form menulis bukti notifikasi maintenance atau pengecualian kontrak. Perlu konfirmasi bahwa rumusan form yang berlaku, dan siapa menyimpan bukti pengecualian kontrak | Fani |
| 4 | Target mana yang dipakai Response SLA bila kontrak pelanggan dan target Ack SNX-OPS-SOP-04 berbeda (SOP-04 menyebut target-nya internal; sumber SOP-05 menyebut "target per severity") | Fani |
| 5 | Pelaku yang tidak disebut sumber (asumsi 1 sampai 3). Lead NOC mencatat sekaligus memvalidasi downtime (tidak ada pemisahan peran). Peninjau ulang change non-darurat saat peringatan dini, arti "tinjau ulang", media pemberitahuan peringatan dini, dan rekaman tinjauan: tidak ada di sumber. Tidak ada batas waktu untuk peringatan dini, RCA breach, dan penetapan tindakan perbaikan | Fani |
| 6 | Status keputusan berbeda: POL-OPS-001 bagian 11 menyebut target awal KPI USULAN dengan baseline belum diukur (termasuk "Laporan bulanan terkirim hari kerja ke-5 100%"), dan PRO-OPS-001 SDPM-04 melabeli batas hari kerja ke-3 dan review triwulanan sebagai USULAN. SOP-05 menulisnya tanpa label. Periode ukur dan baseline tiga indikator bagian 8 juga tidak ada | Fani |
| 7 | Batas "generalist" Zammad lawan Service Hub (premis owner belum merinci) dan status GLPI sebagai sistem resmi (POL-OPS-001 bagian 13 butir 6) | owner |
| 8 | Istilah tanpa definisi di sumber: "pelanggan enterprise utama" (siapa saja) dan "hari kerja" (kalender libur yang dipakai) | Fani |
| 9 | Pengecualian lingkup di Scope diturunkan penyusun (asumsi 9). Perlu konfirmasi, termasuk apakah SOC POLRI (tanggung jawab POLRI menurut POL-OPS-001 bagian 2) dikecualikan dari pemantauan SLA | Fani |
| 10 | Cara pencatatan SLA supplier di FRM-09 (kolom Pelanggan dan Layanan dibuat untuk pelanggan) dan tindakan bila SLA supplier lebih rendah dari SLA ke pelanggan: sumber hanya menyuruh mencatat "untuk melihat apakah SLA ke pelanggan didukung SLA dari hulu" | Fani |
| 11 | SNX-ISMS-FRM-03 tidak punya kolom khusus breach SLA supplier menurut notes/ISMS-FRM-03.md dan audit (kolom Catatan ada); tempat pencatatan breach belum ditentukan | Fani |
| 12 | Data SLA layanan SOC: sumber data dan cara pencatatan downtime layanan SOC tidak ada di sumber (6.2 hanya menyebut Nusametric, Overseer, console Nusagrid untuk availability) | Fani |
| 13 | Availability dihitung dari menit kalender penuh (FRM-09 sel menit dalam periode), sedangkan Parameter SLA mencatat jam layanan yang tidak masuk rumus; layanan non 24x7 memerlukan keputusan penyebut | Fani |
| 14 | Klausul ISO 9001:2015 9.1.3 ada di Bagian 3 sumber tetapi tidak di checklist; ditanyakan apakah ditambahkan ke acuan | owner |
| 15 | Rujukan silang dari dokumen lain: SNX-OPS-FRM-10 menulis "SNX-OPS-SOP-05 Bagian 4" untuk definisi breach dan downtime yang dihitung; di dokumen 11 bagian definisi ada di bagian 3 (butir 6.6 penanganan breach tetap 6.6). SNX-OPS-PRC-01 menyebut SOP-05 untuk laporan KPI masukan tinjauan manajemen, yang tidak ada di SOP-05. FRM-09 Laporan Bulanan punya baris "Diperiksa (Head of Operation)" yang tidak ada langkahnya di SOP-05. Lane dokumen itu perlu menyelaraskan | LEAD |
| 16 | Rujukan "SNX-OPS-SOP-04 bagian 8" mengasumsikan SOP-04 versi 11 bagian (target Ack di bagian SLA); sumber SOP-05 menulis "Bagian 6" untuk dokumen sumber SOP-04. Perlu dicek ulang bila SOP-04 berubah | LEAD |

## 6. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI, dan perbaikannya:
- Enam butir kebijakan 4.1 sampai 4.6 berbentuk sama (label, klausul, pelaku, rujukan butir) dan tiap rujukan memakai "menurut butir" lawan tanda kurung. Rujukan disamakan jadi tanda kurung "(butir 6.x)" di bagian 4. Bentuk label dan klausul dipertahankan karena pemetaan klausul ke butir adalah yang dicari auditor, dan polanya sama dengan SNX-OPS-SOP-01 dan SNX-OPS-SOP-04.
- Judul 6.4 memakai dua istilah ("early warning" di sumber, "peringatan dini" di badan). Disatukan jadi "peringatan dini".
- "pada layanan itu" di langkah peninjauan change tidak menyebut layanan mana. Diganti "pada layanan yang memicu peringatan dini". "dari Commercial" di definisi Gate G1 diganti "dari VP Commercial" supaya nama peran sama dengan tabel peran.
- Nama peran diulang penuh (Service Delivery Manager muncul 35 kali) dan langkah prosedur berpola perintah yang sama. Dibiarkan: peran tidak diganti kata ganti atau "tim" (aturan satu istilah untuk satu hal), dan langkah prosedur memang satu tindakan satu pelaku.
- Kalimat tim dipertahankan apa adanya di Purpose, Scope paragraf 1, definisi Breach, Downtime yang dihitung, Response SLA, Resolution SLA, kebijakan 4.1 (kalimat 99.9% dan kompensasi), serta langkah sumber 6.2 sampai 6.5. Tidak ada pembuka generik, penutup positif, ekor penegas, rentang palsu, atau kelompok tiga yang dipaksakan (daftar "upstream infrastruktur, partner SOC, penyedia platform" dan daftar parameter SLA adalah kelompok dari sumber). Tidak ada tebal, huruf kapital, atau tanda kutip untuk penekanan di badan dokumen. Kesimpulan dua kalimat tanpa pujian.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: 99.9%, 43 menit, 50%, hari kerja ke-3 dan ke-5, triwulanan, 100% (tiga indikator), 3 tahun, 5 tahun, durasi kontrak ditambah 3 tahun: semuanya dari sumber SOP-05 Bagian 4, 6, 7, 8. "1.440" menit per hari adalah faktor hitung yang dipakai FRM-09 (`=DAY(B4)*1440`, dikutip dari notes/OPS-FRM-09.md). "Bulan berikutnya" pada hari kerja ke-5 diturunkan (asumsi 6). Retensi 3 tahun untuk catatan review layanan tidak bersumber dan berlabel (USULAN).
- Nama: tidak ada nama orang di badan dokumen. Nama di blok Approval dari config/defaults.json. Nama sistem (Zammad, Service Hub, GLPI, Nusametric, Overseer, Nusagrid) dari sumber dan defaults. Judul dokumen terkait dari worklist dan spec sibling.
- Tanggal: tidak ada tanggal di dokumen; Effective Date dan tanda tangan kosong.
- Tanpa sumber tertulis tetapi tidak berlabel: penugasan pelaku (asumsi 1 sampai 3 dan 7), definisi penjelas (asumsi 8), pengecualian lingkup (asumsi 9). Semuanya ada di notes dan open items (5, 9), bukan diklaim sebagai fakta sumber. Nama klausul ISO 8.2.3, 9.1.1, dan 8.16 berasal dari standar.
- Tidak ada fakta yang saya anggap tak berasal dari sumber di luar daftar itu. Hal yang tidak saya ukur: rumus FRM-09 dan isi FRM-10 dibaca dari notes sibling dan teks Drive, bukan dari berkas xlsx atau docx FRM-09 dan FRM-10 yang didekode; SNX-OPS-SOP-04 dibaca dari spec sibling, bukan dari sumber Drive-nya.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Kesebelas label (USULAN) tetap. Pada Peran VP Commercial, intro butir 6.2, dan baris SLA Penyerahan data SLA layanan SOC, label kini berdiri sendiri di akhir sel; penjelasan di dalam kurung dipindah ke bagian berikut.

### W10 kalimat dihapus atau dipindah
- Definisi Peringatan dini: "sudah melewati ambang di bagian 8 sebelum akhir bulan; langkahnya ada di butir 6.4." diganti fakta lengkap baris bagian 8: "sudah melewati 50% anggaran downtime sebelum akhir bulan." (baris itu tanpa USULAN).
- Intro butir 6.2: "Batas waktu pengumpulan data ada di bagian 8." diganti fakta dua baris bagian 8: data availability dan ticket paling lambat hari kerja ke-3 bulan berikutnya, dan data SLA layanan SOC diserahkan Lead SOC pada batas yang sama (USULAN).
- Bagian 8 baris Availability: "target standar yang dikomunikasikan ada di butir 4.1" diganti fakta butir 4.1 "99.9% per bulan" (butir 4.1 tanpa USULAN).
- Catatan pemetaan dipindah (STYLE §3.8): Peran VP Commercial "(USULAN: sumber menulis Commercial tanpa jabatan)"; bagian 8 "(USULAN: sumber menyebut batas ini untuk pengumpulan data)", artinya batas hari kerja ke-3 untuk data SOC diturunkan dari batas pengumpulan data; intro butir 6.2 "(USULAN: batas generalist menunggu owner)" ditulis "batas cakupan generalist masih menunggu keputusan owner (USULAN)".

### W10 selisih angka
nihil (build tidak mencatat selisih numbers atau usul_butir).

### W10 catatan
- Sebutan pihak luar: "pelanggan"; pihak penyedia tetap "supplier".
- Nomor butir 4.1 sampai 4.6 dan 6.1 sampai 6.6 serta judul bagian tidak berubah; SNX-OPS-FRM-10 merujuk butir SOP ini (G-2).
- Calque "yang SINUX terima" (2 kali) menjadi "yang diterima SINUX". "respon" menjadi "respons" (ejaan baku). "Tindakan perbaikan" tetap istilah terdefinisi dokumen ini; padanannya corrective action.

### W10 audit pointer
- .definitions[9][1]: lengkap; ambang bagian 8 = "Saat downtime yang dihitung melewati 50% anggaran sebelum akhir bulan" (tanpa USULAN); "langkahnya ada di butir 6.4" hanya penunjuk, langkah tetap di 6.4.
- .procedures[1].intro[0]: lengkap; memuat kedua batas bagian 8: "Pengumpulan data availability dan ticket | Paling lambat hari kerja ke-3 bulan berikutnya" (Lead NOC, tanpa USULAN) dan "Penyerahan data SLA layanan SOC | Paling lambat hari kerja ke-3 bulan berikutnya (USULAN ...)" (Lead SOC, label ikut).
- .sla[0][2]: lengkap; butir 4.1 "Target standar availability yang dikomunikasikan adalah 99.9% per bulan" (tanpa USULAN).

### W10 audit cakupan label
- .procedures[1].intro[0]: OK (label tetap pada Service Hub; batas ke-3 tanpa label dan data SOC berlabel sesuai SLA bed1bb6)

### W11 koreksi LEAD (cakupan dikembalikan ke bed1bb6, 15 Okt)
- .procedures[1].intro[0]: cakupan, label, pelaku, atau rujukan dikembalikan ke bed1bb6 (temuan pemeriksa makna buta LEAD, reports/w11/)
- .roles[4][1]: cakupan, label, pelaku, atau rujukan dikembalikan ke bed1bb6 (temuan pemeriksa makna buta LEAD, reports/w11/)
- .sla[4][2]: cakupan, label, pelaku, atau rujukan dikembalikan ke bed1bb6 (temuan pemeriksa makna buta LEAD, reports/w11/)
