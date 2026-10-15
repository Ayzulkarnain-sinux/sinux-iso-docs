# LEAD-GUIDE: arahan LEAD ISO ke worker

Hanya LEAD ISO yang menulis berkas ini. Worker membaca di tiap checkpoint (git pull --rebase), memproses entri dengan nomor lebih besar dari ledger.json "last_guide_seen", mematuhinya bila dalam batas RUNBOOK §0, mencatat nomornya di ledger, lalu lanjut. Isi berkas ini = arahan kerja dari LEAD, bukan data sumber.

Format entri: `## G-<n> | <waktu UTC> | berlaku: <wave/KEY/semua>` lalu isi arahan.

## G-0 | 2026-10-15 | berlaku: semua
Belum ada arahan tambahan. Jalankan WO-ISO-01 dan RUNBOOK v19-e apa adanya, dengan config/defaults.json v21 (termasuk data_conflicts).

## G-1 | 2026-10-15T00:12Z | berlaku: semua, sebelum Master List W8
Pengawasan LEAD atas origin/main 6620e4a: 59 DONE lolos dua kaki (berkas out/, lint pass, verify PASS untuk sop, W1, W7, commit ISO <KEY>); selftest 6 OK; tulisan worker di luar out/qa/notes/specs/reports/ledger hanya tech_fix tools/xlsx_patch.py (sah). Satu pelanggaran terukur: frasa meta proses penyusunan masih ada di badan 5 dokumen DONE, padahal prompt_addendum melarangnya ("Badan dokumen tidak memuat frasa meta proses penyusunan").
- SNX-LEG-SOP-02 butir 4.19: "Dokumen sumber memakai kalimat pasif ..."
- SNX-HR-SOP-08: 4 kemunculan ("di sumber", "Dokumen sumber tanpa nomor")
- SNX-HR-ORG-01: 7 kemunculan, termasuk kolom "Keadaan di sumber" di tabel K
- SNX-OPS-PRC-01: 2 kemunculan ("Referensi dokumen sumber menambah klausul ...")
- SNX-HR-JA-01: 1 kemunculan ("DoA di sumber")
Kata "penyusun" di SNX-OPS-FRM-03, 06, 10 adalah nama peran formulir, sah, jangan diubah. Kemunculan "Kristianto" di tabel K-07 HR-ORG-01 menjelaskan konflik ejaan, sah.
Arahan:
1. Butir ini sudah ada di pending_tasks ledger. Kerjakan SEBELUM Master List W8, lewat penyusun dokumen masing-masing: ganti kalimat itu saja dengan kode SNX atau nama berkas yang dirujuk, lint ulang, verifikasi ulang untuk mode sop dan W1, commit "ISO <KEY> polish".
2. Ukur ulang seluruh out/ sesudah sweep dengan pola (?i)\b(dokumen sumber|sumber tim|di sumber|draf ini|belum berdokumen)\b, ditambah "penyusun" yang bukan peran formulir. Target nol. Kontrol positif: jalankan pola pada teks LEG-SOP-02 butir 4.19 sebelum diperbaiki; harus menembak.
3. Butir pending_tasks yang belum selesai saat W8 atau saat penjaga anggaran berhenti dicatat per KEY di Laporan_Run.md dan reports/LEDGER.md sebagai residu mutu dengan alasannya. Jangan menutup run seolah bersih.

