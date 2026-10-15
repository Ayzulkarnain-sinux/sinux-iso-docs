# Catatan penyusun HR-SOP-08: Company Leaves

Status: DRAFTED (spec + notes ada). Spec: specs/HR-SOP-08.json. Mode sop, aksi T1, wave W3, nomor SNX-HR-SOP-08 (nomor lama dipertahankan), department "Human Resources", classification "INTERNAL" (worklist), audit_class C2. Approval persis dari config/defaults.json: prepared "Sita Nadia Salsabila Widodo / HRGA Officer", reviewed "Aziz Priyo Widakdo / HR Manager", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "HR Manager" (jabatan tanpa nama): sumber tidak punya baris "Pemilik dokumen" (audit: owner_in_doc "tidak dicantumkan"), sehingga dipakai aturan config/defaults.json process_owner, yaitu jabatan reviewer departemen.

Hasil uji terakhir (bukti mentah: /tmp/pen-HR-SOP-08/lint.out.txt dan /tmp/pen-HR-SOP-08/validate.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-SOP-08.json /tmp/pen-HR-SOP-08/HR-SOP-08.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-SOP-08/HR-SOP-08.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "18 butir (USULAN) menunggu ACC" (sesudah Sweep; sebelumnya 13). Warn PIC SLA nol.
- Validator OOXML (`python3 /mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!". `python3 -I reports/orch/blankscan.py /tmp/pen-HR-SOP-08/HR-SOP-08.docx`: "ok 18" (bukti: /tmp/pen-HR-SOP-08/blankscan.out.txt).
- soffice ke PDF: 18 halaman. Diagram /tmp/pen-HR-SOP-08/HR-SOP-08_flow.png dibuka (sesudah Sweep): sebelas simpul, rankdir TB, empat lajur peran, label Ya dan Tidak terbaca (satu simpul "Cuti tidak diambil" saya keluarkan dari lajur Karyawan karena label cabang bertumpuk).
- Pemeriksaan tambahan atas spec (skrip python3 -I, di scratchpad sesi, bukan di repo): nol em-dash dan en-dash; 28 langkah, terpanjang 18 kata; semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5 (lima peran: Karyawan, Atasan langsung, HRGA Officer, HR Manager, Direktur Utama); semua kode SNX yang dirujuk di badan (SNX-HR-ORG-01, SNX-ISMS-PRO-01) ada di tabel Dokumen terkait; nol temuan untuk frasa terlarang prompt (pada intinya, yang terpenting, secara fundamental, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, tanpa terkecuali, tanpa kompromi, hulu ke hilir), nol "komersil", nol "diagnosa", nol "Pengusaha", nol "Lead"; "Pimpinan Perusahaan" hanya muncul di tabel Definisi.
- tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel). Berkas tools, template, config, control, reference tidak diubah. Berkas yang ditulis hanya specs/HR-SOP-08.json dan notes/HR-SOP-08.md; hasil render hanya di /tmp/pen-HR-SOP-08/.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| PP - Cuti.docx (30617 byte) | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z | 2026-10-13T11:34:27.275Z (get_file_metadata hari ini, sama dengan prompt; fileSize 30617 sama dengan "bytes" di salinan audit) | read_file_content (teks penuh BAB VI, Pasal 22 sampai 34). download_file_content dipanggil, tetapi hasilnya datang inline sebagai base64 dan tidak tersimpan ke berkas, sehingga docx tidak saya dekode. Penomoran ayat dan butir huruf saya ambil dari salinan audit bagian 2 (dipulihkan dari numbering.xml) dan saya cocokkan dengan urutan teks read_file_content dan rujukan internal sumber (Pasal 22 ayat (4) menunjuk ayat (3); Pasal 33 ayat (2) menunjuk ayat (1); Pasal 24 ayat (3) menunjuk Pasal 33). Penomoran tidak saya ukur ulang dari biner |
| Kriteria penerimaan | config/checklist.json baris 16 | tidak berlaku | Description: "Aturan dan alur pengajuan berbagai jenis cuti (cuti tahunan, sakit, melahirkan, dll.) bagi karyawan." Kolom iso_9001 dan iso_27001 kosong |
| Catatan cacat | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian "hr/HR-PP-Cuti.md" (frontmatter baris 1259, bagian 5 butir 1 sampai 18) dan sintesis baris 79 | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Daftar Jabatan (JA-01 Direktur Utama, JA-12 HRGA Officer, JA-14 HR Manager) dan tabel Definisi |

Kalimat perintah di sumber yang ditujukan ke penyusun atau agen: tidak ada. Kalimat bernada perintah di sumber (mis. Pasal 31 ayat (5): "karyawan harus menuruti perintah dari Perusahaan") adalah aturan untuk karyawan dan di luar scope dokumen ini.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Semua jenis cuti diajukan lewat sistem HR dengan persetujuan atasan langsung, paling lambat 7 hari kerja sebelumnya | Pasal 32 ayat (1): "Prosedur pengambilan semua jenis cuti baik cuti tahunan maupun izin cuti kerja dengan dibayar, dilakukan atas persetujuan atasan langsung serta dengan mengajukan permohonan melalui sistem HR yang digunakan oleh Perusahaan;" dan ayat (2): "Permohonan cuti diajukan selambat-lambatnya tujuh 7 (tujuh) hari kerja sebelumnya dan/atau apabila dalam kondisi tertentu akan menyesuaikan dengan ketentuan dan keputusan dari atasan langsung dan Pimpinan Perusahaan;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |
| 2 | Cuti tahunan 12 hari per tahun, 14 hari kerja bila masa kerja di atas 3 tahun | Pasal 23 ayat (2) huruf a: "Karyawan berhak mendapatkan cuti tahunan sebanyak 12 (dua belas) hari selama satu tahun;" dan huruf h: "Karyawan dengan masa kerja diatas 3 (tiga) tahun berhak cuti selama 14 (empat belas) hari kerja;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |
| 3 | Sakit wajib diberitahukan ke atasan dan HR paling lambat pukul 10:00 WIB hari yang sama | Pasal 24 ayat (1): "Karyawan yang tidak dapat bekerja karena sakit atau dalam kondisi tidak sehat yang bukan disebabkan oleh kecelakaan kerja diharuskan untuk memberitahu atasannya dan HR selambat-lambatnya pukul 10:00 WIB di hari yang sama;" | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z |

## 2. Fakta pendukung dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Posisi di SOP |
|---|---|---|---|
| 1 | Cuti tahunan mulai setelah masa percobaan dan/atau 3 bulan; prorata | Pasal 23 ayat (2) huruf b: "Hak cuti diberikan setelah selesai masa percobaan dan/atau telah memiliki masa kerja minimal selama 3 (tiga) bulan;" huruf c: "...maka karyawan berhak mendapatkan jatah cuti tahunan penuh berdasarkan perhitungan (prorata);" | 4.3 |
| 2 | 12 hari tiap Januari sejak tahun kedua | Huruf d: "Sejak tahun kedua dan seterusnya, karyawan akan mendapatkan 12 (dua belas) cuti tahunan di bulan Januari;" | 4.2 |
| 3 | Cuti ulang tahun | Huruf e: "Karyawan berhak mengambil cuti ulang tahun sebanyak 1 (satu) hari kerja yang dapat digunakan pada bulan yang bersangkutan;" | 4.4 |
| 4 | Sisa cuti, batas 6 hari dan 30 Juni | Huruf f: "...dapat dibawa dengan cuti tahun berikutnya maksimal sebanyak 6 (enam) hari;" huruf g: "Sisa cuti yang belum digunakan pada tahun sebelumnya dapat dimanfaatkan pada tahun berjalan dan berlaku hingga 30 Juni tahun tersebut;" | 4.5 |
| 5 | Cuti mendesak | Huruf j: "Apabila karyawan sedang dalam kondisi mendesak atau darurat, dapat secara langsung mengajukan cuti dengan syarat telah memberitahukan dan mendapatkan persetujuan dari atasan langsung serta pekerjaan yang menjadi tanggung jawab karyawan yang bersangkutan dapat didelegasikan kepada tim atau karyawan lain nya untuk sementara waktu;" | 4.9, 6.2 |
| 6 | Pemanggilan kembali | Huruf l: "...karyawan dapat dipanggil kembali bekerja serta wajib memenuhi panggilan tersebut. Dalam kondisi kepentingan Perusahaan tersebut, cuti yang telah diambil oleh karyawan dapat dibatalkan atau dikembalikan." | 4.11, 6.7 |
| 7 | Penundaan cuti oleh Pimpinan Perusahaan | Pasal 32 ayat (3) dan (4): "Untuk kepentingan Perusahaan, Pimpinan Perusahaan dapat menunda waktu cuti karyawan;" "Dalam hal ini, kepada karyawan yang bersangkutan dapat diberikan kompensasi berupa cuti yang lamanya ditentukan dan sesuai persetujuan Pimpinan Perusahaan;" | 4.10, 6.7 |
| 8 | Penanggung jawab pengganti | Pasal 32 ayat (5): "Karyawan yang mengajukan cuti, wajib untuk menunjuk minimal 2 (dua) orang penanggung jawab pengganti atas pekerjaan yang sedang dijalankan." | 4.8, 6.1 |
| 9 | Surat dokter untuk sakit lebih dari 1 hari; tanpa surat dianggap alfa | Pasal 24 ayat (2): "Tanpa surat keterangan sakit dari dokter yang sah, maka absen sakit tersebut dianggap sebagai alfa dan akan diberlakukan potong gaji." | 4.14, 6.3 |
| 10 | Sakit berkepanjangan dan tahap upah | Pasal 33 ayat (2) huruf a sampai d: "untuk 4 (empat) bulan pertama, dibayar 100% (seratus perseratus) dari upah;" "...bulan kedua, dibayar 75%...;" "...bulan ketiga, dibayar 50%...;" "untuk bulan selanjutnya dibayar 25% (dua puluh lima perseratus) dari upah sebelum pemutusan hubungan kerja dilakukan oleh Perusahaan." | 4.15, 4.16, 6.4 |
| 11 | Cuti haid hari pertama dan kedua | Pasal 25 ayat (1): "...wajib memberitahukan kepada Perusahaan dan tidak diwajibkan bekerja pada hari pertama serta kedua waktu haid dengan tetap mendapatkan upah penuh;" | 4.17, 6.5 |
| 12 | Cuti melahirkan | Pasal 26 ayat (1): "Karyawan perempuan berhak memperoleh cuti melahirkan paling singkat selama 3 (tiga) bulan dan dapat memperoleh tambahan paling lama 3 (tiga) bulan berikutnya apabila terdapat kondisi khusus sebagaimana ditentukan berdasarkan peraturan perundang-undangan dan dibuktikan dengan surat keterangan dokter;" | 4.18 |
| 13 | Pendampingan istri, dua tempat untuk peristiwa yang sama | Pasal 26 ayat (6): "...berhak mendapatkan cuti tambahan sebanyak 2 (dua) hari di luar cuti tahunan..." dan Pasal 27 huruf e: "Istri melahirkan atau keguguran kandungan, diberikan izin selama 2 (dua) hari;" | 4.21, 4.25 huruf e |
| 14 | Kelahiran bayi dan tanggungan | Pasal 26 ayat (4): "...wajib memberitahukan kelahiran atas bayi nya kepada Perusahaan atau HR untuk didaftarkan dan dilakukan pengkinian tanggungan karyawan;" | 4.22, 6.6 |
| 15 | Cuti khusus (sembilan alasan) | Pasal 27: "Karyawan menikah, diberikan izin selama 3 (tiga) hari;" ... "Mendapat musibah (kebakaran, kebanjiran, atau hal - hal lain) yang lamanya akan ditetapkan berdasarkan pertimbangan Perusahaan;" | 4.25 |
| 16 | Haji, batas 40 hari dan 10 minggu | Pasal 28 ayat (5): "...jangka waktu maksimal cuti yang diambil tidak boleh lebih dari 40 (empat puluh) hari atau jangka waktu yang berlaku yang diperlukan untuk menunaikan ibadah Haji." ayat (6): "...selambat-lambatnya 10 (sepuluh) minggu sebelum tanggal keberangkatan;" | 4.28, 4.29 |
| 17 | Cuti tanpa dibayar | Pasal 30: "...berdasarkan pada perjanjian atau kesepakatan dan persetujuan dari atasan langsung maupun Perusahaan." | 4.31 |
| 18 | WFH bukan cuti (dasar pengecualian scope) | Pasal 31 ayat (1): "Bekerja dari Rumah dapat diberikan untuk karyawan yang memiliki halangan untuk berangkat ke kantor, tapi bukan karena sakit maupun cuti;" | Scope |
| 19 | Penggantian cuti untuk kerja di hari libur resmi | Pasal 22 ayat (4): "...wajib membayar upah kerja lembur atau memberikan penggantian cuti di hari lain sesuai dengan peraturan yang telah ditetapkan oleh Perusahaan" | 4.32 |
| 20 | Sanksi alfa | Pasal 34 ayat (2) huruf a: "5 hari tidak masuk kerja berturut-turut akan dikenakan Sanksi berupa Surat Peringatan Ketiga dan/atau pemotongan cuti dan/atau pemotongan gaji selama jumlah hari yang ditinggalkan" | 4.34 |
| 21 | Kriteria baris | "Aturan dan alur pengajuan berbagai jenis cuti (cuti tahunan, sakit, melahirkan, dll.) bagi karyawan." (config/checklist.json baris 16) | Bagian 3 di bawah |

## 3. Pemetaan kriteria (Description baris 16)

| Unsur kriteria | Di dokumen | Sumber |
|---|---|---|
| aturan (verbatim PP BAB VI) | Bagian 4, butir 4.1 sampai 4.35 | Pasal 22 ayat (4), Pasal 23 sampai 28, 30, 32 sampai 34 |
| alur pengajuan (disusun) | Bagian 6 (6.1 sampai 6.7), bagian 7 (diagram), bagian 8 (tenggat) | Pasal 23 ayat (2) huruf i, j, l; Pasal 24; Pasal 26; Pasal 32; urutan langkah disusun penyusun |
| cuti tahunan | 4.2 sampai 4.8; 6.1 | Pasal 23, 32 |
| sakit | 4.12 sampai 4.16; 6.3 dan 6.4 | Pasal 23 ayat (2) huruf k, Pasal 24, 33 |
| melahirkan | 4.18 sampai 4.24; 6.6 | Pasal 26 |
| dll. | Haid 4.17 dan 6.5; khusus 4.25; ibadah 4.26 sampai 4.30; tanpa dibayar 4.31; mendesak 4.9 dan 6.2; penundaan dan pemanggilan 4.10, 4.11, dan 6.7; penggantian cuti 4.32 | Pasal 22, 23, 25, 27, 28, 30, 32 |
| bagi karyawan | Scope: seluruh karyawan SINUX, termasuk calon karyawan tetap dalam masa percobaan | Pasal 23 ayat (2) huruf b, Pasal 34 ayat (2) huruf b |

Klausul ISO (checklist tidak memberi acuan; semua satu label "(USULAN, perlu konfirmasi konsultan)" di bagian 11, baris "Status acuan klausul"):

| Klausul | Tercermin di bagian 4 | Prosedur dan rekaman |
|---|---|---|
| ISO 9001:2015 5.3 (Peran, tanggung jawab, dan wewenang organisasi) | 4.36 | Tabel peran bagian 5 |
| ISO 9001:2015 7.5.3 (Pengendalian informasi terdokumentasi) | 4.37 | Tabel rekaman bagian 11 |
| ISO 9001:2015 8.1 (Perencanaan dan pengendalian operasional) | 4.6 | 6.1 sampai 6.7; bagian 8 |
| ISO/IEC 27001:2022 Annex A 6.2 (Syarat dan ketentuan kerja) | 4.1 | Bagian 4 secara keseluruhan |
| ISO/IEC 27001:2022 Annex A 5.33 (Perlindungan rekaman) | 4.37 | Tabel rekaman bagian 11 |
| ISO/IEC 27001:2022 Annex A 5.34 (Privasi dan perlindungan PII) | 4.37 | Klasifikasi RESTRICTED (Internal) untuk surat dokter dan HPL |

Nomor dan nama klausul berasal dari standar, bukan dari dokumen tim, dan ditulis dari ingatan penyusun tanpa membuka teks standar (tidak diukur ulang di sesi ini).

## 4. Pemetaan nama peran (HR-ORG-01)

| Istilah di sumber | Peran di dokumen | Dasar | Label |
|---|---|---|---|
| Karyawan | Karyawan | Istilah sumber; bukan jabatan di Daftar Jabatan HR-ORG-01 | Tidak diberi label |
| atasan, atasan langsung | Atasan langsung | Istilah sumber; HR-ORG-01 mendefinisikan "Atasan langsung" sebagai jabatan tujuan laporan langsung | Tidak diberi label |
| HR | HRGA Officer (JA-12) | HR-ORG-01 mendefinisikan HRGA sebagai fungsi administrasi kepegawaian; JA-12 adalah pemegangnya di bawah HR Manager | USULAN (definisi bagian 3) |
| Perusahaan (pengambil keputusan: menyetujui surat dokter, cuti tanpa dibayar, lama cuti musibah, sanksi) | HR Manager (JA-14) | Process Owner dokumen HR di HR-ORG-01; jabatan terdekat untuk keputusan SDM | USULAN (tabel peran bagian 5) |
| Pimpinan Perusahaan | Direktur Utama (JA-01) | Sumber tidak mendefinisikan; jabatan tertinggi di HR-ORG-01 | USULAN (definisi bagian 3) |
| Pengusaha (Pasal 23, 28, 33) | Perusahaan | Satu istilah subjek (audit butir 15) | Dicatat di sini |
| tim atau karyawan lain nya (Pasal 23 ayat (2) huruf j) | Penanggung jawab pengganti | Satu istilah untuk pengganti pekerjaan | Dicatat di sini |

COO tidak disebut di dokumen ini, sehingga aturan sebutan "Direktur (COO)" tidak terpicu. Samuel di badan dokumen = "Direktur Utama"; "President Director" hanya di blok Approved By.

## 5. Penanganan cacat context/audit

Bagian 5 "Catatan kualitas dan celah" di context/audit/iso-sinux-supdocs-hr-2026-10-14.md (fileId 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tanpa kode, revisi, tanggal, pemilik, penyetuju, klasifikasi; "Peraturan Perusahaan" hanya inferensi dari nama berkas | Teratasi template dan defaults (nomor, Rev 00, Draft, tanggal dan tanda tangan kosong, pemilik HR Manager, INTERNAL). Dokumen menyebut sumber sebagai "PP - Cuti BAB VI" tanpa menulis "Peraturan Perusahaan" sebagai fakta. Open item 15 |
| 2 | Penomoran ayat terverifikasi; rujukan internal cocok | Dipakai untuk rujukan "Pasal n ayat (n)" di akhir tiap butir 4.x. Penomoran tidak diukur ulang dari biner (lihat bagian 1) |
| 3 | Pasal 26 ayat (6) dan Pasal 27 huruf e: peristiwa dan hari sama, kumulatif atau tidak tidak dinyatakan | Diperbaiki sebagian: 4.21 menulis satu hak 2 hari dan menyebut Pasal 27 huruf e; 4.25 huruf e merujuk 4.21. Pembacaan satu hak berlabel USULAN. Open item 6 |
| 4 | Sisa cuti: huruf f (maks 6 hari) dan huruf g (30 Juni) tidak dijelaskan urutannya | Ditulis apa adanya berdampingan di 4.5 dan SLA bagian 8. Tidak ada penafsiran. Open item 4 |
| 5 | Huruf h (14 hari kerja) lawan huruf d (12 cuti Januari); cuti ulang tahun masuk 12 hari atau tidak | Ditulis apa adanya di 4.2 dan 4.4. Open item 5 |
| 6 | Satuan "12 hari" lawan "14 hari kerja" | Satuan sumber dipertahankan; tidak ada definisi "hari" karena akan memperluas satuan ke semua jenis cuti tanpa dasar. Open item 2 |
| 7 | "tujuh 7 (tujuh) hari kerja" penulisan ganda | Diperbaiki: "7 (tujuh) hari kerja" di 4.7 dan bagian 8 |
| 8 | Pasal 34 ayat (2) huruf a: tanpa sanksi 1 hari, tanpa aturan di atas 5 hari, tanpa label subjek | Ditulis apa adanya di 4.34. Label subjek ditafsirkan "di luar masa percobaan" berlabel USULAN. Celah sanksi tidak ditutup. Open item 7 |
| 9 | Rentang sanksi SP Pertama sampai Kedua; dua kategori 5 hari | Ditulis apa adanya di 4.34 dan 4.35; penentu sanksi USULAN ke HR Manager (bagian 9). Open item 7 |
| 10 | Pasal 29 ayat (4) menyebut tata tertib kerja tanpa pasal | Pasal 29 dikecualikan dari scope (USULAN); tidak ada butir yang merujuk tata tertib |
| 11 | Rujukan UU No. 13 Tahun 2003 Pasal 93 ayat (3) tidak diverifikasi | Dikutip apa adanya di 4.16 dan Dokumen terkait; tidak diverifikasi terhadap perubahan regulasi. Open item 9 |
| 12 | Nama "sistem HR" tidak disebut | Istilah sumber dipertahankan dan didefinisikan di bagian 3. Catatan bahwa nama belum tertulis dipindah ke notes ini (Sweep butir 2) dan open item 1. Tidak ada nama sistem yang dikarang |
| 13 | Struktur Pasal 23 ayat (2) hanya judul dengan butir a sampai l | Dirujuk sebagai "Pasal 23 ayat (2) huruf x"; butir dikelompokkan per topik di 4.2 sampai 4.12 |
| 14 | "penuh" bersanding "prorata", rumus tidak dijabarkan | Kata sumber dipertahankan di 4.3; catatan rumus belum tertulis dipindah dari definisi Prorata ke notes ini (Sweep butir 2). Open item 3 |
| 15 | Subjek tidak seragam: Pengusaha lawan Perusahaan; HR, atasan langsung, Pimpinan Perusahaan tidak didefinisikan | Diperbaiki: satu istilah "Perusahaan"; HR, atasan langsung, dan Pimpinan Perusahaan didefinisikan di bagian 3 dan dipetakan ke jabatan HR-ORG-01 (bagian 4 notes ini) |
| 16 | Pasal 28: ayat (2) khusus Islam; ayat (3) dan (4) "ibadah kerohanian lainnya"; batas 40 hari hanya haji | Ditulis apa adanya di 4.27 dan 4.28. Batas untuk ibadah selain haji tidak ditambah. Open item 10 |
| 17 | Pasal 30 tanpa batas maksimum hari | Ditulis apa adanya di 4.31. Open item 11 |
| 18 | Salah ketik: "karyawan lain nya", "bayi nya", "diatas", "Pelanggaran Sanksi atas pelanggaran" | Diperbaiki: "lainnya" (menjadi "penanggung jawab pengganti"), "bayinya", "di atas", "Sanksi alfa" |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Tiga istilah untuk hal yang sama: "alfa" (Pasal 24), "tanpa izin atau mangkir" (Pasal 25), "tanpa keterangan" (Pasal 34) | Satu istilah "alfa"; definisi menyebut dua sebutan lain di sumber |
| B | Pasal 23 ayat (2) huruf b dan c memakai "dan/atau" antara masa percobaan selesai dan 3 bulan kerja; mana yang berlaku tidak dinyatakan | Ditulis apa adanya di 4.3. Open item 8 |
| C | Pasal 24 ayat (3) "4 bulan berturut-turut atau untuk waktu yang lama" lawan Pasal 33 "berkepanjangan dan bersifat terus-menerus": ambang tidak sama | Ditulis apa adanya di 4.15. Open item 8 |
| D | Pasal 32 ayat (1) menyebut "semua jenis cuti" tetapi hanya merinci cuti tahunan dan izin cuti berbayar; cuti sakit, haid, melahirkan, dan ibadah punya mekanisme sendiri atau tidak menyebut sistem HR | Cuti dijadwalkan (6.1) memakai sistem HR; sakit dan haid memakai pemberitahuan; penerapan ke cuti melahirkan, ibadah, dan tanpa dibayar berlabel USULAN. Open item 12 |
| E | Pasal 22 ayat (4) menyerahkan penggantian cuti ke "peraturan yang telah ditetapkan oleh Perusahaan" yang tidak ada di sumber | 4.32 ditulis apa adanya; tidak ada prosedur penggantian cuti karena tidak ada sumber. Open item 13 |
| F | Pasal 34 ayat (1) mencakup pelanggaran "cuti ataupun izin", termasuk izin Pasal 29 yang dikecualikan dari scope | 4.33 ditulis apa adanya; scope tetap mengecualikan Pasal 29 |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Langkah 6.1 (ajukan, lampirkan dokumen, tunjuk pengganti, setujui, ambil cuti) disusun penyusun dari Pasal 32 ayat (1), (2), (5) dan Pasal 23 ayat (2) huruf i. Urutan lampirkan dokumen lalu tunjuk pengganti tidak tertulis di sumber.
2. Dokumen pendukung per jenis cuti (surat dokter dengan HPL, surat dokter HPL istri, surat resmi instansi, dokumentasi haji) dirujuk ke butir 4.18, 4.21, 4.25, 4.28 di langkah 6.1 tanpa mengulang isinya.
3. Cuti sakit dan cuti haid tidak lewat sistem HR menurut sumber (hanya pemberitahuan); saluran pemberitahuan tidak disebut di sumber (open item 12).
4. "HR" di Pasal 24 dan Pasal 26 dibaca HRGA Officer; "Perusahaan atau HR" di Pasal 26 ayat (4) dipersempit menjadi HRGA Officer saja.
5. Karyawan yang mendelegasikan pekerjaan di cuti mendesak mendelegasikannya ke penanggung jawab pengganti (sumber: "tim atau karyawan lain").
6. Pelaku pemanggilan kembali (Pasal 23 ayat (2) huruf l) tidak disebut sumber; dipilih Atasan langsung (USULAN).
7. Rekaman dan lokasi: sistem HR untuk permohonan (nama dari sumber, "yang digunakan oleh Perusahaan"); "Folder Google Drive Departemen HR" untuk dokumen pendukung mengikuti pola FAT-SOP-05, tanpa sumber (USULAN). Retensi tidak diberi angka karena tidak ada sumber.
8. Klasifikasi: worklist memberi INTERNAL untuk SOP, dipakai persis. Rekaman cuti diusulkan RESTRICTED (Internal) di 4.37 (aturan config/defaults.json: data karyawan = RESTRICTED (Internal)).
9. Tiket Zammad dan GLPI, vault, PPN, dan COO tidak muncul di sumber maupun dokumen ini; aturan lintas dokumen itu tidak terpicu.
10. Sumber tidak memuat rujukan internal AI; tidak ada yang dibuang.

## USULAN

| # | Butir USULAN di spec | Pemutus yang disarankan |
|---|---|---|
| U1 | Enam klausul ISO di bagian 11 (9001 5.3, 7.5.3, 8.1; 27001 Annex A 6.2, 5.33, 5.34), label "(USULAN, perlu konfirmasi konsultan)" | Konsultan, lalu owner |
| U2 | Pemetaan istilah sumber ke jabatan: Pimpinan Perusahaan = Direktur Utama; HR = HRGA Officer; keputusan atas nama Perusahaan = HR Lead (definisi bagian 3, tabel peran) | Samuel (Pimpinan Perusahaan), Aziz (HR dan Perusahaan); diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U3 | Pelaku pemanggilan kembali karyawan yang sedang cuti: Atasan langsung (6.7) | Aziz |
| U4 | Pelaku pencatatan HRGA Officer: alfa sakit tanpa surat (6.3), cuti haid (6.5), pembatalan cuti (6.7); penerima surat keterangan dokter dan penerima pemberitahuan haid (6.3, 6.5) | Aziz |
| U5 | Pengecualian scope: hari libur resmi dan upah lembur (Pasal 22 ayat (1) sampai (3)), izin Pasal 29, pemutusan hubungan kerja (WFH berasal dari sumber) | Aziz |
| U6 | Pasal 26 ayat (6) dan Pasal 27 huruf e dibaca satu hak 2 hari (4.21) | Aziz, dengan Legal |
| U7 | Penerapan alur 6.1 (Pasal 32 ayat (1)) ke cuti melahirkan, pendampingan, cuti ibadah, dan cuti tanpa dibayar | Aziz |
| U8 | Label subjek Pasal 34 ayat (2) huruf a = karyawan di luar masa percobaan (4.34) | Aziz, dengan Legal |
| U9 | Urutan cuti mendesak: ajukan di sistem HR sesudah persetujuan atasan langsung (6.2 langkah 4) | Aziz |
| U10 | Penanggung jawab pengganti dicatat pada permohonan (6.1 langkah 3) | Aziz |
| U11 | Akibat penolakan cuti: karyawan tidak mengambil cuti (bagian 9) | Aziz |
| U12 | HR Lead menentukan sanksi alfa, surat peringatan, dan pemotongan cuti tahunan (bagian 9, tabel peran) | Aziz, dengan Samuel; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U13 | Klasifikasi RESTRICTED (Internal) untuk permohonan cuti, surat dokter, dan HPL (4.37) | Aziz, dikonfirmasi owner |
| U14 | Lokasi rekaman (sistem HR, Folder Google Drive Departemen HR), pemilik HRGA Officer, retensi ditetapkan HR Lead bersama Legal (tabel rekaman) | Aziz, dengan Legal; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U15 | HR Lead memeriksa kepatuhan dengan membandingkan permohonan cuti di sistem HR dengan bagian 4 (kesimpulan) | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |
| U16 | HR Lead sebagai pelaku di bagian 9 untuk cuti ibadah kedua kalinya (4.27) dan sakit berkepanjangan saat cuti tahunan (4.12); Pasal 28 ayat (3) dan Pasal 23 ayat (2) huruf k tidak menyebut pelaku | Aziz; diubah W9: HR Manager diganti HR Lead (LEAD G-3 A2) |

Total: 16 butir USULAN. Label "(USULAN)" persis di dokumen terhitung 18 oleh lint (warn); 33 kemunculan kata USULAN di spec termasuk bentuk "(USULAN: ...)" dan "(USULAN pelaku)". Sesudah Sweep, alasan di dalam label sudah dipindah ke notes ini: U3 (pemanggil tidak disebut di PP - Cuti), U4 (penerima surat dokter dan penerima pemberitahuan haid tidak disebut), U8 (Pasal 34 ayat (2) huruf a tanpa label subjek), U9 (urutan tidak disebut), U11 (akibat penolakan tidak dinyatakan).

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Nama sistem HR yang dipakai Perusahaan untuk pengajuan cuti tidak tertulis di sumber | Aziz |
| 2 | Satuan hari: cuti tahunan "12 hari" tanpa kata kerja, "14 hari kerja", cuti khusus dan lainnya tanpa satuan. Hari kerja atau hari kalender belum diputus; definisi hari kerja belum ada | Aziz |
| 3 | Rumus prorata tidak ada; "penuh" bersanding "prorata" (Pasal 23 ayat (2) huruf c) | Aziz |
| 4 | Sisa cuti: batas 6 hari (huruf f) dan batas 30 Juni (huruf g) berurutan atau berdiri sendiri; perlakuan sisa di atas 6 hari tidak ada | Aziz |
| 5 | Cuti ulang tahun termasuk dalam 12 hari atau tambahan; kapan 14 hari mulai diberikan | Aziz |
| 6 | Pasal 26 ayat (6) dan Pasal 27 huruf e: satu hak 2 hari atau dua hak (4 hari) | Aziz, Legal |
| 7 | Pasal 34: tidak ada sanksi SP untuk alfa 1 hari karyawan di luar masa percobaan dan untuk alfa lebih dari 5 hari; rentang "SP Pertama sampai Kedua" tanpa penentu; penerbit SP dan pelaku pemotongan gaji tidak disebut | Aziz, Legal |
| 8 | Ambang sakit berkepanjangan (4 bulan berturut-turut atau "waktu yang lama" di Pasal 24 ayat (3), "terus-menerus" di Pasal 33 ayat (1)); "dan/atau" di Pasal 23 ayat (2) huruf b dan c (masa percobaan selesai atau 3 bulan, mana yang berlaku) | Aziz, Legal |
| 9 | Rujukan UU No. 13 Tahun 2003 Pasal 93 ayat (3) dikutip apa adanya dan belum dicek terhadap perubahan regulasi | Legal |
| 10 | Pasal 28: batas hari untuk ibadah kerohanian selain haji tidak ada (ayat (4) hanya "sesuai jangka waktu"); ayat (2) khusus karyawan beragama Islam | Aziz |
| 11 | Pasal 30: cuti tanpa dibayar tanpa batas maksimum hari | Aziz |
| 12 | Saluran pemberitahuan sakit, haid, dan kelahiran bayi (sistem HR, chat, atau email) tidak disebut; batas waktu keputusan atasan langsung atas permohonan cuti tidak ada; tindak lanjut penolakan dan banding tidak diatur | Aziz |
| 13 | Peraturan penggantian cuti dan upah lembur untuk kerja di hari libur resmi (Pasal 22 ayat (4)) tidak ada di sumber; tidak ada prosedur penggantian cuti di SOP ini | Aziz |
| 14 | Pasal 29 (izin keluar atau terlambat) merujuk tata tertib kerja tanpa nomor pasal; dikecualikan dari SOP ini, dan perlu dokumen terpisah bila diminta | Aziz |
| 15 | Sumber tanpa kode, revisi, tanggal, pemilik, dan penyetuju; "PP" diduga Peraturan Perusahaan dan bab lain tidak ada di batch; belum ada penetapan resmi atas isi BAB VI sebagai aturan SINUX | Aziz, Samuel |
| 16 | Penomoran ayat dan butir huruf tidak diukur ulang dari biner docx (hasil download tidak tersimpan ke berkas); bila verifikator mendekode docx, cocokkan butir 4.x dengan numbering.xml | Verifikator |
| 17 | Kepemilikan: HR Manager sebagai Process Owner berasal dari aturan defaults, bukan dari sumber (sumber tanpa "Pemilik dokumen") | Aziz; ditutup W9: process_owner kini HR Lead (defaults v22) |
| 18 | Hak normatif dan peraturan perundang-undangan yang dirujuk sumber secara umum (Pasal 23 ayat (2) huruf k, Pasal 26 ayat (1) dan (8)) tidak dicek terhadap regulasi terkini | Legal |

## 7. Pemeriksaan bahasa (dua pertanyaan, dijawab sebelum selesai)

**Apa yang membuat teks ini terdengar buatan AI?** Temuan pada draf pertama, semuanya sudah diperbaiki di spec:
- "Pada saat itu" di 4.3 tidak jelas menunjuk apa. Diganti "Setelah syarat itu terpenuhi".
- Kalimat pembuka 4.15 berputar ("mengikuti ketentuan sakit berkepanjangan"). Diganti rujukan ke butir 4.15 dan 4.16.
- Tujuan menulis "pihak yang berwenang", rujukan kabur. Diganti "persetujuan atau pemberitahuan sesuai jenisnya".
- Definisi Perusahaan membawa aturan keputusan, padahal bagian 3 hanya arti istilah. Kalimat itu dipindah ke tabel peran saja.
- "memotong cuti tahunan karyawan" di 4.17 memakai kata kerja tanpa pelaku salinan sumber. Diganti "dikenai pemotongan cuti tahunan karyawan".
- Sisa yang tidak saya ubah dan perlu mata manusia: 37 butir bagian 4 berpola sama (label topik, titik dua, kalimat, rujukan pasal di akhir) dan sel langkah memuat beberapa "(USULAN: ...)". Pola itu dipertahankan karena butir memang diambil verbatim dari sumber dan langkah prosedur menunjuk butir lewat nomor. Kalimat tim di sumber yang sudah jelas tidak dirapikan hanya agar terdengar rapi (T1).

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**
- Semua angka di bagian 4, 8, dan 9 (12, 14, 3, 6, 7, 10:00 WIB, 30 Juni, 4 bulan, 100%, 75%, 50%, 25%, 40 hari, 10 minggu, 1,5 bulan, 2 dan 3 hari, 1 hari) ada di sumber dan dikutip di bagian 2 notes ini. Angka dari sumber dipakai pada lingkupnya; tidak ada angka baru. Batas waktu keputusan atasan langsung sengaja tidak diberi angka ("Belum ditetapkan di sumber").
- Tanpa sumber dan sudah berlabel atau tercatat: nomor klausul ISO (U1, dari ingatan penyusun); lokasi "Folder Google Drive Departemen HR" dan pemilik rekaman (U14); klasifikasi RESTRICTED (Internal) (U13); pemetaan istilah ke jabatan (U2); pelaku langkah yang tidak disebut sumber (U3, U4, U9, U12).
- Nama orang hanya di blok approval dan berasal dari config/defaults.json. Kode JA-01 dan JA-12 berasal dari specs/HR-ORG-01.json. Tidak ada tanggal selain "30 Juni" dari sumber; tanggal efektif kosong.
- Diperbaiki sesudah pemeriksaan: langkah dan definisi sempat menyiratkan bahwa persetujuan atasan langsung dicatat di sistem HR. Sumber hanya menyebut permohonan lewat sistem HR dan persetujuan atasan langsung, sehingga frasa "di sistem HR" dibuang dari langkah persetujuan dan definisi Sistem HR. Akibat penolakan cuti (karyawan tidak mengambil cuti) sempat ditulis sebagai fakta; kini berlabel USULAN (U11).

## Sweep

Putaran penghalusan sesudah DONE (instruksi orkestrator, berkas sweep HR-SOP-08). Yang diubah hanya butir yang ditunjuk. Hasil uji sesudah Sweep: render selesai, lint `"pass": true` (warn "18 butir (USULAN) menunggu ACC"), validator OOXML "All validations PASSED!", blankscan "ok 18".

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Bagian 9, label pelaku HR Manager (cuti ibadah kedua kalinya) | "HR Manager menetapkan cuti itu tanpa upah (butir 4.27)." | "HR Manager menetapkan cuti itu tanpa upah (butir 4.27, USULAN pelaku)." |
| 2 | Bagian 9, label pelaku HR Manager (sakit berkepanjangan saat cuti tahunan) | "...tanpa mengurangi hak normatif pekerja (butir 4.12)." | "...tanpa mengurangi hak normatif pekerja (butir 4.12, USULAN pelaku)." |
| 3 | Bagian 7, lajur diagram lawan 6.7 langkah 3 | Simpul h "Cuti perlu ditunda atau karyawan dipanggil kembali?" dan simpul i "Tunda cuti atau panggil kembali; cuti kompensasi" keduanya di lajur Direktur Utama | Simpul h "Kepentingan Perusahaan mendesak?" tanpa lajur; simpul i "Tunda cuti; cuti kompensasi" di lajur Direktur Utama; simpul k baru "Panggil kembali karyawan" di lajur Atasan langsung; cabang h berlabel Ditunda, Dipanggil, Tidak; i dan k menuju "Cuti selesai" |
| 4 | 6.3 langkah 2 | "...sesuai butir 4.14 (USULAN: sumber tidak menyebut penerima)." | "...sesuai butir 4.14 (USULAN)." |
| 5 | 6.7 langkah 3 | "...bila kondisi butir 4.11 terpenuhi (USULAN: sumber tidak menyebut pemanggil)." | "...bila kondisi butir 4.11 terpenuhi (USULAN)." |
| 6 | 6.2 langkah 4 | "...sesudah persetujuan atasan langsung (USULAN: sumber tidak menyebut urutan)." | "...sesudah persetujuan atasan langsung (USULAN)." |
| 7 | Butir 4.34 | "Sanksi alfa karyawan di luar masa percobaan (USULAN penafsiran: sumber tidak memberi label subjek pada huruf a): ..." | "Sanksi alfa karyawan di luar masa percobaan (USULAN): ..." (isi sanksi tidak berubah) |
| 8 | SLA baris terakhir | "Belum ditetapkan di sumber" | "Belum ditetapkan di PP - Cuti BAB VI" |
| 9 | Dokumen terkait, baris PP - Cuti | "Dokumen sumber tanpa nomor; asal aturan di bagian 4." | "Memuat aturan di bagian 4. Belum bernomor." |
| 10 | Bagian 9, baris Sakit tanpa surat keterangan dokter | "...(butir 6.3, USULAN pelaku). Sumber tidak menyebut pelaku pemotongan gaji." | "...(butir 6.3, USULAN pelaku). Pelaku pemotongan gaji belum ditetapkan di PP - Cuti BAB VI." |
| 11 | Bagian 9, baris Permohonan cuti ditolak | "Karyawan tidak mengambil cuti itu (USULAN: sumber tidak menyatakan akibat penolakan). Sumber tidak mengatur banding atau pencatatan alasan penolakan." | "Karyawan tidak mengambil cuti itu (USULAN). Banding dan pencatatan alasan penolakan belum diatur di PP - Cuti BAB VI." |
| 12 | Definisi Prorata | "Perhitungan jatah cuti secara proporsional. Rumusnya belum tertulis di sumber." | "Perhitungan jatah cuti secara proporsional." (catatan rumus: open item 3) |
| 13 | Definisi Sistem HR | "Sistem yang dipakai Perusahaan untuk mengajukan permohonan cuti. Nama sistemnya belum tertulis di sumber." | "Sistem yang dipakai Perusahaan untuk mengajukan permohonan cuti." (catatan nama: open item 1) |
| 14 | Label klausul ISO (bagian 11, baris Status acuan klausul) | "(USULAN, dikonfirmasi konsultan)" | "(USULAN, perlu konfirmasi konsultan)" |

Penjelasan yang dipindah dari badan dokumen ke notes ini: penerima surat keterangan dokter (U4), pemanggil (U3, U4), urutan pengajuan cuti mendesak (U9), label subjek Pasal 34 ayat (2) huruf a (U8), akibat penolakan (U11), nama sistem HR (open item 1), rumus prorata (open item 3), pelaku pemotongan gaji dan SP (open item 7), banding dan pencatatan alasan penolakan (open item 12).

Tidak diubah karena di luar daftar butir Sweep (untuk keputusan orkestrator): (a) kata "sumber" di Scope kalimat terakhir ("Hanya pengecualian pertama berasal dari sumber..."), di pengantar bagian 4 ("sama dengan sumber"), di 6.5 langkah 1 ("USULAN: sumber menyebut Perusahaan tanpa penerima"), dan di Dokumen terkait baris UU No. 13 Tahun 2003 ("dikutip apa adanya dari sumber"); (b) temuan pemeriksa lain di qa/HR-SOP-08.verify.json: rujukan Pasal 22 di Scope, "butir" untuk 4.x dan 6.x, SP1 sampai SP3 yang tidak dipakai di badan, dua baris SLA berisi syarat atau jumlah, tugas HRGA Officer sebagai penerima surat dokter dan tugas HR Manager di bagian 9 yang belum ada di tabel peran, serta label USULAN yang terlalu luas pada baris Atasan langsung di tabel peran.

## ISO-W9

| Butir | Sebelum | Sesudah |
|---|---|---|
| A2 | Process Owner di sampul: HR Manager | HR Lead |
| A2 | Blok Reviewed: Aziz Priyo Widakdo / HR Manager | Aziz Priyo Widakdo / HR Lead |
| A2 | Tabel peran bagian 5, nama peran | HR Manager | HR Lead |
| A2 | Langkah bagian 6 (kolom PIC dan rekaman Keputusan HR Manager, 6 kemunculan) | HR Manager | HR Lead |
| A2 | Keterangan gambar alur bagian 7 | keputusan HR Manager (butir 6.1 dan 6.4) | keputusan HR Lead (butir 6.1 dan 6.4) |
| A2 | Bagian 9 (4 baris), kesimpulan (2 kalimat), tabel rekaman (3 sel retensi) | HR Manager | HR Lead |
| R2 | Notes USULAN U2, U12, U14, U15, U16 | HR Manager | HR Lead, dengan catatan "diubah W9" di baris itu |
- SPV tidak ditambahkan: dokumen tidak punya kolom tingkat jabatan.
- A3 tidak berlaku: dokumen tidak menyebut JA-03 atau JA-04. B4 tidak berlaku: tidak ada rujukan ke SNX-HR-FRM-01, FRM-02, RPT-01, atau SOP T&D. Lane diagram tidak memuat HR Manager (lane: Karyawan, Atasan langsung, HRGA Officer, Direktur Utama), jadi tidak berubah.

Open item ditutup atau diubah (status baris lama diubah di tabel Open items):
- ditutup W9: process_owner HR Manager diganti HR Lead mengikuti defaults v22.

## W10 (bahasa, ISO-W10)

### W10 label dihapus
nihil. Label di tabel peran ("(USULAN, butir 6.1, 6.2, dan 6.7)" dan sejenisnya) tetap satu per sel, kini "(USULAN)" di akhir sel. Label "(butir 4.x, USULAN pelaku)" di bagian 9 ditulis "sesuai butir 4.x (USULAN: pelaku)"; tidak ada label yang hilang.

### W10 kalimat dihapus atau dipindah
- Butir 4.37: "Lokasi, pemilik, dan masa simpan ada di tabel bagian 11." (kalimat penunjuk, STYLE §3.2; faktanya ada di tabel record bagian 11)
- Pengantar bagian 4: "Istilah subjek disamakan dengan bagian 3" ditulis ulang "hanya sebutan pihak yang disamakan dengan istilah di bagian 3"; "Nomor pasal dan ayat ada di akhir tiap butir" digabung ke kalimat pertama.
- Butir 4.36: "peran dan wewenang tiap pihak dalam SOP ini ada di bagian 5" ditulis ulang "setiap pihak dalam SOP ini menjalankan peran dan wewenang menurut bagian 5".
- Tabel peran: rujukan "(butir 6.1 sampai 6.7)", "butir 6.1, 6.2, dan 6.7", "butir 6.3 sampai 6.7", "butir 6.1, 6.4, dan bagian 9", "(butir 6.7)" dibuang (STYLE §3.1).
- Kata "sumber" sebagai catatan penyusunan diganti nama dokumennya (PP - Cuti BAB VI) di Scope, pengantar bagian 4, 6.5 langkah 1, dan Dokumen terkait baris UU No. 13 Tahun 2003.

### W10 audit pointer
- .policy[46]: pointer murni dibuang, isi tidak dinyatakan ulang (lokasi, pemilik, dan masa simpan tetap di tabel record bagian 11).
- .roles[0][1]: pointer murni dibuang, isi tidak dinyatakan ulang (daftar tugas sama: mengajukan, melampirkan, menunjuk pengganti, memberi tahu sakit, haid, kelahiran bayi, memenuhi panggilan kembali).
- .roles[1][1]: pointer murni dibuang, isi tidak dinyatakan ulang; label (USULAN) tetap.
- .roles[2][1]: pointer murni dibuang, isi tidak dinyatakan ulang; kelima tugas dan label (USULAN) tetap.
- .roles[3][1]: pointer murni dibuang, isi tidak dinyatakan ulang; kelima keputusan dan label (USULAN) tetap.
- .roles[4][1]: pointer murni dibuang, isi tidak dinyatakan ulang.

### W10 selisih angka
- "11": hilang bersama kalimat penunjuk "ada di tabel bagian 11" di butir 4.37.
- "9": hilang bersama rujukan "bagian 9" di sel peran HR Lead; tidak ada angka aturan yang berubah.

### W10 catatan
- Pihak luar: dokumen ini tidak menyebut klien atau pelanggan.
- "bila" diganti "jika"; "Hasil yang dijaga:" di Purpose ditulis ulang sebagai kalimat biasa. Teks pasal PP - Cuti BAB VI di bagian 4 dibiarkan (T1).
- Jembatan istilah: "Record (rekaman)" di butir 4.37, kemunculan pertama di badan.
- Rujukan langkah dan batas (butir 4.7, 4.29, 4.13 di bagian 6 dan 8; butir 6.x di bagian 9) dipertahankan.
