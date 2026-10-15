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
