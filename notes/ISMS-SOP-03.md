# Catatan penyusun ISMS-SOP-03: Backup & Recovery

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-SOP-03.json. Mode sop, aksi T1, wave W2, nomor SNX-ISMS-SOP-03 (nomor lama dipertahankan), department Operation (label ISMS di defaults), classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Process owner = "Lead NOC" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). Judul spec "Backup & Recovery" karena renderer menulis "Operation - SOP <judul>" di Identity Document.

Uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-SOP-03.json /tmp/pen-ISMS-SOP-03/ISMS-SOP-03.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-ISMS-SOP-03/ISMS-SOP-03.docx sop` memberi `"pass": true`, `"fails": []`, `"warns": ["25 butir (USULAN) menunggu ACC"]` (tidak ada warn PIC SLA). Lulus pada putaran pertama dan diulang sesudah tiap suntingan, termasuk putaran perbaikan 1 (lihat bagian "Putaran perbaikan 1"); semuanya lulus. Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`, tanpa -I karena skrip itu mengimpor modul sebelahnya) menjawab "All validations PASSED!". Keluaran lint: /tmp/pen-ISMS-SOP-03/lint.out.txt. PDF 16 halaman dilihat lewat montase: tata letak mengikuti template, diagram satu halaman sendiri, tidak ada tabel terpotong.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-SOP-03_SOP_Backup_Recovery.docx (142164 byte) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc | 2026-10-13T06:09:01Z (get_file_metadata, dicek hari ini, sama dengan prompt) | read_file_content (teks); download_file_content (docx didekode ke /tmp/pen-ISMS-SOP-03/src.docx; comments.xml dan footnotes.xml kosong; gambar word/media/rId28.png dibuka) |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan pendukung | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan pendukung | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content |
| Kriteria penerimaan | config/worklist.json (key ISMS-SOP-03) | Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "7.1.3, 8.5.3" dan ISO/IEC 27001:2022 "8.13, 8.14" (dari prompt orkestrator) |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md baris 2637 sampai 2845 (bagian SOP-03; bagian 5 di baris 2833 sampai 2842); context/audit/iso-sinux-supdocs-ops-2026-10-14.md bagian POL-OPS-001 (bagian 5 di baris 317) dan PRO-OPS-001 (bagian 5 di baris 720) | salinan audit 13 sampai 14 Okt | DATA, dibandingkan dengan teks sumber di atas |
| Pembanding peran dan rujukan | specs/HR-ORG-01.json (DONE); specs/ISMS-SOP-02.json, OPS-SOP-02.json, OPS-SOP-04.json; notes/ISMS-FRM-01.md, OPS-FRM-07.md, OPS-FRM-08.md; salinan audit PLN-01, FRM-01, SOP-04 | draf lane lain dan salinan audit | DATA; dipakai memeriksa nama peran, nama sheet, dan rujukan silang. Isinya bisa basi bila tim sudah mengubahnya |

Kalimat perintah di sumber: tidak ada yang ditujukan ke penyusun atau agent. Kalimat imperatif di PRO-OPS-001 dan POL-OPS-001 adalah langkah prosedur dan butir keputusan, bukan instruksi untuk run ini. Tidak ada open item dari kategori ini.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Restore ke lokasi produksi butuh dua persetujuan, dan restore ke lokasi uji didahulukan bila memungkinkan | "Restore ke lokasi produksi butuh approval Lead NOC dan persetujuan tertulis pelanggan; restore ke path uji terlebih dahulu bila memungkinkan, untuk menghindari menimpa data terbaru." (Bagian 7.3 butir 2) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |
| Frekuensi uji restore: bulanan untuk pelanggan berlayanan backup, triwulanan untuk sistem internal kritis | "Uji restore minimal bulanan untuk setiap pelanggan berlayanan backup, dan minimal triwulanan untuk sistem internal kritis." (Bagian 7.4 butir 1) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |
| Job gagal 2 kali berturut-turut menjadi tiket P2 | "Job gagal dijalankan ulang secepatnya; gagal 2 kali berturut-turut menjadi tiket P2 sesuai SNX-OPS-SOP-04." (Bagian 7.2 butir 2) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |

