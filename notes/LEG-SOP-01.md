# Catatan penyusun LEG-SOP-01: SOP Legal Operational

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-SOP-01.json. Mode sop, aksi T1, wave W3, nomor SNX-LEG-SOP-01 (nomor lama dipertahankan), department Legal, classification INTERNAL (worklist), audit_class C2, review_period YEARLY, status Draft, revision 00, effective_date kosong. Judul meta "Legal Operational" (renderer menambah "SOP" di Document Title). Approval persis: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". process_owner "Line Manager Legal" (sumber: "Pemilik SOP: Line Manager Legal").

Uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-SOP-01.json /tmp/pen-LEG-SOP-01/LEG-SOP-01.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-LEG-SOP-01/LEG-SOP-01.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "20 butir (USULAN) menunggu ACC" (nol warn PIC SLA). Pratinjau PDF (soffice) 23 halaman dilihat lewat contact sheet: sampul, Identity, Revision, Approval, TOC, 11 bagian, dan diagram tampil; diagram dilihat dalam resolusi penuh (13 simpul, rankdir TB, tiga belah ketupat terbaca). Spec memuat 30 butir kebijakan (4.1 sampai 4.30), 10 prosedur (6.1 sampai 6.10) dengan 64 langkah, 17 baris SLA, 6 baris pengecualian, 9 baris rekaman.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SOP Divisi Legal – SINUX.docx (16407 byte, mimeType docx) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (get_file_metadata, dicek ulang hari ini, sama dengan prompt; createdTime 2026-10-13T10:54:47.319Z) | read_file_content (teks utuh, dibandingkan bagian per bagian dengan transkripsi di context/audit bagian 2: sama). download_file_content mengembalikan docx inline (base64), tidak tersimpan ke berkas, sehingga tidak didekode; daftar bagian zip yang terbaca di hasil: numbering, settings, fontTable, styles, customXML, core, document, theme, tanpa comments, footnotes, header, atau footer. Tracked change dan teks tersembunyi di document.xml tidak diuji (lihat Open items 15) |
| Kriteria penerimaan | config/checklist.json baris 34 (dept LEG, "SOP Legal Operational") | checklist modifiedTime tidak diukur ulang di sesi ini | Kolom Description: "SOP ini menjadi panduan departemen Legal untuk menjalankan pekerjaan dan koordinasi antara Line Manager, Staf, serta koordinasi dengan departemen lain." Kolom iso_9001 dan iso_27001 baris ini null |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, K-03, K-13), specs/HR-JA-01.json (uraian JA-08 dan JA-09, Authority Matrix), config/defaults.json v21, specs/ISMS-PRO-01.json (tingkat klasifikasi), context/audit (bagian SOP Divisi Legal dan Jobdesk Line Manager Legal) | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah |

Catatan: link di checklist baris 34 menunjuk fileId 1YxX0cPQDjqaJyQsxEdw-uKnP5XUN_8WK dengan judul sama; get_file_metadata atas fileId itu memberi "Requested entity was not found". Prompt dan worklist memakai 19peOeN1yA-...; yang dipakai di sini.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Pengguna SOP: Line Manager Legal, Staff Legal, dan unit bisnis pemohon, termasuk entitas afiliasi. Di dokumen menjadi Scope, dengan "Pemohon" = departemen SINUX yang mengajukan permintaan | "Berlaku bagi Line Manager Legal dan seluruh Staff Legal, serta unit bisnis SINUX yang mengajukan permintaan legal. Mencakup juga entitas afiliasi atau turunan (misalnya rencana pendirian PT Nusagrid) sepanjang ditugaskan kepada Divisi Legal SINUX." (1. Tujuan, Ruang Lingkup, dan Prinsip) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 2 | Pembagian kerja Line Manager dan Staf: Staff menyiapkan, Line Manager mereview dan menyetujui atau mengembalikan. Di dokumen menjadi butir 4.6 dan prosedur 6.2 langkah 7 dan 8 | "Bagian ini mengatur alur kerja di dalam Divisi Legal: Staff Legal menyiapkan, Line Manager Legal mereview dan menyetujui." (4. SOP Internal Tim Legal) dan "Review Line Manager. Staff menyerahkan draf, tabel redline, dan ringkasan risiko; Line Manager menyetujui atau mengembalikan dengan catatan." (4.1 butir 6) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |
| 3 | Koordinasi dengan departemen lain: kewajiban Pemohon dan batas waktu jawab. Di dokumen menjadi butir 4.7 sampai 4.15, bagian 8, dan prosedur 6.1 | "Melibatkan Legal sejak tahap negosiasi komersial, sebelum ada komitmen tertulis kepada pihak luar." dan "Menjawab pertanyaan Legal dalam 2 hari kerja; tenggat Legal bergeser sebesar keterlambatan jawaban." dan "Tidak menandatangani, menjanjikan, atau mengirim dokumen final sebelum persetujuan Legal dan pejabat berwenang sesuai DoA." (3.2 Kewajiban Divisi Pemohon, butir 1, 4, 5) | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb |

## 2. Fakta pendukung dan kutipan

