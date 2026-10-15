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
