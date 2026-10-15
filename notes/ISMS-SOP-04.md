# Catatan penyusun ISMS-SOP-04: IT Asset & Configuration Management

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-SOP-04.json. Mode sop, aksi T1, wave W2, nomor SNX-ISMS-SOP-04 (nomor lama dipertahankan), department Operation (department_labels ISMS; sumber menulis "Information Security"), classification RESTRICTED (Internal) mengikuti label sumber, audit_class B, process owner "Head of Operation" (jabatan tanpa nama, dari "Pemilik dokumen" di sumber). Catatan worklist: "sumber pendukung POL-OPS-001 dan PRO-OPS-001 (bahan saja)".

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-SOP-04_SOP_IT_Asset_Configuration_Management.docx (159969 byte), sumber utama | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg | 2026-10-13T06:09:01Z (get_file_metadata hari ini, sama dengan data baris) | read_file_content (teks), download_file_content (docx didekode ke /tmp/pen-ISMS-SOP-04/src/; comments.xml dan footnotes.xml kosong, header dan footer hanya judul dan label klasifikasi; gambar word/media/rId25.png dibuka dan cocok dengan diagram mermaid di context/audit) |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata hari ini) | read_file_content. Dipakai untuk definisi Gate G3 dan susunan sub divisi saja |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata hari ini) | read_file_content. Tidak ada kalimatnya yang dipakai di badan dokumen; dibaca untuk checklist G3 (lihat open item 12) |
| Kriteria penerimaan | config/worklist.json baris ISMS-SOP-04 | n/a | Kolom Description berisi nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001:2015 "7.1.3, 8.5.2" dan ISO/IEC 27001:2022 "5.9, 5.11, 7.14, 8.9, 8.19" |
| Pembanding (DATA) | context/audit/iso-sinux-supdocs-isms-2026-10-14.md (bagian SNX-ISMS-SOP-04, SoA, REG-01, SOP-01, SOP-03, PRO-01), context/audit/iso-sinux-supdocs-ops-2026-10-14.md (POL, PRO), specs/HR-ORG-01.json, specs/OPS-SOP-02.json, notes/ISMS-REG-01.md, notes/ISMS-SOP-02.md | salinan audit 13 sampai 14 Okt 2026 | Dibaca lewat repo, bukan dari Drive. Kutipan dari REG-01, SoA, SOP-01 di bawah berasal dari salinan audit dan bisa basi bila tim sudah mengubah berkasnya |

Kalimat perintah dalam sumber yang ditujukan ke penyusun: nihil. Imperatif di sumber adalah langkah prosedur biasa.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Aset baru didaftarkan paling lambat saat mulai dipakai, aset pelanggan sebelum gate G3 | "Aset baru didaftarkan di SNX-ISMS-REG-01 paling lambat saat aset mulai dipakai, dan wajib sebelum gate G3 untuk aset pelanggan." (Bagian 6.1) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |
| 2 | Media dipakai ulang di-wipe, yang tidak dipakai ulang dihancurkan fisik | "Media penyimpanan yang akan dipakai ulang di-wipe dengan metode overwrite atau secure erase; yang tidak dipakai ulang dihancurkan fisik." (Bagian 6.5) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |
| 3 | Drift diperiksa minimal triwulanan dan dianalisis bila tanpa change | "Drift diperiksa minimal triwulanan dengan membandingkan konfigurasi aktual ke baseline; drift tanpa change dianalisis sebagai event keamanan atau ketidaksesuaian." (Bagian 7 butir 5) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |

## 2. Fakta pendukung dan kutipan

Semua dari fileId 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg kecuali disebut lain.

