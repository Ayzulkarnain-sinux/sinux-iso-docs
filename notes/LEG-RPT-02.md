# Catatan penyusun LEG-RPT-02: Legal Compliance Evaluation Report

Status: DRAFTED. Spec: specs/LEG-RPT-02.json. Mode generic (doc_type_cover "REPORT", doc_type_label "Report"), aksi T2, wave W7, nomor SNX-LEG-RPT-02 (nomor lama dipertahankan), department Legal, classification "RESTRICTED (Internal)", audit_class null, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". process_owner "Line Manager Legal": dokumen tanpa sumber, jadi dipakai jabatan reviewer departemen tanpa nama (config/defaults.json process_owner.rule). Catatan worklist kosong.

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-RPT-02.json /tmp/pen-LEG-RPT-02/LEG-RPT-02.docx` exit 0.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-RPT-02/LEG-RPT-02.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "32 butir (USULAN) menunggu ACC".
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-RPT-02/LEG-RPT-02.docx`: "All validations PASSED!". `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-RPT-02/LEG-RPT-02.docx`: "ok 15 LEG-RPT-02.docx []" (putaran sweep).
- Pratinjau PDF lewat soffice, 15 halaman. Lebar kolom tabel disetel sampai judul kolom tidak patah (Daftar Evaluasi Persyaratan: Bidang 3.7, No. di Register 2.3, Persyaratan 3.0, Bukti yang Diperiksa 2.6, Status Kepatuhan 2.7, Catatan dan Rujukan Temuan 2.4 cm). Tabel Ringkasan per Bidang dipecah dua (jumlah; persentase) karena delapan kolom membuat judul patah.
- Pemeriksaan tambahan atas spec: nol em-dash dan en-dash, nol tanda kutip atau tebal untuk penekanan, "Samuel" tidak ada di badan dokumen, "Direktur Utama" dua kali (Istilah Manajemen, Kesimpulan), "COO" satu kali ("Direktur (COO)" pada Istilah Manajemen, sebutan pertama di badan), tiap kode SNX di badan ada di bagian Dokumen Terkait (12 kode, nol kurang, nol lebih), nol frasa terlarang daftar prompt (dicek dengan pemindaian teks spec), rujukan "Ketentuan butir" cocok dengan penomoran (Peran: Staff Legal butir 1 sampai 7, 9 sampai 15, dan 18; Penanggung Jawab Kegiatan butir 8; Line Manager Legal butir 16 dan 17; Manajemen butir 17; Rekaman butir 18; angka ini sesudah sweep, Ketentuan kini 18 butir).

## 1. Sumber

Dokumen ini T2 tanpa sumber: struktur kolom dan petunjuk pengisian saja, sel data faktual kosong, tanpa baris contoh. Alat Drive dimuat dan dipakai hanya baca (get_file_metadata dan read_file_content, empat panggilan) untuk memverifikasi kutipan; nol mutasi Drive. download_file_content tidak dipakai karena teks lengkap sudah terbaca lewat read_file_content.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist ISO SINUX 2026, baris 36 (dept LEG, "Legal Compliance Evaluation Report.", checked false) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (config/checklist.json, exported_at 2026-10-14T19:05:35Z; tidak diukur ulang) | config/checklist.json. Kolom iso_9001 dan iso_27001 baris ini null; link_text dan fileId null |
| Legal Compliance Monitoring & Corrective Action (Google Doc, 7098 byte) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA | 2026-10-14T04:03:12.671Z (get_file_metadata hari ini) | read_file_content satu kali |
| SOP Divisi Legal – SINUX.docx (16407 byte) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (get_file_metadata hari ini) | read_file_content satu kali; teks lengkap, tanpa struktur tabel yang dibutuhkan |
| SOP TEMPLATE internal SINUX (nama badan hukum, via context/CONTEXT-PACK-v19.md bagian 4) | 1n6iPAh7yXLadDkY-bwnuDz9D3fNhBodQ | tidak diukur | Dibaca dari salinan repo, bukan dari Drive |
| Pendukung repo (bukan Drive) | specs/LEG-REG-03.json (kolom Bidang, enam nilai status, Peninjauan Terakhir), specs/LEG-REG-02.json (delapan area), specs/LEG-RPT-01.json (lima nilai Status, Catatan Temuan, aspek M7 dan M8, pengecualian yang menunjuk SNX-LEG-RPT-02), specs/LEG-SOP-01.json (butir 4.24, prosedur 6.7, 6.10), specs/LEG-SOP-03.json (Kategori 4), specs/HR-ORG-01.json (JA-08, JA-09, K-13, unit Management), config/defaults.json v21 | repo kerja | Kutipan dari spec lain bisa basi bila spec itu berubah. LEG-REG-03 disusun worker lain dan sudah ada di specs/ saat dokumen ini disusun |

Pemetaan kriteria ke isi dokumen (nomor bagian menurut hasil render):