Semua kutipan dari fileId 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb. Penanda markdown dan garis miring terbalik di keluaran alat dibuang; tanda hubung pada "3-5" di sumber ditulis "3 sampai 5" di dokumen.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "Menetapkan standar kerja Divisi Legal agar seluruh aspek hukum SINUX (kontrak, korporasi, perizinan, kepatuhan, dan sengketa) ditangani secara tertib, dapat ditelusuri, dan melindungi kepentingan perusahaan." | Purpose |
| 2 | Lima prinsip kerja | "Tidak ada kontrak yang ditandatangani tanpa review Legal." / "Semua pekerjaan tercatat (register, versi dokumen, riwayat persetujuan)." / "Risiko diklasifikasikan dan dieskalasi sesuai tingkatnya, bukan disimpan sendiri." / "Kerahasiaan dokumen dan data adalah kewajiban mutlak." / "Legal memberi opini dan rekomendasi risiko; keputusan bisnis tetap berada pada pemilik keputusan (manajemen/direksi)." | Butir 4.1 sampai 4.5 |
| 3 | Intake | "Pemohon mengirim permintaan melalui kanal resmi [ISI: email/tiket/form] dengan data minimal: pihak, objek, nilai, jangka waktu, tenggat, dan dokumen pendukung." / "Staff Legal mencatat permintaan di register, memberi nomor, dan menentukan prioritas." / "Permintaan yang tidak lengkap dikembalikan kepada pemohon dengan daftar kekurangan." / "Line Manager menugaskan Staff Legal dan menetapkan tenggat." | 6.1, butir 4.7 dan 4.8 |
| 4 | Target waktu, berlabel usulan di sumber | "Target waktu (usulan)": NDA standar 1 hari kerja dan 2 hari kerja; Review kontrak/PKS 1 hari kerja dan 3–5 hari kerja; Draf kontrak baru 1 hari kerja dan 5 hari kerja; Dokumen korporasi/perizinan 2 hari kerja dan "Sesuai proses pihak ketiga"; Urgent "Hari yang sama" dan "Disepakati" | Bagian 8, lima baris pertama |
| 5 | Hasil untuk Pemohon | "Konfirmasi penerimaan dan nomor register permintaan." / "Status permintaan yang dapat ditanyakan kapan saja kepada Staff Legal yang ditugaskan." | Butir 4.15, 6.1 langkah 3 |
| 6 | Klausul kritis | "Klausul kritis yang wajib diperiksa: ruang lingkup dan deliverable; harga dan mekanisme pembayaran (termasuk apakah pembayaran bergantung pada pembayaran klien akhir); batas tanggung jawab dan ganti rugi; hak penangguhan pembayaran atau layanan; ..." (4.1 butir 4) | Butir 4.16 |
| 7 | Persetujuan sesuai DoA | "Persetujuan internal. Kontrak melewati persetujuan sesuai DoA [ISI: nilai/jenis kontrak dan pejabat]." (4.1 butir 8) | Butir 4.20, 6.2 langkah 11 dan 12 |
| 8 | Penandatanganan dan arsip | "Dalam 2 hari kerja setelah ditandatangani: unggah salinan final ke arsip, perbarui register (para pihak, nilai, tanggal efektif, jatuh tempo, pengingat perpanjangan/terminasi, PIC bisnis)." / "Dokumen asli disimpan di tempat yang aman dengan kontrol akses [ISI]." | 6.4 langkah 6 sampai 8, butir 4.25, bagian 8 |
| 9 | Pemantauan kontrak | "Register ditinjau setiap bulan oleh Staff Legal; kontrak yang jatuh tempo dalam 90 hari ditandai." / "Pengingat dikirim kepada PIC bisnis 90, 60, dan 30 hari sebelum jatuh tempo atau batas pemberitahuan terminasi." | 6.5, bagian 8 |
| 10 | Korporasi dan perizinan | "Pendirian atau spin-off entitas. Analisis KBLI terhadap kegiatan usaha, pengecekan persyaratan modal dan perizinan sektor, penyiapan dokumen pendirian, dan pengurusan NIB melalui OSS sesuai PP No. 5 Tahun 2021 dan peraturan turunannya." / "Kewajiban pelaporan berkala (mis. LKPM) dipantau bersama Finance/Compliance [ISI]." | 6.6 |
| 11 | Pelindungan data pribadi dan koordinasi dengan keamanan/IT | "Legal berkoordinasi dengan tim keamanan/IT untuk pelaporan insiden dan perjanjian pemrosesan data." / "Perubahan regulasi yang relevan dipantau dan diringkas dalam memo kepatuhan setiap kuartal." | 6.7, butir 4.21 |
| 12 | Sengketa | "Strategi (negosiasi, mediasi, somasi balasan, atau jalur litigasi) diputuskan oleh manajemen berdasarkan rekomendasi Line Manager." / "Penunjukan advokat eksternal mengikuti batas wewenang Line Manager Legal pada dokumen Jobdesk." | 6.8, butir 4.28 dan 4.29 |
| 13 | Dokumen dan akses | "Dokumen legal diklasifikasikan (Rahasia, Internal, Publik) dan disimpan pada repositori resmi [ISI]." / "Akses diberikan berdasarkan kebutuhan kerja dan dicabut saat peran berakhir." / "Dokumen rahasia tidak dikirim melalui kanal pribadi." / "Retensi dokumen mengikuti ketentuan peraturan perundang-undangan dan kebijakan perusahaan [ISI: periode retensi]." | Butir 4.22 sampai 4.27, 6.9 |
| 14 | Eskalasi risiko | "Tinggi ... Hentikan proses; eskalasi ke manajemen dengan rekomendasi tertulis" / "Sedang ... Negosiasi; laporkan dalam ringkasan" / "Rendah ... Perbaiki langsung" (5. Eskalasi Risiko) | Butir 4.17 sampai 4.19, 6.3 |
| 15 | Pelaporan | "Mingguan: rapat singkat Line Manager dan Staff (status pekerjaan, hambatan, prioritas)." / "Bulanan: laporan kepada manajemen (jumlah permintaan, kontrak selesai, risiko tinggi, izin yang akan jatuh tempo)." / "Triwulanan: memo kepatuhan dan pembaruan playbook/template." | 6.10, bagian 8 |
| 16 | Kontrol dokumen SOP | "Pemilik SOP: Line Manager Legal." / "Ditinjau minimal setahun sekali atau saat ada perubahan regulasi/struktur organisasi." / "Riwayat revisi: v0.1 (Oktober 2026), draf awal untuk review." / "Persetujuan: [ISI: pejabat yang menyetujui]." | Identity (process_owner), bagian 8, Revision History (diganti Rev. 00 menurut defaults), Approval |
| 17 | Lampiran belum disusun | "Lampiran yang Disarankan (belum disusun)": template NDA, PKS, dan addendum; playbook klausul; format tabel redline dan ringkasan risiko; format register kontrak dan register perizinan; matriks delegasi wewenang (DoA) penandatanganan kontrak | Scope (pengecualian), bagian 11 |

