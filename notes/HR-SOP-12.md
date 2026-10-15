# Catatan penyusun HR-SOP-12: Rotation

Status: DRAFTED (spec + notes ada). Spec: specs/HR-SOP-12.json. Mode sop, aksi T2, wave W4, nomor SNX-HR-SOP-12 (nomor SNX lama dipertahankan), department "Human Resources", classification "INTERNAL" (worklist), audit_class None. Approval persis dari config/defaults.json: prepared "Sita Nadia Salsabila Widodo / HRGA Officer", reviewed "Aziz Priyo Widakdo / HR Manager", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "HR Manager" (jabatan tanpa nama): sumber menulis baris "Process Owner" dengan jabatan "HR Lead" dan nama pemegangnya; "HR Lead" dipetakan ke "HR Manager" menurut config/defaults.json data_conflicts (jabatan Aziz) dan specs/HR-ORG-01.json (JA-14).

Hasil uji terakhir (bukti mentah: /tmp/pen-HR-SOP-12/lint.out.txt dan /tmp/pen-HR-SOP-12/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-SOP-12.json /tmp/pen-HR-SOP-12/HR-SOP-12.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-SOP-12/HR-SOP-12.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "46 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Validator OOXML (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- soffice ke PDF: 17 halaman (halaman diagram: 13). Diagram /tmp/pen-HR-SOP-12/HR-SOP-12_flow.png dibuka: 14 simpul, rankdir TB, 12 tingkat vertikal, ukuran 1248 x 2315 piksel (pembanding: diagram HR-SOP-10 1059 x 1916), label Ya dan Tidak terbaca. Draf diagram pertama berukuran 1084 x 3716 dan teksnya terlalu kecil di halaman; simpul dilebur dan label diperpendek sampai ukuran di atas.
- Pemeriksaan tambahan atas spec (skrip python3 -I, di scratchpad sesi, bukan di repo): nol em-dash dan en-dash; 23 langkah, terpanjang 24 kata (dihitung ulang sesudah sweep); semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5 (enam peran) dan semua peran terpakai sebagai PIC; semua kode SNX di badan (SNX-HR-JA-01, SNX-HR-ORG-01, SNX-HR-FRM-01, SNX-HR-FRM-02, SNX-HR-SOP-10, SNX-HR-SOP-11, SNX-HR-SOP-13, SNX-ISMS-SOP-02, SNX-ISMS-PRO-01) ada di tabel Dokumen terkait; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, hulu ke hilir), nol "komersil", nol "diagnosa", nol "Lead", nol "tim", nol frasa meta proses ("sumber", "penyusun", "draf ini"), nol "belum ada".
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control, reference, ledger.json tidak diubah. Berkas yang ditulis hanya specs/HR-SOP-12.json dan notes/HR-SOP-12.md; hasil render hanya di /tmp/pen-HR-SOP-12/. Spec SNX-HR-SOP-10, SNX-HR-SOP-11, dan SNX-HR-SOP-13 dibaca (hanya baca) untuk mencocokkan batas dengan SOP ini.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata hari ini, sama dengan prompt; fileSize 51426 sama dengan "bytes" di salinan audit) | read_file_content (teks penuh, 15 jabatan, bagian 1 sampai 4). download_file_content tidak dipanggil karena teks sudah cukup; numbering tidak dipakai |
| Kriteria penerimaan | config/checklist.json baris 19 | tidak berlaku | Description: "Prosedur perpindahan tugas/fungsi karyawan dalam tingkatan jabatan yang sama untuk penyegaran atau pengembangan keterampilan." Kolom iso_9001 dan iso_27001 kosong |
| Catatan cacat | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian "hr/HR-JA-001.md" (baris 8 sampai 1250, bagian 5 butir 1 sampai 15) dan sintesis baris 78 | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Daftar Jabatan (kolom Unit dan Melapor ke), Matriks Peran, butir K-02, K-03, K-04, K-06 |
| Dokumen saudara | specs/HR-SOP-10.json, specs/HR-SOP-11.json, specs/HR-SOP-13.json, specs/ISMS-SOP-02.json | repo kerja | Batas scope Rotation lawan Promotion, Demotion, Mutation; definisi dan prosedur "Perubahan Akses saat Mutasi" |

Sumber ini tidak memuat satu pun bahasan rotasi: pencarian kata rotasi, rotation, penyegaran, tingkatan, mutasi, dan job rotation di teks sumber (salinan audit) menemukan nol hasil; "grading" hanya muncul sebagai "tidak dicantumkan". Sumber dipakai untuk peran, wewenang, kompetensi, dan batas persetujuan. Alur rotasi (butir 6.1 sampai 6.5) disusun dari kriteria Description dan pola SNX-HR-SOP-10; seluruhnya berlabel (USULAN) lewat kalimat pembuka butir 6.1.

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat bernada kewajiban ("Atasan langsung serta bawahan langsung yang belum ditetapkan secara resmi harus dikonfirmasi oleh manajemen sebelum pengesahan.") adalah aturan untuk Management dan dicatat di Open items 13.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Job Analysis dipakai untuk performance management, competency assessment, dan bukti penetapan peran; karena itu jabatan tujuan, kompetensi, dan wewenang rotasi dirujuk ke SNX-HR-JA-01, bukan ditulis ulang | Bagian 1: "Dokumen digunakan untuk rekrutmen, orientasi karyawan baru, performance management, competency assessment, dan bukti penetapan peran dalam sistem manajemen mutu." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Sumber tidak memuat grading, sehingga "tingkatan jabatan yang sama" dari kriteria baris tidak punya ukuran di sumber; SOP memakai ukuran (USULAN) berupa jumlah garis lapor | Tabel kontrol dokumen, baris Cakupan: "15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 3 | Pedoman klausul 7.2 di sumber: tetapkan kompetensi, nilai kompetensi aktual, tindak kesenjangan, simpan bukti. Ini dasar langkah "pengembangan keterampilan" (butir 4.3, 6.2, dan 6.5) | Bagian 2: "ISO 9001:2015 klausul 7.2: tetapkan kompetensi yang diperlukan, nilai kompetensi aktual, lakukan tindakan jika terdapat kesenjangan, simpan bukti pendukung." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Fakta pendukung dan kutipan verbatim

