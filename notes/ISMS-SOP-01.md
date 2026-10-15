# Catatan penyusun ISMS-SOP-01: SOP Information Security Incident Management

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-SOP-01.json. Mode sop, aksi T1, wave W2, nomor SNX-ISMS-SOP-01 (nomor lama dipertahankan), department Operation (label ISMS di defaults; sumber menulis "Information Security"), classification RESTRICTED (Internal) mengikuti label sumber, audit_class C2, process_owner "Lead SOC" (jabatan, tanpa nama; sama dengan "Pemilik dokumen" sumber). Judul di spec "Information Security Incident Management" karena template menambah "SOP" sendiri ("Operation - SOP Information Security Incident Management").

Hasil uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-SOP-01.json /tmp/pen-ISMS-SOP-01/ISMS-SOP-01.docx`
- `python3 -I tools/lint_doc.py /tmp/pen-ISMS-SOP-01/ISMS-SOP-01.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "5 butir (USULAN) menunggu ACC" (warn PIC SLA: nol).
- Validator OOXML skill docx (`/mnt/skills/public/docx/scripts/office/validate.py`) atas hasil render: "All validations PASSED!".
- PDF soffice 19 halaman; halaman 15 (diagram) dilihat. Diagram TB 13 simpul, 1095 x 2011 px; teks diagram kecil tetapi terbaca. Dokumen pertama wave perlu pratinjau montase oleh orkestrator (RUNBOOK §5 butir 6).
- Pindai mesin sekali pakai (skrip python tidak disimpan): em-dash dan en-dash 0; kode dokumen di badan yang tidak ada di tabel Dokumen terkait 0; semua PIC langkah dan SLA ada di tabel peran bagian 5; langkah terpanjang di bawah 28 kata (53 langkah).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-SOP-01_SOP_IS_Incident_Management.docx (194046 byte) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 | 2026-10-13T06:09:00Z (get_file_metadata hari ini, cocok dengan prompt) | read_file_content (teks); download_file_content didekode ke /tmp/pen-ISMS-SOP-01/ (zip dibuka dengan python3 -I); header, footer, comments.xml, footnotes.xml dibaca (comments dan footnotes kosong); gambar word/media/rId25.png dibuka |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, cocok) | read_file_content; bahan pendukung saja |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte) | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, cocok) | read_file_content; bahan pendukung saja |
| Kriteria penerimaan | prompt penyusun, baris data | Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "10.2" dan ISO/IEC 27001:2022 "5.24, 5.25, 5.26, 5.27, 5.28, 6.8" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md bagian isms/SNX-ISMS-SOP-01 (bagian 5); context/audit/iso-sinux-supdocs-ops-2026-10-14.md bagian POL-OPS-001 dan PRO-OPS-001 (bagian 5) | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; butir dicocokkan ulang ke teks sumber |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json, specs/OPS-SOP-04.json, specs/OPS-SOP-02.json, specs/OPS-FRM-10.json, specs/ISMS-SOP-02.json, notes/ISMS-FRM-02.md, patch ISMS-FRM-02, config/defaults.json | spec dan notes DONE | Untuk nama peran, judul dokumen terkait, istilah yang sama antardokumen |

Peringatan jujur: nama kolom Register, butir sheet Investigasi (2, 12, 13, 15), dan kolom Chain of Custody SNX-ISMS-FRM-02 diambil dari salinan audit (DATA) dan notes/ISMS-FRM-02.md, bukan dari xlsx Drive terbaru. Bila tim mengubah form itu, rujukan butir di bagian 6 bisa basi. SNX-ISMS-PLN-01, SNX-ISMS-REG-02, SNX-ISMS-REG-03, SNX-OPS-RPT-01 hanya dikenal lewat judul di salinan audit.