## 3. Pemetaan klausul ISO (kriteria)

Checklist tidak memberi acuan klausul untuk baris ini. Klausul di bagian 11 dipilih dari isi dokumen dan berlabel satu kali "(USULAN, perlu konfirmasi konsultan)". SoA = konsultan; keterkaitan dengan kontrol 5.31 yang disebut audit (status "Perlu keputusan") adalah inferensi audit, bukan keputusan.

| Klausul | Isi dokumen yang dirujuk |
|---|---|
| ISO 9001:2015 5.3 | Bagian 5 dan butir 4.6 (pembagian menetapkan, menyiapkan, memutuskan) |
| ISO 9001:2015 7.4 | Koordinasi dengan Pemohon dan departemen lain: prosedur 6.1 dan 6.10 |
| ISO 9001:2015 7.5.3 | Register, versi dokumen, arsip, retensi: butir 4.2 dan 4.27 |
| ISO 9001:2015 8.2.3 | Review kontrak oleh Departemen Legal sebelum penandatanganan: butir 4.1 dan prosedur 6.2 |
| ISO/IEC 27001:2022 Annex A 5.31 | Prosedur 6.2, 6.6, 6.7 (persyaratan hukum, regulasi, kontrak) |
| ISO/IEC 27001:2022 Annex A 5.34 | Butir 4.21 (data pribadi, UU No. 27 Tahun 2022) |
| ISO/IEC 27001:2022 Annex A 5.12 | Butir 4.22 (klasifikasi) |
| ISO/IEC 27001:2022 Annex A 5.15 | Butir 4.26 (akses berdasarkan kebutuhan kerja) |
| ISO/IEC 27001:2022 Annex A 5.33 | Butir 4.27 (retensi dan perlindungan rekaman) |

## 4. Keputusan data dan pemetaan peran

- Approval, status, revision, effective_date, review_period, revision_desc: persis dari prompt dan config/defaults.json v21 (D2). Sumber menulis "Persetujuan: [ISI: pejabat yang menyetujui]"; defaults mengalahkan sumber.
- Samuel di badan dokumen: tidak disebut sendiri; "Direktur Utama" hanya muncul di definisi Manajemen. Sumber tidak memakai CEO untuk Samuel di berkas ini (CEO muncul di Jobdesk Line Manager Legal, bukan di sumber ini).
- Sebutan COO: "Direktur (COO)" satu kali, di definisi Manajemen (sebutan pertama di badan dokumen, bagian 3); sesudahnya "COO" dua kali (bagian 5). Dicek dengan pencarian atas teks docx: satu "Direktur (COO)", dua "COO" sesudahnya, nol sebelumnya. Kata "Direksi" dari sumber diganti "Manajemen".
- Tiket: Legal = generalist, jadi GLPI (SINUX Service Hub). Zammad tidak dipakai di dokumen ini. Batas "generalist" belum dirinci owner (defaults), maka kanal berlabel (USULAN) dan masuk open item.
- Vault dan PPN tidak relevan untuk SOP ini.
- Klasifikasi dokumen ini: INTERNAL (worklist). Klasifikasi dokumen legal yang diatur SOP: tingkat SNX-ISMS-PRO-01 menggantikan label Indonesia "Rahasia, Internal, Publik" (butir 4.22 dan 4.23).
- Istilah satu per satu: "Departemen Legal" (kriteria memakai "departemen Legal"; sumber "Divisi Legal"), "Pemohon" (sumber: "Unit Bisnis/Pemohon", "pemohon", "Divisi Pemohon", "unit bisnis SINUX"), "Manajemen" (sumber: "manajemen/direksi", "Direksi/COO"), "DoA" (sumber; HR-JA-01 memakai Authority Matrix, dicatat di definisi).

