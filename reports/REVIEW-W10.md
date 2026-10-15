# REVIEW ISO-W10: pass bahasa dan form rapi (15 Oktober 2026)

Receipt: repo sinux-iso-docs, basis substansi bed1bb6, kerja W10 06.52 (gaspol owner) sampai penutupan sekitar 09.30 UTC oleh WORKER-ISO-03. Arahan: control/LEAD-GUIDE.md G-4, config/STYLE-v23.md. Bukti mesin di reports/w10/ (gerbang per dokumen di gates/, bukti penutupan di close/), putusan pemeriksa buta di qa/<KODE>.w10.json (putaran gagal di .w10.r1.json dan .w10.r2.json), catatan per dokumen di notes/<KODE>.md bagian "## W10". Riwayat: `git log --grep "ISO W10"`.

## RINGKASAN

Verdict: 60 dari 70 dokumen lolos semua gerbang G-4, termasuk pemeriksa bahasa buta (semua skor 4 atau lebih). 10 dokumen gagal pemeriksa dua kali, jadi dikembalikan ke bed1bb6 dan dicatat sebagai residu bernama. Sapuan selesai 08.58 UTC dan audit retroaktif 09.06 UTC, jauh sebelum jam potong 14.00 UTC. Pada 60 dokumen lolos: calque 53 jadi 0, "lewat" 136 jadi 0, kalimat penunjuk 51 jadi 0, sel rata kiri-kanan 2.152 jadi 0, tabel tanpa header berulang 693 jadi 0. Halaman form tidak naik di dokumen mana pun. Gerbang lama semua rc 0. Substansi tidak berubah (butir, heading, nama, kode dijaga mesin). Status tetap Draft.

## A. Gerbang G-4 (dikerjakan, bukti, sisa)

| Gerbang | Dikerjakan | Bukti | Hasil | Sisa |
|---|---|---|---|---|
| 1 Substansi | `w10_langscan.py diff` bed1bb6 lawan W10 per dokumen, ditambah gerbang beku worker: nilai meta, heading, nama peran, PIC, id diagram, kerangka JSON | reports/w10/gates/<KODE>.json (subst_diff); kontrol positif reports/w10/close/langscan_diff_kontrol_positif.txt | 60 lolos: kunci butir, headings, persons, snx tidak muncul. Setiap selisih numbers dan usul_butir tercatat di notes (dicek mesin). Kontrol positif OPS-FRM-10 @4a40352 menembak "7.5" | nihil |
| 2 Bahasa (scan) | scan per berkas final | reports/w10/close/gate_final.jsonl | 60 lolos: calque 0, lewat 0, justified_cells 0, tables_ge3_no_header 0; butir instruksi diawali peran 9 dari 861 (maks per dokumen 25 persen terpenuhi); pointer 51 jadi 0; usulan 954 jadi 993 | GAP pemindai, lihat GAP 1 |
| 3 Pemeriksa bahasa buta | Opus effort medium, tanpa notes penyusun, rubrik a sampai d | qa/<KODE>.w10.json (60), .w10.r1.json (27), .w10.r2.json (10) | 60 PASS: 43 di putaran pertama, 17 sesudah satu putaran perbaikan. 10 gagal kedua, jadi residu | 10 residu (bagian C) |
| 4 Xlsx | freeze, wrap, landscape, fitToWidth 1, print_title_rows untuk semua sheet di xlsx_sheets.json; Kontrol Dokumen di-wrap; tinggi baris; A3 untuk sheet 16 kolom atau lebih | reports/w10/xlsx_sheets.json, xlsx_effective/, gates/ | 17 dari 17 xlsx lolos; residu cetak SNX-FAT-REG-01 tertutup | tinggi baris ditaksir, bukan diukur dari font (RESIDUAL RISK) |
| 5 Halaman form | jumlah halaman dan halaman awal bagian isi, render LibreOffice, bed1bb6 lawan W10 | gates/<KODE>.json medan form; reports/w10/close/ringkasan_gerbang.md | 17 form docx lolos: total halaman 226 jadi 225; halaman awal isi tidak naik di dokumen mana pun (jumlah 153 jadi 151) | nihil |
| 6 Gerbang lama | selftest; lint dan OOXML; blankscan; refcheck2; metascan; grepgate; modifiedTime; Master List | reports/w10/close/: selftest.txt, gate_final.txt dan .jsonl, refcheck_w10.txt/.tsv/.json, metascan.txt, grepgate.txt, w8_rebuild.txt; reports/w10/sources_modtime.json | selftest 6 OK dan langscan selftest OK; 53 docx lint lulus, 53 OOXML PASSED, 0 halaman kosong; 17 xlsx 0 fitur berkurang, 0 CONTOH; refcheck2 1.793 kemunculan, kontrol positif menembak, 0 TIDAK_ADA, 0 DOK_TIDAK_ADA; metascan 0 dengan kontrol positif; HR Lead 248=248, Kristanto 93=93, Divisi Legal 0=0, Daffa 0=0; modifiedTime 54 dari 54 sama (07.02 dan 09.00 UTC, 2 dicek silang langsung oleh worker); Master List 88 baris dibangun ulang | 13 putusan rujukan W10 dibuat worker, bukan pemeriksa terpisah (GAP 4) |
| 7 Larangan | audit tool-call atas transkrip sesi dan 59 subagen | reports/w10/close/tool_audit.txt | 2.140 panggilan tool; nol staging, nol relay_mark, nol checkpoint_put, nol mutasi Drive (110 get_file_metadata saja), nol tulis lewat API GitHub; kontrol positif dan negatif OK. Status Draft, nol tanda tangan dan tanggal efektif (lint) | nihil |