Kalimat perintah di isi sumber: tidak ada yang ditujukan ke penyusun. Satu-satunya bentuk perintah adalah isi prosedur untuk pembaca dokumen, dan itu dituangkan sebagai isi, bukan dijalankan.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Bila data pribadi terlibat, COO dan Legal memutuskan pemberitahuan ke subjek data dan lembaga berwenang, batas 3 x 24 jam sejak diketahui | "Bila insiden melibatkan kegagalan pelindungan data pribadi, COO dan Legal memutuskan pemberitahuan kepada subjek data dan lembaga berwenang sesuai UU PDP (paling lambat 3 x 24 jam sejak diketahui)." (Bagian 11 butir 2) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |
| 2 | Aturan forensik: bukti diamankan sebelum mengubah apa pun | "Forensik terlebih dahulu, perbaikan kemudian: amankan bukti (log, hash file, daftar proses, koneksi aktif, snapshot bila memungkinkan) sebelum mengubah apa pun." (Bagian 9 butir 1) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |
| 3 | Severity P1: kriteria, Ack 15 menit, pemberitahuan internal | "P1 \| Kompromi root atau host baru; kebocoran data pelanggan atau data pribadi; ransomware; akses tidak sah ke sistem kritis \| 15 menit \| Lead SOC dan Head of Operation segera; COO dalam 30 menit" (Bagian 8, tabel severity) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Posisi di spec |
|---|---|---|---|
| 1 | Lapor event paling lambat 1 jam | "Siapa pun yang melihat event keamanan (alert, perilaku aneh, laporan pelanggan, kredensial tersebar) melapor ke SOC on-duty melalui ticketing system atau kanal on-call, paling lambat 1 jam sejak mengetahui." (Bagian 7) | 6.2, SLA |
| 2 | Pemberitahuan pelanggan P1 24 jam, oleh Service Delivery Manager | "Pemberitahuan ke pelanggan mengikuti kontrak; untuk insiden P1, Service Delivery Manager memberi tahu PIC pelanggan paling lambat 24 jam dengan laporan awal." (Bagian 11 butir 1) | 6.6, SLA, bagian 5 |
| 3 | Severity P2 sampai P4 dan Ack | "P2 \| Kompromi terbatas tanpa bukti kebocoran data (misalnya webshell pada satu akun hosting, akun email dipakai spam); malware tertahan \| 30 menit \| Lead SOC dalam 1 jam"; "P3 ... 2 jam kerja ... Melalui tiket"; "P4 ... 1 hari kerja ... Melalui tiket" (Bagian 8) | Definisi, SLA |
| 4 | Satu insiden satu parent ticket, dicatat di FRM-02 | "Satu insiden = satu parent ticket; alert terkait ditautkan. Insiden dicatat di SNX-ISMS-FRM-02." (Bagian 8 butir 3) | 6.3, bagian 4 |
| 5 | Webshell tidak di-probe; quarantine dengan mv | "Webshell tidak pernah di-probe dengan GET atau HEAD, karena probe sama dengan eksekusi."; "File mencurigakan diquarantine dengan memindahkannya (mv) ke folder quarantine, bukan dihapus (rm)." (Bagian 9 butir 2 dan 3) | Bagian 4 |
| 6 | Dua sumber independen untuk klaim bersih | "Klaim “bersih” atau “aman” wajib didukung dua sumber independen (misalnya sweep hash dan pemeriksaan dari vantage eksternal)." (Bagian 9 butir 8) | Bagian 4, 6.4 |
| 7 | Containment dan darurat | "Containment mengikuti SNX-OPS-SOP-02; Lead SOC boleh menyatakan darurat dan langsung bertindak dengan pencatatan." (Bagian 9 butir 4) | Bagian 4, 6.4 |
| 8 | Bukti untuk proses hukum 5 tahun | "Bukti yang mungkin dibutuhkan untuk proses hukum disimpan minimal 5 tahun atau sesuai arahan Legal." (Bagian 10 butir 4) | 6.5, bagian 11 |
| 9 | RCA dan tindakan korektif P1 dan P2 | "Insiden P1 dan P2: RCA dengan SNX-OPS-FRM-10 dan tindakan korektif ber-pemilik dan ber-tenggat." (Bagian 12 butir 2) | Bagian 4, 6.7 |
| 10 | Pemilik dokumen, record, retensi | "Pemilik dokumen \| Lead SOC"; "Security Incident & Investigation Records (register, investigasi, chain of custody) \| SNX-ISMS-FRM-02 \| 5 tahun"; "Change request containment \| SNX-OPS-FRM-04 \| 3 tahun"; "Register risiko keamanan informasi \| SNX-ISMS-REG-02 \| Berlaku sampai digantikan" | meta, bagian 11 |
| 11 | Target kinerja | "Alert kritis di-triage dalam 15 menit \| 95%"; "Mean time to contain insiden P1 \| Dikalibrasi setelah 3 bulan data"; "Laporan insiden tepat waktu dan sesuai format \| 100%"; "Insiden berulang dengan akar yang sama \| Nol" (Bagian 14) | SLA, kolom Indikator |
| 12 | Persiapan | "Daftar kontak eskalasi internal dan eksternal (partner SOC, penyedia infrastruktur, pelanggan) dipelihara di file kontak restricted:ops dan ditinjau triwulanan."; "Latihan tabletop minimal setahun sekali, hasilnya dicatat sebagai bukti di SNX-ISMS-PLN-01." (Bagian 6) | 6.1 |
| 13 | Scope: pelanggan dengan SOC sendiri | "Untuk pelanggan yang SOC-nya menjadi tanggung jawab pelanggan sendiri (misalnya pelanggan pemerintah tertentu), SINUX menangani keamanan host yang dikelolanya sebagai managed services dan berkoordinasi dengan tim keamanan pelanggan." (Bagian 2) | Scope, pengecualian |
| 14 | Dari bahan pendukung: alasan quarantine, USULAN tenggat laporan, USULAN frekuensi update | PRO-OPS-001 SOC-02 (1U8CAdibwBk9x_-Aic2lbev144d6WReTz): "Karantina dengan mv ke folder karantina, bukan rm, agar bukti tetap utuh." SOC-03: "P1 keamanan: laporan awal ke pelanggan dalam 24 jam, laporan final setelah eradikasi. (USULAN tenggat)". POL-OPS-001 bagian 6 (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv): "Target Ack dan update di atas adalah USULAN internal." | Bagian 4, SLA |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 10.2 | Ya | Butir "Pembelajaran (Annex A 5.27) dan tindakan korektif (ISO 9001:2015 10.2)" | 6.7 langkah 4 sampai 6 |
| ISO/IEC 27001:2022 Annex A 5.24 | Ya | Butir Persiapan | 6.1 |
| 5.25 | Ya | Butir Penilaian dan keputusan | 6.3 |
| 5.26 | Ya | Butir Respons, webshell, quarantine, dua sumber independen, containment | 6.4 |
| 5.27 | Ya | Butir Pembelajaran | 6.7 |
| 5.28 | Ya | Butir Pengumpulan bukti | 6.5 |
| 6.8 | Ya | Butir Pelaporan event | 6.2 |