| Unsur kriteria baris 36 | Letak di dokumen |
|---|---|
| Laporan evaluasi | Bagian 6 Isi Laporan: Informasi Umum (6.1), Daftar Evaluasi Persyaratan (6.2), Ringkasan per Bidang (6.3), Ringkasan Temuan dan Pembanding (6.4), Hasil Evaluasi (6.5), Rekomendasi (6.6), Persetujuan dan Pengesahan (6.7) |
| Tingkat kepatuhan | Istilah (Tingkat Kepatuhan, Cakupan Verifikasi, nilai Status Kepatuhan); Ketentuan butir 12, 13, 14, 16; Ringkasan per Bidang (6.3); baris Tingkat Kepatuhan yang Ditetapkan (6.5) |
| Perusahaan | Ruang Lingkup 1.2 (seluruh SINUX, satu laporan per Periode Evaluasi); Nama Perusahaan di Informasi Umum; pengecualian entitas afiliasi atau turunan |
| Peraturan perundang-undangan | Istilah Persyaratan; Daftar Evaluasi Persyaratan (kolom No. di Register dan Persyaratan); Ketentuan butir 2 sampai 6 (sumber SNX-LEG-REG-03); Bidang Kepatuhan Regulasi, Kekayaan Intelektual, Ketenagakerjaan |
| Persyaratan hukum yang berlaku | Istilah Persyaratan hukum; Bidang Perizinan Berusaha, Kontrak Pelanggan, Kontrak Vendor, Pelindungan Data Pribadi, Kerahasiaan Informasi; "yang berlaku" = Ketentuan butir 2 (hanya Persyaratan berstatus Berlaku atau Perlu Diperbarui di SNX-LEG-REG-03) dan butir 4 sampai 6 (perubahan peraturan pada periode) |

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kriteria penerimaan baris 36: yang dievaluasi adalah tingkat kepatuhan perusahaan terhadap dua kelompok, peraturan perundang-undangan dan persyaratan hukum. Di dokumen menjadi Tujuan, Istilah Persyaratan dan Persyaratan hukum, dan Ketentuan butir 2 sampai 6 | "Laporan evaluasi tingkat kepatuhan perusahaan \nterhadap peraturan perundang-undangan dan \npersyaratan hukum yang berlaku." (kolom Description, tanda \n = pemenggalan baris di sel; baris 35 "Legal & Regulatory Requirements Register." memuat "Daftar peraturan perundang-undangan dan \npersyaratan hukum yang relevan dengan kegiatan \nusaha dan operasional perusahaan.") | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY |
| 2 | Perubahan regulasi diringkas Legal dalam memo kepatuhan tiap kuartal. Di dokumen menjadi Ketentuan butir 4 sampai 6 (membandingkan memo kepatuhan dengan SNX-LEG-REG-03, memperbarui register, lalu menulis perubahan di Informasi Umum dan mengevaluasinya; berlabel USULAN karena dipakai untuk menjaga daftar tetap terkini) | "Perubahan regulasi yang relevan dipantau dan diringkas dalam memo kepatuhan setiap kuartal." (bagian 4.5) dan "Triwulanan: memo kepatuhan dan pembaruan playbook/template." (bagian 6 Pelaporan) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 3 | Kesimpulan kepatuhan wajib berbukti, dan bukti yang belum ada tidak boleh menghasilkan status terpenuhi atau pernyataan patuh penuh. Di dokumen menjadi Ketentuan butir 9 dan 14 | "Setiap kesimpulan harus didukung oleh bukti yang dapat ditelusuri. Apabila bukti belum tersedia atau belum diperiksa, status pemenuhan tidak boleh dinyatakan telah terpenuhi." (Metode Pemantauan) dan "Hindari menyatakan seluruh perusahaan telah patuh apabila masih terdapat aspek yang belum diperiksa atau belum diverifikasi" (Kesimpulan) | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |

## 2. Fakta pendukung

| # | Fakta di dokumen | Kutipan verbatim atau asal | fileId atau berkas |
|---|---|---|---|
| 1 | Nama Perusahaan di Informasi Umum | "Company Name (PT Strategi Integrasi Nusantara (SINUX))" (ringkasan template di context/CONTEXT-PACK-v19.md bagian 4) | template 1n6iPAh7yXLadDkY-bwnuDz9D3fNhBodQ |
| 2 | Lima nilai Status Kepatuhan dan artinya | "Sesuai", "Tidak Sesuai", "Sebagian Sesuai", "Belum Diverifikasi", "Tidak Berlaku" dengan "Bukti belum cukup untuk menyimpulkan status kepatuhan." (Petunjuk Pengisian Status). Arti ditulis ulang agar cocok dengan Persyaratan | 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA |
| 3 | Laporan bulanan kepada Manajemen (dasar Ketentuan butir 17) | "Bulanan: laporan kepada manajemen (jumlah permintaan, kontrak selesai, risiko tinggi, izin yang akan jatuh tempo)." | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 4 | Sumber daftar Persyaratan dan nilai Bidang | specs/LEG-REG-03.json: "Kolom Bidang diisi salah satu area pada SNX-LEG-REG-02: Perizinan Berusaha, Kontrak Pelanggan, Kontrak Vendor, Pelindungan Data Pribadi, Kerahasiaan Informasi, Kepatuhan Regulasi, Kekayaan Intelektual, atau Ketenagakerjaan." dan enam nilai Status (Berlaku, Perlu Diperbarui, Dicabut, Dalam Pemantauan, Belum Diverifikasi, Tidak Relevan untuk SINUX) | specs/LEG-REG-03.json |
| 5 | Pengecualian aspek M7 dan M8, Catatan Temuan, Periode Pemantauan, Nomor Temuan | specs/LEG-RPT-01.json: aspek M7 "Kebijakan dan Prosedur Internal", M8 "Tindak Lanjut Temuan Sebelumnya"; pengecualian "Evaluasi tingkat kepatuhan SINUX secara keseluruhan | Diatur di SNX-LEG-RPT-02." | specs/LEG-RPT-01.json |

## 3. Keputusan data dan pemetaan peran

- Approval, status, revision, effective_date, review_period, revision_desc: persis dari prompt dan config/defaults.json v21.
- Samuel di badan dokumen: hanya "Direktur Utama". Blok Approval memakai "President Director" (renderer dan defaults).
- COO: "Direktur (COO)" pada sebutan pertama (Istilah, Manajemen), tidak dipakai lagi sesudahnya.
- Tiket dan vault: tidak relevan; Zammad, GLPI, dan vault tidak disebut. PPN: tidak relevan.
- Klasifikasi: RESTRICTED (Internal) dari prompt; laporan terisi juga RESTRICTED (Internal) karena memuat evaluasi hukum (defaults: hukum = RESTRICTED (Internal)).
- Nama peran mengikuti specs/HR-ORG-01.json (Daftar Jabatan dan Matriks Peran):