## 2. Fakta pendukung dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan, kalimat tim utuh | "SOP ini memastikan informasi, software, dan konfigurasi sistem dicadangkan sesuai kebutuhan bisnis dan kontrak, dilindungi dari kerusakan dan akses tidak sah, serta terbukti dapat dipulihkan melalui uji restore berkala." (Bagian 1) | Bagian 1 |
| 2 | Cakupan layanan pelanggan | "Layanan backup pelanggan (Acronis Cyber Protect, backup VM Nusagrid, backup server dikelola) sesuai kontrak." (Bagian 2) | Bagian 2 |
| 3 | Cakupan sistem internal | "Sistem internal SINUX yang mendukung operasi: ticketing system, Service Hub, knowledge base dan database pendukungnya, password manager, monitoring, konfigurasi network device dan WAF, dokumen di Drive." (Bagian 2) | Bagian 2 |
| 4 | Pengecualian | "Pelanggan tanpa layanan backup tidak dijanjikan pemulihan data; snapshot sebelum perubahan tetap diambil sebagai bagian dari SNX-OPS-SOP-02." (Bagian 2) | Bagian 2 (dikecualikan), bagian 9 baris 1 |
| 5 | Parameter pelanggan | "Layanan backup pelanggan | Sesuai kontrak; standar harian | Sesuai kontrak; standar 30 hari | Sesuai paket | Sesuai kontrak | Sesuai kontrak" (tabel 6.1) | Bagian 4 |
| 6 | Parameter sistem internal kritis | "Sistem internal kritis (ticketing system, password manager, knowledge base dan database-nya) | Harian | 30 hari | Ya | 24 jam | Sesuai SNX-ISMS-PLN-01 Bagian 4 (4 sampai 24 jam)" (tabel 6.1) | Bagian 4 |
| 7 | Parameter konfigurasi dan server kritis | "Konfigurasi network device, WAF, dan server kritis | Setiap perubahan dan mingguan | 90 hari | Ya | 1 minggu | 4 jam" (tabel 6.1) | Bagian 4 |
| 8 | Parameter snapshot | "Snapshot sebelum change | Setiap change yang berisiko | Sampai change dinyatakan stabil, maksimal 14 hari | Tidak wajib | Saat change | Sesuai rollback" (tabel 6.1) | Bagian 4 |
| 9 | Label USULAN dari tim | "Parameter sistem internal adalah USULAN dan ditetapkan bersama SNX-ISMS-PLN-01." (Bagian 6.1) | Bagian 4 (label di dua butir parameter internal) |
| 10 | Aturan 3-2-1, immutable | "Aturan 3-2-1 untuk data kritis: tiga copy, dua media atau platform berbeda, satu di luar lokasi sumber; immutable copy bila platform mendukung." (Bagian 6.2 butir 1) | Definisi dan bagian 4 (arti di bagian 3, aturan di bagian 4) |
| 11 | Enkripsi dan kunci | "Backup di-encrypt saat in transit dan at rest; encryption key disimpan di password manager, terpisah dari backup." (Bagian 6.2 butir 2) | Bagian 4 |
| 12 | Akses console | "Akses ke console dan repository backup dibatasi pada peran operator dengan MFA, sesuai SNX-ISMS-SOP-02." (Bagian 6.2 butir 3) | Bagian 4 |
| 13 | Klasifikasi | "Backup mengikuti klasifikasi data sumbernya (SNX-ISMS-PRO-01)." (Bagian 6.2 butir 4) | Bagian 4 |
| 14 | Properti pelanggan | "Data backup pelanggan adalah properti pelanggan dan hanya dipulihkan atas permintaan atau persetujuan PIC pelanggan yang berwenang." (Bagian 6.2 butir 5) | Bagian 4 (dipetakan ke ISO 9001 8.5.3) |
| 15 | Konfigurasi job | "Setiap job backup baru didokumentasikan: sumber, jadwal, retensi, tujuan, encryption, dan pemilik." dan "Job didaftarkan di SNX-ISMS-FRM-01 (sheet Daftar Job) dan sistemnya di SNX-ISMS-REG-01." (Bagian 7.1 butir 1 dan 2) | 6.1 langkah 3 dan 4 |
| 16 | Perubahan job turun | "Perubahan job yang menurunkan frekuensi atau retensi diperlakukan sebagai change Normal." (Bagian 7.1 butir 3) | Bagian 4 (aturan), 6.1 langkah 6 (tindakan) |
| 17 | Pemantauan | "Shift malam memeriksa status semua job backup dan mencatat hasilnya di SNX-ISMS-FRM-01 (sheet Backup Log)." dan "Kapasitas repository dipantau mingguan; penggunaan di atas 80% ditindaklanjuti." (Bagian 7.2 butir 1 dan 3) | 6.2, bagian 8 |
| 18 | Uji restore, isi uji | "Uji memulihkan sampel data ke lokasi uji, memverifikasi integritas (checksum atau pembukaan file atau start aplikasi), dan mengukur waktu pemulihan terhadap RTO." (Bagian 7.4 butir 2) | 6.4 langkah 1 sampai 3 |
| 19 | Uji gagal | "uji gagal ditangani sebagai tiket P2 dan dianalisis akarnya." dan "Ringkasan uji restore dimasukkan ke laporan bulanan pelanggan dan ke SNX-OPS-RPT-01." (Bagian 7.4 butir 3 dan 4) | 6.4 langkah 5 sampai 9 |
| 20 | Penghapusan | "Backup yang melewati masa retensi dihapus otomatis oleh platform.", "Saat offboarding pelanggan, backup diserahkan atau dihapus sesuai kontrak, dengan berita acara." dan "Media backup fisik yang tidak terpakai dimusnahkan sesuai SNX-ISMS-SOP-04." (Bagian 7.5) | Bagian 4 (otomatis), 6.5 |
| 21 | Peran sumber | "Lead NOC | Pemilik SOP; menetapkan dan meninjau kebijakan backup; menyetujui restore produksi", "Service Delivery Manager | Mencatat parameter backup pelanggan dari kontrak; melaporkan hasil uji restore di laporan bulanan", "Pemilik sistem internal | Menetapkan RPO dan RTO sistemnya", "Lead SOC | Memastikan backup terlindungi dari ransomware dan akses tidak sah" (Bagian 5) | Bagian 5 |
| 22 | Record dan retensi | "Backup Log & Restore Testing Records | SNX-ISMS-FRM-01 | 3 tahun"; "Tiket kegagalan backup dan permintaan restore | SNX-OPS-FRM-08 | 3 tahun"; "Jadwal PM uji restore | SNX-OPS-FRM-07 | 3 tahun" (Bagian 8) | Bagian 11 |
| 23 | Target kinerja | "Job backup sukses | 98%"; "Uji restore bulanan terlaksana per pelanggan backup | 100%"; "Uji restore berhasil pada percobaan pertama | 95%"; "Waktu restore uji dalam RTO | 100%" (Bagian 9) | Bagian 8 (kolom SLA / Timing; template tidak punya slot KPI) |
| 24 | Pemilik dan klasifikasi | "Pemilik dokumen | Lead NOC"; "Klasifikasi | RESTRICTED (Internal)" | meta.process_owner, meta.classification (footer berlabel otomatis) |
| 25 | Acuan klausul | "Acuan ISO 9001:2015 | Klausul 7.1.3, 8.5.3"; "Acuan ISO/IEC 27001:2022 | Klausul atau kontrol Annex A 8.13, 8.14" | Bagian 11 (iso_refs), bagian 4 (label klausul) |
| 26 | Bahan POL-OPS-001: Lead NOC memastikan uji restore bulanan | "memastikan uji restore bulanan berjalan" (Bagian 9.2, Lead NOC) | Bagian 5 (Lead NOC), 6.4 langkah 10, bagian 8 |
| 27 | Bahan POL-OPS-001: Shift 3 = malam | "Shift 3, Malam | 23:00 sampai 07:00 | 22:45 sampai 23:00 | Window maintenance off-office-hour, monitoring backup job, laporan harian" (Bagian 5) | Bagian 3 (definisi Shift malam; jam tidak disalin karena labelnya USULAN di POL-OPS-001) |
| 28 | Bahan PRO-OPS-001: offboarding | "Ekspor data atau backup terakhir sesuai kontrak, serahkan ke pelanggan dengan berita acara." (SDPM-06, Pelaksana: Service Delivery Manager) | Bagian 5 (Service Delivery Manager), 6.5 |
| 29 | Bahan PRO-OPS-001: pelanggan tanpa layanan backup | "Jangan klaim bisa restore untuk pelanggan tanpa layanan backup." (NOC-04) | Mendukung bagian 2 dan bagian 9 baris 1; tidak disalin |

