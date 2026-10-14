# Catatan penyusun ISMS-FRM-02: Security Incident & Investigation Records

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-FRM-02.patch.json. Mode xlsx, aksi T1, nomor SNX-ISMS-FRM-02 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber, audit_class B, wave W5. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-FRM-02.xlsx specs/ISMS-FRM-02.patch.json /tmp/pen-ISMS-FRM-02/out.xlsx` hasilnya `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), Register 5 data validation + 2 rentang conditional formatting + 453 rumus (151 baris x 3 kolom N, O, P), Chain of Custody 2 data validation.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-FRM-02_Security_Incident_Investigation_Records.xlsx (151668 byte) | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 | 2026-10-13T06:09:30Z (get_file_metadata hari ini, cocok dengan prompt; fileSize 151668 sama dengan jumlah byte hasil dekode) | download_file_content (hasil besar tersimpan ke berkas, didekode ke /tmp/src/ISMS-FRM-02.xlsx, kerja di /tmp/pen-ISMS-FRM-02/); semua 6 sheet dibaca dengan openpyxl; gambar image1.png dibuka |
| Kriteria penerimaan | prompt penyusun, baris data | | Description hanya nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001:2015 "10.2" dan ISO/IEC 27001:2022 "5.25, 5.26, 5.27, 5.28" |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md, bagian isms/SNX-ISMS-FRM-02 (baris 215 sampai 445) | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir bagian 5 dicocokkan ulang ke berkas xlsx |
| Pendukung | bagian SNX-ISMS-SOP-01 di berkas audit yang sama (baris 2278 sampai 2360); specs/HR-ORG-01.json | salinan audit; spec DONE | Hanya untuk mencocokkan rujukan severity, titik awal 3 x 24 jam, dan nama peran |

Sheet di sumber: Kontrol Dokumen, Alur Proses, Daftar, Register, Investigasi, Chain of Custody. Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Notifikasi PDP: bila data pribadi terlibat, kolom menandai kajian dengan batas 3 x 24 jam dari waktu deteksi; keputusan ada di COO dan Legal | Kontrol Dokumen B20: "Bila data pribadi terlibat, kolom Notifikasi PDP otomatis menandai kewajiban pemberitahuan maksimal 3 x 24 jam (keputusan COO dan Legal)." Register P5: `=IF(J5="Ya","WAJIB DIKAJI, maksimal "&TEXT(B5+3,"dd-mmm hh:mm"),IF(J5="","","Tidak"))` | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |
| 2 | Insiden P1 dan P2 memakai lembar investigasi per insiden; setiap bukti dicatat di Chain of Custody dengan hash SHA-256 yang diverifikasi tiap perpindahan | Kontrol Dokumen B21: "Untuk insiden P1 dan P2, salin sheet Investigasi per insiden dan isi Chain of Custody untuk setiap bukti." Chain of Custody A2: "Satu baris per perpindahan atau tindakan atas bukti. Hash SHA-256 dihitung saat pengumpulan dan diverifikasi setiap perpindahan." | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |
| 3 | Pemilik dokumen Lead SOC; masa simpan 5 tahun; acuan ISO 9001 klausul 10.2 dan Annex A 5.25 sampai 5.28 | Kontrol Dokumen B10: "Lead SOC"; B14: "5 tahun"; B12: "Klausul 10.2"; B13: "Klausul atau kontrol Annex A 5.25, 5.26, 5.27, 5.28" | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |

Fakta lain dari berkas yang sama: Kontrol Dokumen B15 "Register insiden keamanan informasi, catatan investigasi, dan chain of custody bukti sesuai SNX-ISMS-SOP-01."; B9 "RESTRICTED (Internal)"; Register N5 `=IF(OR(B5="",L5=""),"",ROUND((L5-B5)*24,1))` dan O5 `=IF(OR(B5="",M5=""),"",ROUND((M5-B5)*24,1))`; Daftar kolom B "P1", "P2", "P3", "P4"; Register A4 "ID insiden" dengan Cara pakai B18 "nomor SIR-YYYY-NNN". Rujukan severity di audit SOP-01 (DATA): "2. Event yang terkonfirmasi menjadi insiden dan diberi severity:" disusul tabel P1 sampai P4 (Bagian 8 butir 2 di sumber SOP-01).

