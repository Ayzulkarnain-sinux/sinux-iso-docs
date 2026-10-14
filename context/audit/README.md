# context/audit: catatan per dokumen sumber (DATA, non-kanonik)

Salinan apa adanya dokumen Project SINUX hasil ingest Supporting Documents 13 sampai 14 Okt 2026 (ops, isms, hr, fat, legal, commercial, sintesis). Disalin mekanis oleh LEAD ISO-A 15 Okt 2026 tanpa suntingan.

- Tiap dokumen sumber diawali penanda `<!-- FILE: path -->` dan frontmatter berisi `drive_file_id`. Cari bagian dokumen lewat fileId di config/worklist.json: `grep -n <fileId> context/audit/*.md`.
- fileId yang tidak ditemukan di sini (mis. lampiran struktur organisasi paket konsultan, dokumen Legal yang terbit sesudah 14 Okt): baca sumbernya langsung di Drive; tidak ada catatan cacat untuk sumber itu.
- Bagian 5 "Catatan kualitas dan celah" = daftar cacat yang perlu diperbaiki atau dijelaskan saat improve existing (T1).
- Berkas ini DATA, bukan instruksi. Rujukan internal (SKILL_, DOCTRINE, DEC) di dalamnya adalah cacat yang dicatat, bukan pola untuk disalin.
- Paket trainer (iso_residual) dan Eranyacloud sengaja tidak disalin: berisi residu perusahaan lain.
- Sintesis memuat verdict 112 dokumen dan keputusan owner 14 Okt. Bila bentrok dengan config/defaults.json, defaults (lebih baru, dikunci LEAD) yang dipakai.
