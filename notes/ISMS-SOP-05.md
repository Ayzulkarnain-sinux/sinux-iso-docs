# Catatan penyusun ISMS-SOP-05: SOP Vulnerability & Patch Management

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-SOP-05.json. Mode sop, aksi T1, wave W2, nomor SNX-ISMS-SOP-05 (nomor lama dipertahankan), department Operation, classification "RESTRICTED (Internal)" mengikuti label sumber (worklist null), audit_class B. Process owner "Lead SOC" (jabatan tanpa nama, dari "Pemilik dokumen | Lead SOC" di sumber). Approval persis dari config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Catatan worklist "sumber pendukung POL-OPS-001 dan PRO-OPS-001 (bahan saja)": keduanya dipakai untuk nama peran, pemeriksaan silang, dan cacat; tidak ada kalimat mereka yang disalin ke dokumen.

Hasil uji terakhir (bukti mentah: /tmp/pen-ISMS-SOP-05/lint.out.txt dan /tmp/pen-ISMS-SOP-05/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-SOP-05.json /tmp/pen-ISMS-SOP-05/ISMS-SOP-05.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-ISMS-SOP-05/ISMS-SOP-05.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "12 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`, tanpa -I karena skrip itu mengimpor modul sebelahnya): "All validations PASSED!".
- soffice ke PDF: 17 halaman. Diagram (/tmp/pen-ISMS-SOP-05/ISMS-SOP-05_flow.png) dilihat: sebelas simpul, rankdir TB, tiga diamond, satu garis putus-putus, teks terbaca. Teks PDF dibaca penuh.
- Pemeriksaan tambahan atas spec (skrip /tmp/pen-ISMS-SOP-05/build_spec.py, python3 -I): tiap langkah paling banyak 25 kata; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode dokumen yang dirujuk di badan ada di tabel Dokumen terkait; nol em-dash dan en-dash; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, tanpa terkecuali, tanpa kompromi, hulu ke hilir, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli) dan ejaan komersil, diagnosa, efektifitas, frekwensi, sistim, katagori.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control, reference tidak diubah. Berkas yang ditulis hanya specs/ISMS-SOP-05.json dan notes/ISMS-SOP-05.md; hasil render hanya di /tmp/pen-ISMS-SOP-05/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-SOP-05_SOP_Vulnerability_Patch_Management.docx (176549 byte) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC | 2026-10-13T06:09:02Z (get_file_metadata hari ini, sama dengan prompt; fileSize 176549 sama dengan "bytes" di salinan audit) | read_file_content (teks penuh), download_file_content (docx didekode ke /tmp/pen-ISMS-SOP-05/src/src.docx dengan python3 -I): comments.xml dan footnotes.xml kosong, header dan footer hanya label dan nomor halaman, gambar word/media/rId26.png dibuka dan cocok dengan mermaid di salinan audit |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| Kriteria penerimaan | config/checklist.json baris 89 | Description hanya nama berkas "SNX-ISMS-SOP-05_SOP_Vulnerability_Patch_Management.docx" | Kriteria = substansi sumber tim + ISO 9001:2015 "10.2" dan ISO/IEC 27001:2022 "5.7, 8.7, 8.8, 8.19" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md bagian SNX-ISMS-SOP-05 (dari baris 3054, bagian 5 dari baris 3234); iso-sinux-supdocs-ops-2026-10-14.md bagian POL-OPS-001 dan PRO-OPS-001 (bagian 5 masing-masing) | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive: teks SOP-05 di Drive sama dengan salinan audit |
| Pemeriksaan silang peran dan rekaman (bahan, bukan sumber) | specs/HR-ORG-01.json (DONE), specs/OPS-SOP-02.json, specs/OPS-SOP-03.json, specs/ISMS-SOP-01.json, specs/ISMS-SOP-02.json, notes/OPS-FRM-04.md, OPS-FRM-07.md, OPS-FRM-08.md, ISMS-REG-03.md, config/defaults.json | repo kerja | Dibaca dari repo, bukan dari Drive terbaru; isinya bisa basi bila tim sudah mengubah dokumen itu |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat imperatif di POL dan PRO adalah langkah prosedur dan diperlakukan sebagai isi.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Prioritas Darurat diukur dari eksploitasi aktif dan keterjangkauan dari internet, bukan dari skor CVSS; tenggatnya 72 jam dengan mitigasi dalam 24 jam, dan tenggat semua prioritas berlabel USULAN oleh tim | "Darurat \| Dieksploitasi aktif di dunia nyata dan dapat dijangkau dari internet, atau RCE tanpa autentikasi \| 72 jam; mitigasi sementara (blok WAF, matikan fitur) dalam 24 jam" dan "Tenggat di atas adalah USULAN dan disahkan bersama SNX-ISMS-REG-03." (Bagian 6) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |
| 2 | Pengecualian prioritas Darurat dan Kritis butuh persetujuan Head of Operation dan dicatat sebagai risiko yang diterima | "Pengecualian untuk prioritas Darurat dan Kritis butuh persetujuan Head of Operation dan dicatat di SNX-ISMS-REG-03 sebagai risiko yang diterima." (Bagian 7.4 butir 2) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |
| 3 | Vulnerability yang dieksploitasi aktif diperlakukan sebagai potensi insiden, dengan sweep IOC sebelum dan sesudah patch | "Vulnerability yang dieksploitasi aktif pada aset kita diperlakukan sebagai potensi insiden: lakukan sweep IOC sesuai SNX-ISMS-SOP-01 sebelum dan sesudah patch, karena patch tidak menghapus kompromi yang sudah terjadi." (Bagian 7.2 butir 5) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |

## 2. Fakta pendukung dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Sumber (fileId) dan posisi |
|---|---|---|---|
| 1 | Tujuan, kalimat tim dipertahankan utuh | "SOP ini menetapkan cara SINUX memperoleh informasi technical vulnerability, menilai paparannya, dan menutupnya melalui patch atau mitigasi dalam tenggat yang sesuai risiko, termasuk perlindungan terhadap malware." | 160t8..., Bagian 1 |
| 2 | Scope dan pengecualian patch aplikasi pelanggan | "Berlaku untuk sistem internal SINUX dan sistem pelanggan yang patching-nya menjadi tanggung jawab SINUX menurut kontrak" dan "Patch aplikasi milik pelanggan menjadi tanggung jawab developer atau PIC pelanggan; SINUX menyampaikan temuan dan rekomendasinya." | 160t8..., Bagian 2 |
| 3 | Pemilik dokumen | "Pemilik dokumen \| Lead SOC" | 160t8..., tabel atribut |
| 4 | Sumber informasi dan frekuensi telaah | "Lead SOC menelaah sumber tersebut minimal mingguan dan segera untuk advisory kritis." | 160t8..., Bagian 5 |
| 5 | Kriteria Kritis, Tinggi, Sedang, Rendah | "Kritis \| CVSS 9.0 atau lebih \| 7 hari", "Tinggi \| CVSS 7.0 sampai 8.9 \| 30 hari", "Sedang \| CVSS 4.0 sampai 6.9 \| 90 hari", "Rendah \| CVSS di bawah 4.0 \| Siklus patch berikutnya" | 160t8..., Bagian 6 |
| 6 | Penyesuaian prioritas | "Prioritas dapat dinaikkan atau diturunkan berdasarkan paparan aktual (dapat dijangkau dari internet atau tidak), nilai aset, dan mitigasi yang sudah ada." | 160t8..., Bagian 6 |
| 7 | Scan dan tiket temuan | "Authenticated vulnerability scan terhadap aset internal dan aset pelanggan yang dikelola minimal bulanan, dan setelah perubahan besar." dan "Temuan dicatat sebagai tiket dengan ID aset dari SNX-ISMS-REG-01, CVE, prioritas, dan tenggat." | 160t8..., 7.1 butir 1 dan 3 |
| 8 | Scan eksternal | "Scan eksternal (dari vantage di luar network internal) terhadap layanan yang terbuka ke internet minimal bulanan." | 160t8..., 7.1 butir 2 |
| 9 | Patch lewat change request | "Pemasangan patch pada production melalui SNX-OPS-SOP-02: patch rutin sebagai change Standar atau Normal di window maintenance; patch darurat boleh sebagai change Emergency." | 160t8..., 7.2 butir 2 |
| 10 | Larangan di server cPanel | "Di server cPanel, yum install atau remove perl-\* dilarang; update mengikuti mekanisme resmi panel." | 160t8..., 7.2 butir 3 |
| 11 | Mitigasi kompensasi | "Bila patch belum tersedia atau tidak bisa dipasang, terapkan mitigasi kompensasi (rule WAF, nonaktifkan layanan yang vulnerable, batasi akses network) dan catat." | 160t8..., 7.2 butir 4 |
| 12 | Verifikasi penutupan | "Penutupan diverifikasi dengan scan ulang atau pemeriksaan versi; klaim tertutup didukung dua sumber." dan "Tiket ditutup dengan bukti verifikasi." | 160t8..., 7.3 |
| 13 | Isi pengecualian | "Patch yang tidak dapat dipasang sesuai tenggat dicatat sebagai pengecualian: alasan, mitigasi, tanggal tinjau ulang, dan persetujuan pemilik aset." | 160t8..., 7.4 butir 1 |
| 14 | Malware dan unduhan | "Server dan laptop kerja menjalankan anti-malware atau EDR yang aktif dan diperbarui; fleet hosting pelanggan memakai solusi yang disepakati kontrak (misalnya ImunifyAV untuk panel hosting tertentu)." dan "Download software hanya dari sumber resmi dan diverifikasi checksum bila tersedia." | 160t8..., 7.5 butir 1 dan 3 |
| 15 | Peran | "Lead NOC dan NOC Engineer \| Menjadwalkan dan memasang patch melalui change request", "Pemilik aset \| Menyetujui window patch dan menerima risiko bila patch ditunda", "Service Delivery Manager \| Mengomunikasikan temuan dan jadwal kepada pelanggan" | 160t8..., Bagian 4 |
| 16 | Rekaman dan retensi | "Tiket temuan vulnerability dan patch \| SNX-OPS-FRM-08 \| 3 tahun" dan "Laporan scan \| Folder SOC (RESTRICTED) \| 3 tahun" dan "Pengecualian dan risiko diterima \| SNX-ISMS-REG-03 \| Berlaku sampai digantikan" | 160t8..., Bagian 8 |
| 17 | Indikator kinerja | "Vulnerability Darurat dan Kritis ditutup dalam tenggat \| 95%", "Vulnerability Tinggi ditutup dalam tenggat \| 90%", "Cakupan scan bulanan terhadap aset produksi \| 100%", "Endpoint dengan anti-malware aktif \| 100%" | 160t8..., Bagian 9 |
| 18 | Tiket Ops di Zammad | Premis owner 14 Okt (config/defaults.json "ticketing"): "sistem tiket zammad untuk ops, glpi untuk generalist" | defaults v21, bukan berkas Drive |
| 19 | Lead SOC mengirim advisory ke NOC | "vulnerability advisory ke NOC" (tanggung jawab Lead SOC) | 1bn7..., POL-OPS-001 bagian 9.3 |
| 20 | Pelaku telaah advisory di PRO-OPS-001 berbeda | "Pelaksana: SOC Analyst · Akuntabel: Lead SOC · Pemicu: advisory CVE baru." dan "CVE kritis yang dapat dieksploitasi dari luar dan menyentuh aset SINUX = tiket P2 minimal, rekomendasi patch ke NOC." | 1U8C..., PRO-OPS-001 SOC-04 |
| 21 | Perubahan production wajib go-gate, rule WAF termasuk change Normal | "Setiap perubahan pada production pelanggan atau infra SINUX hanya boleh dieksekusi setelah lima syarat go-gate terpenuhi" dan "Normal \| Resize VM, update konfigurasi web server, instal SSL, ubah rule WAF" | 1bn7..., POL-OPS-001 bagian 7 |
| 22 | Hypervisor Nusagrid dieskalasi ke pihak upstream, WAF dan jaringan ke Tech dan Product | "Infra Nusagrid backend (hypervisor, console platform, node, billing sistem) \| Maxcloud atau Awandata, via grup Nusagrid" dan "WAF (AegisWAF), load balancer, proxy, web, IDVE, DC fisik, jaringan \| om Ipe (Tech dan Product)" | 1bn7..., POL-OPS-001 bagian 6, matriks eskalasi fungsional |
| 23 | Di luar ruang lingkup Divisi Operation | "Di luar ruang lingkup: app-level pelanggan (isi WordPress, plugin, DB aplikasi, kode pelanggan), keputusan harga dan komersial, serta SOC POLRI (tanggung jawab POLRI)." | 1bn7..., POL-OPS-001 bagian 2 |
| 24 | Patch di PM bulanan dan patch kritis segera | "Patch keamanan dan update OS sesuai SNX-ISMS-SOP-05 \| NOC Engineer \| Bulanan, atau segera untuk patch kritis"; "Suplai daftar patch keamanan untuk PM patch dan update OS. \| Lead SOC \| Daftar patch keamanan" | specs/OPS-SOP-03.json (draf sibling, bukan Drive) |
| 25 | Pemilik rekaman dan pelaku di dokumen sibling | FRM-08 dan FRM-07: "Pemilik dokumen \| Lead NOC"; FRM-04: "Pemilik dokumen \| Head of Operation"; REG-03: B10 "ISMS Coordinator"; OPS-SOP-02: Lead NOC "Menyetujui change Standar; menyetujui change Normal bersama ack pelanggan" | notes/OPS-FRM-08.md, OPS-FRM-07.md, OPS-FRM-04.md, ISMS-REG-03.md, specs/OPS-SOP-02.json (dibaca dari repo) |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur dan SLA |
|---|---|---|---|
| ISO 9001:2015 10.2 | Ya, "10.2 (Nonconformity and corrective action)" | 4.7: tiap temuan jadi tiket temuan, ditangani sampai tertutup, ditutup dengan bukti verifikasi | 6.2, 6.5; baris indikator kinerja |
| ISO/IEC 27001:2022 Annex A 5.7 | Ya, "5.7 (Threat intelligence)" | 4.1: empat jenis sumber, telaah oleh Lead SOC | 6.1; baris SLA telaah sumber |
| Annex A 8.7 | Ya, "8.7 (Protection against malware)" | 4.9: anti-malware atau EDR aktif, deteksi ditangani lewat SNX-ISMS-SOP-01 | 6.7; indikator endpoint |
| Annex A 8.8 | Ya, "8.8 (Management of technical vulnerabilities)" | 4.2, 4.3, 4.4, 4.5, 4.6, 4.8 | 6.2, 6.3, 6.4, 6.5, 6.6; baris SLA scan dan tenggat |
| Annex A 8.19 | Ya, "8.19 (Installation of software on operational systems)" | 4.4 (patch di production lewat change request) dan 4.10 (software dari sumber resmi) | 6.3, 6.7 |

