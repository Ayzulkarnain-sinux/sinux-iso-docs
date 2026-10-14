# Catatan penyusun OPS-SOP-04: SOP Technical Incident Handling & Escalation

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-SOP-04.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-SOP-04 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Approval persis dari prompt dan config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. process_owner "Lead NOC" (jabatan tanpa nama, dari "Pemilik dokumen" sumber). status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Hasil uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-SOP-04.json /tmp/pen-OPS-SOP-04/OPS-SOP-04.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-OPS-SOP-04/OPS-SOP-04.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "9 butir (USULAN) menunggu ACC" (warn PIC SLA nol). Hasil render dikonversi soffice ke PDF 18 halaman dan dibaca per bagian; diagram alir (15 simpul, rankdir TB) dibuka sebagai gambar. tools/selftest.sh tidak saya jalankan (menulis ke direktori bersama penyusun paralel); berkas tools, template, reference, config tidak saya ubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-SOP-04_SOP_Technical_Incident_Handling_Escalation.docx (203585 byte, docx di Drive) | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG | 2026-10-13T06:09:04Z (get_file_metadata hari ini, cocok dengan prompt; fileSize 203585 cocok dengan hasil dekode) | read_file_content (teks penuh), download_file_content (didekode ke /tmp/pen-OPS-SOP-04/src.docx, dibuka dengan python3 -I; header1.xml dan footer1.xml dibaca; comments.xml dan footnotes.xml kosong; gambar word/media/rId26.png dibuka dan cocok dengan deskripsi context/audit) |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, cocok dengan prompt) | read_file_content. Bahan saja: definisi app-level pelanggan dan vantage eksternal, dan pemetaan Commercial, Tech dan Product ke jabatan |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, cocok dengan prompt) | read_file_content. Bahan saja: definisi blok ukur, label "(USULAN tenggat)" RCA 2 hari kerja, daftar delapan kelas triage dengan "backup atau snapshot" |
| Kriteria penerimaan | config/checklist.json baris 66 | ekspor checklist W0 | Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.5.1, 8.7, 10.2" dan ISO/IEC 27001:2022 "5.24, 5.26, 8.16" |
| Pendukung dari repo (DATA) | config/defaults.json v21, specs/HR-ORG-01.json, specs/OPS-FRM-08.patch.json, specs/OPS-FRM-10.json, specs/ISMS-FRM-02.patch.json, specs/OPS-FRM-04.patch.json, specs/OPS-SOP-02.json, specs/OPS-SOP-03.json, context/audit | berkas repo | Dibaca untuk nama peran, rumus waktu register, pemilik rekaman, dan konsistensi lintas dokumen. Isi FRM-08, FRM-10, FRM-02, FRM-04 dipakai lewat spec dan notes penyusunnya, bukan dari Drive |

Peringatan jujur: kutipan dari context/audit (SOP-05, ML-00, FRM-08 sheet Daftar) berasal dari salinan audit 13 sampai 14 Okt, bukan dari berkas Drive terbaru. Bila tim sudah mengubahnya, rujukan di bawah bisa basi.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Ack, update, target pulih, dan eskalasi hierarki per severity; target pulih berlabel USULAN dan sama dengan sheet Target Severity di FRM-08 | Bagian 6, baris P1 Kritis: "15 menit", "Tiap 1 jam", "4 jam", "Lead langsung, COO dalam 30 menit, CEO bila COO tidak tersedia". Kepala kolom: "Target pulih (USULAN)". Catatan di bawah tabel: "Target di atas adalah target internal; target pulih sama dengan sheet Target Severity pada SNX-OPS-FRM-08. Komitmen ke pelanggan mengikuti kontrak masing-masing dan tidak boleh melebihi kapasitas riil." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |
| 2 | Alert dikonfirmasi dari dua sinyal, tiket dibuat dalam 10 menit, lalu dicatat di FRM-08 | Bagian 7.1: "Alert dikonfirmasi minimal dari dua sinyal sebelum dinyatakan insiden." dan "Tiket dibuat paling lambat 10 menit setelah konfirmasi, berisi pelanggan, layanan, waktu mulai, gejala, dan bukti awal, lalu dicatat di SNX-OPS-FRM-08." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |
| 3 | RCA wajib untuk P1 dan P2 dengan FRM-10 dan dikirim dalam 2 hari kerja; insiden berulang menjadi problem | Bagian 7.5: "Insiden P1 dan P2 wajib RCA dengan SNX-OPS-FRM-10, dikirim ke pelanggan via email dalam 2 hari kerja setelah pulih." dan "Insiden berulang (3 kali atau lebih pada layanan yang sama dalam 30 hari) diperlakukan sebagai problem dan wajib RCA walau severity rendah." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |

## 2. Fakta penting lain dan kutipan verbatim

Semua kutipan dari fileId 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG kecuali disebut lain. Kutipan dari tabel sumber ditulis "teks sel pertama: teks sel berikutnya"; teks tiap sel verbatim, tanda titik dua pemisah sel adalah tanda saya.

