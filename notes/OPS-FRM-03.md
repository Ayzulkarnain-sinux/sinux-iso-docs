# Catatan penyusun OPS-FRM-03: Project Progress & Monitoring Report

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-FRM-03.json. Mode generic, aksi T1, wave W5, nomor SNX-OPS-FRM-03 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber, audit_class A. Process owner = "Project Manager" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). doc_type_cover "FORM".

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-03_Project_Progress_Monitoring_Report.docx (124151 byte) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR | 2026-10-13T06:09:02Z (get_file_metadata, dicek di sesi ini; cocok dengan prompt) | read_file_content (teks), download_file_content (docx didekode ke /tmp/pen-OPS-FRM-03/src/src.docx, python3 -I + python-docx: 12 tabel, 1 gambar word/media/rId21.png dibuka dan dibandingkan dengan deskripsi audit) |
| Kriteria penerimaan | prompt orkestrator + config/worklist.json baris OPS-FRM-03 | tidak diukur ulang | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001:2015 "8.5.1, 9.1.1" dan ISO/IEC 27001:2022 "5.8" |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md baris 1237 sampai 1430 (bagian 5 Catatan kualitas dan celah) | salinan audit 13 Okt 2026 | DATA, dibandingkan dengan docx asli |
| Pendukung (bahan) | SNX-OPS-SOP-01 Bagian 6.2 butir 3 dan 6.4 (audit baris 3694, 3706 sampai 3711); SNX-OPS-FRM-01 sheet Daftar C2:C5 dan Milestone (audit baris 841, 909 sampai 913); SNX-OPS-FRM-04 Go-gate (audit baris 1458) | salinan audit 13 sampai 14 Okt | Dibaca dari context/audit (DATA), bukan dari Drive terbaru; bisa basi bila tim mengubahnya |

Catatan teknis: read_file_content menaruh petunjuk "[deviasi dari baseline dalam hari]" dan sejenisnya di kolom Status pada tabel Ringkasan status. Tabel docx asli (python-docx, tabel indeks 3) menaruhnya di kolom "Keterangan singkat", dan audit benar. Spec mengikuti docx asli.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Project Manager | "Pemilik dokumen" / "Project Manager" (tabel Atribut, baris data ke-7) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |
| Arti tiga status laporan | "Panduan status: Hijau = sesuai baseline; Kuning = deviasi bisa dipulihkan tanpa mengubah baseline; Merah = butuh keputusan pelanggan atau COO." (di bawah tabel Ringkasan status) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |
| Masa simpan record | "Masa simpan record" / "Durasi kontrak + 3 tahun" (tabel Atribut, baris data ke-11) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Dipakai di spec |
|---|---|---|---|
| 1 | Pemakai, penerima, frekuensi, rujukan SOP | "Template ini dipakai Project Manager untuk laporan progres mingguan (atau sesuai rencana komunikasi proyek) kepada pelanggan dan COO, sesuai SNX-OPS-SOP-01 Bagian 6.4." | Tujuan |
| 2 | Petunjuk kurung siku | "Teks dalam kurung siku adalah petunjuk dan dihapus saat diisi." | Petunjuk Pengisian butir 1 |
| 3 | Nama berkas PDF | "Simpan sebagai PDF dengan nama FRM-03\_\<KodeProyek\>\_\<YYYY-MM-DD\>.pdf di folder proyek." | Petunjuk Pengisian butir 3, Rekaman |
| 4 | Klasifikasi dan pembagian ke pelanggan | "RESTRICTED (Internal), dibagikan ke pelanggan terkait" (Bagian 1, baris Klasifikasi) | Isi Laporan, Identitas laporan |
| 5 | Eskalasi status Merah | Diagram rId21: kotak "Eskalasi" dengan sub-label "Head of Operation, COO"; kotak "Ada status Merah?" bercabang "ya" ke Eskalasi dan "tidak" ke Review | Alur Pengisian, Peran |
| 6 | Pemeriksa sebelum kirim | Diagram rId21: "Review Service Delivery Manager" / "konsistensi dan kelengkapan"; Bagian 10: "Diperiksa (Service Delivery Manager)" | Alur Pengisian, Peran |
| 7 | Sumber data laporan | Diagram rId21: "Tarik data proyek" / "FRM-01, FRM-02, FRM-04"; "[kode proyek, sama dengan SNX-OPS-FRM-01]"; "[persen, dari SNX-OPS-FRM-01]"; "ID (dari FRM-02)"; "Nomor CR (dari FRM-04)" | Lingkup, Alur, Isi Laporan |
| 8 | Acuan klausul | "Klausul 8.5.1, 9.1.1" dan "Klausul atau kontrol Annex A 5.8" | Rekaman dan Acuan ISO |
| 9 | Ambang eskalasi ke COO di SOP induk | "Deviasi jadwal lebih dari 1 minggu dari baseline, atau isu yang menyentuh biaya, dieskalasi ke COO." (SNX-OPS-SOP-01 butir 6.4.5, audit baris 3711) | USULAN 1 |
| 10 | Nilai status milestone di FRM-01 | "Milestone | F5:F24 | Daftar!$C$2:$C$5 | Sesuai rencana, Berisiko, Terlambat, Selesai" (audit baris 841) | Isi Laporan, Progres milestone |
| 11 | Rencana komunikasi | "Susun rencana komunikasi: kanal resmi (email dan grup WhatsApp proyek), frekuensi laporan, dan matriks eskalasi pelanggan." (SNX-OPS-SOP-01 butir 6.2.3, audit baris 3694) | Istilah |
| 12 | Go-gate | "Kolom Go-gate otomatis bernilai `CEK` bila backup, rollback, atau approval belum lengkap" (SNX-OPS-FRM-04, audit baris 1458) | Istilah |
| 13 | Deviasi jadwal dalam hari | "Deviasi = tanggal aktual atau perkiraan dikurangi rencana (hari). Positif berarti terlambat." (SNX-OPS-FRM-01 sheet Milestone A2, audit baris 911) | dasar petunjuk "[deviasi dari baseline dalam hari]" yang dipertahankan |