| Peran di dokumen | Padanan | Dasar |
|---|---|---|
| Staff Legal | Nama peran, dipetakan ke jabatan Legal & Compliance (JA-09), "(USULAN), menunggu konfirmasi (K-13)" | Matriks Peran HR-ORG-01; prompt menetapkan prepared "Staff Legal" |
| Line Manager Legal | Nama peran, dipetakan ke jabatan Legal & Compliance (JA-08), "(USULAN), menunggu konfirmasi (K-13)" | Matriks Peran HR-ORG-01; prompt menetapkan reviewed "Line Manager Legal" |
| Manajemen | Unit Management: Direktur Utama (JA-01) dan Direktur (JA-02) | Daftar Jabatan HR-ORG-01; istilah sama dengan di SNX-LEG-REG-02 |
| Penanggung Jawab Kegiatan | Jabatan menurut HR-ORG-01, ditulis per Persyaratan di SNX-LEG-REG-03; tidak dipetakan ke satu jabatan | Istilah yang sama dengan SNX-LEG-REG-03 |
| Penyetuju Laporan | Belum ditetapkan | HR-ORG-01 tidak memuat penyetuju laporan Legal; pola sama dengan SNX-LEG-RPT-01 |
| Pelaksana Evaluasi | Staff Legal (USULAN) | Peran terdekat; padanan Pelaksana Pemantauan di SNX-LEG-RPT-01 |

Pilihan Bidang (delapan area SNX-LEG-REG-02 dan kolom Bidang SNX-LEG-REG-03), bukan aspek M1 sampai M8 SNX-LEG-RPT-01: laporan ini mengevaluasi Persyaratan yang tercatat di SNX-LEG-REG-03, sehingga pengelompokannya mengikuti register itu dan Persyaratan bisa dipindahkan baris demi baris tanpa pemetaan. Aspek M7 (kebijakan internal) dan M8 (tindak lanjut temuan) dikecualikan atau dirujuk lewat Rujukan Temuan.

## 4. Penanganan cacat context/audit

Hasil `grep -n "Legal Compliance Evaluation Re" context/audit/*.md`: satu baris, `context/audit/iso-sinux-supdocs-sintesis-2026-10-14.md:730:2. Legal Compliance Evaluation Report.`, yaitu butir 2 daftar 13 dokumen Legal usulan konsultan. Tidak ada bagian dokumen atau bagian 5 "Catatan kualitas dan celah" untuk dokumen ini (T2, belum ada berkas sumber). Maka tidak ada cacat sumber yang tercatat untuk dokumen ini. Cacat pada dokumen Legal lain di context/audit yang berpengaruh pada isi laporan ini, dan penanganannya:

| # | Cacat di context/audit (dokumen lain) | Penanganan di dokumen ini |
|---|---|---|
| 1 | Legal Risk Register menulis area "Kekayaan Intelektuan" (salah ketik) | Ditulis "Kekayaan Intelektual", sama dengan SNX-LEG-REG-02 dan SNX-LEG-REG-03 |
| 2 | Atasan Line Manager Legal berbeda di tiga sumber ("[ISI: atasan, mis. Direksi/COO]", "CEO", "Management / Direktur") | Dokumen tidak menyebut atasan Line Manager Legal. "Manajemen" didefinisikan lewat unit Management di SNX-HR-ORG-01 (USULAN) |
| 3 | SOP Divisi Legal: prinsip "Legal memberi opini" bertabrakan dengan penanganan "Hentikan proses" | Tidak ada langkah "menghentikan"; Rekomendasi diserahkan ke Manajemen yang memutuskan tindak lanjut (Ketentuan butir 17, USULAN) |
| 4 | Klasifikasi di SOP Divisi Legal memakai label Rahasia, Internal, Publik, sedangkan skema SNX-ISMS-PRO-01 memakai label Inggris | Memakai tingkat PRO-01: RESTRICTED (Internal) |
| 5 | Dokumen Legal sumber tidak memuat rujukan klausul ISO | Bagian Acuan ISO ditambahkan dengan satu label "(USULAN, perlu konfirmasi konsultan)" |
| 6 | Rujukan regulasi di dokumen Legal ditulis apa adanya (UU No. 27 Tahun 2022, UU ITE tanpa UU No. 1 Tahun 2024) | Tidak ada nomor peraturan di dokumen ini; peraturan dicatat per baris di SNX-LEG-REG-03 sehingga tidak ada rujukan basi di sini |
| 7 | Placeholder "[ISI]" pada SOP Divisi Legal (repositori resmi, periode retensi, DoA) | Repositori dan retensi ditulis berlabel USULAN dan merujuk SNX-LEG-SOP-01 butir 4.24 dan SNX-LEG-SOP-03; DoA tidak dirujuk |

Kalimat bernada instruksi di sumber: tiga petunjuk isi formulir pada dokumen Legal Compliance Monitoring ("Petunjuk Pengisian Status", "[Uraikan kondisi kepatuhan ... Hindari menyatakan ...]", "Bagian ini diisi untuk setiap ketidaksesuaian ..."). Semuanya petunjuk untuk pengguna formulir, bukan perintah kepada agen. Diperlakukan sebagai data dan hanya dipakai sebagai dasar Ketentuan butir 9 dan 14. Tidak ada kalimat yang menyuruh agen melakukan sesuatu.

## USULAN

Spec memuat 38 kemunculan kata USULAN: 32 label "(USULAN)" polos (hitungan lint) dan enam bentuk lain: "(USULAN: satu laporan per tahun)", "(SNX-LEG-SOP-01 prosedur 6.7, USULAN)", "(USULAN, selaras dengan laporan bulanan ...)", "(USULAN, SNX-LEG-SOP-01 butir 4.24)" di Ketentuan, "(butir 4.24, USULAN)" di Dokumen Terkait, dan satu label "(USULAN, perlu konfirmasi konsultan)" di Acuan ISO. Jumlah keputusan yang berbeda ada 21.