Gerbang tambahan worker (dibuat selama run karena pemeriksa menemukan pola yang sama berulang; semuanya di reports/orch/w10.py build):
- Label (USULAN) yang berkurang wajib dicatat verbatim di notes (kontrol reports/w10/label_gate_test.txt).
- Rujukan ke butir berlabel yang diganti fakta wajib tetap membawa label (reports/w10/usulref_gate_test.txt).
- Audit pointer: setiap teks yang kehilangan rujukan butir atau bagian wajib diaudit kelengkapannya di notes.
- Retroaktif atas semua dokumen yang lolos sebelum gerbang itu ada:
  - Audit pointer: 211 jalur di 20 dokumen. 198 lengkap, 10 rujukan dikembalikan, 3 dilengkapi.
  - Audit cakupan label: 113 jalur kandidat di 26 dokumen. 37 diperbaiki ke cakupan bed1bb6.

Tabel per dokumen (status, skor, angka scan bed1bb6 lawan W10, halaman): reports/w10/close/ringkasan_gerbang.md.

## B. Contoh sebelum dan sesudah (3 per departemen)

Sebelum = bed1bb6, sesudah = W10 final. Isi aturan sama; yang berubah bahasa.

| Dept | Jenis | Sebelum | Sesudah |
|---|---|---|---|
| COM | calque | Kebutuhan bisnis customer yang Business Development catat di CRM sebagai salah satu keluaran discovery meeting. (SNX-COM-FRM-01, Istilah) | Kebutuhan bisnis customer yang dicatat Business Development di CRM sebagai salah satu keluaran discovery meeting. |
| COM | perintah | 6.17 Business Development menulis keputusan di kolom Hasil Eskalasi sesudah VP Commercial atau COO memutuskan. (SNX-COM-REG-01) | 6.17 Tulis keputusan di kolom Hasil Eskalasi setelah VP Commercial atau COO memutuskan. |
| COM | penunjuk | Status opportunity di CRM: ... dan Future Nurture. Pemetaan tahap ke status ada di butir 4.7. (SNX-COM-SOP-01, Definisi) | Status opportunity di CRM: ... dan Future Nurture. |
| FAT | calque | Bukti pemotongan PPh Pasal 23 yang klien serahkan kepada SINUX. (SNX-FAT-SOP-01) | Bukti pemotongan PPh Pasal 23 yang diserahkan klien kepada SINUX. |
| FAT | perintah | 6.2 Finance Staff menulis tanggal ia menerima pengajuan di kolom Tanggal Pengajuan. (SNX-FAT-FRM-01) | 6.2 Isi kolom Tanggal Pengajuan dengan tanggal pengajuan diterima. |
| FAT | penunjuk jadi fakta | 4.12 ... Nomor Invoice. Masa simpannya ada di bagian 11. (SNX-FAT-SOP-01) | 4.12 ... Nomor Invoice. Masa simpannya minimal 10 tahun. |
| HR | penunjuk | Pengelompokan pelatihan menurut tujuannya. Daftarnya ada di bagian 6. (SNX-HR-FRM-02) | Pengelompokan pelatihan menurut tujuannya. |
| HR | perintah | 6.3 HRGA Officer menulis di Rujukan Rencana kode pelatihan itu di Tabel 1 SNX-HR-FRM-02. Bila pelatihan tidak ada di sana, kolom dibiarkan kosong. (SNX-HR-RPT-01) | 6.3 Tulis kode pelatihan dari Tabel 1 SNX-HR-FRM-02 di Rujukan Rencana. Jika pelatihan tidak tercantum di sana, kosongkan kolom ini. |
| HR | diksi | Dokumen berklasifikasi RESTRICTED (Internal) dan dikendalikan lewat status dan revisi. (SNX-HR-JA-01) | Dokumen berklasifikasi RESTRICTED (Internal) dan dikendalikan melalui status dan revisi. |
| ISMS | penunjuk | Angka 1 sampai 3 yang menunjukkan prioritas pemulihan sebuah layanan kritis. Urutan pemulihannya ada di bagian 4. (SNX-ISMS-PLN-01) | Angka 1 sampai 3 yang menunjukkan prioritas pemulihan sebuah layanan kritis, dengan urutan pemulihan sesuai bagian 4. |
| ISMS | istilah | Rekaman hasil satu uji, yaitu laporan uji BCP dan IT recovery. Isi minimalnya ada di bagian 4. (SNX-ISMS-PLN-01) | Record (rekaman) hasil satu uji, yaitu laporan uji BCP dan IT recovery. |
| ISMS | diksi | ... (Annex A 5.29). Pelonggaran hanya lewat pengecualian di bagian 9. (SNX-ISMS-PLN-01) | ... (Annex A 5.29). Kontrol hanya boleh dilonggarkan melalui pengecualian di bagian 9. |
| LEG | calque | Kewajiban yang tercantum dalam sebuah izin yang SINUX miliki. (SNX-LEG-REG-03) | Kewajiban yang tercantum dalam izin milik SINUX. |
| LEG | penunjuk | Klausul kontrak yang wajib diperiksa Staff Legal. Daftarnya ada di butir 4.16. (SNX-LEG-SOP-01) | Klausul kontrak yang wajib diperiksa Staff Legal sesuai daftar di butir 4.16. |
| LEG | diksi | Menyerahkan kontrak pelanggan dan data permintaan lewat PIC Internal (Ketentuan butir 1 dan 2). (SNX-LEG-FRM-01) | Menyerahkan kontrak pelanggan dan data permintaan melalui PIC Internal. |
| MKT | calque | Satu produk komunikasi yang SINUX pakai untuk kebutuhan eksternal, seperti satu brosur atau satu konten social media. Jenis yang tercakup ada di bagian 2. (SNX-MKT-REG-01) | Satu produk komunikasi yang dipakai SINUX untuk kebutuhan eksternal, misalnya satu brosur atau satu content social media. |
| MKT | calque | Service level agreement: target tingkat layanan yang SINUX sampaikan kepada customer, misalnya availability layanan. | Service level agreement: target tingkat layanan yang disampaikan SINUX kepada customer, misalnya availability layanan. |
| MKT | diksi | Direktur Utama menyetujui register ini, bukan materinya, lewat blok Approval pada halaman depan. | Direktur Utama menyetujui register ini, bukan materinya, melalui blok Approval pada halaman depan. |
| OPS | penunjuk jadi fakta | Sistem pendukung yang dipakai proses ini disebut di bagian 4. (SNX-OPS-PRC-01) | Sistem pendukung proses ini adalah Nusametric, Overseer, console Nusagrid, Wazuh, AegisWAF, Cloudflare, EDR, Acronis Cyber Protect, Zammad, Service Hub, password manager (vault), Jumphost, dan Google Drive SINUX. |
| OPS | perintah | Bagian A diisi sesudah UAT lolos dan SNX-OPS-FRM-05 ditandatangani. (SNX-OPS-FRM-06) | Isi Bagian A setelah UAT lolos dan SNX-OPS-FRM-05 ditandatangani. |
| OPS | istilah dan diksi | Akui ke pelanggan lewat kanal pelanggan melapor: tiket diterima, nomor tiket, dan sedang dicek, sesuai target Ack di bagian 8. (SNX-OPS-SOP-04) | Kirim Ack ke pelanggan melalui kanal laporan pelanggan: ticket diterima, nomor ticket, dan sedang dicek, sesuai target Ack di bagian 8. |