| # | Fakta di dokumen | Kutipan verbatim | Letak di dokumen |
|---|---|---|---|
| 1 | Tujuan, kalimat tim dipertahankan utuh | "SOP ini memastikan seluruh aset TI dan konfigurasi yang dikelola SINUX teridentifikasi, memiliki pemilik, terklasifikasi, dikendalikan perubahannya, dan dikembalikan atau dimusnahkan secara aman di akhir siklus hidupnya." | Bagian 1 |
| 2 | Scope dan lima kategori aset | "Berlaku untuk aset informasi dan aset TI internal SINUX dan aset pelanggan yang dikelola SINUX sesuai kontrak:" lalu Hardware, Aset virtual, Software dan lisensi, Informasi, Layanan pihak ketiga | Bagian 2 |
| 3 | Data minimal registrasi | "Data minimal: ID aset, nama, jenis, pemilik, pengguna atau pelanggan, lokasi atau platform, klasifikasi (SNX-ISMS-PRO-01), nilai CIA, status, dan tanggal review." | 6.1, prosedur 6.1 langkah 4 |
| 4 | Penamaan | "Penamaan aset konsisten dan unik; IP address dan detail teknis sensitif disimpan di register yang berklasifikasi RESTRICTED." | 6.1, kebijakan butir 1 dan 2, prosedur 6.1 langkah 2 |
| 5 | Penggunaan dapat diterima | "Aset perusahaan dipakai untuk kepentingan kerja." dan "Laptop kerja wajib screen lock otomatis, disk encryption, antivirus atau EDR aktif, dan update OS (A 8.1)." dan "Kredensial tidak disimpan di laptop di luar password manager." | 6.2, kebijakan bagian 4 |
| 6 | Instalasi software | "Instalasi software pada sistem operasional hanya melalui change request dan dari sumber resmi (A 8.19)." | 6.2 butir 3, kebijakan dan prosedur 6.7 langkah 1 |
| 7 | Aset di luar kantor | "Laptop dan media yang dibawa ke luar kantor tetap dalam pengawasan pemakai dan tidak ditinggal di kendaraan." | 6.3 butir 1 |
| 8 | Kehilangan 1 jam | "Kehilangan atau pencurian dilaporkan paling lambat 1 jam sesuai SNX-ISMS-SOP-01; akses akun terkait segera dicabut atau dirotasi." | 6.3 butir 2, prosedur 6.2 |
| 9 | Pengembalian aset | "Saat pemberhentian atau mutasi, seluruh aset perusahaan dan aset pelanggan yang dipegang dikembalikan dan dicocokkan dengan register." | 6.4 butir 1, prosedur 6.3 |
| 10 | Perangkat pribadi | "Informasi kerja di perangkat pribadi (bila diizinkan) dihapus dan dikonfirmasi tertulis." | 6.4 butir 2, prosedur 6.3 langkah 3 dan 4 |
| 11 | VM pelanggan | "VM dan volume pelanggan yang dihapus mengikuti kontrak dan konfirmasi tertulis pelanggan dua kali (SNX-OPS-SOP-02)." | 6.5 butir 2, prosedur 6.4 langkah 3 dan 4 |
| 12 | Berita acara | "Pemusnahan dicatat dengan berita acara: ID aset, metode, tanggal, pelaksana, saksi. Status aset di register diubah menjadi Dimusnahkan." | 6.5 butir 3, prosedur 6.4 langkah 5 dan 6 |
| 13 | Review dan rekonsiliasi | "Pemilik aset meninjau asetnya minimal semester; Head of Operation memastikan review terlaksana." dan "Rekonsiliasi register dengan sumber aktual (console Nusagrid, Overseer, Acronis, Cloudflare, daftar lisensi) dilakukan triwulanan; selisih ditindaklanjuti." | 6.6, prosedur 6.5 |
| 14 | CI dan baseline | "Configuration item ditandai di SNX-ISMS-REG-01 (kolom CI) beserta acuan baseline konfigurasinya." dan "Baseline hardening disusun per jenis sistem (misalnya server Linux, panel hosting, network device, WAF) dan disimpan di knowledge base sebagai runbook." | Bagian 7 butir 1 dan 2, prosedur 6.6 |
| 15 | Change dan backup konfigurasi | "Setiap perubahan konfigurasi CI melalui SNX-OPS-SOP-02; konfigurasi sebelum dan sesudah dicatat di change request." dan "Backup konfigurasi CI diambil setiap perubahan dan mingguan sesuai SNX-ISMS-SOP-03." | Bagian 7 butir 3 dan 4, prosedur 6.7 langkah 1 sampai 3 |
| 16 | Generator | "Konfigurasi yang dihasilkan otomatis oleh generator (misalnya vhost WAF) diverifikasi ulang setelah setiap Apply, karena perubahan manual dapat tertimpa." | Bagian 7 butir 6, prosedur 6.7 langkah 4, pengecualian |
| 17 | Peran sumber | "Pemilik SOP; memastikan register lengkap dan ditinjau" (Head of Operation); "Klasifikasi, akses, dan siklus hidup asetnya" (Pemilik aset); "Mendaftarkan dan memperbarui aset dan CI saat provisioning, perubahan, dan dekomisi" (NOC Engineer); "Baseline hardening dan pemeriksaan drift keamanan" (Lead SOC); "Memakai aset sesuai aturan penggunaan yang dapat diterima" (Pengguna aset) | Bagian 5 |
| 18 | Retensi | "Change request konfigurasi | SNX-OPS-FRM-04 | 3 tahun", "Berita acara pemusnahan | Lampiran SNX-ISMS-REG-01 | 5 tahun", "Information Asset Register | SNX-ISMS-REG-01 | Berlaku sampai digantikan" | Bagian 8 |
| 19 | Empat target | "Aset produksi terdaftar sebelum G3 | 100%", "Review register semesteran terlaksana | 100%", "Selisih rekonsiliasi triwulanan ditutup dalam 30 hari | 95%", "Drift konfigurasi tanpa change | Nol" | Bagian 9, dilebur ke bagian 8 spec |
| 20 | Pemilik dan klasifikasi | "Pemilik dokumen | Head of Operation" dan "Klasifikasi | RESTRICTED (Internal)" | Atribut |
| 21 | Gate G3 (POL-OPS-001, fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv) | "G3 Serah terima | SD dan PM | Operation (NOC, SOC) | Head of Operation | Terdaftar di Service Hub, monitoring aktif, backup teruji, as-built, runbook, akses lewat Jumphost" | Bagian 8 tabel gate, definisi Gate G3 |
| 22 | Skala CIA (salinan audit REG-01, bukan sumber utama) | "nilai C, I, A dengan skala 1 (rendah) sampai 3 (tinggi)" (SNX-ISMS-REG-01, Cara pakai B19, dikutip di context/audit bagian 5 SOP-04) | Definisi Nilai CIA |
| 23 | Tiket (config/defaults.json ticketing, kata owner 14 Okt) | "sistem tiket zammad untuk ops, glpi untuk generalist" | Scope, definisi Zammad dan Service Hub |
| 24 | Sub divisi (POL-OPS-001) | "Divisi Operation berada di bawah COO dan terdiri dari tiga sub divisi: NOC, SOC, serta Service Delivery dan PM." | Definisi NOC, SOC, SD dan PM (kalimat definisi sama dengan ISMS-SOP-02) |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 7.1.3 Infrastruktur | Ya | Butir CI dan baseline | 6.6 |
| ISO 9001:2015 8.5.2 Identifikasi dan ketertelusuran | Ya | Butir inventaris dan identifikasi (ID aset dan nama unik) | 6.1 |
| 27001 5.9 Inventory of information and other associated assets | Ya | Butir inventaris; butir isi register dijaga akurat | 6.1, 6.5 |
| 27001 5.11 Return of assets | Ya | Butir pengembalian aset | 6.3 |
| 27001 7.14 Secure disposal or re-use of equipment | Ya | Butir wipe dan penghancuran | 6.4 |
| 27001 8.9 Configuration management | Ya | Butir CI, change request, drift | 6.6, 6.7 |
| 27001 8.19 Installation of software on operational systems | Ya | Butir instalasi software | 6.7 langkah 1 |
| 5.10, 7.9, 8.1, 8.10 (tambahan, ada di isi sumber) | Ya, sebagai tambahan | Butir penggunaan, laptop, luar kantor, wipe | 6.2, 6.4 |