## 2. Isi patch (yang berubah dan alasannya)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Register baris 5 (clear_rows) | SIR-2026-001, data CONTOH dengan placeholder "[pelapor]", "[pelanggan]" | Dikosongkan; rumus N, O, P, validasi, dan format bersyarat tetap | Sumber V5 "CONTOH" dan A2 "Baris biru muda = CONTOH."; aturan W5 "clear CONTOH" |
| Register!A2 | "Baris biru muda = CONTOH. Kolom abu-abu dihitung otomatis." | "Kolom abu-abu dihitung otomatis." | Baris CONTOH sudah tidak ada; alat menolak teks CONTOH di luar Kontrol Dokumen |
| Kontrol Dokumen B26 (clear_rows) | Legenda "Baris CONTOH: hapus atau timpa saat dipakai" | Dikosongkan | Tidak ada baris contoh yang perlu dihapus atau ditimpa; efek warna kotak, lihat Open item 2 |
| Kontrol Dokumen baris 32 (clear_rows) | Revisi 00 kedua: "Review bahasa dan konsistensi: ... keselarasan RTO dan target pulih" | Dikosongkan | Cacat audit: baris rev 00 ganda di tanggal yang sama; frasa RTO tidak punya isi di form. USULAN 7 |
| Kontrol Dokumen!C31 | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| Kontrol Dokumen!B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi 00, status Draft |
| Kontrol Dokumen!B11 dan B38 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | Data baris (approval.approved) dan config/defaults.json approved_by. USULAN 1 |
| Kontrol Dokumen!B36 | "Lead SOC" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | Data baris (approval.prepared). USULAN 2 |
| Kontrol Dokumen!B37 | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | Data baris (approval.reviewed). USULAN 2 |
| Kontrol Dokumen!B13 | "Klausul atau kontrol Annex A 5.25, 5.26, 5.27, 5.28" | "Annex A 5.25, 5.26, 5.27, 5.28" | Kata "Klausul atau kontrol" menyisakan dua kemungkinan padahal angkanya kontrol Annex A |
| Kontrol Dokumen!B15 | "... chain of custody bukti sesuai SNX-ISMS-SOP-01." | "Register insiden keamanan informasi, catatan investigasi, dan chain of custody bukti. Prosedur dan definisi severity P1 sampai P4 ada di SNX-ISMS-SOP-01." | Cacat audit: definisi severity tidak ada di form. USULAN 3 |
| Kontrol Dokumen!B19 | "Waktu containment dan pemulihan dihitung otomatis dalam jam dari waktu deteksi." | "Jam ke containment dan ke pulih dihitung otomatis dari waktu deteksi, 1 desimal." | Yang dihitung otomatis adalah kolom N dan O (jam), bukan Waktu containment dan Waktu pulih (kolom L dan M, diisi manual); ROUND(...,1) menjelaskan 0.75 jam tampil 0.8. USULAN 5 |
| Kontrol Dokumen!B20 | "... menandai kewajiban pemberitahuan maksimal 3 x 24 jam (keputusan COO dan Legal)." | "Bila data pribadi terlibat, kolom Notifikasi PDP menandai wajib dikaji dengan batas 3 x 24 jam dari waktu deteksi. Direktur (COO) dan Legal memutuskan." | Rumus P menulis "WAJIB DIKAJI", bukan kewajiban memberi tahu, dan batasnya dihitung dari waktu deteksi. Sebutan pertama COO di badan dokumen = "Direktur (COO)" (data_conflicts). USULAN 4 |
| Kontrol Dokumen!B22 | "Laporan insiden ke pelanggan memakai format beku SKILL_ir-report." | "Laporan insiden ke pelanggan memakai format laporan insiden baku." | RUNBOOK §0 butir 6: rujukan SKILL_ dibuang; tidak ada nomor dokumen SNX yang setara. USULAN 6 |
| B4, B5, B9, B10, B12, B14 | nilai sama | nilai sama (di-set ulang agar medan template tertulis eksplisit) | Nomor, Judul, Klasifikasi, Pemilik, Acuan 9001, Masa simpan |

Tidak diubah: tanggal draft "13 Oktober 2026" (B7, B31) dan "Ditetapkan saat pengesahan" (B8) adalah isi sumber. Kolom Tanda tangan dan Tanggal di blok Pengesahan (C36 sampai D38) tetap kosong. Status "Menunggu" (E31) dan "Divisi Operation" (D31) tetap. Cara pakai B18 dan B21 tetap. Rumus tidak diubah.

