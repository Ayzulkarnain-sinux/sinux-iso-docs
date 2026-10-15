# Catatan penyusun HR-ORG-01: Struktur Organisasi SINUX

Status: DRAFTED (spec + notes ada). Spec: specs/HR-ORG-01.json. Mode generic, aksi T2, nomor SNX-HR-ORG-01 (nomor SNX lama dipertahankan), department Human Resources, classification INTERNAL, audit_class None, wave W1. Approval persis dari config/defaults.json: prepared Sita Nadia Salsabila Widodo / HRGA Officer, reviewed Aziz Priyo Widakdo / HR Manager, approved Samuel Kristanto Utomo / President Director. process_owner "HR Manager" (jabatan, tanpa nama): sumber menulis "Process Owner | HR Lead – Aziz Priyo Widakdo"; jabatan Aziz di semua dokumen memakai "HR Manager" (data_conflicts), jadi nilainya HR Manager.

Hasil uji terakhir: render_sop.py lalu lint_doc.py generic = "pass": true, fails kosong, satu warn (13 butir (USULAN) menunggu ACC). Validator OOXML skill docx: "All validations PASSED!". tools/selftest.sh: 6 baris OK, tidak ada berkas tools atau template yang saya ubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata, cocok dengan worklist) | read_file_content, teks penuh 15 jabatan |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, cocok dengan worklist) | read_file_content, teks penuh bagian 1 sampai 13 |
| Lampiran 2 Struktur-Organisasi PT. SINUX.docx (19115 byte) | 1FaPdUww5zNl0O9ZyYg2_Z2nCoU7QMsEg | 2026-09-05T15:48:26Z (get_file_metadata, cocok dengan worklist) | read_file_content dan download_file_content; document.xml didekode di /tmp/pen-HR-ORG-01/ dengan python3 -I |
| Kriteria penerimaan | config/checklist.json baris 21 | Description null | Kriteria = substansi sumber tim + acuan klausul ISO (USULAN, perlu konfirmasi konsultan). Checklist tidak memberi acuan klausul untuk baris ini |
| Pendukung (bahan, bukan sumber utama) | context/audit hr, ops, isms, legal, fat, sintesis | salinan audit 13 sampai 14 Okt | Dibaca lewat salinan audit (DATA). Dipakai hanya untuk: nama peran Finance Lead dan Finance Staff, Line Manager Legal dan Staff Legal, ISMS Coordinator di matriks peran (bagian 8 dokumen), dan untuk catatan K-13 |

Catatan W0 untuk baris ini: Checklist menautkan berkas 1dcziYriRHtTq8E_9QUtTVMe48xvRKNp0. Saya ulang hari ini: get_file_metadata menjawab "Requested entity was not found". Pencarian judul "Struktur Organisasi" hanya menemukan Lampiran 2 di atas dan satu memo struktur dari perusahaan lain (PT Era Awan Digital); memo itu residu pihak lain dan tidak dipakai. Berkas tim untuk baris 21 tetap tidak terlihat; lihat open item 1.

Isi Lampiran 2 (decode document.xml, 13188 byte): sepuluh potongan teks, "STRUKTUR ORGANISASI PT. STRATEGI INTEGRASI NUSANTARA", "Jakarta,1 September 2026", "PT Sinux", "Direktur". Tidak ada gambar, tabel, kotak teks, atau bentuk. Lampiran itu kerangka kosong; tanggal 1 September 2026 tidak dipakai (Effective Date dokumen ini kosong).

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Dokumen mencakup 15 jabatan aktif (JA-01 sampai JA-15); posisi kosong dan grading dikecualikan | "Cakupan \| 15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Semua garis lapor dari Job Analysis belum resmi sampai disahkan, sehingga dokumen ini memberi label menunggu konfirmasi | "Hubungan atasan-bawahan bertanda “usulan/konfirmasi” tidak boleh diperlakukan sebagai reporting line resmi sampai disahkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Divisi Operation hanya berstatus usulan: delapan jabatan, tanpa headcount dan nama pemegang yang diputus | "Divisi Operation diusulkan berisi delapan jabatan: satu Head of Operation, dua jabatan per NOC dan SOC, dan tiga di SD dan PM. Nama jabatan, jenjang, dan headcount adalah USULAN yang disahkan COO." | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |

## 2. Fakta penting lain dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber (fileId) dan posisi |
|---|---|---|---|
| 1 | JA-01 Direktur Utama, atasan organ perusahaan (K-05) | "Atasan Langsung \| Organ perusahaan sesuai ketentuan dan anggaran dasar (verifikasi)" | 1m91..., JA-01 |
| 2 | JA-02 melapor ke Direktur Utama | "Atasan Langsung \| Direktur Utama" | 1m91..., JA-02 |
| 3 | JA-03 atasan Direktur; JA-05 perlu dikonfirmasi (K-01, K-02) | "Atasan Langsung \| Direktur" dan "Bawahan Langsung \| Business Development dan Brand & Marketing. Hubungan pelaporan Manager of Product Tech perlu dikonfirmasi." | 1m91..., JA-03 |
| 4 | JA-04 dan JA-05 atasan Direktur; JA-13 melapor ke JA-04 | "Atasan Langsung \| Direktur" (JA-04, JA-05); "Atasan Langsung \| VP Tech Operation and Services" (JA-13) | 1m91..., JA-04, JA-05, JA-13 |
| 5 | JA-06 dan JA-07 atasan ditulis dengan nama departemen (K-06) | "Atasan Langsung \| Commercial – Laras Rasmawati" | 1m91..., JA-06, JA-07 |
| 6 | JA-08, JA-10, JA-11 atasan tidak tunggal (K-03) | "Atasan Langsung \| Management / Direktur" | 1m91..., JA-08, JA-10, JA-11 |
| 7 | JA-09 melapor ke JA-08 | "Atasan Langsung \| Ester Febe Utomo" dan "Bawahan Langsung \| Alif Altamziz" | 1m91..., JA-09, JA-08 |
| 8 | JA-14 atasan tidak tunggal; nama jabatan HR Lead (K-04, K-06) | "Penamaan Jabatan \| HR Lead" dan "Atasan Langsung \| Direktur atau Management sesuai struktur yang disahkan" | 1m91..., JA-14 |
| 9 | JA-12 melapor ke JA-14; JA-15 melapor ke JA-12 | "Atasan Langsung \| HR Lead – Aziz Priyo Widakdo" (JA-12); "Atasan Langsung \| HRGA Officer – Sita Nadia Salsabila Widodo" (JA-15) | 1m91..., JA-12, JA-15 |
| 10 | Nama unit tidak seragam (K-06) | "Unit / Departemen \| Operations" (JA-04, JA-05); "Operation" (JA-13); "HR / GA" (JA-12); "Human Resources" (JA-14); "HRGA / General Affairs" (JA-15) | 1m91... |
| 11 | Ejaan Samuel dan nama pemegang (K-07) | "Pemegang Jabatan \| Samuel Kristianto Utomo" | 1m91..., JA-01 |
| 12 | Tanggung jawab JA-01 di matriks peran | "Memastikan kebijakan mutu, sasaran mutu, dan kebutuhan sumber daya ditetapkan dan dikomunikasikan." dan "Memimpin tinjauan manajemen dan memastikan keputusan memiliki penanggung jawab serta tenggat tindak lanjut." | 1m91..., JA-01 A.3, A.7 |
| 13 | Tanggung jawab JA-02 dan JA-04 di matriks peran | "Memastikan kepatuhan terhadap kebijakan dan proses yang disahkan." (JA-02 A.5); "Memastikan kontrol keamanan, akses, backup dan perubahan sesuai kebijakan teknis." (JA-04 A.4) | 1m91... |
| 14 | Batas wewenang semua jabatan (satu paragraf di bagian 8) | "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 1m91..., bagian E tiap jabatan |
| 15 | Penyetuju dan tinjauan | "Approved by \| Management / Authorized Director" dan "Next review \| 12 bulan sejak efektif atau saat ada perubahan signifikan" | 1m91..., bagian 4 (K-14, bagian Kesimpulan) |
| 16 | Hak tanda tangan dan KPI dikecualikan | "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." dan "KPI dalam dokumen merupakan usulan indikator, target numerik, bobot dan sumber data ditetapkan pada KPI Matrix terpisah." | 1m91..., bagian 2 |
| 17 | Divisi Operation di bawah COO, tiga sub divisi; garis ke COO usulan | "Divisi Operation berada di bawah COO dan terdiri dari tiga sub divisi: NOC, SOC, serta Service Delivery dan PM." dan "Struktur organisasi penuh SINUX tidak terlihat di scope ini, sehingga garis lapor Operation ke COO adalah USULAN." | 1bn7..., bagian 3 |
| 18 | Garis lapor delapan jabatan Operation | "Lapor ke: COO. Membawahi: Lead NOC, Lead SOC, Service Delivery Manager." (Head of Operation); "Lapor ke: Head of Operation. Membawahi: NOC Engineer." (Lead NOC); "Lapor ke: Lead NOC." (NOC Engineer); "Lapor ke: Head of Operation. Membawahi: SOC Analyst." (Lead SOC); "Lapor ke: Lead SOC." (SOC Analyst); "Lapor ke: Head of Operation. Membawahi: Project Manager, Project Coordinator." (Service Delivery Manager); "Lapor ke: Service Delivery Manager." (Project Manager, Project Coordinator) | 1bn7..., bagian 9.1 sampai 9.4 |
| 19 | Pola kerja | "NOC dan SOC berjalan 3 shift dengan Lead di jam kantor plus on-call; SD dan PM bekerja jam kantor." dan "NOC Engineer (shift, 4 regu)" | 1bn7..., bagian 3, 9.2 |
| 20 | Project Coordinator opsional | "Project Coordinator (opsional bila volume proyek tinggi)" | 1bn7..., bagian 9.4 |
| 21 | Pemilik gate | "G1 Kick-off \| Commercial \| SD dan PM \| Service Delivery Manager", "G2 UAT dan BAST \| SD dan PM \| Pelanggan \| Project Manager", "G3 Serah terima \| SD dan PM \| Operation (NOC, SOC) \| Head of Operation" | 1bn7..., bagian 8 |
| 22 | Pemilik dokumen Operation bertentangan (K-11) | "Pemilik dokumen \| COO (Amirull Yusuf Zulkarnain)" dan "pemilik POL-OPS-001 dan PRO-OPS-001 serta review 6 bulanan" (Head of Operation) | 1bn7..., bagian 1, 9.1 |
| 23 | Pemetaan Erik Dwi Yanto ke NOC (K-10) | "COO: konfirmasi apakah tim Tech Ops yang ada (mis. Erik Dwi Yanto) dipetakan ke NOC." | 1bn7..., bagian 13 |
| 24 | Jabatan Fani di POL-OPS-001 berbeda (K-12) | "Komisaris dan Advisor Fani Fatullah" | 1bn7..., bagian 3 |
| 25 | Penyetuju di POL-OPS-001 (K-14) | "Disahkan oleh \| COO, Amirull Yusuf Zulkarnain" | 1bn7..., Pengesahan |
| 26 | Shift 4 regu berstatus usulan | "(USULAN, jam dan jumlah regu disahkan COO)" | 1bn7..., bagian 5 |
| 27 | Lampiran 2 kosong | "STRUKTUR ORGANISASI PT. STRATEGI INTEGRASI NUSANTARA\n\nJakarta,1 September 2026\n\nPT Sinux\n\nDirektur" | 1FaPdUww..., seluruh isi |
| 28 | Garis Laras ke Direktur Utama (K-01) | config/defaults.json data_conflicts: "Struktur Organisasi: garis tegas ke Direktur (HR-JA-001) dan garis putus-putus ke Direktur Utama, berlabel menunggu konfirmasi" | defaults v21, bukan berkas Drive |
| 29 | Sebutan COO dan Samuel di badan dokumen | defaults: "'Direktur (COO)' pada sebutan pertama, sesudahnya 'COO'"; "badan dokumen: 'Direktur Utama'" | defaults v21 |