Nama kontrol berbahasa Inggris dan nama klausul ISO 9001 berasal dari standar, bukan dari sumber tim.

## 4. Keputusan data

- Approval: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director, persis dari baris dan config/defaults.json. Sumber menulis "Disusun oleh Head of Operation", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber.
- Badan dokumen tidak menyebut COO maupun Samuel, jadi aturan "Direktur (COO)" dan "Direktur Utama" tidak terpakai.
- Tiket: Zammad untuk Ops dan Service Hub (GLPI) untuk generalist hanya muncul di scope, pada kategori "tiket" dari sumber. SOP ini tidak punya langkah yang membuat tiket, jadi tidak ada batas Ops lawan generalist yang perlu ditulis.
- Vault: definisi Password manager memakai rumusan yang sama dengan ISMS-SOP-02, status "menunggu konfirmasi Ops". Tidak ada klaim vault sudah aktif.
- PPN: tidak relevan untuk dokumen ini.
- Klasifikasi: label sumber RESTRICTED (Internal) dipakai; renderer menaruhnya di footer.
- Review period YEARLY, effective date kosong, status Draft, revision 00, revision_desc dari data baris.

## 5. Pemetaan peran (HR-ORG-01)

| Peran di bagian 5 | Padanan di specs/HR-ORG-01.json | Catatan |
|---|---|---|
| Head of Operation | Jabatan Divisi Operation "Head of Operation" (USULAN di POL, belum ada pemegang, K-10 dan K-11) | Nama sama persis |
| NOC Engineer | Jabatan "NOC Engineer" | Nama sama persis |
| Lead SOC | Jabatan "Lead SOC" | Nama sama persis |
| Pemilik aset | Tidak ada di daftar jabatan dan matriks peran | Peran generik dari sumber, dipegang pemilik yang tertulis di kolom Pemilik SNX-ISMS-REG-01. Tidak dipetakan ke satu jabatan |
| Pengguna aset | Tidak ada di daftar jabatan dan matriks peran | Peran generik dari sumber (semua pemakai aset). Tidak dipetakan ke satu jabatan |
| ISMS Coordinator (sumber: "ISO/ISMS Coordinator" sebagai pemeriksa) | "Belum ditetapkan" (K-13) | Tidak dipakai di badan dokumen karena pemeriksa mengikuti defaults |
| Lead NOC, SOC Analyst, Service Delivery Manager | Ada di HR-ORG-01 | Tidak dipakai: sumber SOP-04 tidak memberi mereka tugas |