Nama klausul di bagian 11 (mis. "Penilaian dan keputusan atas event keamanan informasi") adalah terjemahan penyusun dari judul standar, bukan kalimat tim; gaya sama dengan SNX-OPS-SOP-04.

## 4. Keputusan data dan nama peran

- Approval persis dari prompt dan config/defaults.json: prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo. Sumber menulis Disusun "Lead SOC", Diperiksa "ISO/ISMS Coordinator", Disetujui "COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber (D2). USULAN 1.
- COO: di badan dokumen sebutan pertama "Direktur (COO)" ada di baris Definisi (sebelum itu tidak ada sebutan COO), sesudahnya "COO". Samuel tidak disebut di badan dokumen, jadi "Direktur Utama" tidak terpakai.
- Tiket: Zammad untuk Ops dan Service Hub (GLPI) untuk generalist, dengan batas berlabel USULAN (defaults.ticketing) di intro 6.2. Sumber hanya menulis "ticketing system".
- Vault: baris Definisi "Password manager" memuat "Status operasional: menunggu konfirmasi Ops", teks yang sama dengan SNX-OPS-SOP-04. Akses darurat on-call memakai password manager, jadi bergantung pada status itu (open item 7).
- Nama peran bagian 5 dipetakan ke specs/HR-ORG-01.json:

| Sebutan sumber | Nama peran di dokumen | Dasar |
|---|---|---|
| Lead SOC | Lead SOC | HR-ORG-01 Struktur Divisi Operation (USULAN, belum ada pemegang, K-10) |
| SOC Analyst | SOC Analyst | sama |
| NOC | NOC Engineer | Sumber memakai nama sub divisi sebagai peran ("Pemulihan availability, eksekusi perubahan, dukungan teknis"). Peran di HR-ORG-01 yang melakukan hal itu: NOC Engineer. Tafsir penyusun |
| Head of Operation | Head of Operation | HR-ORG-01 (USULAN, K-10, K-11) |
| Service Delivery Manager | Service Delivery Manager | HR-ORG-01. Tidak ada di tabel peran sumber; ditambahkan |
| ISMS Coordinator | ISMS Coordinator | HR-ORG-01 matriks peran: "Belum ditetapkan (K-13)" |
| COO dan Legal | COO dan Legal & Compliance (dua baris) | COO = Direktur (JA-02). "Legal" dipetakan ke jabatan JA-08 dan JA-09 "Legal & Compliance" |
| Seluruh personel | Seluruh personel | bukan jabatan; dipakai apa adanya |
| "ISO/ISMS Coordinator" (pemeriksa di Pengesahan sumber) | tidak dipakai | pemeriksa memakai defaults (Fani) |
| Incident Commander (di baris Lead SOC sumber) | dipertahankan sebagai penugasan Lead SOC, didefinisikan di bagian 3 | HR-ORG-01 tidak memuatnya karena penugasan per insiden, bukan jabatan (sama dengan catatan ISMS-FRM-02) |

