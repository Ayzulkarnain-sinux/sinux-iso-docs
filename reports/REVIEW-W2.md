# REVIEW-W2 (2026-10-14T23:04:15Z)

## SNX-OPS-PRC-01 Operations Business Process Flow
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-PRC-01 Operations Business Process Flow (Rev00 DRAFT).docx
- Sumber: SNX-OPS-PRC-01_Operations_Business_Process_Flow.docx (15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0, modifiedTime 2026-10-13T06:09:03Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Operation berhak menolak serah terima G3 secara tertulis; selama G3 belum lolos layanan berstatus hypercare dengan pemilik SD dan PM | "Operation berhak menolak serah terima G3 secara tertulis bila checklist belum lengkap. Selama G3 belum lolos, layanan berstatus hypercare dengan pemilik SD dan PM." (Bagian 6) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |
| 2 | Perubahan atas proses ini diajukan ke Head of Operation, dikaji dampaknya terhadap SLA dan keamanan informasi, lalu disahkan COO | "Perubahan pada proses ini diajukan ke Head of Operation, dikaji dampaknya terhadap SLA dan keamanan informasi, lalu disahkan COO sebelum dokumen direvisi." (Bagian 9) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |
| 3 | Setiap deal baru berpindah tangan tiga kali dan tiap perpindahan wajib lolos gate tertulis; pemilik gate G1 Service Delivery Manager, G2 Project Manager, G3 Head of Operation | "Setiap deal baru berpindah tangan tiga kali. Tiap perpindahan wajib lolos gate tertulis:" dan "G3 Serah terima operasi \| SD dan PM \| NOC dan SOC \| Head of Operation \| Checklist G3 pada SNX-OPS-FRM-06" (Bagian 6) | 15GrP-ihMm6MC5szQqlAgGlmWjnQ5TmH0 |

### USULAN
Daftar USULAN berlabel (lint menghitung 5 butir).

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | SNX-COM-SOP-01 sebagai prosedur proses 1 (sumber menulis "Prosedur Commercial" tanpa kode) | Bagian 6.1 langkah 1; baris Dokumen terkait SNX-COM-SOP-01 | owner |
| U2 | Kick-off internal 3 hari kerja sejak PO (label USULAN di PRO-OPS-001 SDPM-01) | Bagian 8 baris 1 | Fani |
| U3 | Durasi hypercare standar 2 minggu (label USULAN di POL-OPS-001 Bagian 8) | Bagian 8 baris 2 | Fani |
| U4 | Change request dan Shift Log dicatat di Service Hub; batas dengan Zammad belum diputus | Bagian 4 butir 8 | owner |
| U5 | Status lima jabatan Divisi Operation (Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager, Project Manager) tetap usulan dan belum ada pemegang bernama (label dari POL-OPS-001 dan HR-ORG-01 K-10) | Bagian 3, baris Jabatan Divisi Operation | owner, Fani |

Tidak diberi label tetapi bersumber dari bahan dan patut dikonfirmasi: pemilik rekaman = pemilik proses (asumsi 7), pelaku Checklist G3 (asumsi 4), syarat gate dari POL dan PRO (asumsi 5), hari kerja ke-5 laporan SLA (asumsi 15). Semuanya masuk open items.

### Open items
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis COO (Amirull), defaults dan template menulis Samuel (President Director). Defaults dipakai di blok Approved By, tetapi bagian 6.3 langkah 3 memuat COO sebagai pengesah perubahan proses sesuai kalimat sumber. Selaraskan peran pengesah perubahan dan penanda tangan dokumen | owner, Samuel |
| 2 | Pemeriksa dan penyusun: sumber menulis Head of Operation dan ISO/ISMS Coordinator, defaults menulis Erik dan Fani. ISMS Coordinator belum dipetakan ke jabatan (HR-ORG-01 K-13). Sebutan "Direktur (COO)" menunggu konfirmasi owner | owner, Fani |
| 3 | Hypercare: teks sumber (selama G3 belum lolos, pemilik SD dan PM) berbeda dari gambar sumber (sesudah G3, 2 minggu usulan) dan dari POL-OPS-001 Bagian 9.2 dan PRO-OPS-001 tabel 8.1 (Lead NOC pemilik). Dokumen mengikuti teks. Konfirmasi urutan, pemilik, dan apakah 2 minggu berlaku sebelum atau sesudah G3 | Fani |
| 4 | SNX-COM-SOP-01 dipilih sebagai prosedur proses 1 (menutup cacat "Prosedur Commercial" tanpa kode). Belum ada konfirmasi bahwa itu prosedur yang dimaksud | owner |
| 5 | Zammad lawan Service Hub: sumber menaruh change request dan Shift Log di Service Hub, kata owner Zammad untuk Ops. POL-OPS-001 P-08 menulis semua tiket di GLPI. Batas "generalist" belum dirinci. Singkatan GMF pada "tiket GMF dedicated" tidak dijelaskan di sumber | owner |
| 6 | Proses 4 dimiliki Service Delivery Manager, tetapi G2 dimiliki Project Manager dan G3 Head of Operation. Dokumen membedakan pemilik proses dan pemilik gate; konfirmasi pembedaan ini | Fani |
| 7 | Lima jabatan Divisi Operation berstatus usulan tanpa pemegang (HR-ORG-01 K-10); pemilik dokumen ini Head of Operation. Hubungan Head of Operation dengan VP Tech Operation and Services belum diteta

## SNX-OPS-SOP-01 Project Management & Delivery
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-SOP-01 Project Management & Delivery (Rev00 DRAFT).docx
- Sumber: SNX-OPS-SOP-01_SOP_Project_Management_Delivery.docx (1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo, modifiedTime 2026-10-13T06:09:03Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Scope berjalan dari gate G1 sampai gate G3 | "Berlaku sejak paket handover diterima dari Commercial (gate G1) sampai proyek ditutup dan layanan diserahkan ke operasi (gate G3)." (Bagian 2 Ruang lingkup) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo |
| 2 | Tiga ambang waktu SOP: kick-off internal 3 hari kerja setelah PO, eskalasi ke COO bila deviasi jadwal lebih dari 1 minggu, hypercare 2 minggu. Di SOP-01 tanpa label; di POL dan PRO yang lebih baru berlabel USULAN | SOP-01: "Kick-off internal dilaksanakan paling lambat 3 hari kerja setelah PO" (6.1 butir 5); "Deviasi jadwal lebih dari 1 minggu dari baseline, atau isu yang menyentuh biaya, dieskalasi ke COO." (6.4 butir 5); "Hypercare berjalan 2 minggu setelah go-live, kecuali kontrak menetapkan lain." (6.6 butir 3). PRO: "dalam 3 hari kerja sejak PO. (USULAN)" (SDPM-01); "(USULAN ambang)" (SDPM-02); "(USULAN 2 minggu)" (tabel 8.1 baris 10). POL: "Durasi hypercare standar 2 minggu. (USULAN)" (bagian 8) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo; 1U8CAdibwBk9x_-Aic2lbev144d6WReTz; 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |
| 3 | Gate G1: Project Manager memeriksa paket, Service Delivery Manager memutus menerima atau menolak | SOP-01: "Project Manager menerima paket handover dari Commercial dan memeriksanya dengan checklist G1 pada SNX-OPS-FRM-01 (sheet Checklist G1)." (6.1 butir 1) dan "Service Delivery Manager \| Pemilik SOP; menerima atau menolak paket G1; mengawal hubungan pelanggan; menyetujui closure" (Bagian 5). POL: "G1 Kick-off \| Commercial \| SD dan PM \| Service Delivery Manager" (bagian 8, kolom Pemilik gate) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo; 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |

### USULAN
Sepuluh kemunculan label (USULAN) di teks dokumen, tujuh butir berbeda. Tiap butir punya pemutus yang disarankan. Diagram juga memuat label (USULAN) pada simpul hypercare; itu butir U3.

| # | Butir USULAN | Lokasi di spec | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Kick-off internal paling lambat 3 hari kerja setelah PO | 6.1 butir 5; Bagian 8 baris 1 | Angka dari SOP-01; berlabel USULAN di PRO SDPM-01 yang lebih baru | Fani |
| U2 | Eskalasi ke COO bila deviasi jadwal lebih dari 1 minggu dari baseline | 6.4 butir 8; Bagian 8 baris 5 | Angka dari SOP-01; PRO SDPM-02 "(USULAN ambang)" | Fani |
| U3 | Hypercare 2 minggu setelah go-live, kecuali kontrak menetapkan lain | 6.6 butir 3; Bagian 8 baris 6; diagram simpul akhir | Angka dari SOP-01; POL bagian 8 dan PRO tabel 8.1 menulis USULAN | Fani |
| U4 | Target awal 80% proyek selesai sesuai jadwal baseline | Bagian 8 baris 7 | POL bagian 11: "target awal di bawah adalah USULAN" | Fani |
| U5 | Target awal 90% onboarding live sesuai tanggal kontrak | Bagian 8 baris 8 | Sama dengan U4 | Fani |
| U6 | Tiket change request di Zammad, menggantikan "Service Hub" di sumber | Bagian 11 tabel Rekaman, baris Change request log | Kata owner 14 Okt untuk Ops; penerapan ke change request adalah tafsir; preseden OPS-FRM-04 | Owner, dengan Fani |
| U7 | Nama jabatan Divisi Operation (Head of Operation, Lead NOC, NOC Engineer, Lead SOC, SOC Analyst, Service Delivery Manager, Project Manager) berstatus USULAN di POL-OPS-001 | Bagian 3, definisi "NOC, SOC, SD dan PM" | POL bagian 9 dan HR-ORG-01 K-10: nama jabatan, jenjang, headcount adalah USULAN yang disahkan COO | Owner, dengan Fani |

Target 100% (laporan progres tepat waktu, penutupan lengkap) tidak diberi label karena hanya ada di SOP-01 dan tidak dilawan dokume

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults.approved_by mengunci Samuel Kristanto Utomo / President Director (pembalik: form operasional disetujui COO bila owner memutus). Spec memakai defaults | Owner atau Samuel |
| 2 | Penyusun dan pemeriksa di sumber (Service Delivery Manager dan ISO/ISMS Coordinator) diganti Erik dan Fani menurut defaults. Peran ISMS Coordinator belum ditetapkan (HR-ORG-01 K-13) | Owner |
| 3 | Pemilik hypercare: SOP-01 dan POL bagian 8 menulis SD dan PM; PRO tabel 8.1 baris 10 dan POL 9.2 menulis Lead NOC. Dokumen mengikuti SOP-01 | Fani |
| 4 | Urutan hypercare dan G3: SOP-01 menaruh hypercare sesudah pemeriksaan checklist G3 (6.6 butir 2 dan 3); definisi tim menaruhnya sebelum layanan dinyatakan BAU; PRO tabel 8.1 menaruhnya sesudah G3. Spec mempertahankan urutan SOP-01 | Fani |
| 5 | Cara memasukkan lessons learned ke knowledge base SINUX tidak ada dokumennya; jalur internal di sumber dibuang dari dokumen. Pemilik langkah (Project Manager, dari POL 9.4) belum dikonfirmasi | Owner, dengan Fani |
| 6 | Batas "generalist" lawan Ops untuk sistem tiket belum dirinci owner. SOP ini hanya memakai Zammad untuk tiket change request (U6); SNX-OPS-FRM-04 di sumber menyebut Service Hub | Owner |
| 7 | Sumber data KPI "Proyek selesai sesuai jadwal baseline" dan "Onboarding live sesuai tanggal kontrak": SOP-01 FRM-01, POL bagian 11 "Register proyek" dan "Service Hub" | Fani |
| 8 | Pembagian gate G1 (Project Manager memeriksa, Service Delivery Manager memutus) adalah penegasan penyusun dari tiga lokasi sumber. Checklist G1 di FRM-01 berisi 8 butir, di PRO bagian 8.2 berisi 7 butir (menurut notes OPS-FRM-01); SOP ini merujuk FRM-01 | Fani |
| 9 | Pemetaan peran: Te

## SNX-OPS-SOP-02 Project Change Management
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-SOP-02 Project Change Management (Rev00 DRAFT).docx
- Sumber: SNX-OPS-SOP-02_SOP_Project_Change_Management.docx (15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63, modifiedTime 2026-10-13T06:09:04Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Syarat go-gate: lima syarat yang harus terpenuhi sebelum change production dieksekusi; di dokumen ini menjadi aturan di bagian 4 untuk change teknis | "Tidak ada perubahan production yang dieksekusi sebelum lima syarat ini terpenuhi:" (Bagian 4, diikuti lima butir approval tertulis plus ack pelanggan, backup atau snapshot dengan lokasi dicatat, rollback satu perintah atau satu langkah tertulis, eksekusi satu langkah satu waktu, before dan after terdokumentasi) | 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63 |
| 2 | Change Emergency boleh dieksekusi sebelum CR lengkap; CR dilengkapi dalam 1 hari kerja dan ditinjau Head of Operation; COO diberi tahu dalam 30 menit sejak eksekusi | "Lead on-duty boleh mengeksekusi sebelum CR lengkap, dengan tetap mengambil backup bila memungkinkan dan mencatat setiap langkah." dan "CR dilengkapi paling lambat 1 hari kerja setelahnya dan ditinjau Head of Operation." dan "COO diberi tahu dalam 30 menit sejak eksekusi." (Bagian 6.6) | 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63 |
| 3 | Pembagian jenis change berstatus USULAN di kebijakan induk, sehingga bagian 4 dan 8 memberi label (USULAN) pada jenis, kriteria, dan waktu notifikasi | "Pembagian jenis change adalah USULAN; prinsip go-gate di atasnya bersumber dari keputusan owner." (Bagian 7) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |

### USULAN
Lint menghitung 12 kemunculan label (USULAN), dikelompokkan menjadi 6 butir.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Pembagian jenis change (Standar, Normal, Major, Emergency, Proyek), kriteria, approver per jenis, dan waktu notifikasi pelanggan (H-2, H-5 dengan pengingat H-0, saat itu juga). Label berasal dari POL-OPS-001 bagian 7; jenis Proyek hanya ada di SOP-02 | Bagian 4; bagian 5 (Authority); bagian 8 (tiga baris notifikasi) | owner (Direktur, COO); kelas C1 menuntut ACC COO |
| 2 | Pemberitahuan ke COO dalam 30 menit sejak eksekusi untuk change Emergency (titik awal belum tegas) | Butir 6.6; bagian 8 | owner |
| 3 | CR dibuat di Zammad, bukan Service Hub (GLPI) seperti tertulis di sumber, karena CR adalah pekerjaan Divisi Operation. Sama dengan keputusan di SNX-OPS-FRM-04. Batas "generalist" belum dirinci owner | Definisi Zammad; butir 6.1 | owner, dengan Fani |
| 4 | Arti "kontrol positif": pemeriksaan yang membuktikan hasil change yang diharapkan benar-benar terjadi. Sumber memakai istilah itu tanpa definisi | Bagian 3 | Fani |
| 5 | Peninjau PIR change Major dan change yang berakhir rollback adalah Head of Operation. Sumber hanya menyebut tinjauan dalam 5 hari kerja tanpa pelaku; pola: Head of Operation meninjau CR Emergency (6.6) dan pelanggaran go-gate (POL-OPS-001 12) | Bagian 5 (baris Head of Operation); butir 6.5 langkah terakhir | Fani |
| 6 | Target indikator kinerja: 100%, 95%, 100%, tren menurun. POL-OPS-001 bagian 11 menyatakan target awal berstatus USULAN dan dikalibrasi setelah 3 bulan data; tiga dari empat target hanya ada di SOP-02 | Bagian 8 (empat baris indikator) | owner |

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Penanda tangan: sumber menulis Disusun Head of Operation, Diperiksa ISO/ISMS Coordinator, Disetujui COO (Amirull Yusuf Zulkarnain). Dokumen memakai Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo sesuai defaults (D2). Semua baris ini USULAN di Master List | owner atau Samuel |
| 2 | Head of Operation belum punya pemegang (HR-ORG-01 K-10) dan hubungannya dengan VP Tech Operation and Services belum ditetapkan (K-09). Matriks Peran HR-ORG-01 menaruh tanggung jawab atas "perubahan teknis" pada VP Tech Operation and Services, sedangkan SOP-02 tidak menyebutnya sebagai approver atau tempat eskalasi change Major. Pemilik SOP tetap "Head of Operation" mengikuti sumber | owner, Fani |
| 3 | Batas Ops lawan generalist untuk sistem tiket belum dirinci; POL-OPS-001 P-08 masih menulis semua tiket di GLPI. SOP-02 memakai Zammad (USULAN 3) | owner |
| 4 | Satuan hari pada H-2, H-5, H-0 (kalender atau kerja) belum ditetapkan. PRO-OPS-001 NOC-06 menulis pengajuan CR untuk window maintenance minimal 3 hari kerja sebelumnya, angka yang tidak ada di SOP-02; apakah berlaku untuk change Normal dan Major perlu diputus | owner, Fani |
| 5 | Titik awal 30 menit untuk pemberitahuan COO: sejak eksekusi dimulai atau selesai. POL, PRO, dan tabel Bagian 5 sumber tanpa titik awal | owner |
| 6 | Pelaku yang tidak disebut sumber dan ditafsir dokumen: notifikasi pelanggan (terutama change proyek), memastikan ack pelanggan, melengkapi CR Emergency, memberi tahu COO dan pelanggan pada Emergency, memperbarui SNX-ISMS-REG-01, dan melaporkan indikator bagian 8. Pemetaan Pengaju dan Pelaksana ke NOC Engineer, SOC Analyst, dan Service Delivery Manager mengikuti PRO-OPS-001 | Fani |
| 7 | Selisih dengan POL-OPS-001: (a) POL bagian 7 hanya empat jenis tanpa Pr

## SNX-OPS-SOP-03 Preventive & Corrective Maintenance
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-SOP-03 Preventive & Corrective Maintenance (Rev00 DRAFT).docx
- Sumber: SNX-OPS-SOP-03_SOP_Preventive_Corrective_Maintenance.docx (10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc, modifiedTime 2026-10-13T06:09:04Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Lead NOC menyusun jadwal PM tahunan di SNX-OPS-FRM-07, paling lambat Desember | "Lead NOC menyusun jadwal PM tahunan pada SNX-OPS-FRM-07 (sheet Jadwal PM) paling lambat Desember untuk tahun berikutnya." (Bagian 6.1 butir 1) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |
| 2 | PM yang mengubah sistem berjalan sebagai change Standar atau Normal di window maintenance | "PM yang mengubah sistem (patch, restart, perubahan konfigurasi) dijalankan sebagai change Standar atau Normal sesuai SNX-OPS-SOP-02, di window maintenance." (Bagian 6.2 butir 2) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |
| 3 | Dua target kinerja: kepatuhan jadwal PM 95% dan uji restore bulanan 100% | "Kepatuhan jadwal PM (realisasi dibanding rencana) \| 95%" dan "Uji restore bulanan terlaksana per pelanggan backup \| 100%" (Bagian 9) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |

### USULAN
Lint menghitung 1 butir berlabel di dokumen.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Temuan dihitung berulang bila terjadi tiga kali atau lebih pada aset yang sama dalam 30 hari | Bagian 4, paragraf ke-7 | Sumber memakai "temuan berulang" tanpa kriteria. Angka diambil dari ambang insiden berulang SNX-OPS-SOP-04 dan diperluas ke temuan PM, jadi diberi label | Fani |

Butir tanpa label yang memerlukan penegasan pemutus (bukan angka tanpa sumber, tetapi status keputusannya belum final di dokumen sumber): uji restore bulanan 100% (PRO NOC-04 memberi label USULAN) dan pengajuan change Normal 3 hari kerja (PRO-OPS-001 masih DRAFT). Keduanya di open items 5 dan 8.

### Open items
| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults menetapkan Samuel Kristanto Utomo / President Director. Defaults dipakai | Owner atau Samuel |
| 2 | Lead NOC, NOC Engineer, Lead SOC, Service Delivery Manager, dan Head of Operation belum punya pemegang bernama (HR-ORG-01 K-10); hubungan Head of Operation dengan VP Tech Operation and Services belum ditetapkan (K-09). Pemilik SOP tetap Lead NOC, pemeriksa Fani. "ISO/ISMS Coordinator" di sumber belum ditetapkan (K-13) | Owner, Fani |
| 3 | Sistem tiket: POL-OPS-001 P-08 menulis semua tiket di GLPI, sedangkan premis owner memberi Zammad untuk Ops. SOP ini memakai Zammad. SNX-OPS-FRM-08 adalah register rekap; hubungannya dengan tiket di Zammad perlu ditegaskan, juga di SOP-04 dan FRM-09 | Owner, Fani |
| 4 | Cakupan service report: sumber 6.2 butir 3 (tiap PM) lawan FRM-07 Cara pakai 3 (PM yang mengubah sistem dan CM). Dokumen mengikuti FRM-07. Pemeriksaan read-only harian dan mingguan hanya tercatat per bulan di Jadwal PM | Fani, Lead NOC |
| 5 | Uji restore bulanan 100%: SOP-03 tanpa label, PRO-OPS-001 NOC-04 berlabel USULAN, POL 9.2 hanya "memastikan uji restore bulanan berjalan" | Fani |
| 6 | KPI: POL-OPS-001 Bagian 11 tidak memuat kepatuhan jadwal PM dan uji restore, dan memuat "Backup job sukses 98%" yang tidak ada di SOP-03. Baseline KPI belum diukur (POL 11) | Fani |
| 7 | Dua lokasi matriks severity dan matriks eskalasi (SNX-OPS-SOP-04 dan POL-OPS-001 Bagian 6); target pulih (USULAN di SOP-04) tidak ada di POL. Isi belum dibandingkan baris per baris | Fani (lane SNX-OPS-SOP-04) |
| 8 | Pengajuan change Normal minimal 3 hari kerja (PRO NOC-06) lawan notifikasi pelanggan H-2 untuk Normal (POL Bagian 7); satuan hari kalender atau kerja tidak ditegaskan, da

## SNX-OPS-SOP-04 Technical Incident Handling & Escalation
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-SOP-04 Technical Incident Handling & Escalation (Rev00 DRAFT).docx
- Sumber: SNX-OPS-SOP-04_SOP_Technical_Incident_Handling_Escalation.docx (1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG, modifiedTime 2026-10-13T06:09:04Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Ack, update, target pulih, dan eskalasi hierarki per severity; target pulih berlabel USULAN dan sama dengan sheet Target Severity di FRM-08 | Bagian 6, baris P1 Kritis: "15 menit", "Tiap 1 jam", "4 jam", "Lead langsung, COO dalam 30 menit, CEO bila COO tidak tersedia". Kepala kolom: "Target pulih (USULAN)". Catatan di bawah tabel: "Target di atas adalah target internal; target pulih sama dengan sheet Target Severity pada SNX-OPS-FRM-08. Komitmen ke pelanggan mengikuti kontrak masing-masing dan tidak boleh melebihi kapasitas riil." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |
| 2 | Alert dikonfirmasi dari dua sinyal, tiket dibuat dalam 10 menit, lalu dicatat di FRM-08 | Bagian 7.1: "Alert dikonfirmasi minimal dari dua sinyal sebelum dinyatakan insiden." dan "Tiket dibuat paling lambat 10 menit setelah konfirmasi, berisi pelanggan, layanan, waktu mulai, gejala, dan bukti awal, lalu dicatat di SNX-OPS-FRM-08." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |
| 3 | RCA wajib untuk P1 dan P2 dengan FRM-10 dan dikirim dalam 2 hari kerja; insiden berulang menjadi problem | Bagian 7.5: "Insiden P1 dan P2 wajib RCA dengan SNX-OPS-FRM-10, dikirim ke pelanggan via email dalam 2 hari kerja setelah pulih." dan "Insiden berulang (3 kali atau lebih pada layanan yang sama dalam 30 hari) diperlakukan sebagai problem dan wajib RCA walau severity rendah." | 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG |

### USULAN
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
| U9 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo

### Open items
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Rujukan bagian SOP-04 di spec OPS-FRM-10 basi sesudah SOP-04 dirender ke 11 bagian. Pemetaan: definisi insiden "Bagian 4" menjadi bagian 3; severity "Bagian 6" menjadi definisi di bagian 3 dan target di bagian 8; kewajiban RCA "Bagian 7.5" menjadi bagian 4 dan butir 6.5; insiden berulang "Bagian 7.5 butir 3" menjadi definisi di bagian 3 dan aturan di bagian 4 (baris 30, 44, 45, 46, 248 specs/OPS-FRM-10.json). Spec OPS-SOP-03 sudah merujuk SOP-04 tanpa nomor bagian dan tetap benar | LEAD ISO |
| 2 | Rantai eskalasi P1 sumber tidak menyebut Head of Operation (penanggung jawab P1), tidak menyebut pelaku pemberitahuan ke COO dan Direktur Utama, dan tidak menyebut kapan Head of Operation memanggil personel off-duty. Dokumen memakai Lead NOC sebagai pemberi tahu dan tidak menambah langkah pemanggilan | Fani |
| 3 | Pengirim RCA: SOP-04 menulis Service Delivery Manager "memastikan RCA terkirim"; FRM-10 menulis Head of Operation menyetujui dan mengirim. Dokumen memuat keduanya. Perlu satu rumusan | Fani |
| 4 | Titik awal 30 menit COO untuk P1 insiden (USULAN) berbeda dari SOP-02, yang menghitung 30 menit sejak eksekusi change Emergency. Hubungan target pulih 4 jam dengan anggaran downtime 99.9% di SOP-05 juga belum dijelaskan | Fani |
| 5 | Ack P3 "2 jam kerja" dan P4 "1 hari kerja": kalender kerja belum ditetapkan; FRM-08 menghitung jam kalender (ML-00 riwayat review no. 10, status Terbuka, kutipan dari salinan audit) | Fani |
| 6 | Batas Zammad lawan Service Hub: sumber SOP-04 membagi menurut pelanggan (GMF dan internal ke Service Hub); premis owner membagi Ops lawan generalist. Belum jelas apakah insiden teknis GMF masuk Zammad atau Service Hub | Owner |
| 7 | Retensi tiket asal di Zammad dan Service Hub tidak dite

## SNX-OPS-SOP-05 Service Level Agreement (SLA) Monitoring
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-SOP-05 Service Level Agreement (SLA) Monitoring (Rev00 DRAFT).docx
- Sumber: SNX-OPS-SOP-05_SOP_SLA_Monitoring.docx (1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9-, modifiedTime 2026-10-13T06:09:05Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Peringatan dini: bila downtime yang dihitung melewati 50% anggaran sebelum akhir bulan, Lead NOC memberi tahu dua peran dan change non-darurat ditinjau ulang | "Bila downtime yang dihitung melewati 50% anggaran sebelum akhir bulan, Lead NOC memberi tahu Service Delivery Manager dan Head of Operation, dan change non-darurat pada layanan itu ditinjau ulang." (Bagian 6.4 butir 2) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |
| 2 | Siklus bulanan: data dikumpulkan paling lambat hari kerja ke-3, laporan SLA dikirim paling lambat hari kerja ke-5 | "Data dikumpulkan paling lambat hari kerja ke-3 bulan berikutnya." (Bagian 6.2 butir 4) dan "Laporan SLA bulanan dikirim ke pelanggan paling lambat hari kerja ke-5." (Bagian 6.5 butir 1) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |
| 3 | Target standar availability 99.9% per bulan, dengan anggaran downtime sekitar 43 menit untuk bulan 30 hari | "Target standar availability yang dikomunikasikan adalah 99.9% per bulan." (Bagian 4) dan "Untuk 99.9%, anggaran sekitar 43 menit per bulan 30 hari." (Bagian 6.4 butir 1) | 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- |

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiket GMF dan internal di Service Hub, tiket Ops di Zammad; batas "generalist" belum dirinci owner | 6.2 intro | owner |
| 2 | Target response dan resolution per pelanggan dicatat di kolom Catatan sheet Parameter SLA, sampai FRM-09 punya kolomnya | 6.1 intro | Fani |
| 3 | Jabatan "VP Commercial" untuk peran sumber "Commercial" | Bagian 5, langkah 6.6 | owner |
| 4 | Batas hari kerja ke-3 untuk penyerahan data SLA layanan SOC oleh Lead SOC (sumber hanya menyebut batas itu untuk pengumpulan data) | Bagian 8, baris Lead SOC | Fani |
| 5 | Lokasi simpan "Folder Drive Operation" untuk lima rekaman di bagian 11 | Bagian 11, tabel rekaman | Fani |
| 6 | Rekaman baru "Catatan review layanan triwulanan dan masukan kepuasan pelanggan", pemilik Service Delivery Manager, retensi 3 tahun (disamakan dengan FRM-09); diminta klausul 9.1.2, sumber hanya menyebut "masukan kepuasan pelanggan dicatat" tanpa tempat | Bagian 11, tabel rekaman; 6.5 langkah 5 | Fani |

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Ketidakcocokan SOP dan FRM-09: 6.1 meminta target response dan resolution dicatat di Parameter SLA, 6.3 meminta resolution SLA dihitung, tetapi Parameter SLA tidak punya kolom target itu dan Laporan Bulanan tidak punya kolom resolution SLA. Response SLA di Laporan Bulanan hanya untuk tiket P1 dan P2 (kolom "Tiket P1 dan P2", "Di-ack sesuai target"), sedangkan definisi sumber untuk semua tiket per severity. Perlu tambah kolom di FRM-09 atau ubah SOP | Fani |
| 2 | Target pulih internal P1 di SNX-OPS-SOP-04 (4 jam, USULAN) lebih panjang dari anggaran downtime bulanan 43 menit; tidak ada dokumen yang menjelaskan hubungannya. Angka resolution SLA kontrak tidak ada di dokumen mana pun | Fani |
| 3 | Pengecualian downtime: sumber menulis bukti notifikasi maintenance saja, form menulis bukti notifikasi maintenance atau pengecualian kontrak. Perlu konfirmasi bahwa rumusan form yang berlaku, dan siapa menyimpan bukti pengecualian kontrak | Fani |
| 4 | Target mana yang dipakai Response SLA bila kontrak pelanggan dan target Ack SNX-OPS-SOP-04 berbeda (SOP-04 menyebut target-nya internal; sumber SOP-05 menyebut "target per severity") | Fani |
| 5 | Pelaku yang tidak disebut sumber (asumsi 1 sampai 3). Lead NOC mencatat sekaligus memvalidasi downtime (tidak ada pemisahan peran). Peninjau ulang change non-darurat saat peringatan dini, arti "tinjau ulang", media pemberitahuan peringatan dini, dan rekaman tinjauan: tidak ada di sumber. Tidak ada batas waktu untuk peringatan dini, RCA breach, dan penetapan tindakan perbaikan | Fani |
| 6 | Status keputusan berbeda: POL-OPS-001 bagian 11 menyebut target awal KPI USULAN dengan baseline belum diukur (termasuk "Laporan bulanan terkirim hari kerja ke-5 100%"), dan PRO-OPS-001 S
- SOP meminta resolution SLA dihitung di FRM-09 Laporan Bulanan, tetapi FRM-09 tidak punya kolom target response/resolution; Fani memutus penambahan kolom.

## SNX-ISMS-PRO-01 Information Classification & Handling
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-PRO-01 Information Classification & Handling (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx (1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io, modifiedTime 2026-10-13T06:09:00Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Informasi pelanggan minimal RESTRICTED (butir 4.3) | "Informasi pelanggan minimal RESTRICTED, kecuali pelanggan menetapkan lebih tinggi." | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| 2 | SECRET hanya di password manager (vault) atau sistem khusus ter-encrypt (butir 4.8) | "Hanya password manager internal (vault) atau sistem khusus ter-encrypt; dilarang di dokumen, spreadsheet, chat, tiket, atau email" | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |
| 3 | Syarat sah pengecualian (bagian 9) | "Pengecualian hanya sah bila tertulis, berbatas waktu, disetujui pemilik informasi dan ISMS Coordinator." | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |

### USULAN
Lint menghitung 13 label (USULAN) di dokumen; satu di antaranya baris definisi label itu sendiri. Sisanya 6 keputusan.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Perluasan cakupan prosedur ke seluruh SINUX | Bagian 2 | Judul dan tujuan sumber berbicara tentang informasi SINUX, scope hanya Divisi Operation | Owner |
| U2 | Service Delivery Manager sebagai "Lead" bagi sub divisi Service Delivery dan PM | Definisi Lead sub divisi | Sumber menulis "Lead" tanpa nama jabatan; POL-OPS-001 hanya menyebut Lead NOC dan Lead SOC | Fani |
| U3 | Label SECRET pada subjek email menandai email yang terlanjur memuat SECRET | Butir 4.6 | Menutup pertentangan label email (RESTRICTED atau SECRET) dengan larangan SECRET di email | Fani |
| U4 | Catatan sosialisasi dan catatan pemantauan kepatuhan: lokasi Google Drive, pemilik ISMS Coordinator, retensi 3 tahun | 6.6 langkah 1 dan 2; bagian 11 | Sumber memberi peran sosialisasi dan pemantauan tanpa rekaman. 3 tahun disamakan dengan retensi SNX-ISMS-REG-04 di SNX-ISMS-SOP-02 | Fani |
| U5 | Pemantauan kepatuhan setiap triwulan | Bagian 8 | Sumber tanpa frekuensi; angka mengikuti audit sampling triwulanan di POL-OPS-001 bagian 12 (itu pun USULAN) | Fani |
| U6 | Rekaman persetujuan tertulis (berbagi RESTRICTED ke pihak luar, removable media, pengecualian): lokasi Zammad atau Service Hub, pemilik ISMS Coordinator, retensi 3 tahun | Bagian 11 | Sumber mensyaratkan persetujuan dan pengecualian tertulis tanpa menyebut tempat dan masa simpannya | Fani |

### Open items
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
| 9 | Pelaku tidak disebut sumber, ditulis tafsi

## SNX-ISMS-SOP-01 Information Security Incident Management
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-SOP-01 Information Security Incident Management (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-SOP-01_SOP_IS_Incident_Management.docx (1MApsp9RPPMO1Xottjb2fGQJlaQas2M99, modifiedTime 2026-10-13T06:09:00Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Bila data pribadi terlibat, COO dan Legal memutuskan pemberitahuan ke subjek data dan lembaga berwenang, batas 3 x 24 jam sejak diketahui | "Bila insiden melibatkan kegagalan pelindungan data pribadi, COO dan Legal memutuskan pemberitahuan kepada subjek data dan lembaga berwenang sesuai UU PDP (paling lambat 3 x 24 jam sejak diketahui)." (Bagian 11 butir 2) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |
| 2 | Aturan forensik: bukti diamankan sebelum mengubah apa pun | "Forensik terlebih dahulu, perbaikan kemudian: amankan bukti (log, hash file, daftar proses, koneksi aktif, snapshot bila memungkinkan) sebelum mengubah apa pun." (Bagian 9 butir 1) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |
| 3 | Severity P1: kriteria, Ack 15 menit, pemberitahuan internal | "P1 \| Kompromi root atau host baru; kebocoran data pelanggan atau data pribadi; ransomware; akses tidak sah ke sistem kritis \| 15 menit \| Lead SOC dan Head of Operation segera; COO dalam 30 menit" (Bagian 8, tabel severity) | 1MApsp9RPPMO1Xottjb2fGQJlaQas2M99 |

### USULAN
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

### Open items
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
| 10 | Peran pemberi keputusan notifikasi pelanggan (tabel peran sumb

## SNX-ISMS-SOP-03 Backup & Recovery
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 1; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-SOP-03 Backup & Recovery (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-SOP-03_SOP_Backup_Recovery.docx (1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc, modifiedTime 2026-10-13T06:09:01Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Restore ke lokasi produksi butuh dua persetujuan, dan restore ke lokasi uji didahulukan bila memungkinkan | "Restore ke lokasi produksi butuh approval Lead NOC dan persetujuan tertulis pelanggan; restore ke path uji terlebih dahulu bila memungkinkan, untuk menghindari menimpa data terbaru." (Bagian 7.3 butir 2) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |
| Frekuensi uji restore: bulanan untuk pelanggan berlayanan backup, triwulanan untuk sistem internal kritis | "Uji restore minimal bulanan untuk setiap pelanggan berlayanan backup, dan minimal triwulanan untuk sistem internal kritis." (Bagian 7.4 butir 1) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |
| Job gagal 2 kali berturut-turut menjadi tiket P2 | "Job gagal dijalankan ulang secepatnya; gagal 2 kali berturut-turut menjadi tiket P2 sesuai SNX-OPS-SOP-04." (Bagian 7.2 butir 2) | 1z6y_n2i6cTN6C1y7alJsCasuy9hU6Qzc |

### USULAN
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
| U9 | Tindak lanjut penggunaan repository d

### Open items
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
| 9 | Lead SOC: sumber memberi tanggung jawab "memastikan backup terlindungi dari ransomware da
- Rekaman analisis akar kegagalan backup ditulis 'di tiket P2', sedangkan SNX-OPS-SOP-04 memakai SNX-OPS-FRM-10; selaraskan (Fani).

## SNX-ISMS-SOP-04 IT Asset & Configuration Management
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-SOP-04 IT Asset & Configuration Management (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-SOP-04_SOP_IT_Asset_Configuration_Management.docx (1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg, modifiedTime 2026-10-13T06:09:01Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Aset baru didaftarkan paling lambat saat mulai dipakai, aset pelanggan sebelum gate G3 | "Aset baru didaftarkan di SNX-ISMS-REG-01 paling lambat saat aset mulai dipakai, dan wajib sebelum gate G3 untuk aset pelanggan." (Bagian 6.1) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |
| 2 | Media dipakai ulang di-wipe, yang tidak dipakai ulang dihancurkan fisik | "Media penyimpanan yang akan dipakai ulang di-wipe dengan metode overwrite atau secure erase; yang tidak dipakai ulang dihancurkan fisik." (Bagian 6.5) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |
| 3 | Drift diperiksa minimal triwulanan dan dianalisis bila tanpa change | "Drift diperiksa minimal triwulanan dengan membandingkan konfigurasi aktual ke baseline; drift tanpa change dianalisis sebagai event keamanan atau ketidaksesuaian." (Bagian 7 butir 5) | 1L6fR1mUiCePwKjyrpSPOrCz-6FpJbDpg |

### USULAN
Jumlah USULAN berlabel di dokumen: 3 (sama dengan hitungan lint "3 butir (USULAN)"). Baris rekaman berlabel berlaku untuk seluruh barisnya (nama, lokasi, pemilik, retensi).

| # | Butir | Letak di dokumen | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Pengembalian aset saat pemberhentian atau mutasi paling lambat hari terakhir kerja | Bagian 8 (SLA) | Menutup cacat "tidak ada batas waktu pengembalian aset"; disamakan dengan pencabutan akses di SNX-ISMS-SOP-02. Angka bukan dari sumber tim | Fani dan Aziz (HR) |
| U2 | Rekaman "Catatan rekonsiliasi SNX-ISMS-REG-01": Google Drive, pemilik Head of Operation, 3 tahun | Bagian 11 (rekaman) | Sumber memberi frekuensi dan target rekonsiliasi tetapi tidak memberi rekamannya; 3 tahun disamakan dengan SNX-OPS-FRM-04 | Fani |
| U3 | Rekaman "Catatan pemeriksaan drift": Google Drive, pemilik Lead SOC, 3 tahun | Bagian 11 (rekaman) | Sumber memberi frekuensi pemeriksaan drift tetapi tidak memberi rekamannya; 3 tahun disamakan dengan SNX-OPS-FRM-04 | Fani |

### Open items
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
| 10 | Baseline hardening: belum jelas runbook per jenis sistem sudah ada. Audit REG-01 mencatat acuan baseline "Belum ada" pada tiga baris contoh yang CI
- Tabel Exception memuat frasa 'tidak menjalankan wipe' yang tidak ada di sumber (instruksi tambahan penyusun); Fani konfirmasi atau hapus.

## SNX-ISMS-SOP-05 Vulnerability & Patch Management
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-SOP-05 Vulnerability & Patch Management (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-SOP-05_SOP_Vulnerability_Patch_Management.docx (160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC, modifiedTime 2026-10-13T06:09:02Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Prioritas Darurat diukur dari eksploitasi aktif dan keterjangkauan dari internet, bukan dari skor CVSS; tenggatnya 72 jam dengan mitigasi dalam 24 jam, dan tenggat semua prioritas berlabel USULAN oleh tim | "Darurat \| Dieksploitasi aktif di dunia nyata dan dapat dijangkau dari internet, atau RCE tanpa autentikasi \| 72 jam; mitigasi sementara (blok WAF, matikan fitur) dalam 24 jam" dan "Tenggat di atas adalah USULAN dan disahkan bersama SNX-ISMS-REG-03." (Bagian 6) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |
| 2 | Pengecualian prioritas Darurat dan Kritis butuh persetujuan Head of Operation dan dicatat sebagai risiko yang diterima | "Pengecualian untuk prioritas Darurat dan Kritis butuh persetujuan Head of Operation dan dicatat di SNX-ISMS-REG-03 sebagai risiko yang diterima." (Bagian 7.4 butir 2) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |
| 3 | Vulnerability yang dieksploitasi aktif diperlakukan sebagai potensi insiden, dengan sweep IOC sebelum dan sesudah patch | "Vulnerability yang dieksploitasi aktif pada aset kita diperlakukan sebagai potensi insiden: lakukan sweep IOC sesuai SNX-ISMS-SOP-01 sebelum dan sesudah patch, karena patch tidak menghapus kompromi yang sudah terjadi." (Bagian 7.2 butir 5) | 160t8vg9Eb_ItxjLuWxLG17OIAKpxSsKC |

### USULAN
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

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Tenggat Bagian 6 berlabel USULAN dan "disahkan bersama SNX-ISMS-REG-03", tetapi REG-03 tidak memuat tenggat patch (catatan audit: hanya RTP-003 yang menyebut telaah advisory mingguan). Perlu diputuskan tempat pengesahan tenggat dan apakah angka dijadikan final | Fani |
| 2 | Titik awal hitung tenggat dan satuan hari (kalender atau kerja) tidak ada di sumber; definisi Tenggat memakai usulan penyusun (USULAN 3). Di sumber, tenggat tertulis untuk "perbaikan atau mitigasi", tetapi indikator mengukur "ditutup dalam tenggat"; belum jelas apakah verifikasi masuk hitungan tenggat | Fani |
| 3 | Indikator kinerja: Sedang dan Rendah tanpa target; tidak ada periode ukur, sumber data, atau baseline untuk empat indikator; "Endpoint" di indikator didefinisikan server dan laptop kerja, sehingga fleet hosting pelanggan tidak terhitung dalam 100%, padahal 7.5 mengaturnya terpisah | Fani |
| 4 | Mitigasi 24 jam untuk Darurat: sumber hanya mengatur mitigasi bila patch belum tersedia atau tidak bisa dipasang (7.2 butir 4), sedangkan tabel Bagian 6 memberi mitigasi 24 jam untuk Darurat tanpa syarat itu. Belum jelas apakah mitigasi wajib juga saat patch tersedia dan bisa dipasang dalam 72 jam. Intro 6.4 dibiarkan netral | Fani |
| 5 | Pemetaan antarskala belum ada: prioritas patch, severity tiket P1 sampai P4, dan level risiko REG-02. PRO-OPS-001 SOC-04 menulis "CVE kritis yang dapat dieksploitasi dari luar dan menyentuh aset SINUX = tiket P2 minimal"; kalimat itu tidak dibawa karena bahan saja dan berstatus draf. Perlu diputuskan severity apa yang dipakai tiket temuan di Zammad dan FRM-08 | Fani |
| 6 | Kriteria Darurat tanpa CVSS dan tumpang tindih dengan Kritis (CVSS 9.0 atau lebih tanpa eksploitasi masuk Kritis); aturan prio

## SNX-ISMS-PLN-01 Business Continuity & IT Recovery Plan
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 1; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-PLN-01 Business Continuity & IT Recovery Plan (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-PLN-01_Business_Continuity_IT_Recovery_Plan.docx (1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX, modifiedTime 2026-10-13T06:09:00Z); POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv, modifiedTime 2026-10-13T09:06:27.051Z); PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (1U8CAdibwBk9x_-Aic2lbev144d6WReTz, modifiedTime 2026-10-13T09:06:40.151Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kriteria dan pemutus aktivasi rencana | "Rencana diaktifkan bila insiden P1 diperkirakan melewati RTO layanan Tingkat 1, atau bila beberapa layanan kritis terganggu bersamaan." dan "Pemberi keputusan aktivasi: Head of Operation; bila tidak tersedia, COO; bila keduanya tidak tersedia, CEO." (Bagian 6 butir 1 dan 2) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |
| 2 | RTO dan RPO sistem internal berstatus usulan, RTO layanan pelanggan mengikuti kontrak | "RTO dan RPO sistem internal adalah USULAN dan disahkan Head of Operation; RTO layanan pelanggan mengikuti kontrak." (Bagian 4, di bawah tabel) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |
| 3 | Program uji: tabletop tahunan oleh Head of Operation, restore bulanan oleh Lead NOC | "Tabletop exercise | Satu skenario Bagian 5 per sesi | Tahunan | Head of Operation | Laporan uji (Lampiran A)" dan "Uji restore backup | Sampel data pelanggan berlayanan backup | Bulanan | Lead NOC | SNX-ISMS-FRM-01" (Bagian 10) | 1vwD5tORDQNQ7SNaQ6w4KitPKTcsw9ZVX |

### USULAN
Lint menghitung 18 label (USULAN), satu di antaranya definisi istilah (spec memuat satu label lagi di gambar diagram). Butir bermakna: 9.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | RTO dan RPO sistem internal (monitoring 4 jam dan 24 jam; ticketing 8 jam dan 24 jam; password manager 4 jam dan 24 jam; Jumphost 4 jam dan 1 minggu; WAF dan proxy 4 jam dan 1 minggu; knowledge base 24 jam dan 24 jam) | Bagian 4 | Label USULAN berasal dari sumber; angka tidak diubah | Fani |
| U2 | RTO 4 jam managed services server pelanggan berlaku bila kontrak tidak menetapkan RTO | Bagian 4, bagian 9 | Sumber memberi "4 jam" pada layanan pelanggan sambil menyatakan RTO pelanggan mengikuti kontrak; syarat "bila kontrak tidak menetapkan" adalah tafsir | Fani |
| U3 | Penilaian ulang kriteria aktivasi bila perkiraan durasi atau layanan terdampak berubah | Butir 6.1 langkah 4, diagram | Menutup cacat "cabang tidak tanpa garis kembali"; bukan dari sumber | Fani |
| U4 | Pelaku langkah kesiapan sumber daya (Head of Operation memastikan runbook, cadangan, celah risiko, akses break-glass, laptop on-call; Lead SOC menyimpan salinan kontak) | Butir 6.4 langkah 1 sampai 4, 7, 8; baris peran Head of Operation | Sumber pasif tanpa pelaku | Fani |
| U5 | Salinan offline encryption key backup di luar password manager, disimpan Lead NOC | Bagian 4, butir 6.4 langkah 5, baris peran Lead NOC | Aturan lintas dokumen; label USULAN diwarisi dari SNX-ISMS-SOP-03 | Fani |
| U6 | Laporan uji disimpan di Folder Drive Operation, pemilik Head of Operation, retensi 3 tahun | Bagian 11 | Sumber hanya menulis "Lampiran A dokumen ini"; lokasi, pemilik, dan retensi tanpa sumber | Fani |
| U7 | Parent ticket aktivasi: pemilik Head of Operation, retensi 3 tahun | Bagian 11 | Sumb

### Open items
| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis COO (Amirull Yusuf Zulkarnain); defaults memakai Samuel Kristanto Utomo / President Director. Defaults dipakai | owner, Samuel |
| 2 | Head of Operation, Lead NOC, Lead SOC, Service Delivery Manager adalah jabatan USULAN di POL-OPS-001 dan HR-ORG-01 (K-10), belum ada pemegang bernama; hubungan Head of Operation dengan VP Tech Operation and Services belum ditetapkan (K-09). Sampai ada pemegang, keputusan aktivasi tidak punya orang | owner, Fani |
| 3 | Acronis (platform backup), konfigurasi network device, SIEM, dan dokumen di Drive tidak punya baris di daftar layanan kritis. SNX-ISMS-SOP-03 memuat RTO 4 jam (USULAN) untuk konfigurasi network device. Perlu keputusan apakah baris ditambah dan Tingkatnya | Fani |
| 4 | Sumber menulis "Runbook pemulihan per sistem kritis tersedia"; POL-OPS-001 bagian 13 mencatat runbook Nusagrid VM end-to-end dan alur backup dan restore Acronis belum ada. Dokumen menulis kewajiban, bukan keadaan | Fani |
| 5 | Ketersediaan kapasitas alternatif untuk memindahkan VM kritis dan konfigurasi cadangan WAF, DNS, CDN tidak ditunjukkan sumber; belum ada daftar atau pemilik. Tanpa itu butir redundansi (Annex A 8.14) belum terbukti | Fani |
| 6 | Parent ticket dan layanan ticketing berada di Tingkat 2 (RTO 8 jam), padahal dibutuhkan sejak aktivasi. Tempat mencatat keputusan bila Zammad dan Service Hub mati tidak ditentukan sumber; kontrol pengganti tidak dibuat | Fani |
| 7 | Status password manager (vault) belum terkonfirmasi: REG-01 menulis Aktif, REG-02 dan POL-OPS-001 bagian 13 menulis belum live. Break-glass dan daftar kontak tersimpan di password manager, yang sendiri masuk skenario kehilangan; salinan akses break-glass di luar password manager tidak ada di sumber (han
- Checklist baris 91 menautkan berkas ISMS-FRM-02 (1ILWYIkw...), bukan PLN-01; dipakai sumber worklist 1vwD5tOR... (SNX-ISMS-PLN-01_Business_Continuity_IT_Recovery_Plan.docx).
