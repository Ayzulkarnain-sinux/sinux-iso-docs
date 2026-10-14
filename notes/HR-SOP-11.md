# Catatan penyusun HR-SOP-11: Demotion

Status: DRAFTED (spec + notes ada). Spec: specs/HR-SOP-11.json. Mode sop, aksi T2, wave W4, nomor SNX-HR-SOP-11 (nomor SNX lama dipertahankan), department "Human Resources", classification "INTERNAL" (worklist), audit_class kosong. Approval persis dari config/defaults.json: prepared "Sita Nadia Salsabila Widodo / HRGA Officer", reviewed "Aziz Priyo Widakdo / HR Manager", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Catatan worklist kosong.

Process owner "HR Manager" (jabatan tanpa nama). Sumber punya baris "Process Owner | HR Lead – Aziz Priyo Widakdo". Nama dibuang sesuai aturan, dan jabatan "HR Lead" diganti "HR Manager" karena config/defaults.json data_conflicts (Jabatan Aziz Priyo Widakdo, pakai "HR Manager", konfirmasi owner atau Aziz) mengalahkan sumber, dan SNX-HR-ORG-01 (DONE) memakai HR Manager (JA-14).

Hasil uji terakhir (bukti mentah: /tmp/pen-HR-SOP-11/lint.out.txt dan /tmp/pen-HR-SOP-11/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-SOP-11.json /tmp/pen-HR-SOP-11/HR-SOP-11.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-SOP-11/HR-SOP-11.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "51 butir (USULAN) menunggu ACC". Warn PIC SLA nol (semua PIC langkah dan SLA ada di tabel peran).
- Validator OOXML skill docx (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!". soffice ke PDF: 17 halaman. Uji halaman putaran 1 (kata per halaman via pdftotext, halaman 1 sampai 17): 20, 75, 56, 81, 304, 263, 418, 225, 205, 212, 178, 19, 235, 197, 155, 242, 108. Tidak ada halaman kosong. Halaman 1 adalah sampul dan halaman 12 adalah diagram dengan judul bagian dan keterangan gambar (19 kata). Sebelum putaran 1, halaman 15 hanya header dan footer (4 kata) karena bagian 10 berakhir tepat di dasar halaman 14; tiga baris pengecualian baru menggeser bagian 9 dan 10 sehingga bagian 10 berakhir di tengah halaman 15 dan bagian 11 mulai di halaman 16.
- Diagram /tmp/pen-HR-SOP-11/HR-SOP-11_flow.png dilihat: 19 simpul, rankdir TB, satu cabang putus-putus. Putaran pertama 3107 px tinggi dengan tulisan efektif sekitar 4,3 pt di halaman, terendah di antara dokumen pilot. Saya ringkas jadi 2612 px (sekitar 5,2 pt): label diamond satu baris, label simpul dua baris, dan dua langkah terakhir dibuat sejajar. Varian dengan lajur per peran saya coba dan saya buang karena kotak lajur bertumpuk dan garis saling silang.
- Pemeriksaan tambahan atas spec (skrip python3 -I di sesi, bukan di repo): nol em-dash dan en-dash di spec; 22 langkah, terpanjang 15 kata; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5 (delapan peran: HR Manager, HRGA Officer, Direktur Utama, Direktur (JA-02), Organ perusahaan, Atasan Langsung, Karyawan terkait, Legal & Compliance (JA-08)); semua kode SNX yang dirujuk di badan (SNX-HR-JA-01, SNX-HR-ORG-01, SNX-HR-SOP-10, SNX-HR-SOP-12, SNX-HR-SOP-13, SNX-ISMS-SOP-02, SNX-ISMS-PRO-01) ada di tabel Dokumen terkait; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, hulu ke hilir), nol "komersil", nol "diagnosa", nol "Lead", nol "tim", nol frasa meta ("dokumen sumber", "sumber tim", "penyusun", "draf ini"), nol "belum ada" atau "belum berdokumen".
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas config, control, tools, template, reference, ledger.json, out, qa tidak diubah. Berkas yang ditulis hanya specs/HR-SOP-11.json dan notes/HR-SOP-11.md; hasil render hanya di /tmp/pen-HR-SOP-11/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini, sama dengan prompt; fileSize 51426 sama dengan "bytes" di salinan audit) | read_file_content, teks penuh 15 jabatan dan bagian 1 sampai 4. Struktur docx tidak saya dekode: teks cukup, dan penomoran butir uraian diambil dari urutan teks serta dicocokkan ke specs/HR-JA-01.json |
| Kriteria penerimaan | config/checklist.json baris 18 | modifiedTime checklist 2026-10-14T17:47:13.611Z | Description: "Prosedur penurunan jabatan atau tingkat posisi akibat penurunan kinerja atau pelanggaran aturan perusahaan." Kolom iso_9001 dan iso_27001 kosong, jadi klausul diusulkan |
| Catatan cacat | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian "hr/HR-JA-001.md" (bagian 5, butir 1 sampai 15) dan sintesis baris 78 | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran dan nomor dokumen | specs/HR-ORG-01.json (DONE), specs/HR-JA-01.json, specs/ISMS-SOP-02.json, config/worklist.json | repo kerja | Nama peran bagian 5 dari daftar jabatan HR-ORG-01 (JA-01 Direktur Utama, JA-08 Legal & Compliance, JA-12 HRGA Officer, JA-14 HR Manager). Nomor SNX-HR-SOP-10, 12, 13 dari worklist. Perlakuan perubahan akses saat mutasi dari ISMS-SOP-02 |