## C. Residu bernama (dikembalikan ke bed1bb6)

Isinya sama dengan versi sesudah ISO-W9; percobaan W10 tersimpan di reports/w10/residu/<KODE>.w10-attempt.json dan .notes.md, putusan pemeriksa di qa/<KODE>.w10.r1.json dan .r2.json.

| Dokumen | Jam | Alasan gagal kedua |
|---|---|---|
| SNX-OPS-FRM-10 | 07.20 | r1 istilah badan tidak selaras dengan heading beku; r2 tata letak (label 5 Why terpisah dari tabel, baris Penutupan RCA sendirian) |
| SNX-LEG-FRM-02 | 07.38 | kriteria butir 8.1 dan 1.3 Daftar Periksa menyempit saat dipadatkan; r2 cakupan 8.1 masih menyempit |
| SNX-MKT-REG-02, SNX-MKT-REG-03, SNX-MKT-RPT-01 | 08.09 | fakta pengganti rujukan ke butir berlabel tampil tanpa label; perbaikan r1 hanya menyasar kemunculan yang dikutip pemeriksa |
| SNX-LEG-REG-04, SNX-LEG-RPT-01 | 08.12 | r1 label hilang saat rujukan diganti fakta dan kolom terpotong; r2 kalimat menyempit |
| SNX-OPS-SOP-01, SNX-OPS-SOP-02 | 08.28 | fakta pengganti pointer menyempit; r2 satu penggantian masih menyempit |
| SNX-ISMS-PRO-01 | 08.33 | r1 pelaku bagian 9 hilang dan butir 4.21 bergeser; r2 4.21 menyempit ("pihak ketiga" jadi "layanan pihak ketiga"), 4.14 bergeser |