Pemetaan peran sumber ke nama peran HR-ORG-01 (specs/HR-ORG-01.json: Daftar Jabatan dan Matriks Peran):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Line Manager Legal | Line Manager Legal | Matriks Peran HR-ORG-01: Line Manager Legal = Legal & Compliance (JA-08), "(USULAN), menunggu konfirmasi (K-13)" |
| Staff Legal (Senior/Junior) | Staff Legal | Matriks Peran HR-ORG-01: Staff Legal = JA-09. Penanda Senior/Junior dibuang: HR-ORG-01 dan Jobdesk Staff Legal tidak membedakan level |
| Unit Bisnis/Pemohon | Pemohon | Tidak ada di HR-ORG-01 (bukan jabatan). Dibuat istilah satu kata, didefinisikan di bagian 3: departemen SINUX selain Legal |
| manajemen/direksi, Direksi/COO | Manajemen (Direktur Utama dan COO) | HR-ORG-01 JA-01 Direktur Utama dan JA-02 Direktur; HR-JA-01 mendefinisikan Management sebagai unit tempat JA-01 dan JA-02 berada |
| atasan Line Manager Legal | COO | HR-ORG-01 daftar jabatan: JA-08 melapor ke Direktur (JA-02), menunggu konfirmasi (K-03) |
| tim keamanan/IT | VP Tech Operation and Services | Jabatan terdekat: Matriks Peran HR-ORG-01 menaruh kontrol keamanan, akses, backup, dan perubahan teknis pada JA-04. Pemetaan tafsir (USULAN) |
| Finance/Compliance | Finance | HR-ORG-01 JA-10 "Finance". Fungsi Compliance berada di jabatan Legal & Compliance (JA-08, JA-09), jadi tidak diberi peran terpisah (USULAN) |
| notaris | Notaris | Pihak luar, tidak ada di HR-ORG-01 |
| advokat, konsultan, regulator | Tidak jadi peran | Tidak punya langkah di sumber; disebut sebagai pihak luar di butir 4.29 dan 6.8 hanya untuk advokat |

## 5. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb)

Perintah: `grep -n 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb context/audit/*.md` (baris 1055 file legal dan baris 88 file sintesis; bagian dokumen dibaca dari sekitar baris 1050 sampai 1320).

| # | Cacat di audit | Penanganan |
|---|---|---|
| 1 | Status v0.1 draf, tanpa nomor, tanggal lengkap, persetujuan | Nomor SNX-LEG-SOP-01, Rev. 00, status Draft, effective_date kosong, approval dari defaults |
| 2 | Delapan placeholder [ISI] | Semua diganti USULAN berlabel; lihat tabel di bawah |
| 3 | Rujukan menggantung "alur 5.2 dan 5.3" di 4.3 butir 3 | Diperbaiki: 6.5 langkah 3 menulis "Proses addendum atau amandemen lewat prosedur 6.2 dan 6.4" (review dan negosiasi, penandatanganan). Tafsir audit sendiri "4.1 dan 4.2" (inferensi); pemetaan ke nomor baru. Dicatat di Open items 14 |
| 4 | Atasan Line Manager Legal berbeda di tiga sumber | Bagian 5 dan definisi: COO (USULAN), mengikuti HR-ORG-01 K-03. Sumber lain (CEO di Jobdesk, "Management / Direktur" di HR-JA-001) tidak dipakai. Open items 2 |
| 5 | Target waktu berlabel usulan; KPI Jobdesk bergantung pada SLA ini | Label (USULAN) dipertahankan di tiap baris lima jenis pekerjaan. KPI bukan scope SOP ini (ada di SNX-HR-JA-01) |
| 6 | Lampiran belum disusun; register kontrak dan perizinan belum ada | Tidak dibuat (di luar scope T1). Disebut sebagai pengecualian di Scope dan baris "Belum bernomor" di bagian 11. Register perizinan dipadankan ke SNX-LEG-REG-01 (USULAN). Open items 9 |
| 7 | Retensi dan lokasi repositori tidak ada; SLA korporasi dan urgent tanpa angka | Retensi: "Belum ditetapkan" di tabel rekaman, penetapan diusulkan di SNX-LEG-SOP-03. Repositori: Google Drive departemen Legal (USULAN). SLA korporasi dan urgent ditulis sesuai sumber ("sesuai proses pihak ketiga", "disepakati"); tidak diberi angka karangan. Open items 7 |
| 8 | "Legal memberi opini" bertentangan dengan "Hentikan proses" dan "menahan kontrak" | Dipadukan lewat butir 4.5, 4.6, 4.17 dan prosedur 6.3: Departemen Legal memberi opini dan rekomendasi; Line Manager Legal menghentikan proses di Departemen Legal dan mengeskalasi; keputusan atas risiko Tinggi ada pada Manajemen. Selaras dengan HR-JA-01 ("Legal memberi opini; penahanan berlaku hanya atas keputusan Management (USULAN)"). Open items 5 |
| 9 | Tanpa rujukan klausul ISO; tanpa klasifikasi dokumen untuk SOP itu sendiri | Bagian 11 Acuan standar (berlabel); klasifikasi INTERNAL |
| 10 | Rujukan peraturan tidak diverifikasi di luar sumber | PP No. 5 Tahun 2021 dan UU No. 27 Tahun 2022 ditulis apa adanya seperti sumber; tidak diverifikasi. Open items 17 |
| 11 | "Staff Legal (Senior/Junior)" tanpa dasar di Jobdesk; batas wewenang penunjukan advokat di Jobdesk kosong | Level dibuang (satu peran Staff Legal). Butir 4.29 menyatakan batas belum ditetapkan di SNX-HR-JA-01; langkah 6.8.7 merujuk butir itu. Open items 4 |
| 12 | Label klasifikasi Indonesia berbeda dari skema PRO-01; SOP tidak merujuk PRO-01 | Butir 4.22 memakai PUBLIC, INTERNAL, RESTRICTED (Internal), SECRET; butir 4.23 memberi padanan "Rahasia" (USULAN). SNX-ISMS-PRO-01 masuk bagian 11 |