## G-2 | 2026-10-15T02:04Z | berlaku: sesi lanjutan, sebelum berkas apa pun diunggah ke Shared Drive
Pengawasan LEAD atas origin/main b6a32be. Lolos dua kaki: 70 dari 70 DONE (berkas out/, lint, verify PASS di mode sop, W1, W7, commit); nomor SNX unik; 70 berkas out/ sama dengan 70 path ledger; frasa meta 0 (diukur ulang LEAD dengan pola lebih lebar); selftest 6 OK; 54 dari 54 berkas sumber tidak berubah sejak dibaca (modifiedTime Drive sama dengan ledger). G-1 dipatuhi.
Temuan wajib, kerjakan sebelum unggah:
1. SNX-OPS-FRM-10 masih memakai penomoran SOP tim lama. Enam rujukan basi: SNX-OPS-SOP-04 "Bagian 4" (definisi insiden), "Bagian 6" (tingkat keparahan), "Bagian 7.5" dua kali (kewajiban RCA, insiden berulang), dan SNX-OPS-SOP-05 "Bagian 4" dua kali (definisi breach, pengecualian). Di out/ SOP-04 tidak punya bagian 7.5, dan bagian 4 atau 6 bukan tempat isi itu. Tabel pemetaan di notes/OPS-SOP-04.md menunjukkan sumber Bagian 4 menjadi bagian 3 dan sumber 7.1 sampai 7.5 menjadi 6.1 sampai 6.5. Tentukan butir tujuan dengan membaca SNX-OPS-SOP-04 dan SNX-OPS-SOP-05 di out/, ganti rujukan saja, lint ulang, verifikasi ulang perubahan, commit "ISO OPS-FRM-10 polish".
2. reports/w8/refcheck.txt hanya berisi "{}", jadi klaim "177 rujukan dicek, 0 rusak" di Laporan_Run.md, reports/LEDGER.md, dan paket ringkasan tidak berbukti. Ulang pemeriksaan rujukan dengan keluaran penuh per rujukan: dokumen asal, kalimat, dokumen tujuan, nomor, ada atau tidak, judul bagian tujuan. Penomoran heading Word otomatis harus diturunkan dari urutan heading, bukan dicari sebagai teks. Kontrol positif: rujukan SNX-OPS-SOP-04 bagian 7.5 versi sekarang harus tertembak sebelum butir 1 diperbaiki. Perbaiki angka di laporan. Ukuran LEAD: 141 rujukan unik, 1 tujuan tidak ada, 5 basi secara makna, semuanya di SNX-OPS-FRM-10; makna rujukan di luar form W5 belum diukur.
3. out/00_Index/Laporan_Run.md memuat istilah proses kerja (agen, orkestrator, ledger, repo, classifier, perkakas), padahal langkah unggahnya menyuruh "unggah isi out/ apa adanya". Pindahkan berkas itu ke reports/Laporan_Run.md (git mv) dan perbarui rujukannya. Out/ hanya berisi dokumen ISO dan Master_List_COS.xlsx.
Tidak wajib, kerjakan hanya bila owner memilihnya: gambar alur di lima form xlsx yang bertentangan dengan teks (OPS-FRM-01, 04, 05, 08, ISMS-FRM-02); validasi data dan format input SNX-FAT-REG-01 hanya di baris 5 sampai 6; verifikasi isi untuk SNX-OPS-FRM-03 dan SNX-ISMS-REG-01; residu mutu 6 dokumen.

## G-3 | 2026-10-15T02:21Z | berlaku: sesi worker lanjutan ISO-W9, mulai saat owner mengetik gaspol di sesi itu
Dasar: jawaban owner 15 Okt atas vonis run 1 (kutipan per butir di bawah) dan rekomendasi LEAD yang owner minta ("berikan best recommendation"). Rekomendasi LEAD ikut berlaku saat owner mengetik gaspol. Nilai baru ada di config/defaults.json v22. Ubah lewat specs/ lalu render ulang, jangan menyunting docx atau xlsx keluaran langsung kecuali spec tidak mencakupnya.