## 5. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" SNX-ISMS-SOP-01 (fileId 1MApsp9R...):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Rujukan SNX-OPS-SOP-04 dan SNX-OPS-SOP-02 sudah cocok judulnya; "Lead SOC boleh menyatakan darurat" dianggap selaras dengan change Emergency (inferensi Lead SOC = Lead on-duty) | Diperkuat: SNX-OPS-SOP-02 versi spec repo menyebut Lead SOC eksplisit pada change Emergency SOC. Langkah 6.4 menunjuk SNX-OPS-SOP-02 untuk pencatatan; angka waktu SNX-OPS-SOP-02 tidak disalin |
| 2 | "SKILL_ir-report", "SKILL_incident-rca" bukan nomor dokumen QMS/ISMS; lima section tidak diuraikan | Dibuang (RUNBOOK §0 butir 6). Diganti "format laporan insiden baku" (sama dengan ISMS-FRM-02) dan SNX-OPS-FRM-10 untuk RCA. Frasa "lima section" tidak dibawa karena isinya tidak ada di korpus; open item 1 |
| 3 | Bagian 11 butir 3 tanpa batas waktu; BSSN tidak disebut | Tidak diperbaiki: sumber diam, angka tidak dikarang, BSSN tidak ditambahkan. Langkah pelaporan regulator dan aparat dipertahankan tanpa tenggat. Open item 4 |
| 4 | "frekuensi update severity" dirujuk tetapi tabel severity tidak memuatnya | Diperbaiki: baris SLA "Update status ke pelanggan terdampak" memakai nilai SNX-OPS-SOP-04 (P1 tiap 1 jam; P2 tiap 3 jam atau per shift; P3 harian; P4 saat selesai), berlabel USULAN karena memperluas angka tiket teknis ke insiden keamanan dan karena POL-OPS-001 menyebutnya USULAN internal. Pelaku SOC Analyst, USULAN 5 |
| 5 | Target MTTC P1 tidak ditetapkan | Dipertahankan: "Dikalibrasi setelah 3 bulan data". Istilah didefinisikan lewat kolom Jam ke containment FRM-02. Tidak ada angka dikarang |
| 6 | Ack P1 15 menit tanpa titik awal; tiket "10 menit setelah konfirmasi" di SNX-OPS-SOP-04 juga tanpa kaitan | Diperbaiki sebagian: titik awal "waktu deteksi" (kolom Waktu deteksi FRM-02), berlabel USULAN di bagian 4; penerima Ack berlabel USULAN di bagian 3. Angka 10 menit dari PRO-OPS-001 NOC-01 tidak disalin karena itu aturan NOC |
| 7 | Masa simpan header "Berlaku sampai digantikan" lawan tabel record 5 tahun, 3 tahun | Template tidak punya kolom header itu. Tabel record bagian 11 yang berlaku; "Berlaku sampai digantikan" tinggal pada REG-02 |
| 8 | Pengesahan kosong, riwayat revisi dua baris bertanggal sama | Teratasi template: satu baris Revision 00, Effective Date dan Signature kosong |
| 9 | "ISO/ISMS Coordinator" lawan "ISMS Coordinator" | Moot: pemeriksa memakai defaults; peran badan "ISMS Coordinator" |

Cacat yang ditemukan sendiri saat membaca sumber:

| # | Cacat | Penanganan |
|---|---|---|
| 10 | Service Delivery Manager dipakai di Bagian 11 tetapi tidak ada di tabel peran | Ditambahkan ke bagian 5 |
| 11 | Tabel peran: "Seluruh personel ... sesegera mungkin" lawan Bagian 7 "paling lambat 1 jam" | Diseragamkan ke 1 jam (angka sumber) |
| 12 | Tabel peran: COO dan Legal memutuskan pemberitahuan "pelanggan, regulator, aparat"; Bagian 11 menaruh pemberitahuan P1 ke pelanggan pada Service Delivery Manager menurut kontrak | Diselaraskan: pelanggan tidak termasuk keputusan COO dan Legal; keputusan mereka dibatasi subjek data, lembaga berwenang, regulator sektor, aparat. Tafsir penyusun, open item 10 |
| 13 | Daftar kolom Chain of Custody sumber ("pengumpul") tidak cocok dengan kolom form (Tindakan, Diserahkan oleh, Diterima oleh, Hash diverifikasi) | Langkah 6.5 memakai nama kolom form; langkah verifikasi hash tiap perpindahan ditambah dari catatan form ("diverifikasi setiap perpindahan") |
| 14 | "Lessons learned disetor ... melalui jalur staging" | Jalur staging dibuang (RUNBOOK §0 butir 6); langkah "Simpan lessons learned di knowledge base, tanpa kredensial". Open item 9 |
| 15 | Diagram sumber tidak memuat persiapan, batas lapor 1 jam, pemberitahuan pelanggan P1, pembelajaran | Diagram baru: batas 1 jam, cabang pemberitahuan pelanggan P1, dan pembaruan register risiko ditambah. Persiapan sengaja tidak digambar (bukan langkah dalam satu insiden, dan diagram sudah 13 simpul); diatur di butir 6.1 |
| 16 | "restricted:ops" (label sensitivitas KB) dipakai sebagai nama file kontak | Diganti "file kontak yang aksesnya dibatasi untuk Operation" (teks SNX-OPS-SOP-04) |
| 17 | "merespon" | "merespons" |