Sumber SOP-05 menulis "8.19" tanpa nama dan tanpa penjelasan; nama kontrol itu berasal dari standar, bukan dari dokumen tim. Pemetaan 8.19 ke patch di production dan ke unduhan software adalah tafsir penyusun (asumsi 10). Nama 10.2 juga dari standar.

## 4. Penanganan cacat context/audit

Bagian 5 SNX-ISMS-SOP-05 (fileId 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tenggat Bagian 6 berlabel USULAN dan "disahkan bersama SNX-ISMS-REG-03", tetapi REG-03 tidak memuat tenggat patch | Tidak diperbaiki, tidak bisa tanpa keputusan: setiap baris tenggat di SLA memakai label (USULAN) dan butir 4.2 menyatakan statusnya. Tidak ada angka baru. Open item 1 |
| 2 | Kriteria Darurat tidak memakai CVSS, sehingga CVSS 9.0 atau lebih tanpa eksploitasi masuk Kritis; tidak ada aturan bila skor CVSS tidak tersedia | Sebagian: butir 4.3 dipertahankan dari sumber (prioritas dapat dinaikkan atau diturunkan), dan baris pengecualian "Skor CVSS belum tersedia" memberi prioritas sementara berdasarkan tiga dasar yang sama (USULAN 11). Kriteria Darurat tidak diubah. Open item 6 |
| 3 | Empat skala memakai nama Kritis, Tinggi, Sedang, Rendah tanpa pemetaan | Sebagian: definisi "Prioritas patch" menyatakan skala ini terpisah dari severity tiket P1 sampai P4 (SNX-OPS-SOP-04) dan dari level risiko (SNX-ISMS-REG-02), dan nama itu di dokumen ini selalu berarti prioritas patch. Pemetaan antarskala tidak ditulis karena tidak ada sumber. Open item 5 |
| 4 | KPI hanya Darurat dan Kritis (95%) dan Tinggi (90%); Sedang dan Rendah tanpa target | Tidak diperbaiki: target baru adalah angka tanpa sumber. Empat indikator sumber dipertahankan dengan angka aslinya. Open item 3 |
| 5 | Larangan yum install dan remove perl-* hanya untuk server cPanel | Dipertahankan apa adanya di butir 4.4 (lingkup cPanel). Tidak ada aturan stack lain yang diada-adakan. Sama dengan POL-OPS-001 bagian 7 dan SNX-OPS-SOP-02 |
| 6 | Rujukan SNX-OPS-SOP-02 dan SNX-OPS-SOP-03 sesuai judul; FRM-04 dan FRM-07 sejalan; FRM-08 tidak punya kelas vulnerability atau patch dan severity-nya P1 sampai P4; REG-03 tidak diberi judul di SOP-05 | Judul dokumen memakai judul dari tabel Dokumen terkait sibling. REG-03 diberi judul "Information Security Risk Treatment Plan" di tabel bagian 11. Kekurangan FRM-08 tidak bisa diperbaiki dari SOP ini: tiket temuan ditandai lewat istilah "tiket temuan" dan prioritas patch di tiket, rekap di FRM-08. Open item 12 |

Cacat tambahan yang saya temukan di sumber:

| # | Temuan | Penanganan |
|---|---|---|
| A | Gambar sumber: kotak "Mitigasi kompensasi" dan "Pengecualian" tidak punya panah lanjutan; kotak penutup menulis "bukti scan ulang" saja, sedangkan teks 7.3 menyebut scan ulang atau pemeriksaan versi dan dua sumber | Diagram digambar ulang (11 simpul, TB): mitigasi diarahkan ke verifikasi, pengecualian jadi ujung cabang dari "Tertutup terverifikasi sebelum tenggat?", kotak penutup menulis "bukti verifikasi". Arah mitigasi ke verifikasi adalah tafsir penyusun. Open item 8 |
| B | Dua istilah untuk satu hal: "mitigasi sementara" (tabel Bagian 6) dan "mitigasi kompensasi" (7.2 butir 4) | Satu istilah "mitigasi kompensasi" di seluruh dokumen, didefinisikan di bagian 3 |
| C | Pasif tanpa pelaku: 7.1 (scan, pencatatan tiket), 7.2 butir 1 dan 4, 7.3, 7.4, 7.5 | Diberi pelaku dari tabel peran dan dari POL-OPS-001 bagian 9; lihat asumsi 1 sampai 6. Open item 9 |
| D | "perubahan besar", "advisory kritis", dan "dua sumber" tanpa definisi; "atau" pada "scan ulang atau pemeriksaan versi" bertemu "dua sumber" | "Perubahan besar" dan "Dua sumber" diberi definisi berlabel (USULAN 2 dan 1). "Advisory kritis" tidak didefinisikan (tidak ada sumber), ditulis huruf kecil agar tidak tertukar dengan prioritas Kritis. Open item 7 dan 13 |
| E | Tenggat tanpa titik awal dan tanpa satuan hari (kalender atau kerja) | Definisi "Tenggat" memberi titik awal dan hari kalender, berlabel (USULAN 3). Open item 2 |
| F | Header sumber "Masa simpan record | Berlaku sampai digantikan" bertabrakan dengan tabel record (3 tahun untuk empat rekaman) | Template tidak punya slot masa simpan di blok identitas. Tabel rekaman bagian 11 memakai angka per rekaman dari sumber Bagian 8. Open item 17 |
| G | Riwayat revisi dua baris bertanggal sama, kolom Disetujui "Menunggu"; frasa "keselarasan RTO dan target pulih" tanpa padanan | Teratasi template: satu baris Revision 00, Effective Date kosong, tanda tangan kosong. Frasa RTO tidak dibawa, SOP ini tidak memuat RTO |
| H | Sumber: "aset kita" (7.2 butir 5) tidak jelas apakah aset pelanggan termasuk | Ditulis tanpa kata ganti: butir 4.6 dan 6.3 tidak membatasi ke aset internal; scope bagian 2 yang menentukan. Open item 14 |
| I | Blok pengesahan sumber: Diperiksa oleh "ISO/ISMS Coordinator", Disetujui oleh COO | Diganti dengan data config/defaults.json (reviewed Fani Fatullah, approved Samuel Kristanto Utomo / President Director, kunci D2). Pembalik ada di owner |
| J | Zammad atau GLPI tidak disebut sumber; "tiket" saja | Tiket Ops di Zammad mengikuti premis owner. Open item 15 |

Butir POL-OPS-001 dan PRO-OPS-001 (fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv dan 1U8CAdibwBk9x_-Aic2lbev144d6WReTz) yang menyentuh dokumen ini:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| POL 6 | P-08 menetapkan semua tiket di GLPI, bagian 13 butir 6 menunda GLPI sebagai sistem resmi | Dokumen memakai premis owner (Zammad untuk Ops). Open item 15 |
| POL 7, PRO 8 | Rujukan internal (DOCTRINE, DEC, HANDOVER, CORE, SKILL_, SINUX_SERVICE_HUB, "packet setor", "jalur staging") | Tidak ada yang dibawa; lint lolos. Pasal go-gate (POL P-04) dipakai sebagai dasar tafsir di asumsi 5 tanpa menyebut kode rujukannya |
| POL 3 | Pemilik dokumen POL-OPS-001 bertentangan antara COO dan Head of Operation | Tidak menyentuh SOP-05; pemilik SOP-05 mengikuti sumbernya sendiri (Lead SOC) |
| PRO 10 | SOC-04 kolom Dasar kebijakan "POL §7" padahal POL bagian 7 adalah change management | Tidak dibawa. Dicatat di open item 10 bersama perbedaan pelaku telaah advisory |
| PRO 3 | PRO-OPS-001 tidak berdiri sendiri (matriks severity ada di POL) | Tidak relevan ke SOP-05 selain skala P1 sampai P4 di definisi "Prioritas patch" (open item 5) |

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber SOP-05)

