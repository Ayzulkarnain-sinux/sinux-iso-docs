# ISO-W10 RESUME (WORKER-ISO-03) — baca ini dulu bila konteks diringkas atau container baru

Kebenaran keadaan: `python3 -I reports/orch/w10.py status` (gate + qa per KEY), `reports/w10/gates/KEY.json`, `qa/KEY.w10*.json`, ledger.json medan `w10`, git log. Berkas ini ringkasan, bukan sumber.

## Aturan run (mengikat)
- Hierarki: RUNBOOK §0 > LEAD-GUIDE G-4 > config/STYLE-v23.md > lainnya. Nol mutasi Drive (hanya baca modifiedTime), nol staging, nol kanon KB, nol relay_mark, nol kredensial, status Draft, nol tanda tangan/tanggal efektif, nomor butir dan heading tetap.
- Owner (06:52Z): "Gaspol, saya prefer all document. Make sure semua dikerjakan dengan baik" -> pilot dikirim + commit, lalu sapuan tanpa berhenti.
- Maks 3 subagen paralel (hitung sebelum meluncurkan). Penyusun dan pemeriksa: Agent model opus, effort medium, background.
- Alur per KEY: penyusun (prompt /tmp/claude-0/w10/prompts/EDITOR.md) -> `w10.py build KEY` pass (diverifikasi worker) -> pemeriksa buta (CHECKER.md) -> PASS (semua skor >= 4) -> `w10.py stage KEY` + commit + `git fetch && git push` (jangan pull --autostash saat agen aktif).
- Gagal pemeriksa sekali = satu putaran perbaikan (perbaiki seluruh kelas masalah). Gagal kedua = `revert` ke bed1bb6: salin spec/notes ke reports/w10/residu/KEY.w10-attempt.*, qa ke .r2, gates[residu], commit.
- Jam potong 14.00 UTC: dokumen belum lolos dikembalikan ke bed1bb6 (residu bernama).

## Perkakas (semua di repo)
- tools/render_sop.py: meta.table_defaults {align_left, repeat_header, cant_split, keep_with_table, steps_widths_cm}; tabel generic widths_cm, min_row_cm.
- tools/xlsx_patch.py: freeze, wrap_cols(valign), col_widths, page_setup(paperSize), fit_rows.
- reports/orch/w10.py: terms/termsdiff (peta istilah, sudah dijalankan sekali 07:0xZ), td, xlsxinit, isotitles, build, revert, stage, ptrlist, status. Gerbang build: struktur/nilai beku, lint, OOXML, langscan (calque, lewat, justified, header, instr<=25%), diff substansi (butir/headings/persons/snx), selisih angka di notes, label USULAN berkurang tercatat, rujukan ke butir USULAN, audit pointer, halaman form tidak naik, xlsx cetak.
- reports/orch/w10_grepgate.py: HR Lead/Kristanto/Divisi Legal/Daffa sama dengan bed1bb6.

## Keputusan yang menunggu owner
- "ulang residu": izin putaran ke-3 untuk dokumen residu (lihat daftar di bawah). Tanpa izin, residu tetap bed1bb6.

## Sisa kerja (urutan)
1. Sapuan SOP sisa: HR-SOP-08, 10, 11, 12 (selaraskan batas rotasi/mutasi dengan HR-SOP-13); FAT-SOP-04, 05, 06; COM-SOP-01, 02. LEG-SOP-01..03 sedang disunting.
2. Audit pointer retroaktif (task #5): `w10.py ptrlist KEY` untuk docx yang lolos sebelum gerbang audit pointer (~08:24Z); lengkapi atau catat "### W10 audit pointer", rebuild, commit.
3. Penutupan: selftest; lint/OOXML/blankscan semua; refcheck2 (keluaran ke reports/w10); metascan; w10_grepgate; modifiedTime 54 sumber ulang; w8.py (Master List + USULAN-OPEN); Laporan_Run bagian "Perubahan ISO-W10"; reports/REVIEW-W10.md (tabel per gerbang, residu bernama, 3 contoh sebelum/sesudah per departemen, GAP, OPEN DECISION, RESIDUAL RISK, retraksi/insiden); ledger current_wave W10-DONE; hapus watchdog (ledger.watchdog_trigger_id); commit "ISO W10 penutupan"; HANDOFF 4 blok.

## Catatan untuk REVIEW-W10 (dikumpulkan sepanjang run)
- GAP pemindai: STARTS_ROLE tidak mengenali butir "6.1 Peran ..." (FAT-FRM-01 nyata 12/13, terukur 0/13).
- Skrip istilah: "lewat" bermakna "terlampaui" salah dipetakan 2 kali (ISMS-REG-04, LEG-REG-04), dibetulkan penyusun; judul klausul ISO dikembalikan (isotitles).
- Label "sedang dalam peninjauan" (G-3) menjadi "sedang dalam review" seragam; MKT-REG-01 nilai status "Dalam Peninjauan" -> "Dalam Review" (OPEN DECISION LEAD).
- Insiden: batas 3 subagen sempat terlampaui (~08:21Z, dihentikan, tanpa perubahan berkas); agen MKT menjalankan git hanya-baca; stempel waktu taksiran dibetulkan.
- Paragraf badan rata kiri-kanan berasal dari template (STYLE hanya mengatur sel); widths_cm generic tidak selalu dihormati LibreOffice (tblLayout autofit).