Pola: 7 dari 10 residu (MKT tiga, LEG-REG-04, LEG-RPT-01, OPS-SOP-01, OPS-SOP-02) gagal karena kelas masalah yang kemudian dijaga mesin, yaitu pointer yang diganti fakta tidak lengkap dan label yang hilang atau bergeser. Gerbang itu belum ada saat dokumen ini disunting. Tiga lainnya gagal karena isi menyempit saat dipadatkan (LEG-FRM-02, ISMS-PRO-01) dan tata letak (OPS-FRM-10).

## GAP

| GAP | Dampak | Mitigasi yang diusulkan |
|---|---|---|
| 1. Pemindai STARTS_ROLE tidak mengenali butir berbentuk "6.1 Peran ..." | instr_role_start bisa terukur terlalu rendah. Contoh: SNX-FAT-FRM-01 nyata 12 dari 13 di bed1bb6, terukur 0 | Perbaiki pola di tools/w10_langscan.py dengan kontrol positif, lalu ukur ulang |
| 2. Ada spec yang berubah sesudah pemeriksa buta PASS dan tidak diperiksa ulang pemeriksa terpisah. Diverifikasi worker per jalur terhadap bed1bb6, lalu build ulang dengan semua gerbang mesin. Rinciannya: audit pointer (SNX-HR-SOP-13, FAT-SOP-01, LEG-REG-01, LEG-RPT-02, COM-REG-01, MKT-REG-01); audit cakupan label (37 jalur, 18 dokumen); koreksi worker (SNX-COM-SOP-01, COM-SOP-02, COM-REG-01, LEG-SOP-03, LEG-FRM-03) | Semua perubahan mengembalikan rujukan atau label ke bentuk bed1bb6, atau menyalin fakta dari butir yang dirujuk. Perubahan bahasa baru tidak ada | Satu pemeriksaan buta atas diff jalur itu saja (daftar di notes/<KODE>.md, subjudul audit pointer, audit cakupan label, dan koreksi worker) |
| 3. Paragraf badan rata kiri-kanan berasal dari template; STYLE dan pemindai hanya mengatur sel tabel | Tampilan paragraf badan tidak berubah | Keputusan LEAD: biarkan (template terkunci) atau tambah aturan paragraf |
| 4. 13 rujukan yang kalimatnya diubah W10 diputus worker dengan mencocokkan putusan W9 (asal, tujuan, lokasi sama). Pemeriksa makna terpisah tidak dipakai | Semua 13 menunjuk lokasi yang sama dengan putusan W9 | Tercatat per baris di reports/w10/refsem_w10.json (sumber: orkestrator) |
| 5. widths_cm tabel generic tidak selalu dihormati LibreOffice (tblLayout autofit) | Rubrik d dinilai dari PDF LibreOffice; tampilan di Word belum diukur | HUMAN-VERDICT: buka 3 form di Word |