## 3. Pemetaan klausul ISO

Checklist tidak memberi acuan klausul untuk baris ini. Bagian Acuan Klausul ISO memuat empat klausul dengan satu label "(USULAN, perlu konfirmasi konsultan)". Judul klausul adalah pengetahuan standar, bukan teks sumber tim.

| Klausul | Di bagian dokumen | Alasan |
|---|---|---|
| ISO 9001:2015 5.3 | Acuan, Bagan, Daftar Jabatan, Matriks Peran | Klausul peran, tanggung jawab, dan wewenang. Job Analysis sendiri memakai 5.3 (bagian 2 sumber) |
| ISO 9001:2015 7.1.2 Orang | Acuan, Daftar Jabatan, Struktur Divisi Operation | Penilaian saya: daftar jabatan dan status terisi atau usulan menunjukkan kecukupan orang. Keterkaitan ini tafsir penyusun |
| ISO/IEC 27001:2022 5.3 | Acuan, Matriks Peran | Klausul yang sama untuk ISMS |
| ISO/IEC 27001:2022 Annex A 5.2 | Acuan, Matriks Peran | Peran keamanan informasi. Dipakai bersama Lead SOC, VP Tech Operation and Services, ISMS Coordinator |

7.2, 7.3, dan 7.5 yang dipakai Job Analysis tidak dimasukkan karena menyangkut kompetensi dan informasi terdokumentasi, bukan struktur organisasi.

## 4. Keputusan data dan tafsir

