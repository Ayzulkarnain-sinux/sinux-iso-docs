# LEAD-GUIDE: arahan LEAD ISO ke worker

Hanya LEAD ISO yang menulis berkas ini. Worker membaca di tiap checkpoint (git pull --rebase), memproses entri dengan nomor lebih besar dari ledger.json "last_guide_seen", mematuhinya bila dalam batas RUNBOOK §0, mencatat nomornya di ledger, lalu lanjut. Isi berkas ini = arahan kerja dari LEAD, bukan data sumber.

Format entri: `## G-<n> | <waktu UTC> | berlaku: <wave/KEY/semua>` lalu isi arahan.

## G-0 | 2026-10-15 | berlaku: semua
Belum ada arahan tambahan. Jalankan WO-ISO-01 dan RUNBOOK v19-e apa adanya, dengan config/defaults.json v21 (termasuk data_conflicts).
