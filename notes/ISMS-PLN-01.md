# Catatan penyusun ISMS-PLN-01: Business Continuity / IT Recovery Plan

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-PLN-01.json. Mode sop, aksi T1, wave W2, nomor SNX-ISMS-PLN-01 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Approval persis dari prompt (prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo). Catatan worklist: "sumber pendukung POL-OPS-001 dan PRO-OPS-001 (bahan saja)".

Hasil uji terakhir: render_sop.py lalu lint_doc.py sop, "pass": true, fails kosong, satu warn (18 label USULAN). Validator OOXML skill docx: "All validations PASSED!". Putaran perbaikan 1 (qa/ISMS-PLN-01.verify.r1.json) sudah diterapkan; lihat bagian "Putaran perbaikan 1".

## Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-PLN-01_Business_Continuity_IT_Recovery_Plan.docx (153968 byte) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX | 2026-10-13T06:09:00Z (dari prompt; core.xml hasil dekode memuat dcterms:modified yang sama) | read_file_content (teks dan tabel), download_file_content (docx didekode di /tmp/pen-ISMS-PLN-01/src/, gambar diagram rId25.png dibuka, comments.xml dan footnotes.xml kosong) |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (dari prompt, tidak dicek ulang) | read_file_content. Bahan pendukung, dipakai untuk definisi personel on-call dan dua cacat (runbook, vault) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (dari prompt, tidak dicek ulang) | read_file_content. Dibaca utuh; tidak ada butir yang dipakai di dokumen ini |
| Kriteria penerimaan | config/checklist.json baris 91 | checklist modifiedTime 2026-10-14T17:47:13.611Z (dari catatan W0 lain, tidak dicek ulang) | Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "6.1, 7.1.3" dan ISO/IEC 27001:2022 "5.29, 5.30, 8.14". Judul checklist "Business Continuity / IT Recovery Plan" (tanda miring) dipakai; worklist.json menulis "&" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md baris 682 sampai 910 (bagian 5 PLN-01); iso-sinux-supdocs-ops-2026-10-14.md (bagian 5 POL-OPS-001 dan PRO-OPS-001) | salinan audit 13 sampai 14 Okt | DATA, tiap butir dicocokkan ulang ke teks Drive dan gambar |
| Pendukung dari repo | specs/HR-ORG-01.json, specs/ISMS-SOP-01.json, ISMS-SOP-03.json, OPS-SOP-04.json, notes/ISMS-FRM-03.md, notes/ISMS-REG-02.md, notes/OPS-SOP-04.md | repo, 15 Okt | Dibaca untuk nama peran, rujukan silang, dan retensi. Ini keluaran lane lain, bukan Drive terbaru; kutipannya bisa basi bila tim mengubah dokumen itu |

Tidak ada kalimat perintah untuk agen di tiga sumber (dicek). Daftar keputusan di POL-OPS-001 bagian 13 adalah daftar tugas COO, bukan instruksi untuk penyusun, dan tidak dijalankan.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kriteria dan pemutus aktivasi rencana | "Rencana diaktifkan bila insiden P1 diperkirakan melewati RTO layanan Tingkat 1, atau bila beberapa layanan kritis terganggu bersamaan." dan "Pemberi keputusan aktivasi: Head of Operation; bila tidak tersedia, COO; bila keduanya tidak tersedia, CEO." (Bagian 6 butir 1 dan 2) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |
| 2 | RTO dan RPO sistem internal berstatus usulan, RTO layanan pelanggan mengikuti kontrak | "RTO dan RPO sistem internal adalah USULAN dan disahkan Head of Operation; RTO layanan pelanggan mengikuti kontrak." (Bagian 4, di bawah tabel) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |
| 3 | Program uji: tabletop tahunan oleh Head of Operation, restore bulanan oleh Lead NOC | "Tabletop exercise | Satu skenario Bagian 5 per sesi | Tahunan | Head of Operation | Laporan uji (Lampiran A)" dan "Uji restore backup | Sampel data pelanggan berlayanan backup | Bulanan | Lead NOC | SNX-ISMS-FRM-01" (Bagian 10) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |

## Fakta penting dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Letak di dokumen |
|---|---|---|---|
| 1 | Tujuan | "Rencana ini menetapkan cara SINUX mempertahankan dan memulihkan layanan TI kritis, termasuk keamanan informasinya, saat terjadi gangguan besar, beserta program pengujian yang membuktikan rencana ini berjalan." | Bagian 1 (dua kalimat; kalimat penyesuaian dengan REG-02 pindah ke bagian 4) |
| 2 | Penyesuaian dengan penilaian risiko | "Cakupan dan kedalaman rencana disesuaikan dengan hasil penilaian risiko SNX-ISMS-REG-02." | Bagian 4 butir pertama (ISO 9001:2015 6.1) |
| 3 | Pengecualian scope | "Kelangsungan fasilitas data center dan platform upstream menjadi tanggung jawab penyedianya sesuai kontrak; rencana ini mengatur cara SINUX merespons, berkomunikasi, dan memulihkan bagian yang menjadi kendalinya." | Bagian 2 |
| 4 | Sembilan layanan kritis dengan ketergantungan, dampak, RTO, RPO, Tingkat | Tabel Bagian 4 sumber, mis. "Password manager internal | VM, backup ter-encrypt | Operator tidak dapat mengakses sistem | 4 jam | 24 jam | 1" | Bagian 4, sembilan paragraf |
| 5 | Managed services memakai RTO 4 jam walau RTO pelanggan mengikuti kontrak | "Managed services server pelanggan (termasuk fleet hosting pemerintah) | Akses Jumphost, kredensial, monitoring | SLA dan reputasi | 4 jam | Sesuai kontrak | 1" | Bagian 4 (diberi label USULAN, lihat USULAN U2) |
| 6 | Urutan pemulihan | "akses (password manager, Jumphost) dan monitoring dipulihkan paling awal karena menjadi syarat pemulihan lainnya." | Bagian 4, butir 6.2 |
| 7 | Penunjukan Recovery Lead dan Incident Commander | "Saat aktivasi, Head of Operation menunjuk Recovery Lead (umumnya Lead NOC) dan Incident Commander keamanan (Lead SOC) bila ada unsur keamanan." | Butir 6.1 langkah 5 dan 6 |
| 8 | Pencatatan di parent ticket | "Seluruh keputusan dan langkah dicatat kronologis di parent ticket." | Bagian 4, butir 6.1 langkah 7 |
| 9 | Pelonggaran keamanan | "keamanan informasi tidak dilonggarkan demi kecepatan kecuali disetujui Head of Operation dan dicatat (A 5.29)" | Bagian 4 dan baris pengecualian terakhir |
| 10 | Penilaian awal dan komunikasi awal | "Penilaian awal (0 sampai 30 menit): ruang lingkup dampak, layanan terdampak, penyebab awal, perkiraan durasi." dan "Komunikasi awal (dalam 1 jam): internal ke manajemen; eksternal ke pelanggan terdampak melalui Service Delivery Manager." | Butir 6.2 langkah 1, butir 6.3, bagian 8 |
| 11 | Tabel komunikasi | "Manajemen (COO, CEO) | Head of Operation | Telepon, grup manajemen | Saat aktivasi, lalu tiap 1 jam"; "Pelanggan terdampak | Service Delivery Manager | Email resmi, grup pelanggan | Saat aktivasi, lalu sesuai severity"; "Regulator, aparat, media | COO dan Legal | Sesuai ketentuan | Atas keputusan COO" | Butir 6.3 |
| 12 | Daftar kontak darurat | "Daftar kontak darurat dipelihara di file kontak restricted:ops dan password manager, dengan salinan yang dapat diakses saat sistem utama tidak tersedia." | Butir 6.4 langkah 6 dan 7 |
| 13 | Kesiapan sumber daya | "Setiap keahlian kritis (platform cloud, WAF dan proxy, network, DC fisik, panel hosting, SIEM) memiliki minimal satu cadangan terlatih. Celah saat ini dicatat sebagai risiko di SNX-ISMS-REG-02." dan "Akses break-glass ke sistem kritis tersimpan di password manager dengan prosedur pemakaian dan rotasi." dan "Laptop kerja personel on-call siap dipakai dari luar kantor." | Butir 6.4 |
| 14 | Frekuensi uji | "Uji restore sistem internal kritis | Password manager, tiket, knowledge base, konfigurasi WAF | Triwulanan | Lead NOC"; "Uji pemulihan teknis (simulasi) | Pemulihan satu layanan Tingkat 1 ke environment pengganti | Tahunan | Lead NOC"; "Uji daftar kontak | Kontak darurat internal dan supplier | Semester | Service Delivery Manager" | Butir 6.5, bagian 8, definisi |
| 15 | Perbandingan hasil uji dan peninjauan | "Hasil uji dibandingkan dengan RTO dan RPO; temuan menjadi tindakan perbaikan dengan pemilik dan tenggat. Rencana ditinjau minimal tahunan, setelah aktivasi nyata, dan setelah perubahan besar pada layanan atau supplier." | Butir 6.5, bagian 8 |
| 16 | Skenario gangguan (7 baris) | Mis. "Ransomware atau kompromi luas | Isolasi, forensik, pemulihan dari backup bersih (immutable), rotasi kredensial menyeluruh | SNX-ISMS-SOP-01, SNX-ISMS-SOP-03" | Bagian 9 (tujuh baris pertama) |
| 17 | Isi formulir laporan uji (Lampiran A) | "Nomor uji | BCP-[YYYY]-[nomor]"; "Kesimpulan: [ ] Rencana efektif · [ ] Efektif dengan perbaikan · [ ] Tidak efektif, uji ulang pada [tanggal]"; "Penanggung jawab uji"; "Disetujui (Head of Operation)" | Bagian 4 (dua butir isi laporan uji dan satu butir kesimpulan), definisi Laporan uji |
| 18 | Pemilik dokumen, klasifikasi, masa simpan | "Pemilik dokumen | Head of Operation"; "Klasifikasi | RESTRICTED (Internal)"; "Masa simpan record | Berlaku sampai digantikan" | meta.process_owner, meta.classification, bagian 11 baris pertama tabel rekaman |
| 19 | Dari SNX-ISMS-SOP-01 (lane lain): tinjauan kontak dan tabletop keamanan | Spec SOP-01: "Tinjau daftar kontak eskalasi setiap triwulan." dan "Catat hasil latihan tabletop sebagai bukti di SNX-ISMS-PLN-01." (notes/ISMS-SOP-01.md baris 50 mengutip sumber: "ditinjau triwulanan", "hasilnya dicatat sebagai bukti di SNX-ISMS-PLN-01") | Butir 6.4 langkah 6, butir 6.5 langkah 4 |
| 20 | Dari POL-OPS-001: personel on-call | "ditambah 1 Lead di jam kantor dan on-call di luar jam." (Bagian 5) | Definisi Personel on-call |
| 21 | Dari SNX-ISMS-SOP-03 (lane lain): kunci backup | Spec SOP-03: "Encryption key disimpan di password manager, terpisah dari backup. Salinan offline (break-glass) encryption key disimpan di luar password manager (USULAN)." | Bagian 4 butir kunci backup, butir 6.4 langkah 5 |
| 22 | Dari SNX-OPS-SOP-04 (lane lain): pembaruan P1 ke pelanggan tiap 1 jam | Spec OPS-SOP-04, baris SLA: "Update ke pelanggan | NOC Engineer | P1 tiap 1 jam; P2 tiap 3 jam atau per shift; P3 harian; P4 saat selesai" | Butir 6.3 langkah 3, bagian 8 |

