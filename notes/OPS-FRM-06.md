# Catatan penyusun OPS-FRM-06: Project Handover / BAST & Closure Report

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-FRM-06.json. Mode generic, aksi T1, wave W5, nomor SNX-OPS-FRM-06 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber, audit_class B. Process owner = "Service Delivery Manager" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). Approval persis defaults: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revisi 00, effective_date kosong, review YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-FRM-06.json /tmp/pen-OPS-FRM-06/OPS-FRM-06.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-OPS-FRM-06/OPS-FRM-06.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "15 butir (USULAN) menunggu ACC" (15 kemunculan teks, 10 butir berbeda, lihat bagian USULAN). Diuji ulang sesudah putaran perbaikan 1 (bagian terakhir).
- Render PDF LibreOffice (14 halaman) dibuka: halaman Identity, Peran, Alur Proses, dan Bagian A terbaca; diagram 8 simpul tegak (rankdir TB).
- Pemeriksaan tambahan atas spec: tidak ada em-dash atau en-dash; tiap kode SNX yang dirujuk di badan ada di bagian Dokumen Terkait; tidak ada kalimat panjang yang sama di dua bagian (hanya baris tabel yang berulang pendek); nama peran di tabel Peran, kolom Pelaku Penanganan Pengecualian, dan blok tanda tangan Bagian B dan C sama persis.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-06_Project_Handover_BAST_Closure_Report.docx (139171 byte) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb | 2026-10-13T06:09:02Z (get_file_metadata, sama dengan yang tertulis di prompt) | read_file_content (teks); download_file_content didekode ke /tmp/pen-OPS-FRM-06/src/src.docx (139171 byte, ukuran sama dengan metadata). Isi zip diperiksa: word/media/rId21.png (diagram, dibuka) dan word/comments.xml (642 byte, tanpa teks komentar) |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris 73 OPS-FRM-06 | Kolom Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.5.5, 8.6" dan ISO/IEC 27001:2022 "5.8" (cocok dengan checklist.json: iso_9001 "8.5.5, 8.6", iso_27001 "5.8"; sumber menulis "Klausul atau kontrol Annex A 5.8") |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, berkas ops/SNX-OPS-FRM-06.md mulai baris 1865, bagian 5 Catatan kualitas dan celah | Salinan audit 13 sampai 14 Okt 2026 | DATA, dibandingkan dengan docx asli (teks dan gambar) |
| Pendukung lintas dokumen | Audit POL-OPS-001 (baris 151 sampai 165) dan PRO-OPS-001 (baris 577 sampai 609, 725) di berkas audit yang sama; specs/HR-ORG-01.json untuk nama peran Divisi Operation; notes/OPS-FRM-04.md dan OPS-FRM-05.md untuk perlakuan Zammad dan retensi | Salinan audit dan spec lane lain, bisa basi | Dipakai hanya untuk menyamakan istilah dan untuk open items 2 sampai 6 |