Panjang teks B15, B19, B20 dibatasi karena alat patch tidak mengubah tinggi baris (B19 satu baris, B15 dan B20 dua baris). Hasilnya diperiksa dengan render soffice ke PDF: ketiganya tidak terpotong.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah)

| # | Cacat di audit | Penanganan | Alasan bila tidak diperbaiki |
|---|---|---|---|
| 1 | Hanya 1 baris CONTOH (V5, A2) dengan placeholder; bertanggal 2026-11-03, setelah tanggal draft 13 Oktober 2026 | Diperbaiki: baris 5 dikosongkan, A2 dan legenda B26 dibersihkan | |
| 2 | Definisi severity, SLA respons, dan RTO tidak ada di form | Sebagian: B15 menunjuk SNX-ISMS-SOP-01 untuk definisi severity (USULAN 3). SLA respons tidak disalin ke form | Angka Ack (15 menit, 30 menit, 2 jam kerja, 1 hari kerja) milik SOP-01; menyalinnya membuat dua sumber kebenaran. RTO tidak ada di SOP-01; mengarang target dilarang. USULAN 10 |
| 3 | Masa simpan 5 tahun berbeda dari FRM-01 dan REG-04 (3 tahun), REG-01 sampai REG-03 dan SOA-01 (berlaku sampai digantikan), FRM-03 (durasi kontrak + 3 tahun) | Tidak diubah | 5 tahun adalah isi sumber dan cocok dengan tabel record SOP-01 (baris "Security Incident & Investigation Records" dengan nomor SNX-ISMS-FRM-02 dan masa simpan 5 tahun). Selisih antardokumen bukan cacat satu form. Open item 8 |
| 4 | Notifikasi PDP: hitung dari waktu deteksi (+3 hari), SOP-01 "sejak diketahui"; tidak ada kolom waktu notifikasi aktual; dasar hukum tidak disebut | B20 diperjelas (apa yang dilakukan kolom, siapa memutuskan). Rumus tidak diubah | Titik awal yang benar adalah keputusan Legal, bukan penyusun. USULAN 8 dan 9; Open item 9 |
| 5 | Sheet Investigasi hanya label, Chain of Custody hanya header | Tidak ada cacat | Form kosong adalah bentuk yang benar untuk T1; baris contoh dilarang |
| 6 | "SKILL_ir-report" bernama SKILL_; "RCA-2026-002" tidak punya dokumen bernomor itu | B22 dibersihkan; RCA-2026-002 hilang bersama baris CONTOH | Nomor SNX untuk format laporan pelanggan tidak ada. USULAN 6; Open item 4 |
| 7 | SoA menautkan FRM-02 untuk 5.25 dan 5.28, tidak untuk 5.26 dan 5.27 | Tidak diperbaiki | SNX-ISMS-SOA-01 milik konsultan dan di luar batas tulis. USULAN 11 |
| 8 | Contoh ISR-002 cocok dengan REG-02; severity insiden dan level risiko dua skala berbeda | Tidak ada cacat; contoh sudah dihapus | |
| 9 | Jam ke containment 0.8 dan pulih 5.8 tidak persis (0.75 dan 5.75) | Teks B19 menyebut 1 desimal; rumus tidak diubah | ROUND(...,1) bekerja sesuai rancangan. USULAN 5 |
| 10 | Pengesahan kosong; revisi 00 tercatat dua kali | Baris 32 dikosongkan; tanda tangan dan tanggal tetap kosong | Tanda tangan dan tanggal efektif adalah batas keras RUNBOOK §0 butir 3 |

Cek mesin sekali pakai (skrip openpyxl tidak disimpan): rumus N, O, P baris 5 sampai 155 sama dengan pola baris 5 (0 menyimpang); setelah patch tidak ada sel non-rumus berisi di baris 5; seluruh teks keluaran lolos pola FORBIDDEN dan STYLE tools/lint_doc.py (0 temuan) dan bebas em-dash dan en-dash.

## 4. Asumsi