## Pemetaan klausul ISO (kriteria baris 91)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 6.1 | Ya | Butir pertama: Head of Operation menyesuaikan cakupan dan kedalaman rencana dengan SNX-ISMS-REG-02 | 6.4 langkah 3 (celah dicatat sebagai risiko) |
| ISO 9001:2015 7.1.3 | Ya | Butir layanan kritis (Tingkat, RTO, RPO) dan sembilan paragraf layanan | 6.2, 6.4 |
| 27001 Annex A 5.29 | Ya | Butir kontrol keamanan tetap berlaku; pelonggaran lewat pengecualian | 6.2 langkah 2 sampai 4; baris pengecualian pelonggaran |
| 27001 Annex A 5.30 | Ya | Butir Tingkat, RTO, RPO; urutan pemulihan; butir kesiapan; butir laporan uji | 6.2, 6.4, 6.5 |
| 27001 Annex A 8.14 | Ya | Butir redundansi (kapasitas alternatif untuk VM kritis, konfigurasi cadangan WAF, DNS, CDN) dan butir kesiapan | Bagian 9 baris 1 dan 4; 6.4 |

Nama klausul di bagian 11: nama Annex A (5.29, 5.30) dari sumber tim; "Redundansi fasilitas pemrosesan informasi" untuk 8.14 melengkapi "redundansi" di sumber; "Tindakan menangani risiko dan peluang" (6.1) dan "Infrastruktur" (7.1.3) dari standar ISO 9001:2015, bukan dari sumber tim.

## Keputusan data

- Approval: persis dari prompt dan config/defaults.json. Sumber menulis "Disusun oleh Head of Operation", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain"; defaults mengalahkan sumber (D2).
- Department "Operation" (department_labels ISMS), sumber menulis "Information Security". Process owner "Head of Operation" (jabatan tanpa nama, dari "Pemilik dokumen").
- Sebutan COO: "Direktur (COO)" muncul pertama di tabel Definisi (bagian 3), sesudahnya "COO". CEO di sumber ditulis "Direktur Utama" (data_conflicts); nama CEO tidak ada di sumber dan tidak ditulis. Nama Amirull dan Samuel tidak muncul di badan dokumen.
- Tiket: Zammad untuk Ops, GLPI (Service Hub) untuk generalist. Sumber menulis "Ticketing system (Zammad, Service Hub)" dan "parent ticket" tanpa sistem; parent ticket ditempatkan "di Zammad atau Service Hub (SNX-OPS-SOP-04)", sama dengan cara OPS-SOP-04. Batas "generalist" belum dirinci owner, tidak dibuat di sini (open item 8).
- Vault: "Password manager ... (vault). Status operasional: menunggu konfirmasi Ops", kalimat sama dengan SNX-ISMS-SOP-03.
- Kunci backup punya salinan offline (USULAN): dimasukkan di bagian 4, 6.4 langkah 5, dan pengecualian kehilangan password manager.
- Label "restricted:ops" di sumber bukan tingkat skema SNX-ISMS-PRO-01. Badan dokumen menulis "file kontak berklasifikasi RESTRICTED (Internal)", sesuai tingkat skema dan label dokumen ini. Kutipan sumber di bagian "Fakta penting" tetap verbatim.
- PPN: tidak berlaku.
- Nama peran bagian 5 (dan PIC bagian 6 dan 8) dari specs/HR-ORG-01.json: Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager (daftar jabatan Divisi Operation, USULAN, tanpa pemegang); COO (Direktur, JA-02); Direktur Utama (JA-01); Legal & Compliance (JA-08 dan JA-09; sumber menulis "Legal"). Pemetaan peran sumber yang tidak ada di HR-ORG-01:

| Peran di sumber | Pemetaan | Catatan |
|---|---|---|
| CEO | Direktur Utama (JA-01) | data_conflicts |
| COO | COO, sebutan JA-02 | data_conflicts |
| Legal | Legal & Compliance (JA-08, JA-09) | satu nama jabatan untuk dua pemegang di HR-ORG-01 |
| Recovery Lead | Dipertahankan sebagai peran penunjukan, umumnya Lead NOC | bukan jabatan; sumber menulis "umumnya Lead NOC" |
| Incident Commander keamanan | Fungsi Lead SOC, dipakai di definisi dan baris peran Lead SOC | PIC langkah ditulis Lead SOC |
| ISO/ISMS Coordinator (pemeriksa di sumber) | Tidak dipakai di badan | pemeriksa dokumen = Fani menurut defaults; REG-02 ditulis "pemilik sesuai SNX-ISMS-REG-02" supaya peran ISMS Coordinator (belum ada pemegang, K-13 HR-ORG-01) tidak masuk tabel peran |
| Penanggung jawab uji | Peran di formulir Lampiran A sumber, dipakai sebagai peran sendiri | Lead NOC, Head of Operation, Lead SOC, atau Service Delivery Manager menurut jenis uji |
| Personel on-call, "tim internal" | "Personel on-call" didefinisikan; "tim internal" diganti "personel Divisi Operation yang terlibat" | lesson pilot: tidak ada "tim" tanpa keterangan |