## OPEN DECISION

1. Ulang residu (owner). Untuk 10 dokumen di bagian C diusulkan satu putaran ke-3, dengan gerbang audit pointer dan label yang sekarang ada. G-4 menetapkan gagal kedua sama dengan residu, jadi putaran ke-3 hanya jalan dengan GO owner. Ditanyakan selama run, belum ada jawaban.
2. SNX-MKT-REG-01: nilai status "Dalam Peninjauan" jadi "Dalam Review" mengikuti peta istilah. Ini nilai daftar pilihan, bukan kalimat (LEAD).
3. Sebutan pihak luar: "pelanggan" di dokumen OPS dan ISMS, "customer" di dokumen COM dan MKT, mengikuti dokumen induk masing-masing. Perlu diseragamkan atau tidak (LEAD atau owner).
4. SNX-FAT-SOP-04: "hardcopy" dan "softcopy" tetap, karena ada di judul prosedur yang beku. SOP lain memakai "hard copy" (LEAD).
5. Tetap terbuka dari W9, tidak disentuh W10:
   - ukuran tingkatan jabatan;
   - pengisian Finance Lead;
   - kasus Direktur Utama di SNX-HR-SOP-13;
   - peran Brand & Marketing di SNX-COM-SOP-02;
   - checklist baris 58.

## RESIDUAL RISK

- Paket berisi dua gaya bahasa. 10 residu masih memakai bahasa sesudah W9 ("lewat", calque, sel rata kiri-kanan), sedangkan 60 dokumen lain sudah W10.
- Audit cakupan label hanya mencakup jalur yang jumlah label atau jumlah kalimatnya berubah. Pergeseran cakupan yang kedua jumlahnya tetap sama tidak tertangkap mesin; pemeriksa buta menjadi satu-satunya kanal.
- Tinggi baris xlsx (fit_rows) ditaksir dari panjang teks dan lebar kolom, bukan diukur dari font. Baris bisa sedikit terlalu tinggi atau terpotong di Excel.
- Tata letak SNX-HR-SOP-08 (17 halaman) rapuh: satu suntingan uji memicu halaman kosong. Suntingan berikutnya wajib dijaga blankscan.
- Label (USULAN) di Master List naik dari 1.029 menjadi 1.070. Sebabnya, rujukan ke butir berlabel yang diganti fakta membawa labelnya (aturan pelajaran sapuan). Butir terbuka tetap 942. Peninjau yang membandingkan angka W9 perlu catatan ini.
- Paket staging 1982 (W8, PENDING) masih memuat angka sebelum W9 dan W10. W10 tidak mengirim staging.