## 3. Pemetaan klausul ISO (kriteria)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 7.1.3 (Infrastruktur) | Ya | Butir "Kapasitas repository backup dipantau sebagai bagian dari infrastruktur layanan (ISO 9001:2015 7.1.3)" | 6.2 langkah 5 dan 6 |
| ISO 9001:2015 8.5.3 (Properti milik pelanggan) | Ya | Butir "Data backup pelanggan adalah properti pelanggan (ISO 9001:2015 8.5.3)" | 6.3, 6.5 |
| ISO/IEC 27001:2022 Annex A 8.13 (Information backup) | Ya | Label "(Annex A 8.13)" pada butir uji restore, empat kelompok parameter, dan aturan 3-2-1 | 6.1 sampai 6.4 |
| ISO/IEC 27001:2022 Annex A 8.14 (Redundancy of information processing facilities) | Ya | Label "(Annex A 8.13, 8.14)" pada aturan 3-2-1 | Tidak ada langkah sendiri; lihat open item 15 |

Nama klausul dalam kurung di bagian 11 berasal dari standar dan dari SoA salinan audit ("8.14 | Redundancy of information processing facilities"), bukan dari kalimat tim. Sumber hanya menulis "7.1.3, 8.5.3 (properti pelanggan)" dan "8.14 (redundancy)".

## 4. Keputusan data

- Approval: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director, persis dari prompt dan config/defaults.json. Sumber menulis "Disusun oleh Lead NOC", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber (D2).
- Badan dokumen tidak menyebut COO maupun Samuel, jadi aturan "Direktur (COO)" dan "Direktur Utama" tidak terpakai.
- Department "Operation" (department_labels ISMS), padahal sumber menulis "Information Security".
- Tiket: Zammad untuk tiket Ops (kegagalan backup, permintaan restore, tiket P2), mengikuti premis owner dan keputusan lane OPS-FRM-07, OPS-FRM-08, ISMS-FRM-01. Service Hub (GLPI) hanya muncul sebagai sistem yang dibackup dan di definisi "Ticketing system". Batas "generalist" belum dirinci owner; lihat open item 4.
- Vault: "Password manager" didefinisikan dengan "Status operasional: menunggu konfirmasi Ops". Tidak ada klaim aktif atau belum live.
- Nama peran bagian 5 memakai HR-ORG-01: Lead NOC, NOC Engineer, Lead SOC, Service Delivery Manager ada di daftar jabatan Divisi Operation (semua USULAN, tanpa pemegang, K-10). Dua peran tidak ada di HR-ORG-01 dan dipetakan begini: "Pemilik sistem" (sumber: "Pemilik sistem internal") = kolom Pemilik SNX-ISMS-REG-01, bukan jabatan baru, sama dengan istilah di ISMS-SOP-02; "PIC pelanggan" = pihak luar, bukan jabatan SINUX. "Pemilik sistem internal" dipendekkan jadi "Pemilik sistem" agar sama dengan SOP-02, dan definisinya membatasi pada sistem internal.
- "Path uji" (7.3) dan "lokasi uji" (7.4) di sumber dilebur menjadi "lokasi uji" saja; "Restore Test dan Request" di 7.3 butir 3 diganti "Restore Record" (lihat bagian 5 butir 9).
- Judul spec "Backup & Recovery" tanpa kata SOP.
- Tanggal draft 13 Oktober 2026 tidak dibawa: template tidak punya field itu, Effective Date kosong, status Draft.