Delapan placeholder [ISI] dan hasilnya:

| # | Placeholder sumber | Hasil di dokumen | Letak |
|---|---|---|---|
| 1 | "[ISI: atasan, mis. Direksi/COO]" | Line Manager Legal melapor ke COO (USULAN, K-03) | Bagian 5, baris Line Manager Legal |
| 2 | "[ISI: email/tiket/form]" | Tiket GLPI (USULAN) | Butir 4.7, 6.1 langkah 1 |
| 3 | "[ISI: nilai/jenis kontrak dan pejabat]" | Nilai, jenis, pejabat ada di DoA yang belum terbit; sampai terbit Manajemen memutuskan tiap kontrak (USULAN) | Butir 4.20, 6.2 langkah 11 dan 12 |
| 4 | "[ISI]" kontrol akses dokumen asli | Tempat aman, akses terbatas pada Line Manager Legal dan Staff Legal (USULAN) | Butir 4.25 |
| 5 | "[ISI]" pelaporan berkala LKPM | Staff Legal memantau bersama Finance; penanggung jawab dan jadwal dicatat di register perizinan (USULAN) | 6.6 langkah 10 dan 11, bagian 5 baris Finance |
| 6 | "[ISI]" repositori resmi | Folder Google Drive departemen Legal (USULAN) | Butir 4.24, tabel rekaman |
| 7 | "[ISI: periode retensi]" | Periode belum ditetapkan; usulan penetapan di SNX-LEG-SOP-03 (USULAN) | Butir 4.27, kolom Retensi |
| 8 | "[ISI: pejabat yang menyetujui]" | Samuel Kristanto Utomo / President Director (defaults D2) | Blok Approved By |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

- Pelaku langkah yang di sumber berbentuk pasif (mencatat, memeriksa, mengunggah, mengingatkan, membuka dan mencabut akses, melaporkan pelanggaran) ditetapkan dari kalimat pembuka bagian 4 sumber ("Staff Legal menyiapkan, Line Manager Legal mereview dan menyetujui") dan dari uraian jabatan Legal di specs/HR-JA-01.json (JA-08, JA-09). Butir 4.6 menyatakan ini berstatus (USULAN) dan mencakup pemilik rekaman.
- "unit bisnis" di sumber dibaca "departemen SINUX selain Legal" karena kriteria memakai "departemen lain". Bila sumber memang membatasi pada departemen bisnis, definisi Pemohon perlu dipersempit.
- "Divisi Legal" di sumber ditulis "Departemen Legal" (kriteria baris). "Tim Legal" di judul bagian 4 sumber tidak dipakai.
- Kalimat tim yang diubah: "Kerahasiaan dokumen dan data adalah kewajiban mutlak" menjadi "Departemen Legal menjaga kerahasiaan dokumen dan data" (butir 4.4; "mutlak" adalah penegasan, pelaku diberi nama). Kalimat tim lain dipertahankan dengan perubahan hanya pada pelaku, istilah, dan pemisahan satu langkah satu tindakan. Daftar klausul kritis dan contoh risiko Tinggi dipertahankan utuh.
- Angka dari sumber dipakai pada lingkupnya: 2 hari kerja jawaban Pemohon (Pemohon), 1 hari kerja lapor somasi (Pemohon dan Staff Legal), 2 hari kerja arsip dan register, 90, 60, 30 hari pengingat kontrak, 90 hari pengingat izin (sumber 4.4 butir 3). Tidak ada angka diperluas ke aktivitas lain.
- Output "Penghentian proses tercatat (butir 4.2)" di 6.3 langkah 1 memakai prinsip "Semua pekerjaan tercatat"; nama rekaman lain di kolom Output adalah nama hasil kerja dari kalimat sumber, bukan formulir bernomor.
- Sumber Bagian 7 "Riwayat revisi: v0.1 (Oktober 2026)" tidak dibawa; Revision History memakai Rev. 00 dan deskripsi dari defaults.
- Sumber Bagian 6 Pelaporan dibagi ke dua tempat: aturan frekuensi di bagian 8 (SLA), langkah di 6.10. Playbook dan template yang "belum disusun" tetap ditulis sebagai objek pembaruan triwulanan karena sumber menulisnya begitu.
- Diagram bagian 7 hanya memuat jalur kontrak (permintaan sampai pemantauan); jalur korporasi, kepatuhan, dan sengketa ada di prosedur 6.6 sampai 6.8 tanpa diagram. Caption menyebut lingkupnya.