1. Garis lapor: seluruh garis berasal dari Job Analysis (Draft) dan baru resmi sesudah dokumen ini disahkan (Dasar paragraf 2). Dua nilai di bagan: garis tanpa label (satu atasan tertulis di sumber) dan garis berlabel menunggu konfirmasi (atasan tidak tunggal atau ditandai sumber). Pilihan ini mengikuti defaults (hanya garis Laras dan Aziz yang diberi label di defaults), diperluas ke JA-01, JA-05, JA-08, JA-10, JA-11 karena sumber sendiri menandainya. Bila LEAD menghendaki semua garis berlabel, ubah edges di specs/HR-ORG-01.json.
2. JA-08, JA-10, JA-11, JA-14 ditempatkan di bawah Direktur karena garis ke Direktur disebut dalam teks sumber ("Management / Direktur", "Direktur atau Management"). Penempatan itu tafsir, diberi (USULAN) di K-03 dan K-04.
3. Head of Operation: sumber Job Analysis tidak punya jabatan itu; POL-OPS-001 menaruhnya di bawah COO. Hubungan dengan VP Tech Operation and Services (JA-04) tidak dikarang, jadi dijadikan K-09 dan Gambar 3 berdiri sendiri.
4. Erik Dwi Yanto (JA-13) tetap di bawah JA-04 pada Gambar 1. Pemetaannya ke NOC tidak dilakukan (K-10).
5. Nama dan jabatan mengikuti defaults data_conflicts: Kristanto (bukan Kristianto), HR Manager (bukan HR Lead), Sita Nadia Salsabila Widodo, Direktur Utama di badan dokumen. Ejaan "Ahmad Rifa'i" mengikuti Job Analysis (POL-OPS-001 menulis "Rifai"); dokumen kepegawaian lebih tepat sebagai sumber ejaan nama.
6. "Direktur (COO)": sebutan pertama ada di tabel Definisi (bagian 3); setelah itu Direktur dipakai untuk JA-02 dan COO hanya di bagian Struktur Divisi Operation (aturan dicatat di K-08). Badan dokumen tidak memakai CEO. President Director hanya muncul di blok Approved By.
7. Normalisasi nama unit: Operations dan Operation menjadi Operation; HR / GA, Human Resources, HRGA / General Affairs menjadi Human Resources; atasan JA-06 dan JA-07 menjadi VP Commercial (JA-03). Fungsi General Affairs tidak dijadikan unit sendiri karena sumber memasukkan Office Helper di bawah HRGA Officer.
8. Matriks peran: tiga kelompok baris. (a) Tertulis di sumber: JA-01, JA-02, JA-04, Process Owner JA-14, dengan kalimat tanggung jawab dari uraian jabatan. (b) Jabatan Operation (USULAN) dari POL-OPS-001: pemilik gate G1, G2, G3. (c) Peran tanpa padanan jabatan: ISMS Coordinator, Finance Lead, Finance Staff, dibiarkan "Belum ditetapkan" atau "Belum dipetakan" tanpa mengarang pemegang; Line Manager Legal dan Staff Legal dipasangkan ke JA-08 dan JA-09 sebagai (USULAN) karena JA-09 melapor ke JA-08.
9. Peran yang tidak saya masukkan ke matriks: peran dari dokumen lain (mis. Commercial Manager, Presales, Sales Executive) karena bukan bahan baris ini dan pemetaannya tidak ada di sumber. Dicatat di open item 18.
10. Kode dokumen di Dokumen Terkait memakai nomor draf dari config/worklist.json (SNX-HR-JA-01, SNX-FAT-SOP-01, SNX-FAT-SOP-05, SNX-LEG-SOP-01, SNX-ISMS-PRO-01). POL-OPS-001 memakai kode sumbernya, yang berlabel penomoran USULAN di sumber.
11. Pelaku tinjauan tahunan (HR Manager) diambil dari process_owner dan review_period YEARLY di defaults, ditambah "12 bulan sejak efektif atau saat ada perubahan signifikan" dari Job Analysis.
12. Isi sumber yang berbentuk kalimat perintah: tidak ada yang ditujukan ke penyusun. Kalimat normatif Job Analysis ("harus dikonfirmasi oleh manajemen sebelum pengesahan", "harus diselesaikan sebelum dokumen diberi status Controlled / Effective") dan kotak keputusan COO di POL-OPS-001 bagian 13 dicatat sebagai K dan open item, tidak dijalankan.

## 5. Penanganan cacat context/audit

grep -n pada tiga fileId: 1m91... ada di iso-sinux-supdocs-hr (bagian HR-JA-001) dan sintesis; 1bn7... ada di iso-sinux-supdocs-ops (bagian POL-OPS-001) dan sintesis; 1FaPdUww... tidak ditemukan di context/audit (tidak ada catatan cacat; README audit menyebutnya kosong, dan saya buktikan sendiri lewat decode docx).