Cacat POL-OPS-001 dan PRO-OPS-001 (bagian 5 keduanya) yang relevan: rujukan internal AI tidak disalin; definisi P1 POL yang memuat butir komersial dan legal tidak dipakai (P1 mengikuti kriteria keamanan di sumber SOP-01); tenggat laporan awal 24 jam berstatus USULAN di PRO-OPS-001 SOC-03 tetapi tanpa label di SOP-01 (angka dipakai apa adanya karena sumber utama, dicatat di open item 2); konflik GLPI lawan Zammad ditangani lewat aturan tiket di atas.

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Pelaku langkah yang di sumber pasif atau tanpa pelaku: seluruh langkah Persiapan (Lead SOC, pemilik SOP); laporan insiden disusun SOC Analyst, di-review Lead SOC (sumber), dikirim Service Delivery Manager; RCA disusun Lead SOC dan disetujui Head of Operation (dari "Disusun (Lead NOC atau Lead SOC)" dan "Disetujui (Head of Operation)" di SNX-OPS-FRM-10); tindakan korektif dicatat Lead SOC; statistik bulanan dan lessons learned oleh Lead SOC; pemberitahuan COO untuk P1 oleh Head of Operation (peran "komunikasi ke manajemen"); pemberitahuan data pribadi terlibat ke COO dan Legal oleh Head of Operation; pencatatan keputusan pemberitahuan di butir 15 sheet Investigasi oleh SOC Analyst; update status ke pelanggan oleh SOC Analyst (sejajar NOC Engineer di SNX-OPS-SOP-04).
2. Eradication: SOC Analyst menghapus persistence; NOC Engineer menutup vektor masuk dan memulihkan dari backup (dari peran "NOC" di sumber: pemulihan availability dan eksekusi perubahan; PRO-OPS-001 SOC-02: "Eradikasi dan pemulihan dikoordinasikan dengan NOC").
3. Severity ditetapkan SOC Analyst: sumber menulis "Event yang terkonfirmasi menjadi insiden dan diberi severity" tanpa pelaku; PRO-OPS-001 SOC-01 menaruh triage dan severity pada SOC Analyst.
4. "SOC on-duty" dibaca SOC Analyst yang bertugas.
5. Kolom Authority tabel peran tidak ada di sumber; diturunkan dari kalimat sumber dan form (mis. "boleh menyatakan darurat", approval change request).
6. Definisi umum (Playbook, Tabletop, Lessons learned, PIC pelanggan, Sweep IOC, Triage, Parent ticket, Incident Commander, Insiden berulang, Eradication) adalah penjelasan penyusun, bukan kalimat tim. "App-level pelanggan", "Vantage eksternal", "Zammad", "Service Hub", "Jumphost" disalin dari definisi spec saudara (SNX-OPS-SOP-04, SNX-ISMS-SOP-02).
7. "Tim investigasi" didefinisikan dari butir sheet Investigasi FRM-02; siapa yang menetapkan anggotanya tidak ditulis siapa pun.
8. Lokasi rekaman FRM-02, FRM-10, FRM-04 "Folder Drive Operation" dan REG-02 "Google Drive" mengikuti spec saudara; sumber SOP-01 hanya memberi nomor dan masa simpan. Pemilik rekaman: Lead SOC (FRM-02, dari "Pemilik dokumen" FRM-02), Head of Operation (FRM-10, FRM-04, dari spec saudara), ISMS Coordinator (REG-02, dari notes REG-02).
9. "Review tiap tahun" dalam Kesimpulan berasal dari review_period YEARLY di defaults; pelakunya pemilik SOP.
10. Tabel Severity di sumber memakai kolom Ack dan "Pemberitahuan internal"; Ack dibaca sebagai pengakuan di tiket oleh SOC Analyst (USULAN 3). P1 sampai P4 untuk insiden keamanan dan P1 sampai P4 insiden teknis (SNX-OPS-SOP-04) dibaca sebagai skala yang sama dengan kriteria berbeda; definisi P1 sampai P4 di dokumen ini hanya untuk insiden keamanan.