Isi sumber tidak memuat kalimat perintah untuk pekerja. Kalimat "Teks dalam kurung siku adalah petunjuk" adalah petunjuk isi form, bukan instruksi untuk saya; kurung sikunya sudah diganti label kolom (lihat bagian 2). Nihil open item jenis ini.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini satu dokumen tiga bagian: BAST ke pelanggan (G2), checklist serah terima SD dan PM ke Operation (G3), dan laporan penutupan proyek | "Bagian A, Berita Acara Serah Terima (BAST) implementasi kepada pelanggan (gate G2)." / "Bagian B, checklist serah terima internal dari SD dan PM ke Operation (gate G3)." / "Bagian C, laporan penutupan proyek (closure report)." (Petunjuk pengisian) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |
| 2 | Layanan baru BAU bila semua butir G3 Lolos atau Tidak berlaku; Operation boleh menolak secara tertulis dan layanan tetap hypercare dengan pemilik SD dan PM | "Layanan dinyatakan BAU hanya bila semua butir berstatus Lolos atau Tidak berlaku. Operation berhak menolak serah terima secara tertulis bila checklist belum lengkap; selama itu layanan berstatus hypercare dengan pemilik SD dan PM." (Bagian B) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |
| 3 | Pemilik dokumen adalah Service Delivery Manager; klasifikasi RESTRICTED (Internal); masa simpan record durasi kontrak ditambah 5 tahun | "Pemilik dokumen \| Service Delivery Manager"; "Klasifikasi \| RESTRICTED (Internal)"; "Masa simpan record \| Durasi kontrak + 5 tahun" (tabel Atribut) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Aturan pelanggan pemerintah | "Untuk pelanggan pemerintah melalui main contractor, BAST dibuat atas nama SINUX, versi original disimpan di Drive, dan periode ditetapkan main contractor. Dokumen teknis untuk pelanggan pemerintah tanpa harga, diskon, tier, maupun roadmap komersil." | Petunjuk pengisian. Jadi P3 dan P4 |
| Prasyarat Bagian A | Kotak "UAT lolos" dengan sub-label "SNX-OPS-FRM-05 ditandatangani" mendahului "Bagian A: BAST" | Gambar rId21 (dibuka). Jadi P2 dan simpul pertama diagram |
| Penerima BAU | Kotak "Layanan BAU 24/7" dengan sub-label "diterima Head of Operation"; kotak "Tetap hypercare" dengan sub-label "pemilik SD dan PM" | Gambar rId21 |
| Penyetuju dan peran di G3 | "Menyerahkan (Project Manager)", "Menerima (Lead NOC)", "Menerima (Lead SOC, bila ada layanan SOC)", "Menyetujui (Head of Operation)"; sub-label "PM bersama Lead NOC dan Lead SOC" | Bagian B (blok tanda tangan) dan gambar rId21 |
| Peran Bagian C | "Disusun (Project Manager)", "Disetujui (Service Delivery Manager)" | Bagian C, blok tanda tangan |
| Klausul masa layanan | "Dengan ditandatanganinya berita acara ini, masa layanan atau garansi berjalan sesuai kontrak sejak tanggal [tanggal]." | Bagian A. Kalimat dipertahankan, tanggalnya jadi satu baris tabel |
| Nilai status BAST | Baris deliverable 1 dan 2 berisi "Diterima", baris 3 berisi "Diterima dengan catatan" | Bagian A. Jadi P5; baris dikosongkan |
| Butir G3 berbunyi bersyarat | "Semua aset masuk monitoring NOC (dan SIEM bila layanan SOC), alert sudah diuji"; "Backup aktif dan restore uji pertama berhasil, tercatat di SNX-ISMS-FRM-01 (bila layanan backup ada)" | Bagian B butir 3 dan 4 |
| Sistem tiket di G3 | "Pelanggan, aset, dan kontak terdaftar di ticketing system (Zammad atau Service Hub)" | Bagian B butir 1 |
| Penyetuju dan pemeriksa sumber | "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain"; "Diperiksa oleh \| ISO/ISMS Coordinator"; "Disusun oleh \| Service Delivery Manager" | Atribut dan Pengesahan |
| Rujukan internal AI di Arsip | "Lessons learned disetor ke knowledge base \| [nomor packet staging]" | Bagian C, tabel 5 Arsip |
| Riwayat revisi | "Draft awal untuk sertifikasi ISO 9001:2015 dan ISO/IEC 27001:2022" dan "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | Riwayat revisi, dua baris Revisi 00 bertanggal 13 Oktober 2026 |
| Isu sisa dan arsip | "Catatan atau isu sisa yang disepakati" dengan kolom Uraian, Pemilik, Target selesai; "SNX-OPS-FRM-01 sampai FRM-05 proyek ini \| [folder Drive]"; "BAST bertanda tangan (original) \| [folder Drive]" | Bagian A dan Bagian C |

## 2. Apa yang diubah dari sumber dan kenapa (T1)

