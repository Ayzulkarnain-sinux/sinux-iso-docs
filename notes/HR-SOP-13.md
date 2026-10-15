# Catatan penyusun HR-SOP-13: Mutation

Status: DRAFTED (spec + notes ada). Spec: specs/HR-SOP-13.json. Mode sop, aksi T2, wave W4, nomor SNX-HR-SOP-13 (nomor lama dipertahankan), department "Human Resources", classification "INTERNAL", audit_class None. Approval persis dari config/defaults.json: prepared "Sita Nadia Salsabila Widodo / HRGA Officer", reviewed "Aziz Priyo Widakdo / HR Manager", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "HR Manager" (jabatan tanpa nama): sumber menulis "Process Owner | HR Lead – Aziz Priyo Widakdo"; jabatan Aziz di semua dokumen = HR Manager (config/defaults.json data_conflicts, butir "Jabatan Aziz Priyo Widakdo"), sama dengan HR-ORG-01, HR-JA-01, dan HR-SOP-10.

Hasil uji terakhir (bukti mentah: /tmp/pen-HR-SOP-13/lint.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-SOP-13.json /tmp/pen-HR-SOP-13/HR-SOP-13.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-SOP-13/HR-SOP-13.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "58 butir (USULAN) menunggu ACC" (sesudah putaran sweep). Warn PIC SLA nol.
- Uji sweep: `python3 -I reports/orch/blankscan.py /tmp/pen-HR-SOP-13/HR-SOP-13.docx` memberi `ok 18 HR-SOP-13.docx []` (18 halaman, nol halaman kosong); validator OOXML lulus. Angka halaman putaran 1 di bawah (17 halaman) mendahului sweep.
- Uji halaman (putaran perbaikan 1): `soffice --headless --convert-to pdf` lalu `pdftotext` per halaman. 17 halaman, jumlah kata per halaman 20, 75, 56, 73, 290, 273, 402, 214, 216, 184, 174, 18, 237, 230, 80, 208, 116 (bukti: /tmp/pen-HR-SOP-13/page_words.txt). Halaman 15 yang tadinya kosong kini memuat ujung tabel bagian 9 dan seluruh bagian 10. Halaman 12 hanya diagram dengan judul bagian 7 dan keterangan gambar; halaman 1 sampul.
- Validator OOXML (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!".
- Diagram /tmp/pen-HR-SOP-13/HR-SOP-13_flow.png dibuka (sebelum putaran 1; hanya label simpul 'Berikan informasi jabatan baru' yang berubah sesudahnya): 16 simpul, rankdir TB, label Ya dan Tidak terbaca, garis putus-putus kembali ke simpul awal.
- Pemeriksaan tambahan atas spec (skrip python3 -I di scratchpad sesi, bukan di repo): nol em-dash dan en-dash; 19 langkah, terpanjang 21 kata; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5 (delapan peran); semua kode SNX yang dirujuk di badan ada di tabel Dokumen terkait; nol kalimat yang berulang antarbagian; nol temuan frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, hulu ke hilir), nol "komersil", nol "diagnosa", nol "Lead", nol "tim", nol frasa meta ("dokumen sumber", "sumber tim", "penyusun", "draf ini"); "Atasan Langsung" selalu diikuti Asal atau Tujuan.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control, reference tidak diubah. Berkas yang ditulis hanya specs/HR-SOP-13.json dan notes/HR-SOP-13.md; hasil render hanya di /tmp/pen-HR-SOP-13/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (HR-JA-001, revisi 03, status DRAF) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (dari prompt tugas; tidak diukur ulang di sesi ini karena alat metadata Drive tidak dimuat) | read_file_content, teks penuh (15 jabatan JA-01 sampai JA-15, bagian 1 sampai 4). download_file_content tidak dipanggil: teks sudah lengkap dan penomoran butir tidak dipakai |
| Kriteria penerimaan | config/checklist.json baris 20 | tidak berlaku | Description: "Prosedur pemindahan karyawan ke unit kerja, divisi, atau lokasi operasional lain sesuai kebutuhan organisasi." Kolom iso_9001 dan iso_27001 kosong |
| Catatan cacat | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian "hr/HR-JA-001.md" (frontmatter, bagian 3, 4, 5 butir 1 sampai 15) | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran dan jabatan | specs/HR-ORG-01.json (DONE), specs/HR-JA-01.json (DONE) | repo kerja | Daftar Jabatan, kolom Unit dan Melapor ke, tabel Definisi, butir 4.3 sampai 4.10 di HR-JA-01 |
| Akses saat mutasi | specs/ISMS-SOP-02.json (DONE) | repo kerja | Bagian "Perubahan Akses saat Mutasi", tabel SLA, tabel rekaman, Service Hub (GLPI) |
| Pola dokumen HR serumpun | specs/HR-SOP-10.json (sudah ada di disk saat penyusunan) | repo kerja | Dibaca agar peran, istilah, dan pembagian keputusan sama. Kalimat tidak disalin, hanya pola dan istilah yang sama untuk satu hal |

Sumber utama tidak memuat satu pun ketentuan tentang mutasi, pemindahan karyawan, atau lokasi kerja selain yang dikutip di bawah. Prosedur 6.1 sampai 6.4 disusun untuk memenuhi kolom Description dan seluruhnya berstatus (USULAN) (intro butir 6.1).

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat bernada kewajiban di sumber (mis. "Atasan langsung serta bawahan langsung yang belum ditetapkan secara resmi harus dikonfirmasi oleh manajemen sebelum pengesahan.") ditujukan ke Management, bukan ke penyusun, dan tidak dijalankan.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Garis lapor berlabel usulan atau konfirmasi belum resmi. Dipakai di pengecualian bagian 9 (jabatan atasan berlabel menunggu konfirmasi) dan butir 4.10 | "Hubungan atasan-bawahan bertanda “usulan/konfirmasi” tidak boleh diperlakukan sebagai reporting line resmi sampai disahkan." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Tanggung jawab dan kewenangan harus ditetapkan, dikomunikasikan, dan dipahami. Dipakai di butir 4.7 dan langkah 6.4 nomor 2 dan 3 (karyawan menerima dan mengonfirmasi informasi jabatan baru) | "ISO 9001:2015 klausul 5.3: tanggung jawab dan kewenangan harus ditetapkan, dikomunikasikan dan dipahami." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 3 | Keputusan pengangkatan atau pemutusan hubungan kerja mengikuti delegasi dan persetujuan tertulis. Mutasi diperlakukan sama di butir 4.6 (USULAN) | "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Fakta pendukung dan kutipan verbatim

Semua kutipan dari fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di SOP |
|---|---|---|---|
| 1 | Direktur Utama mengesahkan perubahan organisasi, dasar Direktur Utama menetapkan keputusan mutasi (USULAN) | JA-01 A.6: "Mengesahkan kebijakan utama, anggaran dan perubahan organisasi sesuai kewenangan korporasi." | 4.3, 4.6, peran Direktur Utama |
| 2 | Atasan Direktur Utama = organ perusahaan, dasar pengecualian mutasi Direktur Utama | JA-01 tabel identitas, Atasan Langsung: "Organ perusahaan sesuai ketentuan dan anggaran dasar (verifikasi)" | Scope |
| 3 | Jabatan tidak otomatis memberi hak tanda tangan atau otorisasi keuangan | Bagian 2: "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." | 4.5 |
| 4 | Kompetensi dinilai dan kesenjangan ditindaklanjuti | Bagian 2: "ISO 9001:2015 klausul 7.2: tetapkan kompetensi yang diperlukan, nilai kompetensi aktual, lakukan tindakan jika terdapat kesenjangan, simpan bukti pendukung." | 4.4, 6.2 nomor 4 dan 5 |
| 5 | Masa pengalaman minimum belum ditetapkan | Bagian B tiap jabatan: "Masa pengalaman minimum ditentukan setelah job evaluation." | 4.4 |
| 6 | HR Manager mengendalikan administrasi kepegawaian termasuk perubahan data | JA-14 A.3: "Mengendalikan administrasi kepegawaian, termasuk perjanjian kerja, pengelolaan berkas karyawan, orientasi karyawan baru, perubahan data, dan proses pengakhiran hubungan kerja." | Peran HR Manager, 6.4 nomor 8 |
| 7 | HR Manager merekomendasikan, approver memutuskan | JA-14 E.4: "Merekomendasikan hiring, salary action, disciplinary action dan policy kepada approver" | 4.3, wewenang HR Manager |
| 8 | HRGA Officer memelihara data dan personal file, mengeskalasi keputusan HR | JA-12 A.1: "Memelihara data karyawan, kontrak, personal file dan administrasi orientasi karyawan baru/proses keluar karyawan." JA-12 E.3: "Mengeskalasi keputusan HR dan persetujuan ke HR Lead" | Peran HRGA Officer, 6.4 nomor 4 dan 5 |
| 9 | Legal & Compliance meninjau kontrak tenaga kerja dan memberi clearance | JA-08 A.1: "Melakukan legal peninjauan kontrak pelanggan, vendor, tenaga kerja dan kemitraan." JA-08 E.1 dan E.2: "Memberikan legal clearance/rekomendasi", "Meminta revisi klausul berisiko" | Peran Legal & Compliance (JA-08), pengecualian "Mutasi mengubah perjanjian kerja" |
| 10 | Job Analysis dipakai sebagai bukti penetapan peran | Bagian 1: "Dokumen digunakan untuk rekrutmen, orientasi karyawan baru, performance management, competency assessment, dan bukti penetapan peran dalam sistem manajemen mutu." | Alasan pembaruan SNX-HR-JA-01 di 6.4 nomor 8 |
| 11 | Alternatif penetap keputusan lintas departemen: Direktur | JA-02 A.4 dan A.6: "Menyelesaikan hambatan lintas departemen dengan keputusan yang terdokumentasi." "Mengevaluasi kebutuhan sumber daya, efektivitas tim, dan usulan perbaikan proses." | USULAN U2 (tidak dipakai di badan dokumen) |
| 12 | Kriteria baris | "Prosedur pemindahan karyawan ke unit kerja, divisi, atau lokasi operasional lain sesuai kebutuhan organisasi." (config/checklist.json baris 20) | Bagian 3 di bawah |

Fakta dari dokumen lain di repo (bukan dari sumber Drive), dicocokkan ke spec yang sudah DONE:
- HR-JA-01 butir 4.3 (garis pelaporan berlabel menunggu konfirmasi belum resmi), 4.4 (Authority Matrix), 4.5 (keputusan pengangkatan atau pemutusan mengikuti delegasi), 4.7 (masa pengalaman minimum), 4.10 (lokasi kerja utama semua jabatan).
- ISMS-SOP-02: definisi "Mutasi" = "Perpindahan peran seseorang."; langkah "Beri tahu mutasi paling lambat pada hari efektif." (HR atau atasan langsung); "Ajukan perubahan akses karena mutasi." (Atasan langsung); "Cabut akses lama yang tidak relevan paling lambat 5 hari kerja sesudah mutasi." (Administrator sistem); permintaan akses di Service Hub (GLPI).
- HR-ORG-01: kolom Unit dan Melapor ke di Daftar Jabatan; Divisi Operation dengan sub divisi NOC, SOC, serta SD dan PM; butir K-03, K-04, K-05, K-10 (label menunggu konfirmasi dan jabatan tanpa pemegang).
- HR-SOP-10: pembagian usul oleh atasan, rekomendasi HR Manager, keputusan Direktur Utama, dan rumusan pengecualian scope (SOP-11 penurunan, SOP-12 perpindahan tugas atau fungsi, SOP-13 pemindahan ke unit, divisi, atau lokasi).

## 3. Pemetaan kriteria (Description baris 20)

| Unsur kriteria | Di dokumen | Dasar |
|---|---|---|
| Prosedur | Bagian 6 (6.1 sampai 6.4), bagian 7 (diagram), bagian 8 (batas waktu), bagian 9 (pengecualian) | Disusun, seluruhnya USULAN |
| Pemindahan karyawan | Definisi Mutasi dan Karyawan yang dimutasi; scope; 6.1 nomor 1 sampai 3; 6.3 nomor 2; 6.4 nomor 4 | Kriteria baris |
| ke unit kerja | Definisi Unit kerja (kolom Unit di HR-ORG-01); butir 4.2; langkah 6.1 nomor 1 dan 2 | HR-ORG-01 |
| ke divisi | Definisi Divisi (sub divisi Operation: NOC, SOC, serta SD dan PM); kalimat Batas rotasi dan mutasi di bagian 2; butir 4.2; langkah 6.1 nomor 1 dan 2 | HR-ORG-01 (turunan POL-OPS-001 yang berstatus USULAN) |
| ke lokasi operasional lain | Definisi Lokasi operasional (acuan lokasi kerja utama di HR-JA-01 butir 4.10); butir 4.2; langkah 6.1 nomor 1 dan 2; 6.4 nomor 2 sampai 4 | HR-JA-01 butir 4.10 |
| sesuai kebutuhan organisasi | Definisi Kebutuhan organisasi; butir 4.1; 6.1 nomor 2 (usulan memuat kebutuhan organisasi); scope (pemindahan atas permintaan karyawan dan sebagai sanksi disiplin dikecualikan, USULAN) | Kriteria baris |

Klausul ISO (checklist tidak memberi acuan; semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur dan rekaman |
|---|---|---|
| ISO 9001:2015 5.3 (Peran, tanggung jawab, dan wewenang organisasi) | 4.3, 4.5, 4.6, 4.7, 4.10 | Tabel peran bagian 5; 6.3; 6.4 nomor 2 dan 3 |
| ISO 9001:2015 7.1.2 (Orang) | 4.1 | 6.1 |
| ISO 9001:2015 7.2 (Kompetensi) | 4.4 | 6.2 nomor 4 dan 5 |
| ISO 9001:2015 7.5.3 (Pengendalian informasi terdokumentasi) | 4.11 | Tabel rekaman bagian 11 |
| ISO/IEC 27001:2022 Annex A 5.2 (Peran dan tanggung jawab keamanan informasi) | 4.5 | Tabel peran bagian 5 |
| ISO/IEC 27001:2022 Annex A 5.18 (Hak akses) | 4.9 | 6.4 nomor 6 dan 7 |
| ISO/IEC 27001:2022 Annex A 6.5 (Tanggung jawab setelah pemutusan atau perubahan pekerjaan) | 4.9 | 6.4 nomor 6 dan 7 |

Nomor dan nama klausul berasal dari standar, bukan dari sumber tim, dan ditulis dari ingatan penyusun tanpa membuka teks standar (tidak diukur ulang di sesi ini). Sumber Job Analysis hanya menyebut ISO 9001:2015 klausul 5.3, 7.2, 7.3, dan 7.5 dan tidak memuat rujukan ISO/IEC 27001 (audit butir 15).

## 4. Pemetaan nama peran (HR-ORG-01)

| Istilah di sumber | Peran di dokumen | Dasar | Label |
|---|---|---|---|
| HR Lead (JA-14, Process Owner) | HR Manager | config/defaults.json data_conflicts; HR-ORG-01 JA-14 | Tidak diberi label |
| HRGA Officer (JA-12) | HRGA Officer | HR-ORG-01 JA-12 | Tidak diberi label |
| Direktur Utama (JA-01), "Management / Authorized Director" (blok persetujuan) | Direktur Utama | HR-ORG-01 JA-01; sama dengan HR-SOP-10 | Penetap keputusan = USULAN (U2) |
| atasan langsung (kolom tiap jabatan) | Atasan Langsung Asal dan Atasan Langsung Tujuan | HR-ORG-01 mendefinisikan "Atasan langsung" sebagai jabatan tujuan laporan langsung. Mutasi punya dua atasan, sehingga dipecah dengan nama yang didefinisikan di bagian 3 | USULAN (U3) |
| Legal & Compliance (JA-08) | Legal & Compliance (JA-08) | HR-ORG-01 memberi judul sama untuk JA-08 dan JA-09, kode JA-08 membedakan; sama dengan HR-SOP-10 | USULAN (U11) |
| Karyawan | Karyawan yang dimutasi | Istilah sumber; bukan jabatan di Daftar Jabatan | Tidak diberi label |
| atasan langsung bila pengusul dan penanggap satu jabatan | Penanggap alternatif (jabatan tujuan garis lapor dari Atasan Langsung Asal) | Putaran 1: mutasi yang hanya mengubah lokasi operasional membuat Atasan Langsung Tujuan sama dengan Atasan Langsung Asal. Kolom Melapor ke di HR-ORG-01 menunjuk jabatan berikutnya | USULAN (U17) |
| Administrator sistem (di ISMS-SOP-02) | Tidak dijadikan peran di dokumen ini | Pelaku pencabutan akses diatur ISMS-SOP-02; dokumen ini hanya merujuknya (butir 4.9) | Dicatat di sini |

COO tidak disebut di dokumen ini, sehingga aturan sebutan "Direktur (COO)" tidak terpicu. Samuel di badan dokumen = "Direktur Utama"; "President Director" hanya di blok Approved By.

## 5. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" di context/audit/iso-sinux-supdocs-hr-2026-10-14.md (fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1):

| Butir audit | Relevan? | Penanganan |
|---|---|---|
| 1 Status DRAF, nomor "usulan", Effective Date kosong | Ya | Dokumen ini merujuk SNX-HR-JA-01 (nomor SNX hasil W1), bukan HR-JA-001. Status JA-01 tetap Draft, sehingga semua rujukan ke butirnya ikut berstatus belum disahkan. Effective Date dokumen ini kosong |
| 2 Tidak ada KPI, bagan, grade; posisi kosong tidak dicantumkan | Sebagian | Nihil grade berarti tingkat jabatan tidak bisa diukur dari sumber. Dokumen ini memakai ukuran Tingkatan jabatan dari HR-SOP-12 (jumlah garis lapor sampai Direktur Utama, USULAN) untuk membedakan mutasi dari kenaikan dan penurunan jabatan (pengecualian bagian 9 baris 5). Dicatat di open item O1 |
| 3 Kalimat terpotong di Bagian 1 | Tidak | Kalimat itu tidak dikutip. Tidak ada fakta mutasi di dalamnya |
| 4 Frasa kompetensi rusak (mis. "pihak terkait management", "Risk pemahaman karyawan") | Tidak langsung | Dokumen ini tidak mengutip kompetensi. Langkah 6.2 nomor 4 menunjuk persyaratan jabatan di SNX-HR-JA-01, yang sudah memulihkan frasa itu (USULAN di dokumen itu). Kutipan JA-08 A.1 di bagian 2 notes ini memuat "legal peninjauan" apa adanya (frasa rusak dari sumber) dan tidak masuk badan dokumen |
| 5 Pelaporan Manager of Product Tech tidak konsisten | Ya | Ditangani lewat pengecualian bagian 9 baris 4 (jabatan berlabel menunggu konfirmasi di SNX-HR-ORG-01): Direktur Utama menunjuk jabatan pengusul dan penanggap (USULAN) |
| 6 Atasan JA-06 dan JA-07 ditulis "Commercial - Laras Rasmawati" | Ya, tidak langsung | Dokumen ini membaca atasan dari kolom Melapor ke di SNX-HR-ORG-01, yang sudah menormalkan menjadi VP Commercial (JA-03) |
| 7 Atasan JA-08, JA-10, JA-11, JA-14 tidak satu | Ya | Sama dengan butir 5: pengecualian bagian 9 baris 4 |
| 8 Penamaan unit tidak seragam (Operations, Operation, HR / GA, Human Resources, HRGA / General Affairs) | Ya | Definisi Unit kerja memakai kolom Unit di Daftar Jabatan SNX-HR-ORG-01 (satu bentuk per unit), bukan nama unit di sumber |
| 9 Dua jabatan berjudul "Legal & Compliance" | Ya | Peran ditulis "Legal & Compliance (JA-08)" |
| 10 Tidak ada Finance Lead dan Finance Staff | Tidak | Peran itu tidak dipakai di dokumen ini |
| 11 Ejaan Direktur Utama dan sebutan CEO | Ya | Badan dokumen "Direktur Utama" tanpa nama; blok Approved By "Samuel Kristanto Utomo / President Director" menurut config/defaults.json |
| 12 Teks B dan F identik, batas nominal wewenang tidak ada | Ya | Batas nominal tidak ada, sehingga hak tanda tangan dan otorisasi keuangan dirujuk ke Authority Matrix (butir 4.5), tanpa angka |
| 13 Masa pengalaman minimum belum ada | Ya | Butir 4.4: HR Manager menilai pengalaman dari persyaratan pendidikan dan pengalaman jabatan tujuan sampai masa itu ditetapkan (USULAN) |
| 14 Jumlah tabel tidak cocok | Tidak | Tidak berpengaruh |
| 15 Tidak ada rujukan ISO/IEC 27001 | Ya | Annex A 5.2, 5.18, 6.5 ditambahkan di bagian 11 dengan label (USULAN, perlu konfirmasi konsultan) |

## 6. Asumsi

1. Sumber tidak punya proses mutasi, sehingga alur dibangun dari peran dan batas wewenang di Job Analysis ditambah pola HR-SOP-10 agar kenaikan, penurunan, dan mutasi punya pembagian keputusan yang sama.
2. Pengusul = jabatan di tempat tujuan (Atasan Langsung Tujuan), karena kriteria menyebut pemindahan ke unit, divisi, atau lokasi "sesuai kebutuhan organisasi" dan kebutuhan itu paling dekat dengan jabatan yang menerima.
3. Angka batas waktu 3, 3, 5, 5, dan 2 hari kerja mengikuti pola HR-SOP-10 agar satu set SOP HR seragam. Angka itu tidak punya sumber dan berlabel (USULAN). Satu-satunya angka bersumber adalah "paling lambat 5 hari kerja sesudah mutasi" (ISMS-SOP-02), dipakai pada lingkupnya (mutasi) di butir 4.9.
4. "Lokasi operasional lain" dibaca sebagai tempat kerja selain lokasi kerja utama di HR-JA-01 butir 4.10 yang disebut di keputusan mutasi. Daftar lokasi tidak dibuat.
5. "Divisi" dibaca sebagai sub divisi Operation (NOC, SOC, serta SD dan PM), sesuai kalimat Batas rotasi dan mutasi dari orkestrator, karena hanya itu yang bernama divisi di dokumen yang sudah DONE. Susunan itu berstatus USULAN di HR-ORG-01 (butir K-10), sehingga definisi Divisi di dokumen ini berlabel (USULAN).
6. Definisi Tingkatan jabatan (jumlah garis lapor sampai Direktur Utama) disalin dari HR-SOP-12 agar batas kenaikan, penurunan, dan rotasi memakai satu ukuran. Ukuran itu berlabel (USULAN) di kedua dokumen karena HR-JA-01 tidak memuat grading.
7. Satu istilah satu hal (putaran 1): "informasi jabatan baru" (uraian jabatan tujuan, garis lapor baru, lokasi operasional tujuan) didefinisikan sekali di bagian 3 dan dipakai di 4.7, bagian 5, 6.4 nomor 2 dan 3, SLA, dan bagian 9. "Menyimpulkan kualifikasi" dan "kesimpulan kualifikasi" dipakai di semua tempat (4.3, 4.4, bagian 5, 6.2, 6.3, 6.4, SLA, rekaman); kata "menilai" dan "kesimpulan penilaian" tidak dipakai.

## USULAN

Hitungan: 58 kemunculan "(USULAN)" menurut lint (satu butir bisa muncul di beberapa bagian), dikelompokkan menjadi 22 butir keputusan di bawah.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Seluruh prosedur 6.1 sampai 6.4, diagram, dan pembagian langkah per peran | Bagian 6, 7, intro 6.1 | Aziz (pemilik proses), lalu Samuel mengesahkan |
| U2 | Direktur Utama menetapkan keputusan mutasi dan HR Manager hanya merekomendasikan. Alternatif: Direktur (JA-02) untuk mutasi lintas departemen (fakta pendukung 11) | 4.3, 4.6, peran Direktur Utama, 6.3 | Samuel |
| U3 | Atasan Langsung Tujuan sebagai pengusul dan Atasan Langsung Asal sebagai penanggap, termasuk istilah dan definisinya (label ditambah di putaran 1) | Bagian 3 (Atasan Langsung Asal, Atasan Langsung Tujuan, Usulan mutasi), 4.1, 4.2, 4.3, 5, 6.1, 6.2 | Aziz |
| U4 | Pengecualian scope: pemindahan atas permintaan karyawan dan sebagai sanksi disiplin | Bagian 2 | Aziz |
| U5 | Pengecualian scope: gaji, tunjangan, dan biaya yang timbul karena mutasi | Bagian 2 | FAT (pemutus biaya), Aziz (gaji dan tunjangan) |
| U6 | Pengecualian scope: mutasi Direktur Utama (JA-01) | Bagian 2 | Samuel |
| U7 | Batas waktu SLA dan hari kerja tanpa hari libur resmi | Bagian 3 (Hari kerja), bagian 8 | Aziz |
| U8 | Wewenang jabatan asal berakhir pada tanggal berlaku | 4.5 | Samuel, Aziz |
| U9 | Konfirmasi tertulis karyawan atas informasi jabatan baru | 4.7, 6.4 nomor 3, peran Karyawan yang dimutasi | Aziz |
| U10 | Penunjukan pengganti dan catatan serah terima pekerjaan | 4.8, 6.2 nomor 3, 6.4 nomor 1, bagian 11 | Aziz |
| U11 | Peninjauan Legal & Compliance (JA-08) atas perubahan perjanjian kerja | Peran Legal & Compliance, bagian 9 baris 7 | Legal |
| U12 | Penanganan pengecualian: jabatan atasan berlabel menunggu konfirmasi atau tanpa pemegang, jabatan tujuan belum tercantum, pengalihan ke SOP-10 atau SOP-11, keberatan Atasan Langsung Asal, keputusan dengan syarat, keberatan karyawan, penundaan tanggal berlaku | Bagian 9 | Samuel, Aziz |
| U13 | Penilaian pengalaman jabatan tujuan sampai masa pengalaman minimum ditetapkan | 4.4 | Aziz |
| U14 | Atasan Langsung Tujuan yang mengajukan perubahan hak akses (ISMS-SOP-02 hanya menulis "Atasan langsung"), dengan batas 1 hari kerja sesudah pemberitahuan mutasi diterima. Alasan angka: ISMS-SOP-02 memberi 5 hari kerja untuk pencabutan akses lama, sehingga pengajuan harus terjadi dini. Angka 1 tidak punya sumber | Butir 4.9, 6.4 nomor 7, SLA baris 8 | Fani (pemilik akses sistem Operation), lalu owner bila lintas unit |
| U15 | Klasifikasi RESTRICTED (Internal) dan lokasi, pemilik, retensi rekaman (personal file di folder Google Drive Departemen HR, selama karyawan bekerja) | 4.11, bagian 11 | Aziz (lokasi dan retensi), owner (klasifikasi) |
| U17 | Penanggap alternatif (jabatan tujuan garis lapor dari Atasan Langsung Asal) menanggapi usulan bila Atasan Langsung Tujuan dan Atasan Langsung Asal satu jabatan, mis. mutasi lokasi saja | Bagian 3, 4.3, 5, intro 6.2, bagian 9 baris 3 | Aziz |
| U18 | Tingkatan jabatan diukur dari jumlah garis lapor sampai Direktur Utama (sama dengan HR-SOP-12), dan pengalihan ke HR-SOP-10 atau HR-SOP-11 menurut ukuran itu | Bagian 3, bagian 9 baris 5 | Aziz, owner |
| U19 | Sub divisi Operation (NOC, SOC, SD dan PM) sebagai pengertian Divisi | Bagian 3 (Divisi), bagian 2 (Batas rotasi dan mutasi) | Owner (menunggu K-10 di HR-ORG-01) |
| U20 | Kalimat Batas rotasi dan mutasi (rotasi = sementara, penyegaran atau pengembangan keterampilan, dalam unit kerja dan tingkatan jabatan yang sama, kembali ke tugas semula; mutasi = menetap, karena kebutuhan organisasi). Kalimat sama di HR-SOP-12 | Bagian 2 | Aziz, owner |
| U21 | Perpindahan sementara di luar batas rotasi (mis. sementara ke unit atau lokasi lain) dikecualikan dari SOP ini dan belum diatur SOP mana pun | Bagian 2 (pengecualian) | Aziz |
| U22 | Bila Atasan Langsung Tujuan sama dengan Atasan Langsung Asal dan jabatan itu Direktur Utama, Direktur Utama menanggapi sendiri usulan (tidak ada jabatan di atasnya di HR-ORG-01) | Bagian 9 baris 3 | Samuel |
| U16 | Klausul ISO 9001:2015 dan ISO/IEC 27001:2022 di bagian 11 | Bagian 11 (label "(USULAN, perlu konfirmasi konsultan)") | Owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| O1 | Batas rotasi dan mutasi sudah memakai kalimat yang sama dengan HR-SOP-12 (bagian 2, sweep). Dua selisih tersisa untuk orkestrator di HR-SOP-12: (a) definisi Unit kerja HR-SOP-12 menaruh NOC, SOC, serta SD dan PM dalam satu unit Operation (USULAN); sesuai kalimat batas, pindah menetap antar sub divisi adalah mutasi dan pindah sementara yang kembali ke tugas semula adalah rotasi, sehingga kalimat itu perlu dihapus atau disesuaikan di HR-SOP-12; (b) HR-SOP-11 mengukur penurunan dengan tingkat posisi (grading, belum ditetapkan), sedangkan dokumen ini mengalihkan penurunan lewat tingkatan jabatan HR-SOP-12. Penulisan "Atasan Langsung Asal" dan "Atasan Langsung Tujuan" dengan huruf kapital di HR-SOP-12 diminta orkestrator dan tidak diubah di sini Diubah W9: definisi Unit kerja kini sama dengan HR-SOP-12 (NOC, SOC, serta SD dan PM dalam satu unit Operation, USULAN); kalimat batas tetap identik. Selisih (a) tentang pindah antar sub divisi tetap mengikuti kalimat batas dan perlu diputus LEAD. | Aziz (lewat orkestrator) |
| O2 | Daftar lokasi operasional SINUX selain lokasi kerja utama tidak ada di sumber. Dokumen tidak membuatnya | Aziz, owner |
| O3 | Mutasi atas permintaan karyawan dan sebagai sanksi disiplin dikecualikan (U4). Perlu keputusan apakah keduanya butuh SOP sendiri | Aziz |
| O4 | Peraturan Perusahaan lengkap tidak dibaca. Bila memuat ketentuan mutasi, tempat kerja, atau persetujuan karyawan, ketentuan itu harus didahulukan dari butir 4.1 sampai 4.7 | Aziz, Legal |
| O5 | Pengembalian dan pemindahan aset kerja saat pindah lokasi tidak diatur. SNX-ISMS-SOP-04 hanya mengatur pengembalian aset saat pemberhentian | Fani |
| O6 | Mutasi mendesak (butuh pindah sebelum keputusan selesai) tidak diatur | Aziz, Samuel |
| O7 | Butir K-03, K-04, K-05, dan K-10 di SNX-HR-ORG-01 (atasan berlabel menunggu konfirmasi, jabatan Divisi Operation tanpa pemegang) menentukan siapa Atasan Langsung Tujuan dan Asal untuk jabatan itu. Sampai terjawab, bagian 9 baris 4 berlaku | Owner |
| O8 | Nama jabatan di dokumen ini mengikuti HR-ORG-01 (HR Manager). Sumber menulis HR Lead. Konfirmasi Aziz atau owner (data_conflicts) Ditutup W9: owner 15 Okt memutus jabatan Aziz = HR Lead; dokumen memakai HR Lead. | Aziz, owner |
| O10 | Pengajuan perubahan hak akses dan pencabutan akses lama: SNX-ISMS-SOP-02 tidak membedakan atasan asal dan tujuan. Dokumen ini menunjuk Atasan Langsung Tujuan dan batas 1 hari kerja (U14); pemilik ISMS-SOP-02 perlu mengonfirmasi | Fani |
| O11 | Penanggap alternatif (U17) hanya dirumuskan untuk kasus pengusul sama dengan penanggap. Bila Atasan Langsung Asal berlabel menunggu konfirmasi atau tanpa pemegang, berlaku bagian 9 baris 4 Diubah W9: kasus Direktur Utama sebagai Atasan Langsung Tujuan dan Asal ditangani lewat pengecualian di butir 4.3 (USULAN). | Aziz |
| O12 | Perpindahan sementara ke unit, sub divisi, atau lokasi lain yang tidak termasuk rotasi (U21) tidak diatur HR-SOP-12 maupun dokumen ini. Perlu keputusan apakah butuh SOP atau butir sendiri | Aziz |
| O9 | modifiedTime sumber dikutip dari prompt tugas dan tidak diukur ulang di sesi ini | Orkestrator |

## 7. Jawaban dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI?
- Setiap butir bagian 4 dibuka dengan pola yang sama: judul, kurung klausul, titik dua. Pola ini dipertahankan karena memetakan butir ke klausul untuk auditor, sama dengan HR-SOP-10 dan HR-SOP-08. Butir 4.8 memang tanpa klausul karena saya tidak yakin nomor klausulnya.
- Rumus kalimat "X mengusulkan, Y menanggapi, Z menetapkan" di 4.3 dan penunjuk "(butir 6.x)" di hampir tiap kalimat terdengar mekanis. Penunjuk dipertahankan karena aturan "satu fakta disebut sekali, bagian lain merujuk nomor butir".
- Kalimat pasif padahal pelakunya diketahui: tujuan butir 3 ("diajukan"), butir 4.9 ("dicabut", "diajukan"), 4.1 ("mutasi dilakukan"), 6.4 nomor 6 ("agar perubahan hak akses diajukan"), dan bagian 9 baris 2 ("usulan diproses"). Semua sudah menyebut pelaku: Atasan Langsung Tujuan, HRGA Officer, atau SNX-ISMS-SOP-02 sebagai pengatur pencabutan dengan batas 5 hari kerja.
- Pengulangan isi: daftar uraian jabatan, garis lapor, dan lokasi muncul di enam tempat. Kini didefinisikan sekali sebagai "informasi jabatan baru" di bagian 3, dan bagian lain menyebut istilahnya. Butir 4.3 tidak lagi mengulang tabel peran, hanya menunjuk bagian 5.
- Pemicu peninjauan di bagian 10 ("perubahan secara signifikan") diganti dua pemicu yang bisa dicek: Direktur Utama mengubah penetap keputusan di butir 4.6, atau revisi SNX-HR-ORG-01 menambah atau menghapus unit kerja atau divisi.
- Tiga kata benda berjejer yang bukan daftar asli: tidak ada. Daftar "unit kerja, divisi, atau lokasi operasional" dan "setujui, setujui dengan syarat, atau tolak" berasal dari kriteria dan dari tiga hasil keputusan yang nyata.
- Tidak ada pembuka generik, penutup positif, huruf tebal, kapital, atau tanda kutip untuk penekanan di badan dokumen. Lint dan pemeriksaan skrip tidak menemukan frasa terlarang.

Adakah fakta, angka, nama, atau tanggal tanpa sumber?
- Angka 3, 3, 5, 5, dan 2 hari kerja, serta 1 hari kerja untuk pengajuan hak akses: tanpa sumber, berlabel (USULAN) di tabel SLA. Angka 5 hari kerja di butir 4.9 dan di baris SLA pengajuan akses: bersumber ISMS-SOP-02, dipakai pada lingkup mutasi.
- Klausul ISO: dari pengetahuan standar, bukan dari sumber, satu label (USULAN, perlu konfirmasi konsultan). Annex A 6.5 dan ISO 9001 7.1.2 tidak muncul di sumber sama sekali.
- Nama orang di badan dokumen: nihil. Nama hanya di blok Prepared, Reviewed, dan Approved dari config/defaults.json.
- Tanggal: nihil. Effective Date kosong.
- Sistem: Service Hub (GLPI) dari ISMS-SOP-02; Google Drive (folder Departemen HR) berlabel USULAN. Sistem HR atau HRIS tidak disebut karena sumber hanya menyebut kompetensi "HRIS", bukan sistem yang dipakai.
- Lokasi kerja utama: dirujuk ke HR-JA-01 butir 4.10 tanpa menyalin alamatnya; alamat itu berasal dari Peraturan Perusahaan lewat HR-JA-01 dan tidak diukur ulang di sini.
- Pemisahan peran, wewenang jabatan asal berakhir, konfirmasi karyawan, serah terima pekerjaan, dan pengecualian bagian 9: rancangan penyusun, semua berlabel (USULAN) per butir atau lewat intro 6.1.

## Sweep

Putaran sweep (penghalusan sesudah DONE), instruksi /tmp/claude-0/prompts/HR-SOP-13.sweep.txt. Tiga butir diubah di specs/HR-SOP-13.json. Berkas lain tidak disentuh.

| Butir | Sebelum | Sesudah |
|---|---|---|
| 1. Atasan Langsung Asal sama dengan Tujuan (mutasi lokasi saja), aturan pengganti di 4.3 | Aturan sudah masuk di putaran 1: butir 4.3 menunjuk Penanggap alternatif, bagian 9 baris 3, definisi, dan tabel peran. Kasus Direktur Utama sebagai Atasan Langsung Tujuan belum ditangani | Bagian 9 baris 3 ditambah: "Bila jabatan itu Direktur Utama, Direktur Utama menanggapi sendiri usulan itu (USULAN)" (U22). Butir 4.3 dan baris lain tidak berubah |
| 2. Definisi Divisi dan rotasi bertabrakan dengan HR-SOP-12 | Divisi: "Divisi Operation beserta sub divisinya, yaitu NOC, SOC, serta SD dan PM. Susunan ini mengikuti SNX-HR-ORG-01, yang menandainya (USULAN)." Pengecualian rotasi: "perpindahan tugas atau fungsi pada unit kerja, divisi, lokasi operasional, dan tingkatan jabatan yang sama (SNX-HR-SOP-12)". Definisi Mutasi: "Pemindahan karyawan ke ..." | Divisi: "Sub divisi Operation, yaitu NOC, SOC, serta SD dan PM. SNX-HR-ORG-01 menyatakan susunan ini berstatus (USULAN)." Pengecualian rotasi: "rotasi menurut batas di bawah (SNX-HR-SOP-12); perpindahan sementara di luar batas rotasi (USULAN)". Mutasi: "Pemindahan menetap karyawan ke ...". Tujuan dan scope paragraf 1 memakai "secara menetap". Dokumen terkait SNX-HR-SOP-12: "perpindahan sementara dalam unit kerja dan tingkatan jabatan yang sama, dengan karyawan kembali ke tugas semula" |
| 3. Kalimat batas rotasi dan mutasi yang seragam | Tidak ada kalimat batas; rumusan batas berbeda dari HR-SOP-12 | Bagian 2 paragraf 3 memuat kalimat dari orkestrator verbatim: "Batas rotasi dan mutasi: perpindahan sementara untuk penyegaran atau pengembangan keterampilan, dalam unit kerja dan tingkatan jabatan yang sama, dengan karyawan kembali ke tugas semula sesudah masa rotasi, adalah rotasi (SNX-HR-SOP-12). Perpindahan menetap karena kebutuhan organisasi ke unit kerja, sub divisi Operation (NOC, SOC, serta SD dan PM), atau lokasi operasional lain adalah mutasi (SNX-HR-SOP-13) (USULAN)." Nama peran sudah berkapital di dokumen ini; penetap keputusan tetap Direktur Utama |

Catatan: pindah antar sub divisi NOC ke SOC kini terbaca satu arah menurut kalimat batas: menetap adalah mutasi, sementara dan kembali ke tugas semula adalah rotasi. Temuan pemeriksa lain yang tidak masuk daftar sweep (kalimat "ukuran ini (USULAN)" tanpa predikat, sinonim "setelah" dan "sesudah", retensi rekaman, empat baris rekaman identik) tidak diubah dan tetap terbuka untuk orkestrator.

## ISO-W9

Sumber: LEAD G-3 (A2, A3, B2, B4) dan butir kerja ISO-W9. Hanya butir di bawah yang diubah.

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 jabatan Aziz | "HR Manager" (31 kemunculan: Peran, PIC, SLA, rekaman, simpul diagram, process_owner, blok Reviewed) | "HR Lead"; blok Reviewed "Aziz Priyo Widakdo / HR Lead" |
| B2 butir 4.3 vs bagian 9 | 4.3: peran mengusulkan, menanggapi, menetapkan keputusan berbeda satu sama lain, tanpa pengecualian. Bagian 9 baris 3: "Bila jabatan itu Direktur Utama, Direktur Utama menanggapi sendiri usulan itu (USULAN)." | 4.3 ditambah: "Pengecualian: bila Direktur Utama adalah Atasan Langsung Tujuan, Direktur Utama mengusulkan sekaligus memutuskan, dan bila ia juga Atasan Langsung Asal, ia menanggapi sendiri. Pemeriksa yang terpisah dari Direktur Utama adalah HR Lead, lewat kesimpulan kualifikasi dan rekomendasi di butir 6.2 dan 6.3 (USULAN)." Bagian 9 baris 3 merujuk pengecualian itu: "Bila jabatan yang sama itu Direktur Utama, Direktur Utama menanggapi sendiri usulan itu sesuai pengecualian di butir 4.3 (USULAN)." |
| B2 label bagian 9 baris 3 | label (USULAN) hanya di kalimat kedua | label (USULAN) di kedua kalimat |
| B2 label bagian 9 baris 2 | "HR Lead menambahkan jabatan itu lewat revisi kedua dokumen." tanpa label | "... lewat revisi kedua dokumen (USULAN)." |
| B2 label bagian 9 baris 8 | "HR Lead mencatat tindakan pemenuhan syarat dan melapor ke Direktur Utama saat syarat terpenuhi." tanpa label | "... saat syarat terpenuhi (USULAN)." |
| B2 NOC, SOC (bagian 3, Unit kerja) | "Unit yang tercantum di kolom Unit pada Daftar Jabatan SNX-HR-ORG-01." | "Nama di kolom Unit pada SNX-HR-ORG-01, misalnya Commercial, Operation, atau Legal. Sub divisi NOC, SOC, serta SD dan PM berada dalam satu unit Operation (USULAN)." (sama dengan SNX-HR-SOP-12) |

Alasan B2: butir 4.3 yang keliru, bukan bagian 9. Direktur Utama memang dapat menjadi Atasan Langsung Tujuan dan Asal sekaligus penetap keputusan (4.6), jadi aturan "berbeda satu sama lain" tanpa pengecualian tidak bisa dipenuhi. Menghapus kalimat bagian 9 tidak menyelesaikan kasus itu. Pengecualian ditulis di 4.3, dengan kontrol pengganti yang sudah ada di dokumen (kesimpulan kualifikasi dan rekomendasi HR Lead di 6.2 dan 6.3, bukan kontrol baru). Seluruhnya berlabel (USULAN); pemutus Samuel, Aziz.

Definisi Divisi dan kalimat batas rotasi dan mutasi tidak diubah (kalimat batas identik di SOP-10, 11, 12, 13; penetap keputusan tetap Direktur Utama).

A3 garis lapor JA-03 dan JA-04: dokumen ini tidak menyebut atasan atau garis lapor JA-03 atau JA-04 dan tidak memakai keduanya sebagai contoh ukuran tingkatan jabatan, jadi tidak ada perubahan. Label K-02, K-03, K-04 tidak disentuh. SPV tidak ditambahkan: dokumen tidak punya kolom tingkat jabatan.

Open item: O8 ditutup W9; O1 dan O11 diubah W9. Tambahan open item W9: pengecualian Direktur Utama di butir 4.3 dan kontrol penggantinya (USULAN), pemutus Samuel dan Aziz.