Semua kutipan dari fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 kecuali baris 11 sampai 15.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di SOP |
|---|---|---|---|
| 1 | Tanggung jawab harus dikomunikasikan dan dipahami | Bagian 2: "ISO 9001:2015 klausul 5.3: tanggung jawab dan kewenangan harus ditetapkan, dikomunikasikan dan dipahami." | 4.7, 6.4 langkah 1 dan 2 |
| 2 | Rotasi tidak otomatis memberi hak tanda tangan atau otorisasi keuangan | Bagian 2: "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." | 4.6 |
| 3 | Persetujuan tertulis untuk keputusan personalia | Tiap jabatan, Batasan umum: "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 4.5 |
| 4 | HR Manager merekomendasikan, approver memutuskan | JA-14 E.4: "Merekomendasikan hiring, salary action, disciplinary action dan policy kepada approver" | 4.5, tabel peran (HR Manager) |
| 5 | HRGA Officer meminta kelengkapan dan memproses administrasi; keputusan HR naik ke HR Manager | JA-12 E.1 sampai E.3: "Meminta kelengkapan data/dokumen", "Memproses administrasi dalam SOP", "Mengeskalasi keputusan HR dan persetujuan ke HR Lead" | Tabel peran (HRGA Officer) |
| 6 | HRGA Officer memelihara data karyawan dan personal file | JA-12 A.1: "Memelihara data karyawan, kontrak, personal file dan administrasi orientasi karyawan baru/proses keluar karyawan." | Definisi Personal file, 6.4 langkah 3 dan 6, 6.5 langkah 4 dan 7 |
| 7 | HR Manager memastikan kebutuhan kompetensi, mengevaluasi kesenjangan, menindaklanjuti pelatihan | JA-14 A.5: "Memastikan kebutuhan kompetensi tiap jabatan telah ditetapkan, kesenjangan kompetensi dievaluasi, serta rencana dan efektivitas pelatihan ditindaklanjuti." | 4.3, 6.5 langkah 2 dan 3 |
| 8 | Garis lapor bertanda usulan atau konfirmasi belum resmi | Bagian 2: "Hubungan atasan-bawahan bertanda “usulan/konfirmasi” tidak boleh diperlakukan sebagai reporting line resmi sampai disahkan." | Bagian 9 baris "Garis lapor ... berlabel menunggu konfirmasi" |
| 9 | Peninjauan 12 bulan atau saat perubahan signifikan | Bagian 4: "Next review | 12 bulan sejak efektif atau saat ada perubahan signifikan" | Kesimpulan kalimat 2 (YEARLY dari meta; pemicu lebih awal "grading jabatan ditetapkan" adalah bentuk khusus perubahan signifikan, (USULAN) lewat rujukan butir 4.2) |
| 10 | Pemilik proses | Tabel kontrol dokumen: "Process Owner" bernilai "HR Lead" diikuti nama pemegang jabatan | meta.process_owner |
| 11 | Mutasi di dokumen ISMS = perpindahan peran; langkah akses saat mutasi | specs/ISMS-SOP-02.json: "Mutasi", "Perpindahan peran seseorang."; prosedur 6.4: "Beri tahu mutasi paling lambat pada hari efektif." dan "Ajukan perubahan akses karena mutasi." dan "Cabut akses lama yang tidak relevan paling lambat 5 hari kerja sesudah mutasi." | 4.8, 6.4 langkah 4 dan 5, 6.5 langkah 5 dan 6, SLA baris 7 |
| 12 | Competency Matrix memetakan standar per tingkatan jabatan | config/checklist.json baris 9: "Matriks pemetaan standar keterampilan, pengetahuan, dan perilaku yang wajib dimiliki karyawan pada setiap tingkatan jabatan." | 4.2 kalimat 3, tabel Dokumen terkait (SNX-HR-FRM-01) |
| 13 | Training Plan dan Matrix menurut jenjang jabatan | config/checklist.json baris 10: "Dokumen perencanaan tahunan yang mengatur jadwal, jenis pelatihan, dan target peserta pelatihan sesuai jenjang jabatan." | 4.3, 6.5 langkah 3, tabel Dokumen terkait (SNX-HR-FRM-02) |
| 14 | Batas dengan Promotion, Demotion, Mutation | config/checklist.json baris 17, 18, 20: "Prosedur kenaikan jabatan dan tanggung jawab karyawan berdasarkan prestasi dan kualifikasi." / "Prosedur penurunan jabatan atau tingkat posisi akibat penurunan kinerja atau pelanggaran aturan perusahaan." / "Prosedur pemindahan karyawan ke unit kerja, divisi, atau lokasi operasional lain sesuai kebutuhan organisasi." | Scope, bagian 9 baris 3 dan 4 |
| 15 | Kolom Melapor ke dan Unit tiap jabatan | specs/HR-ORG-01.json, Daftar Jabatan, mis. JA-06: "Brand & Marketing", unit "Commercial", melapor ke "VP Commercial (JA-03)" | Definisi Tingkatan jabatan, Unit kerja, Atasan Langsung Asal dan tujuan |

## 3. Pemetaan kriteria (Description baris 19)

Kriteria: "Prosedur perpindahan tugas/fungsi karyawan dalam tingkatan jabatan yang sama untuk penyegaran atau pengembangan keterampilan."

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| Prosedur | Bagian 6 (6.1 sampai 6.5, 23 langkah), bagian 7 (diagram), bagian 8 (batas waktu), bagian 9 | Disusun dari kriteria dan pola SNX-HR-SOP-10; seluruhnya (USULAN) |
| perpindahan tugas/fungsi karyawan | Definisi Rotasi, Jabatan tujuan, Karyawan yang dirotasi; usulan 6.1; pembaruan data karyawan 6.4 langkah 3 | Kriteria; peran dan data dari SNX-HR-JA-01 |
| dalam tingkatan jabatan yang sama | Definisi Tingkatan jabatan dan Unit kerja; butir 4.2; penilaian 6.2 langkah 3; bagian 9 baris 3, 4, 6 | Kriteria; ukuran (USULAN) karena sumber tanpa grading (fakta kunci 2) |
| untuk penyegaran | Definisi Penyegaran; butir 4.1; penilaian 6.2 langkah 4 | Kata kriteria; definisi (USULAN) |
| atau pengembangan keterampilan | Definisi Pengembangan keterampilan dan Keterampilan yang dituju; butir 4.3; 6.2 langkah 4; 6.5 langkah 2 dan 3 | Kriteria; fakta kunci 3; fakta pendukung 7 dan 13 |