| Sumber | Spec | Dasar |
|---|---|---|
| 16 blok sumber (atribut, riwayat revisi, petunjuk, diagram, A, B, C, pengesahan) | 14 bagian generic: Tujuan, Ruang Lingkup, Definisi, Ketentuan Pengisian, Peran, Alur Proses, Bagian A, Bagian B, Bagian C, Penanganan Pengecualian, Rekaman dan Retensi, Acuan Klausul ISO, Dokumen Terkait, Kesimpulan | Mode generic memakai halaman depan template (identitas, revisi, approval) dan badan bebas. Tiga bagian form dipertahankan utuh sebagai Bagian A, B, C |
| Atribut dan Pengesahan | Blok Identity, Revision History, Approval dari meta | Nilai dari defaults (prepared, reviewed, approved) dan prompt. Pengesahan sumber (Service Delivery Manager, ISO/ISMS Coordinator, COO) tidak dibawa; lihat open item 1 dan 13 |
| Petunjuk pengisian | Ketentuan P1 sampai P5 | Substansi sama, dipecah per butir bernomor agar bagian lain bisa merujuk nomornya |
| Aturan di awal Bagian B | P6, P7, dan P8; paragraf pembuka Bagian B hanya merujuk nomornya | Kalimat yang sama tidak disalin ke dua bagian |
| Tanda kurung siku "[nomor]", "[hari]", "[nama]", "[folder Drive]" | Label kolom atau baris, sel isian kosong | Aturan form baru: sel data faktual kosong, tanpa baris contoh. Kalimat pembuka BAST dipertahankan, hari dan tanggal pindah ke tabel |
| Status contoh "Diterima" (baris 1 dan 2) dan "Diterima dengan catatan" (baris 3) | Baris deliverable 1 sampai 3 hanya bernomor; nilai status jadi P5 | Cacat tercatat butir 2 |
| "Layanan BAU 24/7" di gambar | Simpul "Layanan BAU" | Lihat open item 12 |
| "Semua kriteria lolos?" di gambar | "Semua butir Lolos atau Tidak berlaku?" | Pertanyaan lama tidak sama dengan aturan teks (Tidak berlaku juga lolos) |
| Kotak "Tetap hypercare" tanpa panah balik | Garis balik ke Bagian B berlabel (USULAN) | Cacat tercatat butir 8 |
| "Zammad atau Service Hub" | Istilah "ticketing system" didefinisikan sebagai Zammad (USULAN) | Owner 14 Okt, defaults.ticketing; preseden notes/OPS-FRM-04.md |
| "Lessons learned disetor ke knowledge base \| [nomor packet staging]" | Baris "Lessons learned proyek ini" dengan lokasi kosong | Rujukan jalur staging dilarang (RUNBOOK §0 butir 6); lihat open item 10 |
| Dua baris Revisi 00 | Satu baris revisi dari meta | Renderer hanya punya satu baris; lihat cacat butir 9 |
| Tidak ada bagian Rekaman, Acuan, Dokumen Terkait | Tiga bagian itu ditambah | Dituntut RUNBOOK §6 (acuan klausul, tabel rekaman, rujukan kode ke Dokumen Terkait) dan prompt (acuan klausul wajib) |

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Seluruh isian placeholder kosong atau teks petunjuk dalam kurung siku | Dipertahankan sebagai form kosong (benar untuk T1 form). Kurung siku diganti label kolom, tidak ada data karangan |
| 2 | Status contoh "Diterima" dan "Diterima dengan catatan" terisi di tabel deliverable | Diperbaiki: baris dikosongkan, dua nilai dipindah ke P5 sebagai daftar pilihan |
| 3 | Bagian A bergate G2 dan Bagian B bergate G3, Bagian C tanpa nomor gate | Tidak diubah: sumber tidak menetapkan gate untuk laporan penutupan, dan menambahnya adalah keputusan proses. Open item 13 |
| 4 | Butir 3 dan 4 bisa Tidak berlaku, tanpa panduan alasan wajib | Diperbaiki. Syarat bersyarat di sumber dibatasi pada unsurnya: butir 3 "Semua aset masuk monitoring NOC (dan SIEM bila layanan SOC), alert sudah diuji" hanya melepas unsur SIEM bila tidak ada layanan SOC, dan butir 4 "(bila layanan backup ada)" berlaku utuh. Itu P8; monitoring NOC dan uji alert tidak boleh Tidak berlaku. P9 mewajibkan alasan di kolom Bukti atau referensi, berlabel (USULAN). Penanganan Pengecualian punya satu baris per kondisi (butir 3, butir 4) dengan pelakunya. Tafsir awal di audit ("sehingga butir bisa Tidak berlaku") dibaca terlalu luas untuk butir 3; lihat putaran perbaikan 1 |
| 5 | Checklist G3 11 butir lawan 8 butir di PRO-OPS-001 §8.2; butir 2, 8, 10 tanpa padanan; rujukan ke SOP-01 6.5 dan 6.6 cocok; FRM-07 dirujuk SOP-03 bukan SOP-05 | Tidak diubah: 11 butir sumber dipertahankan utuh (T1) dan PRO-OPS-001 di luar lane saya. Open item 3. Rujukan ke SOP-01 6.5 dan 6.6 dipertahankan di P1; cek ulang setelah SOP-01 dirender, open item 14 |
| 6 | Tiga rujukan ISMS (REG-01, FRM-01, REG-04) ada; SNX-ISMS-PRO-01 tidak disebut di sumber | Ketiganya masuk Dokumen Terkait. PRO-01 tidak ditambah ke badan karena sumber tidak menyebutnya; tingkat klasifikasi dipakai lewat meta saja |
| 7 | Gambar menyebut "24/7", teks tidak | Label diganti "Layanan BAU" tanpa 24/7; open item 12 |
| 8 | Gambar tanpa batas waktu hypercare dan tanpa panah balik dari "Tetap hypercare" | Panah balik ditambah berlabel (USULAN), dengan satu baris penanganan berpelaku; dasar kalimat PRO-OPS-001 "layanan tetap hypercare dengan pemilik SD dan PM sampai kriteria terpenuhi" (audit baris 609). Batas waktu tidak ditambah: POL-OPS-001 menulis "Durasi hypercare standar 2 minggu. (USULAN)" (audit baris 155) untuk dokumen lain; "Durasi hypercare" masuk daftar pengecualian Ruang Lingkup, open item 6 |
| 9 | Dua baris Revisi 00 bertanggal sama, "Menunggu"; "keselarasan RTO dan target pulih" tidak relevan | Satu baris revisi dengan teks dari prompt. Teks lama dicatat di tabel Fakta pendukung. Frasa RTO tidak dibawa karena form ini tidak membahas RTO |
| 10 | Seluruh blok tanda tangan kosong | Dipertahankan kosong; tanda tangan, tanggal efektif, dan tanggal lain tidak diisi (batas keras 3). Kolom Signature di halaman approval juga kosong |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | Rujukan jalur staging "[nomor packet staging]" di tabel Arsip | Dibuang (RUNBOOK §0 butir 6); baris lessons learned tanpa lokasi. Open item 10 |
| B | Pertanyaan keputusan di gambar "Semua kriteria lolos?" tidak menyebut Tidak berlaku, padahal Bagian B menganggapnya lolos | Disamakan dengan teks di diagram baru |
| C | "Operation berhak menolak" tidak menunjuk peran | Ditaruh pada Head of Operation berlabel (USULAN) dan dicatat sebagai open item 7 |
| D | Retensi 5 tahun di form ini, 3 tahun di FRM-01, FRM-02, FRM-03, FRM-05 yang diarsipkan bersamanya (Bagian C Arsip) | Tidak diubah. Open item 2 |
| E | "Pihak Pertama" BAST tidak ditunjuk perannya | Pengisi Bagian A ditaruh pada Project Manager berlabel (USULAN); penanda tangan Pihak Pertama tetap kolom isian. Open item 9 |
| F | Butir 3 checklist bisa dibaca Tidak berlaku utuh bila tidak ada layanan SOC (tafsir audit); sumber hanya mensyaratkan SOC untuk SIEM | Dikoreksi di putaran perbaikan 1 (P8, P9, baris 3 Penanganan Pengecualian) |
| G | Butir 11 menyebut Lead SOC padahal blok tanda tangan menulis "bila ada layanan SOC" | Baris 5 Penanganan Pengecualian, berlabel (USULAN) |