## USULAN

Label (USULAN) tercetak di dokumen pada butir 2 sampai 7. Butir 1 adalah data defaults di blok Approval (tanpa label di teks, sama dengan dokumen saudara); butir 8 dan 9 berupa tafsir pelaku dan nama peran, tidak berlabel di teks.

| # | Butir | Letak | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Penyusun Erik Dwi Yanto, pemeriksa Fani Fatullah, penyetuju Samuel Kristanto Utomo menggantikan "Lead SOC", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" di sumber (defaults D2; pembalik: form operasional disetujui COO bila owner memutuskan) | Blok Approval | owner |
| 2 | Waktu deteksi sebagai titik awal Ack, pemberitahuan COO 30 menit, Lead SOC 1 jam (P2), dan pemberitahuan pelanggan P1 24 jam | Bagian 4, 8 | Fani |
| 3 | Ack berarti pengakuan SOC Analyst di tiket (sumber tidak menyebut penerima Ack: tiket atau pelanggan) | Bagian 3 | Fani |
| 4 | Batas Zammad (personel Operation) lawan Service Hub (personel lain) untuk melapor event | 6.2 intro | owner |
| 5 | Frekuensi update ke pelanggan terdampak disalin dari SNX-OPS-SOP-04 dan dipakai untuk insiden keamanan | Bagian 8 | Fani |
| 6 | Lokasi rekaman FRM-02, FRM-10, FRM-04 di Folder Drive Operation | Bagian 11 | Fani |
| 7 | Pemilik Lead SOC dan lokasi "RESTRICTED (Internal)" untuk bukti insiden (sumber hanya menulis "lokasi RESTRICTED") | Bagian 11, 6.5 | Fani, Lead SOC |
| 8 | Penugasan pelaku pada langkah yang di sumber tanpa pelaku (daftar di bagian 6 butir 1 dan 2) | Bagian 5, 6 | Fani |
| 9 | Pemetaan peran: NOC menjadi NOC Engineer; Legal menjadi Legal & Compliance; pelanggan dikeluarkan dari keputusan COO dan Legal | Bagian 5 | Fani, owner |

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Format laporan insiden baku (sumber: "lima section dengan urutan tetap") tidak punya nomor SNX dan isinya tidak ada di korpus. Bagian 6.7 menyebut "format laporan insiden baku" tanpa rujukan | Fani |
| 2 | Tidak ada tenggat untuk laporan insiden akhir dan RCA insiden keamanan. PRO-OPS-001 menulis laporan final "setelah eradikasi" dan RCA "2 hari kerja" sebagai USULAN untuk jalur NOC. KPI "Laporan insiden tepat waktu" belum punya ukuran tepat waktu. Tenggat 24 jam laporan awal pelanggan di sumber SOP-01 berstatus USULAN di PRO-OPS-001 | Fani, COO |
| 3 | Titik awal 3 x 24 jam: sumber "sejak diketahui"; form SNX-ISMS-FRM-02 menghitung dari waktu deteksi (rumus kolom Notifikasi PDP). Dokumen memakai "sejak diketahui" dan tidak mendefinisikannya | Legal |
| 4 | Tidak ada batas waktu pelaporan ke regulator sektor atau aparat; BSSN tidak disebut sama sekali di sumber | Legal |
| 5 | Bila COO tidak dapat dihubungi saat insiden P1: sumber diam. POL-OPS-001 bagian 6 memuat eskalasi ke CEO (di dokumen ini: Direktur Utama), SNX-OPS-SOP-04 punya baris pengecualian serupa. Belum ditambahkan ke dokumen ini | owner, Samuel |
| 6 | Pelaku langkah Persiapan tidak ada di sumber (Lead SOC dipakai); siapa memberi akses darurat on-call juga tidak jelas (akses diatur SNX-ISMS-SOP-02) | Fani |
| 7 | Status password manager (vault) "menunggu konfirmasi Ops"; akses darurat on-call bergantung padanya | Ops |
| 8 | Istilah tanpa definisi di sumber: "alert kritis", "sistem kritis", "host baru" (P1), "tepat waktu". Dokumen memakai kata sumber apa adanya | Fani |
| 9 | Cara lessons learned masuk ke knowledge base: jalur lama (staging) dibuang dan belum ada pengganti bernomor SNX | Fani |
| 10 | Peran pemberi keputusan notifikasi pelanggan (tabel peran sumber lawan Bagian 11) dan siapa mengirim laporan insiden ke pelanggan (sumber hanya "dikirim") perlu konfirmasi | Fani |
| 11 | Retensi tiket insiden (parent ticket) dan laporan insiden tidak ditetapkan di sumber; tidak ada baris rekaman untuk keduanya di bagian 11 | Fani |
| 12 | Bentuk kanal on-call dan lokasi file kontak eskalasi tidak disebut sumber | Ops |
| 13 | Lead SOC, Head of Operation, ISMS Coordinator belum punya pemegang (HR-ORG-01 K-10, K-13); Incident Commander bukan jabatan | owner |
| 14 | Rujukan butir sheet Investigasi (2, 12, 13, 15) dan kolom Register berasal dari salinan audit; verifikator perlu mencocokkan dengan xlsx FRM-02 Drive terbaru (diubah W9: rujukan butir sheet Investigasi diganti label butir; kolom Register tetap perlu dicocokkan) | LEAD ISO |
| 15 | Tanggal draft 13 Oktober 2026 di sumber tidak dibawa ke dokumen (template memakai Effective Date kosong); tanggal efektif dan tanda tangan kosong sampai pengesahan | owner |