## Penanganan cacat context/audit

Catatan PLN-01 (bagian 5, fileId 1vwD5tOR...):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | RTO dan RPO sistem internal berlabel USULAN; baris 1 tanpa angka; baris 2 memakai "4 jam" sehingga "RTO layanan pelanggan mengikuti kontrak" tidak cocok; MTPD tidak ada | Label USULAN dipertahankan (bagian 4). Baris 2 ditulis "RTO 4 jam bila kontrak tidak menetapkan RTO (USULAN)" dan ditambah baris pengecualian "Kontrak pelanggan menetapkan RTO yang berbeda" (USULAN U2). MTPD tidak ditambah: tidak ada di sumber dan tidak diminta klausul kriteria; open item 14 |
| 2 | Cakupan bagian 4 tidak memuat Acronis, konfigurasi network device, dokumen di Drive; SIEM tanpa baris | Tidak diperbaiki diam-diam: angka RTO tanpa sumber dilarang dan Tingkatnya tidak diketahui. Scope tetap seperti sumber. Open item 3 untuk Fani |
| 3 | "Sesuai penyedia" dan "Sesuai SLA kontrak" tidak dapat dibandingkan dengan target internal | Dipertahankan apa adanya (sumber tim; angka bukan milik SINUX) |
| 4 | Tingkat vs pengelompokan SNX-ISMS-SOP-03 (tidak bertentangan karena SOP-03 mendelegasikan RTO ke PLN-01) | Tidak ada perubahan. Nilai RTO internal (4, 8, 24 jam) ditulis sama dengan sumber supaya "rentang 4 sampai 24 jam" di SOP-03 tetap benar |
| 5 | Jumphost dan WAF: RPO "1 minggu (konfigurasi)", RTO 4 jam selaras SOP-03 | Dipertahankan |
| 6 | Komunikasi awal ke pelanggan 1 jam vs laporan awal P1 24 jam di SNX-ISMS-SOP-01 | Dibedakan: butir 6.3 menulis bahwa laporan awal insiden keamanan mengikuti SNX-ISMS-SOP-01; pembaruan P1 tiap 1 jam dirujuk ke SNX-OPS-SOP-04. Konfirmasi open item 12 |
| 7 | Diagram: kotak "output akhir" masih diikuti kotak "Uji rencana berkala"; "Uji rencana berkala" tidak ada di tahapan Bagian 7 | Diperbaiki: alur berakhir di "RCA dan pembaruan rencana"; siklus uji tidak digambar sebagai tahap pemulihan karena ada di butir 6.5 dan bagian 8. Warna biru dan oranye di legenda sumber tidak dibawa (renderer tanpa warna simpul) |
| 8 | Diagram: cabang "tidak" tanpa garis kembali; kasus "beberapa layanan kritis terganggu bersamaan" tidak punya cabang | Diperbaiki: simpul keputusan memuat kedua kriteria; garis putus-putus kembali dari "Tangani sebagai P1" ke keputusan, berlabel "Nilai ulang bila perkiraan berubah (USULAN U3)". Tambahan ini bukan dari sumber |
| 9 | CEO hanya muncul di PLN-01 dan SNX-OPS-SOP-04, tanpa nama | Diganti "Direktur Utama" (data_conflicts). Nama tidak ditulis |
| 10 | FRM-03 tidak punya kolom kontak eskalasi dan rencana alternatif per supplier; Lampiran A form kosong | FRM-03 tetap dirujuk seperti sumber dan kekurangannya dicatat di open item 10 (USULAN 8 di notes/ISMS-FRM-03.md belum diterapkan). Kontak eskalasi supplier dihubungkan ke daftar kontak darurat. Lampiran A: lihat Asumsi 12 dan open item 11 |
| 11 | Pengesahan kosong; dua baris riwayat revisi bertanggal sama berstatus Menunggu | Teratasi oleh template: satu baris Revision 00, Effective Date kosong, Signature kosong |

Catatan POL-OPS-001 dan PRO-OPS-001 yang relevan:

| # | Cacat | Penanganan |
|---|---|---|
| 12 | POL #7 dan PRO #8: rujukan SKILL_*, DOCTRINE, DEC, HANDOVER, CORE, CLAIM_CLASS_POLICY, SINUX_*, "packet setor", "jalur staging", "japri", "om Ipe", "WA owner" | Tidak ada yang disalin. Lint lulus pada pola rujukan internal |
| 13 | POL #6: GLPI sebagai sistem tiket resmi vs Zammad di PRC-01; bagian 13 butir 6 | Mengikuti defaults: Zammad untuk Ops, Service Hub (GLPI) untuk generalist; open item 8 |
| 14 | POL bagian 13 butir 7: kredensial masih di Google Sheets dan Excel, vault belum live | Vault ditulis "menunggu konfirmasi Ops"; open item 7 |
| 15 | POL bagian 13 butir 8: "Runbook yang belum ada: Nusagrid VM end-to-end, alur backup dan restore Acronis, checklist onboarding pelanggan, cek mingguan Overseer." bertentangan dengan kalimat sumber PLN-01 "Runbook pemulihan per sistem kritis tersedia" | Kalimat "tersedia" diubah menjadi kewajiban ("Sediakan runbook ... di knowledge base"), supaya dokumen tidak menyatakan keadaan yang belum terbukti. Open item 4 |
| 16 | POL #3: pemilik POL-OPS-001 COO vs Head of Operation | Tidak menyangkut PLN-01 (pemilik dokumen ini Head of Operation menurut sumber) |
| 17 | POL #13: matriks severity tanpa target pulih; SNX-OPS-SOP-04 memuat target pulih P1 "4 jam" (USULAN) | "RTO layanan Tingkat 1 yang terdampak" tidak disamakan dengan target pulih P1; open item 9 |
| 18 | PRO #7 dan lainnya | Tidak relevan |

## Putaran perbaikan 1

| # | Temuan verifikator | Perbaikan |
|---|---|---|
| 1 | Pengantar 6.4 memuat catatan proses ("karena sumber tidak menyebut pelaku") | Kalimat jadi "Pelaku langkah 1 sampai 4, 7, dan 8 berstatus (USULAN) sampai Head of Operation menetapkannya." Alasan "sumber pasif tanpa pelaku" tinggal di notes (Asumsi 9, U4). Pencarian "sumber", "penyusun", "tafsir", "dokumen sumber" di spec: hanya "sumber daya" yang sah |
| 2 | "restricted:ops" bukan tingkat PRO-01 | Diganti "file kontak berklasifikasi RESTRICTED (Internal)" (6.4 langkah 6) |
| 3 | Butir 8.14 membuang "bila kapasitas alternatif tersedia" | Butir jadi "Recovery Lead memindahkan VM kritis bila kapasitas alternatif tersedia, dan mengalihkan lalu lintas WAF, DNS, atau CDN sesuai konfigurasi cadangan, menurut skenario di bagian 9." |
| 4a | Butir kesiapan di bagian 4 pasif | Diberi pelaku: Head of Operation dan Lead SOC menyiapkan |
| 4b | Lead SOC tidak masuk Penanggung jawab uji; bagian 8 tanpa frekuensi tabletop keamanan | Lead SOC ditambahkan ke baris Penanggung jawab uji; baris SLA "Tabletop exercise keamanan (SNX-ISMS-SOP-01) | Lead SOC | Minimal tahunan" (SOP-01: "Latihan tabletop minimal setahun sekali") |
| 4c | "copy" dan "salinan", "latihan tabletop keamanan" dan "Tabletop exercise" berganti-ganti | Definisi Immutable copy memakai "Salinan backup"; semua "latihan tabletop keamanan" jadi "tabletop exercise keamanan" |
| 4d | Pelaku dan lokasi tanpa label | Label (USULAN) ditambah pada: Service Delivery Manager menyampaikan RTO kontrak (baris peran dan baris pengecualian), Head of Operation meminta personel on-call bekerja jarak jauh (baris pengecualian), lokasi Google Drive dokumen ini (bagian 11). USULAN U9 |
| 4e | Rujukan VPN ke SOP-02 tidak ada di SOP-02 | Rujukan SOP-02 hanya untuk Jumphost; VPN ditulis tanpa rujukan SOP-02. Baris Dokumen terkait SOP-02 tidak lagi menyebut VPN. Open item 18 |
| 4f | Lead NOC menyusun semua RCA, padahal POL-OPS-001 membagi RCA ketersediaan (NOC) dan keamanan (SOC) | 6.2 jadi 14 langkah: langkah 12 RCA aspek ketersediaan (Lead NOC), langkah 13 RCA aspek keamanan bila ada unsur keamanan (Lead SOC, mengikuti SNX-ISMS-SOP-01 "Menyusun RCA ... insiden P1 dan P2"), langkah 14 pembaruan rencana. Baris peran Lead NOC dan Lead SOC disesuaikan |
| 4g | Lampiran A jadi paragraf; judul "SOP" dan "&" lawan "/" | Tidak diubah: format terkunci (D4); sudah tercatat di Asumsi 12 dan open item 11 dan 17 |

## Asumsi dan tafsir