## 6. Penanganan cacat context/audit

Bagian SNX-ISMS-SOP-04 (fileId 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg), bagian 5 Catatan kualitas dan celah:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Header ISO memuat 5.9, 5.11, 7.14, 8.9, 8.19, tetapi isi merujuk juga 5.10, 7.9, 8.1, 8.10 | Diperbaiki: bagian 11 memuat lima klausul kriteria dan empat tambahan dengan keterangan. Tiap tambahan punya butir di bagian 4 (5.10, 8.1, 7.9, 8.10). SoA memetakan kesembilan kontrol itu ke SOP-04 (audit SoA baris 5.9, 5.10, 5.11, 7.9, 7.14, 8.1, 8.9, 8.10, 8.19). SoA juga memetakan 7.10 Storage media ke SOP-04, tidak ada di kriteria atau sumber: open item 14 |
| 2 | Rujukan SNX-OPS-SOP-02 untuk change CI dan konfirmasi hapus VM | Dipertahankan. Dicek ke specs/OPS-SOP-02.json: "Minta konfirmasi tertulis pelanggan dua kali sebelum delete VM" ada di sana, dan change request dicatat di SNX-OPS-FRM-04 |
| 3 | Batas pelaporan 1 jam dan rujukan SNX-ISMS-SOP-01 | Dipertahankan. Titik awal "sejak mengetahuinya" diambil dari SOP-01 ("paling lambat 1 jam sejak mengetahui", dikutip di audit); sumber SOP-04 tidak menyebut titik awal |
| 4 | Tidak ada batas waktu pengembalian aset; SNX-ISMS-SOP-02 mencabut akses paling lambat hari terakhir kerja | Diisi sebagai USULAN U1 (hari terakhir kerja), selaras dengan SOP-02. Angka bukan dari sumber tim |
| 5 | SNX-ISMS-PRO-01 dan SNX-ISMS-SOP-03 merujuk SOP-04 untuk pemusnahan media | Tidak ada perubahan: langkah wipe dan hancur fisik dipertahankan dan konsisten dengan rujukan itu |
| 6 | Berita acara 5 tahun sebagai "Lampiran SNX-ISMS-REG-01", sementara REG-01 B14 hanya "Berlaku sampai digantikan" | Diperbaiki di dokumen ini: tabel rekaman menyebut sheet Pemusnahan dan 5 tahun. specs/ISMS-REG-01.patch.json sudah menulis B14 "Berita acara di sheet Pemusnahan: 5 tahun (SNX-ISMS-SOP-04)". Template tidak punya kolom masa simpan di header, jadi hanya tabel bagian 11 yang berlaku |
| 7 | Skala nilai CIA tidak didefinisikan | Diperbaiki: definisi Nilai CIA memakai skala 1 sampai 3 dari REG-01 (fakta 22) |
| 8 | Pengesahan kosong dan riwayat revisi dua baris bertanggal sama | Teratasi oleh template: satu baris Rev 00, effective date kosong, signature kosong |
| 9 | (temuan penyusun, tidak ada di audit) Diagram: "Lanjut operasi" buntu tanpa garis kembali | Diperbaiki: garis putus-putus "siklus berikutnya" kembali ke Tinjau aset |
| 10 | (temuan penyusun) Diagram: label "register 6 bulan, sumber 3 bulan" tidak cocok dengan teks "minimal semester" dan "triwulanan" | Diperbaiki: node memakai "minimal semester" dan "triwulan" |
| 11 | (temuan penyusun) Diagram menulis "Terapkan baseline" tetapi teks hanya "disusun" dan "disimpan di knowledge base"; diagram memberi drift hanya jalur event keamanan, teks juga menyebut ketidaksesuaian | Diperbaiki: node "Susun baseline hardening dan simpan sebagai runbook"; node analisis memuat kedua jalur |
| 12 | (temuan penyusun) Peran "ISO/ISMS Coordinator" di blok pengesahan | Tidak terpakai (defaults) |
| 13 | (pemeriksaan penyusun) Rujukan internal AI | Tidak ada di sumber SOP-04; lint lulus |