| # | Butir USULAN | Pemutus yang disarankan |
|---|---|---|
| 1 | Frekuensi laporan satu per tahun (Ketentuan butir 1). Satu-satunya angka tanpa sumber | Legal |
| 2 | Persyaratan yang dievaluasi = baris SNX-LEG-REG-03 berstatus Berlaku atau Perlu Diperbarui pada akhir Periode Evaluasi (Ketentuan butir 2) | Legal |
| 3 | Persyaratan berstatus Belum Diverifikasi di SNX-LEG-REG-03 dicatat di Batasan Evaluasi dan tidak dihitung (Ketentuan butir 3) | Legal |
| 4 | Memo kepatuhan dibandingkan dengan SNX-LEG-REG-03 (butir 4); perubahan peraturan yang belum tercatat diperbarui lebih dulu di register (butir 5), lalu ditulis di Informasi Umum dan dievaluasi sebagai Persyaratan (butir 6). Memo triwulanan dari sumber, dipakai di sini untuk menjaga daftar terkini | Legal |
| 5 | Penanggung Jawab Kegiatan menyerahkan Bukti kepada Staff Legal (Ketentuan butir 8, Peran). Kewajiban untuk unit lain | owner |
| 6 | Hasil pemantauan SNX-LEG-RPT-01 dipakai sebagai Bukti (Ketentuan butir 10) | Legal |
| 7 | Catatan Temuan dibuat lebih dulu di SNX-LEG-RPT-01 bila Persyaratan Sebagian Sesuai atau Tidak Sesuai belum punya Catatan Temuan; Tindakan Perbaikan tidak diulang di laporan ini (Ketentuan butir 11) | Legal |
| 8 | Rumus Cakupan Verifikasi dan Tingkat Kepatuhan (persentase), pengeluaran Tidak Berlaku dari pembagi, dan baris Seluruh Bidang dihitung dari semua baris, bukan rata-rata (Istilah, Ketentuan butir 12, Petunjuk butir 6). Tidak ada ambang angka | Legal |
| 9 | Larangan menyatakan SINUX patuh penuh diperluas ke status Sebagian Sesuai dan Tidak Sesuai (Ketentuan butir 14). Sumber hanya menyebut aspek yang belum diperiksa atau belum diverifikasi | Legal |
| 10 | Staff Legal sebagai Pelaksana Evaluasi; Line Manager Legal sebagai pemilik dokumen, pemeriksa laporan terisi, dan penetap Tingkat Kepatuhan (Ketentuan butir 16, Peran) | Legal |
| 11 | Line Manager Legal menyampaikan laporan terisi ke Manajemen, dan Manajemen memutuskan tindak lanjut atas Rekomendasi (Ketentuan butir 17). Laporan bulanan dari sumber, diperluas ke laporan ini | Samuel |
| 12 | Manajemen = Direktur Utama dan Direktur (COO), yaitu unit Management di SNX-HR-ORG-01 (Istilah) | owner |
| 13 | Baris persetujuan per laporan: Staff Legal menyusun, Line Manager Legal memeriksa, Penyetuju Laporan menyetujui dengan jabatan belum ditetapkan (Peran, Petunjuk butir 11) | Samuel |
| 14 | Penyimpanan di folder Google Drive departemen Legal, pencatat Staff Legal, pemilik Line Manager Legal, penandaan RESTRICTED (Internal) (Ketentuan butir 18, Rekaman). Lokasi berlabel USULAN di SNX-LEG-SOP-01 butir 4.24 dan SNX-LEG-SOP-03 butir 4.8; pemilik dan pencatat mengikuti SNX-LEG-SOP-03 butir 4.26 | Legal |
| 15 | Retensi: Kategori 4 (dokumen penelaahan Legal) di SNX-LEG-SOP-03, pemilihan menunggu keputusan Legal | Legal |
| 16 | Lima nilai Status Kepatuhan sama dengan nilai Status di SNX-LEG-RPT-01 | Legal |
| 17 | Definisi Persyaratan hukum (syarat perizinan dan kontrak) dan Penanggung Jawab Kegiatan (jabatan menurut SNX-HR-ORG-01, tercatat di SNX-LEG-REG-03) | Legal |
| 18 | Tujuh butir pengecualian lingkup: kebijakan internal, pemantauan periodik dan temuan, penilaian risiko hukum, penelaahan kontrak, tinjauan rinci data pribadi, pemutakhiran daftar Persyaratan, kepatuhan pihak lain | Legal |
| 19 | Entitas afiliasi atau turunan SINUX tidak dievaluasi di laporan ini sampai ada keputusan (butir pengecualian kedelapan) | owner |
| 20 | Kolom Bukti dari Dokumen Legal: pemetaan Bidang ke SNX-LEG-REG-01, FRM-01, FRM-02, FRM-03, dan dokumen Penanggung Jawab Kegiatan | Legal |
| 21 | Tujuh klausul ISO 9001:2015 (8.2.2, 9.1.3, 10.2) dan ISO/IEC 27001:2022 (9.1, 10.2, Annex A 5.31, 5.34), label "(USULAN, perlu konfirmasi konsultan)". Checklist baris 36 tidak memberi acuan klausul. Pemetaan Line Manager Legal ke JA-08 dan Staff Legal ke JA-09 (K-13 di SNX-HR-ORG-01) ikut berlabel USULAN di bagian Peran | owner, diteruskan ke konsultan; diubah W9: pemetaan Legal tidak lagi berlabel USULAN; label USULAN klausul ISO tetap |

## 5. Asumsi (bukan USULAN berlabel, tetapi bukan dari teks sumber)