Pengecualian scope: kenaikan, penurunan, dan pemindahan ke unit kerja, divisi, atau lokasi lain mengikuti batas di checklist (fakta pendukung 14) dan scope SNX-HR-SOP-10, SNX-HR-SOP-11, SNX-HR-SOP-13 yang sudah ditulis. Pengecualian tujuan lain dan gaji (USULAN) diturunkan dari kriteria karena sumber diam.

Klausul ISO (checklist tidak memberi acuan; semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur dan rekaman |
|---|---|---|
| ISO 9001:2015 5.3 (Peran, tanggung jawab, dan wewenang organisasi) | 4.2, 4.4, 4.6, 4.7 | Tabel peran bagian 5; 6.4 langkah 1 dan 2 |
| ISO 9001:2015 7.2 (Kompetensi) | 4.1, 4.3 | 6.2 langkah 4; 6.5 langkah 2 dan 3 |
| ISO 9001:2015 7.5.3 (Pengendalian informasi terdokumentasi) | 4.10 | Tabel rekaman bagian 11 |
| ISO/IEC 27001:2022 7.2 (Kompetensi) | 4.3 | 6.5 langkah 2 dan 3 |
| ISO/IEC 27001:2022 Annex A 5.2 (Peran dan tanggung jawab keamanan informasi) | 4.6 | Tabel peran bagian 5 |
| ISO/IEC 27001:2022 Annex A 5.18 (Hak akses) | 4.8 | 6.4 langkah 4 dan 5; 6.5 langkah 5 dan 6 |

Nomor dan nama klausul berasal dari standar, bukan dari sumber (sumber hanya menyebut 9001 klausul 5.3, 7.2, 7.3, 7.5 dan tidak menyebut 27001), dan ditulis dari ingatan penyusun tanpa membuka teks standar (tidak diukur ulang di sesi ini).

## 4. Pemetaan nama peran (HR-ORG-01)

| Istilah di sumber atau kriteria | Peran di dokumen | Dasar | Label |
|---|---|---|---|
| HR Lead (Process Owner, Prepared by, atasan JA-12) | HR Manager (JA-14) | config/defaults.json data_conflicts "Jabatan Aziz Priyo Widakdo"; ORG-01 JA-14 | Tidak diberi label |
| HRGA Officer (JA-12) | HRGA Officer | Daftar Jabatan ORG-01 | Tidak diberi label |
| Management / Authorized Director (Approved by), approver | Direktur Utama (JA-01) | Template Approved By dan config/defaults.json; ORG-01 K-14 | USULAN (tabel peran, butir 4.5) |
| atasan langsung | Atasan Langsung Asal dan Atasan Langsung Tujuan | ORG-01 mendefinisikan "Atasan langsung"; rotasi punya dua jabatan sehingga dua sebutan, masing-masing didefinisikan di bagian 3 | Dicatat di sini |
| (tidak ada di sumber) karyawan yang berpindah tugas | Karyawan yang dirotasi | Istilah baru untuk satu hal; didefinisikan di bagian 3 | Dicatat di sini |
| Sebutan CEO, COO | Tidak dipakai | Dokumen tidak menyebut COO; "Direktur Utama" di badan, "President Director" hanya di blok Approved By | Aturan COO tidak terpicu |

Uji definisi Tingkatan jabatan terhadap ORG-01 (hanya di notes ini, bukan di dokumen). Jumlah garis lapor sampai Direktur Utama (JA-01) menurut kolom Melapor ke; tanda * berarti garisnya berlabel menunggu konfirmasi (K-02, K-03, K-04):

| Jabatan | Unit (ORG-01) | Jumlah garis lapor |
|---|---|---|
| JA-02 Direktur | Management | 1 |
| JA-03 VP Commercial | Commercial | 2 |
| JA-04 VP Tech Operation and Services | Operation | 2 |
| JA-05 Manager of Product Tech | Operation | 2* (3 bila K-02 memilih VP Commercial) |
| JA-06 Brand & Marketing, JA-07 Business Development | Commercial | 3 |
| JA-08 Legal & Compliance | Legal | 2* |
| JA-09 Legal & Compliance | Legal | 3 |
| JA-10 Finance, JA-11 Accounting & Tax | Finance, Accounting & Tax | 2* |
| JA-12 HRGA Officer | Human Resources | 3 |
| JA-13 Technical/Operation Engineer L1 | Operation | 3 |
| JA-14 HR Manager | Human Resources | 2* |
| JA-15 Office Helper | Human Resources | 4 |

Akibatnya, dari 15 jabatan yang kini ada hanya dua pasangan yang satu unit dan satu tingkatan: JA-06 dengan JA-07, dan JA-04 dengan JA-05 (yang terakhir bergantung pada K-02). Delapan jabatan Divisi Operation yang berstatus USULAN di ORG-01 (tanpa pemegang) menambah satu pasangan, NOC Engineer dengan SOC Analyst (masing-masing empat garis lapor sampai JA-01), karena sub divisi NOC dan SOC berada dalam satu unit Operation dan rotasi sementara di antaranya tetap rotasi menurut kalimat Batas rotasi dan mutasi di bagian 2. Ini dicatat di Open items 2 sebagai keputusan lingkup untuk Aziz.

## 5. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" di context/audit/iso-sinux-supdocs-hr-2026-10-14.md (fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status DRAF, revisi "03 -", tanggal efektif "-", nomor "usulan"; bukan dokumen terkendali | Tidak diteruskan ke SOP. SOP merujuk SNX-HR-JA-01 dan SNX-HR-ORG-01, yang masih Draft; ketergantungan ini dicatat di Open items 10 |
| 2 | Tidak ada KPI per jabatan, bagan organisasi, grading | KPI tidak dipakai (penilaian hasil rotasi berbasis kompetensi, bukan angka kinerja). Bagan dan grading: SOP merujuk ORG-01 untuk garis lapor dan memakai ukuran tingkatan (USULAN) karena grading tidak ada (fakta kunci 2). Open items 2 |
| 3 | Kalimat terpotong di Bagian 1 paragraf 2 | Tidak dipakai; tidak ada kalimat dari paragraf itu di SOP |
| 4 | Frasa kompetensi janggal ("Risk pemahaman karyawan", "pihak terkait management", dan sejenisnya) | Tidak ada frasa kompetensi sumber yang disalin ke SOP. "Keterampilan yang dituju" dirujuk ke kompetensi di SNX-HR-JA-01, yang memulihkannya (notes/HR-JA-01.md tabel 5, USULAN di sana). Karena itu penilaian keterampilan bergantung pada konfirmasi pemegang fungsi atas pemulihan itu: Open items 11 |
| 5 | Pelaporan Manager of Product Tech tidak konsisten (JA-05 lawan JA-03) | Memengaruhi hitungan tingkatan JA-05 (2 atau 3 garis lapor). Ditangani bagian 9 baris "Garis lapor ... berlabel menunggu konfirmasi" dan uji di bagian 4 notes ini; keputusan di ORG-01 K-02 |
| 6 | Atasan JA-06 dan JA-07 ditulis "Commercial - Laras Rasmawati" | Tidak dipakai langsung; SOP menghitung lewat ORG-01 yang menulis VP Commercial (JA-03) |
| 7 | Atasan JA-08, JA-10, JA-11, JA-14 "Management / Direktur", tidak satu atasan | Memengaruhi hitungan tingkatan. Ditangani bagian 9 baris "Garis lapor ... berlabel menunggu konfirmasi" (Direktur Utama menetapkan, USULAN); ORG-01 K-03 dan K-04 |
| 8 | Penamaan unit tidak seragam (Operations, Operation, HR / GA, Human Resources, HRGA / General Affairs) | SOP memakai nilai kolom Unit di ORG-01 (Operation, Human Resources, dan seterusnya) lewat definisi Unit kerja; ORG-01 K-06 |
| 9 | Dua jabatan berjudul sama "Legal & Compliance" | SOP tidak memakai judul jabatan tanpa kode; pembedanya garis lapor (JA-09 melapor ke JA-08), sehingga menurut definisi tingkatan keduanya berbeda tingkatan (3 lawan 2 garis lapor). Konsekuensi ini disebut di bagian 4 notes ini |
| 10 | Tidak ada jabatan Finance Lead atau Finance Staff | Tidak relevan untuk SOP ini; nol rujukan |
| 11 | Ejaan Samuel (Kristianto, Kristanto, Utomo) dan sebutan CEO | Badan dokumen memakai "Direktur Utama"; blok Approved By memakai "Samuel Kristanto Utomo / President Director" persis dari config/defaults.json |
| 12 | Teks persyaratan B dan F identik; empat varian pendidikan dan pengalaman | Tidak dipakai. Empat kelompok (SNX-HR-JA-01 butir 4.9) tidak dijadikan ukuran tingkatan karena K2 memuat JA-05 sampai JA-12, jadi jabatan manajer (JA-05 Manager of Product Tech) dan pelaksana (JA-12 HRGA Officer) jatuh ke kelompok sama |
| 13 | Masa pengalaman minimum belum ada; sertifikasi hanya bila ditetapkan Competency Matrix | Tidak dipakai; rotasi tidak mensyaratkan pengalaman. Rujukan ke Competency Matrix (SNX-HR-FRM-01) hanya untuk tingkatan jabatan (butir 4.2, USULAN) |
| 14 | Jumlah tabel stats.json 34 lawan 17 | Tidak relevan |
| 15 | Rujukan ISO di sumber hanya 9001 (5.3, 7.2, 7.3, 7.5); nol rujukan 27001 | Klausul di bagian 11 ditambah 27001:2022 7.2, Annex A 5.2, 5.18, semuanya berlabel "(USULAN, perlu konfirmasi konsultan)". Klausul 7.3 sumber tidak dipakai |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Sumber tidak memuat konsep rotasi, tingkatan jabatan, atau penyegaran (fakta di bagian 1 notes) | Seluruh alur disusun dari kriteria; semua langkah berlabel USULAN lewat kalimat pembuka 6.1. Tidak ada kalimat sumber yang dikutip sebagai dasar alur |
| B | Sumber tidak menyebut sistem untuk hak akses atau tiket | SOP tidak menyebut Zammad atau GLPI; perubahan hak akses dirujuk ke SNX-ISMS-SOP-02, yang punya langkah dan rekamannya sendiri |
| C | "Mutasi" di SNX-ISMS-SOP-02 berarti perpindahan peran, sedangkan "Mutation" (SNX-HR-SOP-13) berarti pemindahan unit, divisi, atau lokasi | Butir 4.8 menyebut perbedaan itu sekali dan memperlakukan rotasi sebagai mutasi menurut ISMS (USULAN). Pemutus: Fani dengan Aziz |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Rotasi dibaca sementara: ada masa rotasi, lalu karyawan kembali ke tugas semula (butir 4.9, 6.5). Kriteria tidak menyebut sementara atau permanen. Tafsir ini berlabel USULAN dan menjadi Open items 1.
2. "Tingkatan jabatan yang sama" diukur dengan jumlah garis lapor sampai Direktur Utama di ORG-01. Pilihan lain yang dipertimbangkan dan ditolak: kelompok persyaratan pendidikan (cacat 12), dan "atasan langsung yang sama" (menolak pasangan sejajar yang berbeda atasan langsung).
3. Rotasi dibatasi satu unit kerja karena SNX-HR-SOP-10 dan SNX-HR-SOP-13 sudah menarik batasnya di sana. Sub divisi Divisi Operation (NOC, SOC, serta SD dan PM) dianggap satu unit Operation karena ORG-01 menaruh ketiganya di bawah unit Operation (USULAN). Kalimat Batas rotasi dan mutasi di bagian 2 (dari orkestrator, USULAN) hanya menggolongkan perpindahan menetap ke sub divisi itu sebagai mutasi; perpindahan sementara antar sub divisi dalam unit Operation tetap rotasi.
4. Pengusul = Atasan Langsung Asal; penetap = Direktur Utama; penilai dan perekomendasi = HR Manager; pencatat dan pengarsip = HRGA Officer. Pola ini sama dengan SNX-HR-SOP-10 agar set dokumen HR seragam. Atasan Langsung Tujuan menanggapi usulan (langkah tambahan khas rotasi, USULAN).
5. Selama masa rotasi, pengajuan perubahan hak akses dilakukan Atasan Langsung Tujuan; saat masa rotasi berakhir oleh Atasan Langsung Asal. Sumber tidak menyebut garis lapor karyawan selama masa rotasi (Open items 8).
6. Angka batas waktu bagian 8 (3, 3, 5, 5, 2, 5 hari kerja) tidak berasal dari sumber. Angka dipakai ulang dari pola SNX-HR-SOP-10 supaya seragam, semuanya berlabel USULAN. Satu-satunya batas waktu bersumber adalah pemberitahuan perubahan tugas "paling lambat pada tanggal berlaku", yang mengikuti "Beri tahu mutasi paling lambat pada hari efektif." di SNX-ISMS-SOP-02.
7. Lokasi rekaman ("folder Google Drive Departemen HR"), pemilik HRGA Officer, dan retensi "selama karyawan bekerja di SINUX" tanpa sumber; mengikuti pola SNX-HR-SOP-10 dan berlabel USULAN. Tidak ada angka retensi.
8. Klasifikasi: worklist memberi INTERNAL untuk SOP, dipakai persis. Rekaman rotasi diusulkan RESTRICTED (Internal) di 4.10 (aturan config/defaults.json: data karyawan = RESTRICTED (Internal)).
9. Tiket Zammad dan GLPI, vault, PPN, dan COO tidak muncul di dokumen ini; aturan lintas dokumen itu tidak terpicu.
10. Sumber tidak memuat rujukan internal AI; tidak ada yang dibuang.
11. Perubahan perjanjian kerja dan gaji akibat rotasi tidak diatur. Gaji dan tunjangan dikecualikan di scope (USULAN); perjanjian kerja menjadi Open items 6 (tidak ada Legal & Compliance di tabel peran karena tidak ada kontrol pengganti di sumber).

## USULAN

| # | Butir USULAN di spec | Pemutus yang disarankan |
|---|---|---|
| U1 | Klausul ISO di bagian 11: 9001:2015 5.3, 7.2, 7.5.3; 27001:2022 7.2, Annex A 5.2, 5.18, label "(USULAN, perlu konfirmasi konsultan)" | Konsultan, lalu owner |
| U2 | Definisi Tingkatan jabatan: jumlah garis lapor sampai Direktur Utama (JA-01) | Aziz, dengan Samuel |
| U3 | Tingkatan jabatan memakai SNX-HR-FRM-01 bila sudah disahkan dan menetapkan tingkatan (4.2) | Aziz |
| U4 | Syarat satu unit kerja (4.2); definisi Unit kerja dengan sub divisi NOC, SOC, serta SD dan PM dalam satu unit Operation; kalimat Batas rotasi dan mutasi di bagian 2 (sementara = rotasi, menetap = mutasi) | Aziz, dengan Samuel |
| U5 | Definisi Penyegaran: tugas atau fungsi berbeda tanpa keterampilan yang dituju | Aziz |
| U6 | Hari kerja tidak termasuk hari libur resmi | Aziz |
| U7 | Pengecualian scope: tujuan selain butir 4.1, dan gaji serta tunjangan akibat rotasi | Aziz |
| U8 | Keputusan rotasi tertulis oleh Direktur Utama; rotasi berlaku sesudah keputusan itu (4.5, tabel peran) | Samuel, dengan Aziz |
| U9 | Batas wewenang HR Manager: merekomendasikan, tidak memutuskan, dengan rujukan JA-14 (tabel peran); diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Samuel, dengan Aziz |
| U10 | Konfirmasi tertulis karyawan atas uraian jabatan tujuan sebelum tanggal berlaku (4.7, 6.4, SLA) | Aziz |
| U11 | Penilaian kompetensi aktual sesudah masa rotasi, pencatatan kesenjangan, dan tindakan pelatihan di SNX-HR-FRM-02 (4.3, 6.5) | Aziz |
| U12 | Rotasi diperlakukan sebagai mutasi menurut SNX-ISMS-SOP-02; pengajuan akses oleh Atasan Langsung Tujuan (saat berlaku) dan Atasan Langsung Asal (saat berakhir) (4.8, 6.4, 6.5) | Fani, dengan Aziz |
| U13 | Masa rotasi ditulis Direktur Utama di keputusan; karyawan kembali ke tugas semula sesudah masa rotasi (4.9) | Aziz, dengan Samuel |
| U14 | Klasifikasi RESTRICTED (Internal) untuk rekaman rotasi (4.10) | Aziz, dikonfirmasi owner |
| U15 | Lokasi rekaman (folder Google Drive Departemen HR), pemilik HRGA Officer, retensi selama karyawan bekerja (bagian 11) | Aziz |
| U16 | Tanggapan tertulis Atasan Langsung Tujuan sebagai langkah wajib dan wewenangnya menolak (6.2, tabel peran, bagian 9 baris 1) | Aziz |
| U17 | Pengusul = Atasan Langsung Asal; karyawan atau HR Manager yang memprakarsai menyampaikan ke Atasan Langsung Asal (6.1, bagian 9 baris 7); diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Aziz |
| U18 | Batas waktu bagian 8: 3, 3, 5, 5, 2, dan 5 hari kerja; konfirmasi sebelum tanggal berlaku; laporan hasil rotasi pada akhir masa rotasi | Aziz |
| U19 | Penanganan bagian 9: pengembalian usulan oleh HR Manager atau HRGA Officer, rujukan ke SNX-HR-SOP-10, SNX-HR-SOP-11, SNX-HR-SOP-13, dan penetapan garis lapor oleh Direktur Utama; diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Aziz, dengan Samuel untuk garis lapor |
| U20 | Seluruh langkah 6.1 sampai 6.5 (kalimat pembuka 6.1) dan diagram (keterangan Gambar 1) | Aziz, dengan Samuel |
| U21 | HR Manager memeriksa kepatuhan dengan membandingkan rekaman, langkah, dan batas waktu (Kesimpulan kalimat 1); diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Aziz |
| U22 | Pemicu peninjauan lebih awal: grading jabatan ditetapkan (Kesimpulan kalimat 2) | Aziz |

Total: 22 butir USULAN. Label "(USULAN)" persis di dokumen terhitung 46 oleh lint (warn); satu butir bisa berlabel di beberapa tempat (mis. U18 di delapan baris SLA, U15 di enam sel tabel rekaman).

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Kalimat Batas rotasi dan mutasi di bagian 2 (USULAN) menetapkan perpindahan sementara dengan kembali ke tugas semula sebagai rotasi, dan perpindahan menetap sebagai mutasi. Lama masa rotasi dan frekuensi rotasi tidak ada di SNX-HR-JA-01, SNX-HR-ORG-01, maupun sumber | Aziz, Samuel |
| 2 | Ukuran "tingkatan jabatan yang sama". Grading tidak ada; dipakai jumlah garis lapor. Dengan 15 jabatan sekarang hanya JA-06 dengan JA-07 dan JA-04 dengan JA-05 yang memenuhi (bagian 4 notes ini). Perlu diputus apakah lingkup ini memang dimaksud, atau tingkatan ditetapkan lewat grading atau SNX-HR-FRM-01; diubah W9: JA-04 kini punya dua garis lapor tegas (ke Direktur dan ke Direktur Utama, LEAD G-3 A3); pasangan JA-04 dengan JA-05 belum dihitung ulang, lihat open item 15 | Aziz, owner |
| 3 | Batas Rotation lawan Mutation memakai kalimat di bagian 2 (USULAN): perpindahan sementara antar sub divisi Operation (NOC, SOC, serta SD dan PM) dalam satu unit Operation tetap rotasi; perpindahan menetap ke sub divisi itu, ke unit kerja lain, atau ke lokasi lain adalah mutasi (SNX-HR-SOP-13). Perlu konfirmasi karena ORG-01 menaruh ketiga sub divisi di bawah satu Divisi Operation | Aziz |
| 4 | Penetap rotasi. Dokumen memakai Direktur Utama (USULAN). Alternatif: HR Manager menetapkan dalam batas Authority Matrix, yang belum bernomor; diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Samuel, Aziz |
| 5 | Siapa boleh memprakarsai rotasi (Atasan Langsung Asal, karyawan, HR Manager) dan akibat bila Atasan Langsung Asal menolak mengajukan usulan; diubah W9: sebutan jabatan HR Manager menjadi HR Lead di dokumen | Aziz |
| 6 | Akibat rotasi pada perjanjian kerja, gaji, dan tunjangan tidak diatur; tidak ada peran Legal & Compliance di dokumen. Perlu diputus apakah rotasi pernah menuntut perubahan perjanjian kerja | Aziz, Legal |
| 7 | Perpindahan dengan tujuan selain penyegaran atau pengembangan keterampilan (mis. kebutuhan operasional) tidak punya dokumen pengatur selain SNX-HR-SOP-13 untuk pindah unit; dokumen ini hanya mengembalikan usulannya | Aziz |
| 8 | Garis lapor karyawan selama masa rotasi (tetap ke Atasan Langsung Asal atau pindah ke Atasan Langsung Tujuan) tidak ditetapkan. Dokumen menaruh pengajuan hak akses pada Atasan Langsung Tujuan saat berlaku | Aziz, Fani |
| 9 | Batas waktu bagian 8, lokasi dan retensi rekaman, dan klasifikasi RESTRICTED (Internal) tanpa sumber (U14, U15, U18) | Aziz |
| 10 | Dokumen ini bergantung pada SNX-HR-JA-01 dan SNX-HR-ORG-01 yang berstatus Draft (butir K-02, K-03, K-04 di ORG-01 memengaruhi hitungan tingkatan), SNX-HR-FRM-01 dan SNX-HR-FRM-02 (dalam pengerjaan saat itu), serta SNX-HR-SOP-11 dan SNX-HR-SOP-13 yang batasnya dicocokkan ke scope yang sudah tertulis. Verifikator mencocokkan ulang sesudah semuanya selesai; diubah W9: SNX-HR-FRM-02 sudah ada, "dalam pengerjaan" dihapus dan dirujuk dengan nomor dan judul; R2: SNX-HR-FRM-01 (Employee Competency Matrix) juga sudah ada, "dalam pengerjaan" dihapus dan dirujuk dengan nomor dan judul. | Verifikator, Aziz |
| 11 | Frasa kompetensi sumber yang janggal (audit butir 4) dipulihkan di SNX-HR-JA-01 sebagai USULAN. "Keterampilan yang dituju" memakai kompetensi hasil pemulihan itu; perlu konfirmasi pemegang fungsi | Aziz |
| 12 | Klausul ISO ditulis dari ingatan penyusun, belum dicek terhadap teks standar | Konsultan |
| 13 | Kalimat bernada kewajiban di sumber ("Atasan langsung serta bawahan langsung yang belum ditetapkan secara resmi harus dikonfirmasi oleh manajemen sebelum pengesahan.") ditujukan ke Management, bukan ke penyusun; tidak dijalankan, dicatat saja | Samuel, Aziz |
| 14 | Kepemilikan: HR Manager sebagai Process Owner berasal dari pemetaan "HR Lead" ke HR Manager (config/defaults.json), bukan dari konfirmasi Aziz atas SOP ini; ditutup W9: owner 15 Okt memutus jabatan Aziz = HR Lead; Process Owner dan seluruh dokumen memakai HR Lead. | Aziz |
| 15 | Sejak JA-03 dan JA-04 punya dua garis tegas (ke Direktur dan ke Direktur Utama, LEAD G-3 A3), ukuran tingkatan jabatan (USULAN) "jumlah garis lapor sampai Direktur Utama" bermakna ganda untuk JA-03, JA-04, dan bawahannya; perlu aturan jalur mana yang dihitung. Teks dokumen tidak diubah (R2) | Aziz, owner |

## 7. Pemeriksaan bahasa (dua pertanyaan, dijawab sebelum selesai)

Apa yang membuat teks ini terdengar buatan AI? Temuan pada draf pertama, semuanya sudah diperbaiki di spec:
- Definisi Atasan Langsung Tujuan memakai "Jabatannya bisa sama dengan ...", sehingga "-nya" bisa menunjuk dua hal. Diganti "Jabatan ini bisa sama dengan Atasan Langsung Asal."
- Butir 4.4 menyebut HRGA Officer "mencatat dan mengarsipkan setiap tahap", padahal HR Manager yang menulis kesimpulan penilaian dan kesenjangan. Dipersempit menjadi "memperbarui data karyawan dan mengarsipkan rekaman (butir 6.4 dan 6.5)".
- Butir 4.8 semula menyatakan rotasi termasuk mutasi seolah isi dokumen ISMS. Itu tafsir; diganti "Rotasi diperlakukan sebagai mutasi (USULAN)".
- Definisi Unit kerja memakai "Isi kolom Unit"; diganti "Nama di kolom Unit pada SNX-HR-ORG-01".
- Draf awal memuat "tugas sesudah masa rotasi" di usulan dan keputusan sehingga arah akhir rotasi terbuka (kembali atau menetap). Diganti satu aturan eksplisit (butir 4.9) agar langkah akhir punya pelaku yang jelas.
- Diagram draf pertama 22 simpul dan terlalu panjang untuk halaman; dilebur dan label diperpendek.
- Sisa yang tidak saya ubah dan perlu mata manusia: pola butir bagian 4 yang berulang (judul, rujukan ISO dalam kurung, titik dua, kalimat, rujukan butir) dan awalan "Hasil yang dijaga:" di Purpose, keduanya pola yang sama dengan SNX-HR-SOP-10 sehingga set dokumen HR seragam; banyaknya label (USULAN) (46 kemunculan) yang membuat bacaan berat tetapi memang menandai isi tanpa sumber.

Adakah fakta, angka, nama, atau tanggal tanpa sumber?
- Angka di bagian 8 (3, 3, 5, 5, 2, 5 hari kerja) tidak bersumber; semuanya berlabel USULAN (U18). Satu batas waktu ("paling lambat pada tanggal berlaku") bersumber dari SNX-ISMS-SOP-02. Tidak ada angka lain: jumlah hitungan garis lapor di definisi Tingkatan jabatan berupa cara menghitung, bukan data; hasil hitungannya hanya ada di notes ini dan berasal dari kolom Melapor ke di ORG-01.
- Tanpa sumber dan sudah berlabel atau tercatat: klausul ISO (U1, dari ingatan); definisi Tingkatan jabatan, Unit kerja, Penyegaran (U2, U4, U5); lokasi rekaman, pemilik, retensi (U15); klasifikasi RESTRICTED (Internal) (U14); semua pelaku langkah yang tidak disebut sumber (U8, U9, U12, U16, U17).
- Nama orang hanya di blok approval dan berasal dari config/defaults.json. Kode JA-01 dan JA-14 berasal dari specs/HR-ORG-01.json dan sumber; JA-12 dari sumber. Nama unit (Commercial, Operation, Legal) dan sub divisi (NOC, SOC, SD dan PM) dari specs/HR-ORG-01.json. Nama sistem: hanya Google Drive (U15, berlabel); tidak ada Zammad, GLPI, atau vault. Tidak ada tanggal; tanggal efektif kosong.
- Diperbaiki sesudah pemeriksaan: usulan semula meminta karyawan menyebut "tugas sesudah masa rotasi", yang tidak punya dasar dan membuka dua kemungkinan; diganti aturan kembali ke tugas semula berlabel USULAN. Butir 4.8 semula menyatakan rotasi termasuk mutasi sebagai fakta; kini berlabel USULAN.

## Sweep

Sumber butir: /tmp/claude-0/prompts/HR-SOP-12.sweep.txt dan qa/HR-SOP-12.verify.json (nonblocking). Hanya specs/HR-SOP-12.json dan notes/HR-SOP-12.md yang diubah. Salinan spec sebelum sweep: /tmp/pen-HR-SOP-12/HR-SOP-12.pre-sweep.json.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1 (4.2 unit kerja) | 4.2: "jabatan tujuan harus satu tingkatan dan satu unit kerja dengan jabatan karyawan, menurut definisi di bagian 3." (tanpa label) | 4.2: "jabatan tujuan harus satu tingkatan dengan jabatan karyawan menurut definisi di bagian 3, dan berada di unit kerja yang sama (USULAN; batas rotasi dan mutasi ada di bagian 2)." |
| 1 (pasif) | Purpose: "hasilnya dinilai sesudah masa rotasi." 4.8: "hak akses lama yang tidak relevan dicabut dan hak akses baru diajukan". Langkah 6.4 nomor 4 dan 6.5 nomor 5: "agar perubahan hak akses diajukan menurut SNX-ISMS-SOP-02" | Purpose: "HR Manager menilai keterampilan karyawan sesudah masa rotasi." 4.8: "Atasan Langsung Tujuan saat tanggal berlaku, dan Atasan Langsung Asal saat masa rotasi berakhir, mengajukan perubahan hak akses menurut butir Perubahan Akses saat Mutasi di SNX-ISMS-SOP-02". Dua langkah: "supaya ia mengajukan perubahan hak akses" (rujukan SNX-ISMS-SOP-02 tinggal di langkah pengajuan berikutnya). Pencabutan akses lama oleh peran di SNX-ISMS-SOP-02 tidak disebut ulang di SOP ini |
| 1 (sinonim) | Output "Permintaan perubahan akses" (dua langkah); "setelah" di bagian 9 baris 2; "ke tugas sebelum rotasi" (6.5 langkah 4); Dokumen terkait: "perubahan akses saat mutasi"; 4.8: "SNX-ISMS-SOP-02 memakai kata mutasi untuk perpindahan peran seseorang" | "Permintaan perubahan hak akses"; "sesudah"; "ke tugas semula"; "perubahan hak akses saat mutasi"; "kata mutasi di SNX-ISMS-SOP-02 berarti perpindahan peran seseorang" |
| 2 | Sama dengan butir 1 (duplikat dalam instruksi) | Sama dengan butir 1; tidak ada perubahan tambahan |
| 3 | "(USULAN, dikonfirmasi konsultan)" di bagian 11, baris "Status acuan klausul" | "(USULAN, perlu konfirmasi konsultan)" |
| 4 (kalimat batas) | Scope dua paragraf; definisi Unit kerja: "Sub divisi NOC, SOC, serta SD dan PM berada dalam satu unit Operation (USULAN)." | Scope paragraf ketiga berisi kalimat identik: "Batas rotasi dan mutasi: perpindahan sementara untuk penyegaran atau pengembangan keterampilan, dalam unit kerja dan tingkatan jabatan yang sama, dengan karyawan kembali ke tugas semula sesudah masa rotasi, adalah rotasi (SNX-HR-SOP-12). Perpindahan menetap karena kebutuhan organisasi ke unit kerja, sub divisi Operation (NOC, SOC, serta SD dan PM), atau lokasi operasional lain adalah mutasi (SNX-HR-SOP-13) (USULAN)." Definisi Unit kerja tidak diubah: "Sub divisi NOC, SOC, serta SD dan PM berada dalam satu unit Operation (USULAN)." (perubahan sementara di sweep pertama dibatalkan, lihat baris Pembatalan) |
| 4 (nama peran) | "Atasan Langsung asal", "Atasan Langsung tujuan" (42 kemunculan: 24 dan 18, juga di tabel peran, langkah, SLA, bagian 9, diagram); dua kemunculan "Atasan Langsung" tanpa keterangan (keterangan Gambar 1, tabel Dokumen terkait baris SNX-HR-ORG-01) | "Atasan Langsung Asal" (27 kemunculan) dan "Atasan Langsung Tujuan" (21 kemunculan, bertambah karena 4.8 dan dua langkah kini menyebut pelaku), termasuk di diagram; dua kemunculan tanpa keterangan diberi keterangan |
| 4 (penetap) | Direktur Utama | Tidak diubah |
| Pembatalan (temuan qa/HR-SOP-12.sweep.r1.json) | Di sweep pertama definisi Unit kerja diubah menjadi "Sub divisi NOC, SOC, serta SD dan PM dihitung sebagai unit kerja tersendiri (USULAN)." | Dibatalkan; kembali ke "Sub divisi NOC, SOC, serta SD dan PM berada dalam satu unit Operation (USULAN)." Alasan: perubahan itu membalik makna di luar butir dan salah membaca kalimat batas. Kalimat batas hanya menggolongkan perpindahan menetap ke sub divisi Operation sebagai mutasi; perpindahan sementara antar sub divisi dalam unit Operation tetap rotasi. Dengan definisi unit tersendiri, 4.2 dan bagian 9 (baris "Jabatan tujuan berada di unit kerja lain") akan menolak rotasi sementara antar sub divisi. Dengan definisi dikembalikan, 4.2 dan bagian 9 tidak menolaknya karena sub divisi itu satu unit Operation; teks 4.2 dan bagian 9 tidak diubah |

Hal yang sengaja tidak diubah (di luar butir): keterangan Gambar 1 dan garis putus-putus simpul "Kembalikan usulan" yang kembali ke simpul pengajuan untuk semua jenis pengembalian; tugas bagian 9 yang belum tercermin penuh di tabel peran (HRGA Officer memberi tahu Atasan Langsung Asal, Direktur Utama menetapkan garis lapor dan penundaan tanggal berlaku); awalan "Hasil yang dijaga:" di Purpose, yang sama dengan SNX-HR-SOP-10. Ketiganya temuan verify nonblocking yang bukan butir sweep; dicatat agar LEAD memutuskan.

Catatan: kode SNX-HR-SOP-12 muncul di badan dokumen hanya pada kalimat batas (kalimat itu wajib identik dengan SNX-HR-SOP-13), sehingga tidak dimasukkan ke tabel Dokumen terkait (dokumen tidak mendaftar dirinya sendiri).

Uji sesudah sweep (bukti: /tmp/pen-HR-SOP-12/lint.out.txt, validate.out.txt, blankscan.out.txt): render tanpa galat; lint `"pass": true`, `"fails": []`, warn 46 butir (USULAN), warn PIC SLA nol; validator OOXML "All validations PASSED!"; blankscan.py `ok 17 HR-SOP-12.docx []`; JSON valid; nol em-dash dan en-dash; terpanjang langkah 24 kata; semua PIC ada di tabel peran.

## ISO-W9

Sumber: LEAD G-3 (A2, A3, B2, B4) dan butir kerja ISO-W9. Hanya butir di bawah yang diubah.

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 jabatan Aziz | "HR Manager" (38 kemunculan: Peran, PIC, SLA, rekaman, simpul diagram, process_owner, blok Reviewed) | "HR Lead"; blok Reviewed "Aziz Priyo Widakdo / HR Lead" |
| B4 SNX-HR-FRM-02 (bagian 11) | "Annual Training Plan & Training Matrix, dalam pengerjaan: tempat tindakan pelatihan atas kesenjangan keterampilan (butir 4.3 dan 6.5 SOP ini, (USULAN))." | "Annual Training Plan & Training Matrix: tempat tindakan pelatihan atas kesenjangan keterampilan (butir 4.3 dan 6.5 SOP ini, (USULAN))." |
| R2 B4 SNX-HR-FRM-01 (bagian 11) | "Employee Competency Matrix, dalam pengerjaan: standar keterampilan, pengetahuan, dan perilaku per tingkatan jabatan; acuan tingkatan jabatan bila sudah disahkan (butir 4.2 SOP ini, (USULAN))." | "Employee Competency Matrix: standar keterampilan, pengetahuan, dan perilaku per tingkatan jabatan; acuan tingkatan jabatan bila sudah disahkan (butir 4.2 SOP ini, (USULAN))." |

A3 garis lapor JA-03 dan JA-04: dokumen ini tidak menyebut atasan atau garis lapor JA-03 atau JA-04 dan tidak memakai keduanya sebagai contoh ukuran tingkatan jabatan, jadi tidak ada perubahan. Label K-02, K-03, K-04 tidak disentuh. SPV tidak ditambahkan: dokumen tidak punya kolom tingkat jabatan. Ukuran tingkatan jabatan (USULAN, jumlah garis lapor) tidak diubah dan tidak memakai JA-03 atau JA-04 sebagai contoh di spec. Catatan lama di notes ini yang menyebut JA-04 sebagai contoh hitungan (open item 2) bersifat riwayat; hitung ulang dengan dua garis lapor JA-04 (Direktur dan Direktur Utama) belum dilakukan karena ukurannya tidak berubah dan pemutus (LEAD, SNX-HR-ORG-01) memegang garis baru itu. Kalimat batas rotasi dan mutasi dan definisi Unit kerja (NOC, SOC, serta SD dan PM) tidak diubah; SNX-HR-SOP-13 kini memakai definisi Unit kerja yang sama.

Open item: #14 ditutup W9; #10 diubah W9.

Open item R2 (baru, nomor 15): Sejak JA-03 dan JA-04 punya dua garis tegas (ke Direktur dan ke Direktur Utama, LEAD G-3 A3), ukuran tingkatan jabatan (USULAN) "jumlah garis lapor sampai Direktur Utama" bermakna ganda untuk JA-03, JA-04, dan bawahannya; perlu aturan jalur mana yang dihitung. Teks dokumen tidak diubah (R2). Pemutus: Aziz, owner. Open item #2 dan #10 diberi tanda "diubah W9" di barisnya.