## 4. Asumsi

| # | Asumsi | Dasar |
|---|---|---|
| A1 | "SD dan PM" ditulis "Service Delivery dan Project Management" tanpa kata "Divisi" atau "sub divisi" | Sumber hanya menulis "SD dan PM"; HR-ORG-01 menyebutnya sub divisi menurut POL-OPS-001 yang masih USULAN, jadi tidak dibawa |
| A2 | Pemilik hypercare "SD dan PM" dibaca sebagai Service Delivery Manager dan Project Manager, berlabel (USULAN 10) di Definisi | Audit bagian 4 memetakan demikian. Bertentangan dengan PRO-OPS-001 yang menulis Lead NOC sebagai pemilik hypercare (audit baris 578); open item 4 |
| A3 | "Operation" dibaca sebagai penerima G3: NOC, SOC, dan Head of Operation | Gambar dan blok tanda tangan G3 menyebut Lead NOC, Lead SOC, Head of Operation; sintesis menulis "Operation (NOC, SOC)" |
| A4 | Definisi NOC dan SOC memakai rumusan HR-ORG-01 (draft), singkatan diperluas dari istilah baku | Sumber hanya memakai singkatannya. Rumusan "memantau dashboard layanan dan menangani tiket" dan "memantau SIEM dan menangani insiden keamanan" berasal dari HR-ORG-01 yang berstatus Draft |
| A5 | Judul klausul ISO (8.5.5 Kegiatan setelah penyerahan, 8.6 Pelepasan produk dan jasa, Annex A 5.8 Keamanan informasi dalam manajemen proyek) | Judul baku standar, terjemahan saya. Worklist hanya memberi nomor klausul. Tidak ada sumber tim untuk judulnya |
| A6 | Kolom "Hubungan dengan dokumen ini" di Acuan Klausul ISO menautkan klausul ke butir form | Hubungan dibaca dari isi form (tanggal garansi, isu sisa, G3, butir 2, 7, 8), bukan dari penjelasan konsultan |
| A7 | Pengecualian Ruang Lingkup ditulis dari kode dokumen yang dirujuk sumber | Sumber tidak punya bagian pengecualian. Tiap baris menunjuk dokumen sumber yang menanganinya (FRM-05, FRM-09, FRM-07, kontrak) atau keadaan form (tanpa durasi hypercare) |
| A8 | "Service Delivery Manager meninjau dokumen setiap tahun" | review_period YEARLY dari prompt dan pemilik dokumen dari sumber; tidak ada kalimat sumber tentang siapa yang meninjau |
| A9 | Tabel Hari dan tanggal penandatanganan serta Tanggal mulai masa layanan atau garansi menjadi baris isian | Kalimat sumber "Pada hari ini, [hari], tanggal [tanggal]" dan "sejak tanggal [tanggal]" memuat dua tanggal itu |
| A10 | Sebutan COO tidak muncul di badan dokumen | COO hanya ada di blok persetujuan sumber, yang diganti defaults. Aturan "Direktur (COO)" tidak terpakai. Samuel muncul sekali sebagai "Direktur Utama" di Kesimpulan; Zammad dan GLPI mengikuti owner 14 Okt; vault dan PPN tidak ada di sumber dan tidak ditambahkan |