1. Nama Perusahaan diisi "PT Strategi Integrasi Nusantara (SINUX)" dari template (fakta pendukung 1).
2. "Tanggal Evaluasi" ditafsirkan sebagai tanggal pemeriksaan Bukti yang terakhir, dan "Periode Evaluasi" sebagai rentang waktu yang dievaluasi (Petunjuk butir 1). Tidak ada sumber untuk kedua kolom.
3. "Daftar Persyaratan yang Dipakai" diisi tanggal peninjauan terakhir SNX-LEG-REG-03. Register itu menyimpan Peninjauan Terakhir per baris, sehingga tanggal yang ditulis perlu dijelaskan Staff Legal (lihat open item 9).
4. "Persentase" dan "Cakupan Verifikasi" memakai nama Indonesia yang dibuat untuk laporan ini; istilahnya tidak ada di sumber mana pun (termasuk dalam USULAN 8).
5. Petunjuk mekanis seperti "Staff Legal menambah baris dengan nama Bidang yang sama" tidak berlabel karena tidak menambah fakta atau angka.
6. Kata "Bidang" menggantikan kata "aspek" dari SNX-LEG-RPT-01 agar sama dengan SNX-LEG-REG-02 dan SNX-LEG-REG-03; "aspek" hanya dipakai saat menunjuk M7 dan M8 di SNX-LEG-RPT-01.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju Laporan per periode belum ditetapkan; sumber hanya punya baris "Disetujui oleh" tanpa jabatan | Samuel |
| 2 | Batas SNX-LEG-RPT-01 dan SNX-LEG-RPT-02: RPT-01 sudah memuat "Ringkasan Hasil Pemantauan" (jumlah aspek Sesuai) yang dekat dengan tingkat kepatuhan. Pembeda di dokumen ini: RPT-02 menghitung persentase atas seluruh Persyaratan di SNX-LEG-REG-03 untuk satu Periode Evaluasi, RPT-01 memuat temuan per Periode Pemantauan. Belum diputus | Legal |
| 3 | RPT-01 memakai aspek M1 sampai M8, RPT-02 dan REG-03 memakai delapan Bidang. Tidak ada pemetaan tertulis M ke Bidang, dan aspek M6 (Keamanan Informasi) tidak punya Bidang sendiri. Sebaiknya diputus sebelum dokumen disahkan | Legal |
| 4 | Nama "Belum Diverifikasi" dipakai dua kali dengan arti berbeda: di SNX-LEG-REG-03 untuk relevansi peraturan, di dokumen ini untuk Bukti. Nilai dipertahankan karena berasal dari nilai Status SNX-LEG-RPT-01; Ketentuan butir 3 memakai kata "statusnya di SNX-LEG-REG-03" untuk membedakan | Legal |
| 5 | Ambang kategori Tingkat Kepatuhan (misalnya batas persen untuk tingkat baik, cukup, kurang) tidak ada di sumber mana pun; dokumen hanya memuat persentase dan kesimpulan tertulis. Bila Manajemen ingin target, perlu ditetapkan | Samuel |
| 6 | Frekuensi evaluasi (usulan satu per tahun) dan hubungannya dengan tinjauan manajemen dan audit internal, yang termasuk lane konsultan | Legal, diteruskan ke konsultan |
| 7 | Entitas afiliasi atau turunan: SOP Divisi Legal menyatakan "Mencakup juga entitas afiliasi atau turunan (misalnya rencana pendirian PT Nusagrid) sepanjang ditugaskan kepada Divisi Legal SINUX". Dokumen ini mengecualikannya sampai ada keputusan | owner |
| 8 | Kewajiban Penanggung Jawab Kegiatan menyerahkan Bukti ke Staff Legal belum disepakati unit mana pun dan tidak ada di sumber | owner |
| 9 | Kecocokan dengan SNX-LEG-REG-03 saat register itu berstatus final: nilai Bidang, enam nilai Status, kolom Peninjauan Terakhir (per baris, bukan satu tanggal), dan Penanggung Jawab Kegiatan. Perubahan di sana mengubah Ketentuan butir 2 sampai 6 dan Petunjuk butir 2 sampai 4 | Legal |
| 10 | Pemetaan Line Manager Legal ke JA-08 dan Staff Legal ke JA-09 menunggu konfirmasi (K-13 di SNX-HR-ORG-01). Bila peta berubah, bagian Peran ikut berubah | owner; ditutup W9: owner 15 Okt memutus pemetaan Legal, tidak lagi menunggu konfirmasi |
| 11 | Retensi laporan terisi dan Bukti belum ditetapkan. Dokumen ini menyebut Kategori 4 di SNX-LEG-SOP-03, sedangkan SNX-LEG-RPT-01 menyebut Kategori 4 atau Kategori 6; pilihan perlu diseragamkan | Legal |
| 12 | Judul klausul ISO 8.2.2, 9.1.3, 10.2 (9001) dan 9.1, 10.2 (27001) berasal dari pengetahuan umum penyusun, tanpa berkas di repo; judul Annex A 5.31 dan 5.34 mengikuti spec Legal lain. SNX-LEG-REG-03 menulis 8.2.2 "produk dan layanan", dokumen ini dan SNX-LEG-SOP-01 memakai "produk dan jasa". Perlu satu ejaan dari konsultan | owner, diteruskan ke konsultan |
| 13 | Sumber tidak memuat butir "Pemilik dokumen" (T2 tanpa sumber); process_owner diambil dari jabatan reviewer departemen | Legal |
| 14 | Checklist baris 36 tidak memberi acuan klausul (kolom iso_9001 dan iso_27001 null); seluruh klausul di bagian Acuan ISO adalah USULAN | owner, diteruskan ke konsultan |
| 15 | Checklist baris 36 bertanda checked false (tim belum menandai ada) dan tidak tertaut berkas. Dokumen ini ditulis baru sepenuhnya | owner (informasi, tanpa keputusan) |
| 16 | Tiga petunjuk isi formulir di sumber dicatat sebagai data, bukan instruksi (bagian 4). Tidak ada kalimat yang menyuruh agen melakukan sesuatu | owner (informasi, tanpa keputusan) |

## 6. Jawaban dua pertanyaan sebelum selesai

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama, semuanya sudah diperbaiki di spec akhir:
- Benda sebagai pelaku kata kerja manusia: "Rujukan Temuan menghubungkan Persyaratan ... dengan Catatan Temuan", "Status Berlaku dan Perlu Diperbarui di register itu menentukan Persyaratan", "Catatan Temuan yang mencatat kekurangan", "Status Kepatuhan ... yang menunjukkan keadaan pemenuhan". Diganti rumusan isi ("Kolom Catatan dan Rujukan Temuan memuat tautan ..."), kalimat berpelaku, atau kata "memuat". Pemindaian ulang kata kerja menelaah, memeriksa, meminta, memastikan, menyetujui, menunjukkan, menyatakan, menghasilkan, membatasi, menunjuk, merujuk, menguraikan, memantau, mencatat, memakai, menentukan, menetapkan, menghitung, menghubungkan, menyimpan, mengisi, menulis, menyerahkan, menyampaikan, memutuskan, menerima, membandingkan, memperbarui pada seluruh teks spec: sisa kemunculan semuanya berpelaku peran (Staff Legal, Line Manager Legal, Penanggung Jawab Kegiatan, Manajemen, Penyetuju Laporan) atau berada di definisi tanpa subjek benda.
- Pengulangan antarbagian: kalimat "Staff Legal menghitung ... dan Line Manager Legal menetapkannya" di Tujuan dan di Ketentuan; "sama dengan kolom Bidang di SNX-LEG-REG-03" di Ruang Lingkup dan Istilah; instruksi "diisi satu dari lima nilai" di Istilah dan Petunjuk; keterangan "dikecualikan dari laporan ini" di tabel Dokumen Terkait dan tabel pengecualian; syarat "Berlaku atau Perlu Diperbarui" di Ketentuan dan Dokumen Terkait. Masing-masing disisakan di satu tempat.
- Judul kolom yang patah di pratinjau ("Registe r", "Persyarata n", "Kepatuha n"): lebar kolom disetel ulang, dan kolom "Rujukan Temuan/Catatan" diganti "Catatan dan Rujukan Temuan" agar bisa membungkus baris.