1. Kalimat pasif sumber diberi pelaku: Recovery Lead mencatat keputusan dan langkah di parent ticket (sumber: "dicatat kronologis"); Head of Operation menetapkan (aktivasi, penunjukan, pelonggaran, pemilik dan tenggat tindakan perbaikan); pencatat dan penetap dibedakan di bagian 4, 5, dan 6.
2. Titik awal "0 sampai 30 menit" dan "dalam 1 jam" tidak disebut sumber; dibaca "sejak aktivasi". Tabel komunikasi sumber menulis "Saat aktivasi" dan daftar tahapan menulis "dalam 1 jam"; digabung: komunikasi dimulai saat aktivasi, pesan pertama paling lambat 1 jam sejak aktivasi.
3. "RTO layanan Tingkat 1" dibaca sebagai RTO layanan Tingkat 1 yang terdampak (diagram sumber menulis "RTO Tingkat 1").
4. Kriteria "P1 ... atau beberapa layanan kritis terganggu bersamaan" dipertahankan; Head of Operation menilai kriteria (sumber menyebut hanya pemutus).
5. "Pulihkan akses dan monitoring paling awal" dipecah dari "Tingkat 1 terlebih dahulu" menjadi dua langkah (6.2 langkah 5 dan 6).
6. Lead SOC memimpin respons keamanan (6.2 langkah 3) dari "Incident Commander keamanan (Lead SOC)"; isolasi dan forensik pada skenario ransomware dari baris sumber.
7. RCA ketersediaan disusun Lead NOC mengikuti peran Lead NOC di SNX-OPS-SOP-04 ("menyusun RCA P1 dan P2"); RCA keamanan disusun Lead SOC mengikuti SNX-ISMS-SOP-01 dan RACI POL-OPS-001 bagian 10 (R ketersediaan NOC, R keamanan SOC); pembaruan rencana dilakukan Head of Operation (pemilik dokumen).
8. "Rotasi kredensial darurat" dan "hapus jalur sementara" dilakukan Recovery Lead (sumber pasif).
9. Pelaku langkah 6.4 nomor 1 sampai 4, 7, 8 (Head of Operation, Lead SOC) tidak disebut sumber; diberi label USULAN (U4). Langkah 5 (Lead NOC, kunci offline) dari SOP-03; langkah 6 (Lead SOC, tinjauan triwulanan) dari SOP-01.
10. "Sistem utama" pada "salinan yang dapat diakses saat sistem utama tidak tersedia" dipertahankan apa adanya; sistem yang dimaksud tidak disebut sumber (open item 13).
11. Skenario bagian 5 sumber dipindah ke bagian 9 (Exception Management) karena template SOP tidak punya bagian skenario; tiap baris diberi pelaku. Baris tambahan: "Kontrak pelanggan menetapkan RTO yang berbeda" (turunan kalimat sumber dan peran Service Delivery Manager di SOP-03) dan "Pelonggaran kontrol keamanan" (dari Bagian 7 sumber).
12. Lampiran A tidak dibawa sebagai tabel: template SOP tidak punya bagian lampiran, dan lint melarang sel kosong di tabel mode sop. Semua kolom formulir dipindah ke dua butir bagian 4 (isi laporan uji) dan satu butir kesimpulan. Tidak ada formulir kosong siap isi di dokumen ini.
13. Matriks eskalasi ke penyedia upstream dirujuk ke SNX-OPS-SOP-04 butir 6.6 (ada di spec OPS-SOP-04), bukan ditulis ulang.
14. Immutable: sumber menulis "backup bersih (immutable)"; SOP-03 menyatakan immutable copy dipakai bila platform mendukung; dokumen mengikuti SOP-03 ("dengan immutable copy bila platform mendukung").
15. Konfigurasi cadangan dan kapasitas alternatif (butir redundansi bagian 4) dipakai "sesuai skenario"; sumber tidak menunjukkan apakah keduanya sudah ada (open item 5).
16. Retensi: 3 tahun untuk FRM-01 dari SOP-03, 5 tahun untuk RCA FRM-10 dari SOP-04 (kutipan sumber SOP-04 di notes/OPS-SOP-04.md baris 52); 3 tahun untuk laporan uji dan parent ticket adalah USULAN. "Berlaku sampai digantikan" dari baris "Masa simpan record" sumber, dipakai untuk dokumen ini dan REG-02.
17. Definisi umum (Containment, Baseline, Break-glass, Upstream, Tabletop exercise, Sistem internal, Manajemen) adalah penjelasan penyusun, bukan kalimat tim.
18. Nama klausul ISO 9001:2015 6.1 dan 7.1.3 dan frasa "fasilitas pemrosesan informasi" untuk 8.14 dari standar.
19. Diagram: 12 simpul, rankdir TB. Simpul "Penilaian awal" ditaruh sebelum "Komunikasi awal" mengikuti urutan Bagian 7 sumber, walau butir 6.3 menyatakan komunikasi berjalan dalam 1 jam pertama bersamaan dengan langkah lain.

## USULAN