Bagian POL-OPS-001 dan PRO-OPS-001 (fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv dan 1U8CAdibwBk9x_-Aic2lbev144d6WReTz), hanya yang relevan:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | POL: status DRAFT v0.1 dan penomoran USULAN; pemilik COO di kontrol dokumen tetapi Head of Operation di bagian 9.1 | Badan dokumen hanya memakai definisi Gate G3 dan susunan sub divisi dari POL. Pemilik gate G3 = Head of Operation tertulis di tabel gate POL bagian 8, jadi tidak terkena konflik pemilik. Open item 13 |
| 2 | POL: rujukan DOCTRINE, DEC, HANDOVER, SKILL_, SINUX_SERVICE_HUB, CORE; PRO: SKILL_, CLAIM_CLASS_POLICY, "packet setor", "jalur staging" | Tidak ada yang disalin. Lint nol temuan |
| 3 | POL: P-08 menulis semua tiket di GLPI, PRC-01 menulis Zammad | Mengikuti defaults (Zammad Ops, GLPI generalist), hanya di scope. Open item 16 |
| 4 | PRO: checklist G3 "Pelanggan, aset, dan kontak terdaftar di Service Hub" | Tidak diubah ke Service Hub karena sumber SOP-04 menyebut SNX-ISMS-REG-01. Open item 12 |
| 5 | POL dan PRO butir lain (RACI, severity, hypercare, KPI, shift, runbook yang belum ada) | Tidak relevan untuk SOP-04, tidak dipakai |

## 7. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Sumber hanya memberi satu peran pelaksana: NOC Engineer "mendaftarkan dan memperbarui aset dan CI saat provisioning, perubahan, dan dekomisi". Pelaku langkah lain yang ditulis pasif di sumber diberi pelaku dari tabel peran: NOC Engineer untuk penamaan, pencocokan aset kembali, rekonsiliasi dan tindak lanjut selisih, pemusnahan, berita acara, status Dimusnahkan, change request, backup konfigurasi, verifikasi setelah Apply, dan pencabutan atau rotasi akses akun saat aset hilang; Pengguna aset untuk pelaporan kehilangan, pengembalian aset, penghapusan dan konfirmasi di perangkat pribadi; Pemilik aset untuk klasifikasi, nilai CIA, keputusan pensiun aset.
2. Pencabutan atau rotasi akses akun saat aset hilang: sumber pasif tanpa pelaku. ISMS-SOP-02 (pilot) memakai peran "Administrator sistem", yang tidak ada di HR-ORG-01, jadi dokumen ini memakai NOC Engineer dan merujuk SNX-ISMS-SOP-02 untuk caranya. Rujukan ke SOP-02 itu tambahan penyusun.
3. Nilai CIA ditetapkan Pemilik aset: sumber memberi Pemilik aset "Klasifikasi", sedangkan nilai CIA hanya ada di daftar data minimal. Tafsir.
4. Keputusan pensiun aset oleh Pemilik aset: dari "siklus hidup asetnya" dan diamond "Aset dipensiunkan?" di diagram sumber, yang berada sesudah node review. Diletakkan di prosedur 6.5.
5. Head of Operation memantau empat target di bagian 8: sumber hanya memberinya "memastikan register lengkap dan ditinjau" dan "memastikan review terlaksana". Pemantauan target adalah tafsir.
6. Output langkah "Tidak ada baris review terlambat (berwarna merah)": dari Cara pakai SNX-ISMS-REG-01 sesudah patch ("baris merah berarti review terlambat", notes/ISMS-REG-01.md). Bukan dari sumber SOP-04.
7. Kolom Authority tabel peran tidak ada di sumber; diturunkan dari kalimat tanggung jawab sumber (kolom paling tipis: Head of Operation dan Pengguna aset).
8. Lokasi record SNX-ISMS-REG-01 dan sheet Pemusnahan "Google Drive" dan pemilik Head of Operation: REG-01 adalah berkas Drive (worklist) dan "Pemilik dokumen" REG-01 = Head of Operation (notes/ISMS-REG-01.md). Sumber SOP-04 hanya memberi nomor. Lokasi SNX-OPS-FRM-04 "Berkas SNX-OPS-FRM-04" dan pemilik Head of Operation mengikuti specs/OPS-SOP-02.json.
9. Definisi umum (Apply, Baseline hardening, Change request, Nilai CIA, Rekonsiliasi, Wipe) adalah penjelasan penyusun, bukan kalimat tim. Definisi Password manager, Service Hub, Zammad, NOC SOC SD dan PM disamakan dengan ISMS-SOP-02.
10. Pengecualian scope "aset pelanggan yang tidak dikelola SINUX menurut kontrak": diturunkan dari kalimat scope sumber sendiri ("yang dikelola SINUX sesuai kontrak"), bukan fakta baru.
11. Empat target kinerja (bagian 9 sumber) dilebur ke kolom SLA / Timing karena template tidak punya slot KPI (sama dengan ISMS-SOP-02).
12. "Mutasi": sumber menulis seluruh aset dikembalikan saat mutasi, ditulis apa adanya.
13. Judul dokumen terkait (SOP Information Security Incident Management, SOP User Access Control & Authorization, SOP Backup & Recovery, Information Classification & Handling Procedure, Statement of Applicability (SoA), Project Change Management, Change Request & Approval Log) diambil dari salinan audit dan specs lain di repo, bukan dari Drive.