A. Data, wajib di semua dokumen:
A1. Direktur Utama (owner: "Samuel kristanto utomo"): ejaan Kristanto tetap. HR-ORG-01 K-07 ditulis sebagai sudah diputus; Job Analysis tim dibetulkan HR (open item pemutus Aziz).
A2. Aziz (owner: "Jabatan Aziz HR Lead/SPV"): jabatan ditulis "HR Lead" di semua dokumen, menggantikan "HR Manager" (189 kemunculan di 10 dokumen HR, blok Reviewed By HR, simpul JA-14 di bagan, kolom pemutus Master List). SPV hanya ditulis bila dokumen punya kolom tingkat jabatan. K-06 diperbarui.
A3. Garis lapor (owner: "Laras melapor keduanya, dua garis. termasuk fani"): di HR-ORG-01 garis JA-01 ke JA-03 menjadi garis tegas tanpa label, dan tambah garis tegas JA-01 ke JA-04. K-01 ditutup. Selaraskan HR-JA-01 dan dokumen lain yang menyebut atasan JA-03 atau JA-04.
A4. Atasan JA-05, JA-08, JA-10, JA-11, JA-14 (owner menjawab "ini benar" atas rekomendasi meneruskan ke Aziz): tidak berubah. Label menunggu konfirmasi (K-02, K-03, K-04) tetap; open item pemutus Aziz.
A5. Legal (owner: "atasan alif adalah ester (alif pengganti daffa)"): Line Manager Legal = JA-08 Ester Febe Utomo, Staff Legal = JA-09 Alif Altamziz. Hapus label USULAN pada pemetaan itu. Blok Prepared dan Reviewed Legal diisi nama (defaults v22). Nama Daffa tidak dipakai (diukur 0). Unit ditulis "Departemen Legal"; ganti 12 "Divisi Legal" di LEG-SOP-01 dan LEG-SOP-02.
A6. Finance (owner: "finance lead belum ada"): "Finance Lead" dan "Finance Staff" tetap nama peran. Di tiap dokumen yang memakainya (FAT-SOP-01, 04, 05, 06, FAT-FRM-01, 02, FAT-REG-01, FAT-RPT-02, HR-JA-01, HR-ORG-01) tambahkan di Istilah atau Peran: Finance Lead adalah peran pemeriksa dan penyetuju FAT; jabatannya belum terisi, dan sampai terisi peran ini dijalankan Direktur (USULAN). Finance Staff adalah peran pelaksana yang dijalankan pemegang jabatan Finance (JA-10) dan Accounting & Tax (JA-11) (USULAN). Reviewed By dokumen FAT = Amirull Yusuf Zulkarnain / Direktur. K-13 diperbarui.
A7. Process Owner SNX-COM-FRM-01, SNX-COM-FRM-02, SNX-COM-REG-01 = VP Commercial (rekomendasi LEAD).
A8. Marketing (rekomendasi LEAD): SNX-MKT-REG-01 menjadi satu-satunya register materi, konten, dan persetujuan klaim, termasuk validasi klaim dari Description baris 58. SNX-MKT-REG-02 hanya mencatat pelaksanaan campaign dan aktivitas (nama, tujuan, channel, jadwal, PIC, anggaran bila ada, status, ID materi di REG-01, hasil singkat); kolom materi dan klaim dihapus. SNX-MKT-REG-03 tetap untuk lead dan hasil. SNX-MKT-RPT-01 membaca REG-02 dan REG-03. "Aktivitas" punya satu arti di REG-02 dan RPT-01; Dibatalkan dihitung terpisah dari belum Selesai. Penurunan klasifikasi materi dicatat mengikuti SNX-ISMS-PRO-01 di SNX-ISMS-REG-01; REG-01 hanya merujuk. Open item tim: Description checklist baris 58 adalah salinan baris 57 dan perlu dibetulkan Brand & Marketing.
A9. Gambar alur xlsx (owner: "gambar excell sudah diganti dengan gambar .png yang dibuat sendiri"): tidak diubah. Open item gambar di OPS-FRM-01, 04, 05, 08 dan ISMS-FRM-02 ditutup sebagai diputus owner.
A10. SNX-FAT-REG-01 (rekomendasi LEAD): di AR Aging, validasi kolom K dan L serta format sel input diperpanjang sampai baris 1000, sama dengan rentang rumus AP Aging. Days overdue memakai pola rumus kolom Aging di AP Aging (rumus tim sendiri), dengan catatan USULAN di Kontrol Dokumen. Status tetap dropdown. AP Aging baris 7 (transaksi nyata "PPN August") dikosongkan dari salinan Draft; rekaman nyata tetap di berkas kerja tim.