## 5. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah; fileId 1z6y_n2i6...)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Parameter sistem internal berlabel USULAN; kolom RTO hanya merujuk rentang "4 sampai 24 jam"; angka per sistem ada di PLN-01 Bagian 4 (password manager 4 jam, ticketing 8 jam, knowledge base 24 jam), tidak ada di SOP-03 | Sebagian diperbaiki. Label USULAN dipertahankan pada dua butir parameter internal. Angka per sistem sengaja tidak disalin supaya tidak ada dua tempat yang bisa saling beda (di PLN-01 angka itu juga berlabel USULAN dan disahkan Head of Operation). Mekanismenya dibuat jelas: Pemilik sistem menetapkan RPO dan RTO (bagian 4, bagian 5, 6.1 langkah 2), NOC Engineer mencatat RTO tiap job di Daftar Job (6.1 langkah 3), dan Restore Record menghitung "Dalam RTO" dari Daftar Job (6.4 langkah 3). Open item 6 |
| 2 | Kelompok "Sistem internal kritis" menyamakan tiga sistem (Harian, 30 hari, RPO 24 jam), sedangkan PLN-01 memberi Tingkat 1, 2, 3 | Tidak diubah. Tidak bertentangan: RPO ketiganya di PLN-01 sama (24 jam), dan RTO didelegasikan ke PLN-01. Penjelasan ini hanya di notes |
| 3 | Monitoring (PLN-01 baris 3, RPO 24 jam) dan Jumphost (baris 6, RPO 1 minggu konfigurasi) ada di PLN-01 tetapi tidak muncul di tabel 6.1; "Jumphost" nol kemunculan di SOP-03 | Diperbaiki berlabel (USULAN): monitoring dimasukkan ke kelompok sistem internal kritis, Jumphost dimasukkan ke scope dan dihitung sebagai server kritis (parameter konfigurasi: RPO 1 minggu, RTO 4 jam, cocok dengan PLN-01). PLN-01 juga mengandalkan SOP ini untuk pemulihan Jumphost. USULAN U1 dan U2 |
| 4 | Tidak ada jadwal jam backup, lokasi, atau penyedia offsite | Sebagian. Jadwal jam per job ada di kolom Jadwal sheet Daftar Job (bukan di SOP), dan 6.1 langkah 3 mewajibkan kolom itu terisi. Lokasi atau penyedia offsite tidak ada di sumber mana pun yang saya baca, tidak diisi, open item 8. Jumlah copy tetap dari aturan 3-2-1 |
| 5 | "P2" pada tiket backup berbeda konteks dengan P2 insiden keamanan di SNX-ISMS-SOP-01 | Diperbaiki lewat definisi "Tiket P2": severity P2 (Tinggi) menurut SNX-OPS-SOP-04. SOP-01 tidak dirujuk supaya dokumen tidak menambah rujukan |
| 6 | Header masa simpan "Berlaku sampai digantikan" vs tabel record "3 tahun" | Template tidak punya field itu. Hanya tabel record bagian 11 yang berlaku (tiga baris dari sumber, dua berita acara, dan tiga rekaman yang dihasilkan langkah prosedur; lihat Putaran perbaikan 1) |
| 7 | "SKILL_backup-snapshot-ops" bukan dokumen bernomor | Dihapus (RUNBOOK §0 butir 6), tidak ada pengganti: isinya tidak terbaca dan tidak boleh dirujuk. Referensi ISO tetap di bagian 11 |
| 8 | Pengesahan kosong; dua baris riwayat revisi bertanggal sama berstatus Menunggu | Teratasi template: satu baris Revision 00, Effective Date kosong, Signature kosong |
| 9 | Bagian 7.3 butir 3 menyebut sheet "Restore Test dan Request", padahal FRM-01 memakai "Restore Record" | Diperbaiki: dokumen memakai "Restore Record" di 6.3 langkah 7, 6.4 langkah 3 sampai 4, dan peran |
| 10 | FRM-07 menjadwalkan uji restore bulanan pelanggan (aktivitas 7) tetapi tidak memuat uji triwulanan sistem internal yang dituntut 7.4 butir 1 | Tidak bisa diperbaiki dari dokumen ini. 6.4 langkah 1 menunjuk FRM-07 hanya untuk pelanggan; uji sistem internal tercantum di bagian 8 saja. Open item 7 |
| 11 | (Tambahan, dari pembacaan gambar rId28) Diagram sumber hanya mencatat dan melaporkan hasil bila restore lolos, padahal 7.4 butir 3 mencatat hasil "berhasil atau gagal" | Diperbaiki: diagram baru mencatat hasil uji sebelum keputusan "Uji restore lolos?", dan jalur gagal ikut berakhir di laporan (garis putus-putus kembali ke alur utama) |
| 12 | (Tambahan) "Job gagal dijalankan ulang secepatnya" tanpa batas waktu | Diperbaiki berlabel: "pada shift yang sama (USULAN)" di 6.2 langkah 3 dan bagian 8 (U8). Open item 18 |
| 13 | (Tambahan) Tabel 6.1 dan kelompok "Dokumen di Drive": scope menyebut dokumen Drive, tabel 6.1 tidak punya baris untuk itu | Ditulis berlabel: Lead NOC menetapkan parameternya sebelum SOP berlaku (U6). Open item 5 |

Cacat dari POL-OPS-001 dan PRO-OPS-001 yang relevan:

| # | Cacat | Penanganan |
|---|---|---|
| 14 | POL-OPS-001 P-08 menetapkan semua tiket di GLPI; owner 14 Okt: Zammad untuk Ops | Mengikuti owner: tiket Ops di Zammad. Open item 4 |
| 15 | PRO-OPS-001 NOC-04 butir 4 menandai "Uji restore terjadwal minimal sekali per bulan per pelanggan backup" sebagai (USULAN), sedangkan SOP-03 menulisnya tanpa label | Angka tetap tanpa label karena SOP-03 adalah sumber utama dan menulisnya sebagai ketentuan. Perbedaan label dicatat di open item 17 |
| 16 | Tujuh SKILL_* di baris Rujukan teknis PRO-OPS-001 (termasuk SKILL_backup-snapshot-ops) dan "packet setor", "jalur staging" | Tidak ada yang dibawa ke dokumen |
| 17 | POL-OPS-001 Bagian 13: runbook "alur backup dan restore Acronis" belum ada; vault belum live sebelum kredensial dari dua sumber dimigrasikan | Langkah SOP-03 sengaja umum, tidak menyebut perintah platform. Open item 3 dan 14 |
| 18 | POL-OPS-001 Bagian 3 menulis Fani Fatullah sebagai Komisaris dan Advisor | Tidak terbawa: Fani hanya muncul di blok Reviewed By sesuai defaults |
| 19 | PRO-OPS-001 memakai "blok ukur" dan "blok ubah" | Tidak dipakai di dokumen ini |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kalimat pasif sumber diberi pelaku dari bagian 5: NOC Engineer mendaftarkan job dan sistemnya (7.1 pasif; FRM-01 menyebut NOC Engineer mengisi log), mencatat permintaan restore sebagai tiket, melaksanakan restore, serta menjalankan ulang job.
2. Lead NOC menganalisis akar uji restore gagal: sumber 7.4 butir 3 pasif. Dasar: SOP-04 lane OPS (draf specs/OPS-SOP-04.json) menugaskan Lead NOC menyusun RCA P1 dan P2, dan POL-OPS-001 Bagian 9.2 menyebut Lead NOC menyusun RCA bersama engineer.
3. NOC Engineer memperbaiki job yang menyebabkan uji gagal: dari kotak diagram sumber "Analisis akar / tiket P2, perbaiki job", pelaku tidak disebut.
4. Lead NOC memasukkan ringkasan ke SNX-OPS-RPT-01 dan Service Delivery Manager ke laporan bulanan pelanggan. Hanya yang kedua didukung kalimat peran sumber ("melaporkan hasil uji restore di laporan bulanan"); pelaku RPT-01 tidak disebut di mana pun, jadi langkahnya diberi label (USULAN) di dokumen (U14). Open item 10.
5. Lead NOC memeriksa pelaksanaan uji restore tiap bulan: dari POL-OPS-001 Bagian 9.2 ("memastikan uji restore bulanan berjalan"); "tiap bulan" mengikuti frekuensi uji dan target 100% per bulan.
6. Offboarding (direvisi di putaran perbaikan 1): sumber SOP-03 pasif, PRO-OPS-001 SDPM-06 menunjuk Service Delivery Manager sebagai pelaksana ("Ekspor data atau backup terakhir sesuai kontrak, serahkan ke pelanggan dengan berita acara."). Dokumen kini mengikuti SDPM-06: Service Delivery Manager mencatat ketentuan kontrak, menyerahkan backup ke pelanggan, dan membuat berita acara. NOC Engineer tetap ada sebagai pelaksana teknis ekspor atau penghapusan di platform backup, berlabel (USULAN) di 6.5 langkah 2 dan di bagian 5 (U13), karena akses console dibatasi pada peran operator (bagian 4) dan di draf ISMS-SOP-02 baris matriks SD dan PM tidak punya akses Acronis. Open item 11.
7. Pemusnahan media fisik oleh NOC Engineer (berlabel (USULAN) di 6.5 langkah 5 dan bagian 5, U15): sumber SOP-03 pasif; SOP-04 (salinan audit) memberi NOC Engineer peran "dekomisi". Berita acara pemusnahan 5 tahun dan lokasi "Lampiran SNX-ISMS-REG-01" dari SOP-04 (salinan audit), bukan SOP-03.
8. Kolom Authority tabel peran tidak ada di sumber. Isinya diturunkan dari kalimat tanggung jawab sumber; Lead SOC paling tipis karena sumber hanya satu kalimat.
9. Lokasi record "Google Drive": FRM-01, FRM-07, FRM-08 adalah berkas xlsx di Drive (sumber audit); folder tidak disebut. Tiket sumber FRM-08 hidup di Zammad. Pemilik record Lead NOC mengikuti "Pemilik dokumen" masing-masing (FRM-01 dari audit; FRM-07 dan FRM-08 dari notes lane lain).
10. Definisi umum (Job, Platform backup, Restore, Uji restore, Lokasi produksi, Lokasi uji, Console dan repository backup) adalah penjelasan penyusun, bukan kalimat tim. "Data kritis" tidak didefinisikan di sumber; definisi di dokumen berlabel USULAN.
11. "Lead NOC meninjau dokumen setiap tahun" dari review_period YEARLY di defaults dan "Pemilik SOP" di sumber. "Lead NOC memantau kepatuhan lewat empat indikator" adalah tafsir: sumber memuat indikator tanpa penanggung jawab.
12. Kolom "Dalam RTO" dan "Integritas terverifikasi" di Restore Record, serta "Tindakan bila gagal" dan "Ref tiket" di Backup Log, diambil dari struktur FRM-01 di salinan audit dan notes/ISMS-FRM-01.md, bukan dari SOP-03.
13. Diagram memuat jalur konfigurasi, pemantauan, dan uji restore seperti sumber. Alur restore atas permintaan (6.3) tidak digambar agar diagram tetap terbaca di satu halaman; template hanya punya satu diagram. Open item 16.
14. Titik awal "tiap shift malam" mengikuti definisi Shift malam = Shift 3 (FRM-01 dropdown Shift 1 sampai 3; POL-OPS-001 Bagian 5 "Shift 3, Malam").

## USULAN