Lint menghitung 18 label (USULAN), satu di antaranya definisi istilah (spec memuat satu label lagi di gambar diagram). Butir bermakna: 9.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | RTO dan RPO sistem internal (monitoring 4 jam dan 24 jam; ticketing 8 jam dan 24 jam; password manager 4 jam dan 24 jam; Jumphost 4 jam dan 1 minggu; WAF dan proxy 4 jam dan 1 minggu; knowledge base 24 jam dan 24 jam) | Bagian 4 | Label USULAN berasal dari sumber; angka tidak diubah | Fani |
| U2 | RTO 4 jam managed services server pelanggan berlaku bila kontrak tidak menetapkan RTO | Bagian 4, bagian 9 | Sumber memberi "4 jam" pada layanan pelanggan sambil menyatakan RTO pelanggan mengikuti kontrak; syarat "bila kontrak tidak menetapkan" adalah tafsir | Fani |
| U3 | Penilaian ulang kriteria aktivasi bila perkiraan durasi atau layanan terdampak berubah | Butir 6.1 langkah 4, diagram | Menutup cacat "cabang tidak tanpa garis kembali"; bukan dari sumber | Fani |
| U4 | Pelaku langkah kesiapan sumber daya (Head of Operation memastikan runbook, cadangan, celah risiko, akses break-glass, laptop on-call; Lead SOC menyimpan salinan kontak) | Butir 6.4 langkah 1 sampai 4, 7, 8; baris peran Head of Operation | Sumber pasif tanpa pelaku | Fani |
| U5 | Salinan offline encryption key backup di luar password manager, disimpan Lead NOC | Bagian 4, butir 6.4 langkah 5, baris peran Lead NOC | Aturan lintas dokumen; label USULAN diwarisi dari SNX-ISMS-SOP-03 | Fani |
| U6 | Laporan uji disimpan di Folder Drive Operation, pemilik Head of Operation, retensi 3 tahun | Bagian 11 | Sumber hanya menulis "Lampiran A dokumen ini"; lokasi, pemilik, dan retensi tanpa sumber | Fani |
| U7 | Parent ticket aktivasi: pemilik Head of Operation, retensi 3 tahun | Bagian 11 | Sumber tidak menyebut pemilik dan retensi; 3 tahun disamakan dengan rekap tiket di SNX-OPS-SOP-04 | Fani |
| U8 | Lokasi RCA: Folder Drive Operation, subfolder per tahun | Bagian 11 | Label USULAN diwarisi dari SNX-OPS-SOP-04 dan SNX-ISMS-SOP-01 | Fani |
| U9 | Pelaku dan lokasi tambahan: Service Delivery Manager menyampaikan RTO kontrak ke Recovery Lead; Head of Operation meminta personel on-call bekerja jarak jauh; Google Drive sebagai lokasi dokumen ini | Bagian 5, bagian 9, bagian 11 | Sumber pasif atau diam tentang pelaku dan lokasi; diturunkan dari peran di SNX-ISMS-SOP-03 dan POL-OPS-001 bagian 9 | Fani |

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis COO (Amirull Yusuf Zulkarnain); defaults memakai Samuel Kristanto Utomo / President Director. Defaults dipakai | owner, Samuel |
| 2 | Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager adalah jabatan USULAN di POL-OPS-001 dan HR-ORG-01 (K-10), belum ada pemegang bernama; hubungan Head of Operation dengan VP Tech Operation and Services belum ditetapkan (K-09). Sampai ada pemegang, keputusan aktivasi tidak punya orang | owner, Fani |
| 3 | Acronis (platform backup), konfigurasi network device, SIEM, dan dokumen di Drive tidak punya baris di daftar layanan kritis. SNX-ISMS-SOP-03 memuat RTO 4 jam (USULAN) untuk konfigurasi network device. Perlu keputusan apakah baris ditambah dan Tingkatnya | Fani |
| 4 | Sumber menulis "Runbook pemulihan per sistem kritis tersedia"; POL-OPS-001 bagian 13 mencatat runbook Nusagrid VM end-to-end dan alur backup dan restore Acronis belum ada. Dokumen menulis kewajiban, bukan keadaan | Fani |
| 5 | Ketersediaan kapasitas alternatif untuk memindahkan VM kritis dan konfigurasi cadangan WAF, DNS, CDN tidak ditunjukkan sumber; belum ada daftar atau pemilik. Tanpa itu butir redundansi (Annex A 8.14) belum terbukti | Fani |
| 6 | Parent ticket dan layanan ticketing berada di Tingkat 2 (RTO 8 jam), padahal dibutuhkan sejak aktivasi. Tempat mencatat keputusan bila Zammad dan Service Hub mati tidak ditentukan sumber; kontrol pengganti tidak dibuat | Fani |
| 7 | Status password manager (vault) belum terkonfirmasi: REG-01 menulis Aktif, REG-02 dan POL-OPS-001 bagian 13 menulis belum live. Break-glass dan daftar kontak tersimpan di password manager, yang sendiri masuk skenario kehilangan; salinan akses break-glass di luar password manager tidak ada di sumber (hanya salinan offline encryption key, USULAN U5) | Ops (Fani) |
| 8 | Batas "generalist" lawan Ops untuk Service Hub (GLPI) belum dirinci owner; dokumen mengikuti rumusan OPS-SOP-04 ("Zammad atau Service Hub") | owner |
| 9 | "RTO layanan Tingkat 1" dibaca RTO layanan yang terdampak; SNX-OPS-SOP-04 punya skala sendiri (target pulih P1 4 jam, USULAN). Perlu ditegaskan hubungannya | Fani |
| 10 | SNX-ISMS-FRM-03 tidak punya kolom kontak eskalasi dan rencana alternatif per supplier, padahal skenario kegagalan supplier merujuk ke sana (USULAN 8 di notes/ISMS-FRM-03.md belum diterapkan) | Fani |
| 11 | Lampiran A (formulir laporan uji) tidak bisa ditampung template SOP sebagai tabel. Isi kolomnya ada di bagian 4. Bila tim ingin formulir kosong siap isi, itu dokumen baru di luar 88 baris | owner, Aziz |
| 12 | Komunikasi awal ke pelanggan 1 jam (PLN-01) dan laporan awal P1 24 jam (SNX-ISMS-SOP-01) memakai pemicu berbeda; dokumen membedakannya. Perlu konfirmasi bahwa keduanya berlaku bersamaan | Fani |
| 13 | Tabletop: PLN-01 menugaskan Head of Operation, SNX-ISMS-SOP-01 menugaskan Lead SOC dan mencatat hasilnya di PLN-01; dokumen memuat dua langkah (6.5 langkah 3 dan 4). Perlu ditegaskan apakah satu sesi tahunan memenuhi keduanya. Juga: pemelihara harian daftar kontak darurat tidak disebut (SOP-01 hanya menyebut peninjau triwulanan Lead SOC), dan "sistem utama" pada salinan kontak tidak jelas | Fani |
| 14 | MTPD tidak ada di sumber dan tidak ditambah; angka RTO per layanan belum dihubungkan dengan batas toleransi bisnis | Fani |
| 15 | Titik awal 30 menit dan 1 jam dibaca "sejak aktivasi" (tafsir; OPS-SOP-04 memakai waktu Dilaporkan sebagai titik awal Ack) | Fani |
| 16 | Template tidak punya slot KPI dan sumber PLN-01 tidak punya KPI; bagian 8 berisi jadwal dan batas waktu saja | Aziz |
| 17 | Tampilan: bagian 4 berisi 21 paragraf karena template tidak punya tabel di bagian itu; daftar sembilan layanan kritis lebih mudah dibaca sebagai tabel. Renderer juga mengawali Document Title dengan "SOP" untuk dokumen jenis rencana, dan nama berkas memakai "&" (worklist) sementara judul dokumen memakai "/" (checklist baris 91). Perubahan butuh keputusan format | Aziz |
| 18 | SNX-ISMS-SOP-02 tidak memuat VPN, sedangkan skenario gangguan internet atau kantor di sumber PLN-01 menyebut "akses melalui Jumphost dan VPN". Dokumen merujuk SOP-02 hanya untuk Jumphost | Fani |
| 19 | Frekuensi tabletop exercise keamanan (minimal tahunan) berasal dari SNX-ISMS-SOP-01, bukan sumber PLN-01; perlu konfirmasi bahwa satu jadwal tahunan cukup untuk dua tabletop (lihat butir 13) | Fani |