## USULAN

Delapan placeholder [ISI] tercakup (butir 1 sampai 8). Lint menghitung 20 kemunculan "(USULAN)" termasuk baris definisi label, lima baris SLA, dan dua label pemetaan peran Legal di bagian 5 (butir 14). Total 17 butir keputusan.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Atasan Line Manager Legal = COO (ganti placeholder 1; tiga sumber berbeda) | Bagian 5 baris Line Manager Legal | owner, dikukuhkan Samuel (HR-ORG-01 K-03) |
| 2 | Kanal permintaan = tiket GLPI (ganti placeholder 2) | Butir 4.7, 6.1 | owner (batas "generalist") |
| 3 | Sampai DoA terbit, Manajemen memutuskan persetujuan tiap kontrak (ganti placeholder 3) | Butir 4.20 | Samuel |
| 4 | Dokumen asli di tempat aman dengan akses terbatas pada Line Manager Legal dan Staff Legal (ganti placeholder 4) | Butir 4.25, tabel rekaman | Legal |
| 5 | Pemantauan pelaporan berkala (LKPM) oleh Staff Legal bersama Finance; penanggung jawab dan jadwal di register perizinan; "Finance/Compliance" dipetakan ke Finance (ganti placeholder 5) | 6.6 langkah 10 dan 11, bagian 5 | FAT |
| 6 | Repositori resmi = folder Google Drive departemen Legal (ganti placeholder 6) | Butir 4.24, tabel rekaman | Legal |
| 7 | Periode retensi belum ditetapkan, penetapan di SNX-LEG-SOP-03 (ganti placeholder 7) | Butir 4.27, kolom Retensi | Legal |
| 8 | Penyetuju SOP = Samuel Kristanto Utomo / President Director (ganti placeholder 8; defaults D2, bukan label di badan dokumen) | Blok Approved By | Samuel |
| 9 | Pelaku langkah pasif dan pemilik rekaman ditetapkan dari pembagian peran dan HR-JA-01 | Butir 4.6, tabel rekaman | Legal |
| 10 | Label Rahasia di sumber setara RESTRICTED (Internal) dan SECRET | Butir 4.23 | Fani (pemilik skema SNX-ISMS-PRO-01 di sisi Operation dan ISMS) |
| 11 | "tim keamanan/IT" dipetakan ke VP Tech Operation and Services | Bagian 5, 6.7 langkah 2 | Fani |
| 12 | Lima baris target waktu tetap berlabel usulan seperti sumber; penyelesaian urgent "disepakati Line Manager Legal dan Pemohon" (pihak penyepakat bukan dari sumber) | Bagian 8 baris 1 sampai 5 | Legal, dikukuhkan owner |
| 13 | DoA dibaca sama dengan Authority Matrix di SNX-HR-JA-01 | Definisi DoA | Legal |
| 14 | Line Manager Legal dan Staff Legal dipasangkan ke JA-08 dan JA-09 (dari HR-ORG-01 K-13) | Bagian 11, SNX-HR-ORG-01 | Aziz, dengan Legal |
| 15 | SNX-LEG-REG-01 sebagai register perizinan | Bagian 11 | Legal |
| 16 | SNX-LEG-FRM-03 sebagai tempat hasil tinjauan pelindungan data pribadi | Bagian 11 | Legal |
| 17 | Daftar klausul ISO 9001:2015 (5.3, 7.4, 7.5.3, 8.2.3) dan ISO/IEC 27001:2022 (Annex A 5.31, 5.34, 5.12, 5.15, 5.33), label "(USULAN, perlu konfirmasi konsultan)" | Bagian 11, Acuan standar | owner, diteruskan ke konsultan |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Batas "generalist" untuk tiket GLPI belum dirinci owner. Apakah semua permintaan layanan legal masuk GLPI, atau ada yang lewat Zammad | owner |
| 2 | Atasan Line Manager Legal berbeda di sumber ("Direksi/COO"), Jobdesk ("CEO"), dan HR-JA-001 ("Management / Direktur"); HR-ORG-01 K-03 masih menunggu | owner, Samuel |
| 3 | DoA (Authority Matrix) belum terbit: pejabat penyetuju, batas nilai, dan jenis kontrak kosong. Butir 4.20 hanya jembatan sementara | Samuel |
| 4 | Batas wewenang Line Manager Legal menunjuk notaris, konsultan, advokat kosong di Jobdesk dan "Belum ditetapkan" di SNX-HR-JA-01; butir 4.29 dan 6.8 langkah 7 bergantung padanya | Legal, Samuel |
| 5 | Konfirmasi tafsir pertentangan "memberi opini" dan "hentikan proses": Line Manager Legal menghentikan proses di Departemen Legal, keputusan di Manajemen. Jobdesk memakai kata "menahan kontrak" | Legal |
| 6 | Periode retensi dan lokasi arsip (termasuk dokumen asli) belum ada; SNX-LEG-SOP-03 harus memutus dan dokumen ini diselaraskan | Legal |
| 7 | Tanpa angka di sumber: penyelesaian dokumen korporasi dan urgent; waktu lapor pelanggaran atau wanprestasi kontrak ("segera"); penanganan surat regulator dan perubahan fakta yang dilaporkan Pemohon (sumber hanya mewajibkan laporan) | Legal |
| 8 | Pemohon yang menandatangani, menjanjikan, mengirim, atau mengubah dokumen tanpa review: sumber melarang tanpa menetapkan penanganan, maka tidak ada baris di bagian 9 | Legal, Samuel |
| 9 | Register permintaan tidak punya format lampiran dan tidak ada dokumen bernomor di checklist; register kontrak juga tidak ada. Menambah baris checklist di luar 88 baris hanya bila konsultan meminta | Legal, owner |
| 10 | Tumpang tindih dengan SNX-LEG-SOP-02 (Contract Review & Legal Approval) dan SNX-LEG-SOP-03 (Legal Document Control & Retention): sinkronkan prosedur 6.2, 6.4, dan 6.9 setelah ketiganya selesai | Legal |
| 11 | Skala risiko dokumen ini tiga tingkat (Tinggi, Sedang, Rendah). Audit mencatat Legal Risk Register memakai Rendah, Sedang, Tinggi, Sangat Tinggi (SNX-LEG-REG-02) | Legal |
| 12 | Jobdesk Line Manager Legal memuat hubungan kerja dengan Finance (pembayaran, pajak, bea meterai) dan Human Resources (kontrak kerja) yang tidak punya langkah di sumber SOP; hanya pelaporan berkala dengan Finance yang ada di sumber | Legal |
| 13 | "Staff Legal (Senior/Junior)" di sumber: level dibuang. Konfirmasi bahwa tidak ada perbedaan wewenang antarlevel | Legal, Aziz |
| 14 | Rujukan menggantung "alur 5.2 dan 5.3" dipetakan ke review dan penandatanganan (6.2 dan 6.4); konfirmasi maksud tim | Legal |
| 15 | document.xml sumber tidak didekode (hasil download_file_content inline); tracked change dan teks tersembunyi belum diperiksa. Tidak ada comments, footnotes, header, footer menurut daftar bagian zip | owner (unduh ulang manual bila perlu) |
| 16 | Link checklist baris 34 menunjuk fileId 1YxX0cPQDjqaJyQsxEdw-uKnP5XUN_8WK yang tidak terbaca lewat konektor; konfirmasi bahwa isinya sama dengan 19peOeN1yA-... | owner |
| 17 | Rujukan PP No. 5 Tahun 2021 dan UU No. 27 Tahun 2022 ditulis seperti sumber, belum diverifikasi oleh Legal atau konsultan | Legal |
| 18 | Staff Legal tidak berwenang memberi persetujuan hukum final: HR-JA-01 (JA-09) menyatakannya, sumber diam. Dokumen ini hanya menulis "Persetujuan ada pada Line Manager Legal" di tabel peran. Konfirmasi | Legal |