Lint menghitung 25 penyebutan "(USULAN)" di dokumen (satu butir bisa muncul di bagian 4, 5, 6, dan 8); di bawah ini 17 butir unik.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Jumphost masuk scope dan dihitung sebagai server kritis (parameter konfigurasi) | Bagian 2, bagian 4 | Menutup cacat audit 3; PLN-01 mengandalkan SOP ini untuk pemulihan Jumphost | Fani |
| U2 | Monitoring (Nusametric dan Overseer) masuk kelompok sistem internal kritis | Bagian 4 | Menutup cacat audit 3; PLN-01 baris 3 memberi RPO 24 jam | Fani |
| U3 | Definisi "Data kritis" = data pada sistem internal kritis dan data pelanggan yang dicakup layanan backup | Bagian 3 | Sumber memakai istilah ini di aturan 3-2-1 tanpa definisi | Fani |
| U4 | Parameter sistem internal kritis: backup minimal harian, retensi minimal 30 hari, offsite wajib, RPO 24 jam, RTO sesuai PLN-01 | Bagian 4 | Label USULAN dari sumber ("Parameter sistem internal adalah USULAN") | Fani |
| U5 | Parameter konfigurasi network device, WAF, server kritis: setiap perubahan dan mingguan, 90 hari, offsite wajib, RPO 1 minggu, RTO 4 jam | Bagian 4 | Label USULAN dari sumber | Fani |
| U6 | Parameter backup dokumen di Drive ditetapkan Lead NOC sebelum SOP berlaku | Bagian 4 | Scope menyebut dokumen Drive, tabel 6.1 tidak punya baris | Fani |
| U7 | Salinan offline (break-glass) encryption key di luar password manager, dipegang Lead NOC | Bagian 4, 5, 6.1 langkah 5 | Perbaikan lintas dokumen RUNBOOK §6: key disimpan di password manager yang ikut dibackup. Sibling ISMS-FRM-01 memuat USULAN yang sama | Fani |
| U8 | Job gagal dijalankan ulang pada shift yang sama | 6.2 langkah 3, bagian 8 | Sumber hanya "secepatnya"; batas waktu terukur diperlukan | Fani |
| U9 | Tindak lanjut penggunaan repository di atas 80% dicatat sebagai tiket di Zammad | 6.2 langkah 6 | Sumber pasif tanpa pelaku dan tanpa rekaman | Fani |
| U10 | Restore sistem internal saat insiden: Lead NOC menyetujui, persetujuan PIC pelanggan tidak berlaku, dicatat Pemulihan insiden | Bagian 9 baris 5 | PLN-01 merujuk SOP ini untuk restore sistem internal; 7.3 sumber hanya mengatur permintaan pelanggan | Fani |
| U11 | Lokasi (folder Drive Operation) dan pemilik (Service Delivery Manager) berita acara penyerahan atau penghapusan backup | Bagian 11 | Sumber menyebut berita acara tetapi tidak memasukkannya ke tabel record | Fani |
| U12 | Retensi berita acara penyerahan atau penghapusan 3 tahun | Bagian 11 | Disamakan dengan retensi record lain di SOP ini; kontrak pelanggan mungkin menentukan lain | Fani, Legal |
| U13 | NOC Engineer sebagai pelaksana teknis ekspor atau penghapusan backup pelanggan saat offboarding | 6.5 langkah 2, bagian 5 | PRO-OPS-001 SDPM-06 menunjuk Service Delivery Manager; akses console dibatasi pada peran operator | Fani |
| U14 | Lead NOC sebagai pelaku memasukkan ringkasan uji restore ke SNX-OPS-RPT-01 | 6.4 langkah 9, bagian 5 | Sumber 7.4 butir 4 pasif; pelaku tidak disebut di mana pun | Fani |
| U15 | NOC Engineer sebagai pelaku pemusnahan media backup fisik | 6.5 langkah 5, bagian 5 | Sumber 7.5 butir 3 pasif | Fani |
| U16 | Persetujuan tertulis PIC pelanggan dilampirkan di tiket permintaan restore di Zammad | Bagian 11 | Sumber menyebut persetujuan tertulis tanpa lokasi; retensi mengikuti tiket (3 tahun, sumber 7.3 dan bagian 8) | Fani |
| U17 | Tiket tindak lanjut kapasitas repository (di atas 80%) sebagai rekaman, pemilik Lead NOC, retensi 3 tahun | Bagian 11 (melengkapi U9) | Sumber hanya menulis "ditindaklanjuti" tanpa rekaman | Fani |