Sisa yang disengaja:
- Pembuka kalimat "Staff Legal menulis ...", "Staff Legal mengisi ..." berulang di Ketentuan dan Petunjuk. Dibiarkan karena aturan satu langkah, satu pelaku lebih penting daripada variasi.
- Label "(USULAN)" muncul 32 kali. Dibiarkan karena aturan label per butir berlaku.
- Pola "Hasil yang dijaga: ..." di Tujuan mengikuti dokumen Legal lain agar set dokumen seragam.
- Tidak ada kelompok tiga yang dipaksakan: daftar tiga atau lebih di teks (misalnya jumlah, Cakupan Verifikasi, Tingkat Kepatuhan; atau nama, tanggal, tanda tangan) adalah isi kolom atau keluaran nyata. Tidak ada penutup positif, em-dash, penekanan tebal atau huruf kapital, atau atribusi kabur (pemindaian frasa terlarang prompt: nol temuan). Kata "Persyaratan", "Bukti", dan "Bidang" berhuruf kapital karena istilah yang didefinisikan, bukan penekanan.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir di dokumen | Sumber atau status |
|---|---|
| "satu laporan per tahun" | Tanpa sumber, berlabel USULAN 1; satu-satunya angka di dokumen |
| Rumus persentase Cakupan Verifikasi dan Tingkat Kepatuhan | Metode, bukan fakta; USULAN 8. Tidak ada ambang angka |
| "delapan Bidang" dan namanya | specs/LEG-REG-03.json dan specs/LEG-REG-02.json (fakta pendukung 4); hitungan dari tabel dokumen sendiri |
| "lima nilai" Status Kepatuhan | Dokumen Drive 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA (fakta pendukung 2); artinya ditulis ulang dan berlabel USULAN 16 |
| Memo kepatuhan triwulanan, laporan bulanan kepada Manajemen | SOP Divisi Legal 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb (fakta kunci 2, fakta pendukung 3); penggunaan di laporan ini USULAN 4 dan 11 |
| Rujukan butir 4.24, prosedur 6.7 dan 6.10 (SNX-LEG-SOP-01), Kategori 4 (SNX-LEG-SOP-03), JA-08, JA-09, K-13 (SNX-HR-ORG-01), aspek M7 dan M8 (SNX-LEG-RPT-01) | Dicek terhadap specs/ di repo; bisa basi bila spec itu berubah |
| Nama Perusahaan | Template, fakta pendukung 1, asumsi 1 |
| Klausul ISO | USULAN 21; judul dari pengetahuan umum untuk lima butir (open item 12) |
| Tanggal, nomor peraturan, nomor izin, nilai, nama orang selain Samuel Kristanto Utomo di blok Approval | Nol; sel tanggal dan data faktual dibiarkan kosong, tidak ada baris contoh |

## Sweep

Putaran penghalusan sesudah DONE (instruksi /tmp/claude-0/prompts/LEG-RPT-02.sweep.txt), lalu perbaikan atas temuan qa/LEG-RPT-02.sweep.r1.json. Dua butir sweep diubah; fakta, angka, nama, dan struktur lain tetap. Penomoran Ketentuan bergeser karena butir 4 dipecah; semua rujukan "Ketentuan butir" di spec dan di notes ini sudah disesuaikan.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Ketentuan butir 4 memuat tiga tindakan dengan urutan tidak jelas | Satu butir: "4. Staff Legal membandingkan memo kepatuhan pada Periode Evaluasi dengan SNX-LEG-REG-03 (SNX-LEG-SOP-01 prosedur 6.7, USULAN). Staff Legal menulis perubahan peraturan yang belum tercatat di register itu pada tabel Informasi Umum, memperbaruinya di register lebih dulu, lalu mengevaluasinya (USULAN)." Ketentuan 16 butir | Tiga butir berurutan, pelaku Staff Legal di tiap butir: "4. Staff Legal membandingkan memo kepatuhan pada Periode Evaluasi dengan SNX-LEG-REG-03 (SNX-LEG-SOP-01 prosedur 6.7, USULAN)." / "5. Untuk tiap perubahan peraturan yang belum tercatat di SNX-LEG-REG-03, Staff Legal memperbarui register itu lebih dulu (USULAN)." / "6. Setelah memperbarui register, Staff Legal menulis perubahan itu di tabel Informasi Umum, lalu mengevaluasinya sebagai Persyaratan (USULAN)." Tindakan evaluasi dari teks lama tetap ada (butir 6, perbaikan r1 butir 2). Ketentuan kini 18 butir; butir lama 5 sampai 16 menjadi 7 sampai 18; rujukan di Peran, Petunjuk butir 2, 5, 9, dan Rekaman ikut digeser |
| 2 | Konsistensi Legal: Line Manager Legal dan Staff Legal sebagai nama peran yang dipetakan ke jabatan, bukan nama jabatan | Peran Staff Legal: "Dipetakan ke Legal & Compliance (JA-09) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." Peran Line Manager Legal: "Dipetakan ke Legal & Compliance (JA-08) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." Dokumen Terkait SNX-HR-ORG-01: "Struktur Organisasi SINUX. Sumber nama jabatan Line Manager Legal, Staff Legal, unit Management, dan jabatan untuk kolom Penanggung Jawab Kegiatan." (kolom itu sudah tidak ada) | Peran Staff Legal: "Nama peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." Peran Line Manager Legal: "Nama peran ini dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." Dokumen Terkait SNX-HR-ORG-01: "Struktur Organisasi SINUX. Sumber jabatan Legal & Compliance (JA-08 dan JA-09), yang dipetakan ke nama peran Line Manager Legal dan Staff Legal (USULAN), serta unit Management dan jabatan Penanggung Jawab Kegiatan." |
| 2a | Pemilik rekaman Legal mengikuti SNX-LEG-SOP-03 | Rekaman laporan terisi, lokasi dan pemilik: "Folder Google Drive departemen Legal (Ketentuan butir 16). Pencatat Staff Legal, pemilik Line Manager Legal (USULAN). Klasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01." Dokumen Terkait SNX-LEG-SOP-03: "Legal Document Control & Retention. Tempat usulan periode retensi dan Kategori 4 (dokumen penelaahan Legal)." | Lokasi dan pemilik: "Folder Google Drive departemen Legal (Ketentuan butir 18; SNX-LEG-SOP-03 butir 4.8). Pencatat Staff Legal, pemilik Line Manager Legal (SNX-LEG-SOP-03 butir 4.26, USULAN). Klasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01." Dokumen Terkait SNX-LEG-SOP-03: "Legal Document Control & Retention. Tempat usulan periode retensi dan Kategori 4 (dokumen penelaahan Legal), repositori resmi (butir 4.8), dan pembagian pemilik rekaman dan pencatat (butir 4.26)." Kolom Retensi baris laporan terisi tidak diubah: tetap "Belum ditetapkan. Kategori 4 (dokumen penelaahan Legal) di SNX-LEG-SOP-03; pemilihan kategori menunggu keputusan Legal (USULAN)." (versi sweep pertama yang menetapkan Kategori 4 dibatalkan, perbaikan r1 butir 1); open item 11 dan USULAN 15 sama dengan sebelum sweep |