## 7. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya lima tanda; empat saya perbaiki dan satu saya biarkan:
   - Kalimat Purpose memakai tiga "untuk" berurutan ("untuk menjalankan..., untuk berkoordinasi..., dan untuk berkoordinasi...") yang terdengar kelompok tiga dipaksakan. Diperbaiki: dua bagian ("menjalankan pekerjaan hukum, dengan koordinasi antara Line Manager Legal dan Staff Legal serta koordinasi dengan departemen lain").
   - Isi yang sama muncul di dua bagian: daftar kolom register di definisi dan di langkah, daftar yang diperiksa due diligence di definisi dan di langkah, kolom tabel redline di definisi dan di langkah, angka batas waktu di kebijakan, langkah, dan SLA. Diperbaiki: definisi hanya arti, aturan di bagian 4, angka batas waktu hanya di bagian 8, langkah merujuk nomor butir.
   - Definisi "Permintaan" memakai kata "permintaan layanan legal" untuk dirinya sendiri (melingkar), dan frasa "dokumen sumber" menempel di badan dokumen. Diperbaiki: "Pengajuan satu pekerjaan hukum oleh Pemohon...", dan "dokumen sumber" diganti nama dokumennya (SOP Divisi Legal versi 0.1) yang juga masuk tabel Dokumen terkait.
   - Rujukan silang berbunyi "langkah 6 di 6.4 dan langkah 7 di 6.4". Diperbaiki menjadi "6.4 langkah 6 dan 7".
   - Dibiarkan: banyak butir dan langkah dibuka dengan "Staff Legal" atau "Pemohon", dan kolom Output memakai pola "Hasil pemeriksaan ...". Itu mengikuti satu pelaku per langkah dan nama hasil kerja; mengganti variasi hanya agar terdengar manusiawi bisa mengaburkan pelaku. Kalimat "Tidak ada wewenang persetujuan di SOP ini" muncul tiga kali di tabel peran dengan kata yang sama karena fakta yang sama.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa terhadap tabel Fakta kunci, tabel peran, dan USULAN:
   - Angka: 1, 2, 3 sampai 5, 5 hari kerja, 90, 60, 30 hari, dan 2 hari jawaban, semuanya dari sumber (target waktu berlabel usulan di sumber). Tidak ada angka lain di dokumen. Tidak ada tanggal selain "Oktober 2026" dan "versi 0.1" pada nama draf sumber (dari sumber).
   - Nama orang: hanya Samuel Kristanto Utomo di blok Approved By (defaults). Nama badan: PT Nusagrid (sumber), SINUX. Nama sistem: GLPI dan SINUX Service Hub (defaults), Google Drive (USULAN, tidak ada di sumber), OSS dan NIB (sumber).
   - Dari pengetahuan umum, bukan sumber: kepanjangan KBLI, NIB, OSS, LKPM, NDA, DoA, PKS; definisi Addendum, Somasi, Wanprestasi, Term sheet; judul klausul ISO. Kepanjangan LKPM dan DoA tidak ditulis di sumber; sisanya istilah baku. Ini tercatat agar Legal dapat mengoreksi.
   - Pelaku tiap langkah pasif dan pemilik rekaman bukan dari sumber (USULAN 9). Nama hasil kerja di kolom Output ("Hasil pemeriksaan penandatangan", "Paket review") adalah rumusan penyusun.
   - Diperbaiki sebelum selesai: kata "Catatan penghentian proses" (nama rekaman karangan) diganti "Penghentian proses tercatat (butir 4.2)" yang bersandar pada prinsip sumber "Semua pekerjaan tercatat".