### 5.1 HR-JA-001 (bagian 5 Catatan kualitas dan celah)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status DRAF, Revision "03 -", Effective Date "-", nomor "usulan" | Tidak diwarisi: dokumen ini Draft, Rev 00, Effective Date kosong. Bagian Dasar menyebut Job Analysis berstatus Draft dan menurunkan konsekuensinya: garis lapor baru resmi sesudah disahkan |
| 2 | Tidak ada KPI, bagan, grade; posisi kosong tidak dicantumkan | Bagan dibuat di sini (Gambar 1 dan 2). KPI, grade, dan posisi kosong dikecualikan eksplisit di Ruang Lingkup, dengan KPI Matrix dan Authority Matrix di Dokumen Terkait |
| 3 | Kalimat terpotong di bagian 1 paragraf 2 | Tidak dikutip. Ketentuan memakai kalimat utuh dari bagian 2 sumber |
| 4 | Frasa kompetensi janggal (mis. "pihak terkait management", "Risk pemahaman karyawan") | Tidak berlaku: dokumen ini tidak memuat kompetensi. Kalimat uraian jabatan yang dikutip (JA-01 A.3, A.7; JA-02 A.5; JA-04 A.4) saya periksa dan bersih dari frasa itu. Perbaikan frasa menjadi tugas HR-JA-01 |
| 5 | Pelaporan JA-05 tidak konsisten | Diperbaiki sebagian: Gambar 1 menggambar dua garis, satu tegas ke Direktur dan satu berlabel ke VP Commercial; keputusannya K-02 |
| 6 | Atasan JA-06 dan JA-07 ditulis nama departemen | Diperbaiki: ditulis VP Commercial (JA-03); perubahan dicatat K-06 |
| 7 | Atasan JA-08, JA-10, JA-11, JA-14 tidak tunggal | Tidak diputus diam-diam: garis berlabel menunggu konfirmasi, K-03 dan K-04, penempatan di bawah Direktur ditandai (USULAN) |
| 8 | Nama unit tidak seragam | Diperbaiki: satu nama per unit; asalnya dicatat K-06 |
| 9 | Dua jabatan berjudul sama "Legal & Compliance" | Dibedakan lewat garis lapor (kalimat di Daftar Jabatan) dan kode JA; pemasangan Line Manager Legal dan Staff Legal berlabel (USULAN), K-13 |
| 10 | Finance Lead dan Finance Staff tidak punya jabatan | Tidak dikarang: baris "Belum dipetakan" di Matriks Peran, K-13 |
| 11 | Ejaan Samuel dan sebutan CEO | Diperbaiki: Kristanto, Direktur Utama; CEO tidak dipakai di badan dokumen; K-07 |
| 12 | Teks B dan F identik di 15 jabatan; kalimat batasan umum identik | Batasan umum dikutip satu kali sebagai satu paragraf di Matriks Peran, tidak diulang per jabatan |
| 13 | Masa pengalaman minimum belum ada | Tidak berlaku bagi dokumen ini |
| 14 | Jumlah tabel 34 lawan 17 | Tidak berlaku bagi dokumen ini |
| 15 | Bagian 2 menyebut 7.3 dan 7.5 tanpa teks klausul; tidak ada rujukan 27001 | Dokumen ini memakai 5.3 dan 7.1.2 serta 27001 5.3 dan Annex A 5.2, semua berlabel (USULAN, perlu konfirmasi konsultan) |

### 5.2 POL-OPS-001 (bagian 5 Catatan kualitas dan celah)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | DRAFT v0.1, tanda tangan kosong, kode penomoran USULAN | Dokumen Terkait menyebut "DRAFT v0.1, penomoran masih USULAN" |
| 2 | Banyak butir USULAN | Label dipertahankan untuk delapan jabatan, garis ke COO, dan pola kerja 4 regu; tidak ada yang dinaikkan menjadi fakta |
| 3 | Pemilik dokumen COO lawan Head of Operation | Tidak diputus: K-11 |
| 4 | Baseline KPI tidak ada | Tidak berlaku (KPI dikecualikan) |
| 5 | Nama pemegang delapan jabatan kosong | Tidak dikarang: kolom pemegang di matriks berstatus "belum ada pemegang"; K-10, termasuk pemetaan Erik |
| 6 | Sistem tiket GLPI lawan Zammad | Tidak berlaku, dokumen ini tidak menyebut sistem tiket |
| 7 | Rujukan internal AI dan istilah informal | Tidak ada yang disalin. "om Ipe", "japri", kode DOCTRINE, DEC, HANDOVER, SKILL tidak muncul; lint lulus |
| 8 sampai 11, 13 | Definisi P1, AegisWAF lawan Wazuh, runbook, RACI Change Major, target pulih | Tidak berlaku; RACI tidak disalin, pemilik gate diambil langsung dari tabel gate bagian 8 |
| 12 | Tidak ada klausul ISO | Klausul ditambahkan dengan label (USULAN, perlu konfirmasi konsultan) |
| tambahan | Fani "Komisaris dan Advisor" lawan VP Tech Operation and Services | Diperbaiki: VP Tech Operation and Services (data_conflicts dan premis owner); K-12 meminta POL-OPS-001 diselaraskan. Frasa lama sengaja tidak ditulis di dokumen (lint melarangnya) |

## USULAN

Lint menghitung 13 kemunculan "(USULAN)" di dokumen: 12 menempel pada tujuh butir di bawah, satu adalah istilah "(USULAN)" di tabel Definisi. Ditambah satu label klausul. Dikelompokkan menjadi 7 butir:

| # | Butir | Letak di dokumen | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Delapan jabatan Divisi Operation: nama jabatan, jenjang, headcount, garis lapor ke COO (6 kemunculan label: Struktur Divisi Operation, caption Gambar 3, empat baris matriks peran) | Bagian 7, Matriks Peran | Label dari sumber POL-OPS-001, dipertahankan | owner (sebagai COO) |
| U2 | Pola kerja shift 4 regu dan jam kantor tiap jabatan | Tabel Struktur Divisi Operation, kolom Pola kerja | Sumber menandai jumlah regu USULAN | owner (sebagai COO), Fani |
| U3 | Pelanggan, vendor, dan partner tidak digambar di bagan | Ruang Lingkup | Sumber diam; penyusun menarik batas | Aziz |
| U4 | JA-08, JA-10, JA-11 ditempatkan di bawah Direktur sebelum atasan tunggal diputus | Gambar 2, Daftar Jabatan, K-03 | Sumber menulis "Management / Direktur" | owner, Samuel |
| U5 | JA-14 ditempatkan di bawah Direktur sebelum atasan tunggal diputus | Gambar 2, Daftar Jabatan, K-04 | Sumber menulis "Direktur atau Management sesuai struktur yang disahkan" | Aziz, owner |
| U6 | Line Manager Legal = JA-08 dan Staff Legal = JA-09 | Matriks Peran, K-13 | Disimpulkan dari JA-09 melapor ke JA-08; sumber tidak menyatakan | Legal |
| U7 | Empat klausul ISO: 9001 5.3 dan 7.1.2, 27001 5.3 dan Annex A 5.2 | Acuan Klausul ISO | Checklist tanpa acuan klausul; label "(USULAN, perlu konfirmasi konsultan)" | owner, diteruskan ke konsultan |

Garis Laras ke Direktur Utama (K-01) tidak berlabel (USULAN) karena berasal dari keterangan owner di defaults; keputusan tetap menunggu konfirmasi.

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Berkas tim untuk checklist baris 21 (1dcziYriRHtTq8E_9QUtTVMe48xvRKNp0) tidak terlihat oleh konektor. Minta tim membagikan berkas itu. Bila isinya beda dari Job Analysis, dokumen ini perlu direvisi | Aziz (tim HR) |
| 2 | K-01 Garis VP Commercial (JA-03) ke Direktur dan ke Direktur Utama | owner, Samuel |
| 3 | K-02 Atasan Manager of Product Tech (JA-05): Direktur atau VP Commercial | owner, Samuel |
| 4 | K-03 Atasan Legal & Compliance (JA-08), Finance (JA-10), Accounting & Tax (JA-11). Catatan audit: Jobdesk Line Manager Legal menulis atasan lain, SOP Legal berisi placeholder, jadi tiga versi | owner, Samuel, Legal |
| 5 | K-04 Atasan HR Manager (JA-14) | Aziz, owner |
| 6 | K-05 Organ perusahaan di atas Direktur Utama menurut anggaran dasar | Samuel, Legal |
| 7 | K-06 Penamaan: HR Manager lawan HR Lead, nama unit, atasan JA-06 dan JA-07 | Aziz, owner |
| 8 | K-07 Ejaan Kristanto lawan Kristianto, dan sebutan Direktur Utama lawan President Director di blok Approved By | owner, Samuel |
| 9 | K-08 Sebutan Direktur lawan COO untuk JA-02 | owner |
| 10 | K-09 Hubungan Head of Operation dengan VP Tech Operation and Services (JA-04) | owner (COO), Fani |
| 11 | K-10 Pemegang delapan jabatan Operation, headcount riil, pemetaan Erik Dwi Yanto ke NOC | owner (COO) |
| 12 | K-11 Pemilik POL-OPS-001: COO atau Head of Operation | owner (COO), Fani |
| 13 | K-12 Penyelarasan jabatan Fani di POL-OPS-001. Tanggal efektif jabatan VP belum disebut siapa pun | owner, Fani |
| 14 | K-13 Pemetaan ISMS Coordinator, Finance Lead, Finance Staff ke jabatan; konfirmasi Line Manager dan Staff Legal. Jawaban owner 14 Okt untuk nama MR, ISMS Coordinator, Ketua Tim ISO: "ini belum terpikir juga". Belum jelas apakah ketiganya satu peran | owner, FAT, Legal |
| 15 | K-14 Penyetuju dokumen ini: Direktur Utama (template) lawan Management / Authorized Director (Job Analysis) lawan COO (dokumen Operation) | owner, Samuel |
| 16 | Konsultan: apakah dokumen ini dipakai mengisi Lampiran 2 yang kosong (1FaPdUww...), dan konfirmasi empat klausul USULAN | owner, konsultan |
| 17 | Garis putus-putus tidak bisa digambar karena renderer hanya mendukung label teks (lihat GAP). Label "menunggu konfirmasi (K-nn)" dipakai sebagai pengganti. Bila LEAD ingin garis putus-putus, perlu entri LEAD-GUIDE dan perubahan render_flow yang lolos selftest | LEAD |
| 18 | Peran dari dokumen lain yang belum dipetakan ke jabatan (mis. Commercial Manager, Presales, Sales Executive) tidak dimasukkan; tambahkan bila owner memutus pemetaannya | owner, Laras |
| 19 | Kode SNX di Dokumen Terkait memakai nomor draf worklist; cek ulang pada W8 bahwa dokumen itu ada dan memakai nama peran yang sama dengan Matriks Peran | orkestrator |
| 20 | Pihak eksternal (pelanggan, vendor, partner) dikecualikan dari bagan karena sumber diam (U3) | Aziz |