| # | Fakta di dokumen | Kutipan verbatim | Posisi sumber | Posisi di dokumen baru |
|---|---|---|---|---|
| 1 | Tujuan (dipertahankan utuh, suara tim) | "SOP ini menetapkan cara mendeteksi, mencatat, mengklasifikasi, menangani, mengeskalasi, dan menutup insiden teknis, agar layanan pulih secepat mungkin dan insiden besar tidak terulang." | Bagian 1 | Bagian 1 |
| 2 | Lingkup 24/7 | "Berlaku untuk seluruh gangguan teknis pada layanan yang dikelola SINUX, baik terdeteksi melalui monitoring maupun dilaporkan pelanggan, selama 24 jam sehari, 7 hari seminggu." | Bagian 2 | Bagian 2 |
| 3 | Insiden keamanan dikecualikan | "Insiden yang berindikasi keamanan informasi (kompromi, webshell, malware, kebocoran data, akun disalahgunakan) diserahkan ke SNX-ISMS-SOP-01; NOC tetap menangani sisi availabilitynya." | Bagian 2 | Bagian 2, 6.2, 9 |
| 4 | Pemilik, klasifikasi, acuan ISO | "Pemilik dokumen: Lead NOC"; "Klasifikasi: RESTRICTED (Internal)"; "Acuan ISO 9001:2015: Klausul 8.5.1, 8.7, 10.2"; "Acuan ISO/IEC 27001:2022: Klausul atau kontrol Annex A 5.24, 5.26, 8.16" | Tabel Atribut | Identity, bagian 4, bagian 11 |
| 5 | Definisi lima istilah | "Insiden: Gangguan tidak terencana atau penurunan mutu layanan"; "Ack: Pengakuan pertama ke pelanggan bahwa tiket diterima dan sedang ditangani"; "Workaround: Pemulihan sementara sebelum akar masalah diperbaiki"; "Problem: Akar masalah dari satu atau beberapa insiden, ditangani melalui RCA" | Bagian 4 | Bagian 3 |
| 6 | Peran | "Lead NOC: Pemilik SOP; eskalasi teknis kedua; menyusun RCA P1 dan P2"; "Head of Operation: Penanggung jawab P1 sampai RCA selesai; memanggil personel off-duty"; "Service Delivery Manager: Komunikasi formal ke pelanggan untuk P1 dan P2; memastikan RCA terkirim"; "COO: Diberi tahu dalam 30 menit untuk P1; keputusan bila P1 menuntut komitmen baru" | Bagian 5 | Bagian 5 |
| 7 | Definisi severity P1 sampai P4 | P1: "Kompromi root atau host baru; production pelanggan down berkepanjangan dan jalur vendor buntu; insiden keamanan data pelanggan; tuntutan komitmen scope atau komersial baru yang tidak bisa ditunda; hal legal"; P4: "Service request, pertanyaan, perubahan terjadwal" | Bagian 6 | Bagian 3 |
| 8 | Ack dan update per severity | Ack: "15 menit", "30 menit", "2 jam kerja", "1 hari kerja". Update: "Tiap 1 jam", "Tiap 3 jam atau per shift", "Harian", "Saat selesai". Target pulih: "4 jam", "8 jam", "24 jam", "72 jam". Eskalasi: "Lead dalam 1 jam", "Lead bila melewati target", "Tidak perlu" | Bagian 6 | Bagian 8, butir 6.6 |
| 9 | Matriks eskalasi fungsional | "Infra Nusagrid backend (hypervisor, console, node, billing sistem): Penyedia infrastruktur Nusagrid (Maxcloud atau Awandata), via grup Nusagrid"; "WAF, load balancer, proxy, web, DC fisik, network: Tech dan Product"; "SOC, SIEM, Wazuh untuk pelanggan dengan partner SOC: Partner SOC (Arktech)"; "Platform Nusametric: TelemetryFlow"; "Harga, quote, kontrak: Commercial"; "Pelanggan pemerintah di lapangan: PIC proyek sesuai format komunikasi pelanggan"; "P1 saat COO tidak dapat dihubungi: CEO" | Bagian 6, Matriks eskalasi fungsional | Butir 6.2 langkah 7, butir 6.6 |
| 10 | PIC eksternal tidak ditulis | "Nama dan kontak PIC eksternal disimpan di file kontak restricted:ops, tidak di dokumen ini." | Bagian 6 | Bagian 4 |
| 11 | Sumber deteksi dan kanal | "Insiden terdeteksi dari monitoring (Nusametric, Overseer, console Nusagrid, Acronis, Cloudflare) atau laporan pelanggan (Zammad melalui WhatsApp, telepon, email; Service Hub untuk GMF dan internal)." | Bagian 7.1 | Butir 6.1 |
| 12 | Status hanya setelah dicek di monitoring | "Akui ke pelanggan sesuai target Ack. Status disampaikan setelah dicek di monitoring, dengan frasa “dari pantauan kami”." | Bagian 7.2 | Bagian 4 (aturan), butir 6.2 langkah 1 (Ack) |
| 13 | Kelas triage dan serah-serah | "Tetapkan severity (Bagian 6) dan kelas triage: akses atau firewall atau VPN, VM lifecycle, down atau performa, OTP atau email, backup, SSL atau DNS, DC atau colo, billing."; "Menyangkut app-level pelanggan: serahkan ke developer atau PIC pelanggan dengan penjelasan tertulis."; "Menyangkut harga: serahkan ke Commercial." | Bagian 7.2 | Butir 6.2 |
| 14 | Kredensial pelanggan | "Kredensial pelanggan hanya diterima melalui direct message atau password manager; pelanggan diminta rotate setelah dipakai." | Bagian 7.3 | Bagian 4 (kanal), butir 6.3 langkah 6 (rotate) |
| 15 | Pemulihan yang mengubah production | "Pemulihan yang mengubah production mengikuti SNX-OPS-SOP-02 (P1 boleh sebagai change Emergency)." | Bagian 7.3 | Butir 6.3 langkah 4, bagian 9 |
| 16 | Shift saat P1 | "Insiden P1 yang berjalan saat pergantian shift tidak dipindah di tengah langkah teknis." | Bagian 7.3 | Bagian 9 |
| 17 | Verifikasi dan penutupan | "Verifikasi dari sisi pelanggan (browser nyata, vantage eksternal) dan konfirmasi pelanggan."; "Tutup tiket dengan ringkasan gejala, akar (bila sudah diketahui), tindakan, dan waktu pulih."; "Lengkapi SNX-OPS-FRM-08: waktu Ack, waktu pulih, status SLA." | Bagian 7.4 | Butir 6.4 |
| 18 | Tindakan korektif | "Tindakan korektif dicatat dengan pemilik dan tenggat, lalu dipantau sampai efektif." | Bagian 7.5 | Bagian 4, butir 6.5 langkah 7 dan 8 |
| 19 | Komunikasi pelanggan | Ack: "Tiket diterima, nomor tiket, sedang dicek"; Update: "Kondisi terkini, langkah berikutnya, estimasi bila ada"; Pulih: "Waktu pulih, ringkasan tindakan" dengan kanal "Sama, plus email untuk P1 dan P2"; RCA: "Kronologi, akar, tindakan korektif" dengan kanal "Email resmi" | Bagian 8 | Butir 6.2 sampai 6.5 |
| 20 | Rekaman dan masa simpan | "Technical Ticket / Incident Register: SNX-OPS-FRM-08, 3 tahun"; "RCA & Corrective Action Report: SNX-OPS-FRM-10, 5 tahun"; "Security Incident & Investigation Records: SNX-ISMS-FRM-02, 5 tahun"; "Change request emergency: SNX-OPS-FRM-04, 3 tahun" | Bagian 9 | Bagian 11 (tabel Rekaman) |
| 21 | Indikator kinerja | "Tiket P1 dan P2 di-ack dalam target: 95%"; "Mean time to restore P1: Dikalibrasi setelah 3 bulan data"; "RCA P1 dan P2 terkirim dalam 2 hari kerja: 100%"; "Tindakan korektif selesai sesuai tenggat: 90%" | Bagian 10 | Bagian 8 (empat baris Indikator; template tidak punya slot KPI) |
| 22 | Titik awal waktu di register (fakta dari form tim, bukan dari SOP-04) | "Respon (Dilaporkan sampai Ack), durasi pulih (Dilaporkan sampai Pulih), dan status SLA dihitung otomatis memakai sheet Target Severity." (Kontrol Dokumen B20 setelah patch OPS-FRM-08); rumus S dan T sumber FRM-08: ROUND((J-I)*1440,0) dan ROUND((K-I)*24,1) dengan I = Dilaporkan | specs/OPS-FRM-08.patch.json, notes/OPS-FRM-08.md; fileId FRM-08 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz | Bagian 3 (Waktu Dilaporkan), bagian 4 |
| 23 | Rantai RCA di form tim (bukan dari SOP-04) | "Head of Operation: Pemilik dokumen. Menyetujui dan mengirim RCA." (Peran, spec OPS-FRM-10) dan "Lead NOC atau Lead SOC: Menyusun dan mencatat RCA dari bagian Identitas sampai Tindakan" | specs/OPS-FRM-10.json; fileId FRM-10 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS | Butir 6.5 langkah 1, 4, 5, 7 |