Sumber hanya menyebut demotion secara tidak langsung: tidak ada prosedur, kriteria, atau ambang penurunan jabatan. Karena itu seluruh alur bagian 6 adalah rancangan T2 yang dibangun dari peran dan wewenang di sumber, dan intro butir 6.1 menyatakan langkah 6.1 sampai 6.5 berstatus (USULAN) sampai SOP disahkan.

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat bernada perintah di sumber adalah aturan isi dokumen itu sendiri (mis. "Atasan langsung serta bawahan langsung yang belum ditetapkan secara resmi harus dikonfirmasi oleh manajemen sebelum pengesahan") dan tidak dijalankan; relevansinya dicatat di open items O8.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | HR Manager (JA-14) memegang pemeriksaan dugaan pelanggaran dan penegakan disiplin; dasar butir 4.3 dan langkah 6.1 | JA-14, Uraian Jabatan butir 7: "Menangani hubungan karyawan, pemeriksaan dugaan pelanggaran, penegakan disiplin, penyelesaian keluhan, dan mitigasi risiko ketenagakerjaan secara objektif." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | HR Manager hanya merekomendasikan tindakan disiplin dan salary action kepada approver; pemutusan hubungan kerja dan perubahan kontrak mengikuti persetujuan tertulis. Dasar pemisahan peran (butir 4.4, 4.6) | JA-14, Wewenang butir 4: "Merekomendasikan hiring, salary action, disciplinary action dan policy kepada approver". Batasan umum: "keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 3 | Grading tidak ada di Job Analysis, sehingga "tingkat posisi" belum punya jenjang resmi; penurunan tingkat posisi ditaruh di scope dengan label (USULAN) | Tabel kontrol dokumen, Cakupan: "15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## Fakta pendukung

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi di SOP |
|---|---|---|---|
| 1 | Rencana perbaikan kinerja ada di proses manajemen kinerja yang dikendalikan HR Manager | JA-14, Uraian butir 4: "Mengendalikan proses manajemen kinerja, termasuk penyusunan KPI, penilaian berkala, kalibrasi hasil, rencana perbaikan kinerja, dan pengarsipan dokumen." | Definisi, 4.2 |
| 2 | Target kinerja ada di KPI Matrix, bukan di Job Analysis | Bagian 2: "KPI dalam dokumen merupakan usulan indikator, target numerik, bobot dan sumber data ditetapkan pada KPI Matrix terpisah." | 4.2 |
| 3 | Penyesuaian kompensasi ada di tangan HR Manager sebatas usulan | JA-14, Uraian butir 6: "Meninjau data penggajian, tunjangan, kepesertaan BPJS, usulan penyesuaian kompensasi, dan administrasi insentif sesuai kewenangan serta persetujuan yang berlaku." | Scope, bagian 9 |
| 4 | Fairness dan objektivitas dituntut dari HR Manager | JA-14, Kompetensi Perilaku butir 2: "Judgment dan fairness". Uraian butir 7: "secara objektif" | 4.3, 4.5 |
| 5 | HRGA Officer memelihara personal file dan meneruskan keputusan HR ke HR Manager | JA-12, Uraian butir 1: "Memelihara data karyawan, kontrak, personal file dan administrasi orientasi karyawan baru/proses keluar karyawan." Wewenang butir 1 sampai 3: "Meminta kelengkapan data/dokumen", "Memproses administrasi dalam SOP", "Mengeskalasi keputusan HR dan persetujuan ke HR Lead" | Definisi Personal file, bagian 5 |
| 6 | Akses informasi personal dikendalikan HR Manager | JA-14, Wewenang butir 6: "Mengendalikan akses informasi personal sesuai kebijakan" | 4.10 |
| 7 | Legal & Compliance (JA-08) meninjau kontrak tenaga kerja dan memberi legal clearance | JA-08, Uraian butir 1: "Melakukan legal peninjauan kontrak pelanggan, vendor, tenaga kerja dan kemitraan." Wewenang butir 1 dan 2: "Memberikan legal clearance/rekomendasi", "Meminta revisi klausul berisiko" | Bagian 5, bagian 9 |
| 8 | Wewenang tanda tangan kontrak dan keuangan tidak melekat otomatis pada jabatan | Bagian 2: "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." | 4.7 |
| 9 | Atasan Direktur Utama berada di luar jabatan di daftar | JA-01, Atasan Langsung: "Organ perusahaan sesuai ketentuan dan anggaran dasar (verifikasi)" | Scope |
| 10 | Atasan HR Manager belum satu | JA-14, Atasan Langsung: "Direktur atau Management sesuai struktur yang disahkan" | Bagian 9 |
| 11 | Status dokumen sumber masih draf, bukan dokumen terkendali | Tabel kontrol: "DRAF – Menunggu verifikasi jabatan dan persetujuan Management"; Bagian 4: "semua hubungan pelaporan dan batas otoritas yang belum terkonfirmasi harus diselesaikan sebelum dokumen diberi status Controlled / Effective." | Seluruh dokumen berlabel Draft, bagian 9 |
| 12 | Perubahan akses saat mutasi (bukan dari sumber ini; dari specs/ISMS-SOP-02.json, prosedur "Perubahan Akses saat Mutasi") | "Beri tahu mutasi paling lambat pada hari efektif." (HR atau atasan langsung); "Ajukan perubahan akses karena mutasi." (atasan langsung); "Cabut akses lama yang tidak relevan paling lambat 5 hari kerja sesudah mutasi." (administrator sistem). Definisi: "Mutasi: Perpindahan peran seseorang." | 4.9, langkah 6.5, SLA baris terakhir |
| 13 | Kriteria baris | "Prosedur penurunan jabatan atau tingkat posisi akibat penurunan kinerja atau pelanggaran aturan perusahaan." (config/checklist.json baris 18) | Pemetaan di bawah |