## 7. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI? Hasil pemeriksaan draf pertama, dan perbaikannya:

1. Kosakata ruang kerja penyusun bocor ke dokumen: "sumber tidak menyebut titik awal", "belum dirinci owner", "menurut sumber". Auditor tidak tahu "sumber" yang dimaksud. Diganti "titik awal belum ditetapkan", "belum diputus pimpinan SINUX"; kalimat "menurut sumber" dihapus.
2. Frasa kabur yang lahir dari menyalin pola: "pihak luar yang sama" (baris Legal & Compliance) dan "Sistem terpulihkan". Diganti rujukan butir 6.6 dan "Sistem dipulihkan".
3. Bentuk kalimat yang berulang: empat langkah "Beri tahu ... tentang insiden P1 atau P2" dan banyak keluaran berbentuk "... di tiket". Dipertahankan karena tiap langkah beda pelaku atau penerima dan prosedur memang berulang; tidak digabung agar satu langkah tetap satu pelaku.
4. Kelompok tiga yang dipaksakan: tidak ada yang ditambahkan penyusun. Daftar lima kata kerja di Tujuan dan daftar empat butir Persiapan adalah susunan tim dan tetap. Kalimat tim yang jelas (forensik terlebih dahulu, webshell tidak di-probe) dipertahankan.
5. Pemindaian pola (kalimat pengisi, ekor penegas, penutup generik, atribusi kabur, tebal atau kapital untuk penekanan, em-dash dan en-dash, lindung nilai bertumpuk): nol temuan pada teks akhir. Kapital yang ada adalah nama sistem, nama tingkat klasifikasi, dan singkatan. Istilah English (triage, containment, eradication, parent ticket, playbook, backup) adalah sebutan kerja tim dan tidak diterjemahkan.
6. Kesimpulan satu kalimat, tanpa pujian, memuat pelaku dan frekuensi tinjauan.

Adakah fakta, angka, nama, atau tanggal tanpa sumber? Hasil pemeriksaan teks akhir:

| Butir di dokumen | Sumber |
|---|---|
| 1 jam, 15 menit, 30 menit, 2 jam kerja, 1 hari kerja, 24 jam, 3 x 24 jam, 5 tahun, 3 tahun, triwulan, setahun, 95%, 100%, nol, 3 bulan | Sumber SOP-01 (Bagian 6 sampai 14) |
| Update ke pelanggan P1 tiap 1 jam, P2 tiap 3 jam atau per shift, P3 harian, P4 saat selesai | SNX-OPS-SOP-04 dan POL-OPS-001 bagian 6; berlabel USULAN |
| Waktu deteksi sebagai titik awal; Ack di tiket | Tidak ada di sumber; berlabel USULAN (USULAN 2 dan 3) |
| Zammad untuk Ops, Service Hub untuk generalist | config/defaults.json ticketing; batas berlabel USULAN |
| Nama kolom dan butir FRM-02 (Data pribadi terlibat, Waktu deteksi, Jam ke containment, Hash diverifikasi, Diserahkan oleh, Diterima oleh; butir 2, 12, 13, 15) | Salinan audit FRM-02 dan notes/ISMS-FRM-02.md (DATA, tidak dicek ke xlsx Drive); open item 14 |
| RCA disusun Lead SOC dan disetujui Head of Operation | specs/OPS-FRM-10.json dan notes OPS-FRM-10 (kutipan "Disusun (Lead NOC atau Lead SOC)", "Disetujui (Head of Operation)") |
| Judul SNX-ISMS-PLN-01, REG-02, REG-03, OPS-RPT-01, ISMS-PRO-01 | Salinan audit korpus ISMS dan Ops |
| Judul dan nama klausul Annex A 5.24 sampai 6.8, ISO 9001:2015 10.2 | Standar; terjemahan penyusun |
| "agar bukti tetap utuh" | PRO-OPS-001 SOC-02 |
| Daftar lima skenario playbook | Sumber SOP-01 Bagian 6 butir 3 |
| Peran pelaku yang tidak disebut sumber (bagian 6 butir 1 dan 2) | Tafsir penyusun; USULAN 8 |
| Definisi umum (Playbook, Tabletop, Lessons learned, PIC pelanggan) | Penjelasan penyusun, tanpa angka atau nama |
| Folder Drive Operation, Google Drive untuk REG-02 | Spec saudara; berlabel USULAN (REG-02 tanpa label karena berkas itu memang berkas Drive) |
| Nama orang: Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo | Prompt dan config/defaults.json |
| Tanggal | Tidak ada tanggal di spec; tanggal draft 13 Oktober 2026 sumber tidak dibawa |