## USULAN

Jumlah USULAN berlabel di dokumen: 3 (sama dengan hitungan lint "3 butir (USULAN)"). Baris rekaman berlabel berlaku untuk seluruh barisnya (nama, lokasi, pemilik, retensi).

| # | Butir | Letak di dokumen | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Pengembalian aset saat pemberhentian atau mutasi paling lambat hari terakhir kerja | Bagian 8 (SLA) | Menutup cacat "tidak ada batas waktu pengembalian aset"; disamakan dengan pencabutan akses di SNX-ISMS-SOP-02. Angka bukan dari sumber tim | Fani dan Aziz (HR) |
| U2 | Rekaman "Catatan rekonsiliasi SNX-ISMS-REG-01": Google Drive, pemilik Head of Operation, 3 tahun | Bagian 11 (rekaman) | Sumber memberi frekuensi dan target rekonsiliasi tetapi tidak memberi rekamannya; 3 tahun disamakan dengan SNX-OPS-FRM-04 | Fani |
| U3 | Rekaman "Catatan pemeriksaan drift": Google Drive, pemilik Lead SOC, 3 tahun | Bagian 11 (rekaman) | Sumber memberi frekuensi pemeriksaan drift tetapi tidak memberi rekamannya; 3 tahun disamakan dengan SNX-OPS-FRM-04 | Fani |