Penanda tangan (Erik, Fani, Samuel) dan process owner "Lead NOC" juga berstatus USULAN menurut config/defaults.json; tidak diberi label di badan dokumen.

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju: sumber COO (Amirull Yusuf Zulkarnain), template dan defaults Samuel Kristanto Utomo / President Director. Defaults dipakai | Owner atau Samuel |
| 2 | Pemeriksa: sumber "ISO/ISMS Coordinator"; defaults Fani. HR-ORG-01 K-13: ISMS Coordinator belum ditetapkan, jadi bagian 5 tidak memuat peran itu | Owner |
| 3 | Status password manager (vault): "menunggu konfirmasi Ops". Aturan penyimpanan encryption key di password manager baru bisa dipatuhi bila vault live; POL-OPS-001 Bagian 13 menyebut migrasi kredensial dari dua sumber belum selesai | Ops |
| 4 | Batas Zammad lawan Service Hub (GLPI): POL-OPS-001 P-08 masih "semua tiket di GLPI". Dokumen memakai Zammad untuk tiket Ops. Saluran permintaan restore sistem internal (bukan pelanggan) belum ditentukan | Owner |
| 5 | Parameter backup dokumen di Drive tidak ada di sumber (U6) | Fani |
| 6 | RTO per sistem internal ada di PLN-01 (4, 8, 24 jam, berlabel USULAN, disahkan Head of Operation) dan tidak disalin. Head of Operation belum ada pemegang (HR-ORG-01 K-10) dan tidak ada di bagian 5 SOP ini; SOP menunjuk Pemilik sistem sebagai penetap | Fani |
| 7 | SNX-OPS-FRM-07 tidak memuat uji restore triwulanan sistem internal (cacat sumber). Notes OPS-FRM-07 USULAN 3 menunggu Fani; bila tidak ditambah, uji internal tidak punya jadwal | Fani |
| 8 | SNX-ISMS-FRM-01 Daftar Job tidak punya kolom Tujuan (lokasi atau platform), padahal 6.1 langkah 3 meminta "tujuan". Lokasi dan penyedia offsite tidak ada di sumber. Sheet Ringkasan FRM-01 menghitung keberhasilan uji restore; apakah itu sama dengan "berhasil pada percobaan pertama" (KPI 95%) belum diperiksa | Pemilik FRM-01 (Lead NOC), Fani |
| 9 | Lead SOC: sumber memberi tanggung jawab "memastikan backup terlindungi dari ransomware dan akses tidak sah" tanpa langkah, frekuensi, atau rekaman. Dokumen hanya menyebutnya di bagian 5. Tidak diisi karena akan mengarang | Fani |
| 10 | Pelaku yang memasukkan ringkasan uji restore ke SNX-OPS-RPT-01 tidak disebut sumber; dokumen memakai Lead NOC berlabel USULAN (asumsi 4, U14) | Fani |
| 11 | Pelaku offboarding: sumber SOP-03 pasif; dokumen mengikuti PRO-OPS-001 SDPM-06 (Service Delivery Manager) dan memberi label USULAN pada NOC Engineer sebagai pelaksana teknis (U13). Pelaku pemusnahan media fisik (U15) juga tidak disebut sumber (asumsi 6 dan 7) | Fani |
| 12 | Apakah restore ke lokasi produksi juga harus lewat change request SNX-OPS-SOP-02: POL-OPS-001 P-04 mewajibkan go-gate untuk ubah production, sumber SOP-03 tidak menyebutnya. Tidak ditambahkan | Fani |
| 13 | Scope hanya punya satu pengecualian (pelanggan tanpa layanan backup). POL-OPS-001 Bagian 2 mengecualikan app-level pelanggan (isi WordPress, plugin, DB aplikasi); apakah restore data app-level di luar SOP ini belum diputus | Fani |
| 14 | Sumber tidak memuat kontrol pengganti untuk "restore ke lokasi uji tidak memungkinkan" dan "platform tidak mendukung immutable copy". Bagian 9 hanya menyebut pelaku dan ketentuan yang sudah ada; tidak ada kontrol baru | Fani |
| 15 | Annex A 8.14 (redundansi fasilitas pemrosesan informasi) hanya dicakup lewat copy, offsite, dan aturan 3-2-1. Redundansi fasilitas ada di PLN-01 dan SoA menandainya "Sebagian" | Konsultan SoA |
| 16 | Diagram tidak memuat restore atas permintaan (6.3); template hanya punya satu diagram | Aziz (template) |
| 17 | POL-OPS-001 dan PRO-OPS-001 berstatus DRAFT v0.1 dengan penomoran USULAN; kode POL-OPS-001 di bagian 11 diganti nomor SNX bila terbit. PRO-OPS-001 NOC-04 menandai uji restore bulanan sebagai USULAN, SOP-03 tidak | Fani |
| 18 | Angka 80% kapasitas, 2 kali berturut-turut, 98%, 95% dan seterusnya bersumber SOP-03 tanpa baseline pengukuran; POL-OPS-001 Bagian 11 mencatat baseline KPI belum diukur | Fani |
| 19 | Template tidak punya slot KPI; empat target sumber dilebur ke kolom SLA / Timing bagian 8 | Aziz (template) |
| 20 | Tidak ada tanggal draft di dokumen; Effective Date dan tanda tangan kosong sampai Samuel menandatangani | Samuel |
| 21 | Sumber Bagian 9 (Pemantauan kinerja) tidak menyebut penanggung jawab empat indikator. Bagian 8 dan Conclusion memakai Lead NOC | Fani |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan yang saya ubah:
- Hal yang sama muncul di empat tempat: aturan restore produksi (butuh approval Lead NOC dan persetujuan tertulis) ada di bagian 4, di kolom wewenang NOC Engineer, di baris pengecualian, dan di langkah 6.3. Sama dengan itu, kalimat pengecualian pelanggan tanpa layanan backup muncul di bagian 2 dan 9. Saya sisakan aturan di bagian 4 dan bagian 2; tempat lain merujuk ("sesuai approval dan persetujuan di bagian 4", "langkah 3 dan 4", "(bagian 2)").
- Kolom wewenang Service Delivery Manager di draf pertama berbunyi "Menjadikan kontrak sebagai dasar parameter backup pelanggan", kalimat pengisi yang terdengar rapi tetapi kosong. Saya ganti dengan hal yang benar-benar dikerjakan peran itu.
- Butir kebijakan pertama memakai kalimat tim "Backup dianggap ada hanya bila restore-nya terbukti" (judul gambar di sumber). Kalimat ini pendek dan spesifik; saya tidak menggantinya dengan pembuka umum.
- Label "(Annex A 8.13)" muncul di enam butir dan terdengar mekanis. Dipertahankan karena kriteria menuntut kontrol tercermin di bagian 4, tetapi tidak saya tempelkan pada butir yang bukan inti 8.13 (enkripsi, akses console, klasifikasi).
- Sinonim: sumber memakai "path uji" dan "lokasi uji", "pemulihan" dan "restore", "kunci" dan "encryption key". Saya pilih satu: lokasi uji, restore (arti di definisi), encryption key. "Approval" hanya untuk Lead NOC, "persetujuan" hanya untuk PIC pelanggan.
- Daftar tiga item muncul karena datanya memang tiga (mis. frekuensi, retensi, offsite) atau lebih; tidak ada kelompok tiga yang dibuat demi irama. Kalimat tim yang sudah jelas dipertahankan (tujuan, parameter, prinsip perlindungan).
- Tidak ada pembuka atau penutup generik, em-dash, en-dash, tebal atau huruf kapital untuk penekanan. Lint gaya lulus.
- Diagram: judul gambar sumber sudah dipakai di kebijakan, jadi diagram tidak mengulang judul.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka tanpa sumber yang tertulis di dokumen hanya yang berlabel USULAN: "pada shift yang sama" (batas waktu job diulang), retensi berita acara 3 tahun, dan butir kebijakan yang menjadi usulan (U1 sampai U17). Tidak ada angka lain.
- Semua angka lain dari SOP-03: 30 hari, 90 hari, 14 hari, 24 jam, 1 minggu, 4 jam, 4 sampai 24 jam, 2 kali berturut-turut, 80%, 98%, 100%, 95%, 3 tahun (tiga record). Angka 5 tahun untuk berita acara pemusnahan dari SOP-04 (salinan audit), dan tertulis "sesuai SNX-ISMS-SOP-04".
- Nama orang hanya tiga penanda tangan dari config/defaults.json. Tidak ada tanggal.
- Nama sistem dari sumber: Acronis Cyber Protect, Nusagrid, Zammad, Service Hub (GLPI), Drive, WAF, Jumphost. Nusametric dan Overseer dari POL-OPS-001 dan PRO-OPS-001 (bahan), bukan dari SOP-03; Jumphost dari PLN-01 (salinan audit), berlabel USULAN.
- Yang bukan kalimat tim dan sudah dicatat di bagian 6: nama klausul ISO, definisi umum, pelaku kalimat pasif, kolom wewenang, lokasi Google Drive, nama kolom sheet FRM-01 (dari salinan audit, bukan berkas Drive terbaru).
- Hal yang saya koreksi setelah pemeriksaan: kata "Menjadikan kontrak ..." diganti, pengulangan aturan dikurangi, definisi "Shift malam" diubah dari "ditetapkan di POL-OPS-001" menjadi "tercantum di POL-OPS-001" karena jam di POL-OPS-001 masih berlabel USULAN.

## Putaran perbaikan 1

Verifikator memberi PASS dengan temuan nonblocking (qa/ISMS-SOP-03.verify.r1.json). Orkestrator meminta satu perbaikan wajib dan merapikan sisanya bila murah dan aman.