1. Pelaku kalimat pasif di 7.1: scan dan triage oleh SOC Analyst (peran sumber "Vulnerability scan, triage temuan"), pembuatan tiket oleh SOC Analyst, penetapan prioritas dan pengisian tenggat oleh Lead SOC (peran sumber "menilai prioritas"). Dipisah supaya yang menetapkan dan yang mencatat berbeda.
2. Lead SOC meneruskan tiket temuan ke Lead NOC (6.2 langkah 6) dan advisory yang berlaku ke SOC Analyst (6.1 langkah 2). Sumber SOP-05 tidak menyebut serah terima ini; dasarnya "vulnerability advisory ke NOC" (POL-OPS-001 bagian 9.3) dan langkah Lead SOC di SNX-OPS-SOP-03 ("Suplai daftar patch keamanan").
3. Pembagian pemasangan patch: NOC Engineer menguji, mengajukan change request, dan memasang (pengaju dan pelaksana menurut SNX-OPS-SOP-02); Lead NOC mengusulkan jadwal di window maintenance (peran sumber "Menjadwalkan"); Pemilik aset menyetujui window (peran sumber). Persetujuan change request sendiri tidak diulang, mengikuti SNX-OPS-SOP-02. Output "jadwal di SNX-OPS-FRM-07" dan "service report di SNX-OPS-FRM-07" berasal dari record sumber "Jadwal dan service report patch bulanan".
4. Penutupan: SOC Analyst memeriksa (scan ulang atau pemeriksaan versi), Lead SOC memverifikasi dan menutup tiket (peran sumber "memverifikasi penutupan"). Tafsir "dua sumber" = dua bukti dari cara berbeda, contoh scan ulang dan pemeriksaan versi, berlabel (USULAN 1).
5. Mitigasi kompensasi dilakukan NOC Engineer (sumber tanpa pelaku; rule WAF dan SIEM di POL-OPS-001 dan SNX-OPS-SOP-02 dijalankan NOC Engineer atau SOC Analyst). Kalimat "Mitigasi yang mengubah production mengikuti SNX-OPS-SOP-02" ditambahkan karena POL-OPS-001 bagian 7 mewajibkan go-gate untuk setiap perubahan production dan menyebut "ubah rule WAF" sebagai change Normal. Sumber SOP-05 hanya menyebut change request untuk pemasangan patch. Open item 11.
6. Pencatat pengecualian: Lead SOC (sumber pasif). Persetujuan oleh Pemilik aset (semua pengecualian) dan Head of Operation (Darurat dan Kritis), sesuai 7.4. Pencatatan di SNX-ISMS-REG-03 dibaca hanya untuk Darurat dan Kritis (7.4 butir 2); pengecualian prioritas lain dicatat di tiket temuan (7.4 butir 1 tidak menyebut tempat). Langkah tinjau ulang di tanggal tinjau ulang ditambahkan karena sumber mewajibkan tanggal itu tetapi tidak menunjuk peninjau (USULAN 10).
7. Pelaku perlindungan malware: SOC Analyst memeriksa anti-malware atau EDR di endpoint (POL-OPS-001 bagian 9.3: SOC Analyst memantau EDR) dan menangani deteksi (SNX-ISMS-SOP-01: SOC Analyst triage event); NOC Engineer memeriksa fleet hosting pelanggan; "Seluruh personel" untuk aturan unduhan, nama peran sama dengan SNX-ISMS-SOP-01. Sumber 7.5 tanpa pelaku.
8. Indikator kinerja: PIC Lead SOC (pemilik SOP, memantau kepatuhan), pola sama dengan SNX-ISMS-SOP-01. Sumber Bagian 9 tanpa kolom PIC. PIC baris tenggat "Lead NOC dan NOC Engineer" mengikuti peran sumber "Menjadwalkan dan memasang patch".
9. "Patch darurat" di 7.2 butir 2 dibaca sebagai patch untuk vulnerability prioritas Darurat. "Patch rutin" tidak dipakai sebagai istilah; langkah menyebut jenis change Standar atau Normal dan Emergency boleh untuk prioritas Darurat.
10. Definisi di bagian 3 adalah penjelasan penyusun yang diturunkan dari kalimat sumber, dari dokumen sibling (change request, Window maintenance, PIC pelanggan, IOC, Zammad), atau dari pengetahuan umum (BSSN, CISA, CSIRT, CVE, CVSS skala 0 sampai 10, RCE, EDR, WAF). Tidak ada fakta SINUX yang diperkenalkan lewat definisi. Nama klausul 8.19 dan 10.2 dari standar. Pemetaan 8.19 ke patch di production dan unduhan software adalah tafsir.
11. Pengecualian lingkup di bagian 2: patch aplikasi pelanggan dari sumber Bagian 2; "penanganan insiden keamanan diatur di SNX-ISMS-SOP-01" diturunkan penyusun dari rujukan sumber (7.2 butir 5 dan 7.5 butir 2). Open item 14.
12. Lokasi dan pemilik rekaman (bagian 11): sumber hanya memberi nomor dan masa simpan, dan lokasi "Folder SOC (RESTRICTED)". Pemilik FRM-08 dan FRM-07 (Lead NOC), FRM-04 (Head of Operation), REG-03 (ISMS Coordinator) diambil dari notes sibling yang mengutip sumber masing-masing; "Google Drive" untuk REG-03 mengikuti SNX-ISMS-SOP-01. "ISMS Coordinator" hanya muncul di tabel rekaman, tidak di tabel peran, karena SOP ini tidak memberinya tugas dan HR-ORG-01 menulis belum ditetapkan (K-13). Pemilik laporan scan (Lead SOC) berlabel (USULAN 12).
13. Pemetaan peran sumber ke HR-ORG-01: Lead SOC, SOC Analyst, Lead NOC, NOC Engineer, Head of Operation, Service Delivery Manager sudah ada di Daftar Jabatan dan Matriks Peran Divisi Operation (berstatus USULAN di sana). "Pemilik aset" bukan jabatan; maknanya mengikuti kolom Pemilik SNX-ISMS-REG-01. "ISO/ISMS Coordinator" di blok pengesahan sumber diganti data defaults. Badan dokumen tidak menyebut COO atau Direktur Utama, jadi aturan sebutan "Direktur (COO)" tidak terpakai. Vault tidak disebut, jadi status "menunggu konfirmasi Ops" tidak terpakai.
14. Tabel Document Title di halaman identitas tercetak "Operation - SOP Vulnerability & Patch Management" oleh renderer; bukan isian spec.

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | "Dua sumber" berarti dua bukti dari cara pemeriksaan berbeda, contoh hasil scan ulang dan hasil pemeriksaan versi | Bagian 3, definisi Dua sumber | Fani |
| 2 | "Perubahan besar" (pemicu scan tambahan) sama dengan change jenis Major menurut SNX-OPS-SOP-02 | Bagian 3, definisi Perubahan besar | Fani |
| 3 | Tenggat dihitung sejak Lead SOC menetapkan prioritas di tiket temuan, dalam hari kalender | Bagian 3, definisi Tenggat | Fani |
| 4 | Mitigasi kompensasi prioritas Darurat dalam 24 jam (angka sumber, berlabel USULAN oleh tim) | Bagian 8 | Fani |
| 5 | Tenggat Darurat 72 jam (angka sumber, label USULAN oleh tim) | Bagian 8 | Fani |
| 6 | Tenggat Kritis 7 hari (angka sumber, label USULAN oleh tim) | Bagian 8 | Fani |
| 7 | Tenggat Tinggi 30 hari (angka sumber, label USULAN oleh tim) | Bagian 8 | Fani |
| 8 | Tenggat Sedang 90 hari (angka sumber, label USULAN oleh tim) | Bagian 8 | Fani |
| 9 | Tenggat Rendah "siklus patch berikutnya" (sumber, label USULAN oleh tim; panjang siklus tidak ada di sumber) | Bagian 8 | Fani |
| 10 | Lead SOC meninjau ulang pengecualian pada tanggal tinjau ulang yang tercatat | Bagian 6.6 langkah 5 | Fani |
| 11 | Bila skor CVSS belum tersedia, Lead SOC menetapkan prioritas sementara dari paparan aktual, nilai aset, dan mitigasi yang sudah ada | Bagian 9, baris Skor CVSS | Fani |
| 12 | Pemilik laporan scan di Folder SOC adalah Lead SOC | Bagian 11, tabel rekaman | Fani |

