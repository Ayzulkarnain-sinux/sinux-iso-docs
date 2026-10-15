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