## USULAN

Sepuluh butir berlabel (USULAN) di spec. Tiap butir punya pemutus yang disarankan.

| # | Butir USULAN | Lokasi di spec | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Zammad sebagai ticketing system Operation untuk form ini (sumber: "Zammad atau Service Hub") | Definisi, Ticketing system; dipakai Bagian B butir 1 dan 9 | Owner, dengan Fani |
| 2 | P9: unsur SIEM yang tidak berlaku pada butir 3, dan butir 4 Tidak berlaku, diberi alasan di kolom Bukti atau referensi | Ketentuan P9; Penanganan Pengecualian baris 3 dan 4 | Fani |
| 3 | P10: kolom Bukti atau referensi berisi nama dan letak rekaman, bukan isi kredensial | Ketentuan P10 | Fani |
| 4 | Project Manager mengisi Bagian A | Peran, baris Project Manager | Fani |
| 5 | Head of Operation menolak serah terima G3 | Peran, baris Head of Operation; Penanganan Pengecualian baris 1 | Fani |
| 6 | Garis balik hypercare ke Bagian B dan keputusan G3 ulang pada form yang sama | Diagram (label garis dan keterangan Gambar 1); Penanganan Pengecualian baris 2 | Fani |
| 7 | Folder checklist G3 dan laporan penutupan sama dengan folder BAST | Rekaman dan Retensi, paragraf pembuka dan dua baris tabel | Fani |
| 8 | Service Delivery Manager sebagai pemilik semua rekaman form ini | Rekaman dan Retensi, paragraf pembuka dan kolom Lokasi dan pemilik | Fani |
| 9 | Tanpa layanan SOC, briefing serah terima (butir 11) cukup ke Lead NOC | Penanganan Pengecualian baris 5 | Fani |
| 10 | Service Delivery dan Project Management dipetakan ke Service Delivery Manager dan Project Manager | Definisi, SD dan PM; dipakai Peran dan Penanganan Pengecualian | Fani |

