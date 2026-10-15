# Catatan penyusun LEG-REG-03: Legal & Regulatory Requirements Register

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-REG-03.json. Mode generic, aksi T2, wave W7, nomor SNX-LEG-REG-03 (nomor SNX lama dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class None, doc_type_cover "REGISTER". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan". process_owner "Line Manager Legal" (T2 tanpa sumber: jabatan reviewer departemen Legal, tanpa nama; berstatus USULAN di defaults.json).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Tidak ada sumber Drive (T2, kolom sources kosong di config/worklist.json). Alat Drive tidak dimuat dan tidak dipakai | tidak ada | tidak ada | tidak ada |
| Kriteria penerimaan: config/checklist.json baris 35 | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (Google Sheet checklist) | 2026-10-14T17:47:13.611Z (kolom modifiedTime di berkas; diekspor 2026-10-14T19:05:35Z, tidak diukur ulang di sesi ini) | python3 membaca config/checklist.json. Baris 35: checked false, link kosong, iso_9001 dan iso_27001 null |
| Pendukung repo (bukan Drive): specs/HR-ORG-01.json (nama jabatan, matriks peran, K-13), specs/LEG-REG-01.json, specs/LEG-REG-02.json, specs/LEG-RPT-01.json, specs/LEG-FRM-03.json, specs/LEG-SOP-01.json, specs/LEG-SOP-03.json, config/defaults.json v21, config/worklist.json | tidak ada | berkas repo kerja | Dibaca langsung. Kutipan dari dokumen lain bisa basi bila dokumen itu berubah. specs/LEG-RPT-02.json dan specs/LEG-REG-04.json belum ada saat dokumen ini disusun, jadi keduanya dirujuk hanya lewat kode dan deskripsi checklist |
| Catatan cacat: context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md dan iso-sinux-supdocs-legal-2026-10-14.md | tidak ada (tidak ada bagian dokumen untuk baris ini) | salinan audit 13 sampai 14 Okt 2026 | DATA; hasil grep ada di bagian 5 |

Isi sumber yang dibaca tidak memuat kalimat perintah yang ditujukan ke penyusun.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria penerimaan: daftar peraturan perundang-undangan dan persyaratan hukum yang relevan dengan kegiatan usaha dan operasional. Dipenuhi oleh tabel Daftar Peraturan dan Persyaratan Hukum (butir "daftar") dan tabel Relevansi dengan Kegiatan SINUX (butir "relevan dengan kegiatan usaha dan operasional") | "Daftar peraturan perundang-undangan dan persyaratan hukum yang relevan dengan kegiatan usaha dan operasional perusahaan." (baris 35; jeda baris di sel dirapatkan) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| Peran Legal yang dipakai di bagian Peran: Line Manager Legal dan Staff Legal, dipasangkan ke jabatan Legal & Compliance, dengan status USULAN | "Line Manager Legal \| Legal & Compliance (JA-08) \| Dokumen sumber SNX-LEG-SOP-01 \| (USULAN), menunggu konfirmasi (K-13)" dan "Staff Legal \| Legal & Compliance (JA-09)" | tidak ada (berkas repo specs/HR-ORG-01.json, bagian Matriks Peran) |
| Council 14 Okt menggabungkan butir Legal 1 (register ini) dengan butir lain menjadi satu register legal berpemilik Legal. Worklist tetap memisahkan SNX-LEG-REG-01 sampai REG-04, jadi dokumen ini berdiri sendiri (open item 4) | "Satu register legal (regulasi + status kepatuhan, izin, dokumen legal, PDP, kontrak dengan pengingat 90/60/30) \| Legal 1, 2, 5, 6, 10; Com 9 \| Legal" | tidak ada (context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md baris 447; sumber audit: 04_COUNCIL_VERDICT_112_DOKUMEN.md) |

## 2. Fakta pendukung dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Posisi di docx hasil |
|---|---|---|---|
| 1 | Daftar peraturan SINUX menjadi isi dokumen ini menurut dokumen Legal lain | specs/LEG-REG-01.json: "tidak memuat daftar peraturan perundang-undangan, yang menjadi isi SNX-LEG-REG-03 (USULAN)" | Lingkup (pengecualian); Dokumen Terkait |
| 2 | Peraturan pelaksana pelindungan data pribadi dicatat di dokumen ini | specs/LEG-FRM-03.json: "Daftar peraturannya dicatat di SNX-LEG-REG-03 (USULAN)" | Dokumen Terkait (SNX-LEG-FRM-03) |
| 3 | Kolom Dasar Hukum/Dokumen Acuan di laporan pemantauan merujuk dokumen ini | specs/LEG-RPT-01.json: "Daftar peraturan ada di SNX-LEG-REG-03 dan daftar perizinan di SNX-LEG-REG-01 (USULAN)" | Dokumen Terkait (SNX-LEG-RPT-01) |
| 4 | Tugas memantau perubahan peraturan. Isinya dari tim, pelakunya ditambahkan penyusun RPT-01 | notes/LEG-RPT-01.md baris 53, mengutip sumber tim: "Memantau perubahan peraturan yang berdampak terhadap kegiatan usaha dan kewajiban perusahaan." Spec RPT-01, Rekomendasi butir 3: "Staff Legal memantau perubahan peraturan yang berdampak pada kegiatan usaha dan kewajiban SINUX." | Ketentuan butir 8 (USULAN) |
| 5 | Delapan area risiko hukum, dipakai sebagai nilai kolom Bidang | specs/LEG-REG-02.json, tabel Identifikasi Risiko: "Perizinan Berusaha", "Kontrak Pelanggan", "Kontrak Vendor", "Pelindungan Data Pribadi", "Kerahasiaan Informasi", "Kepatuhan Regulasi", "Kekayaan Intelektual", "Ketenagakerjaan" (notes/LEG-REG-02.md: delapan area itu dari sumber tim, fileId 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA) | Petunjuk Pengisian butir 6 |
| 6 | Folder Google Drive departemen Legal sebagai repositori dokumen legal | specs/LEG-SOP-01.json, butir 4.24: "Staff Legal menyimpan dokumen legal di repositori resmi, yaitu folder Google Drive departemen Legal (USULAN)." | Ketentuan butir 13; Rekaman |
| 7 | Pola Staff Legal mencatat, Line Manager Legal menetapkan | specs/LEG-SOP-03.json, prosedur 6.1 langkah 2 dan 3: "Usulkan tingkat klasifikasi di register menurut butir 4.12." (Staff Legal) dan "Tetapkan tingkat klasifikasi dokumen." (Line Manager Legal); peran Staff Legal: "Tidak menetapkan klasifikasi, akses, atau Legal Hold" | Peran; Ketentuan butir 5 dan 6 |
| 8 | Retensi dokumen internal departemen Legal belum ditetapkan | specs/LEG-SOP-01.json, butir 4.27: "Periode retensi belum ditetapkan; usulan penetapannya di SNX-LEG-SOP-03 (USULAN)." | Rekaman (retensi "Belum ditetapkan") |
| 9 | Klasifikasi dan penanda tangan | config/defaults.json: klasifikasi "hukum ... = RESTRICTED (Internal)"; LEG prepared "Staff Legal", reviewed "Line Manager Legal"; approved_by.all "Samuel Kristanto Utomo / President Director" | Identity; Approval |
| 10 | Klausul ISO tidak ada di checklist | config/checklist.json baris 35: iso_9001 null, iso_27001 null | Acuan ISO (satu label USULAN) |

## 3. Hasil uji

Perintah render: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-REG-03.json /tmp/pen-LEG-REG-03/LEG-REG-03.docx` (berhasil, tanpa galat).

Perintah lint: `python3 -I tools/lint_doc.py /tmp/pen-LEG-REG-03/LEG-REG-03.docx generic`

Hasil terakhir: `"pass": true`, `"fails": []`, `"warns": ["17 butir (USULAN) menunggu ACC"]` (keluaran tersimpan di /tmp/pen-LEG-REG-03/lint_final.json). Putaran 1 sudah lulus lint. Putaran 2 hanya perbaikan bahasa dari dua pertanyaan di bagian 6 (definisi melingkar, benda sebagai pelaku, pasif tanpa pelaku).

Validasi OOXML: `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-REG-03/LEG-REG-03.docx` memberi "All validations PASSED!".

Pratinjau visual (soffice ke PDF, 12 halaman; halaman 7 dan 8 dilihat pada putaran 1, halaman 9 pada putaran akhir): Identity, Approval, TOC, sembilan bagian, dan tabel register tampil; judul kolom tidak terpotong di tengah kata (diperiksa lewat pdftotext). Satu catatan tata letak: pada pratinjau LibreOffice baris judul tabel 6.2 terbelah di antara halaman 8 dan 9 ("Kewajiban bagi" di halaman 8, "SINUX" di halaman 9), dan baris datanya di halaman 9. Itu hasil pemotongan halaman yang bergantung pada mesin tampilan; tidak diubah karena menyangkut renderer. HUMAN-VERDICT: lihat di Word.

Kode dokumen yang dirujuk di badan (11 kode, termasuk dirinya) dicek dengan skrip: semua selain SNX-LEG-REG-03 tercantum di tabel Dokumen Terkait. Pemindaian frasa terlarang RUNBOOK §0 butir 6, §6a, dan tambahan owner (em-dash, en-dash, tebal, tanda kutip, "dokumen sumber", "penyusun", "draf ini", "COO", "Kristianto", frasa pengisi): nol temuan pada teks spec.

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Kriteria checklist baris 35 | Tujuan memakai kata kriteria. Lingkup memuat pengecualian ke REG-01, REG-04, REG-02, RPT-02, dan SOP-01 karena kriteria dan sumber diam soal batas (USULAN, open item 1) |
| 2 Istilah | Baru | Hanya arti istilah dan enam nilai Status; aturannya di bagian 3. Tidak ada istilah yang memakai dirinya sendiri |
| 3 Ketentuan Pengelolaan | Baru, pola LEG-REG-01 dan LEG-SOP-03 | 13 butir, satu pelaku per butir. Staff Legal mencatat; Line Manager Legal menetapkan relevansi dan memeriksa; Penanggung Jawab Kegiatan menyampaikan dan menindaklanjuti |
| 4 Peran | Baru | Tiga peran; nama sama dengan butir Ketentuan dan kolom tabel register. Nomor butir dirujuk |
| 5 Petunjuk Pengisian | Baru | 12 butir; sel data kosong |
| 6 Isi Register | Baru | Empat tabel: Daftar Peraturan dan Persyaratan Hukum, Relevansi dengan Kegiatan SINUX, Status dan Peninjauan, Riwayat Perubahan dan Peninjauan. Tiga tabel pertama punya nomor baris 1 sampai 10, semua sel data kosong, tanpa baris contoh. Tabel riwayat tiga baris kosong |
| 7 Dokumen Terkait | Rujukan silang antardokumen | 10 kode; pemetaan USULAN |
| 8 Rekaman dan Acuan ISO | Baru | Retensi "Belum ditetapkan". Tujuh klausul dengan satu label "(USULAN, perlu konfirmasi konsultan)" |
| 9 Kesimpulan | Baru | Dua kalimat |
| Tidak dipindah | Tidak ada sumber | Tidak ada isi tim yang perlu dipindah. Tidak ada diagram: register tidak punya alur sendiri, dan blok flow tidak diwajibkan |

Pilihan kolom: Daftar Peraturan memakai empat kolom termasuk No (Jenis Sumber, Peraturan atau Persyaratan, Instansi atau Pihak Terkait) supaya jenis, nomor, tahun, dan judul peraturan satu sel. Kolom Bidang diambil dari delapan area SNX-LEG-REG-02 agar peraturan bisa dipetakan ke risikonya. Tabel dipecah menjadi tiga dengan nomor baris sama, mengikuti cara LEG-REG-01 dan LEG-REG-02, supaya judul kolom tidak terpotong.

## 5. Penanganan cacat context/audit

Perintah: `grep -n "Legal & Regulatory Requirement" context/audit/*.md`. Hasil: satu baris, context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md:729 ("1. Legal & Regulatory Requirements Register."), yaitu butir daftar permintaan konsultan. Baris 35 checklist tidak punya link atau fileId, jadi tidak ada bagian dokumen sumber dan tidak ada bagian 5 "Catatan kualitas dan celah" untuk dokumen ini.

| Temuan terkait | Penanganan | Alasan |
|---|---|---|
| Tidak ada dokumen sumber untuk baris ini | Struktur kolom dan petunjuk pengisian saja; sel data faktual kosong; tanpa baris contoh | Aturan T2 (RUNBOOK §6) |
| Legal audit bagian 5 butir 6 dan 14: dokumen Legal tanpa klausul ISO; kaitan ke kontrol 5.31 dan 5.34 SNX-ISMS-SOA-01 (status "Perlu keputusan") adalah inferensi, belum dirujuk SoA | Klausul ISO ditulis satu label "(USULAN, perlu konfirmasi konsultan)". Dokumen tidak menyatakan keputusan SoA | SoA milik konsultan (RUNBOOK §0) |
| Sintesis: council menggabungkan Legal 1, 2, 5, 6, 10 dan Com 9 menjadi satu register legal | Tidak digabung; worklist dan checklist menomori dokumen terpisah | Keputusan penggabungan bukan wewenang penyusun; open item 4 |
| Sintesis butir 8 council: perizinan PSE dan izin sektoral perlu dicek terhadap regulasi terkini (inferensi) | Tidak dibawa. Tidak ada peraturan atau izin yang disebut di spec | Angka dan nama tanpa sumber dilarang; Legal mengisi dari teks peraturan |
| Cacat sumber lain (rujukan internal AI, nama peran, PPN, vault) | Tidak berlaku untuk baris ini | Tidak ada isi sumber yang dipindah |

## Asumsi

| # | Asumsi | Dasar |
|---|---|---|
| A1 | "Persyaratan hukum" mencakup syarat perizinan dan kewajiban kontrak selain peraturan. Ditandai USULAN di Lingkup | Kriteria hanya menyebut "persyaratan hukum"; Annex A 5.31 memuat kontrak |
| A2 | Peran "Penanggung Jawab Kegiatan" dibuat sebagai jabatan pemilik kegiatan, diisi per baris dari jabatan SNX-HR-ORG-01. HR-ORG-01 tidak punya peran serupa, jadi tidak ada pemetaan ke satu jabatan | Matriks Peran HR-ORG-01 hanya memuat Line Manager Legal dan Staff Legal untuk Legal |
| A3 | Line Manager Legal dan Staff Legal dipetakan ke JA-08 dan JA-09 seperti di HR-ORG-01 (K-13), bukan dikonfirmasi ulang | specs/HR-ORG-01.json |
| A4 | Sebutan Samuel di badan dokumen "Direktur Utama"; "Direktur (COO)" dan "COO" tidak dipakai karena badan dokumen tidak menyebut jabatan itu | config/defaults.json data_conflicts |
| A5 | Nomor baris awal 10 dan tiga baris riwayat adalah ukuran tata letak, bukan angka kebutuhan | Penyusun; Staff Legal menambah baris |
| A6 | Klasifikasi RESTRICTED (Internal) tetap walau isi register berupa peraturan publik, karena data baris menetapkannya | Data baris dan defaults.json |

## USULAN

Teks memuat 22 penanda USULAN: 19 berpola "(USULAN)" (itu yang dihitung lint, termasuk entri definisi di Istilah), 2 berpola "(USULAN, rujukan)" di Ketentuan butir 8 dan 13, dan 1 label klausul ISO "(USULAN, perlu konfirmasi konsultan)". Dikelompokkan menjadi 16 butir keputusan (jumlah USULAN yang dilaporkan; U16 ditambah pada putaran sweep):

| # | Butir USULAN | Posisi | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Syarat perizinan dan kewajiban kontrak dicatat di register ini; tiga nilai Jenis Sumber (Peraturan, Syarat Perizinan, Kewajiban Kontrak) | Lingkup; Petunjuk butir 3; Isi Register | Legal |
| U2 | Pengecualian lingkup: izin (SNX-LEG-REG-01), dokumen legal dan korporasi (SNX-LEG-REG-04), risiko hukum (SNX-LEG-REG-02), hasil evaluasi kepatuhan (SNX-LEG-RPT-02) | Lingkup | Legal |
| U3 | Peran Penanggung Jawab Kegiatan, dan kolom jabatan diisi nama jabatan, bukan nama orang | Istilah; Petunjuk butir 8 | owner (pemetaan peran ke jabatan) |
| U4 | Enam nilai Status (Berlaku, Perlu Diperbarui, Dicabut, Dalam Pemantauan, Belum Diverifikasi, Tidak Relevan untuk SINUX) | Istilah; Isi Register | Legal |
| U5 | Line Manager Legal menetapkan relevansi tiap peraturan | Ketentuan butir 5 | Legal |
| U6 | Line Manager Legal memeriksa kelengkapan dan keakuratan register sebelum dinyatakan selesai | Ketentuan butir 7 | Legal |
| U7 | Staff Legal memantau perubahan peraturan (tugas dari tim, penunjuk pelaku usulan) | Ketentuan butir 8 | Legal |
| U8 | Peninjauan register setiap bulan | Ketentuan butir 9 | Legal |
| U9 | Penanggung Jawab Kegiatan menjalankan tindak lanjut yang tercatat atas jabatannya | Ketentuan butir 12 | owner |
| U10 | Penyimpanan di folder Google Drive departemen Legal dengan klasifikasi RESTRICTED (Internal); termasuk butir 4.24 SNX-LEG-SOP-01 | Ketentuan butir 13; Dokumen Terkait; Rekaman | Legal (klasifikasi: owner menurut defaults.json) |
| U11 | Line Manager Legal sebagai pemilik dokumen dan pemilik rekaman register; Staff Legal pencatat | Peran; Rekaman; meta process_owner | Legal |
| U12 | Pembagian tugas mengikuti pola SNX-LEG-SOP-03 | Peran | Legal |
| U13 | Kolom Bidang memakai delapan area SNX-LEG-REG-02; peraturan di luar area diisi Kepatuhan Regulasi | Petunjuk butir 6 | Legal |
| U14 | Pemetaan tiap dokumen terkait ke register ini | Dokumen Terkait | Legal |
| U15 | Tujuh klausul ISO: ISO 9001:2015 4.2, 5.1.2, 7.5.3, 8.2.2; ISO/IEC 27001:2022 4.2, Annex A 5.31, Annex A 5.34. Judul klausul dalam bahasa Indonesia terjemahan penyusun | Acuan ISO | owner (konsultan mengonfirmasi) |
| U16 | Pemetaan peran Line Manager Legal dan Staff Legal ke jabatan Legal & Compliance (JA-08 dan JA-09) di SNX-HR-ORG-01, menunggu konfirmasi K-13 | Peran; Dokumen Terkait | owner (K-13 di SNX-HR-ORG-01); ditutup W9: pemetaan diputus owner (LEAD G-3 A5) |

## Open items

| # | Open item | Pemutus |
|---|---|---|
| 1 | Batas dengan dokumen lain: apakah syarat perizinan dan kewajiban kontrak masuk register ini, dan apakah register izin (REG-01), register dokumen legal (REG-04), dan register kontrak tetap terpisah (U1, U2) | Legal |
| 2 | Isi baris tidak dikerjakan karena tidak ada sumber. Legal perlu mengisi peraturan yang berlaku bagi SINUX dari teks peraturan, termasuk peraturan pelaksana pelindungan data pribadi dan sistem elektronik yang dicatat di notes/LEG-FRM-03.md open item 4 | Legal |
| 3 | Jabatan untuk peran Penanggung Jawab Kegiatan tiap kegiatan usaha (Commercial, Operation, HR, Finance, Accounting & Tax) | owner |
| 4 | Council 14 Okt menggabungkan register legal menjadi satu; worklist menomori REG-01 sampai REG-04 terpisah. Apakah digabung atau tetap | owner |
| 5 | Masa retensi register dan salinan peraturan belum ditetapkan; usulan ada di SNX-LEG-SOP-03 | Legal |
| 6 | Klausul ISO dan keterkaitan ke kontrol 5.31 dan 5.34 di SoA (status "Perlu keputusan" menurut audit) | owner (SoA oleh konsultan) |
| 7 | Frekuensi peninjauan bulanan (U8) dan status Dalam Pemantauan untuk rancangan peraturan | Legal |
| 8 | Pratinjau di Word: baris judul tabel 6.2 terbelah antara halaman 8 dan 9 pada pratinjau LibreOffice | HUMAN-VERDICT, orkestrator atau owner |

## 6. Dua pertanyaan penutup

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI? Temuan pada draf pertama, semuanya diperbaiki di spec:

| Temuan | Perbaikan |
|---|---|
| Definisi status "Berlaku" memakai kata berlaku, dan "Belum Diverifikasi" memakai Berlaku; definisi melingkar | "Peraturan masih mengikat dan relevan bagi SINUX, dan isi baris sesuai teks terbaru"; "Pemeriksaan apakah peraturan masih mengikat dan relevan belum selesai" |
| "Hasil pemeriksaan menunjukkan ..." (benda sebagai pelaku) | "Peraturan tidak mengikat kegiatan usaha maupun operasional SINUX menurut penetapan Line Manager Legal" |
| "Register mengidentifikasi dan mendokumentasikan ... dan memperbaruinya" di tabel Acuan ISO | "Register memuat ... yang teridentifikasi, dan isinya diperbarui lewat Peninjauan"; kata kerja manusia pada benda diganti "memuat" |
| Status ditulis pasif tanpa pelaku ("sudah diperiksa") | Diganti keadaan peraturan ("masih mengikat") |
| "Kewajiban Kontrak" didefinisikan dengan kata Kewajiban; "Peninjauan" didefinisikan lengkap dengan pelaku Staff Legal sehingga mengulang Ketentuan butir 9 | Diganti uraian polos; pelaku hanya di Ketentuan |
| Istilah "Departemen Legal" dan "departemen Legal" berganti | Satu bentuk "departemen Legal" |
| Pola "berstatus (USULAN)" berulang | Dipertahankan: label USULAN diwajibkan RUNBOOK. Tiap pemakaian menempel pada butir yang berbeda |
| Kesimpulan memakai kalimat yang sama dengan register Legal lain | Dipertahankan satu kalimat pola, ditambah rujukan Ketentuan butir 9 supaya khusus untuk register ini |

Sisa yang masih dapat terdengar seperti templat: butir Petunjuk Pengisian berpola "Kolom X memuat ...". Pola itu dipertahankan karena petunjuk pengisian memang berulang per kolom dan tiap butir mengatur kolom yang berbeda.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber? Pemeriksaan per jenis:

| Jenis | Hasil |
|---|---|
| Nama orang | Hanya "Samuel Kristanto Utomo" di blok Approval, dari data baris dan defaults.json. Badan dokumen memakai jabatan |
| Nama peraturan, nomor, tahun, instansi | Nol. Sel data dibiarkan kosong. Tidak ada contoh peraturan di teks |
| Angka | "setiap bulan" (U8, USULAN); "setiap tahun" dari review_period YEARLY di data baris; "enam nilai Status" (U4); "delapan area" (dari SNX-LEG-REG-02); "baris 1 sampai 10" adalah ukuran tata letak (A5). Tidak ada angka lain |
| Tanggal | Nol. effective_date kosong; tabel tanggal kosong |
| Sistem | Google Drive (dari SNX-LEG-SOP-01 butir 4.24). Zammad dan GLPI tidak dipakai karena register tidak memuat tiket |
| Nomor klausul ISO dan judulnya | Dari pengetahuan umum standar, bukan dari sumber repo; seluruhnya berlabel USULAN dan perlu konfirmasi konsultan (U15) |
| Peran dan pembagian tugas | Staff Legal dan Line Manager Legal dari HR-ORG-01. Pembagian tugas tiap butir berlabel USULAN atau mengikuti pola SOP-03 (U5 sampai U12) |

## Sweep

Putaran sweep sesudah DONE (instruksi /tmp/claude-0/prompts/LEG-REG-03.sweep.txt; temuan nonblocking butir 1 dan 2 di qa/LEG-REG-03.verify.json). Hanya dua butir diubah; temuan nonblocking lain (butir 7 Ketentuan, ejaan Pelindungan, rumus "berstatus (USULAN)", SNX-LEG-SOP-02, UU di open item 2) tidak disentuh karena di luar butir sweep.

| # | Lokasi | Sebelum | Sesudah |
|---|---|---|---|
| 1a | Peran, paragraf penjelas | "Nama jabatan Staff Legal dan Line Manager Legal mengikuti SNX-HR-ORG-01." | "Line Manager Legal dan Staff Legal adalah nama peran; SNX-HR-ORG-01 memetakannya ke jabatan Legal & Compliance, JA-08 dan JA-09 (USULAN)." |
| 1b | Dokumen Terkait, baris SNX-HR-ORG-01 | "Sumber nama jabatan Line Manager Legal dan Staff Legal, dan jabatan untuk kolom Penanggung Jawab Kegiatan." | "Matriks Peran memetakan peran Line Manager Legal dan Staff Legal ke jabatan Legal & Compliance, JA-08 dan JA-09 (USULAN). Daftar jabatannya menjadi acuan kolom Penanggung Jawab Kegiatan." |
| 2a | Rekaman, baris 1 (register) | "Pemilik: Staff Legal." | "Pemilik: Line Manager Legal. Pencatat: Staff Legal (SNX-LEG-SOP-03 butir 4.26)." |
| 2b | Rekaman, baris 2 (salinan) | "Pemilik: Staff Legal." | "Pemilik: Line Manager Legal. Pencatat: Staff Legal." |
| 2c | Peran, baris Line Manager Legal | "Pemilik dokumen (USULAN)." | "Pemilik dokumen dan pemilik rekaman register (USULAN)." |

Alasan butir 2: specs/LEG-SOP-03.json butir 4.26 menulis "Line Manager Legal menjadi pemilik rekaman di bagian 11 dan Staff Legal pencatatnya", dan tabel Rekaman SOP-03 memberi "pemilik Line Manager Legal" untuk dokumen internal departemen Legal. Dokumen ini kini sama. Pembedaan menetapkan (Line Manager Legal) dan mencatat (Staff Legal) tetap konsisten dengan Ketentuan butir 5, 6, 13 dan tabel Peran, jadi tidak ada butir Ketentuan yang diubah.

Uji sesudah sweep: render berhasil; `python3 -I tools/lint_doc.py ... generic` memberi "pass": true, "fails": [] (warns: 19 butir USULAN); validate.py docx "All validations PASSED!"; `python3 -I reports/orch/blankscan.py` memberi "ok 12 LEG-REG-03.docx []". Kode dokumen di badan tetap tercantum di Dokumen Terkait (tidak ada kode baru). Pemindaian em-dash dan en-dash pada notes ini: nol.


## ISO-W9

Putaran perbaikan ISO-W9 (LEAD G-3 A5, hasil pemeriksa makna R457). Hanya butir di bawah yang berubah.

| butir | sebelum | sesudah |
|---|---|---|
| meta.approval, blok Prepared dan Reviewed | Prepared "Staff Legal"; Reviewed "Line Manager Legal" | Prepared "Alif Altamziz / Staff Legal"; Reviewed "Ester Febe Utomo / Line Manager Legal" (config/defaults.json v22 prepared_reviewed.LEG) |
| A5, Peran, paragraf penjelas | "... JA-08 dan JA-09 (USULAN). Pembuat ..." | "... JA-08 dan JA-09. Pembuat ..."; USULAN pembagian tugas mengikuti pola SNX-LEG-SOP-03 tetap |
| A5, Dokumen Terkait, baris SNX-HR-ORG-01 | "... JA-08 dan JA-09 (USULAN). Daftar ..." | "... JA-08 dan JA-09. Daftar ..." |
| R2, hygiene notes, U16 | tanpa penanda W9 pada baris | ditambah "ditutup W9" pada baris itu |

Open item:

- U16 (pemetaan peran ke JA-08 dan JA-09, menunggu konfirmasi K-13): ditutup W9: pemetaan diputus owner (LEAD G-3 A5).
- R2: baris U16 kini memuat "ditutup W9" di barisnya sendiri; tidak ada baris dihapus.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil (label "(USULAN)" pada Status, Peran, Lingkup, Ketentuan 9, dan Acuan ISO dipertahankan; posisinya dipindah ke akhir butir).
### W10 kalimat dihapus atau dipindah
- Istilah, Bidang: "Nilainya ada di Petunjuk Pengisian butir 6." dihapus (kalimat penunjuk).
- Ketentuan 9: "menurut butir 3" dihapus; isi butir 3 (pemberitahuan perubahan kegiatan) ditulis langsung.
- Peran: "(Ketentuan butir 1, 4, 6, 8 sampai 11, 13)", "(Ketentuan butir 5 dan 7)", dan "(Ketentuan butir 2, 3, dan 12)" dihapus.
- Paragraf di bawah tabel Peran: "Line Manager Legal dan Staff Legal adalah nama peran; SNX-HR-ORG-01 memetakannya ke jabatan Legal & Compliance, JA-08 dan JA-09." dipindah ke tabel Peran sebagai "Jabatan: Legal & Compliance (JA-09)" dan "(JA-08)", seperti SNX-LEG-REG-01.
- Petunjuk 10: "menurut Ketentuan butir 9" dihapus. Petunjuk 12: "(Ketentuan butir 11)" dihapus.
- Rekaman: "(Ketentuan butir 13)" dihapus. Kesimpulan: "menurut Ketentuan butir 9" diganti faktanya "setiap bulan".
### W10 selisih angka
nihil (lihat subst_diff build; token nomor butir rujukan yang hilang sudah dicatat di bagian di atas).
### W10 catatan
- Pihak luar: "pelanggan" (dengan vendor), sama dengan dokumen Legal lain.
- Rujukan tabel memakai teks h2 beku: "Riwayat Perubahan dan Peninjauan", "Status dan Peninjauan"; "Review (tinjauan)" diperkenalkan di Istilah, "record (rekaman)" di Peran.
- Petunjuk Pengisian jadi kalimat perintah; calque "yang SINUX miliki", "yang harus SINUX lakukan", "yang ia ketahui" ditulis ulang.
### W10 putaran perbaikan 1 (pemeriksa buta r1)
- Kesimpulan: "setiap bulan" diberi (USULAN) dan pemicu perubahan kegiatan dikembalikan: "Staff Legal meninjau isinya setiap bulan (USULAN) dan setiap kali kegiatan SINUX berubah."
- Petunjuk 10: kriteria tanggal review dikembalikan: "menurut Ketentuan butir 9, yaitu setiap bulan (USULAN) dan saat kegiatan berubah."
- Rekaman, Lokasi: "Folder Google Drive Departemen Legal (USULAN)." (label dari Ketentuan butir 13 dibawa).
- Ketentuan 9: label dipindah tepat setelah "setiap bulan" agar tidak menutupi pemicu perubahan kegiatan.

### W10 audit pointer
- .sections[1].blocks[1].table.rows[1][1]: lengkap (kalimat penunjuk "nilainya ada di Petunjuk 6" dibuang, delapan nilai Bidang tetap di Petunjuk 6)
- .sections[2].blocks[8].p: lengkap (penunjuk ke butir 3 dibuang, pemicu pemberitahuan Penanggung Jawab Kegiatan, bulanan, USULAN utuh)
- .sections[3].blocks[0].table.rows[0][1]: lengkap (penunjuk balik ke daftar Ketentuan dibuang, semua tugas tetap tertulis)
- .sections[3].blocks[0].table.rows[1][1]: lengkap (penunjuk balik ke Ketentuan 5 dan 7 dibuang, tugas, pemilik, USULAN tetap)
- .sections[3].blocks[0].table.rows[2][1]: lengkap (penunjuk balik ke Ketentuan 2, 3, 12 dibuang, tiga tugas tetap tertulis)
- .sections[4].blocks[11].p: lengkap (penunjuk Ketentuan 11 dibuang, termasuk review tanpa perubahan dan kolom No. Baris utuh)
- .sections[7].blocks[1].table.rows[0][1]: lengkap (penunjuk Ketentuan 13 dibuang, lokasi, pemilik, pencatat, klasifikasi, USULAN tetap)
- .sections[8].blocks[0].p: lengkap (isi Ketentuan 9 disalin: bulanan USULAN dan saat kegiatan berubah)