Butir yang tidak punya sumber dan bukan USULAN tercetak: definisi umum dan tafsir pelaku. Keduanya sudah tercatat di bagian 6 dan USULAN 8.

## ISO-W9

Dasar: hasil pemeriksa makna S05 dan LEAD-GUIDE item ISMS-SOP-01. Sheet Investigasi SNX-ISMS-FRM-02 tidak menampilkan nomor butir, jadi butir disebut dengan labelnya (label A4, A14, A15, A17 sheet Investigasi). Hanya label rujukan yang diganti.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 6.3 langkah 12, kolom Output | Nama Incident Commander di butir 2 sheet Investigasi | Nama Incident Commander di butir Incident Commander sheet Investigasi |
| 6.4 langkah 6, kolom Output | Hasil sweep di butir 12 sheet Investigasi | Hasil sweep di butir Sweep ke host sejenis sheet Investigasi |
| 6.4 langkah 11, kolom Output | Hasil verifikasi di butir 13 sheet Investigasi | Hasil verifikasi di butir Verifikasi bersih sheet Investigasi |
| 6.6 langkah 5, kolom Aktivitas | di butir 15 sheet Investigasi SNX-ISMS-FRM-02 | di butir Pemberitahuan sheet Investigasi SNX-ISMS-FRM-02 |
| 6.6 langkah 5, kolom Output | Butir 15 sheet Investigasi terisi | Butir Pemberitahuan sheet Investigasi terisi |

Open item yang ditutup atau diubah:

- Open item 14: diubah W9: rujukan butir sheet Investigasi memakai label; kolom Register tetap perlu dicocokkan dengan xlsx FRM-02 terbaru.
## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Label dipindah ke akhir kalimat atau butir, isi tetap: definisi Ack (asli: "Pengakuan pertama SOC Analyst di ticket bahwa event atau insiden diterima dan sedang ditangani (USULAN: penerima Ack belum ditetapkan)."), bagian 4 batas waktu (asli: "Batas waktu di bagian 8 dihitung dari waktu deteksi (USULAN: titik awal belum ditetapkan), kecuali batas lapor ..."), intro 6.2 (asli: "Personel Operation melapor melalui Zammad dan personel lain melalui Service Hub (USULAN: batas ini belum diputus pimpinan SINUX)."). Jumlah label tetap 9.

### W10 kalimat dihapus atau dipindah
- Definisi Direktur (COO): "Dokumen Operation menyebut jabatan ini COO, dan dokumen ini memakai COO setelah sebutan ini." diringkas menjadi satu kalimat fakta.
- Bagian 4 pengumpulan bukti: "menurut SNX-ISMS-PRO-01" dihapus (satu rujukan per paragraf); tingkat RESTRICTED (Internal) tetap, dan SNX-ISMS-PRO-01 tetap di Dokumen Terkait.

### W10 selisih angka
nihil

### W10 catatan
- Sebutan pihak luar: "pelanggan" (keputusan lintas dokumen ISMS).
- "bila" diganti "jika"; "menurut" diganti "sesuai" di beberapa kalimat; "akar yang sama" menjadi "root cause yang sama"; jembatan "Root cause analysis (analisis akar masalah)" di definisi RCA.
- Judul klausul ISO 10.2 dan judul Annex A di iso_refs tidak diubah.

### W10 audit cakupan label
- .definitions[1][1]: OK (label tetap mencakup penerima Ack yang belum ditetapkan)
- .policy[3]: OK (label tetap mencakup titik awal hitungan dari waktu deteksi, pengecualian tetap tanpa label)