## 3. Peta bagian sumber ke 11 bagian template

| Bagian sumber | Tujuan di dokumen baru | Catatan |
|---|---|---|
| 1 Tujuan | 1 Purpose | Kalimat tim utuh |
| 2 Ruang lingkup | 2 Scope | Kalimat tim utuh pada butir 1; pengecualian ditulis jelas pada butir 2 dan 3 |
| 3 Referensi | Bagian 11 (Dokumen terkait dan Acuan standar) | Rujukan HANDOVER, SKILL_ dibuang (RUNBOOK §0 butir 6) |
| 4 Definisi | 3 Definition (lima istilah tim + 25 istilah tambahan) | Definisi P1 sampai P4 pindah dari tabel severity ke sini |
| 5 Peran | 5 Roles (enam peran sumber + empat penerima eskalasi) | Kolom Authority diturunkan, lihat asumsi |
| 6 Severity dan eskalasi | Bagian 3 (definisi), bagian 8 (Ack, update, pulih, eskalasi), butir 6.6 (matriks fungsional) | Tabel tujuh kolom dipecah menurut jenis isinya |
| 7 Prosedur 7.1 sampai 7.5 | 6.1 sampai 6.5 | Bagian 7.1 sampai 7.5 sumber sama dengan 6.1 sampai 6.5 baru; butir 6.6 baru memuat eskalasi |
| 7 Diagram | 7 Process Flow | Digambar ulang dari spec, lihat cacat 5 sampai 7 |
| 8 Komunikasi pelanggan | Tersebar di butir 6.2, 6.3, 6.4, 6.5 | Tiap baris tabel menjadi satu langkah dengan pelaku |
| 9 Record terkait | Bagian 11 (tabel Rekaman) | Kolom Lokasi dan pemilik ditambah (USULAN) |
| 10 Pemantauan kinerja | Bagian 8 (baris Indikator) dan bagian 10 | |
| Pengesahan | Blok Approval template | Tiga penanda tangan dari defaults |