Satu perbedaan dengan SNX-LEG-SOP-03 yang dipertahankan, berlabel USULAN di baris itu: baris rekaman Bukti pemenuhan Persyaratan. SNX-LEG-SOP-03 menetapkan Line Manager Legal sebagai pemilik rekaman di bagian 11 SOP itu (butir 4.26), dan butir 4.26 tidak mencakup Bukti asli milik unit lain. Maka Bukti asli tetap dimiliki Penanggung Jawab Kegiatan, sedangkan salinan Bukti di folder Google Drive departemen Legal dimiliki Line Manager Legal menurut pola SNX-LEG-SOP-03 (perluasan butir 4.26, USULAN). Pencatat lokasi tetap Staff Legal. Pemutus: Legal.

Hasil uji sesudah perbaikan r1: render exit 0; lint_doc generic "pass": true, fails kosong, satu warn "32 butir (USULAN) menunggu ACC"; validate.py "All validations PASSED!"; blankscan.py "ok 15 LEG-RPT-02.docx []".


## ISO-W9

| butir | sebelum | sesudah |
|---|---|---|
| Blok Approval, Prepared By | Staff Legal | Alif Altamziz / Staff Legal |
| Blok Approval, Reviewed By | Line Manager Legal | Ester Febe Utomo / Line Manager Legal |
| Tabel Peran, Staff Legal | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| Tabel Peran, Line Manager Legal | ... di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN). | ... di SNX-HR-ORG-01. |
| Dokumen Terkait, baris SNX-HR-ORG-01 | ... Line Manager Legal dan Staff Legal (USULAN), serta unit ... | ... Line Manager Legal dan Staff Legal, serta unit ... |
| R2: USULAN 21, notes | baris tanpa penanda W9 | ditambah "diubah W9" di baris itu (alasan satu baris) |
| R2: Open item 10, notes | baris tanpa penanda W9 | ditambah "ditutup W9" di baris itu (alasan satu baris) |

Open item:
- Pemetaan Legal (USULAN K-13 di tabel USULAN dan catatan lama): ditutup W9: owner 15 Okt memutus Line Manager Legal = JA-08 Ester Febe Utomo, Staff Legal = JA-09 Alif Altamziz (LEAD G-3 A5); label USULAN dan menunggu konfirmasi pada pemetaan itu dihapus. USULAN lain tetap. Open item 10: ditutup W9: pemetaan sudah diputus owner.
- A3: tidak ada garis lapor JA-03/JA-04 (Direktur Utama dan Direktur (COO) disebut hanya sebagai unit Management).

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Ketentuan 17, kalimat pertama: "(USULAN, selaras dengan laporan bulanan di SNX-LEG-SOP-01 prosedur 6.10)" menjadi "selaras dengan laporan bulanan di SNX-LEG-SOP-01 prosedur 6.10" dan butir ditutup satu label "(USULAN)" di akhir (STYLE §3.5 satu label per butir). Status kedua kalimat tetap usulan; label tidak dibuang dari butir.
### W10 kalimat dihapus atau dipindah
- Ruang Lingkup, baris kebijakan internal: "Pemantauannya ada di aspek M7 SNX-LEG-RPT-01." digabung jadi "dan dipantau pada aspek M7 SNX-LEG-RPT-01".
- Peran: "(Ketentuan butir 1 sampai 7, 9 sampai 15, dan 18)", "(Ketentuan butir 16 dan 17)", "(Ketentuan butir 8)", "(Ketentuan butir 17)" dihapus.
- Peran: "Nama peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01." dan versi JA-08 dipadatkan menjadi "Jabatan: Legal & Compliance (JA-0x)."; sumber pemetaan tetap di Dokumen Terkait SNX-HR-ORG-01.
- Petunjuk 2: "menurut Ketentuan butir 6" diganti faktanya (perubahan peraturan yang baru dicatat ke SNX-LEG-REG-03). Petunjuk 5: "menurut Ketentuan butir 11" dihapus. Petunjuk 9: "menurut Ketentuan butir 3" dan "menurut Ketentuan butir 13" diganti faktanya.
- Dokumen Terkait SNX-LEG-REG-03: "(Ketentuan butir 2)" dihapus. Rekaman: "(Ketentuan butir 18; ...)" dan "(Ketentuan butir 18)" dihapus; rujukan "SNX-LEG-SOP-03 butir 4.26" di baris laporan terisi dihapus karena sudah ada di Dokumen Terkait SNX-LEG-SOP-03 (satu rujukan per sel).
### W10 selisih angka
nihil (subst_diff build kosong).
### W10 catatan
- Pihak luar: "pelanggan" (dan vendor/pemasok), sama dengan dokumen Legal lain.
- "Review (tinjauan)" diperkenalkan di tabel butir yang dikecualikan, "record (rekaman)" di Dokumen Terkait SNX-LEG-SOP-03.
- Petunjuk Pengisian jadi kalimat perintah (0 dari 11 diawali peran). Kolom Daftar Evaluasi Persyaratan dilebarkan untuk Persyaratan dan Catatan; halaman tetap 15, ISI mulai halaman 10.
### W10 putaran perbaikan 1 (pemeriksa buta r1)
- Ketentuan 17: label pada kalimat penyampaian dikembalikan: "... SNX-LEG-SOP-01 prosedur 6.10 (USULAN). Manajemen memutuskan tindak lanjut atas Rekomendasi (USULAN)." Catatan "W10 label dihapus" di atas tidak berlaku lagi (nihil).
- Petunjuk 2: "tulis perubahan peraturan pada periode itu yang baru dicatat ke SNX-LEG-REG-03 (USULAN)." (batas periode dan label dikembalikan).
- Petunjuk 9: "Persyaratan yang masih Belum Diverifikasi di SNX-LEG-REG-03 dan tidak dihitung (USULAN)" (unsur pengecualian dan label dikembalikan).
- Rekaman, Lokasi: "Folder Google Drive Departemen Legal (USULAN, SNX-LEG-SOP-03 butir 4.8) ... Pemilik: Line Manager Legal (SNX-LEG-SOP-03 butir 4.26, USULAN)." (rujukan 4.26 dikembalikan).
- Petunjuk 5: syarat "untuk status Sebagian Sesuai atau Tidak Sesuai" ditambahkan. Acuan 8.2.2: "yang berlaku" dikembalikan.
- Tabel 6.2 widths_cm [3.5, 2.0, 3.2, 2.6, 2.5, 2.2] (tidak ada kata terpotong); tabel 6.5 min_row_cm 2.0, tidak terbelah. Halaman tetap 15 (ISI hlm 10): Rekaman baris Bukti, Dokumen Terkait SNX-LEG-RPT-01 dan SNX-HR-ORG-01, serta Acuan 9.1 dipadatkan.
- Residu renderer: paragraf badan rata kiri-kanan berasal dari template; tidak ada medan spec untuk perataan paragraf.

