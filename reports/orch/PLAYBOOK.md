# PLAYBOOK orkestrator WORKER-ISO-01 (baca ini dulu sesudah konteks diringkas)

Kebenaran keadaan = ledger.json (`python3 -I reports/orch/orch.py summary`). Aturan run = ledger.json "run_rules". Prompt subagen ditulis ke /tmp/claude-0/prompts/<KEY>.<pen|ver|pdf>.txt; subagen diminta membaca berkas itu (Read) sebagai instruksinya.

Per dokumen (dari /home/claude/iso-run):
1. `orch.py pen KEY > /tmp/claude-0/prompts/KEY.pen.txt`; `orch.py set KEY IN_PROGRESS`; Agent model sonnet, background, prompt: baca berkas prompt itu. Catat id: `orch.py set KEY IN_PROGRESS pen_agent=<id>`.
2. Selesai: `orch.py set KEY DRAFTED` lalu `orch.py post KEY` (xlsx butuh /tmp/src/KEY.xlsx dari penyusun).
3. LINT_FAIL: SendMessage ke pen_agent berisi fails (loops+1, maks 2) lalu ulang 2; lewat 2 = `orch.py set KEY NEEDS_REVIEW`.
4. LINT_PASS dan butuh verifikasi (run_rules.verify): `orch.py ver KEY > prompts/KEY.ver.txt`; Agent opus background. Butuh cek PDF (run_rules.pdfcheck): `orch.py pdf KEY > prompts/KEY.pdf.txt`; Agent opus background.
5. Hasil: `orch.py finish KEY` (vres + DONE + commit + push bila PASS); cek pdfcheck dulu bila ada. FAIL = SendMessage pen_agent berisi blocking (loops+1, maks 2), post, verifikasi ulang (pindahkan qa/KEY.verify.json ke .rN.json dulu).
6. Tidak butuh verifikasi (W5/W6 di luar sampel): `orch.py finish KEY noverify`.
Push: `git pull --rebase --autostash -q origin main && git push -q origin main` (gagal 3x = zip out/ + ledger.json lewat SendUserFile).

Checkpoint tiap wave (RUNBOOK §9): `orch.py report W<n>`; commit reports + ledger; pull --rebase; baca control/LEAD-GUIDE.md (G-n > last_guide_seen); hapus watchdog lama (delete_trigger id ledger.watchdog_trigger_id), buat send_later +45 menit, simpan id; cek sisa token < 1.500.000 = langsung W8.
W8: Master_List_COS.xlsx (88 baris) + Laporan_Run.md (W8 di out/00_Index; sejak ISO-W9 di reports/, arahan LEAD G-2 butir 3), push final, packet staging final (bila konektor KB ada), hapus watchdog, HANDOFF empat blok.

## Sweep (sesudah semua dokumen DONE atau saat slot penyusun kosong)
Daftar: `python3 -I reports/orch/sweep.py list` (salinan awal /tmp/claude-0/sweep-list.txt, 36 dokumen). Per dokumen:
1. `sweep.py prompt KEY`; `orch.py set KEY IN_PROGRESS sweep=1`; SendMessage ke pen_agent: baca /tmp/claude-0/prompts/KEY.sweep.txt.
2. Selesai: `orch.py set KEY DRAFTED`; `orch.py post KEY`; `sweep.py diff KEY`; `sweep.py dv KEY`; Agent opus baca /tmp/claude-0/prompts/KEY.dv.txt.
3. qa/KEY.sweep.json PASS: `orch.py finish KEY` (atau `finish KEY noverify` bila dokumen tidak disampel) lalu `orch.py set KEY DONE sweep=2`. FAIL: satu putaran perbaikan, lalu ulang 2.
Cek rujukan silang mesin: `python3 -I reports/orch/refcheck.py` (harus {}).