Pengesahan tenggat 4 sampai 9 lewat SNX-ISMS-REG-03 (kalimat sumber) tidak terlihat di REG-03; pemutus tetap Fani sebagai pemeriksa dokumen, dengan owner bila angka berdampak ke kontrak pelanggan.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Tenggat Bagian 6 berlabel USULAN dan "disahkan bersama SNX-ISMS-REG-03", tetapi REG-03 tidak memuat tenggat patch (catatan audit: hanya RTP-003 yang menyebut telaah advisory mingguan). Perlu diputuskan tempat pengesahan tenggat dan apakah angka dijadikan final | Fani |
| 2 | Titik awal hitung tenggat dan satuan hari (kalender atau kerja) tidak ada di sumber; definisi Tenggat memakai usulan penyusun (USULAN 3). Di sumber, tenggat tertulis untuk "perbaikan atau mitigasi", tetapi indikator mengukur "ditutup dalam tenggat"; belum jelas apakah verifikasi masuk hitungan tenggat | Fani |
| 3 | Indikator kinerja: Sedang dan Rendah tanpa target; tidak ada periode ukur, sumber data, atau baseline untuk empat indikator; "Endpoint" di indikator didefinisikan server dan laptop kerja, sehingga fleet hosting pelanggan tidak terhitung dalam 100%, padahal 7.5 mengaturnya terpisah | Fani |
| 4 | Mitigasi 24 jam untuk Darurat: sumber hanya mengatur mitigasi bila patch belum tersedia atau tidak bisa dipasang (7.2 butir 4), sedangkan tabel Bagian 6 memberi mitigasi 24 jam untuk Darurat tanpa syarat itu. Belum jelas apakah mitigasi wajib juga saat patch tersedia dan bisa dipasang dalam 72 jam. Intro 6.4 dibiarkan netral | Fani |
| 5 | Pemetaan antarskala belum ada: prioritas patch, severity tiket P1 sampai P4, dan level risiko REG-02. PRO-OPS-001 SOC-04 menulis "CVE kritis yang dapat dieksploitasi dari luar dan menyentuh aset SINUX = tiket P2 minimal"; kalimat itu tidak dibawa karena bahan saja dan berstatus draf. Perlu diputuskan severity apa yang dipakai tiket temuan di Zammad dan FRM-08 | Fani |
| 6 | Kriteria Darurat tanpa CVSS dan tumpang tindih dengan Kritis (CVSS 9.0 atau lebih tanpa eksploitasi masuk Kritis); aturan prioritas sementara bila CVSS tidak ada (USULAN 11) belum disahkan; alasan penyesuaian prioritas (butir 4.3) tidak wajib dicatat di sumber | Fani |
| 7 | "Advisory kritis" (telaah segera) tidak didefinisikan; belum jelas apakah sama dengan prioritas Darurat dan Kritis | Fani |
| 8 | Alur sesudah mitigasi tidak ditulis sumber (gambar sumber tanpa garis lanjutan). Diagram baru mengarahkan mitigasi ke verifikasi dan pengecualian ke ujung cabang; konfirmasi bahwa itu maksud tim | Fani |
| 9 | Pelaku yang tidak disebut sumber (asumsi 1 sampai 8): pembuat tiket, penguji patch, penerus tiket ke NOC, pemeriksa versi, pencatat pengecualian, peninjau ulang pengecualian, pemeriksa anti-malware, pelaku mitigasi, dan PIC indikator. Tidak ada batas waktu untuk pengecualian, serah terima ke NOC, dan verifikasi penutupan | Fani |
| 10 | Pelaku telaah advisory berbeda antardokumen: SOP-05 dan POL-OPS-001 bagian 9.3 menunjuk Lead SOC; PRO-OPS-001 SOC-04 menunjuk SOC Analyst dengan Lead SOC akuntabel dan dasar kebijakan "POL §7" yang topiknya change management; REG-03 RTP-003 berpemilik Lead NOC dan merujuk SOP-05 (open item 6 di notes/ISMS-REG-03.md). Dokumen ini mengikuti sumber SOP-05 | Fani |
| 11 | Mitigasi yang mengubah production (rule WAF, nonaktifkan layanan, batasi akses) lewat SNX-OPS-SOP-02: sumber SOP-05 menyebut change request hanya untuk pemasangan patch. Dasar tambahan: POL-OPS-001 bagian 7 (go-gate untuk semua perubahan production). Konfirmasi bahwa kalimat intro 6.4 benar | Fani |
| 12 | Kesenjangan dokumen terkait: FRM-08 tidak punya kelas triage vulnerability atau patch dan severity-nya P1 sampai P4 (catatan audit); pemilik FRM-08 Lead NOC padahal tiket temuan ditangani SOC; SNX-OPS-SOP-02 mendefinisikan Emergency untuk memulihkan layanan atau menahan insiden tanpa menyebut patch Darurat; SNX-OPS-SOP-03 menulis "patch kritis" segera tanpa menunggu jadwal bulanan (nama skala berbeda dari prioritas patch) dan meminta Lead SOC menyuplai "daftar patch keamanan" sedangkan SOP-05 menyerahkan tiket temuan. Change Normal diajukan minimal 3 hari kerja sebelum window (SOP-03) dan notifikasi pelanggan H-2 (POL-OPS-001 bagian 7); itu menekan tenggat Kritis 7 hari. Lane dokumen itu perlu menyelaraskan | LEAD, Fani |
| 13 | "Dua sumber" (USULAN 1): sumber menulis verifikasi dengan "scan ulang atau pemeriksaan versi" lalu "klaim tertutup didukung dua sumber". Perlu dipastikan apa dua sumber itu | Fani |
| 14 | Lingkup: (a) hypervisor dan platform Nusagrid dieskalasi ke pihak upstream menurut POL-OPS-001 bagian 6 (matriks eskalasi), WAF dan jaringan ke Tech dan Product, sedangkan SOP-05 menugaskan NOC Engineer memasang patch; siapa yang memasang patch sistem itu belum jelas; (b) SOC POLRI di luar ruang lingkup Divisi Operation menurut POL-OPS-001 bagian 2, dan SOP-05 tidak menyebut POLRI (ImunifyAV disebut sebagai contoh); (c) "aset kita" di 7.2 butir 5, apakah sweep IOC berlaku untuk aset pelanggan; (d) pengecualian lingkup "penanganan insiden" di bagian 2 diturunkan penyusun | Fani |
| 15 | Sistem tiket: sumber tanpa nama sistem; dokumen memakai Zammad (premis owner "zammad untuk ops, glpi untuk generalist"). POL-OPS-001 P-08 menulis semua tiket di GLPI dan bagian 13 butir 6 menunda GLPI sebagai sistem resmi. Batas "generalist" belum dirinci owner | owner |
| 16 | Pengecualian: tempat mencatat pengecualian prioritas Tinggi, Sedang, dan Rendah (sumber hanya menyebut REG-03 untuk Darurat dan Kritis); siapa mengisi kolom "Diterima oleh" REG-03 untuk pengecualian itu (REG-03 mensyaratkan penerimaan tertulis pemilik risiko); apakah pengecualian yang melewati tanggal tinjau ulang dieskalasi | Fani |
| 17 | Masa simpan: header sumber "Berlaku sampai digantikan" bertabrakan dengan tabel record 3 tahun; template tidak punya slot masa simpan. Tabel bagian 11 dipakai. Lokasi rekaman hasil uji patch, pemeriksaan versi, dan status anti-malware per endpoint tidak ada di sumber (ditulis di tiket temuan, kecuali status anti-malware yang tidak punya register) | Fani |
| 18 | Peran: "ISMS Coordinator" belum ditetapkan di HR-ORG-01 (K-13) padahal dicantumkan sebagai pemilik REG-03; "Pemilik aset" bukan jabatan di HR-ORG-01 dan harus diisi dari kolom Pemilik REG-01 (yang masih memuat nama fungsi seperti "Tech dan Product" menurut notes sibling). Blok pengesahan: penyetuju sumber COO, defaults mengunci Samuel Kristanto Utomo / President Director (pembalik: owner) | owner |