## 4. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" SNX-OPS-SOP-04 (fileId 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG), baris 4233 sampai 4490 context/audit/iso-sinux-supdocs-ops-2026-10-14.md, dicocokkan ulang ke docx dan gambar.

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Target pulih berlabel USULAN; kedua sisi (SOP-04 dan FRM-08) cocok | Label dipertahankan: "(USULAN)" pada baris SLA target pulih (bagian 8). Kecocokan dengan FRM-08 saya periksa ulang di notes/OPS-FRM-08.md (Target Severity D5 sampai D8: 4, 8, 24, 72 jam) dan salinan audit. USULAN U3 |
| 2 | Mean time to restore P1 tanpa angka | Tidak diisi (angka tanpa sumber dilarang). Teks sumber dipertahankan di bagian 8; istilah didefinisikan di bagian 3. Open item 14 |
| 3 | Dua baris riwayat revisi 00 bertanggal sama; baris kedua menyebut RTO padahal tidak ada angka RTO atau RPO | Teratasi template: satu baris Revision 00, Effective Date kosong. Kata RTO tidak masuk dokumen baru |
| 4 | Kolom Disetujui "Menunggu", tanda tangan kosong; kolom nama berisi jabatan, hanya COO bernama | Tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Tiga nama dari defaults (USULAN U9). Open item 8 |
| 5 | Gambar menulis "Zammad atau GLPI", teks 7.1 tidak menyebut GLPI | Diperbaiki: simpul gambar baru "Buat tiket dan catat di SNX-OPS-FRM-08"; teks 6.1 memakai Zammad untuk laporan WhatsApp, telepon, email, dan Service Hub (GLPI) untuk laporan GMF dan internal, berlabel (USULAN) karena batas generalist belum dirinci owner. Definisi Zammad dan Service Hub sama dengan SNX-ISMS-SOP-02. USULAN U4, open item 6 |
| 6 | Gambar hanya punya cabang "ya" pada "P1 atau P2?" dan tidak memuat insiden berulang | Diperbaiki: simpul "P1, P2, atau berulang?" punya cabang Ya ke RCA dan Tidak ke Selesai |
| 7 | Gambar menaruh eskalasi dari triage ("melewati target"); teks 7.3 menaruhnya di diagnosa dan pemulihan | Diperbaiki: gambar baru menggambar eskalasi dari triage ("eskalasi sesuai severity") dan dari diagnosa ("target terlewat atau butuh pihak lain"), keduanya putus-putus dan kembali ke alur utama. Teks: butir 6.3 langkah 3 dan butir 6.6 |
| 8 | Target pulih P1 4 jam tidak dihubungkan ke anggaran 43 menit di SOP-05 | Sebagian diperbaiki: bagian 4 memisahkan target internal dan SLA kontrak, dan menyatakan pengukuran SLA kontrak mengikuti SNX-OPS-SOP-05 (rangkuman SOP-05: "mengukur, memantau, melaporkan, dan menindaklanjuti pencapaian SLA ke pelanggan"). Hubungan angka 4 jam dengan anggaran 43 menit tidak saya karang. Open item 4 mencatat perbedaan titik awal waktu dengan SOP-02 |
| 9 | Titik awal hitung Ack tidak didefinisikan | Diperbaiki: istilah "Waktu Dilaporkan" di bagian 3 dan aturan di bagian 4: Ack dan pulih dihitung dari waktu Dilaporkan, sama dengan rumus FRM-08 (fakta 22). Untuk insiden dari monitoring, waktu alert terkonfirmasi (USULAN U1). Titik awal 30 menit COO memakai titik yang sama (USULAN U2) |
| 10 | Rujukan HANDOVER §2, SKILL_ops-frontline, SKILL_incident-rca | Dibuang. Definisi P1 ditulis penuh di bagian 3 (isi HANDOVER §2 tidak ada di sumber, jadi tabel severity sumber menjadi satu-satunya teks definisi). SKILL_ops-frontline: delapan kelas triage sudah tertulis di butir 6.2. SKILL_incident-rca diganti SNX-OPS-FRM-10 |
| 11 | Nama PIC eksternal sengaja tidak ditulis; sumber merujuk "file kontak restricted:ops" | Dipertahankan: bagian 4 menulis berkas kontak yang aksesnya dibatasi untuk Operation. Label "restricted:ops" adalah label sensitivitas KB, jadi tidak ditulis. Open item 19 |

Cacat dari bagian 5 POL-OPS-001 (fileId 1bn7EHpm...) dan PRO-OPS-001 (fileId 1U8CAdib...) yang relevan untuk dokumen ini; dua dokumen itu bahan saja:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 12 | POL butir 6: P-08 "semua tiket di GLPI" lawan Zammad untuk Ops | Mengikuti premis owner: Zammad untuk Ops, Service Hub (GLPI) untuk generalist. Lihat cacat 5 |
| 13 | POL butir 8: definisi P1 memuat tuntutan komitmen komersial dan hal legal yang bukan kriteria ketersediaan | Definisi owner dipertahankan utuh di bagian 3 (suara tim, T1). Open item 12 |
| 14 | POL butir 3 dan butir 11: pemilik dokumen tidak konsisten (COO atau Head of Operation); Head of Operation sebagai pemilik POL-OPS-001 | Tidak relevan untuk SOP-04: sumber SOP-04 menulis Lead NOC dan itu yang dipakai. Open item 9 |
| 15 | POL butir 7 dan 10: rujukan DOCTRINE, SKILL_, om Ipe, WA owner | Tidak ada yang disalin. "om Ipe" diganti jabatan Manager of Product Tech, "CEO" diganti Direktur Utama (data_conflicts) |
| 16 | POL butir 13: matriks severity POL tidak memuat target pulih; angka hanya di SOP-04 | Tidak ada konflik; SOP-04 tetap satu-satunya dokumen dengan target pulih |
| 17 | PRO butir 2: RCA 2 hari kerja berlabel "(USULAN tenggat)" di NOC-02, tetapi SOP-04 dan FRM-10 menulisnya sebagai aturan | Sumber utama dipakai: 2 hari kerja tanpa label di bagian 8. Open item 18 |
| 18 | PRO butir 8: istilah "blok ukur", "blok ubah", "packet setor" ditandai artefak internal | "blok ukur read-only" ada di sumber SOP-04 sendiri dan bukan pola terlarang di RUNBOOK §0 butir 6, jadi dipertahankan dan didefinisikan di bagian 3. "blok ubah" dan "packet setor" tidak masuk |
| 19 | PRO butir 11: "10 menit" tiket berlaku untuk semua alert | Sejalan dengan SOP-04 (butir 6.1 langkah 3, bagian 8); tidak ada konflik |

