# PLAYBOOK orkestrator WORKER-ISO-01 (baca ini dulu sesudah konteks diringkas)

Kebenaran keadaan = ledger.json (`python3 -I reports/orch/orch.py summary`). Aturan run = ledger.json "run_rules". Prompt subagen ditulis ke /tmp/claude-0/prompts/<KEY>.<pen|ver|pdf>.txt; subagen diminta membaca berkas itu (Read) sebagai instruksinya.

Per dokumen (dari /home/claude/iso-run):
1. `orch.py pen KEY > /tmp/claude-0/prompts/KEY.pen.txt`; `orch.py set KEY IN_PROGRESS`; Agent model sonnet, background, prompt: baca berkas prompt itu. Catat id: `orch.py set KEY IN_PROGRESS pen_agent=<id>`.
2. Selesai: `orch.py set KEY DRAFTED` lalu `orch.py post KEY` (xlsx butuh /tmp/src/KEY.xlsx dari penyusun).
3. LINT_FAIL: SendMessage ke pen_agent berisi fails (loops+1, maks 2) lalu ulang 2; lewat 2 = `orch.py set KEY NEEDS_REVIEW`.
4. LINT_PASS dan butuh verifikasi (run_rules.verify): `orch.py ver KEY > prompts/KEY.ver.txt`; Agent opus background. Butuh cek PDF (run_rules.pdfcheck): `orch.py pdf KEY > prompts/KEY.pdf.txt`; Agent opus background.
5. Hasil: `orch.py vres KEY` (dan baca qa/KEY.pdfcheck.json). PASS semua = `orch.py set KEY DONE` + `orch.py commit KEY` + push. FAIL = SendMessage pen_agent berisi blocking (loops+1, maks 2), post, verifikasi ulang (pindahkan qa/KEY.verify.json ke .rN.json dulu).
6. Tidak butuh verifikasi (W5/W6 di luar sampel): LINT_PASS langsung DONE + commit.
Push: `git pull --rebase -q origin main && git push -q origin main` (gagal 3x = zip out/ + ledger.json lewat SendUserFile).

Checkpoint tiap wave (RUNBOOK §9): `orch.py report W<n>`; commit reports + ledger; pull --rebase; baca control/LEAD-GUIDE.md (G-n > last_guide_seen); hapus watchdog lama (delete_trigger id ledger.watchdog_trigger_id), buat send_later +45 menit, simpan id; cek sisa token < 1.500.000 = langsung W8.
W8: Master_List_COS.xlsx (88 baris) + Laporan_Run.md di out/00_Index, push final, packet staging final (bila konektor KB ada), hapus watchdog, HANDOFF empat blok.