## Open items

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber COO (Amirull), template dan defaults Samuel. Defaults dipakai | Owner atau Samuel |
| 2 | Head of Operation belum punya pemegang bernama di HR-ORG-01 (K-10, K-11); pemilik SOP dan pemilik record tetap "Head of Operation" | Owner, Fani |
| 3 | Pemilik aset dan Pengguna aset adalah peran generik, bukan jabatan di HR-ORG-01. Pemilik tiap aset ditentukan kolom Pemilik SNX-ISMS-REG-01 | Fani |
| 4 | Pelaksana langkah yang ditulis pasif di sumber (asumsi 1 sampai 5) adalah tafsir: NOC Engineer untuk rekonsiliasi, pemusnahan, change request, backup konfigurasi; Pemilik aset untuk nilai CIA dan keputusan pensiun; Head of Operation memantau target. Perlu konfirmasi | Fani |
| 5 | Pencabutan atau rotasi akses saat aset hilang: sumber tanpa pelaku. SNX-ISMS-SOP-02 memakai "Administrator sistem" yang tidak ada di HR-ORG-01; dua SOP perlu satu nama peran | Fani |
| 6 | Penerima pengembalian aset dan penerima konfirmasi tertulis penghapusan informasi di perangkat pribadi tidak disebut; rekaman konfirmasi itu tidak punya lokasi dan tidak ada di tabel rekaman. HR-ORG-01 mendefinisikan HRGA mengelola inventaris kantor, tetapi sumber tidak menugaskannya | Fani, Aziz |
| 7 | Tidak ada tindakan bila aset tidak dikembalikan atau tidak cocok dengan SNX-ISMS-REG-01; sumber diam, tidak ada kontrol pengganti yang ditulis | Fani, Aziz |
| 8 | Saksi berita acara pemusnahan: sumber hanya menulis "pelaksana, saksi" tanpa peran saksi | Fani |
| 9 | Pola ID aset dan penamaan yang "konsisten dan unik" tidak didefinisikan di sumber maupun di SNX-ISMS-REG-01 | Fani |
| 10 | Baseline hardening: belum jelas runbook per jenis sistem sudah ada. Audit REG-01 mencatat acuan baseline "Belum ada" pada tiga baris contoh yang CI = "Ya"; daftar runbook yang belum ada di POL bagian 13 tidak menyebut baseline. "Knowledge base" sebagai tempat simpan tidak dirinci | Fani (Lead SOC) |
| 11 | Selisih rekonsiliasi yang melewati 30 hari: target 95% berarti 5% boleh lewat, tetapi tidak ada eskalasi atau pelaku; penanganan "ketidaksesuaian" untuk drift tidak punya rujukan prosedur bernomor | Fani |
| 12 | Checklist G3 di PRO-OPS-001 bagian 8.2 menulis "Pelanggan, aset, dan kontak terdaftar di Service Hub", sementara SOP ini mensyaratkan SNX-ISMS-REG-01 sebelum G3. Dua tempat pendaftaran aset pelanggan. Aturan "wajib sebelum G3" memakai istilah aset pelanggan, target 100% memakai istilah aset produksi; ditulis apa adanya | Fani |
| 13 | POL-OPS-001 masih DRAFT v0.1 dengan penomoran USULAN dan pemilik ganda (COO atau Head of Operation); kode POL-OPS-001 di definisi Gate G3 diganti nomor SNX bila sudah terbit | Fani |
| 14 | SoA SNX-ISMS-SOA-01 memetakan 7.10 Storage media ke SOP-04, padahal kriteria baris dan sumber tidak memuat 7.10 (SoA menandainya "Sebagian"). Perlu keputusan menambah 7.10 ke SOP ini atau mengubah SoA | Konsultan SoA, Fani |
| 15 | Status password manager (vault) menunggu konfirmasi Ops, sementara SOP mewajibkan kredensial di laptop hanya disimpan di sana | Fani (Ops) |
| 16 | Batas Zammad (Ops) lawan Service Hub GLPI (generalist) belum dirinci owner; POL-OPS-001 P-08 masih menulis semua tiket di GLPI. Di SOP ini nama kedua sistem hanya ada di scope | Owner |
| 17 | Scope: sumber diam soal pengecualian. POL-OPS-001 bagian 2 mengecualikan app-level pelanggan, keputusan harga dan komersial, serta SOC POLRI untuk Divisi Operation; belum diputus apakah dibawa ke SOP ini | Fani |
| 18 | "Mutasi" mewajibkan pengembalian seluruh aset menurut sumber; mungkin yang dimaksud hanya aset yang tidak relevan lagi | Aziz, Fani |
| 19 | Template tidak punya slot KPI (empat target dilebur ke bagian 8) dan tidak punya kolom masa simpan di header | Aziz (template) |
| 20 | Kutipan REG-01 (skala CIA, baris merah review terlambat, sheet Pemusnahan), SoA, SOP-01, judul dokumen terkait berasal dari salinan audit dan notes lain, bukan dari Drive terbaru | Fani |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan yang saya lakukan:
- Butir kebijakan memakai dua pola berbeda: label ISO di depan ("Inventaris dan identifikasi (Annex A 5.9...):") pada butir pertama, di belakang pada butir lain. Saya seragamkan di belakang kalimat. Label Annex A yang menempel di hampir tiap butir tetap terasa mekanis, tetapi kriteria menuntutnya.
- Penutup "Butir 6.x mengatur ..." berulang di tujuh butir kebijakan dan terdengar seperti templat. Saya ganti dengan rujukan pendek "Lihat butir 6.x".
- Beberapa butir kebijakan pasif padahal pelakunya diketahui (pengembalian aset, penghapusan media, penghapusan VM pelanggan). Saya ubah ke kalimat aktif dengan Pengguna aset atau NOC Engineer. Butir yang kalimat timnya sudah jelas (penggunaan yang dapat diterima, kredensial di laptop, aset di luar kantor) dibiarkan.
- Pengecualian bagian 9 semula menyalin kalimat langkah prosedur. Saya pendekkan menjadi rujukan ke langkah di butir 6.x supaya satu fakta disebut sekali.
- Pada render pertama label "Tidak" di diagram bertabrakan dengan kotak analisis drift; saya pindahkan keterangan itu ke dalam teks diamond.
- Kolom output langkah yang berulang ("... di SNX-ISMS-REG-01") sengaja sama karena menunjuk rekaman yang sama. Kalimat Tujuan dan kalimat tim lain dipertahankan utuh (T1).
- Tidak ada pembuka generik, penutup positif, "tanpa terkecuali", atau em-dash. Tebal, huruf kapital, dan tanda kutip tidak dipakai untuk penekanan. Kesimpulan 2 kalimat.
- Sisa yang saya tahu masih kaku: tabel definisi berisi 17 baris, beberapa terlalu pendek (Wipe, Zammad). Dipertahankan karena istilah dipakai di badan dokumen.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka tanpa sumber hanya tiga item berlabel (USULAN): pengembalian aset paling lambat hari terakhir kerja, retensi 3 tahun catatan rekonsiliasi, retensi 3 tahun catatan pemeriksaan drift (beserta lokasi dan pemilik rekamannya).
- Angka lain dari sumber: 1 jam, 30 hari, 95%, 100%, triwulan, semester, minggu, 3 tahun (SNX-OPS-FRM-04), 5 tahun (berita acara). Skala 1 sampai 3 dari REG-01. "Dua kali" konfirmasi dari sumber dan SNX-OPS-SOP-02.
- Nama orang hanya tiga penanda tangan dari defaults. Tidak ada tanggal; effective date kosong; status Draft.
- Sistem semuanya dari sumber atau defaults: Nusagrid, Overseer, Acronis, Cloudflare, Zammad, Service Hub (GLPI), Google Drive, knowledge base, password manager. Tidak ada hostname atau alamat.
- Yang bukan dari sumber tim dan sudah dicatat di bagian 7: pelaku langkah (asumsi 1 sampai 5), "sejak mengetahuinya" (dari SNX-ISMS-SOP-01), rujukan SNX-ISMS-SOP-02 untuk pencabutan akses, output "baris review terlambat berwarna merah" (dari REG-01), definisi istilah, nama kontrol Annex A dalam bahasa Inggris, lokasi Google Drive untuk rekaman.
- Yang saya ubah sesudah pemeriksaan: lihat jawaban pertanyaan 1, ditambah penggantian "sheet Pemusnahan" sebagai lokasi berita acara setelah dicek ke audit REG-01, dan penambahan SoA di dokumen terkait karena iso_refs menyebutnya.