1. Gambar "Alur Proses" (image1.png) dibuka dan sejalan dengan sheet lain: tujuh kotak, dua keputusan ("P1 atau P2?", "Data pribadi terlibat?"), dua cabang oranye. Gambar tidak memuat nama orang, SKILL_, atau nomor yang salah. Alat patch tidak mengedit gambar; lihat Open item 1.
2. Pemilik dokumen tetap "Lead SOC" karena sumber menulisnya sebagai peran (aturan process_owner: ikuti "Pemilik dokumen" di sumber, tanpa nama). Kolom "Disusun oleh" memuat Erik Dwi Yanto sesuai data baris; pemilik dan penyusun tidak harus orang yang sama.
3. Tanggal draft dan tanggal revisi 13 Oktober 2026 dibiarkan karena berasal dari sumber (modifiedTime 2026-10-13T06:09:30Z cocok).
4. Kalimat perintah di sumber (Cara pakai 1 sampai 5, legenda "Sel rumus: jangan diubah", "salin sheet ini per insiden P1 dan P2") adalah isi form untuk pengguna, bukan arahan ke penyusun. Tidak dijalankan sebagai instruksi; yang masih berlaku tetap dipertahankan. Tidak ada kalimat di sumber yang ditujukan ke penyusun atau alat.
5. Peran di sheet dicocokkan ke specs/HR-ORG-01.json: "Lead SOC" ada di Struktur Divisi Operation (USULAN, belum ada pemegang, K-10), nama dipakai apa adanya. "Incident Commander" dan "Tim investigasi" tidak ada di HR-ORG-01 karena keduanya penugasan per insiden, bukan jabatan; terdekat Lead SOC, tetapi sel isian tidak diubah karena sumber memakainya sebagai isian per insiden. "ISO/ISMS Coordinator" di sumber sepadan dengan "ISMS Coordinator" di HR-ORG-01 (Belum ditetapkan, K-13); sebutannya hilang dari berkas karena B37 kini diisi Fani sesuai data baris.
6. Sebutan pertama COO di badan dokumen ada di B20 ("Direktur (COO)"). Samuel tidak disebut di badan dokumen, hanya di blok pengesahan ("President Director"). Teks pada gambar "COO dan Legal" tidak dapat diubah dari patch.

## USULAN

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: Samuel Kristanto Utomo / President Director (default D2) menggantikan "COO, Amirull Yusuf Zulkarnain" di Kontrol Dokumen B11 dan B38. Defaults memberi pembalik "form operasional disetujui COO bila owner memutuskan". | owner |
| 2 | Disusun oleh Erik Dwi Yanto / Technical/Operation Engineer L1 dan Diperiksa oleh Fani Fatullah / VP Tech Operation and Services (defaults) menggantikan "Lead SOC" dan "ISO/ISMS Coordinator" di B36 dan B37. | owner |
| 3 | Kalimat B15 yang menunjuk SNX-ISMS-SOP-01 sebagai tempat definisi severity P1 sampai P4. Dasarnya salinan audit SOP-01 (Bagian 8 butir 2); SOP-01 belum punya spec di repo ini dan belum dibaca langsung dari Drive. | Fani |
| 4 | Kalimat B20 yang menulis "menandai wajib dikaji" dan "dari waktu deteksi" menggantikan "menandai kewajiban pemberitahuan". Isinya hanya menjelaskan rumus P, tetapi kalimatnya tambahan penyusun. | Legal |
| 5 | Kalimat B19 yang menyebut hasil jam dibulatkan 1 desimal. Isinya menjelaskan ROUND(...,1) yang sudah ada. | Fani |
| 6 | B22 tanpa nama SKILL_ dan tanpa nomor dokumen: "format laporan insiden baku". Perlu nomor SNX atau lokasi format laporan insiden untuk pelanggan. | Fani |
| 7 | Baris riwayat revisi kedua (rev 00 tanggal sama, frasa RTO) dikosongkan dan C31 memakai "Draft awal untuk review dan pengesahan". | Fani |
| 8 | Titik awal batas 3 x 24 jam: form menghitung dari waktu deteksi, SOP-01 Bagian 11 butir 2 menulis "paling lambat 3 x 24 jam sejak diketahui". Tidak diterapkan di rumus. | Legal |
| 9 | Kolom waktu pemberitahuan aktual ke lembaga berwenang dan ke subjek data di Register (sekarang hanya "Tgl info pelanggan"). Tidak diterapkan di berkas. | Legal |
| 10 | Target waktu pulih insiden keamanan (RTO). Tidak ada di form maupun di SOP-01; SNX-OPS-SOP-04 punya target berlabel USULAN untuk insiden teknis. Tidak diterapkan di berkas. | Fani |
| 11 | SoA menautkan SNX-ISMS-FRM-02 juga untuk kontrol 5.26 dan 5.27 (sekarang hanya 5.25 dan 5.28, padahal keempatnya ada di header FRM-02). Tidak diterapkan di berkas. | Fani |

## Open items