Label (USULAN) juga muncul di baris definisi "(USULAN)", di Kesimpulan, dan di paragraf pembuka bagian Peran; ketiganya bukan butir baru.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults.approved_by mengunci Samuel Kristanto Utomo / President Director, dengan pembalik "form operasional disetujui COO bila owner memutus". Spec memakai defaults | Owner |
| 2 | Masa simpan: form ini "Durasi kontrak + 5 tahun", sedangkan FRM-01, FRM-02, FRM-03, FRM-05 yang diarsipkan bersamanya di Bagian C memakai "Durasi kontrak + 3 tahun". Angka 5 tahun dipakai hanya untuk tiga rekaman form ini | Owner, dengan Fani |
| 3 | Checklist G3 di form ini 11 butir, di PRO-OPS-001 §8.2 delapan butir. Butir 2, 8, 10 tidak punya padanan. Form ini tidak diubah; PRO-OPS-001 perlu diselaraskan atau form diakui sebagai versi lengkap | Fani |
| 4 | Pemilik hypercare: form ini dan POL-OPS-001 menulis SD dan PM; PRO-OPS-001 §8.1 baris 10 dan POL-OPS-001 bagian 9.2 menulis Lead NOC. Form ini mengikuti sumbernya sendiri | Fani |
| 5 | "Head of Operation" belum punya pemegang (HR-ORG-01 K-10); hubungannya dengan VP Tech Operation and Services belum ditetapkan (K-09). Form ini memakai nama peran dari sumber | Owner, dengan Fani |
| 6 | Durasi hypercare tidak ada di form ini. POL-OPS-001 menulis 2 minggu berlabel USULAN. Tidak dipindah ke form ini | Fani |
| 7 | Sumber menulis "Operation berhak menolak" tanpa menunjuk peran. Spec menaruhnya pada Head of Operation (USULAN 5); POL-OPS-001 menulis wewenang "menolak serah terima G3" pada Head of Operation (audit baris 165) | Fani |
| 8 | "periode ditetapkan main contractor" (P3): periode pelaksanaan, periode layanan atau garansi, atau keduanya, tidak dirinci | Fani |
| 9 | Penanda tangan Pihak Pertama pada BAST (nama dan jabatan di SINUX) tidak ditunjuk perannya di sumber | Fani |
| 10 | Tempat lessons learned: sumber menulis "disetor ke knowledge base" dengan nomor jalur staging, rujukan internal yang dibuang. Tujuan penyimpanan selain folder Drive belum ditetapkan; baris Lessons learned di tabel Arsip dibiarkan tanpa lokasi | Owner, dengan Fani |
| 11 | Batas "generalist" untuk GLPI belum dirinci owner. Form ini hanya menyebut tiket generalist di luar form (Definisi, Ticketing system) | Owner |
| 12 | "24/7" ada di gambar sumber, tidak di teks Bagian B. Dibuang dari label simpul; SOP-04 menyebut 24 jam sehari tujuh hari seminggu (audit, bukan sumber form ini) | Fani |
| 13 | Bagian C tidak punya nomor gate. Dibiarkan | Fani |
| 14 | Rujukan "SNX-OPS-SOP-01 Bagian 6.5 dan 6.6" (P1) dicek ulang terhadap SOP-01 hasil render (state QUEUED saat ini) | Orkestrator |
| 15 | "ISO/ISMS Coordinator" sebagai pemeriksa di sumber digantikan Fani menurut defaults; peran ISMS Coordinator belum ditetapkan (HR-ORG-01 K-13) | Owner |

## Jawaban dua pertanyaan akhir

### Apa yang membuat teks ini terdengar buatan AI

Saya membaca ulang spec dan menemukan lima hal, lalu memperbaikinya:

| Temuan | Perbaikan |
|---|---|
| Kalimat meta di Ketentuan Pengisian: "Setiap ketentuan diberi nomor P. Bagian lain merujuk nomornya dan tidak mengulang uraiannya." Kalimat itu bicara tentang dokumen, bukan isi dokumen | Diganti "Bagian lain merujuk ketentuan di bawah dengan nomor P." |
| Pembuka Bagian A dan C identik: "Sel dibiarkan kosong sampai diisi dari dokumen proyek." Pengulangan pola yang sama di dua tempat | Bagian A: "Bagian A dipakai pada G2 dan diisi dari dokumen proyek." Bagian C: "Bagian C diisi dari dokumen proyek sesudah layanan diterima sebagai BAU." Tiap kalimat membawa fakta bagiannya |
| Baris Ruang Lingkup "Dikerjakan di proyek" menyatakan siapa membuat as-built dan runbook, yang tidak ada di sumber, dan terdengar menyempurnakan | Diganti "Tidak dibuat di form ini." |
| Kalimat tanpa pelaku di pembuka Bagian A dan C ("diisi dari dokumen proyek") | Dibuang di putaran perbaikan 1; pembuka kini hanya menyebut kapan bagian dipakai |
| Rumusan "Hasil yang dijaga: ..." di Tujuan dan "Butir berlabel (USULAN) perlu diputus pimpinan SINUX" di Kesimpulan terdengar baku | Dipertahankan: bentuknya diminta RUNBOOK §6a butir 4 dan kalimatnya memuat fakta (BAU hanya sesudah dua penerimaan; butir USULAN belum diputus), bukan pujian |
| Daftar tiga yang tampak dipaksakan | Dicek: "BAST, checklist, laporan penutupan" adalah tiga bagian nyata di sumber; peran di blok tanda tangan mengikuti sumber. Tidak ada daftar tiga yang dibuat untuk irama. Tidak ada tebal, kapital, atau tanda kutip untuk penekanan, tidak ada sinonim berganti (satu istilah: "checklist G3", "layanan", "pekerjaan" dengan definisi pembeda), tidak ada em-dash atau en-dash |