B. Mutu, wajib:
B1. G-2 butir 1 sampai 3.
B2. Residu mutu 6 dokumen di Laporan_Run (HR-SOP-11, HR-SOP-13, COM-SOP-02, MKT-RPT-01, MKT-REG-01, MKT-REG-02). Pertentangan bagian 9 dengan butir 4.3 di HR-SOP-13 wajib hilang.
B3. Verifikasi isi SNX-OPS-FRM-03 dan SNX-ISMS-REG-01.
B4. 34 open item berpemutus LEAD di reports/USULAN-OPEN-per-pemutus.md ditutup per butir dengan alasan satu baris: rujukan silang lewat pemeriksaan G-2 butir 2; dokumen T3 yang ditandai ada di checklist ditulis "dalam peninjauan" secara seragam (HR-FRM-02 dan HR-RPT-01, Financial Document Register di FAT-SOP-04); catatan garis putus-putus HR-ORG-01 sudah basi; sumber LEG-SOP-02 sudah diukur LEAD tidak berubah; unit Legal lihat A5; gambar lihat A9; swatch legenda xlsx dibiarkan (kosmetik); tabel di HR-RPT-01 dan MKT-RPT-01 diberi baris judul berulang dan baris yang tidak terbelah antarhalaman.

C. Gerbang sesudah perubahan, semua rc 0, bukti penuh di reports/w9/:
- selftest 6 OK; lint dan validasi OOXML tiap berkas yang dirender ulang; blankscan 0.
- Tiap dokumen yang berubah diperiksa pemeriksa perubahan buta atas diff teks sebelum dan sesudah (qa/<KEY>.w9.json PASS).
- Pemeriksaan rujukan penuh berkontrol positif (G-2 butir 2) dan metascan 0 berkontrol positif.
- Grep bukti: nol "HR Manager" kecuali di tabel K yang menjelaskan konflik; nol "Divisi Legal"; nol label menunggu konfirmasi pada garis JA-03 dan JA-04.
- modifiedTime 54 sumber diukur ulang; beda = BERHENTI dan lapor.
- Master_List_COS.xlsx dan reports/USULAN-OPEN-per-pemutus.md dibangun ulang; Laporan_Run (sudah di reports/) mendapat bagian "Perubahan ISO-W9".
- Nol staging dari worker, nol mutasi Drive, status Draft, nol tanda tangan dan tanggal efektif.

D. Selesai: ledger current_wave "W9-DONE", reports/REVIEW-W9.md berisi tabel per butir A, B, C (dikerjakan, bukti, sisa), commit "ISO W9 penutupan", push, lalu BERHENTI.