## 2. Pemetaan kriteria (Description baris 18)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| prosedur | Bagian 6 (6.1 sampai 6.5, 22 langkah), bagian 7 (diagram), bagian 8 (batas waktu), bagian 9 (pengecualian) | Rancangan T2; dasar peran di fakta kunci 1 dan 2 |
| penurunan jabatan | Definisi Penurunan jabatan; scope; langkah 6.2 sampai 6.5 | Daftar jabatan SNX-HR-ORG-01 |
| tingkat posisi | Definisi Posisi dan Tingkat posisi; scope kalimat ketiga; Penurunan jabatan mencakup "tingkat posisi yang lebih rendah". Langkah memakai istilah Posisi tujuan agar satu jalur melayani jabatan maupun tingkat posisi | Fakta kunci 3: grading tidak dicantumkan, jadi bagian tingkat posisi berlabel (USULAN) |
| akibat penurunan kinerja | Butir 4.1, 4.2; definisi Penurunan kinerja, Rencana perbaikan kinerja, Penilaian kinerja; jalur kinerja di diagram | Fakta pendukung 1 dan 2 |
| atau pelanggaran aturan perusahaan | Butir 4.1, 4.3, 4.5; langkah 6.1; bagian 9 baris pertama | Fakta kunci 1 |

Klausul ISO (checklist tidak memberi acuan; semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur dan rekaman |
|---|---|---|
| ISO 9001:2015 5.3 (Peran, tanggung jawab, dan wewenang organisasi) | 4.4, 4.6, 4.7, 4.8 | Tabel peran bagian 5 |
| ISO 9001:2015 7.2 (Kompetensi) | 4.1, 4.2 | Langkah 6.3 dan 6.4 (bukti dasar dan kesimpulan) |
| ISO 9001:2015 7.5.3 (Pengendalian informasi terdokumentasi) | 4.10 | Tabel rekaman bagian 11 |
| ISO/IEC 27001:2022 Annex A 5.2 (Peran dan tanggung jawab keamanan informasi) | 4.7 | Tabel peran bagian 5 |
| ISO/IEC 27001:2022 Annex A 5.18 (Hak akses) | 4.9 | Langkah 6.5 butir 5 dan 6 |
| ISO/IEC 27001:2022 Annex A 5.33 (Perlindungan rekaman) | 4.10 | Tabel rekaman bagian 11 |
| ISO/IEC 27001:2022 Annex A 5.34 (Privasi dan perlindungan PII) | 4.10 | Klasifikasi RESTRICTED (Internal) |
| ISO/IEC 27001:2022 Annex A 6.4 (Proses disipliner) | 4.1, 4.3, 4.5 | Langkah 6.1 dan 6.3 |
| ISO/IEC 27001:2022 Annex A 6.5 (Tanggung jawab setelah pemutusan atau perubahan hubungan kerja) | 4.9 | Langkah 6.5 |

Judul klausul ditulis dari pengetahuan standar, bukan dari sumber atau checklist. Semuanya menunggu konfirmasi konsultan.

## USULAN

Dokumen memuat 51 penanda "(USULAN)", mewakili 20 butir keputusan di bawah. Pemutus yang disarankan dipilih dari owner, Samuel, Aziz, FAT, Legal, atau Fani.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Seluruh alur 6.1 sampai 6.5 dan diagramnya. Sumber tidak memuat prosedur penurunan jabatan | Bagian 6, 7 | Aziz |
| U2 | Pembagian peran: Atasan Langsung mengusulkan, HR Manager memeriksa dan merekomendasikan, Direktur Utama menetapkan keputusan; wewenang HR Manager hanya merekomendasikan | 4.4, bagian 5 | Samuel |
| U3 | Direktur Utama menyetujui atau menolak dalam batas anggaran dasar dan delegasi tertulis | Bagian 5 | Samuel |
| U4 | Ambang hasil penilaian kinerja dan lama pelaksanaan rencana perbaikan kinerja; penetapan oleh Direktur Utama atas usulan HR Manager | 4.2, bagian 10 | Samuel (atas usulan Aziz) |
| U5 | Dasar selain penurunan kinerja dan pelanggaran aturan perusahaan tidak diproses lewat SOP ini | 4.1 | Aziz |
| U6 | Usulan atas dasar pelanggaran hanya diajukan bila pemeriksaan menyimpulkan terbukti | 4.3, langkah 6.1, bagian 9 | Aziz, dengan masukan Legal |
| U7 | Hak karyawan terkait menanggapi usulan sebelum HR Manager menyimpulkan, dan batas tanggapan 5 hari kerja | 4.5, langkah 6.3, SLA, bagian 9 | Aziz, dengan masukan Legal |
| U8 | Berlaku hanya sesudah keputusan tertulis Direktur Utama; tanggal berlaku tidak mendahului tanggal keputusan | 4.6 | Samuel |
| U9 | Wewenang posisi sekarang yang tidak ada di posisi tujuan berhenti pada tanggal berlaku | 4.7 | Samuel |
| U10 | Karyawan terkait mengonfirmasi tertulis bahwa ia memahami uraian posisi tujuan sebelum tanggal berlaku | 4.8, langkah 6.5, SLA | Aziz |
| U11 | Klasifikasi rekaman penurunan jabatan RESTRICTED (Internal) | 4.10 | owner (peran ISMS Coordinator belum ditetapkan, K-13 di SNX-HR-ORG-01) |
| U12 | Lokasi simpan rekaman (personal file di folder Google Drive Departemen HR) dan retensi selama karyawan bekerja di SINUX | Bagian 11 | Aziz, dengan masukan Legal untuk retensi |
| U13 | Batas waktu: 10 hari kerja pemeriksaan pelanggaran, 3 hari kerja pemeriksaan kelengkapan, 5 hari kerja tanggapan, 5 hari kerja rekomendasi, 5 hari kerja keputusan, 2 hari kerja pemberitahuan keputusan. Angka tanpa sumber; angka yang sama dengan SNX-HR-SOP-10 hanya untuk keseragaman, bukan karena sumber | Bagian 8 | Aziz (butir keputusan: Samuel) |
| U14 | Hari kerja tidak termasuk hari libur resmi | Definisi | Aziz |
| U15 | Penurunan tingkat posisi baru berjalan sesudah grading ditetapkan | Scope, definisi | owner |
| U16 | Dikecualikan dari scope: sanksi disiplin selain penurunan jabatan; penetapan besarnya gaji dan tunjangan; penurunan jabatan Direktur Utama (JA-01) | Scope | Aziz (sanksi dan gaji), Samuel (JA-01) |
| U17 | Penanganan pengecualian: tanpa tanggapan, posisi tujuan belum tercantum, Atasan Langsung belum pasti atau terlibat, karyawan terkait adalah HR Manager (Direktur Utama menunjuk pengganti), perubahan perjanjian kerja ke Legal & Compliance (JA-08), usulan penyesuaian kompensasi, konfirmasi uraian tertunda | Bagian 9 | Aziz, dengan Samuel untuk penunjukan pengganti dan Legal untuk perjanjian kerja |
| U18 | HR Manager memeriksa kepatuhan terhadap SOP dengan membandingkan rekaman, langkah, dan batas waktu | Bagian 10 | Aziz |
| U19 | Semua acuan klausul ISO 9001:2015 dan ISO/IEC 27001:2022 di bagian 11 (label "USULAN, perlu konfirmasi konsultan") | Bagian 11 | owner (konfirmasi konsultan) |
| U20 | Peran pengganti agar satu peran tidak mengusulkan sekaligus memutuskan atau memeriksa usulannya sendiri: Organ perusahaan memutuskan usulan penurunan Direktur (JA-02) sebagai pengganti Direktur Utama; Direktur (JA-02) menjalankan langkah HR Manager di butir 6.1 dan 6.4 bila HR Manager adalah Atasan Langsung karyawan terkait (HRGA Officer, JA-12); HR Manager menjalankan langkah HRGA Officer di butir 6.3 dan 6.5 bila HRGA Officer adalah Atasan Langsung (Office Helper, JA-15) atau karyawan terkait | Butir 4.4, bagian 5, bagian 9 | Samuel, owner |

## Asumsi

1. Penurunan jabatan diputus Direktur Utama, mengikuti pola SNX-HR-SOP-10 untuk kenaikan jabatan. Sumber hanya menyebut persetujuan tertulis menurut delegasi yang berlaku, tanpa menunjuk pemutus.
2. Hanya dua hasil keputusan (setujui atau tolak). Opsi "setujui dengan syarat" di SNX-HR-SOP-10 tidak dipakai karena syarat pada penurunan jabatan tidak punya padanan di sumber.
3. "Aturan perusahaan" dibaca sebagai ketentuan tertulis SINUX yang berlaku. Sumber tidak menyebut Peraturan Perusahaan, jadi dokumen tidak merujuknya (open item O1).
4. Peran bagian 5 memakai nama dari specs/HR-ORG-01.json. Peran "Karyawan terkait" bukan jabatan; ia dipakai untuk karyawan yang diperiksa atau diusulkan, supaya tidak ada dua istilah untuk orang yang sama di langkah 6.1 dan 6.2. SNX-HR-SOP-10 memakai "Karyawan yang diusulkan" untuk kenaikan jabatan. Peran "Direktur (JA-02)" dan "Organ perusahaan" ditambahkan di bagian 5 karena bagian 9 memakainya sebagai peran pengganti; nama keduanya dari daftar jabatan HR-ORG-01 (JA-02) dan dari catatan K-05 di sana. Pemetaan peran sumber ke HR-ORG-01: "HR Lead" di sumber dipetakan ke HR Manager (JA-14); atasan umum "Management" tidak dipakai, diganti Direktur Utama atau Atasan Langsung.
5. Perubahan hak akses mengikuti SNX-ISMS-SOP-02 apa adanya. Pencabutan akses lama (5 hari kerja) tidak diulang di badan SOP ini dan administrator sistem tidak dijadikan peran, supaya aturan akses tetap di satu dokumen.

## Penanganan cacat context/audit (bagian 5, HR-JA-001)

| Butir audit | Relevan | Penanganan |
|---|---|---|
| 1. Status DRAF, Revision "03 -", nomor "usulan" | Ya | SOP merujuk SNX-HR-JA-01 (nomor di worklist), bukan HR-JA-001. Seluruh dokumen berstatus Draft, dan butir yang bergantung pada Job Analysis diberi label (USULAN) |
| 2. Tanpa KPI per jabatan, tanpa bagan, tanpa grading | Ya | KPI diarahkan ke KPI Matrix (4.2, belum bernomor). Grading tidak ada: penurunan tingkat posisi berlabel (USULAN) di scope (U15, open item O5) |
| 3. Kalimat terpotong di bagian 1 | Tidak | SOP tidak mengutipnya (sudah disambung di SNX-HR-JA-01 butir 4.1) |
| 4. Frasa kompetensi janggal | Tidak | SOP tidak mengutip bagian Kompetensi. "pihak terkait influence" (JA-14 D.5) tidak dipakai |
| 5. Pelaporan Manager of Product Tech | Tidak | Di luar peran SOP |
| 6. Atasan JA-06 dan JA-07 ditulis nama departemen | Tidak | Di luar peran SOP |
| 7. Atasan JA-08, JA-10, JA-11, JA-14 umum ("Management / Direktur") | Sebagian | Atasan HR Manager (JA-14) belum satu: bagian 9 menetapkan Direktur Utama menunjuk jabatan pengusul bila Atasan Langsung berlabel menunggu konfirmasi, dan menunjuk pengganti bila karyawan terkait memegang peran HR Manager (U17, open item O7) |
| 8. Nama unit tidak seragam | Sebagian | Nama departemen di identitas dokumen "Human Resources" (defaults.json). Badan dokumen tidak menyebut unit |
| 9. Dua jabatan "Legal & Compliance" | Ya | Peran ditulis "Legal & Compliance (JA-08)" supaya tidak tertukar dengan JA-09. Pemetaan JA-08 sebagai Line Manager Legal tidak dipakai |
| 10. Finance Lead dan Finance Staff tanpa jabatan | Tidak | Tidak ada peran Finance di SOP |
| 11. Ejaan nama dan sebutan Direktur Utama | Ya | "Samuel Kristanto Utomo / President Director" hanya di blok Approved By. Badan dokumen: "Direktur Utama" (data_conflicts). Sebutan CEO tidak dipakai |
| 12. Teks B dan F identik, tanpa batas nominal wewenang | Sebagian | Kutipan "Batasan umum" dipakai sekali sebagai dasar (4.6). SOP tidak menaruh batas nominal apa pun; hak tanda tangan dan otorisasi keuangan dirujuk ke Authority Matrix (4.7) |
| 13. Masa pengalaman minimum belum ada | Tidak | Penurunan jabatan tidak menilai kualifikasi posisi tujuan; uraian posisi tujuan cukup diserahkan (langkah 6.5) |
| 14. Selisih jumlah tabel | Tidak | UNMEASURED di audit, tidak memengaruhi isi |
| 15. Tidak ada rujukan ISO/IEC 27001, padanan 7.3 dan 7.5 bukan teks sumber | Ya | Semua acuan klausul berlabel "(USULAN, perlu konfirmasi konsultan)"; judul klausul bukan dari sumber (lihat bawah tabel klausul) |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| O1 | Sumber tidak menyebut ketentuan tertulis mana yang, bila dilanggar, dapat berujung penurunan jabatan (mis. Peraturan Perusahaan). Definisi "Pelanggaran aturan perusahaan" masih umum | Legal, Aziz |
| O2 | Apakah penurunan jabatan memerlukan persetujuan karyawan atau perubahan perjanjian kerja menurut hukum ketenagakerjaan dan perjanjian kerja SINUX. Dokumen hanya mengirim perubahan perjanjian kerja ke tinjauan Legal & Compliance (JA-08) | Legal |
| O3 | Ambang hasil penilaian kinerja dan lama rencana perbaikan kinerja (U4) belum ditetapkan, sehingga jalur penurunan kinerja belum bisa dijalankan sampai Direktur Utama menetapkannya; SOP Performance Appraisal masih dalam peninjauan. Setelah ditetapkan, SOP ini direvisi | Samuel, Aziz |
| O4 | SOP Performance Appraisal dan SOP Employee Offboarding dalam peninjauan dan belum punya kode SNX di worklist. Setelah bernomor, ganti nama dengan kode di bagian 2, 3, dan 11. SOP Payroll Process (juga dalam peninjauan) belum dirujuk karena gaji dikecualikan | Aziz |
| O5 | Grading belum ada di SNX-HR-JA-01 dan SNX-HR-ORG-01, sehingga penurunan tingkat posisi di dalam jabatan yang sama belum bisa dijalankan | owner, Aziz |
| O6 | Sanksi disiplin selain penurunan jabatan (teguran, surat peringatan) tidak punya SOP di daftar HR. Apakah perlu dokumen sendiri | owner, Aziz |
| O7 | Atasan HR Manager belum satu (K-04 di SNX-HR-ORG-01). Penunjukan pemeriksa dan pengusul pengganti bila HR Manager atau HRGA Officer menjadi karyawan terkait ditulis berlabel (USULAN) dan perlu diputus | Samuel, owner |
| O8 | Authority Matrix dan KPI Matrix belum bernomor, dirujuk dengan "Belum bernomor". Status konfirmasi data_conflicts yang bukan "selesai" dan berlaku di dokumen ini: jabatan Aziz (HR Manager lawan HR Lead, owner atau Aziz), ejaan dan sebutan Samuel (owner atau Samuel). Catat di Laporan_Run | owner |
| O9 | Penetapan besarnya gaji dan tunjangan sesudah penurunan jabatan di luar SOP ini. Dokumen mana yang mengaturnya (SOP Payroll Process dalam peninjauan) dan siapa penetapnya belum jelas | Aziz, FAT |
| O10 | Lokasi simpan dan retensi rekaman (U12) dan klasifikasi RESTRICTED (Internal) (U11) belum dikonfirmasi pemilik dokumen terkait | Aziz, owner |
| O11 | Pemisahan peran (butir 4.4): bila karyawan terkait Direktur (JA-02), Direktur Utama mengusulkan sekaligus memutuskan, sehingga bagian 9 menyerahkan keputusan ke Organ perusahaan (USULAN). Organ perusahaan menurut anggaran dasar belum disebut namanya di sumber (JA-01: "Organ perusahaan sesuai ketentuan dan anggaran dasar (verifikasi)"; K-05 di SNX-HR-ORG-01), dan tata cara keputusannya belum ada | Samuel, owner |
| O12 | Pemisahan peran: bila karyawan terkait HRGA Officer (JA-12), HR Manager adalah Atasan Langsungnya dan Direktur (JA-02) menggantikan langkah HR Manager. Bila karyawan terkait Office Helper (JA-15), HR Manager menggantikan langkah HRGA Officer. Penunjukan Direktur dan HR Manager sebagai pengganti perlu diputus; sah tidaknya Direktur sebagai pengganti bergantung pada garis lapor HR Manager ke Direktur yang masih menunggu konfirmasi (K-04) | Samuel, owner |
| O13 | Pemisahan peran: bila karyawan terkait HR Manager (JA-14), bagian 9 hanya menyebut Direktur Utama menunjuk karyawan lain, tanpa peran pengganti tetap. Atasan Langsungnya (K-04) belum satu, dan Direktur tidak bisa sekaligus mengusulkan dan menggantikan HR Manager. Peran pengganti tetap belum ada | Samuel, owner |

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI (diperiksa pada draf pertama, lalu diperbaiki):
- "karyawan sempat menanggapi usulan" terdengar seperti terjemahan lepas dan salah register. Diganti "karyawan diberi kesempatan menanggapi usulan".
- Definisi "Dasar penurunan" menyalin dua alasan yang sama dengan butir 4.1, sehingga satu fakta tertulis dua kali. Definisi diganti arti saja ("Alasan yang ditulis di usulan sebagai sebab penurunan jabatan"); dua alasannya tinggal di 4.1.
- Tanda kurung bersarang "(butir 6.4, (USULAN))" tampak mekanis. Diubah jadi "(butir 6.4) (USULAN)" di empat tempat.
- Langkah 6.1 butir kedua memuat dua tindakan ("periksa bukti dan minta keterangan"). Dijadikan satu tindakan: periksa dugaan pelanggaran secara objektif, termasuk meminta keterangan karyawan terkait.
- Putaran perbaikan 1: kalimat pasif dengan pelaku yang diketahui saya ubah menjadi aktif dan menyebut pelaku (Purpose, 4.1 sampai 4.3, 4.6, 4.9, bagian 8 kolom batas waktu, bagian 9, dan simpul akhir diagram). Dua istilah ganda saya satukan: "uraian posisi tujuan" (kini punya definisi di bagian 3, dipakai di Purpose, Scope, 4.8, bagian 5, 6.5) menggantikan "uraian tanggung jawab posisi tujuan", dan "data kepegawaian" menggantikan "data jabatan". Kalimat 4.4 tentang HRGA Officer saya selaraskan dengan langkah yang ada (memeriksa kelengkapan usulan dan mengarsipkan rekaman). Kalimat "belum ditetapkan" pada ambang dan grading saya biarkan karena pelaku penetapan disebut di kalimat berikutnya.
- Sisa yang saya biarkan dan akui: sepuluh butir kebijakan memakai pola sama ("Judul (klausul): ..."), pola itu dari template SNX-HR-SOP-10 dan memudahkan auditor memetakan klausul; tiga belas baris pengecualian berirama sama "X melakukan Y (USULAN)" karena memang satu pelaku satu tindakan; 51 penanda USULAN terasa berulang tetapi tiap penanda menandai isi yang belum diputus. Kelompok tiga tidak dipaksakan: daftar tiga di dokumen (mis. rekaman di tabel bagian 11) adalah daftar nyata. Nol em-dash, nol en-dash, nol penekanan tebal atau kapital atau tanda kutip.

Adakah fakta, angka, nama, atau tanggal tanpa sumber:
- Angka: 10, 3, 5, 5, 5, dan 2 hari kerja di bagian 8 tanpa sumber, semuanya berlabel (USULAN) (U13). Angka "5 hari kerja" pencabutan akses ada di ISMS-SOP-02, tidak diulang di badan SOP. Nol angka lain, nol tanggal.
- Nama: hanya di blok approval (dari config/defaults.json). Badan dokumen memakai peran. Nol nama orang di badan.
- Sistem: Google Drive hanya muncul di tabel rekaman, berlabel (USULAN). Zammad, GLPI, dan vault tidak disebut karena tidak relevan.
- Judul klausul ISO dan keseluruhan acuan: bukan dari sumber, berlabel "(USULAN, perlu konfirmasi konsultan)".
- Rancangan langkah, pemutus (Direktur Utama), hak menanggapi, dan penanganan pengecualian: tidak ada di sumber. Seluruhnya berlabel (USULAN) per butir atau lewat intro butir 6.1 (daftar di bagian USULAN).
- Definisi "Pelanggaran aturan perusahaan", "Posisi", dan "Tingkat posisi" adalah rumusan polos tanpa angka atau nama; rumusannya milik penyusun dan masuk open item O1 dan O5.
