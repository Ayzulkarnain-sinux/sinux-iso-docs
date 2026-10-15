# ISO-W10 RESUME (WORKER-ISO-03) [SELESAI: W10-DONE 09.24 UTC, lihat reports/REVIEW-W10.md], baca ini dulu bila konteks diringkas atau container baru

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
1. Sapuan SOP sisa (08:52Z): HR-SOP-08/10/11/12 dan FAT-SOP-04/05/06 build pass, pemeriksa buta berjalan. COM-SOP-01, 02 belum disunting (luncurkan penyusun saat slot kosong). LEG-SOP-01..03 dan ISMS-SOP-02..05 lolos, di-push.
2. Audit pointer retroaktif (task #5, prompt /tmp/claude-0/w10/prompts/AUDIT.md): selesai dan di-push untuk OPS-PRC-01, OPS-FRM-06, HR-JA-01, HR-FRM-01, HR-FRM-02, HR-RPT-01, HR-SOP-13, COM-FRM-01, COM-FRM-02, FAT-FRM-01, LEG-FRM-01, LEG-FRM-03, LEG-REG-01..03, LEG-RPT-02. Agen mengaudit COM-REG-01, MKT-REG-01, FAT-RPT-02. Sisa: FAT-SOP-01. Spec yang diubah audit (rujukan dikembalikan, diverifikasi worker, bukan pemeriksa buta): HR-SOP-13 policy[2], LEG-REG-01 petunjuk 9, LEG-RPT-02 petunjuk 5.
3. Penutupan: selftest; lint/OOXML/blankscan semua; refcheck2 (keluaran ke reports/w10); metascan; w10_grepgate; modifiedTime 54 sumber ulang; w8.py (Master List + USULAN-OPEN); Laporan_Run bagian "Perubahan ISO-W10"; reports/REVIEW-W10.md (tabel per gerbang, residu bernama, 3 contoh sebelum/sesudah per departemen, GAP, OPEN DECISION, RESIDUAL RISK, retraksi/insiden); ledger current_wave W10-DONE; hapus watchdog (ledger.watchdog_trigger_id); commit "ISO W10 penutupan"; HANDOFF 4 blok.

## Catatan untuk REVIEW-W10 (dikumpulkan sepanjang run)
- GAP pemindai: STARTS_ROLE tidak mengenali butir "6.1 Peran ..." (FAT-FRM-01 nyata 12/13, terukur 0/13).
- Skrip istilah: "lewat" bermakna "terlampaui" salah dipetakan 2 kali (ISMS-REG-04, LEG-REG-04), dibetulkan penyusun; judul klausul ISO dikembalikan (isotitles).
- Label "sedang dalam peninjauan" (G-3) menjadi "sedang dalam review" seragam; MKT-REG-01 nilai status "Dalam Peninjauan" -> "Dalam Review" (OPEN DECISION LEAD).
- Insiden: batas 3 subagen sempat terlampaui (~08:21Z, dihentikan, tanpa perubahan berkas); agen MKT menjalankan git hanya-baca; stempel waktu taksiran dibetulkan.
- Paragraf badan rata kiri-kanan berasal dari template (STYLE hanya mengatur sel); widths_cm generic tidak selalu dihormati LibreOffice (tblLayout autofit).
- Skrip istilah "lewat" bermakna "terlampaui": kejadian ketiga di HR-SOP-11 SLA ("batas tanggapan melalui"), dibetulkan penyusun.
- Insiden: penyusun LEG-SOP menjalankan git hanya-baca (dilaporkan sendiri). Penyusun HR menjalankan build HR-SOP-13 (spec tetap) sehingga out/ dan gate dirender ulang; gate gagal karena audit pointer belum ada, diselesaikan audit retroaktif.
- HR-SOP-08 tata letak 17 halaman rapuh (satu suntingan uji memicu halaman kosong). FAT-SOP-04 keterangan Gambar 1 dipendekkan, isi dipindah ke label node.

## Tambahan 08:57Z
- Audit cakupan label (task #6, prompt /tmp/claude-0/w10/prompts/LABEL.md, kandidat /tmp/claude-0/w10/work/labelscope.json, 113 jalur): batch A (LEG, MKT, OPS, ISMS) agen berjalan; batch B (COM-FRM/REG, FAT, HR-RPT-01, HR-SOP-08, HR-SOP-13) belum.
- Temuan uji kering refcheck2: LEG-SOP-03 exceptions[6][1] "sesuai SNX-ISMS-SOP-01 (butir 4.17)" salah tujuan (butir 4.17 milik LEG-SOP-03). Perbaiki SETELAH audit label batch A selesai: "... sebagai event keamanan sesuai SNX-ISMS-SOP-01 (USULAN untuk pelapor)." + baris audit pointer di notes, rebuild, commit.
- Penutupan refcheck2: 13 TIDAK_ADA cocok adjudikasi W9 berdasar (asal, tujuan, lokasi) tetapi kalimat diubah W10. Rencana: glob refsem juga reports/w10/refsem*.json (tech_fix), tulis reports/w10/refsem_w10.json berisi baris yang dicek ulang worker, lalu refcheck2 tag w10 harus 0 TIDAK_ADA.
- HR-SOP-10/11/12 r2 pemeriksa berjalan; COM-SOP-01/02 pemeriksa berjalan.

## Status akhir (09.24Z)
W10-DONE. 60 lolos, 10 residu (bed1bb6). Semua gerbang penutupan rc 0 (reports/w10/close/). Satu-satunya keputusan menunggu owner: ulang residu. Watchdog menyala 09.22Z dan tidak dipasang ulang. Jangan mulai kerja baru tanpa GO owner.