Cacat tambahan yang saya temukan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | Rantai eskalasi P1 tidak menyebut Head of Operation, padahal peran sumber menjadikannya penanggung jawab P1 | Tidak diperbaiki diam-diam: rantai sumber (Lead NOC, COO, Direktur Utama) dipertahankan. Open item 2 |
| B | Sumber memakai dua rumusan untuk satu hal: "COO tidak tersedia" (tabel severity) dan "COO tidak dapat dihubungi" (matriks) | Disatukan menjadi "tidak dapat dihubungi" di seluruh dokumen |
| C | Tabel severity memakai "Lead" tanpa keterangan | Ditulis "Lead NOC" (satu-satunya Lead di tabel peran sumber). Asumsi 2 |
| D | Sumber SOP-04 memuat delapan kelas triage tanpa kelas keamanan; dropdown Kelas triage di FRM-08 memuat sembilan nilai termasuk "Keamanan (ke SOC)" dan "Backup atau snapshot" | Butir 6.2 langkah 4 memakai "backup atau snapshot" (sama dengan FRM-08 dan PRO-OPS-001); langkah 5 menambahkan pemilihan kelas Keamanan (ke SOC) di FRM-08 saat insiden diserahkan ke SOC. Open item 11 |
| E | Penomoran bagian SOP-04 berubah setelah dipindah ke template. Spec OPS-FRM-10 merujuk "SNX-OPS-SOP-04 Bagian 4", "Bagian 6", "Bagian 7.5" dan "Bagian 7.5 butir 3" | Tidak bisa diperbaiki dari sini (di luar batas tulis). Pemetaan baru di open item 1 |
| F | Sumber tidak menyebut pelaku untuk banyak kalimat pasif (RCA dikirim, tindakan korektif dicatat dan dipantau, status disampaikan, eskalasi fungsional) | Pelaku diberikan dari tabel peran; lihat asumsi 3 sampai 8. Tidak ada kontrol pengganti yang ditambahkan |

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Nama peran bagian 5 mengikuti specs/HR-ORG-01.json: NOC Engineer, Lead NOC, SOC Analyst, Head of Operation, Service Delivery Manager ada di daftar jabatan Divisi Operation. "NOC Engineer (on-duty)" ditulis NOC Engineer dengan "Saat on-duty" di kolom tanggung jawab. "COO" dipetakan ke Direktur (COO, JA-02) dan "CEO" ke Direktur Utama (JA-01) menurut data_conflicts. Tiga peran penerima eskalasi tidak ada di sumber sebagai jabatan dan dipetakan ke jabatan terdekat di HR-ORG-01: "Commercial" ke VP Commercial (JA-03; POL-OPS-001 menulis Laras sebagai tujuan harga, quote, kontrak), "Tech dan Product" ke Manager of Product Tech (JA-05; POL-OPS-001 menaruh "om Ipe (Tech dan Product)" pada baris yang sama), "PIC proyek" ke Project Manager (jabatan Divisi Operation di HR-ORG-01). Ketiganya berlabel USULAN di tabel peran (U5 sampai U7).
2. "Lead" di tabel severity sumber dibaca Lead NOC: tabel peran sumber hanya memuat Lead NOC, dan SOP ini untuk insiden teknis. Lead SOC tidak muncul di SOP ini.
3. Pelaku langkah deteksi, pencatatan, triage, serah, diagnosa, pemulihan, update berkala, verifikasi, penutupan, pengisian FRM-08, dan eskalasi fungsional dibaca NOC Engineer, karena sumber menulis tanggung jawab itu pada NOC Engineer (on-duty) dan "Eskalasi bila target terlewat atau butuh pihak lain" ada di tahap yang NOC jalankan. Eskalasi fungsional ke partner SOC dan ke Nusametric juga dibaca NOC Engineer; bila SOC Analyst sudah memegang insiden, pelakunya bisa berbeda (open item 2 mencakup rantai eskalasi).
4. Pemberi tahu COO dan Direktur Utama pada P1 dibaca Lead NOC, mengikuti urutan sumber "Lead langsung, COO dalam 30 menit, CEO bila COO tidak tersedia". Sumber tidak menyebut pelakunya.
5. Pengiriman RCA ke pelanggan oleh Head of Operation (menyetujui dan mengirim) berasal dari form tim FRM-10; "memastikan RCA terkirim" oleh Service Delivery Manager berasal dari SOP-04. Keduanya dimuat (butir 6.5 langkah 4 sampai 6). Email pulih untuk P1 dan P2 oleh Service Delivery Manager dibaca dari "Komunikasi formal ke pelanggan untuk P1 dan P2".
6. Tindakan korektif dicatat oleh Lead NOC (FRM-10: Lead NOC atau Lead SOC mengisi bagian Tindakan) dan dipantau oleh Head of Operation ("Penanggung jawab P1 sampai RCA selesai"). Penetapan insiden berulang sebagai problem oleh Lead NOC adalah tafsir; sumber tidak menyebut pelaku maupun data hitungnya.
7. Kolom Authority bagian 5 tidak ada di sumber. Isinya diturunkan dari kalimat sumber dan langkah yang diberikan ke peran itu (mis. NOC Engineer menetapkan severity karena langkah "Tetapkan severity" ada pada triage). Kolom COO, Direktur Utama, dan tiga penerima eskalasi paling tipis.
8. Langkah "COO memutuskan komitmen baru bila P1 menuntutnya" (butir 6.6 langkah 6) dibuat dari kalimat peran COO. Sumber tidak menyebut tempat mencatat keputusan itu; kolom rekaman hanya "Keputusan COO".
9. Isi kolom rekaman "Kolom Eskalasi ke di SNX-OPS-FRM-08" memakai kolom N register FRM-08 (teks bebas). Sumber SOP-04 tidak menyebut tempat mencatat eskalasi.
10. Definisi baru yang bukan kalimat tim: Blok ukur (dari pemakaian di PRO-OPS-001 CHG-01), App-level pelanggan dan Vantage eksternal (dari POL-OPS-001 P-05 dan P-09, termasuk contoh dan "127.0.0.1"), Mean time to restore, Kelas triage, Severity, Status SLA, Target pulih, Eskalasi fungsional dan hierarki, Insiden berulang (dari angka sumber butir 7.5), Tindakan korektif (dari definisi Korektif di FRM-10), RCA, NOC dan SOC (dari HR-ORG-01), (USULAN) (dari HR-ORG-01).
11. Nama klausul ISO di bagian 11 dan di label bagian 4 diambil dari teks standar (ISO 9001:2015 8.5.1, 8.7, 10.2; ISO/IEC 27001:2022 Annex A 5.24, 5.26, 8.16), bukan dari sumber tim. Sumber tim hanya memberi nomor, dan "8.7 (output tidak sesuai)".
12. Keputusan "Waktu Ack dan pulih dihitung dari waktu Dilaporkan" dibaca dari rumus register FRM-08 (kolom S dan T), dokumen tim yang sama-sama berstatus Draft.
13. Tenggat RCA 2 hari kerja dan KPI 95%, 100%, 90% dipakai pada lingkup sumbernya (RCA insiden P1 dan P2; Ack P1 dan P2; RCA P1 dan P2; tindakan korektif). Tidak diperluas ke problem dari insiden berulang atau ke severity lain.
14. Baris Indikator di bagian 8 dipegang Lead NOC (pemilik SOP) atau Head of Operation menurut peran yang bertanggung jawab atas aktivitasnya; sumber tidak menyebut pemantau indikator. Kalimat penutup "Lead NOC memantau kepatuhan" adalah tafsir yang sama.
15. Pemilik rekaman diambil dari "Pemilik dokumen" tiap form (FRM-08 Lead NOC; FRM-10 Head of Operation; FRM-04 Head of Operation; ISMS-FRM-02 Lead SOC), bukan dari SOP-04. Lokasi "Folder Drive Operation" tanpa sumber (USULAN U8), diselaraskan dengan baris FRM-10 yang sudah ada.
16. Kata "tidak merespons" (sumber "tidak merespon") dan "mengonfirmasi" memakai ejaan baku; "mengeskalasi" mengikuti kalimat tujuan sumber.
17. Perubahan terhadap kalimat tim hanya untuk ejaan, pelaku, atau membuang rujukan internal. Kalimat tujuan, kalimat lingkup butir 1, definisi lima istilah, definisi P1 sampai P4, dan semua angka tabel severity dipertahankan.