Kalimat tim dipertahankan apa adanya: kalimat pembuka BAST, kalimat penyerahan Pihak Pertama, klausul masa layanan, 11 kriteria Bagian B, dan label kolom Bagian C.

### Adakah fakta, angka, nama, atau tanggal tanpa sumber

Hasil pemeriksaan butir per butir terhadap spec:

| Butir di spec | Sumber |
|---|---|
| Nama dan jabatan di halaman approval | config/defaults.json (prepared_reviewed.OPS, approved_by); bukan dari sumber form |
| 5 tahun (retensi, diagram) | Sumber: "Durasi kontrak + 5 tahun" |
| Angka 11 butir, kode SNX-ISMS-REG-01, SNX-ISMS-FRM-01, SNX-ISMS-REG-04, SNX-OPS-FRM-05, FRM-07, FRM-09 | Sumber, Bagian B dan Arsip |
| SNX-OPS-FRM-01 sampai FRM-04 di Dokumen Terkait beserta judulnya | Sumber menyebut "FRM-01 sampai FRM-05"; judul dari config/checklist.json |
| SNX-OPS-SOP-01 Bagian 6.5 dan 6.6 | Sumber, Petunjuk pengisian; judul "SOP Project Management & Delivery" dari config/checklist.json |
| Klausul 8.5.5, 8.6, Annex A 5.8 | Sumber dan config/checklist.json; judul klausul adalah asumsi A5 |
| Definisi NOC, SOC, Jumphost, main contractor, BAU, baseline | Rumusan saya dari pemakaian di sumber atau HR-ORG-01 (A4); tidak memuat angka, nama, atau tanggal |
| Folder, pemilik rekaman, pengisi Bagian A, penolak G3, panah balik, Zammad, P9, P10, briefing ke Lead NOC saja, pemetaan SD dan PM ke jabatan | Tanpa sumber, berlabel (USULAN) |
| Tanggal | Tidak ada tanggal di spec. Tanggal efektif kosong; "13 Oktober 2026" (tanggal draft sumber) tidak dibawa |

Tidak ditemukan fakta, angka, nama, atau tanggal tanpa sumber yang tidak berlabel. Temuan dari pemeriksaan: baris "Dikerjakan di proyek" (sudah dibuang) dan judul klausul ISO yang saya terjemahkan sendiri (dicatat sebagai asumsi A5).

## Putaran perbaikan 1 (verifikator buta: FAIL, 1 blocking)

Blocking: baris 3 Penanganan Pengecualian membolehkan butir 3 utuh Tidak berlaku bila tidak ada layanan SOC. Sumber: "Semua aset masuk monitoring NOC (dan SIEM bila layanan SOC), alert sudah diuji" (Bagian B butir 3). Syarat SOC hanya untuk SIEM; P6 menghitung Tidak berlaku sebagai lolos, jadi layanan bisa masuk BAU tanpa bukti monitoring NOC.

| Perubahan | Lokasi di spec |
|---|---|
| P8 baru memuat batas: tanpa layanan SOC hanya unsur SIEM butir 3 yang tidak berlaku; monitoring NOC dan uji alert tetap diperiksa; butir 3 tidak boleh Tidak berlaku; butir 4 Tidak berlaku bila tidak ada layanan backup. Alasan jadi P9 (USULAN), kredensial jadi P10 (USULAN) | Ketentuan Pengisian; Bagian B paragraf pembuka merujuk P6, P7, P8 |
| Penanganan Pengecualian dipecah per kondisi: butir 3 (SIEM saja), butir 4, butir 11 | Penanganan Pengecualian baris 3, 4, 5 |