| # | Butir | Pemutus / pemilik |
|---|---|---|
| 1 | Gambar "Alur Proses" memakai sebutan "COO dan Legal" pada kotak Kaji notifikasi PDP, tanpa bentuk "Direktur (COO)". Alat patch tidak mengedit gambar; gambar harus dibuat ulang bila sebutannya mau diseragamkan. | LEAD ISO / owner |
| 2 | Efek samping clear_rows pada legenda warna: baris 26 dikosongkan, tetapi kotak warna A26 berubah mengikuti kotak A27 (abu-abu), sehingga ada dua kotak abu-abu bersebelahan dengan satu label "Sel rumus: jangan diubah". Kosmetik; alat patch tidak bisa menghapus warna tanpa meniru baris bawahnya. | LEAD ISO (tech_fix xlsx_patch) |
| 3 | Alat patch tidak mengubah tinggi baris. Teks B15, B19, B20 dipendekkan agar muat dalam tinggi baris yang ada (dicek dengan render soffice). | LEAD ISO |
| 4 | Format laporan insiden untuk pelanggan tidak punya nomor SNX dan isinya tidak ada di korpus (sumber menyebutnya "format beku"). Lihat USULAN 6. | Fani |
| 5 | Peran tanpa pemegang: Lead SOC (K-10), ISMS Coordinator (K-13). "Incident Commander" tidak ada di HR-ORG-01. | owner |
| 6 | SNX-ISMS-SOP-01 belum punya spec di repo ini. Verifikator perlu mencocokkan pointer severity di B15 dengan SOP-01 hasil draf W2. | LEAD ISO |
| 7 | Tanggal draft 13 Oktober 2026 dipertahankan dari sumber; tanggal efektif dan tanda tangan kosong sampai pengesahan. | owner |
| 8 | Masa simpan 5 tahun berbeda dari beberapa dokumen ISMS dan Ops lain; tidak diubah. Penyeragaman masa simpan antardokumen belum diputus. | Fani |
| 9 | Dasar hukum PDP tidak disebut di form (UU PDP disebut di SOP-01 menurut audit). Tidak ditambahkan karena sumber form diam. Lihat USULAN 8 dan 9. | Legal |

## 5. Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI?

1. B20 pada draf pertama 204 karakter, memuat kata "otomatis" dan "bahwa" yang tidak menambah arti, dan tidak muat di tinggi baris. Diperbaiki menjadi 151 karakter: satu keterangan tentang apa yang ditandai kolom, satu tentang siapa memutuskan.
2. B22 "format laporan insiden baku" masih agak kabur karena sumbernya sendiri tidak menyebut nomor atau isi format. Dibiarkan polos, tidak diberi sifat tambahan, dan dicatat sebagai USULAN 6 dan Open item 4.
3. "Direktur (COO)" di B20 memakai kurung di dalam kalimat; bentuk itu diwajibkan data_conflicts, jadi dipertahankan.
4. Pola yang dihindari dan sudah dicek: tidak ada kelompok tiga yang dipaksakan, ekor penegas, kata kosong, penutup positif, tanda kutip atau huruf kapital untuk penekanan. Kata "WAJIB DIKAJI" milik rumus Register P5 dan tidak ditiru di teks B20, yang memakai huruf biasa. Pemindaian pola lint_doc: 0 temuan.

Adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir di berkas | Sumber |
|---|---|
| 3 x 24 jam, "dari waktu deteksi" (B20) | Kontrol Dokumen B20 sumber dan rumus Register P5 (B5+3) |
| 1 desimal (B19) | Rumus N5 dan O5, ROUND(...,1) |
| 5 tahun, Lead SOC, 10.2, Annex A 5.25 sampai 5.28 (B10, B12, B13, B14) | Sumber (B10, B12, B13, B14) dan prompt penyusun |
| Nama dan jabatan penyusun, pemeriksa, penyetuju (B11, B36 sampai B38) | Data baris di prompt dan config/defaults.json |
| "Direktur (COO)" (B20) | config/defaults.json data_conflicts |
| SNX-ISMS-SOP-01 memuat definisi severity P1 sampai P4 (B15) | Hanya salinan audit (DATA); tidak dicek ke Drive. Dilabeli USULAN 3 |
| Tanggal 13 Oktober 2026 | Sumber B7 dan B31, tidak diubah |

Semua butir lain berasal dari sumber atau data baris. Tidak ada angka, nama, atau tanggal baru yang ditambahkan penyusun.