## USULAN

Lint menghitung 9 label "(USULAN)" di dokumen. Sembilan butir di bawah adalah butir unik; beberapa muncul di lebih dari satu sel.

| # | USULAN | Di mana | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Waktu Dilaporkan untuk insiden dari monitoring = waktu alert terkonfirmasi | Bagian 3 (Waktu Dilaporkan) | Menutup cacat "titik awal hitung Ack tidak didefinisikan"; sumber hanya punya "Dilaporkan" untuk laporan pelanggan | Fani |
| U2 | Batas 30 menit pemberitahuan COO untuk P1 dihitung dari waktu Dilaporkan | Bagian 4, bagian 8 | Angka 30 menit dari sumber; titik awalnya tidak. SOP-02 memakai "sejak eksekusi" untuk change Emergency | Fani, COO |
| U3 | Target pulih P1 4 jam, P2 8 jam, P3 24 jam, P4 72 jam | Bagian 8 | Label USULAN dari sumber dan dari FRM-08; belum diputus pimpinan | Fani, COO |
| U4 | Zammad untuk laporan WhatsApp, telepon, email; Service Hub (GLPI) untuk laporan GMF dan internal | Butir 6.1 (intro) | Premis owner "zammad untuk ops, glpi untuk generalist"; batas "generalist" belum dirinci. Sumber SOP-04 menulis pembagian GMF dan internal | Owner |
| U5 | Commercial dipetakan ke VP Commercial | Bagian 5 | Sumber menulis fungsi, bukan jabatan | Fani |
| U6 | Tech dan Product dipetakan ke Manager of Product Tech | Bagian 5 | Sumber menulis fungsi, bukan jabatan | Fani |
| U7 | PIC proyek dipetakan ke Project Manager | Bagian 5 | Sumber menulis "PIC proyek" tanpa jabatan; bisa juga merujuk PIC pihak pelanggan | Fani |
| U8 | Lokasi rekaman: Folder Drive Operation (FRM-10 dengan subfolder per tahun) untuk FRM-08, FRM-10, ISMS-FRM-02, FRM-04 | Bagian 11, tabel Rekaman | Sumber hanya memberi nomor dan masa simpan; baris FRM-10 mengikuti spec OPS-FRM-10 | Fani |
| U9 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Lead NOC, ISO/ISMS Coordinator, COO. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: dokumen operasional disetujui COO bila owner memutus | Blok Approval | Defaults (D2) mengalahkan sumber | Owner, Samuel |