### W10 rujukan USULAN dicek (adjudikasi worker, gerbang rujukan USULAN)
- .sections[4].blocks[4].p (butir 5): label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.
- .sections[7].blocks[1].table.rows[1][1]: label (USULAN) ditambah; teks ini menyatakan ulang isi butir berlabel (USULAN) yang rujukannya dihapus.

### W10 audit pointer
- .sections[3].blocks[0].table.rows[0][1]: lengkap (penunjuk balik ke daftar Ketentuan dibuang, semua tugas, jabatan, USULAN tetap)
- .sections[3].blocks[0].table.rows[1][1]: lengkap (penunjuk balik ke Ketentuan 16 dan 17 dibuang, tugas dan USULAN tetap)
- .sections[3].blocks[0].table.rows[2][1]: lengkap (penunjuk balik ke Ketentuan 8 dibuang, tugas menyerahkan Bukti utuh)
- .sections[3].blocks[0].table.rows[4][1]: lengkap (penunjuk balik ke Ketentuan 17 dibuang, keputusan tindak lanjut Manajemen dan USULAN tetap)
- .sections[4].blocks[1].p: lengkap (penunjuk Ketentuan 6 diganti isi perubahan peraturan yang dicatat ke SNX-LEG-REG-03; langkah evaluasi tetap di Ketentuan 6)
- .sections[4].blocks[4].p: rujukan dikembalikan (langkah mencatat Catatan Temuan di SNX-LEG-RPT-01 lebih dulu dan larangan mengulang tindakan: "sesuai Ketentuan butir 11")
- .sections[4].blocks[8].p: lengkap (isi Ketentuan 3 dan 13 disalin: Persyaratan Belum Diverifikasi tidak dihitung, Bidang dikosongkan beserta alasan, USULAN)
- .sections[6].blocks[1].table.rows[0][1]: lengkap (penunjuk balik ke Ketentuan 2 dibuang, isi sumber utuh)
- .sections[7].blocks[1].table.rows[0][1]: lengkap (penunjuk Ketentuan 18 dibuang, lokasi, pencatat, pemilik, klasifikasi, USULAN tetap)
- .sections[7].blocks[1].table.rows[1][1]: lengkap (penunjuk Ketentuan 18 dibuang, lokasi kolom Bukti yang Diperiksa, pencatat, pemilik tetap)

### W10 audit cakupan label
- .sections[0].blocks[4].p: OK (label tetap pada kolom Bukti dari Dokumen Legal)
- .sections[2].blocks[0].p: OK (label tetap pada frekuensi laporan)
- .sections[3].blocks[0].table.rows[0][1]: OK (label tetap pada Pelaksana Evaluasi)
- .sections[3].blocks[0].table.rows[1][1]: OK (label tetap pada pemilik dokumen)
- .sections[4].blocks[1].p: OK (label baru karena rujukan Ketentuan butir 6 yang berlabel diganti fakta, hanya kalimat itu)
- .sections[4].blocks[4].p: diperbaiki (label baru dihapus; rujukan butir 11 tetap, kalimat juga memuat alasan status yang tidak berlabel di bed1bb6)
- .sections[4].blocks[5].p: OK (label tetap pada cara hitung baris Seluruh Bidang)
- .sections[4].blocks[8].p: diperbaiki (dipisah; label hanya pada Persyaratan Belum Diverifikasi dari Ketentuan butir 3, isi butir 13 tanpa label)
- .sections[7].blocks[1].table.rows[0][1]: OK (label menggantikan rujukan Ketentuan butir 18 pada folder)
- .sections[7].blocks[1].table.rows[1][1]: diperbaiki (label ganda di akhir dihapus; cakupan sama dengan bed1bb6)

### W11 koreksi LEAD (cakupan dikembalikan ke bed1bb6, 15 Okt)
- .sections[7].blocks[1].table.rows[0][1]: cakupan, label, pelaku, atau rujukan dikembalikan ke bed1bb6 (temuan pemeriksa makna buta LEAD, reports/w11/)