## 6. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI, dan perbaikannya:
- Sepuluh butir kebijakan 4.1 sampai 4.10 berbentuk sama (label, klausul, pelaku, rujukan butir) dan berakhir dengan "(butir 6.x)". Bentuk ini dipertahankan karena auditor mencari pemetaan klausul ke butir, dan polanya sama dengan SNX-OPS-SOP-05 dan SNX-ISMS-SOP-01. Kalimat di dalam tiap butir dibuat berbeda panjang dan susunan; butir 4.2 sengaja berupa daftar kriteria, butir 4.3 pendek.
- Bagian 6.4 dan 6.6 awalnya sama-sama dibuka dengan "Prosedur ini dipakai bila ..." (draf pertama). Diganti: "Mitigasi kompensasi dipakai bila ..." dan "Pengecualian hanya untuk patch yang ...".
- Frasa "sesuai jadwal di bagian 8" muncul empat kali dan "di tiket temuan" lebih dari lima belas kali di kolom Output. Dibiarkan: yang pertama mencegah angka waktu disalin ke dua bagian, yang kedua karena semua rekaman memang hidup di tiket temuan, dan satu istilah dipakai untuk satu hal.
- Definisi di bagian 3 (CVE, CVSS, RCE, WAF, EDR, BSSN, CSIRT sektor) bisa ditempel ke perusahaan mana pun. Dibiarkan pendek karena fungsinya memberi arti istilah untuk pembaca audit; definisi yang membawa konteks SINUX (Tiket temuan, Pemilik aset, Prioritas patch, Tenggat, Window maintenance) dibuat spesifik.
- Nama peran diulang penuh (Lead SOC, SOC Analyst, NOC Engineer) tanpa kata ganti atau "tim", dan langkah prosedur berpola perintah. Dibiarkan: aturan satu istilah untuk satu hal dan satu tindakan satu pelaku.
- Kalimat tim dipertahankan di Purpose utuh, di definisi pengecualian patch aplikasi pelanggan, daftar stack, kriteria prioritas, alasan sweep IOC ("patch tidak menghapus kompromi yang sudah terjadi"), dan langkah malware. Tidak ada pembuka generik, penutup positif, ekor penegas, rentang palsu, atau tebal, huruf kapital, dan tanda kutip untuk penekanan. Daftar dari sumber (empat sumber, tiga bentuk mitigasi, empat unsur pengecualian) dipertahankan jumlahnya, bukan kelompok tiga yang dipaksakan. Kesimpulan dua kalimat tanpa pujian.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: 72 jam, 24 jam, 7, 30, 90 hari, CVSS 9.0, 7.0, 8.9, 4.0, 6.9, bulanan, mingguan, 95%, 90%, 100%, 3 tahun dari sumber SOP-05 Bagian 5, 6, 7, 8, 9. Tidak ada angka lain di dokumen. Label (USULAN) ada pada enam angka tenggat karena tim sendiri melabelinya. "0 sampai 10" pada definisi CVSS adalah skala standar CVSS, bukan dari sumber. "Hari kalender" dan titik awal tenggat berlabel (USULAN 3).
- Nama: tidak ada nama orang di badan dokumen; nama di blok Approval dari config/defaults.json. Nama sistem (Zammad, WHM, cPanel, CloudLinux, Zimbra, nginx, PHP, Acronis, ImunifyAV, CISA KEV, BSSN) dari sumber atau defaults. Kepanjangan BSSN, CISA, CSIRT, CVE, CVSS, RCE, EDR, IOC dari pengetahuan umum, bukan dari sumber. Judul dokumen terkait dari checklist dan spec sibling. Pemilik rekaman FRM-04, FRM-07, FRM-08, REG-03 dari notes sibling (bukan dibuka ulang di Drive); Zammad dari premis owner, bukan dari sumber SOP-05.
- Tanggal: tidak ada tanggal di dokumen; Effective Date dan tanda tangan kosong.
- Tanpa sumber tertulis dan tidak berlabel (USULAN) di dokumen, tetapi tercatat di sini sebagai tafsir: penugasan pelaku (asumsi 1 sampai 8), serah terima Lead SOC ke Lead NOC (asumsi 2), mitigasi yang mengubah production lewat SNX-OPS-SOP-02 (asumsi 5), pencatatan pengecualian prioritas bukan Darurat dan Kritis hanya di tiket (asumsi 6), pemetaan klausul 8.19 (asumsi 10), pengecualian lingkup penanganan insiden (asumsi 11), kewenangan Lead NOC menyetujui change Standar dan Normal NOC (dari spec SNX-OPS-SOP-02, bukan sumber SOP-05). Semuanya ada di open items 9, 11, 14, 16, dan 18, bukan diklaim sebagai fakta sumber.
- Hal yang tidak saya ukur: isi SNX-OPS-SOP-02, SOP-03, SNX-ISMS-SOP-01, FRM-04, FRM-07, FRM-08, REG-01, REG-03, dan HR-ORG-01 dibaca dari spec dan notes sibling di repo, bukan dari berkas Drive terbaru; kutipannya bisa basi bila tim sudah mengubah dokumen itu.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil

### W10 kalimat dihapus atau dipindah
- Scope: "(penyampaian temuan dan rekomendasinya ada di bagian 9)" diganti fakta dari bagian 9 dalam kalimat terpisah.
- Definisi Tenggat: "nilainya ada di bagian 8" menjadi rujukan "(bagian 8)".
- Butir 4.2: "Tenggat tiap prioritas ada di bagian 8" menjadi "Tenggat tiap prioritas (bagian 8)".
- Intro 6.1: "Sumber yang ditelaah tercantum di butir 4.1." ditulis ulang "Lead SOC menelaah empat jenis sumber informasi vulnerability sesuai butir 4.1."
- Langkah 6.1 dan 6.2: "sesuai jadwal di bagian 8" diganti jadwal dari bagian 8.

### W10 selisih angka
- 9: nomor bagian di kalimat penunjuk "(penyampaian temuan dan rekomendasinya ada di bagian 9)" di Scope, diganti faktanya. Bukan angka substansi.

### W10 audit pointer
- .scope[2]: lengkap; bagian 9 baris Aplikasi milik pelanggan: Service Delivery Manager menyampaikan temuan dan rekomendasi ke developer atau PIC pelanggan; pelaku dan pihak penerima tetap; tanpa (USULAN).
- .procedures[0].steps[0][0]: lengkap; bagian 8 = minimal mingguan, advisory kritis segera (tanpa (USULAN)); rujukan butir 4.1 dipindah ke intro prosedur yang sama ("sesuai butir 4.1"), daftar empat jenis sumber tetap di butir 4.1.
- .procedures[1].steps[0][0]: lengkap; bagian 8 = minimal bulanan, dan setelah perubahan besar (tanpa (USULAN) di baris bagian 8).
- .procedures[1].steps[1][0]: lengkap; bagian 8 = scan eksternal minimal bulanan (tanpa (USULAN)).

### W10 catatan
- Sebutan pihak luar: "pelanggan" (keputusan lintas dokumen ISMS).
- "bila" diganti "jika"; "menurut" diganti "sesuai"; "butuh" menjadi "memerlukan"; beberapa kalimat panjang dipecah.
- Bagian 9 baris "Patch tidak dapat dipasang sesuai tenggat" ditulis dengan satu pelaku (Lead SOC mencatat dan meminta persetujuan), sesuai simpul alur "Catat pengecualian dan minta persetujuan".

### W10 audit cakupan label
- .definitions[22][1]: diperbaiki (definisi dipisah lagi dari kalimat berlabel; label hanya pada cara hitung hari kalender)