## Sweep

Putaran penghalusan sesudah DONE (15 Okt 2026). Hanya dua butir diubah; fakta, angka, nama, dan struktur lain tetap. Diff terhadap versi ter-commit (8cdd7bb) dicek: hanya baris di bawah yang berbeda.

| # | Butir | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Label klausul ISO (spec, bagian 11 Acuan standar; notes bagian 3 dan USULAN 17) | "(USULAN, dikonfirmasi konsultan)" | "(USULAN, perlu konfirmasi konsultan)" |
| 2a | Bagian 5, baris Line Manager Legal dan Staff Legal | Tanpa keterangan pemetaan jabatan | Ditambah kalimat penutup: "Dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." dan sama untuk JA-09, mengikuti rumusan di SNX-LEG-SOP-03 |
| 2b | Bagian 11, baris SNX-HR-JA-01 | "memuat uraian tugas, wewenang, dan indikator kinerja Line Manager Legal dan Staff Legal" | "memuat uraian jabatan Legal & Compliance (JA-08 dan JA-09), tempat peran Line Manager Legal dan Staff Legal dipetakan" |
| 2c | Bagian 11, baris SNX-HR-ORG-01 | "Line Manager Legal dan Staff Legal dipetakan ke JA-08 dan JA-09 (USULAN, butir K-13)" | "Peran Line Manager Legal dan Staff Legal dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09) (USULAN, butir K-13)" |
| 2d | Tabel rekaman bagian 11, 8 baris (register permintaan, register kontrak, register perizinan, draf dan catatan negosiasi, salinan final, dokumen asli, berkas kasus, memo kepatuhan) | "pemilik Staff Legal" | "pemilik Line Manager Legal" (baris Laporan bulanan sudah Line Manager Legal) |
| 2e | Butir 4.6 | Pembagian menetapkan, menyiapkan, memutuskan, lalu kalimat USULAN pelaku dan pemilik rekaman | Disisipi: "Line Manager Legal menjadi pemilik rekaman Departemen Legal di bagian 11 dan Staff Legal pencatatnya, sama dengan SNX-LEG-SOP-03." |

Alasan 2d dan 2e: SNX-LEG-SOP-03 butir 4.26 menetapkan Line Manager Legal sebagai pemilik rekaman dan Staff Legal sebagai pencatat, dan seluruh baris tabel Rekaman di sana berpemilik Line Manager Legal. Draf pertama dokumen ini memberi Staff Legal sebagai pemilik, jadi diselaraskan, bukan dipertahankan. Tidak ada perbedaan yang dibiarkan. Tabel peran di bagian 5 tetap menyatakan Staff Legal mencatat dan menyiapkan, sehingga pembedaan "menetapkan" dan "mencatat" konsisten di bagian 4, 5, dan 11.

Uji sweep: render_sop.py lalu lint_doc.py sop memberi "pass": true, "fails": [], satu warn "20 butir (USULAN) menunggu ACC" (dua lebih banyak dari sebelumnya karena dua label pemetaan di 2a); validate.py (docx skill) "All validations PASSED!"; blankscan.py "ok 23 LEG-SOP-01.docx []".