## 3. Hasil uji

Perintah render: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-FRM-03.json /tmp/pen-OPS-FRM-03/OPS-FRM-03.docx` (berhasil, tanpa galat).

Perintah lint: `python3 -I tools/lint_doc.py /tmp/pen-OPS-FRM-03/OPS-FRM-03.docx generic`

Hasil terakhir: `"pass": true`, `"fails": []`, `"warns": ["1 butir (USULAN) menunggu ACC"]`.

Pemeriksaan tambahan atas docx hasil: "Direktur (COO)" muncul sekali (paragraf Tujuan, sebutan pertama di badan), sesudahnya "COO"; tidak ada em-dash maupun en-dash; tidak ada nama Direktur Utama di badan dokumen. Konversi PDF lewat soffice berhasil (10 halaman), pratinjau halaman dilihat: sampul, Identity, Revision, Approval, TOC, diagram TB, tabel isian terbaca. Tabel Peran, Isian 1 (judul tabel di dasar halaman 7), dan Distribusi terpotong antarhalaman; itu efek aliran halaman renderer dan tidak diubah.

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Petunjuk pengisian (kalimat pertama) + audit | Pengecualian lingkup: KPI layanan (audit: "KPI: tidak ada KPI di dokumen ini"); pencatatan rinci tetap di FRM-01, FRM-02, FRM-04 |
| 2 Istilah | Panduan status sumber; SOP-01, FRM-01, FRM-04 | Hanya arti istilah. Aturan pemakaian ada di bagian 4 dan di Isi Laporan; kalimat panduan status disalin sekali (bagian 2) |
| 3 Peran | Tabel peran audit (bagian 4 audit) | Lima peran dari sumber. "ISO/ISMS Coordinator" (pemeriksa di Pengesahan sumber) tidak dimasukkan karena blok Pengesahan diganti blok Approval template; "Divisi Operation" di riwayat revisi sumber juga diganti oleh template |
| 4 Petunjuk Pengisian | Petunjuk pengisian sumber | Tiga butir |
| 5 Alur Pengisian | Diagram rId21 | 7 simpul, rankdir TB, label simpul sumber dipertahankan kecuali dua simpul (lihat bagian 5 butir 6) |
| 6 Isi Laporan | Bagian 1 sampai 10 sumber | Judul h2 sama dengan sumber tanpa nomor "Bagian n" (renderer sudah menomori 6.1 sampai 6.10, dan "Bagian n" bentrok dengan nomor bagian dokumen). Jumlah baris tabel sama dengan sumber. Petunjuk kurung siku dipertahankan (suara tim, T1); sel data kosong; nol baris contoh |
| 7 Dokumen Terkait | Kode yang disebut di badan | SOP-01, SOP-02, FRM-01, FRM-02, FRM-04. Judul dari salinan audit; bila tim mengganti judul, selaraskan |
| 8 Rekaman dan Acuan ISO | Atribut sumber | Retensi verbatim; acuan klausul sesuai prompt |

Blok "Pengesahan" sumber tidak dipertahankan di badan: tiga penanda tangan dokumen kini di blok Approval halaman depan (prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo, persis sesuai data baris). Tabel "Distribusi dan persetujuan laporan" (isian per laporan: Disusun, Diperiksa, Diterima) tetap, kosong.

Penyesuaian tulisan yang disengaja: kode dokumen ditulis lengkap (SNX-OPS-FRM-01, bukan FRM-01) agar satu istilah untuk satu dokumen; pola nama berkas "FRM-03_<KodeProyek>_<YYYY-MM-DD>.pdf" dibiarkan seperti sumber karena itu nama berkas, bukan rujukan dokumen. Acuan 27001 ditulis "Kontrol Annex A 5.8" (bukan "Klausul atau kontrol"), karena 5.8 adalah kontrol Annex A; sama dengan keputusan di notes OPS-FRM-01.

## 5. Penanganan cacat context/audit (bagian 5, fileId 147U5gBLjtLKHau5cQbLUym8iInh2b_RR)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Seluruh isian placeholder kosong atau petunjuk kurung siku | Sel data kosong, tanpa baris contoh. Petunjuk kurung siku dipertahankan sebagai suara tim (T1) dan Petunjuk Pengisian butir 1 menyuruh menghapusnya saat diisi |
| 2 | Tiga warna status tanpa dropdown, tanpa ambang angka deviasi | Docx tidak punya dropdown: Isi Laporan, Ringkasan status menyuruh menulis salah satu dari Hijau, Kuning, Merah; arti warna di Istilah. Ambang angka hanya untuk Jadwal, berlabel (USULAN), memakai angka SOP-01 butir 6.4.5 (1 minggu). Ambang untuk Scope, Mutu, Risiko, Keamanan informasi, dan status Keseluruhan tidak ada sumbernya: open item 1 |
| 3 | Hanya 4, 3, 3, 2 baris; tidak dinyatakan boleh ditambah | Jumlah baris tetap seperti sumber; Petunjuk Pengisian butir 2 menyatakan baris boleh ditambah (versi polos, asumsi 3) |
| 4 | Kolom Status milestone tanpa nilai; FRM-01 memakai Sesuai rencana, Berisiko, Terlambat, Selesai; rujukan SOP-01 6.4 dan FRM-04 cocok | Diperbaiki: paragraf di atas tabel Progres milestone menyebut nilai FRM-01. Rujukan SOP-01 Bagian 6.4 dan FRM-04 dipertahankan |
| 5 | Klasifikasi RESTRICTED (Internal) tetapi dibagikan ke pelanggan | Dipertahankan verbatim di Identitas laporan karena itu substansi tim dan label wajib mengikuti sumber. Dicatat sebagai open item 2 |
| 6 | Gambar menulis "PDF, mingguan", teks menulis "mingguan (atau sesuai rencana komunikasi proyek)" | Diperbaiki: simpul diagram menjadi "Kirim PDF ke pelanggan dan COO" tanpa "mingguan"; frekuensi hanya disebut sekali, di Tujuan, dengan kedua bentuk. Simpul "Arsip di folder proyek" tidak lagi memuat pola nama berkas (pola ada di Petunjuk Pengisian butir 3). Legenda sumber (kotak biru, kotak oranye, garis putus-putus) dihapus karena renderer tidak menggambar warna maupun garis putus-putus; arti jalurnya ditulis di keterangan Gambar 1 |
| 7 | Dua baris revisi 00 bertanggal sama; frasa "keselarasan RTO dan target pulih" tidak relevan | Diperbaiki: satu baris revisi 00 dari revision_desc data baris; frasa RTO dibuang |
| 8 | Bagian 10 dan Pengesahan tanpa nama, tanda tangan, tanggal | Bagian 10 dibiarkan kosong (diisi per laporan). Tanda tangan dan tanggal blok Approval kosong (batas keras 3); nama diisi dari data baris |

## Asumsi

1. Pelaku "mengeskalasi", "mengirim", dan "menyimpan PDF" ditulis Project Manager. Diagram sumber tanpa lajur pelaku; dasarnya "Template ini dipakai Project Manager untuk laporan ... kepada pelanggan dan COO" dan peran Project Manager sebagai penyusun di audit (bagian 4).
2. Pemilik rekaman laporan = Project Manager (pemilik dokumen); lokasi = folder proyek (sumber).
3. "Project Manager menambah baris tabel bila isi laporan melebihi baris yang tersedia": kalimat petunjuk pemakaian, bukan angka; sumber diam.
4. Lingkup "proyek yang rencananya tercatat di SNX-OPS-FRM-01" ditafsir dari "[kode proyek, sama dengan SNX-OPS-FRM-01]" dan "[persen, dari SNX-OPS-FRM-01]".
5. Arti Baseline, Milestone, dan Go-gate disusun dari FRM-01, SOP-01 butir 6.4, dan FRM-04; sumber FRM-03 memakai ketiganya tanpa definisi.
6. "[urutan laporan, misalnya 05]" dipertahankan karena petunjuk format tim, bukan baris contoh.
7. Judul dokumen terkait (bagian Dokumen Terkait) diambil dari salinan audit; bukan hasil pembacaan Drive terbaru.
8. Kolom "Bukti atau referensi" memakai "tiket Zammad" sesuai kata owner 14 Okt (config/defaults.json ticketing) menggantikan "tiket" di sumber.

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Deviasi jadwal lebih dari 1 minggu dari baseline = status Merah (angka dari SOP-01 butir 6.4.5, dipakai pada ambang status laporan; sumber FRM-03 tanpa angka) | Isi Laporan, Ringkasan status (berlabel "(USULAN)") | Fani |
| 2 | Tiga penanda tangan: prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo, menggantikan Disusun "Project Manager", Diperiksa "ISO/ISMS Coordinator", Disetujui "COO, Amirull Yusuf Zulkarnain" di sumber (config/defaults.json D2; pembalik: form operasional disetujui COO bila owner memutus) | Blok Approval halaman depan | owner |
| 3 | Kolom Bukti memakai "tiket Zammad" | Isi Laporan, Pekerjaan periode ini | owner |
| 4 | Pelaku Project Manager untuk eskalasi, pengiriman, penyimpanan PDF, dan kepemilikan rekaman | Peran, Rekaman | Fani |
| 5 | Arti Baseline, Milestone, dan Go-gate hasil tafsir lintas dokumen | Istilah | Fani |

## Open items

1. Aturan menentukan status Keseluruhan dan ambang Kuning dan Merah untuk Scope, Mutu, Risiko dan isu, Keamanan informasi tidak ada di sumber. Penentu: Fani.
2. Klasifikasi RESTRICTED (Internal) dengan pembagian ke pelanggan: sumber tidak menyebut label atau persetujuan untuk salinan yang keluar. Penentu: owner atau Fani.
3. Hubungan eskalasi status Merah (Head of Operation dan COO menurut diagram; "butuh keputusan pelanggan atau COO" menurut panduan status) dengan SOP-01 butir 6.4.3 (risiko Tinggi atau Kritis ke Head of Operation) dan 6.4.5 (deviasi lebih dari 1 minggu ke COO) tidak dinyatakan. Penentu: Fani.
4. Proyek mana yang wajib memakai FRM-03 (semua proyek atau yang punya workbook SNX-OPS-FRM-01) tidak dinyatakan. Penentu: Fani.
5. Batas sistem tiket: audit FRM-04 menulis "CR juga dibuat di Service Hub" (GLPI), sedangkan data owner menyebut Zammad untuk Ops. Kolom Bukti sudah ditulis "tiket Zammad"; konfirmasi untuk tiket dan CR. Penentu: owner.
6. Penyetuju dokumen: sumber menulis COO, Amirull Yusuf Zulkarnain; data baris menetapkan Samuel Kristanto Utomo / President Director. Konfirmasi pembalik D2. Penentu: owner.
7. Nilai status milestone diambil dari FRM-01 sheet Daftar (salinan audit). Bila tim mengubah daftar itu, selaraskan paragraf di Progres milestone. Penentu: Fani.
8. Kalimat perintah di sumber ("Teks dalam kurung siku adalah petunjuk dan dihapus saat diisi", "Simpan sebagai PDF ...") adalah isi form untuk Project Manager, bukan perintah ke penyusun. Dipakai sebagai isi dokumen, tidak dijalankan. Tidak ada kalimat perintah lain yang menyasar penyusun.
9. Tata letak: tabel Peran, judul tabel Identitas laporan, dan tabel Distribusi terpotong antarhalaman di pratinjau LibreOffice. Efek renderer; tidak diubah (di luar batas tulis).

## 6. Pemeriksaan mutu (dua pertanyaan)

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI? Temuan pada draf pertama dan perbaikannya:

| Temuan | Perbaikan |
|---|---|
| Judul h2 "Isian 1." sampai "Isian 10." bertumpuk dengan nomor otomatis 6.1 sampai 6.10 (tampak seperti penomoran ganda) | Awalan "Isian n." dibuang; tidak ada kalimat yang merujuk nomor isian |
| Tujuan memuat daftar enam isi laporan yang bisa tertempel di laporan proyek mana pun | Dipertahankan hanya karena daftar itu persis struktur form sumber (status, milestone, pekerjaan, risiko dan isu, change request, keputusan); tidak ada klaim manfaat |
| Kalimat label "USULAN" bertele-tele di dalam kurung | Dipecah: "(USULAN). Ambang ini sama dengan ambang eskalasi ke COO di SNX-OPS-SOP-01 Bagian 6.4." |
| Benda diberi kata kerja manusia | Dicek: tidak ada ("Form ini dipakai", "Laporan memuat" bersifat deskriptif, pelaku tindakan selalu peran) |
| Kelompok tiga dipaksakan | Dicek: "FRM-01, FRM-02, FRM-04", "Hijau, Kuning, Merah", tiga butir petunjuk, tiga baris distribusi semuanya dari sumber; tidak ada kelompok tiga tambahan |
| Frasa pengisi, penutup positif, tebal, kapital, kutip untuk penekanan, em-dash | Nol temuan (lint gaya pass; em-dash dan en-dash dicari di teks hasil: tidak ada) |

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir | Sumber atau status |
|---|---|
| "1 minggu" pada status Jadwal | Angka SOP-01 butir 6.4.5; dipakai di luar lingkup asalnya (eskalasi), jadi berlabel (USULAN) |
| "Retensi Durasi kontrak + 3 tahun" | Sumber, Atribut |
| Nama Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo | Data baris dan config/defaults.json |
| "tiket Zammad" | Kata owner 14 Okt di config/defaults.json |
| "Bagian 6.2 butir 3" SOP-01 | Salinan audit baris 3694 |
| Nama Amirull Yusuf Zulkarnain | Tidak dipakai di badan; hanya muncul di catatan ini sebagai isi sumber |
| Tanggal | Tidak ada tanggal di dokumen hasil (tanggal draft 13 Oktober 2026 di sumber tidak dibawa; tanggal efektif kosong) |
| Pelaku Project Manager, arti istilah, lingkup | Tafsir, bukan fakta baru; dicatat di Asumsi 1, 2, 4, 5 dan USULAN 4 dan 5, tanpa angka atau nama baru |

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil (satu label USULAN pada ambang Jadwal 1 minggu dipertahankan dan dipindah ke akhir butir).
### W10 kalimat dihapus atau dipindah
- "Arti tiap warna ada di bagian Istilah." (kalimat penunjuk; diganti "Isi kolom Status dengan Hijau, Kuning, atau Merah sesuai arti di tabel Istilah.")
- "Ambang ini sama dengan ambang eskalasi ke COO di SNX-OPS-SOP-01 Bagian 6.4." digabung ke kalimat ambang Jadwal, label (USULAN) di akhir butir; isi tidak berubah.
### W10 selisih angka
nihil (subst_diff kosong).
### W10 catatan
- Sebutan pihak luar: "pelanggan" (sama dengan dokumen induk OPS).
- Petunjuk Pengisian ditulis sebagai kalimat perintah (0 dari 3 butir diawali nama peran).
- Label node diagram dibuat satu baris agar gambar alur lebih pendek (19,0 cm menjadi 17,1 cm) dan bagian Isi Laporan tetap mulai di halaman 7; id, bentuk, dan edges tidak berubah.
- Tabel isian bagian 6 diberi min_row_cm 0,9 agar cukup untuk tulisan tangan; jumlah halaman tetap 10.

### W10 audit cakupan label
- .sections[5].blocks[4].p: diperbaiki (dipisah lagi; kesamaan dengan ambang eskalasi COO tanpa label)