## GAP

| # | GAP | Mitigasi yang diusulkan |
|---|---|---|
| 1 | defaults meminta garis putus-putus untuk garis Laras dan Aziz; tools/render_sop.py (render_flow) tidak punya gaya garis. Saya tidak boleh mengubah tools | Label teks "menunggu konfirmasi (K-nn)" pada garis; keterangan di bagian Bagan Organisasi. Usul ke LEAD: tech_fix kecil di render_flow bila ingin gaya putus-putus |
| 2 | Berkas tim baris 21 tidak terbaca (open item 1) | Dokumen disusun dari Job Analysis, POL-OPS-001, Lampiran 2 sebagai sumber worklist; direvisi bila berkas dibagikan |
| 3 | Kolom Description checklist kosong, tanpa acuan klausul | Klausul disusun penyusun dan berlabel (USULAN, perlu konfirmasi konsultan) |
| 4 | Tabel di dokumen tampil rata kanan-kiri dengan celah lebar pada sel pendek (gaya template). Tidak saya ubah (D4) | Tidak ada; keputusan Aziz atas template |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan yang saya lakukan:
- Pengulangan penjelasan label yang sama di empat tempat (Ruang Lingkup, Dasar, Daftar Jabatan, Butir Menunggu Konfirmasi). Terdengar seperti bahan pengisi. Saya hapus tiga, menyisakan penjelasan di bagian Dasar dan Bagan.
- Kalimat Ruang Lingkup yang menyatakan status USULAN delapan jabatan, lalu diulang di Struktur Divisi Operation. Saya hapus yang pertama.
- Aturan pemakaian COO ada di tabel Definisi (campur arti dan aturan). Saya pindahkan ke K-08, definisi tinggal artinya.
- "Pengawas kepatuhan" untuk JA-02 adalah kata saya; sumber memakai "Memastikan kepatuhan". Saya ganti menjadi "Penanggung jawab kepatuhan".
- "Keterangan pimpinan SINUX" di K-01 adalah atribusi kabur. Saya ganti menjadi "keterangan tambahan saat dokumen ini disusun".
- Kalimat Tujuan kedua punya tiga unsur (peran, tanggung jawab, wewenang). Ini bunyi judul klausul 5.3, bukan kelompok tiga yang dipaksakan, jadi saya biarkan.
- Label "(USULAN)" muncul 13 kali dan "menunggu konfirmasi" belasan kali. Terdengar mekanis, tapi RUNBOOK menuntut label itu dan tiap kemunculan menempel pada butir yang berbeda.
- Tidak ada pembuka generik, penutup positif, em-dash, en-dash penyambung kalimat, tebal, huruf kapital, atau tanda kutip untuk penekanan. Lint gaya lulus.
- Tabel Definisi dan tabel peran sengaja berisi kalimat pendek satu klausa; panjangnya bervariasi mengikuti isi sumber.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Garis JA-03 ke Direktur Utama: bukan dari tiga sumber Drive; dari defaults (kata owner), berlabel menunggu konfirmasi (K-01).
- Baris Matriks Peran untuk ISMS Coordinator, Finance Lead, Finance Staff, Line Manager Legal, Staff Legal: nama peran dan dokumen pemakainya dari salinan context/audit dan defaults (prepared_reviewed FAT dan LEG), bukan dari tiga sumber Drive. Pemasangan Line Manager dan Staff Legal ke JA-08 dan JA-09 adalah (USULAN). Peran "pemilik dokumen SNX-ISMS-PRO-01 = ISMS Coordinator" dari salinan audit ISMS (owner_in_doc), belum saya cek ke Drive.
- Judul dan nomor klausul ISO 9001 5.3, 7.1.2, 27001 5.3, Annex A 5.2: pengetahuan standar, tanpa sumber tim, berlabel (USULAN, perlu konfirmasi konsultan). Keterkaitan 7.1.2 adalah tafsir.
- Definisi NOC, SOC, HRGA, SD dan PM, ISMS: diturunkan dari kalimat tugas di sumber (POL-OPS-001 9.2, 9.3, 9.4; JA-12 A.1 dan A.4), bukan kalimat definisi sumber. ISMS = sistem manajemen keamanan informasi adalah istilah standar ISO/IEC 27001.
- "Tidak ada" pada kolom Membawahi untuk NOC Engineer, SOC Analyst, Project Manager, Project Coordinator: sumber hanya tidak menyebut bawahan; kesimpulan "tidak ada" berasal dari ringkasan audit (bagian 9 ringkasan jabatan), bukan teks sumber.
- "Jam kantor" untuk Service Delivery Manager, Project Manager, Project Coordinator: dari kalimat "SD dan PM bekerja jam kantor" di bagian 3 sumber; untuk Head of Operation sumber tidak menyebut, ditulis "Tidak disebut di sumber".
- Batas "pelanggan, vendor, dan partner dikecualikan": keputusan penyusun (U3).
- Penyeragaman nama unit dan "VP Commercial" untuk atasan JA-06 dan JA-07: keputusan penyusun, dicatat K-06.
- Nomor SNX-HR-JA-01, SNX-FAT-SOP-01, SNX-FAT-SOP-05, SNX-LEG-SOP-01, SNX-ISMS-PRO-01 dari config/worklist.json (nomor draf).
- Tanggal: tidak ada tanggal di dokumen. Tanggal Lampiran 2 (1 September 2026) dan tanggal POL-OPS-001 (12 Oktober 2026) tidak dipakai.
- Angka: 15 jabatan, 8 jabatan, 4 regu, 12 bulan semuanya dari sumber atau defaults; tidak ada angka karangan.