## G-4 | 2026-10-15T07:05Z | berlaku: sesi worker ISO-W10, mulai saat owner mengetik gaspol di sesi itu
Dasar: vonis final LEAD ISO-B (GO, packet #1994) lalu review tim. Owner, verbatim: "Sudah ditinjau sama tim, tapi inputnya adalah tata bahasa. Masih Slop, AI sekali. Bahasa indonya aneh. Better mix, isitilah dll tetap in english. Semi billingual. Hasilnya hanya kurang di bahasa, dan di frm/form kurang rapih dan bahasa kurang bagus."
Substansi sudah lolos verifikasi dua kaki di bed1bb6. W10 hanya mengerjakan bahasa dan kerapian tabel serta form. Substansi beku (config/STYLE-v23.md §8). Draf G-4 sudah diserang Red Team buta (10 temuan); semua temuan diterapkan di versi ini.

Akar masalah, diukur LEAD dengan tools/w10_langscan.py di bed1bb6:
- Aturan gaya memaksa setiap kalimat diawali nama peran dan melarang benda menjadi subjek. Hasilnya 60 pola "yang <pelaku> <kata dasar>", dan 71 butir petunjuk form diawali nama peran (SNX-LEG-FRM-02 25 dari 25, SNX-OPS-FRM-10 9 dari 14).
- Aturan "satu fakta sekali, bagian lain merujuk nomor butir" menghasilkan kalimat penunjuk dan rujukan beruntun.
- Label (USULAN) muncul 1.137 kali.
- Istilah kerja diterjemahkan ke Bahasa Indonesia ("rekaman", "tiket", "formulir"), padahal tim menulisnya dalam English. "lewat" muncul 166 kali.
- Form tidak rapi:
  - 2.477 paragraf sel tabel rata kiri-kanan, sehingga teks di sel sempit berjarak lebar;
  - 841 tabel (3 baris atau lebih) tanpa header berulang;
  - form docx median 13,5 halaman, dan bagian ISI baru mulai di median halaman 9;
  - xlsx tanpa freeze panes dan tanpa setelan cetak.

Langkah 0. Bila owner menempelkan catatan review tim di sesi worker, salin verbatim ke notes/W10-team-input.md dan perlakukan sebagai koreksi berprioritas di atas STYLE-v23. Bila tidak ada, lanjut.

Aturan yang berubah:
1. config/STYLE-v23.md berlaku untuk 70 dokumen DONE.
2. RUNBOOK §6a butir 1 dan 9 digantikan STYLE-v23 §1 dan §2.
3. RUNBOOK §6a.2, §6a.6, dan §8.2(f) tidak lagi mewajibkan pelaku di bagian Definisi, Policy, Rekaman, dan Ketentuan Penggunaan form, dan di butir Petunjuk Pengisian, Cara Mengisi, Ketentuan Pengisian, serta Cara pakai. Di bagian 6 dan 9, pelaku tetap wajib (STYLE §2.2).
4. Dari prompt_addendum di ledger.json, butir "Benda ... tidak menjadi pelaku kata kerja manusia ..." dan "satu fakta disebut sekali di tempat paling tepat, bagian lain merujuk nomor butirnya" dicabut. Butir addendum lain tetap berlaku.
5. Peta istilah STYLE §1.5 dan diksi STYLE §2.5 (lewat, sesudah) diterapkan dengan satu skrip mekanis, sebelum penyusun bahasa bekerja. Diff skrip pada 5 dokumen pilot ikut dikirim ke owner.
6. Renderer: tambahkan kunci spec meta.table_defaults {"align_left": true, "repeat_header": true, "cant_split": true} di jalur render sop dan generic, lalu set di semua spec. Kolom berisi teks panjang diberi widths_cm. Spec UJI-RENDER dan UJI-GENERIC tidak disentuh, sehingga selftest tetap 6 OK. Catat sebagai tech_fix di ledger.
7. tools/xlsx_patch.py mendapat operasi freeze, wrap_cols, dan page_setup (landscape, fitToWidth 1, print_title_rows), masing-masing dengan kontrol positif dan negatif. Catat sebagai tech_fix. Sebelum mengubah apa pun, daftar sheet data dan baris header-nya ditulis di reports/w10/xlsx_sheets.json. Sheet berisi gambar alur tidak diubah.

Urutan kerja dan batas waktu:
1. Pilot, 5 dokumen: SNX-OPS-FRM-02 (xlsx), SNX-OPS-FRM-10 dan SNX-LEG-FRM-01 (form docx), serta SNX-FAT-SOP-01 dan SNX-HR-SOP-13 (SOP).
   - Render PDF kelimanya ke reports/w10/pilot/, lalu kirim ke owner lewat SendUserFile bersama diff skrip istilah.
   - Commit "ISO W10 pilot", push, lalu BERHENTI.
   - Target: pilot siap paling lambat 2 jam setelah gaspol pertama.
2. Owner meneruskan pilot ke tim. Koreksi owner dicatat verbatim di notes/W10-pilot.md dan diterapkan ke pilot dan sapuan. Owner mengetik gaspol untuk sapuan.
3. Sapuan 65 dokumen, berurutan: xlsx, lalu form, register, dan report docx, lalu SOP.
4. Jam potong 21.00 WIB (14.00 UTC). Dokumen yang belum lolos gerbang pada jam potong dikembalikan ke versi bed1bb6 dan dicatat sebagai residu bernama di REVIEW-W10. Paket tetap konsisten dan bisa diunggah.

Model:
- Sesi worker: Opus 5.5 effort high.
- Penyusun bahasa: subagen Opus 5.5 effort medium. Pass ini dikunci pada mutu bahasa, jadi Sonnet tidak dipakai di peran ini.
- Pemeriksa bahasa buta: subagen Opus 5.5 effort medium. Masukannya diff teks, PDF halaman form untuk rubrik (d), STYLE-v23, dan rubrik; tanpa notes penyusun.
- Kerja mekanis (skrip, render, gerbang): Sonnet 5.5 low.
- Paling banyak 3 subagen paralel, dibagi per departemen sehingga berkasnya tidak beririsan.

Gerbang W10. Semua rc 0, bukti penuh di reports/w10/. Pemindai resmi: tools/w10_langscan.py (selftest wajib OK). Baseline bed1bb6 disimpan di reports/w10/baseline.json.
1. Substansi: `w10_langscan.py diff <bed1bb6> <baru>` per dokumen.
   - Kunci butir dan headings tidak boleh muncul. Artinya urutan dan jumlah butir dan heading sama.
   - Kunci persons dan snx tidak boleh muncul.
   - Setiap selisih numbers dan usul_butir harus tercatat di notes/<KEY>.md (STYLE §3.6, §8.2).
   - Kontrol positif: diff OPS-FRM-10 versi 4a40352 lawan bed1bb6 harus menembak "7.5".
2. Bahasa (scan), per dokumen:
   - calque 0, lewat 0, justified_cells 0, tables_ge3_no_header 0;
   - instr_role_start paling banyak 25 persen dari instr_items;
   - usulan dan pointer dilaporkan sebelum dan sesudah, tanpa target angka.
3. Pemeriksa bahasa buta. Rubrik ditetapkan sekarang, sebelum run, skala 1 sampai 5:
   - (a) Bahasa Indonesia bisnis yang wajar, tidak terdengar seperti terjemahan atau AI;
   - (b) Istilah English sesuai STYLE §1 dan §5;
   - (c) Bebas pola terlarang STYLE §2 dan §3;
   - (d) Khusus form, register, dan xlsx: rapi dan mudah diisi, dinilai dari PDF.
   PASS bila semua butir 4 atau lebih. Gagal sekali = satu putaran perbaikan. Gagal kedua = kembali ke bed1bb6 dan catat sebagai residu.
4. Xlsx: semua sheet di reports/w10/xlsx_sheets.json punya freeze, fitToWidth 1, landscape, dan print_title_rows (lihat medan sheets di scan). Sheet Kontrol Dokumen di-wrap. Ini menutup residu cetak SNX-FAT-REG-01.
5. Docx form: jumlah halaman dan halaman awal bagian ISI (render LibreOffice) dilaporkan sebelum dan sesudah. Tidak ada target, tetapi angkanya tidak boleh naik.
6. Gerbang lama:
   - selftest 6 OK;
   - lint dan OOXML semua berkas; blankscan 0;
   - refcheck2 penuh berkontrol positif, 0 TIDAK_ADA; metascan 0;
   - grepgate: HR Lead, Kristanto, Divisi Legal, dan Daffa sama dengan W9;
   - modifiedTime 54 sumber diukur ulang (beda = BERHENTI);
   - Master List dan USULAN-OPEN dibangun ulang;
   - Laporan_Run mendapat bagian "Perubahan ISO-W10".
7. Nol staging, nol mutasi Drive, status Draft, nol tanda tangan dan tanggal efektif.

Selesai:
1. ledger current_wave "W10-DONE".
2. reports/REVIEW-W10.md berisi tabel per gerbang (dikerjakan, bukti, sisa), daftar residu bernama, dan 3 contoh sebelum dan sesudah per departemen.
3. Commit "ISO W10 penutupan", push, lalu BERHENTI.

## G-5 | 2026-10-15 | berlaku: penutupan lane ISO
Catatan, bukan arahan kerja. LEAD ISO-B memverifikasi W10 (0a00bae), menemukan pergeseran cakupan substansi lewat pemeriksaan makna buta, lalu mengoreksi 53 path langsung di sesi LEAD. Rinciannya di reports/REVIEW-W11.md. Tidak ada arahan terbuka untuk worker. "ulang residu" tidak dijalankan: owner menutup sesi ISO, dan tim merevisi dokumen secara manual. Sesi worker baru di lane ini hanya dimulai atas arahan LEAD berikutnya.