## Dua pertanyaan akhir

1. Apa yang membuat teks ini terdengar buatan AI? Hasil telaah: (a) sembilan paragraf layanan di bagian 4 berpola sama (Tingkat, Bergantung pada, Bila mati, RTO, RPO). Pola itu berasal dari kolom tabel sumber yang diratakan karena template tidak punya tabel di bagian 4; dipertahankan karena auditor membandingkannya dengan sumber. (b) Kata kerja "Pastikan" berulang di butir 6.4 dan 6.5. Diperbaiki di 6.4 (Sediakan, Siapkan, Simpan); dua "Pastikan" di 6.5 dipertahankan karena Lead NOC memang bertanggung jawab atas uji restore, bukan melaksanakannya. (c) Baris pengecualian sering dibuka "Recovery Lead memimpin ..."; dipertahankan karena Recovery Lead memang pemimpin pemulihan di semua skenario itu. (d) Kalimat pasif tanpa pelaku untuk aktivasi, urutan pemulihan, dan pencatatan uji diubah menjadi aktif dengan pelaku. (e) Aturan yang sama di tiga tempat ("umumnya Lead NOC", "dipegang Lead SOC", daftar tiga peran penanggung jawab uji) dikurangi menjadi satu atau dua tempat dan definisi tidak lagi memuat aturan. (f) Catatan proses bocor ke pengantar 6.4 ("karena sumber tidak menyebut pelaku"); dihapus pada putaran perbaikan 1 dan dipindah ke notes. (g) Tidak ada pembuka generik, penutup positif, tebal, tanda kutip penekanan, atau em-dash; lint gaya lulus. Sisa risiko: nada formal rata di sel peran yang panjang.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa satu per satu. Angka 4, 8, 24 jam, 1 minggu, 30 menit, 1 jam, Tingkat 1 sampai 3, bulanan, triwulanan, semester, tahunan dari sumber PLN-01. "Tiap 1 jam" untuk pembaruan P1 ke pelanggan dari spec OPS-SOP-04; "triwulan" tinjauan kontak dari SOP-01 (kutipan di notes/ISMS-SOP-01.md); 3 tahun (FRM-01) dari SOP-03; 5 tahun (FRM-10) dari SOP-04; "Berlaku sampai digantikan" dari sumber PLN-01. Tanpa sumber dan diberi label USULAN: RTO 4 jam bersyarat kontrak, penilaian ulang aktivasi, pelaku langkah 6.4, 3 tahun untuk laporan uji dan parent ticket, lokasi folder dan pemilik. Tanpa sumber dan tanpa label: nama klausul 6.1 dan 7.1.3 dari standar, serta definisi umum; keduanya dicatat di Asumsi 17 dan 18. Titik awal 30 menit dan 1 jam ("sejak aktivasi") adalah tafsir, dicatat di Asumsi 2 dan open item 15. Nama orang di badan dokumen: nol. Tanggal: nol. Kredensial: nol; URL login tidak ditulis.

## Hasil uji

- python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/ISMS-PLN-01.json /tmp/pen-ISMS-PLN-01/ISMS-PLN-01.docx: berhasil.
- python3 -I tools/lint_doc.py /tmp/pen-ISMS-PLN-01/ISMS-PLN-01.docx sop: "pass": true, fails kosong, warns: "18 butir (USULAN) menunggu ACC" (tidak ada warn PIC SLA). Diulang sesudah putaran perbaikan 1: tetap pass.
- Validasi OOXML (skill docx, validate.py): "All validations PASSED!". PDF dirender dengan soffice (19 halaman); diagram 12 simpul terbaca penuh satu halaman.