## Open items

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Rujukan bagian SOP-04 di spec OPS-FRM-10 basi sesudah SOP-04 dirender ke 11 bagian. Pemetaan: definisi insiden "Bagian 4" menjadi bagian 3; severity "Bagian 6" menjadi definisi di bagian 3 dan target di bagian 8; kewajiban RCA "Bagian 7.5" menjadi bagian 4 dan butir 6.5; insiden berulang "Bagian 7.5 butir 3" menjadi definisi di bagian 3 dan aturan di bagian 4 (baris 30, 44, 45, 46, 248 specs/OPS-FRM-10.json). Spec OPS-SOP-03 sudah merujuk SOP-04 tanpa nomor bagian dan tetap benar | LEAD ISO |
| 2 | Rantai eskalasi P1 sumber tidak menyebut Head of Operation (penanggung jawab P1), tidak menyebut pelaku pemberitahuan ke COO dan Direktur Utama, dan tidak menyebut kapan Head of Operation memanggil personel off-duty. Dokumen memakai Lead NOC sebagai pemberi tahu dan tidak menambah langkah pemanggilan | Fani |
| 3 | Pengirim RCA: SOP-04 menulis Service Delivery Manager "memastikan RCA terkirim"; FRM-10 menulis Head of Operation menyetujui dan mengirim. Dokumen memuat keduanya. Perlu satu rumusan | Fani |
| 4 | Titik awal 30 menit COO untuk P1 insiden (USULAN) berbeda dari SOP-02, yang menghitung 30 menit sejak eksekusi change Emergency. Hubungan target pulih 4 jam dengan anggaran downtime 99.9% di SOP-05 juga belum dijelaskan | Fani |
| 5 | Ack P3 "2 jam kerja" dan P4 "1 hari kerja": kalender kerja belum ditetapkan; FRM-08 menghitung jam kalender (ML-00 riwayat review no. 10, status Terbuka, kutipan dari salinan audit) | Fani |
| 6 | Batas Zammad lawan Service Hub: sumber SOP-04 membagi menurut pelanggan (GMF dan internal ke Service Hub); premis owner membagi Ops lawan generalist. Belum jelas apakah insiden teknis GMF masuk Zammad atau Service Hub | Owner |
| 7 | Retensi tiket asal di Zammad dan Service Hub tidak ditetapkan sumber; hanya register FRM-08 (3 tahun) dan form lain yang punya masa simpan | Fani |
| 8 | Penyetuju: sumber COO (Amirull Yusuf Zulkarnain); template dan defaults Samuel Kristanto Utomo. Defaults dipakai. Samuel sebagai penyetuju untuk SOP operasional perlu konfirmasi | Owner, Samuel |
| 9 | Pemilik dokumen "Lead NOC" dan peran Head of Operation belum punya pemegang nyata di HR-ORG-01 (K-10). Reviewer Fani Fatullah = VP Tech Operation and Services, bukan Head of Operation | Fani, COO |
| 10 | Password manager (vault): status "menunggu konfirmasi Ops" ditulis di definisi. Aturan kredensial pelanggan lewat password manager baru dapat dipatuhi bila vault aktif | Ops |
| 11 | Kelas triage: SOP memuat delapan kelas, dropdown FRM-08 memuat sembilan (tambahan "Keamanan (ke SOC)"). Dokumen memakai delapan kelas plus pemilihan kelas Keamanan di FRM-08 saat insiden diserahkan ke SOC; perlu konfirmasi bahwa itu cara pakai yang dimaksud | Fani |
| 12 | Definisi P1 dari owner memuat "berkepanjangan" dan "jalur vendor buntu" tanpa ambang waktu atau kriteria, serta tuntutan komitmen komersial dan hal legal yang bukan kriteria teknis. Dipertahankan utuh | Owner |
| 13 | Penanganan bila pelanggan tidak mengonfirmasi pemulihan (butir 6.4 langkah 2) tidak ada di sumber; tidak ada batas waktu tunggu atau penutupan otomatis | Fani |
| 14 | Mean time to restore P1 "Dikalibrasi setelah 3 bulan data": belum jelas mulai dari tanggal efektif atau dari data FRM-08 yang ada, siapa menghitung, dan dari sumber data apa. Tiga indikator lain di bagian 8 juga tanpa sumber data (kecuali Ack 95%, yang dihitung di sheet Ringkasan FRM-08) | Fani |
| 15 | Insiden berulang: sumber tidak menyebut siapa menghitung 3 kali dalam 30 hari dan dari data mana, apakah RCA problem dikirim ke pelanggan, dan kapan. Dokumen memakai Lead NOC untuk penetapan problem dan menulis pengiriman RCA hanya untuk P1 dan P2 | Fani |
| 16 | Pelaksanaan service request tidak diatur di SOP ini. PRO-OPS-001 NOC-03 (bahan saja) memuat prosedurnya, tetapi belum ada dokumen SNX bernomor | Fani |
| 17 | Lingkup "layanan yang dikelola SINUX" tanpa daftar layanan; POL-OPS-001 bagian 2 (bahan) memuat daftarnya, belum menjadi dokumen resmi | Fani |
| 18 | RCA 2 hari kerja: SOP-04 dan FRM-10 menulisnya sebagai aturan, PRO-OPS-001 NOC-02 menandainya "(USULAN tenggat)". Dokumen ini tanpa label | Fani |
| 19 | Berkas kontak PIC eksternal tidak punya nomor atau nama berkas yang bisa dirujuk; sumber hanya menyebut "file kontak restricted:ops" | Fani |
| 20 | Nama klausul ISO (9001 8.5.1, 8.7, 10.2; 27001 5.24, 5.26, 8.16) dan pemetaannya ke bagian 4 perlu dicocokkan dengan SoA yang disusun konsultan | Konsultan SoA |
| 21 | Kalimat perintah di isi sumber: tidak ada kalimat perintah kepada pembaca AI di tiga sumber (hanya kalimat prosedur untuk pelaksana). Tidak ada yang dijalankan atau dicatat sebagai tindakan | Nihil |

## Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Pada draf pertama saya temukan dan perbaiki hal berikut: (a) pembuka bagian 4 "Setiap insiden dicatat, dipulihkan, lalu insiden P1 dan P2 wajib RCA" mengulang aturan RCA yang ada tiga baris di bawahnya, dihapus; (b) kalimat "peran, severity, kelas triage, dan matriks eskalasi ditetapkan sebelum insiden terjadi" berbunyi seperti prinsip umum yang bisa ditempel ke perusahaan mana pun, diganti penunjuk bagian yang konkret; (c) "dari pencatatan sampai penutupan tiket" terbaca seperti rentang retoris, diganti "butir 6.1 sampai 6.4"; (d) dua kalimat penutup menyebut "Lead NOC" berturut-turut, digabung menjadi satu kalimat; (e) kalimat meta "sesudah baris ini dokumen ini menulis COO" diganti kalimat biasa; (f) "mengeskalasikan" dan "mengeskalasi" bercampur, disatukan; (g) kalimat "Service request dicatat sebagai P4" ada di bagian 2 dan bagian 9, kini hanya di bagian 9; (h) definisi Eskalasi hierarki memuat "menurut" dua kali berturut-turut, dirapikan; (i) berkas kontak PIC eksternal pada draf pertama ditulis "berklasifikasi RESTRICTED (Internal)", padahal sumber hanya menulis label KB "restricted:ops" dan tidak menyebut tingkat klasifikasi, diganti "aksesnya dibatasi untuk Operation"; (j) label Annex A 8.16 pada draf pertama hanya menempel pada aturan frasa "dari pantauan kami", padahal kontrol itu tentang pemantauan, kini mencakup pemantauan dan konfirmasi alert. Sejak draf pertama sudah saya hindari: definisi yang saling menunjuk (Service request dan P4), kata "Lead" tanpa NOC atau SOC, "CEO" (diganti Direktur Utama), dan tanda pisah panjang. Yang masih terdengar mesin dan saya biarkan: pola "Label (klausul): isi" pada enam butir bagian 4 (kontrol ISO wajib tercermin di sana dan pola sama dipakai SNX-ISMS-SOP-02), kolom rekaman "Kolom Eskalasi ke di SNX-OPS-FRM-08" yang berulang delapan kali di butir 6.6 (rekamannya memang sama), dan rujukan silang "butir 6.x" yang rapat karena aturan satu fakta satu tempat.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa satu per satu terhadap dokumen jadi. Angka (10 menit, 15 menit, 30 menit, 2 jam kerja, 1 hari kerja, 1 jam, 3 jam, 4/8/24/72 jam, 2 hari kerja, 3 kali dalam 30 hari, 95%, 100%, 90%, 3 bulan, 3 tahun, 5 tahun, 24 jam sehari 7 hari seminggu) semuanya dari sumber SOP-04; "127.0.0.1" dari POL-OPS-001 P-09. Nama orang hanya tiga di blok Approval (defaults.json). Nama sistem dan pihak luar (Nusametric, Overseer, Nusagrid, Acronis, Cloudflare, Zammad, Service Hub, GLPI, Maxcloud, Awandata, Arktech, TelemetryFlow, GMF) dari sumber. Tanggal: tidak ada yang ditulis di dokumen; Effective Date kosong. Butir tanpa sumber SOP-04 yang tertulis di dokumen: titik awal waktu Dilaporkan untuk monitoring dan batas 30 menit COO (U1, U2), lokasi rekaman (U8), pemetaan tiga peran (U5 sampai U7), pemilik rekaman (dari form tim, asumsi 15), pengirim RCA Head of Operation (dari FRM-10, asumsi 5), nama klausul ISO (dari standar, asumsi 11), definisi baru (asumsi 10). Setiap butir itu berlabel USULAN di dokumen atau dicatat sebagai asumsi dan open item di atas. Tidak ada koreksi tambahan setelah pemeriksaan ini.