| # | Temuan verifikator | Penanganan |
|---|---|---|
| 1 | Pelaku serah atau hapus backup saat offboarding ditulis NOC Engineer tanpa label, padahal PRO-OPS-001 SDPM-06 menunjuk Service Delivery Manager (wajib) | Diperbaiki. 6.5 kini: Service Delivery Manager mencatat ketentuan kontrak (langkah 1), NOC Engineer mengekspor atau menghapus di platform backup berlabel (USULAN) (langkah 2), Service Delivery Manager menyerahkan backup ke pelanggan (langkah 3) dan membuat berita acara (langkah 4), NOC Engineer memusnahkan media fisik berlabel (USULAN) (langkah 5). Bagian 5 diselaraskan. U13 dan U15 |
| 2 | Pelaku tanpa sumber (Lead NOC ke SNX-OPS-RPT-01, NOC Engineer memusnahkan media fisik) tanpa label | Diperbaiki: label (USULAN) di langkah dan di bagian 5 (U14, U15) |
| 3 | Kalimat pasif di bagian 4 padahal pelaku diketahui (snapshot, kapasitas, copy offline encryption key) | Diperbaiki: NOC Engineer mengambil snapshot, NOC Engineer memantau kapasitas repository, Lead NOC menyimpan copy offline encryption key. Kalimat pasif lain di bagian 4 (enkripsi, pembatasan akses, klasifikasi) tidak diubah karena pelakunya tidak disebut sumber |
| 4 | "copy" dan "salinan" berganti; "restore" dan "dipulihkan" berganti | Diperbaiki: "copy" dipakai di seluruh dokumen (definisi Offsite copy, copy offline encryption key, copy backup); "restore" dipakai di kebijakan, langkah, dan pengecualian ("Restore data itu hanya atas permintaan...", "tidak dijanjikan restore data", "Data di-restore ke lokasi produksi"). Dua pemakaian "dipulihkan" dipertahankan: kalimat Tujuan (kalimat tim, utuh) dan definisi Uji restore yang mengikutinya. "Pemulihan insiden" adalah nilai dropdown FRM-01, bukan istilah bebas |
| 5 | Isi sama di bagian 4 dan 5 (Lead NOC menetapkan, Lead SOC memastikan, Pemilik sistem menetapkan, Service Delivery Manager mencatat) | Diperbaiki: empat kalimat peran dihapus dari bagian 4 (Service Delivery Manager mencatat, Lead NOC menetapkan, Pemilik sistem menetapkan, Lead SOC memastikan); bagian 4 hanya memuat satu butir penunjuk "Peran yang menetapkan parameter backup dan peran yang mencatatnya ada di bagian 5 dan butir 6.1". Peran dan tanggung jawabnya tinggal di bagian 5 dan 6.1. Konsekuensi: Lead SOC kini hanya muncul di bagian 5 (open item 9 tetap) |
| 6 | Bagian 9 baris 1: penanganan (snapshot) tidak nyambung dengan kondisi (permintaan restore) | Diperbaiki: baris hanya memuat "NOC Engineer tidak menjanjikan restore data kepada pelanggan itu (bagian 2)". Snapshot tetap di scope (bagian 2) |
| 7 | Kolom "tujuan" di 6.1 langkah 3 tidak ada di Daftar Job FRM-01 | Tidak diubah: sumber 7.1 butir 1 menyebut "tujuan"; ketidaksesuaian ada di FRM-01. Tetap open item 8 |
| 8 | Rekaman yang dihasilkan langkah prosedur belum ada di tabel rekaman (persetujuan tertulis PIC pelanggan, kapasitas repository, change request FRM-04) | Diperbaiki: tiga baris ditambah di bagian 11. Persetujuan tertulis: dilampirkan di tiket Zammad (USULAN), 3 tahun sama dengan tiket (U16). Change request: berkas SNX-OPS-FRM-04, pemilik dan retensi 3 tahun sesuai SNX-OPS-SOP-02 (draf lane OPS-SOP-02 mencatat 3 tahun). Kapasitas: tiket Zammad hanya bila di atas 80%, pemilik Lead NOC, 3 tahun, berlabel (USULAN) (U17). Pembacaan kapasitas mingguan sendiri tidak punya rekaman di sumber; 6.2 langkah 5 hanya mencatat di tiket bila di atas 80% |
| 9 | Annex A 8.14 hanya ditopang lewat aturan 3-2-1 | Tidak diubah, sama dengan sumber. Open item 15 |
| 10 | PIC empat indikator NOC Engineer, Conclusion menyebut Lead NOC | Diperbaiki: PIC empat indikator di bagian 8 jadi Lead NOC, Lead NOC diberi tanggung jawab "memantau empat indikator kinerja di bagian 8" di bagian 5, dan open item 21 mencatat bahwa sumber tidak menyebut penanggung jawab |

Uji ulang: render lalu lint sop memberi `"pass": true`, `"fails": []`, satu warn (25 butir USULAN), tanpa warn PIC SLA; validator OOXML PASSED; pemeriksaan tambahan atas spec (PIC, kode dokumen terhadap Dokumen terkait, panjang langkah, em-dash, en-dash) bersih.

## Hasil uji sendiri

- Perintah 1: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-SOP-03.json /tmp/pen-ISMS-SOP-03/ISMS-SOP-03.docx` (exit 0).
- Perintah 2: `python3 -I tools/lint_doc.py /tmp/pen-ISMS-SOP-03/ISMS-SOP-03.docx sop` memberi `"pass": true`, `"fails": []`, satu warn (25 butir USULAN, setelah putaran perbaikan 1).
- Pemeriksaan tambahan atas spec (skrip sementara di scratchpad, tidak masuk repo): nol em-dash, en-dash, tanda § dan tanda `**`; semua PIC langkah dan SLA ada di tabel peran bagian 5; semua kode dokumen di badan tercantum di Dokumen terkait, dan sebaliknya; tidak ada langkah di atas 24 kata.
- Validator OOXML: "All validations PASSED!" (413 paragraf).
