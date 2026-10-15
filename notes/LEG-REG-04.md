# Catatan penyusun LEG-REG-04: Company Legal Documents Register

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-REG-04.json. Mode generic, aksi T2 tanpa sumber, wave W7, nomor SNX-LEG-REG-04 (nomor SNX lama dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class None, doc_type_cover "REGISTER". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". Process owner "Line Manager Legal" (jabatan reviewer departemen Legal, tanpa nama; dokumen ini tanpa sumber, lihat USULAN 1). Catatan worklist kosong.

## 1. Sumber

Worklist tidak menunjuk sumber untuk baris ini (sources: []). Dokumen disusun dari struktur kolom dan petunjuk pengisian; sel data faktual kosong, tanpa baris contoh. Bahan di bawah dipakai sebagai kerangka dan pembanding, bukan sebagai isi register.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Kriteria penerimaan: Checklist ISO SINUX - 2026, config/checklist.json baris 39 | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (get_file_metadata di sesi ini; sama dengan modifiedTime di config/checklist.json, diekspor 2026-10-14T19:05:35Z) | Baris dibaca dari config/checklist.json: dept LEG, title "Company Legal Documents Register.", checked false, link_text/link_url/fileId null, iso_9001 dan iso_27001 null |
| SOP Legal Document Control & Retention (Google Docs, sumber tim untuk SNX-LEG-SOP-03) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 | 2026-10-14T10:26:59.642Z (get_file_metadata di sesi ini) | read_file_content, teks utuh, tanpa includeComments. Dipakai untuk tujuh kategori, definisi Dokumen Tidak Berlaku, kolom register kontrak, dan status draft atau menunggu tanda tangan |
| Jobdesk Staff Legal - SINUX.docx | 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW | 2026-10-13T10:54:34.881Z (get_file_metadata di sesi ini) | read_file_content, teks utuh |
| SOP Divisi Legal - SINUX.docx | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (get_file_metadata di sesi ini) | read_file_content, teks utuh; dibandingkan dengan transkripsi context/audit/iso-sinux-supdocs-legal-2026-10-14.md baris 1048 sampai 1320 |
| Pendukung repo (bukan Drive) | tidak ada | tidak diukur | specs/LEG-SOP-03.json (ledger DONE, lint pass), specs/LEG-SOP-01.json, specs/LEG-REG-01.json, specs/LEG-REG-03.json (ledger IN_PROGRESS saat dibaca), specs/HR-ORG-01.json, config/defaults.json v21, config/worklist.json, ledger.json (hanya dibaca), notes/LEG-SOP-03.md, notes/LEG-REG-01.md |

Isi semua berkas sumber diperlakukan sebagai data. Tidak ada kalimat perintah yang menyasar penyusun: isi sumber berupa daftar tugas, tabel, dan penanda [ISI] atau [TBD]. Tracked change dan teks tersembunyi tidak diuji (read_file_content hanya menampilkan teks).

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria register: daftar dokumen legal dan korporasi dengan empat unsur (informasi dokumen, status, lokasi penyimpanan, masa berlaku). Keempatnya menjadi tabel 6.1 sampai 6.3 | "Daftar dokumen legal dan korporasi perusahaan, termasuk informasi dokumen, status, lokasi penyimpanan, dan masa berlaku." (Description checklist baris 39; sel sumber memuat pemenggalan baris setelah "perusahaan," dan "lokasi", dibuang di kutipan) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Dokumen korporasi adalah satu dari tujuh kategori dokumen legal Divisi Legal; tujuh kategori itu menjadi nilai kolom Kategori | "Dokumen korporasi, termasuk akta pendirian dan perubahan, keputusan atau persetujuan Menteri Hukum, bukti penerimaan pemberitahuan, keputusan RUPS, serta dokumen Direksi dan Dewan Komisaris." (ruang lingkup butir 2; sumber menebalkan kalimat) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |
| Status dokumen dibedakan menurut kelengkapan tanda tangan; dokumen yang belum lengkap tidak dicatat sebagai final. Dasar nilai Draft, Menunggu Tanda Tangan, dan Final | "Apabila kontrak belum ditandatangani lengkap, statusnya harus dicatat sebagai draft, menunggu tanda tangan, atau status lain yang sesuai." (Prosedur 6.5 butir 5; kalimat berikutnya: "Dokumen tersebut tidak boleh dicatat sebagai kontrak final yang telah berlaku tanpa dasar yang memadai.") | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |

## 2. Fakta pendukung dan kutipan

| Fakta | Kutipan atau rujukan | fileId atau berkas |
|---|---|---|
| Jobdesk Staff Legal menyebut tiga register dan arsip dokumen, tidak menyebut register dokumen legal. Register ini menjadi register baru sesuai checklist | "Memelihara register permintaan, register kontrak, register perizinan, dan arsip dokumen." | 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW |
| Sumber tim sudah memuat masa berlaku dan lokasi simpan sebagai butir register kontrak | "jangka waktu dan tanggal berakhir;" dan "lokasi penyimpanan dokumen." (daftar informasi register kontrak, Prosedur 6.5 butir 2) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |
| Definisi dokumen tidak berlaku, dipakai untuk arti status Tidak Berlaku | "Dokumen yang telah digantikan, dicabut, berakhir masa berlakunya, atau tidak lagi digunakan untuk tujuan operasional, tetapi mungkin tetap perlu disimpan sebagai rekaman historis atau bukti hukum." (Definisi, "Dokumen Kedaluwarsa atau Tidak Berlaku") | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |
| Lokasi repositori resmi di sumber masih placeholder, jadi kolom lokasi tidak bisa diisi dari sumber | "Staff Legal mengunggah salinan final ke repositori resmi Perusahaan, yaitu [TBD]." dan "Dokumen legal diklasifikasikan (Rahasia, Internal, Publik) dan disimpan pada repositori resmi [ISI]." | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0; 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb (butir 4.7 butir 1) |
| Register dokumen legal sudah dirancang di SNX-LEG-SOP-03 dan dipadankan dengan baris ini; daftar kolomnya dipakai | "Register dokumen legal memuat kolom berikut: ID register, kategori (Kategori 1 sampai 7 di bagian 2), judul, pihak, nomor versi, status, tingkat klasifikasi, lokasi simpan, tanggal berlaku, tanggal berakhir, tanggal pemicu, tanggal akhir masa retensi, dan penanda Legal Hold. Register dokumen legal dipadankan dengan SNX-LEG-REG-04." (butir 4.2) | specs/LEG-SOP-03.json |
| Peran Staff Legal dan Line Manager Legal, pemilik dan pencatat rekaman | Matriks Peran SNX-HR-ORG-01: Line Manager Legal = Legal & Compliance (JA-08), Staff Legal = Legal & Compliance (JA-09), status "(USULAN), menunggu konfirmasi (K-13)". SNX-LEG-SOP-03 butir 4.26: "Line Manager Legal menjadi pemilik rekaman di bagian 11 dan Staff Legal pencatatnya." | specs/HR-ORG-01.json; specs/LEG-SOP-03.json; diubah W9: pemetaan tidak lagi USULAN, pemetaan diputus owner (LEAD G-3 A5) |
| Data baris dan nama | config/defaults.json v21: LEG prepared "Staff Legal", reviewed "Line Manager Legal"; approved "Samuel Kristanto Utomo / President Director"; Samuel di badan dokumen "Direktur Utama" | config/defaults.json |

## 3. Hasil uji

Perintah dijalankan dari /home/claude/iso-run, hasil terakhir:

- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-REG-04.json /tmp/pen-LEG-REG-04/LEG-REG-04.docx` sukses.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-REG-04/LEG-REG-04.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "20 butir (USULAN) menunggu ACC". Keluaran mentah ada di /tmp/pen-LEG-REG-04/lint.json.
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-REG-04/LEG-REG-04.docx`: "All validations PASSED!" (setelah sweep).
- `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-REG-04/LEG-REG-04.docx`: `ok`, 13 halaman, tanpa halaman kosong (setelah sweep).
- Pratinjau PDF lewat soffice (12 halaman sebelum sweep, 13 sesudahnya). Halaman 9 dilihat sebagai gambar: judul 6.1 dan tabel Informasi Dokumen tampil, judul kolom "ID Register" tidak terpotong sesudah lebar kolom dinaikkan ke 2,3 cm. Format template tidak diubah.
- Pemeriksaan silang dengan skrip: semua butir SNX-LEG-SOP-03 yang dikutip di spec (4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.8, 4.11, 4.12, 4.13 sampai 4.15, 4.21, 4.22) ada di specs/LEG-SOP-03.json; prosedur 6.5, 6.6, 6.7 berjudul Penetapan dan Evaluasi Masa Retensi, Legal Hold, dan Pemusnahan Dokumen; butir 4.24 SNX-LEG-SOP-01 ada; sembilan kode SNX yang disebut di badan semuanya ada di tabel Dokumen Terkait (kecuali nomor dokumen ini sendiri).
- tools/selftest.sh tidak dijalankan: tidak ada perubahan di tools/, template/, atau reference/.

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Kriteria baris 39; tujuh kategori dan pengecualian di SNX-LEG-SOP-03 | Dua kalimat tujuan. Lingkup memuat Kategori 1 sampai 7, pengecualian (dokumen departemen lain, daftar peraturan, proses review kontrak), dan batas dengan register kontrak serta SNX-LEG-REG-01 |
| 2 Istilah | Definisi SNX-LEG-SOP-03, tabel Kategori Dokumen, tabel Status Dokumen | Hanya arti istilah dan nilai kolom. Aturannya ada di bagian 3 |
| 3 Ketentuan Pengelolaan | SNX-LEG-SOP-03 butir 4.1 sampai 4.22, prosedur 6.5 sampai 6.7 | 14 butir, satu pelaku per butir, rujukan butir SOP di akhir kalimat |
| 4 Peran | SNX-HR-ORG-01, SNX-LEG-SOP-03 butir 4.26 | Dua peran, tugas merujuk nomor butir Ketentuan |
| 5 Petunjuk Pengisian | Kolom tabel dan SNX-LEG-SOP-03 | 13 butir, satu per kolom atau pasangan kolom; butir 1 dan 11 hanya merujuk Ketentuan agar kalimat tidak ganda |
| 6 Isi Register | Kriteria baris 39 dan SNX-LEG-SOP-03 butir 4.2 | Empat tabel, 10 baris, nomor ID Register 1 sampai 10, semua sel data kosong |
| 7 Dokumen Terkait | Kode yang disebut di badan | Delapan kode |
| 8 Rekaman dan Acuan ISO | SNX-LEG-SOP-03 bagian 11 dan butir 4.26 | Dua baris rekaman; lima klausul dengan satu label "(USULAN, perlu konfirmasi konsultan)" |
| 9 Kesimpulan | Status dokumen, review_period | Dua kalimat |

Diagram tidak dibuat: kriteria tidak meminta alur dan register tidak punya langkah berurutan.

Kriteria penerimaan, unsur demi unsur:

| Unsur kriteria | Letak di dokumen |
|---|---|
| Daftar dokumen legal dan korporasi perusahaan | Bagian 6, tabel 6.1 sampai 6.4, baris 1 sampai 10; Lingkup dan tabel Kategori Dokumen (Kategori 2 = dokumen korporasi) |
| Informasi dokumen | Tabel 6.1: ID Register, Kategori, Judul Dokumen, Nomor Dokumen, Pihak, Nomor Versi |
| Status | Tabel 6.2, kolom Status; lima nilai di bagian 2; Ketentuan butir 3 dan 4 |
| Lokasi penyimpanan | Tabel 6.3, kolom Lokasi Simpan Salinan Elektronik dan Lokasi Dokumen Asli; Ketentuan butir 5 |
| Masa berlaku | Tabel 6.2, kolom Tanggal Berlaku dan Tanggal Berakhir; Petunjuk Pengisian butir 8; Ketentuan butir 2 dan 4 |

Kolom lain (Tingkat Klasifikasi, tabel Retensi) berasal dari SNX-LEG-SOP-03 butir 4.2 dan ditandai USULAN di dokumen.

## 5. Penanganan cacat context/audit

Perintah: `grep -n "Company Legal Documents Regist" context/audit/*.md`. Hasil: satu baris, context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 733 ("5. Company Legal Documents Register.", daftar dokumen Legal yang diminta konsultan). Tidak ada bagian dokumen atau bagian 5 "Catatan kualitas dan celah" untuk dokumen ini, karena belum ada berkas sumbernya. Cacat dokumen sendiri nihil. Cacat dari dokumen Legal tetangga yang relevan untuk register ini ditangani sebagai berikut (context/audit/iso-sinux-supdocs-legal-2026-10-14.md, bagian 5 tiap dokumen):

| Cacat tercatat | Letak audit | Penanganan di dokumen ini |
|---|---|---|
| Register perizinan sumber hanya template kosong, belum menunjukkan legalitas perusahaan | baris 150, butir 1 | Sel data dibiarkan kosong (T2 tanpa sumber); isi dari dokumen asli oleh Staff Legal, open item 1 |
| Register perizinan tanpa kolom lokasi bukti | baris 153, butir 4 | Dua kolom lokasi: Lokasi Simpan Salinan Elektronik dan Lokasi Dokumen Asli (tabel 6.3) |
| Frekuensi pemeriksaan hanya "berkala" | baris 152, butir 3 | Pemeriksaan bulanan atas Tanggal Berakhir (Ketentuan butir 4, USULAN); pengingat jatuh tempo tetap di register kontrak dan SNX-LEG-REG-01, tanpa angka baru |
| Tabel inventaris tanpa kolom klasifikasi; SOP Divisi Legal 4.7 memakai tiga tingkat "Rahasia, Internal, Publik" | baris 548 (butir 9) dan baris 1316 (butir 12) | Kolom Tingkat Klasifikasi dengan empat tingkat SNX-ISMS-PRO-01 (tabel 6.3, Petunjuk 9) |
| Repositori resmi dan periode retensi masih [ISI] | baris 1306 dan 1311 (butir 2 dan 7) | Lokasi memakai folder Google Drive departemen Legal sebagai USULAN (SNX-LEG-SOP-01 butir 4.24); angka retensi tidak ditulis, merujuk SNX-LEG-SOP-03 bagian 11 yang berstatus USULAN |
| Tiga dokumen Legal memakai tiga kosakata status berbeda | baris 552, butir 13 | Dokumen ini memakai lima nilai SNX-LEG-SOP-03 butir 4.3 (status dokumen, bukan status izin); selisih dengan SNX-LEG-REG-01 dan SNX-LEG-REG-03 dicatat di open item 3 |
| Peran "Pejabat yang Berwenang" atau "Manajemen" tanpa jabatan | baris 1042 (butir 13, Legal Risk Register) | Peran itu tidak dipakai; hanya Staff Legal dan Line Manager Legal |
| Skema nomor dan nama dokumen ganda pada register perizinan | baris 156 dan 157, butir 7 dan 8 | Satu nomor SNX-LEG-REG-04 dan satu judul Company Legal Documents Register |

## Asumsi

1. Register ini dimaknai sebagai "register dokumen legal" yang SNX-LEG-SOP-03 butir 4.2 padankan dengan baris ini, jadi Kategori 1 sampai 7 dicakup, termasuk dokumen korporasi (Kategori 2). Kriteria hanya menyebut "dokumen legal dan korporasi"; cakupan penuh tujuh kategori adalah tafsir (USULAN 3).
2. Satu baris untuk satu versi dokumen, karena SNX-LEG-SOP-03 butir 4.6 memberi status per versi (satu versi Final yang berlaku, versi lain Tidak Berlaku).
3. Kolom Lokasi di butir 4.2 dipecah dua mengikuti prosedur 6.3 SNX-LEG-SOP-03, yang mencatat lokasi salinan elektronik dan lokasi tempat aman dokumen asli secara terpisah.
4. Kolom Keputusan Evaluasi ditambahkan ke tabel Retensi karena prosedur 6.5 langkah 6 SNX-LEG-SOP-03 meminta keputusan evaluasi dicatat "di register"; butir 4.2 tidak menyebut kolomnya.
5. Dokumen tanpa pihak lawan memakai SINUX di kolom Pihak, mengikuti bagian NamaPihak pada nama berkas di SNX-LEG-SOP-03 butir 4.4 (USULAN 21).
6. Peran Staff Legal dan Line Manager Legal dipetakan ke JA-09 dan JA-08 menurut SNX-HR-ORG-01 (K-13, menunggu konfirmasi). Atasan Line Manager Legal tidak disebut di badan dokumen; ditutup W9: pemetaan diputus owner (LEAD G-3 A5).
7. Pemilik rekaman register = Line Manager Legal dan pencatat = Staff Legal, mengikuti SNX-LEG-SOP-03 butir 4.26. SNX-LEG-REG-01 dan SNX-LEG-REG-03 menulis pemilik Staff Legal (open item 4).
8. Angka dari sumber tidak diperluas: 90, 60, dan 30 hari serta 2 hari kerja tidak dipakai di dokumen ini. Batas waktu pengarsipan hanya dirujuk ke SNX-LEG-SOP-03 bagian 8.
9. Klasifikasi RESTRICTED (Internal) dari data baris; label footer dipasang renderer.

## USULAN

Lint menghitung 20 penanda "(USULAN)" di docx (setelah sweep). Satu penanda bisa menutup lebih dari satu butir; butir 20 memakai label "(USULAN, perlu konfirmasi konsultan)". Daftar di bawah per butir.

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (prepared Staff Legal, reviewed Line Manager Legal, approved Samuel Kristanto Utomo / President Director) dan process owner Line Manager Legal; dokumen tanpa sumber, nilai dari config/defaults.json | Identity, blok Approval, Peran | owner; diubah W9: nama orang kini di blok Prepared dan Reviewed (config/defaults.json v22) |
| 2 | Pemetaan Staff Legal dan Line Manager Legal ke JA-09 dan JA-08, dan pembagian tugas mencatat versus menetapkan | Peran | Legal; diubah W9: pemetaan ke JA-09 dan JA-08 diputus owner (LEAD G-3 A5); pembagian tugas tetap USULAN |
| 3 | Cakupan Kategori 1 sampai 7 dan dokumen fisik maupun elektronik | Lingkup | Legal |
| 4 | Pengecualian lingkup: daftar peraturan (SNX-LEG-REG-03) dan proses review kontrak sebelum penandatanganan (SNX-LEG-SOP-02) | Lingkup | Legal |
| 5 | Pembagian dengan register kontrak dan SNX-LEG-REG-01: Nomor Dokumen yang sama, jadwal jatuh tempo, pengingat, dan tindak lanjut tetap di sana | Lingkup; Dokumen Terkait | Legal |
| 6 | Kolom Nomor Dokumen (tidak ada di daftar kolom butir 4.2) dan nilai tidak bernomor | Petunjuk 4; tabel 6.1 | Legal |
| 7 | Lima nilai status dari SNX-LEG-SOP-03 butir 4.3 | Istilah, Status Dokumen | Legal |
| 8 | Pemisahan dua kolom lokasi dan nilai tidak ada dokumen fisik; folder Google Drive departemen Legal dan tempat aman sebagai lokasi simpan | Istilah; Petunjuk 10; tabel 6.3 | Legal |
| 9 | Satu baris untuk satu versi dokumen | Ketentuan 1 | Legal |
| 10 | ID Register berupa nomor urut baris dan tidak dipakai ulang | Petunjuk 2 | Legal |
| 11 | Pemeriksaan register setiap bulan atas Tanggal Berakhir dan perubahan status menjadi Tidak Berlaku | Ketentuan 4 | Legal |
| 12 | Nilai tidak ada masa berlaku untuk dokumen tanpa tanggal berakhir | Petunjuk 8 | Legal |
| 13 | Staff Legal mengusulkan dan Line Manager Legal menetapkan Tingkat Klasifikasi; tingkat dasar di SNX-LEG-SOP-03 butir 4.12 | Ketentuan 6 dan 7; Petunjuk 9 | Legal |
| 14 | Legal Hold ditetapkan Line Manager Legal; empat kolom tabel Retensi (Tanggal Pemicu, Tanggal Akhir Masa Retensi, Penanda Legal Hold, Keputusan Evaluasi) | Ketentuan 8 sampai 11; tabel 6.4 | Legal |
| 15 | Baris dokumen yang dimusnahkan tetap disimpan; register berlaku sampai digantikan; periode retensi per kategori mengikuti SNX-LEG-SOP-03 bagian 11 | Ketentuan 12; Rekaman | Legal dan FAT (irisan periode 10 tahun dengan arsip FAT, seperti di notes/LEG-SOP-03.md) |
| 16 | Line Manager Legal memeriksa kelengkapan dan keakuratan isi register setiap tahun | Ketentuan 13 | Legal |
| 17 | Register disimpan di folder Google Drive departemen Legal dengan klasifikasi RESTRICTED (Internal) | Ketentuan 14; Rekaman | Legal |
| 18 | Pemilik rekaman Line Manager Legal dan pencatat Staff Legal | Rekaman | Legal |
| 19 | Pemetaan delapan dokumen di tabel Dokumen Terkait | Dokumen Terkait | Legal |
| 20 | Klausul ISO 9001:2015 7.5.2 dan 7.5.3; ISO/IEC 27001:2022 7.5.3, Annex A 5.12 dan 5.33. Checklist baris 39 tidak memberi acuan (iso_9001 dan iso_27001 null) | Rekaman dan Acuan ISO | owner (setelah konfirmasi konsultan) |
| 21 | Kolom Pihak diisi SINUX untuk dokumen tanpa pihak lain; SNX-LEG-SOP-03 butir 4.4 mengatur nama berkas, dan kalimatnya berlabel USULAN di sana (ditambahkan saat sweep) | Petunjuk 5; tabel 6.1 | Legal |

## Open items

1. Semua sel data register kosong: judul, nomor, pihak, versi, status, tanggal, klasifikasi, lokasi, dan retensi tidak ada di sumber, dan sumber tim hanya berisi kerangka. Register belum bisa menjadi bukti audit sampai Staff Legal mengisinya dari dokumen asli. Penentu: Legal.
2. Batas dengan register kontrak dan SNX-LEG-REG-01: Akta Pendirian, Anggaran Dasar, dan izin bisa tercatat di dua register, dengan Nomor Dokumen, status, dan masa berlaku di keduanya. Dokumen ini hanya menetapkan Nomor Dokumen sebagai kunci pencocokan. Perlu diputuskan satu register sebagai pemilik tiap jenis (sama dengan open item 8 notes/LEG-REG-01.md). Penentu: Legal.
3. Kosakata status Legal belum satu: dokumen ini memakai Draft, Menunggu Tanda Tangan, Final, Tidak Berlaku, Dimusnahkan; SNX-LEG-REG-01 memakai Berlaku, Perlu Diperbarui, Kedaluwarsa, Belum Diverifikasi, Belum Tersedia, Tidak Berlaku untuk Perusahaan; SNX-LEG-REG-03 memakai Berlaku, Perlu Diperbarui, Dicabut, Dalam Pemantauan, Belum Diverifikasi, Tidak Relevan untuk SINUX. Arti "Tidak Berlaku" berbeda antara dokumen ini dan SNX-LEG-REG-01. Penentu: Legal.
4. Pemilik rekaman register: SNX-LEG-SOP-03 butir 4.26 menunjuk Line Manager Legal (pencatat Staff Legal); SNX-LEG-REG-01 dan SNX-LEG-REG-03 menulis pemilik Staff Legal. Penentu: Legal.
5. Periode masa retensi per kategori masih USULAN di SNX-LEG-SOP-03 bagian 11 (usulan 10 tahun untuk Kategori 1, 3, 5 beririsan dengan arsip FAT dan menunggu Samuel). Kolom Tanggal Akhir Masa Retensi tidak bisa diisi sebelum periode diputus. Penentu: Legal, FAT, dan Samuel.
6. Lokasi simpan: sumber tim menulis repositori resmi "[TBD]" dan SOP Divisi Legal menulis "[ISI]"; folder Google Drive departemen Legal adalah USULAN (SNX-LEG-SOP-01 butir 4.24). Lokasi tempat aman untuk dokumen asli belum ditetapkan di sumber mana pun. Penentu: Legal.
7. Kolom Nomor Dokumen, Keputusan Evaluasi, dan pemisahan dua kolom lokasi melampaui daftar kolom butir 4.2 SNX-LEG-SOP-03. Bila Legal menolaknya, butir 4.2 atau tabel di dokumen ini diselaraskan. Penentu: Legal.
8. Pemeriksaan bulanan atas Tanggal Berakhir tidak punya padanan di SNX-LEG-SOP-03: langkah 3 prosedur 6.5 hanya memeriksa tanggal akhir masa retensi. Penentu: Legal.
9. Kutipan dari SNX-LEG-SOP-03, SNX-LEG-SOP-01, SNX-LEG-REG-01, SNX-LEG-REG-03, dan SNX-HR-ORG-01 diambil dari specs di repo, bukan dokumen final. SNX-LEG-REG-03 berstatus IN_PROGRESS saat dibaca, jadi kalimat pengecualian lingkup yang merujuknya perlu dicek ulang setelah dokumen itu selesai. Penentu: orkestrator.
10. Komentar Drive pada berkas sumber tidak diminta (read_file_content tanpa includeComments), dan tracked change atau teks tersembunyi tidak diuji. Penentu: orkestrator.

## 6. Pemeriksaan mutu (dua pertanyaan)

**Apa yang membuat teks ini terdengar buatan AI?** Setelah draf pertama, empat hal ditemukan dan diperbaiki:
- Lima baris acuan ISO semuanya diawali "Register memuat" atau "Register mencatat". Kalimatnya diganti, tiap baris menyebut isi yang tercatat dan lokasinya di register.
- Definisi status Final dan Dimusnahkan memberi dokumen kata kerja manusia ("menyelesaikan pemeriksaan") dan mengulang kata "dokumen" dua kali dalam satu kalimat. Keduanya ditulis ulang dalam bentuk pasif tanpa pelaku semu.
- Petunjuk Pengisian butir 1 dan 11 mengulang kalimat Ketentuan butir 2 dan 8. Keduanya dipendekkan menjadi rujukan nomor butir.
- Label "(USULAN)" ditempel di tiap kutipan butir SOP. Label dipertahankan hanya pada butir yang memang belum diputus, dan tidak diulang pada kutipan yang sumbernya sudah berlabel.
Yang tetap: tiga belas butir Petunjuk Pengisian berpola "Kolom X memuat ...". Pola itu dipertahankan karena tiap butir menjelaskan satu kolom, dan penyeragaman membantu pengisi.

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**
- Nama: hanya Samuel Kristanto Utomo (config/defaults.json, blok Approval) dan "Direktur Utama" di badan dokumen. Staff Legal dan Line Manager Legal adalah nama peran, dipetakan ke jabatan Legal & Compliance (JA-09 dan JA-08) di SNX-HR-ORG-01 dan berlabel USULAN. Tidak ada nama orang lain; diubah W9: pemetaan tidak lagi USULAN, pemetaan diputus owner (LEAD G-3 A5); nama orang hanya di blok Prepared dan Reviewed.
- Tanggal: nol. Effective Date kosong.
- Angka: tidak ada angka faktual. "Baris 1 sampai 10" adalah ukuran lembar, bukan fakta. "v01, v02" dari SNX-LEG-SOP-03 butir 4.5. Frekuensi "setiap bulan" dan "setiap tahun" berlabel USULAN (USULAN 11 dan 16). Angka 90, 60, 30 hari dan 2 hari kerja sengaja tidak dipakai.
- Sistem: Google Drive (USULAN, SNX-LEG-SOP-01 butir 4.24). GLPI dan Zammad tidak disebut karena register tidak punya langkah tiket.
- Isi tujuh kategori dan arti status: kutipan dari sumber tim (fileId 12WUHJ...) dan SNX-LEG-SOP-03; lima nilai status berlabel USULAN.
- Tanpa sumber dan berlabel: nilai tidak bernomor, tidak ada masa berlaku, dan tidak ada dokumen fisik; ID Register berupa nomor urut; satu baris per versi; kolom Nomor Dokumen dan Keputusan Evaluasi; klausul ISO.
- Tidak dinyatakan "belum ada" untuk dokumen lain: checklist baris 39 checked false, tetapi badan dokumen tidak menulis status keberadaan dokumen lain selain merujuk kode dan fungsinya.

## Sweep

Putaran penghalusan atas dasar qa/LEG-REG-04.verify.json (verdict PASS, nol blocking). Hanya spec dan notes yang diubah; fakta, angka, nama, dan struktur bagian tetap. Salinan spec sebelum sweep: /tmp/pen-LEG-REG-04/LEG-REG-04.before-sweep.json.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1a | Label USULAN pada pemetaan jabatan (Peran) | "Nama jabatan Staff Legal dan Line Manager Legal mengikuti SNX-HR-ORG-01." | "Staff Legal dan Line Manager Legal adalah nama peran yang dipetakan ke jabatan Legal & Compliance (JA-09 dan JA-08) di SNX-HR-ORG-01 (USULAN)." |
| 1b | Label USULAN pada pemetaan jabatan (Dokumen Terkait) | "Sumber nama jabatan Line Manager Legal dan Staff Legal." | "Sumber nama peran Line Manager Legal dan Staff Legal. Pemetaannya ke jabatan Legal & Compliance berstatus (USULAN)." |
| 1c | Label dan rujukan aturan Pihak = SINUX (Petunjuk 5) | "kolom diisi SINUX (SNX-LEG-SOP-03 butir 4.4)." | "kolom diisi SINUX, sama dengan bagian NamaPihak pada nama berkas (SNX-LEG-SOP-03 butir 4.4, USULAN)." Butir baru USULAN 21 |
| 1d | Dokumen asli versus dokumen elektronik, dan Kategori yang ditentukan pencatat (Ketentuan 2) | "Staff Legal mengisi Kategori, Judul Dokumen, ... dan Tanggal Berakhir dari dokumen asli." | "Staff Legal menentukan Kategori menurut bagian Istilah, dan mengisi Judul Dokumen, ... dan Tanggal Berakhir dari dokumen asli atau, untuk dokumen yang hanya ada secara elektronik, dari salinan elektroniknya." |
| 1e | Dokumen asli versus dokumen elektronik (Petunjuk 8) | "memuat tanggal yang tertulis pada dokumen asli." | "memuat tanggal yang tertulis pada dokumen asli atau salinan elektroniknya." |
| 1f | Pasif tanpa pelaku (Isi Register, paragraf pembuka) | "Baris 1 sampai 10 disediakan dan semua sel data kosong. Kolom ID Register sudah bernomor. Nilai pada kolom ... dipilih dari nilai yang tertulis di bagian Istilah dan Petunjuk Pengisian." | "Baris 1 sampai 10 sudah bernomor di kolom ID Register, dan semua sel datanya kosong. Staff Legal memilih nilai kolom ... dari nilai yang tertulis di bagian Istilah dan Petunjuk Pengisian." |
| 1g | Pasif tanpa pelaku dan isi berulang: baris dokumen dimusnahkan (Ketentuan 12) | "Barisnya tetap disimpan di register (USULAN)." | "Staff Legal tetap menyimpan barisnya di register (USULAN)." |
| 1h | Isi berulang: baris dokumen dimusnahkan (Petunjuk 2) | "... tidak dipakai ulang untuk dokumen lain, termasuk bila dokumennya sudah dimusnahkan (USULAN)." | "... dan Staff Legal tidak memakainya ulang untuk dokumen lain (USULAN)." |
| 1i | Isi berulang: baris dokumen dimusnahkan (Rekaman, kolom Retensi) | "Berlaku sampai digantikan. Baris dokumen yang dimusnahkan tetap disimpan (USULAN, SNX-LEG-SOP-03 bagian 11)." | "Berlaku sampai digantikan (USULAN, SNX-LEG-SOP-03 bagian 11). Baris dokumen yang dimusnahkan mengikuti Ketentuan butir 12." |
| 1j | Isi berulang: pemeriksaan bulanan (Peran) | "memeriksa register tiap bulan," | "memeriksa register," (frekuensi hanya di Ketentuan 4) |
| 1k | Isi berulang: pemeriksaan bulanan (Kesimpulan) | "Line Manager Legal meninjau dokumen ini setiap tahun, dan Staff Legal memeriksa isi register setiap bulan menurut Ketentuan butir 4." | "Line Manager Legal meninjau dokumen ini setiap tahun. Staff Legal memeriksa isi register menurut Ketentuan butir 4." |
| 2a | Line Manager Legal dan Staff Legal sebagai nama peran yang dipetakan ke Legal & Compliance (JA-08, JA-09) | lihat 1a dan 1b | lihat 1a dan 1b; tabel Peran, Ketentuan, dan Rekaman sudah memakai "Line Manager Legal" dan "Staff Legal" sebagai nama peran tanpa kata "jabatan" |
| 2b | Pemilik rekaman Legal mengikuti SNX-LEG-SOP-03 | Tidak berubah: tabel Rekaman menulis pemilik Line Manager Legal dan pencatat Staff Legal | Sudah selaras dengan SNX-LEG-SOP-03 butir 4.26, jadi tidak ada perubahan. Selisihnya ada di SNX-LEG-REG-01 dan SNX-LEG-REG-03 (pemilik Staff Legal), bukan di dokumen ini; tetap open item 4 |

Temuan verifikator yang tidak diubah karena di luar butir sweep:
- "Lokasi simpan" (istilah) versus "lokasi penyimpanan" (judul tabel 6.3 dan Tujuan): dipertahankan karena kata "lokasi penyimpanan" berasal dari kriteria baris 39. Pemutus bila ingin diseragamkan: orkestrator.
- Irisan dengan SNX-LEG-REG-01 dan perbedaan arti Tidak Berlaku: tetap open item 2 sampai 4, pemutus Legal.
- Cacat context/audit: tidak ada tindakan baru (notes bagian 5).

Uji sesudah sweep: render sukses; lint_doc generic `pass: true`, fails kosong, warn "20 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan `ok` (13 halaman). Nol em-dash dan en-dash di spec (grep).


## ISO-W9

Putaran perbaikan ISO-W9 (LEAD G-3 A5, hasil pemeriksa makna R457). Hanya butir di bawah yang berubah.

| butir | sebelum | sesudah |
|---|---|---|
| meta.approval, blok Prepared dan Reviewed | Prepared "Staff Legal"; Reviewed "Line Manager Legal" | Prepared "Alif Altamziz / Staff Legal"; Reviewed "Ester Febe Utomo / Line Manager Legal" (config/defaults.json v22 prepared_reviewed.LEG) |
| A5, Peran, paragraf penjelas | "... (JA-09 dan JA-08) di SNX-HR-ORG-01 (USULAN). Pembuat ..." | "... (JA-09 dan JA-08) di SNX-HR-ORG-01. Pembuat ..."; USULAN pembagian tugas mengikuti SNX-LEG-SOP-03 tetap |
| A5, Dokumen Terkait, baris SNX-HR-ORG-01 | "... Pemetaannya ke jabatan Legal & Compliance berstatus (USULAN)." | "... Sumber nama peran Line Manager Legal dan Staff Legal, yang dipetakan ke jabatan Legal & Compliance (JA-09 dan JA-08)." |
| Rujukan, Ketentuan butir 5 (hasil pemeriksa makna R457) | "5. Staff Legal mencatat Lokasi Simpan Salinan Elektronik dan Lokasi Dokumen Asli dalam batas waktu pengarsipan di SNX-LEG-SOP-03 bagian 8." | "5. Staff Legal mencatat Lokasi Simpan Salinan Elektronik dalam batas waktu pengarsipan di SNX-LEG-SOP-03 bagian 8, dan mencatat Lokasi Dokumen Asli menurut SNX-LEG-SOP-03 prosedur 6.3 langkah 4." Dasar: bagian 8 (2 hari kerja) hanya untuk 6.3 langkah 1 dan 2; 6.3 langkah 4 tidak punya batas waktu di bagian 8 |
| R2, Dokumen Terkait, baris SNX-HR-ORG-01 | "... (JA-09 dan JA-08)." (urutan kode terbalik dari urutan peran) | "... (JA-08 dan JA-09)." |
| R2, hygiene notes, USULAN 1 dan 2, Asumsi 6, Fakta baris Peran, Sweep baris Nama | tanpa penanda W9 pada baris; baris Nama menyatakan tidak ada nama orang lain dan pemetaan berlabel USULAN | ditambah "diubah W9" atau "ditutup W9" pada baris itu |

Open item:

- Open item 2 (pemetaan ke JA-09 dan JA-08): bagian pemetaan ditutup W9: diputus owner (LEAD G-3 A5). Pembagian tugas mencatat versus menetapkan tetap terbuka (Legal).
- Asumsi 6 (K-13, menunggu konfirmasi): ditutup W9: pemetaan diputus owner (LEAD G-3 A5).
- Rujukan Ketentuan butir 5 ke SNX-LEG-SOP-03 bagian 8: diubah W9: hanya berlaku untuk Lokasi Simpan Salinan Elektronik.
- R2: urutan kode jabatan di Dokumen Terkait baris SNX-HR-ORG-01 diperbaiki menjadi (JA-08 dan JA-09); baris notes terkait kini memuat penanda W9 di barisnya sendiri; tidak ada baris dihapus.