## Sweep

Putaran sweep sesudah DONE. Hanya dua butir dikerjakan; fakta, angka, nama, dan struktur dokumen tidak berubah. 17 sel atau kalimat di specs/HR-ORG-01.json diubah (butir 1: 16 lokasi, butir 2: 1 lokasi), ditambah penyelarasan label di notes ini.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1 | Dokumen Terkait: "Billing & Invoicing. Dokumen sumbernya memakai peran Finance Lead dan Finance Staff." | "Billing & Invoicing. Memuat peran Finance Lead dan Finance Staff." |
| 1 | Dokumen Terkait: "Tax Administration & Reporting. Dokumen sumbernya memakai peran Finance Lead dan Finance Staff." | "Tax Administration & Reporting. Memuat peran Finance Lead dan Finance Staff." |
| 1 | Dokumen Terkait: "Legal Operational. Dokumen sumbernya memakai peran Line Manager Legal dan Staff Legal." | "Legal Operational. Memuat peran Line Manager Legal dan Staff Legal." |
| 1 | Matriks Peran, kolom Dasar (Finance Lead dan Finance Staff): "Dokumen sumber SNX-FAT-SOP-01 dan SNX-FAT-SOP-05" | "SNX-FAT-SOP-01 dan SNX-FAT-SOP-05" |
| 1 | Matriks Peran, kolom Dasar (Line Manager Legal dan Staff Legal): "Dokumen sumber SNX-LEG-SOP-01" | "SNX-LEG-SOP-01" |
| 1 | Bagan Organisasi, pengantar: "Garis tanpa label tercantum sebagai satu atasan langsung di sumber." | "Garis tanpa label menunjukkan satu atasan langsung yang tertulis di Job Analysis." |
| 1 | Butir Menunggu Konfirmasi, header kolom: "Keadaan di sumber" | "Keadaan saat ini" |
| 1 | K-13: "Sumber tidak menunjuk jabatan untuk ISMS Coordinator, Finance Lead, dan Finance Staff; Job Analysis hanya memuat JA-10 Finance dan JA-11 Accounting & Tax. ... tanpa pernyataan di sumber." | "Job Analysis tidak menunjuk jabatan untuk ISMS Coordinator, Finance Lead, dan Finance Staff; yang ada hanya JA-10 Finance dan JA-11 Accounting & Tax. ... Job Analysis tidak menyatakan pemasangan itu." |
| 1 | Matriks Peran, kolom Status (empat baris): "Tercantum di sumber" | "Tercantum di Job Analysis" |
| 1 | Ruang Lingkup, tabel pengecualian: "Tidak digambarkan di bagan karena sumber tidak memuatnya (USULAN)." | "Tidak digambarkan di bagan karena Job Analysis dan POL-OPS-001 tidak memuatnya (USULAN)." |
| 1 | Struktur Divisi Operation, Pola kerja Head of Operation: "Tidak disebut di sumber" | "Tidak disebut di POL-OPS-001" |
| 2 | Acuan Klausul ISO: "(USULAN, dikonfirmasi konsultan)" | "(USULAN, perlu konfirmasi konsultan)"; label yang sama di notes ini diselaraskan (7 tempat) |

Catatan untuk orkestrator, tidak saya ubah karena di luar daftar butir:
- Kata "sumber" masih ada di badan dokumen pada tabel Definisi ("Menunggu konfirmasi": "di sumbernya") dan bagian Dasar (paragraf 2 "sumbernya sendiri", paragraf 4 "Bila sumber memakai sebutan lain"). Bila ingin bersih, ganti menjadi "di Job Analysis atau POL-OPS-001".
- GAP 1 dan open item 17 di notes ini sudah usang: tools/render_sop.py sekarang menggambar garis berlabel "menunggu konfirmasi" putus-putus (render_flow baris 192), dan pemeriksa mengonfirmasinya di gambar hasil render. Syarat garis putus-putus untuk Laras dan Aziz terpenuhi. Butir itu saya biarkan karena sweep membatasi perubahan.
- Temuan nonblocking di qa/HR-ORG-01.verify.json di luar dua butir sweep tidak dikerjakan.