## Hasil uji sendiri

- python3 -m json.tool specs/ISMS-SOP-04.json: valid.
- python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-SOP-04.json /tmp/pen-ISMS-SOP-04/ISMS-SOP-04.docx: sukses, 16 halaman (LibreOffice), diagram TB 13 simpul dan 3 lane; diagram dibuka dan terbaca, tidak ada label bertabrakan.
- python3 -I tools/lint_doc.py /tmp/pen-ISMS-SOP-04/ISMS-SOP-04.docx sop: "pass": true, fails kosong, warns hanya "3 butir (USULAN) menunggu ACC" (warns PIC SLA nol).
- Validasi OOXML (/mnt/skills/public/docx/scripts/office/validate.py): All validations PASSED. Validator dijalankan tanpa -I karena skrip memuat modul pendampingnya dari foldernya sendiri; berkas docx hanya diberikan sebagai argumen.
- Langkah prosedur: 30 langkah, terpanjang 24 kata (batas 25). Semua PIC langkah dan SLA ada di tabel peran bagian 5. Semua kode dokumen di badan tercantum di tabel dokumen terkait bagian 11. Nol em-dash dan en-dash.
- Berkas uji: /tmp/pen-ISMS-SOP-04/ISMS-SOP-04.docx (bukan hasil final; render final oleh orkestrator ke out/08_ISMS).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil

### W10 kalimat dihapus atau dipindah
Kalimat penunjuk di bagian 4 dihapus (isi butir rujukan tetap di bagian 6): "Lihat butir 6.1.", "Lihat butir 6.6.", "Lihat butir 6.7.", "Lihat butir 6.2.", "Lihat butir 6.3.", "Lihat butir 6.4.", "Lihat butir 6.5."

### W10 selisih angka
- 6.1, 6.2, 6.5, 6.6: nomor butir di kalimat penunjuk "Lihat butir 6.x." di bagian 4 yang dihapus; butir 6.3, 6.4, 6.7 masih dirujuk di tempat lain dalam dokumen. Bukan angka substansi.

### W10 audit pointer
- .policy[0]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.1 tanpa (USULAN)).
- .policy[2]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.6 tanpa (USULAN)).
- .policy[4]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.7 tanpa (USULAN)); kalimat dipecah dua.
- .policy[9]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.2 tanpa (USULAN)).
- .policy[10]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.3 tanpa (USULAN)).
- .policy[11]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.4 tanpa (USULAN)).
- .policy[13]: pointer murni dibuang, isi tidak dinyatakan ulang (butir 6.5 tanpa (USULAN)).
- .exceptions[0][1]: lengkap; langkah 2 butir 6.4 = NOC Engineer menghancurkan fisik media yang tidak dipakai ulang; "tanpa wipe" tetap; tanpa (USULAN).
- .exceptions[1][1]: lengkap; langkah 3 butir 6.4 = NOC Engineer meminta konfirmasi tertulis pelanggan dua kali sebelum menghapus, sesuai SNX-OPS-SOP-02; langkah 4 = hapus VM atau volume sesuai kontrak setelah dua konfirmasi diterima; urutan tetap; pengecualian wipe dan penghancuran fisik tetap; tanpa (USULAN).

### W10 catatan
- Sebutan pihak luar: "pelanggan" (keputusan lintas dokumen ISMS).
- "bila" diganti "jika"; beberapa "menurut" diganti "sesuai".