## Insiden dan retraksi

| Waktu (UTC) | Hal | Penanganan |
|---|---|---|
| ~08.21 | Batas 3 subagen paralel terlampaui sekali (penyusun OPS-SOP-03..05) | TaskStop beberapa detik kemudian, berkas tidak berubah, diluncurkan ulang saat slot kosong (ledger agent_incidents) |
| 08.01 dan ~08.3x | Dua penyusun (MKT dan LEG-SOP) menjalankan git hanya baca padahal dilarang | Dilaporkan sendiri oleh agen; tanpa tulis atau commit; tercatat di ledger |
| sebelum 08.38 | Penyusun HR me-render ulang SNX-HR-SOP-13 (spec tetap), sehingga gate-nya gagal karena gerbang audit pointer yang baru | Diselesaikan lewat audit pointer retroaktif; satu rujukan bagian 9 dikembalikan |
| W10 | Skrip istilah memetakan "lewat" bermakna "terlampaui" jadi "melalui" di 3 tempat (SNX-ISMS-REG-04, LEG-REG-04, HR-SOP-11), dan memetakan judul klausul ISO | Dibetulkan penyusun; judul klausul dikembalikan mesin (w10.py isotitles) |
| 08.54 | refcheck2 membaca "butir 4.7 dan bagian 11" sebagai "butir 11", menghasilkan TIDAK_ADA palsu | tech_fix refcheck2 dengan 4 kasus uji (reports/w10/refcheck2_listkind_test.txt) |
| 08.53 | Uji kering refcheck2 menemukan rujukan salah tujuan buatan W10 di SNX-LEG-SOP-03 ("SNX-ISMS-SOP-01 (butir 4.17)") | Dibetulkan ke cakupan bed1bb6 (09.06) |
| ~09.15 | metascan menemukan frasa "penyusun" buatan W10 di SNX-LEG-FRM-03 | Dikembalikan ke bentuk bed1bb6, metascan 0 |
| Retraksi | Stempel waktu taksiran di ledger (tech_fixes, progres) sempat ditulis sebelum diukur | Dibetulkan dengan `date -u` dan waktu commit; taksiran yang tersisa ditandai "~" |

## Tafsir yang dipakai

- Gaspol owner 06.52 UTC ("Gaspol, saya prefer all document. Make sure semua dikerjakan dengan baik") dibaca sebagai berikut: pilot tetap dikirim dan di-commit ("ISO W10 pilot", c7d431d, 07.36 UTC, 4 lolos, OPS-FRM-10 residu), lalu sapuan berjalan tanpa berhenti menunggu gaspol kedua. Kutipan verbatim di notes/W10-pilot.md.
- Heading beku tidak dipetakan. Istilah English di badan diberi jembatan pada pemakaian pertama, misalnya "Record (rekaman)". Judul klausul ISO tidak dipetakan.
- Label (USULAN) satu per butir di akhir hanya bila seluruh butir berstatus usulan. Butir yang mencampur ketentuan berlaku dan usulan tetap berlabel per kalimat seperti bed1bb6.
- Rujukan ke langkah atau batas yang harus dijalankan pembaca dipertahankan (STYLE §3.1). Kalimat penunjuk lokasi murni dibuang (§3.2).
- Xlsx dengan 16 kolom atau lebih dicetak A3 landscape fitToWidth 1. Sheet bergambar alur tidak diubah.