Butir 3 tidak dipecah menjadi sub-butir: 11 butir sumber tetap utuh dan bernomor sama (T1); batasnya cukup di P8.

Nonblocking yang ikut diperbaiki (qa/OPS-FRM-06.verify.r1.json, hanya dibaca):

| Nonblocking | Perbaikan |
|---|---|
| Pembuka Peran tanpa label untuk Bagian A | "Project Manager mencatat isi Bagian B dan C, dan Bagian A (USULAN)." |
| Butir 11 tanpa kasus tanpa layanan SOC | Baris 5 Penanganan Pengecualian, berlabel (USULAN 9) |
| Judul kolom "Lokasi (folder Drive)" dipakai untuk lessons learned | Judul menjadi "Lokasi" |
| Kalimat Rekaman janggal; "Drive" dan "Google Drive" bergantian | "Baru lokasi BAST original yang ditetapkan, yaitu Drive." Satu sebutan "Drive" |
| Pemetaan SD dan PM ke jabatan tanpa label | Definisi memakai rumusan yang sama dengan Peran dan diberi (USULAN 10) |
| Pasif tanpa pelaku di pembuka Bagian A dan C | Kalimat "diisi dari dokumen proyek" dibuang |
| "pimpinan SINUX" kabur | Definisi USULAN: "pemeriksa atau penyetuju dokumen"; Kesimpulan: "pemeriksa dokumen (Reviewed By)" |
| Zammad menggantikan "Zammad atau Service Hub" | Tidak diubah; sudah USULAN 1 dan open item 11, dipastikan saat ACC |

Uji ulang: render_sop.py berhasil; lint_doc.py generic: "pass": true, "fails": [], warn "15 butir (USULAN) menunggu ACC".

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil (15 label USULAN tetap; jumlah sama dengan bed1bb6).
### W10 kalimat dihapus atau dipindah
- "Aturan G3 ada di P6, P7, dan P8." (kalimat penunjuk; diganti instruksi "Isi kolom Status dengan Lolos, Belum, atau Tidak berlaku sesuai P6 sampai P8.")
- Definisi As-built: "Isinya tertulis di Bagian B butir 5." (penunjuk; diganti faktanya: topologi, IP address, versi, akses, dan ketergantungan vendor)
- Dokumen Terkait SNX-OPS-FRM-05: rujukan "(P2)" dihapus agar sel memuat satu rujukan.
- Dokumen Terkait SNX-OPS-FRM-01 sampai -05: "Diarsipkan bersama form ini (tabel Arsip, Bagian C)." dipendekkan menjadi "Ikut diarsipkan."; lokasinya tetap tertulis di tabel Arsip Bagian C.
- Dokumen Terkait FRM-07, FRM-09, ISMS-REG-01, ISMS-FRM-01, ISMS-REG-04: kata "Tempat" dibuang (mis. "Tempat parameter SLA (butir 9)." menjadi "Parameter SLA (butir 9).").
### W10 selisih angka
nihil (subst_diff kosong).
### W10 catatan
- Sebutan pihak luar: "pelanggan" (dokumen induk OPS).
- Ketentuan Pengisian P1, P2, P4, P5, P9, P10 ditulis sebagai kalimat perintah; P7 tidak lagi diawali nama peran (0 dari 23 butir instruksi diawali peran). "komersil" dibakukan menjadi "komersial".
- Label node diagram dibuat satu atau dua baris lebar (id, bentuk, edges tetap) agar gambar alur 17,7 cm dan Bagian A tetap mulai di halaman 9.
- Tabel isian (rincian deliverable, isu sisa A dan C, lessons learned) diberi min_row_cm 0,9; lebar kolom tabel Bagian B, Pengecualian, Rekaman, Acuan, dan Dokumen Terkait disetel ulang. Halaman tetap 14.
### W10 audit pointer
- .sections[2].blocks[0].table.rows[15][1]: lengkap; "Isinya tertulis di Bagian B butir 5" diganti isi Bagian B butir 5 (Bagian B tabel deliverable baris "Dokumen as-built": topologi, IP address, versi, akses, ketergantungan vendor), lima unsur sama persis; tidak berlabel USULAN.
