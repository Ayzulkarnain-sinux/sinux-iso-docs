# Catatan penyusun LEG-SOP-03: SOP Legal Document Control & Retention

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-SOP-03.json. Mode sop, aksi T2, wave W4, nomor SNX-LEG-SOP-03 (nomor SNX lama dipertahankan), department Legal, classification INTERNAL, audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Judul meta "Legal Document Control & Retention" (renderer menambah "SOP" di Document Title). Approval persis: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". process_owner "Departemen Legal" (lihat bagian 4).

Uji terakhir:
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-SOP-03.json /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx` sukses.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "42 butir (USULAN) menunggu ACC" (nol warn PIC SLA; angka sesudah sweep, semula 40).
- Validator OOXML (`python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx`): "All validations PASSED!".
- `bash tools/selftest.sh`: 6 baris OK (template sha, kontrol positif sop, kontrol positif generic, kontrol negatif, format terkunci, kontrol gaya dan dummy).
- Pratinjau PDF (soffice) 22 halaman, dilihat lewat contact sheet dan diagram dalam resolusi penuh: sampul, Identity, Revision, Approval, TOC, 11 bagian, diagram (13 simpul, rankdir TB, lima belah ketupat) tampil. Tabel Rekaman bagian 11 tinggi karena kolom tengah template sempit; format tidak diubah.
- Isi spec: 2 paragraf Purpose, 10 paragraf Scope, 18 istilah, 26 butir kebijakan (4.1 sampai 4.26), 4 peran, 8 prosedur (6.1 sampai 6.8) dengan 46 langkah, 6 baris SLA, 7 baris pengecualian, 12 dokumen terkait, 12 baris rekaman.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SOP Legal Document Control & Retention (Google Docs; sumber utama, dibuat 2026-10-14T09:13Z per catatan W0) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 | 2026-10-14T10:26:59.642Z (dari prompt; tidak diukur ulang di sesi ini) | read_file_content, teks utuh (9 bagian). Tidak ada catatan di context/audit untuk fileId ini (lihat bagian 5) |
| SOP Divisi Legal – SINUX.docx | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (dari prompt) | read_file_content, dibandingkan dengan transkripsi di context/audit/iso-sinux-supdocs-legal-2026-10-14.md baris 1048 sampai 1320 |
| SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io | 2026-10-13T06:09:00Z (dari prompt) | read_file_content, teks utuh |
| SINUX_Job_Analysis_2026.docx | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (dari prompt) | read_file_content, teks utuh |
| Kriteria penerimaan | config/checklist.json baris 38 (dept LEG, "SOP Legal Document Control & Retention.", checked false, link null, iso_9001 dan iso_27001 null) | checklist modifiedTime 2026-10-14T17:47:13.611Z | Kolom Description: "Prosedur standar untuk pengendalian dokumen legal, termasuk pengelolaan versi, penyimpanan, akses, dan masa retensi dokumen." |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, K-13), specs/LEG-SOP-01.json dan specs/LEG-SOP-02.json (istilah, butir yang menunjuk SOP ini), specs/ISMS-PRO-01.json, specs/ISMS-SOP-01/02/04.json, specs/FAT-SOP-01.json, notes/FAT-SOP-01.md, config/defaults.json v21, config/worklist.json | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah |

Isi docx tidak diunduh (download_file_content tidak dipakai); tracked change dan teks tersembunyi di document.xml tidak diuji (Open items 12).

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Cakupan pengendalian dokumen legal yang diminta tim: pengendalian, penyimpanan, akses, retensi, pemusnahan, dan hasil yang dijaga (tersedia, asli, rahasia, tidak diubah tanpa hak, tertelusur). Di dokumen menjadi Purpose dan butir 4.1 sampai 4.25 | "SOP ini bertujuan untuk menetapkan tata cara pengendalian, penyimpanan, pengaksesan, penggunaan, pemeliharaan, retensi, dan pemusnahan dokumen yang dikelola oleh Divisi Legal PT Strategi Integrasi Nusantara" dan "SOP ini dimaksudkan untuk memastikan bahwa dokumen Legal tersedia ketika diperlukan, terjaga keaslian dan kerahasiaannya, terlindungi dari akses atau perubahan yang tidak sah, serta dapat ditelusuri sepanjang siklus hidup dokumen." (2. Tujuan, butir 1 dan 2) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |
| 2 | Pembagian kewenangan: Line Manager Legal menetapkan klasifikasi dan akses, menyetujui pengarsipan atau pemusnahan, dan memastikan penanganan Legal Hold. Di dokumen menjadi butir 4.11, 4.13, 4.22, 4.23, 4.26 dan bagian 5 | "Mengawasi penerapan SOP, menetapkan klasifikasi dan akses sesuai kewenangan, menyetujui tindakan pengarsipan atau pemusnahan sesuai ketentuan internal, serta memastikan penanganan Legal Hold." (6. Tanggung Jawab, baris Line Manager Legal) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |
| 3 | Pengendalian versi, arsip, dan akses: pola nama berkas, pemisahan versi lama, unggah salinan final dalam 2 hari kerja, dokumen asli di tempat aman, akses menurut kebutuhan kerja dan klasifikasi. Di dokumen menjadi butir 4.4 sampai 4.10 dan 4.13, prosedur 6.2 sampai 6.4, dan SLA baris 1 | "Dokumen diberi nama secara konsisten, misalnya: “JenisDokumen_NamaPihak_Versi_Tanggal”." dan "Versi draft yang sudah tidak digunakan dipisahkan atau ditandai dengan jelas agar tidak tertukar dengan versi yang berlaku." dan "Dalam waktu paling lambat 2 (dua) hari kerja setelah kontrak ditandatangani lengkap oleh para pihak, Staff Legal mengunggah salinan final ke repositori resmi Perusahaan" dan "Akses terhadap kontrak diberikan berdasarkan kebutuhan kerja dan klasifikasi kerahasiaan dokumen." (7. Prosedur Pelaksanaan, bagian Negosiasi dan Pengendalian Versi, Pencatatan dan Pengarsipan) | 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 |

## 2. Fakta pendukung dan kutipan

Penanda markdown dan garis miring terbalik di keluaran alat dibuang. Semua kutipan verbatim dari fileId yang tertulis di kolom pertama. Singkatan kolom pertama: 12WUH... = 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0; 19pe... = 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb; 1h5P... = 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io; 1m91... = 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1. Bagian sumber utama dinomori menurut urutannya (1 Identitas sampai 9 Catatan Pemeriksaan dan Persetujuan), karena penomoran otomatis docx dimulai ulang di tiap judul.

| fileId | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 12WUH... | Tujuh kategori dokumen (bagian 2) | "Dokumen kontraktual, termasuk NDA, IaaS Contract, Technology Services Contract, Hardware Sale and Purchase Agreement, PKS, KSO, Subcontract, addendum, dan dokumen terkait lainnya." / "Dokumen korporasi, termasuk akta pendirian dan perubahan, keputusan atau persetujuan Menteri Hukum, bukti penerimaan pemberitahuan, keputusan RUPS, serta dokumen Direksi dan Dewan Komisaris." / "Dokumen perizinan dan kepatuhan, termasuk NIB, perizinan berusaha, sertifikat, persetujuan regulator, dan dokumen pendukung kepatuhan." / "Dokumen penelaahan Legal, termasuk legal opinion, legal memorandum, hasil uji tuntas (due diligence), hasil pemeriksaan kepatuhan, dan ringkasan risiko." / "Dokumen sengketa dan penanganan hukum, termasuk somasi, surat kuasa, dokumen perkara, korespondensi hukum, dan dokumen penyelesaian sengketa." / "Dokumen internal Divisi Legal, termasuk SOP, instruksi kerja, template kontrak, checklist, register, laporan, serta bukti persetujuan." / "Dokumen pelindungan data dan kerahasiaan, termasuk NDA, dokumen pemrosesan data pribadi, catatan insiden, dan dokumen terkait lainnya yang dikelola Divisi Legal." | Scope, Kategori 1 sampai 7 |
| 12WUH... | Pengguna dan bentuk dokumen | "SOP ini berlaku bagi Line Manager Legal, Staff Legal, dan pihak lain yang diberikan kewenangan untuk mengakses atau mengelola dokumen Legal Perusahaan." / "SOP ini berlaku untuk dokumen dalam bentuk fisik maupun elektronik, termasuk dokumen yang disimpan pada repositori digital resmi Perusahaan." | Scope |
| 12WUH... | Definisi Dokumen legal, Dokumen Final, Dokumen Terkendali, Masa retensi, Legal Hold, Dokumen Tidak Berlaku, Repositori resmi | "Dokumen yang dibuat, diterima, ditelaah, digunakan, atau disimpan oleh Divisi Legal sehubungan dengan kegiatan hukum, korporasi, perizinan, kontrak, kepatuhan, atau sengketa Perusahaan." / "Dokumen yang telah menyelesaikan proses pemeriksaan dan persetujuan yang dipersyaratkan serta, jika relevan, telah ditandatangani oleh para pihak atau pejabat berwenang." / "Dokumen yang identitas, versi, status, akses, dan perubahannya dikelola sesuai prosedur pengendalian dokumen." / "Jangka waktu penyimpanan dokumen sebelum dilakukan evaluasi untuk penyimpanan lebih lanjut, pemindahan ke arsip, atau pemusnahan sesuai ketentuan yang berlaku." / "Penangguhan pemusnahan atau penghapusan dokumen karena dokumen tersebut diperlukan untuk sengketa, pemeriksaan, audit, investigasi, permintaan regulator, atau proses hukum lainnya." / "Dokumen yang telah digantikan, dicabut, berakhir masa berlakunya, atau tidak lagi digunakan untuk tujuan operasional, tetapi mungkin tetap perlu disimpan sebagai rekaman historis atau bukti hukum." / "Lokasi penyimpanan dokumen fisik atau elektronik yang ditetapkan oleh Perusahaan sebagai tempat penyimpanan resmi dan terkendali." | Bagian 3, butir 4.19 sampai 4.23 |
| 12WUH... | Status kontrak yang belum lengkap | "Apabila kontrak belum ditandatangani lengkap, statusnya harus dicatat sebagai draft, menunggu tanda tangan, atau status lain yang sesuai. Dokumen tersebut tidak boleh dicatat sebagai kontrak final yang telah berlaku tanpa dasar yang memadai." | Butir 4.3, pengecualian baris 1 |
| 12WUH... | Dokumen asli | "Dokumen asli disimpan pada tempat yang aman dengan kontrol akses sesuai SOP Legal Document Control & Retention." | Butir 4.10 |
| 12WUH... | Pemantauan dan peninjauan | "Line Manager Legal bertanggung jawab memantau penerapan SOP ini." / "Pelaksanaan SOP dapat dievaluasi melalui register permintaan Legal, ketepatan waktu review, kelengkapan bukti persetujuan, dan hasil pemeriksaan dokumen." / "SOP ditinjau sekurang-kurangnya satu kali dalam setahun atau ketika terdapat perubahan regulasi, struktur organisasi, kewenangan persetujuan, proses bisnis, atau kebutuhan pengendalian internal." / "Usulan perubahan SOP disampaikan kepada pemilik dokumen untuk ditinjau dan disetujui sesuai mekanisme pengendalian dokumen Perusahaan." | Butir 4.25, prosedur 6.8, SLA baris 6 |
| 12WUH... | Dasar hukum | "Undang-Undang Nomor 8 Tahun 1997 tentang Dokumen Perusahaan." / "Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi." / "Ketentuan peraturan perundang-undangan lainnya yang relevan dengan jenis dokumen yang dikelola." | Prosedur 6.5 langkah 1, bagian 11 |
| 12WUH... | Identitas | "Pemilik Dokumen | Departemen Legal" dan "Klasifikasi | Internal" | meta process_owner, classification |
| 19pe... | Klasifikasi, repositori, akses, retensi | "Dokumen legal diklasifikasikan (Rahasia, Internal, Publik) dan disimpan pada repositori resmi [ISI]." / "Akses diberikan berdasarkan kebutuhan kerja dan dicabut saat peran berakhir." / "Dokumen rahasia tidak dikirim melalui kanal pribadi." / "Retensi dokumen mengikuti ketentuan peraturan perundang-undangan dan kebijakan perusahaan [ISI: periode retensi]." / "Dokumen asli disimpan di tempat yang aman dengan kontrol akses [ISI]." | Butir 4.10, 4.15, 4.17, 4.19 |
| 19pe... | Angka pelaporan, dipakai pada lingkupnya oleh SNX-LEG-SOP-01 | "Melaporkan kepada Legal paling lambat 1 hari kerja setiap somasi, klaim, surat regulator, atau perubahan fakta yang memengaruhi kontrak." | Tidak dipakai sebagai angka di sini; prosedur 6.6 menunjuk butir 4.14 SNX-LEG-SOP-01 |
| 1h5P... | Pemilik informasi menetapkan klasifikasi | "Pemilik informasi (pemilik aset pada SNX-ISMS-REG-01) menetapkan klasifikasi saat informasi dibuat atau diterima." | Butir 4.11 |
| 1h5P... | Pelabelan folder (tabel Pelabelan, baris Folder Drive) | "Nama folder atau deskripsi menyebut tingkat; izin akses sesuai tingkat" | Butir 4.9 |
| 1h5P... | Contoh tingkat | INTERNAL "SOP umum, jadwal shift, pengumuman internal, template"; RESTRICTED "Topologi dan konfigurasi pelanggan, register risiko, laporan insiden, kontrak, harga, data karyawan"; SECRET "Kredensial, private key dan sertifikat, token API, data pribadi sensitif, data pelanggan yang diatur regulator" | Butir 4.12 |
| 1h5P... | Berbagi ke pihak luar | RESTRICTED: "Butuh NDA atau kontrak yang berlaku dan persetujuan pemilik informasi" | Butir 4.18 |
| 1h5P... | Retensi dan pemusnahan per tingkat | Retensi INTERNAL "Sesuai master list", RESTRICTED "Sesuai master list dan kontrak"; Pemusnahan INTERNAL "Hapus biasa", RESTRICTED "Hapus aman; kertas dihancurkan", SECRET "Hapus aman dan rotasi; media dihancurkan atau di-wipe sesuai SNX-ISMS-SOP-04" | Butir 4.19, 4.23; metode tidak disalin, hanya dirujuk |
| 1h5P... | Pelaporan pelanggaran | "Pelanggaran penanganan informasi RESTRICTED atau SECRET dilaporkan sebagai event keamanan sesuai SNX-ISMS-SOP-01 dan ditindak sesuai kebijakan disipliner perusahaan." | Pengecualian baris 7 |
| 1m91... | Tugas JA-09 terkait arsip dan versi | "Memeriksa kelengkapan tanda tangan, lampiran dan arsip dokumen." / "Document version control" (Kompetensi Teknis JA-09, butir 5) / "Tidak memberi legal persetujuan final tanpa delegasi" | Bagian 5 baris Staff Legal, prosedur 6.2 langkah 5 |
| 1m91... | Tugas JA-08 terkait dokumentasi legal | "Mengelola dokumentasi legal, NDA, surat kuasa dan legal register." | Bagian 5 baris Line Manager Legal |
| 1m91... | Tanggung jawab kontrol keamanan, akses, backup | JA-04: "Memastikan kontrol keamanan, akses, backup dan perubahan sesuai kebijakan teknis." | Bagian 5 baris VP Tech Operation and Services (wewenang menurut SNX-HR-ORG-01) |

Dasar angka yang diambil dari dokumen lain di repo (bukan dari sumber Drive baris ini):

| Angka di dokumen | Dasar di repo | Kutipan |
|---|---|---|
| 10 tahun (Kategori 1, 3, 5) | notes/FAT-SOP-01.md bagian 2 baris 18 dan specs/FAT-SOP-01.json (rekaman "Invoice, e-Faktur Pajak, PKS, PO, dan BAST (PDF)") | "Seluruh arsip dokumen penagihan dan bukti perpajakan wajib disimpan selama minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001." Berlaku untuk arsip FAT, bukan arsip Legal; dipakai di sini sebagai satu-satunya angka retensi dokumen kontrak yang ada di SINUX, berlabel (USULAN) |
| 5 tahun (Kategori 7, berita acara pemusnahan) | specs/ISMS-SOP-04.json rekaman "Berita acara pemusnahan (sheet Pemusnahan, SNX-ISMS-REG-01)" 5 tahun; specs/ISMS-PRO-01.json rekaman SNX-ISMS-FRM-02 5 tahun | Angka dokumen Operation; berlabel (USULAN) |
| 3 tahun (Kategori 6 versi Tidak Berlaku, tiket akses, tinjauan akses, evaluasi SOP) dan "setiap semester" | specs/ISMS-SOP-02.json: "Tiket permintaan akses ... 3 tahun" dan "akses biasa setiap semester" | Angka dokumen Operation; berlabel (USULAN) |

## 3. Pemetaan klausul ISO (kriteria)

Checklist tidak memberi acuan klausul untuk baris ini (iso_9001 dan iso_27001 null). Klausul di bagian 11 dipilih dari isi dokumen dan berlabel satu kali "(USULAN, perlu konfirmasi konsultan)". SoA = konsultan.

| Klausul | Isi dokumen yang dirujuk |
|---|---|
| ISO 9001:2015 5.3 | Bagian 5 dan butir 4.26 (pembagian menetapkan, mencatat, menjalankan) |
| ISO 9001:2015 7.5.2 | Pencatatan, penamaan berkas, status: butir 4.1 sampai 4.7 |
| ISO 9001:2015 7.5.3 | Penyimpanan, akses, pengendalian versi, retensi, pemusnahan: butir 4.8 sampai 4.24 |
| ISO/IEC 27001:2022 Annex A 5.12 dan 5.13 | Butir 4.9, 4.11, 4.12 (klasifikasi dan pelabelan folder) |
| ISO/IEC 27001:2022 Annex A 5.14 | Butir 4.17 dan 4.18 (pengiriman dan pembagian) |
| ISO/IEC 27001:2022 Annex A 5.15 dan 5.18 | Butir 4.13 sampai 4.16 (akses, pencabutan, tinjauan) |
| ISO/IEC 27001:2022 Annex A 5.31 dan 5.34 | Butir 4.19 dan 4.20 (persyaratan hukum untuk retensi; data pribadi di Kategori 7) |
| ISO/IEC 27001:2022 Annex A 5.33 | Butir 4.1, 4.2, 4.21 (register dan evaluasi retensi) |
| ISO/IEC 27001:2022 Annex A 7.10 | Butir 4.10 (dokumen asli fisik) |
| ISO/IEC 27001:2022 Annex A 8.10 | Butir 4.23 dan 4.24 (pemusnahan dan berita acara) |

## 4. Keputusan data dan pemetaan peran

- Approval, status, revision, effective_date, review_period, revision_desc: persis dari prompt dan config/defaults.json v21. Sumber utama menulis blok "Disusun oleh / Diperiksa oleh / Disetujui oleh" kosong; defaults mengalahkan.
- process_owner "Departemen Legal": kutipan sumber utama "Pemilik Dokumen | Departemen Legal". Ini unit, bukan nama orang, dan sesuai aturan "ikuti Pemilik dokumen di sumber". SNX-LEG-SOP-01 dan SNX-LEG-SOP-02 memakai "Line Manager Legal" karena sumbernya (SOP Divisi Legal) menulis "Pemilik SOP: Line Manager Legal". Dua dokumen itu tetap benar terhadap sumbernya masing-masing; di SOP ini Line Manager Legal bertindak sebagai wakil pemilik untuk pemantauan, peninjauan, dan usulan perubahan (butir 4.25, prosedur 6.8). Bila owner ingin satu pemilik di ketiga SOP Legal: ganti ke "Line Manager Legal" (Open items 14).
- Nama orang dan jabatan: tidak ada nama orang di badan dokumen. "Direktur (COO)" dan "Direktur Utama" tidak muncul di badan (nol sebutan), jadi aturan sebutan pertama tidak terpakai. Samuel hanya di blok Approved By.
- Tiket: Legal = generalist, jadi GLPI (SINUX Service Hub). Zammad tidak dipakai. Batas "generalist" belum dirinci owner (defaults), maka kanal berlabel (USULAN).
- Vault dan PPN tidak relevan untuk SOP ini.
- Klasifikasi dokumen ini: INTERNAL (worklist). Klasifikasi dokumen legal yang diatur SOP: tingkat SNX-ISMS-PRO-01, bukan label Indonesia "Rahasia, Internal, Publik" di SOP Divisi Legal 4.7. Padanan istilah "dokumen rahasia" (sumber) ke RESTRICTED (Internal) dan SECRET ditulis di butir 4.17 berlabel (USULAN), sama dengan SNX-LEG-SOP-01 butir 4.23.
- Istilah satu per satu: "Departemen Legal" (sumber "Divisi Legal"), "Staff Legal" (sumber "Legal Staff"), "Pemohon" (istilah SNX-LEG-SOP-01; sumber tidak menyebut peminta akses), "Dokumen Tidak Berlaku" (sumber "Dokumen Kedaluwarsa atau Tidak Berlaku"; dua nama untuk satu hal disatukan), "Masa retensi" (sumber "Retensi Dokumen"), "Repositori resmi" (sumber "Repositori Resmi"), "register" (definisi: register dokumen legal), "Dokumen asli" dan "salinan Dokumen Final" konsisten.

Pemetaan peran sumber ke nama peran HR-ORG-01 (specs/HR-ORG-01.json: Daftar Jabatan dan Matriks Peran):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Line Manager Legal | Line Manager Legal | Matriks Peran HR-ORG-01: Legal & Compliance (JA-08), "(USULAN), menunggu konfirmasi (K-13)" |
| Legal Staff | Staff Legal | Matriks Peran HR-ORG-01: JA-09. Baris sumber kosong; tugas diambil dari uraian JA-09 (kutipan di bagian 2) |
| Pemilik Dokumen/PIC | Tidak dibawa sebagai peran | Baris sumber kosong dan istilahnya tidak didefinisikan. Fungsi yang masuk akal (menetapkan klasifikasi dan akses) sudah tertulis milik Line Manager Legal di baris pertama. Open items 2 |
| Unit IT/Keamanan Informasi | VP Tech Operation and Services | Jabatan terdekat: Matriks Peran HR-ORG-01 menaruh kontrol keamanan, akses, backup, dan perubahan teknis pada JA-04. Baris sumber kosong; satu-satunya tugas yang dibawa adalah wipe atau penghancuran media (SNX-ISMS-SOP-04), karena sumber tidak menyebut kontrol teknis lain. Pemetaan (USULAN) |
| Pihak Berwenang | Tidak dibawa sebagai peran | Baris sumber kosong. Tidak ada langkah yang butuh peran ini: persetujuan pemusnahan sudah milik Line Manager Legal menurut sumber. Open items 2 |
| (tidak ada di sumber) | Pemohon | Peran yang meminta akses ke dokumen legal; istilah dan definisi sama dengan SNX-LEG-SOP-01 |

## 5. Penanganan cacat sumber

Perintah: `grep -n 12WUHJcA3eWUjC_Ytg-_cr0RdAz3dI3b0f1n60yxazf0 context/audit/*.md` tanpa hasil (dokumen tim terbit sesudah ingest 13 sampai 14 Okt; README audit membenarkan "dokumen Legal yang terbit sesudah 14 Okt: baca sumbernya langsung"). Cacat sumber utama dicatat di bawah dari pembacaan langsung. `grep -n 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb context/audit/*.md` memberi baris 1055 (file legal) dan 88 (sintesis); `grep -n 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io` memberi baris 924, 1092 (isms) dan 67 (sintesis); `grep -n 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1` memberi baris 15 (hr) dan 78 (sintesis). Bagian 5 "Catatan kualitas dan celah" dibaca: legal baris 1296 sampai 1312, isms baris 1099 sampai 1109, hr baris 1232 sampai 1250.

Sumber utama (12WUH...), pembacaan langsung:

| # | Cacat | Penanganan |
|---|---|---|
| 1 | Bagian 7 "Prosedur Pelaksanaan" hampir seluruhnya salinan prosedur review kontrak (pengajuan permintaan penelaahan kontrak, target waktu NDA dan PKS, uji tuntas pihak lawan, matriks aspek review, klasifikasi risiko, persetujuan Legal, DoA, penandatanganan, pemantauan kontrak berjalan). Isinya milik SNX-LEG-SOP-02 dan SNX-LEG-SOP-01 | Tidak disalin. Hanya potongan yang mengendalikan dokumen dibawa: pola nama berkas, pemisahan versi lama, status kontrak yang belum lengkap, unggah salinan final dalam 2 hari kerja, kolom register, dokumen asli di tempat aman, akses menurut kebutuhan kerja. Pembatas scope ditulis di Scope. Open items 1 |
| 2 | Tabel Tanggung Jawab: empat dari lima baris kosong (Legal Staff, Pemilik Dokumen/PIC, Unit IT/Keamanan Informasi, Pihak Berwenang) | Dua dipetakan dan diisi dari uraian jabatan, dua tidak dibawa (bagian 4). Open items 2 |
| 3 | Tiga placeholder "[TBD]": kanal permintaan, repositori resmi, matriks DoA | Kanal dan DoA di luar kriteria baris ini (SNX-LEG-SOP-02). Repositori: folder Google Drive departemen Legal (USULAN), selaras SNX-LEG-SOP-01 butir 4.24. Tidak ada [TBD] tersisa di dokumen |
| 4 | Rujukan melingkar: "kontrol akses sesuai SOP Legal Document Control & Retention" menunjuk dokumen ini sendiri tanpa isi | Diisi: butir 4.9, 4.10, 4.13 sampai 4.17 dan prosedur 6.4 |
| 5 | Tidak ada masa retensi, tidak ada metode pemusnahan, tidak ada prosedur Legal Hold, tidak ada aturan versi untuk dokumen non-kontrak, padahal Tujuan dan definisi menyebutnya | Diisi sebagai USULAN: tabel Rekaman, prosedur 6.5 sampai 6.7, butir 4.4 sampai 4.7. Metode pemusnahan hanya dirujuk ke SNX-ISMS-PRO-01 |
| 6 | NDA muncul di dua kategori (kontraktual dan pelindungan data) | NDA di Kategori 1 saja; Kategori 7 memuat dokumen pemrosesan data pribadi dan catatan insiden |
| 7 | Contoh nama berkas memuat nama pihak lain ("Arkana") | Diganti NamaPihak (sama dengan SNX-LEG-SOP-02 butir 4.15) |
| 8 | Ukuran evaluasi SOP di bagian 8 sumber menyebut "register permintaan Legal" dan "ketepatan waktu review" (ukuran review kontrak) | Diadaptasi ke register dokumen legal dan ketepatan waktu pengarsipan; berlabel (USULAN) di prosedur 6.8 langkah 1 |
| 9 | Penanda format literal di judul docx (tanda bintang) dan identitas kosong (nomor, disusun, diperiksa, disetujui, tanggal, tanda tangan) | Tidak dibawa; identitas dari defaults dan prompt, tanda tangan dan tanggal kosong |
| 10 | Sebutan "Perusahaan" dan "Divisi Legal" | "SINUX" dan "Departemen Legal" |

SOP Divisi Legal (19pe..., audit legal bagian 5):

| # audit | Cacat | Penanganan di SOP ini |
|---|---|---|
| 2, 7 | Placeholder repositori resmi, kontrol akses dokumen asli, dan periode retensi belum diisi | Repositori (butir 4.8), dokumen asli (butir 4.10), periode retensi (tabel Rekaman), semuanya USULAN |
| 9 | Tanpa acuan klausul ISO dan tanpa klasifikasi dokumen untuk SOP itu sendiri | Bagian 11 Acuan standar (berlabel); klasifikasi INTERNAL |
| 12 | Label klasifikasi Indonesia berbeda dari skema SNX-ISMS-PRO-01 dan SOP tidak merujuk PRO-01 | Butir 4.9, 4.11, 4.12, 4.17 memakai tingkat PRO-01; SNX-ISMS-PRO-01 masuk bagian 11 |
| 1, 4, 11 | Status v0.1 tanpa nomor, atasan Line Manager Legal tidak seragam, "Staff Legal (Senior/Junior)" | Nomor SNX-LEG-SOP-03, Rev. 00, Draft; atasan tidak dibahas (tidak perlu di SOP ini); level Senior/Junior tidak dipakai |
| 3, 5, 6, 8, 10 | Rujukan alur 5.2 dan 5.3, target waktu, lampiran belum disusun, konflik opini versus hentikan proses, rujukan peraturan | Bukan lingkup SOP ini (ditangani di SNX-LEG-SOP-01 dan 02); rujukan UU 8/1997 dan 27/2022 ditulis seperti sumber, tidak diverifikasi (Open items 8) |

SNX-ISMS-PRO-01 (1h5P..., audit isms bagian 5):

| Cacat | Penanganan |
|---|---|
| Ruang lingkup PRO-01 hanya "personel Divisi Operation dan pihak ketiga"; Legal tidak disebut | SOP ini menerapkan tingkat dan aturan PRO-01 ke dokumen legal, mengikuti SNX-LEG-SOP-01 dan 02. Open items 9 |
| Retensi INTERNAL dan RESTRICTED merujuk "master list" tanpa nomor | Tabel Rekaman memuat periode sendiri (USULAN); hubungan dengan master list perusahaan jadi open item 9 |
| Rujukan SNX-ISMS-SOP-04 untuk pemusnahan SECRET konsisten | Dipakai di langkah 6.7 langkah 5 dan butir 4.24 |
| Dua penamaan peran penyusun ("ISMS Coordinator", "ISO/ISMS Coordinator") dan tanda tangan kosong | Tidak relevan; peran ISMS Coordinator tidak dipakai di dokumen ini (HR-ORG-01 K-13 menyatakan belum ditetapkan) |

SINUX_Job_Analysis_2026 (1m91..., audit hr bagian 5):

| # audit | Cacat | Penanganan |
|---|---|---|
| 9 | JA-08 dan JA-09 berjudul sama "Legal & Compliance"; pemetaan ke Line Manager dan Staff tidak dinyatakan | Mengikuti HR-ORG-01 (JA-08 = Line Manager Legal, JA-09 = Staff Legal, K-13); label (USULAN) di bagian 5 |
| 4 | Frasa kompetensi janggal ("Legal kepatuhan register" di JA-08 C.3, "pengendalian dokumen" huruf kecil) | Tidak dikutip; hanya butir tugas A yang dipakai |
| 7, 11 | Atasan JA-08 "Management / Direktur"; ejaan "Kristianto" dan sebutan CEO | Tidak muncul di badan dokumen; blok Approved By memakai ejaan defaults "Samuel Kristanto Utomo" |
| 1 | Status DRAF dan revision "03 -" | Hanya sebagai sumber uraian tugas; tidak dikutip sebagai fakta berlaku |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

- Pelaku langkah yang di sumber pasif (mencatat, mengunggah, memisahkan versi, memberi akses, mencabut akses) ditetapkan dari pembagian "menetapkan" (Line Manager Legal) dan "mencatat dan menjalankan" (Staff Legal), dengan dasar uraian JA-08 dan JA-09. Butir 4.26 menyatakan ini berstatus (USULAN), termasuk pemilik rekaman.
- Line Manager Legal "menyetujui tindakan pengarsipan atau pemusnahan" (sumber) dibaca sebagai keputusan evaluasi masa retensi di prosedur 6.5 langkah 5; persetujuan pemusnahan tidak diminta dua kali. Pemusnahan (6.7) mulai dari daftar yang sudah diputus.
- "pemindahan ke arsip" (definisi Masa retensi di sumber) dibaca sebagai subfolder Arsip di folder Google Drive departemen Legal (definisi Arsip, USULAN), karena sumber tidak menyebut lokasi arsip.
- Dokumen bertanda Legal Hold keluar dari daftar evaluasi dan pemusnahan (prosedur 6.6 langkah 3). Sumber hanya mendefinisikan Legal Hold dan menyebut Line Manager Legal memastikan penanganannya; langkah menetapkan dan mencabut adalah USULAN.
- Status Final, Tidak Berlaku diambil dari definisi sumber, Draft dan Menunggu Tanda Tangan dari kalimat status kontrak sumber, Dimusnahkan dari SNX-ISMS-SOP-04 (USULAN).
- Tingkat dasar klasifikasi (butir 4.12) memakai contoh PRO-01: kontrak dan data karyawan di RESTRICTED, SOP umum dan template di INTERNAL, data pribadi sensitif di SECRET. Penerapan ke kategori Legal adalah USULAN; SNX-LEG-SOP-02 butir 4.17 menyatakan tingkat tiap jenis kontrak belum ditetapkan.
- Angka 2 hari kerja dipakai pada lingkup sumber (kontrak yang ditandatangani lengkap). Perluasan ke Kategori 2 sampai 7 diberi label (USULAN). Pemeriksaan register tiap bulan memperluas tinjauan register kontrak bulanan sumber; berlabel (USULAN). Angka 90, 60, 30 hari dan 1 hari kerja somasi tidak dipakai (milik SNX-LEG-SOP-01 dan 02).
- Ketika peraturan, kontrak, dan kebijakan SINUX berbeda, berlaku periode terpanjang: tafsir penyusun (USULAN). "Kontrak" sebagai dasar retensi berasal dari PRO-01 ("Sesuai master list dan kontrak"), bukan dari sumber utama.
- Kategori 4 (penelaahan Legal) mengikuti masa simpan dokumen yang ditelaah supaya tidak menambah angka baru.
- Pemusnahan memakai metode per tingkat di PRO-01 tanpa menyalin tabelnya, supaya satu fakta hanya di satu dokumen. Wipe media oleh VP Tech Operation and Services mengikuti pemetaan di bagian 4 (di SNX-ISMS-SOP-04 pelakunya NOC Engineer).
- "penggunaan" dan "pemeliharaan" di Tujuan sumber tidak jadi unsur terpisah: pemeliharaan dibaca sebagai pengelolaan versi dan status; penggunaan dicakup akses.
- Diagram bagian 7 memuat satu alur umur dokumen (pencatatan, versi, akses, retensi, Legal Hold, pemusnahan) dalam 13 simpul; langkah rinci ada di 6.1 sampai 6.7.

## USULAN

Lint menghitung 42 kemunculan "(USULAN)" di dokumen, termasuk baris definisi label, baris tabel Rekaman, dan label klausul. Jumlah butir keputusan: 24 (butir 24 ditambah saat sweep).

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Kanal permintaan akses = tiket GLPI, permintaan wipe media lewat GLPI, dan batas pemakaian GLPI untuk departemen selain Operation (definisi GLPI) | Definisi GLPI; butir 4.14; prosedur 6.4 langkah 1; 6.7 langkah 4 | owner (batas "generalist" belum dirinci) |
| 2 | Repositori resmi = folder Google Drive departemen Legal; Arsip = subfolder Arsip di folder itu | Butir 4.8; definisi Arsip; butir 4.21 | Legal |
| 3 | Register dokumen legal dipadankan dengan SNX-LEG-REG-04, dengan tiga kolom retensi (tanggal pemicu, tanggal akhir masa retensi, penanda Legal Hold) | Butir 4.2 | Legal |
| 4 | Bagian NamaPihak diisi SINUX untuk dokumen tanpa pihak lawan; dokumen internal bernomor SNX dinamai dengan nomor dan judul | Butir 4.4 | Legal |
| 5 | Nomor versi berikutnya untuk tiap perubahan tanpa menimpa berkas; Dokumen Final hanya diubah lewat versi baru atau addendum | Butir 4.5 dan 4.7; 6.2 langkah 1 dan 7 | Legal |
| 6 | Dokumen asli di tempat aman, akses terbatas pada Line Manager Legal dan Staff Legal | Butir 4.10; tabel Rekaman | Legal (selaras SNX-LEG-SOP-01 butir 4.25) |
| 7 | Line Manager Legal sebagai pemilik informasi untuk dokumen legal; tingkat dasar klasifikasi tiap jenis dokumen; Line Manager Legal menyetujui pembagian RESTRICTED (Internal) ke pihak luar | Butir 4.11, 4.12, 4.18; 6.4 langkah 7 | Fani (pemilik skema SNX-ISMS-PRO-01 di sisi Operation dan ISMS), bersama Legal |
| 8 | Tinjauan daftar akses folder Legal setiap semester, mengikuti irama review akses biasa di SNX-ISMS-SOP-02 | Butir 4.16; 6.4 langkah 5; SLA baris 4 | Legal, dikonfirmasi Fani |
| 9 | Bila peraturan, kontrak, dan kebijakan SINUX menetapkan periode berbeda, berlaku yang terpanjang | Butir 4.19; pengecualian baris 4 | Legal |
| 10 | Masa retensi 10 tahun untuk Kategori 1 (sejak kontrak berakhir atau diakhiri), Kategori 3 (sejak izin atau persetujuan berakhir, dicabut, atau digantikan), Kategori 5 (sejak sengketa selesai, tidak dimusnahkan selama Legal Hold) | Tabel Rekaman bagian 11 | Legal dan FAT (irisan dengan arsip PKS 10 tahun di SNX-FAT-SOP-01), dikukuhkan Samuel |
| 11 | Kategori 2 disimpan selama SINUX berdiri; Kategori 4 mengikuti masa simpan dokumen yang ditelaah | Tabel Rekaman | Legal, dikukuhkan Samuel |
| 12 | Kategori 6 versi Tidak Berlaku 3 tahun sejak digantikan; Kategori 7 5 tahun sejak pemrosesan berakhir atau insiden ditutup | Tabel Rekaman | Legal |
| 13 | Retensi rekaman proses: register sampai digantikan (baris dokumen yang dimusnahkan tetap disimpan), tiket permintaan akses 3 tahun, hasil tinjauan akses 3 tahun, daftar dan berita acara pemusnahan 5 tahun, catatan evaluasi SOP 3 tahun | Tabel Rekaman | Legal |
| 14 | Line Manager Legal menetapkan dan mencabut Legal Hold (sumber hanya: memastikan penanganan Legal Hold) | Butir 4.22; prosedur 6.6 | Legal |
| 15 | Berita acara pemusnahan memuat ID register, metode, tanggal, pelaksana, persetujuan; format mengikuti SNX-ISMS-SOP-04; status Dimusnahkan | Butir 4.3, 4.24; 6.7 langkah 6 dan 7 | Legal, dikonfirmasi Fani |
| 16 | Unit IT/Keamanan Informasi dipetakan ke VP Tech Operation and Services, pelaku wipe atau penghancuran media | Bagian 5; 6.7 langkah 5 | Fani |
| 17 | Batas 2 hari kerja unggah salinan Dokumen Final diperluas ke Kategori 2 sampai 7 | SLA baris 2 | Legal |
| 18 | Pemeriksaan register untuk dokumen yang masa retensinya berakhir, setiap bulan | 6.5 langkah 3; SLA baris 3 | Legal |
| 19 | Pelapor pelanggaran penanganan dokumen RESTRICTED (Internal) atau SECRET = Staff Legal atau Line Manager Legal yang menemukannya | Pengecualian baris 7 | Fani (pemilik SNX-ISMS-SOP-01), bersama Legal |
| 20 | Pelaku langkah dan pemilik rekaman ditetapkan dari pembagian peran dan SNX-HR-JA-01 | Butir 4.26; tabel Rekaman | Legal |
| 21 | Ukuran evaluasi pelaksanaan SOP diadaptasi dari ukuran review kontrak: register dokumen legal dan ketepatan waktu pengarsipan | 6.8 langkah 1 | Legal |
| 22 | Pemetaan Line Manager Legal dan Staff Legal ke JA-08 dan JA-09 (K-13) | Bagian 5 | owner atau Aziz (K-13 HR-ORG-01) |
| 23 | Daftar klausul ISO 9001:2015 dan ISO/IEC 27001:2022 di bagian 11 | Acuan standar | konsultan |
| 24 | Padanan istilah "dokumen rahasia" (sumber: "Dokumen rahasia tidak dikirim melalui kanal pribadi.") dengan RESTRICTED (Internal) dan SECRET | Butir 4.17 | Fani (pemilik skema SNX-ISMS-PRO-01), bersama Legal |

## Open items

| # | Open item | Pemutus |
|---|---|---|
| 1 | Sumber utama memuat prosedur review kontrak di bagian prosedurnya. Konfirmasi bahwa isi itu memang milik SNX-LEG-SOP-02 dan SNX-LEG-SOP-01 dan tidak perlu diulang di SOP ini | Legal |
| 2 | Tabel Tanggung Jawab sumber kosong untuk Legal Staff, Pemilik Dokumen/PIC, Unit IT/Keamanan Informasi, dan Pihak Berwenang. Pemilik Dokumen/PIC dan Pihak Berwenang tidak dibawa sebagai peran. Konfirmasi tugasnya bila memang ada | Legal |
| 3 | Lokasi fisik "tempat aman" untuk dokumen asli belum ditetapkan (butir 4.10); kontrol aksesnya hanya "terbatas pada Line Manager Legal dan Staff Legal" (USULAN) | Legal |
| 4 | Pemicu pencabutan akses saat peran penerima akses berakhir: sumber tidak menyebut siapa memberi tahu Line Manager Legal. SNX-ISMS-SOP-02 memakai "HR atau atasan langsung" untuk sistem Operation; belum ada padanan untuk folder Legal | Legal dan Aziz |
| 5 | Pelaksana wipe atau penghancuran media: SNX-ISMS-SOP-04 memakai NOC Engineer, yang di SNX-HR-ORG-01 masih USULAN tanpa pemegang. Dokumen ini memetakan ke VP Tech Operation and Services. Apakah backup folder Google Drive Legal masuk SNX-ISMS-SOP-03 juga belum diketahui | Fani |
| 6 | Persetujuan pemusnahan: sumber Legal hanya menyebut Line Manager Legal; pemusnahan arsip penagihan di sumber FAT perlu Finance Lead dan CEO (notes/FAT-SOP-01.md baris 50). Apakah pemusnahan dokumen legal, khususnya Kategori 1 sampai 3, perlu persetujuan Direktur Utama | owner atau Samuel |
| 7 | Satu angka seragam 10 tahun diambil dari konvensi FAT, bukan dari ketentuan hukum. Periode Kategori 7 (5 tahun) berpotensi bertabrakan dengan kewajiban penghapusan data pribadi di UU Nomor 27 Tahun 2022; belum diperiksa | Legal |
| 8 | UU Nomor 8 Tahun 1997 dan UU Nomor 27 Tahun 2022 ditulis seperti sumber utama dan tidak diverifikasi terhadap teks undang-undang. Periksa juga peraturan sektor untuk perizinan (Kategori 3) | Legal |
| 9 | Ruang lingkup SNX-ISMS-PRO-01 hanya Divisi Operation (audit isms bagian 5), dan baris Retensi PRO-01 merujuk "master list" tanpa nomor. Konfirmasi penerapan tingkat PRO-01 ke dokumen Legal, dan hubungan tabel Rekaman dengan master list perusahaan. Sintesis audit 14 Okt juga mengusulkan satu prosedur kendali dokumen dan rekaman beserta master list tingkat perusahaan; bila terbit, periksa tumpang tindih dengan SOP ini | Fani dan owner |
| 10 | SNX-LEG-REG-04 (baris 39, W7) disusun kemudian; kolomnya harus selaras dengan butir 4.2 SOP ini (ID register, kategori, judul, pihak, nomor versi, status, tingkat klasifikasi, lokasi simpan, tanggal berlaku, tanggal berakhir, tanggal pemicu, tanggal akhir masa retensi, penanda Legal Hold) | orkestrator dan Legal |
| 11 | SNX-FAT-SOP-04 (W4) disusun paralel dan dirujuk sebagai batas scope. Periksa pembagian dokumen yang memuat keduanya, misalnya PKS yang menjadi dasar invoice (salinan di arsip FAT 10 tahun) | orkestrator |
| 12 | Tracked change dan teks tersembunyi di docx sumber tidak diuji; download_file_content tidak dipakai. Checklist baris 38 tidak punya tautan ke sumber utama (link null) | orkestrator atau owner |
| 13 | Nama peran Line Manager Legal dan Staff Legal menunggu K-13 di SNX-HR-ORG-01; bila nama peran berubah, render ulang | owner atau Aziz |
| 14 | process_owner "Departemen Legal" mengikuti sumber, sedangkan SNX-LEG-SOP-01 dan 02 memakai "Line Manager Legal". Pilih satu bentuk untuk ketiga SOP Legal bila diinginkan | owner |
| 15 | Hal yang tidak diatur karena sumber diam: dokumen asli hilang atau rusak, salinan dokumen legal di departemen lain saat Legal Hold, lokasi bukti penandatanganan elektronik (SNX-LEG-SOP-02 menyebut menyimpannya) | Legal |
| 16 | Kalimat perintah di sumber yang ditujukan ke pembaca otomatis: nihil | tidak ada |

## Jawaban dua pertanyaan penutup (lalu teks diperbaiki)

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

- Pola kalimat berulang "Staff Legal ... Line Manager Legal ... " dan kolom Output yang seragam ("Baris register terbarui", "Akses dicabut"). Ini wajar untuk SOP berlangkah, tetapi saya buang langkah yang hanya menghasilkan kata umum: langkah VP Tech Operation and Services "Jaga kontrol keamanan teknis folder" dengan output "Kontrol teknis folder terjaga" (tanpa sumber, tanpa rekaman) dihapus.
- Daftar paralel yang rapi: empat hasil di Purpose ("tersedia, terjaga keaslian dan kerahasiaannya, terlindungi, dapat ditelusuri"), tiga dasar retensi, lima status. Keempat hasil di Purpose berasal dari kalimat tim dan dipertahankan karena sudah jelas (aksi baris ini T2, tetapi kalimat tim yang jelas tidak diganti hanya agar terdengar rapi); daftar tiga dasar retensi dan lima status juga berasal dari sumber atau PRO-01, bukan tambahan.
- Pengulangan isi antarbagian: kalimat penutup Conclusion semula mengulang "sekurang-kurangnya satu kali setahun" dari SLA; diganti rujukan "dalam batas waktu di bagian 8". Butir 4.26 semula menyalin isi tabel peran; dipangkas menjadi pembagian tiga pelaku. Label "(USULAN)" pada pemilik rekaman yang semula diulang di 12 baris tabel Rekaman dipindah ke butir 4.26 dan baris tabel merujuk butir itu.
- Kalimat otoritas semu atau penegasan: "mutlak" di sumber ("kewajiban mutlak" untuk kerahasiaan) tidak dibawa; tidak ada "tanpa terkecuali", "pada intinya", "yang terpenting", "dalam rangka", "adapun". Pengecekan pola dilakukan dengan pencarian atas teks spec; hasil nol kecuali kata "penyusunan" yang kemudian diganti "pembuatan" agar tidak tertembak pola meta.
- Sisa yang masih terdengar seragam: tabel Rekaman, karena kolom tengah berisi lokasi yang sama untuk hampir semua baris. Itu informasi, bukan hiasan.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka 2 hari kerja (kontrak): sumber utama. Angka 2 hari kerja untuk Kategori 2 sampai 7, "setiap bulan" (register), "setiap semester" (akses): berlabel (USULAN), dasar di bagian 2.
- Angka retensi 10, 5, 3 tahun dan "selama SINUX berdiri": tidak ada di sumber Legal; seluruhnya berlabel (USULAN), dasar konvensi di repo dicatat di bagian 2, dan Open items 7 menyatakan bahwa angka itu bukan dari ketentuan hukum.
- Nomor dan nama: "v02" dan "20261014" hanya di contoh nama berkas (dari sumber, nama pihaknya diganti NamaPihak). Kode SNX dari repo (semua tercantum di tabel Dokumen terkait). JA-04, JA-08, JA-09, K-13 dari specs/HR-ORG-01.json. Nol nama orang di badan dokumen. Nol tanggal selain contoh nama berkas.
- Sistem: Google Drive, GLPI (SINUX Service Hub) dari defaults dan SNX-LEG-SOP-01; penggunaannya untuk dokumen ini berlabel (USULAN).
- Klausul ISO dan Annex A: dari pengetahuan standar, bukan dari sumber; satu label "(USULAN, perlu konfirmasi konsultan)".
- Fakta yang saya tambahkan lalu beri label setelah pemeriksaan ini: status Dimusnahkan (butir 4.3, semula tanpa label), ukuran evaluasi di prosedur 6.8 langkah 1 (semula tanpa label), permintaan wipe lewat GLPI (6.7 langkah 4).

## Sweep

Putaran sweep 15 Okt 2026, instruksi /tmp/claude-0/prompts/LEG-SOP-03.sweep.txt. Dua butir, empat perubahan teks di spec dan satu di notes. Fakta, angka, nama, dan struktur lain tidak diubah. Temuan pemeriksa dibaca dari qa/LEG-SOP-03.verify.json (verdict PASS, tidak ada blocking); temuan nonblocking lain di berkas itu di luar dua butir sweep dan tidak disentuh.

| Butir | Lokasi | Sebelum | Sesudah |
|---|---|---|---|
| 1a | Definisi GLPI | "Sistem tiket SINUX Service Hub yang dipakai departemen selain Operation." | "Sistem tiket SINUX Service Hub yang dipakai departemen selain Operation (USULAN)." Dasar: config/defaults.json "ticketing" menyatakan batas "generalist" belum dirinci owner; USULAN baris 1 |
| 1b | Butir 4.17 | "Dokumen RESTRICTED (Internal) dan SECRET tidak dikirim lewat kanal pribadi. Pengiriman dan pencetakan dokumen legal mengikuti aturan per tingkat di SNX-ISMS-PRO-01." | Disisipi "Padanan istilah dokumen rahasia dengan kedua tingkat ini berstatus (USULAN)." sebelum kalimat Pengiriman. Kalimat ini sejajar dengan SNX-LEG-SOP-01 butir 4.23; USULAN baris 24. Sumber 19pe memakai "Dokumen rahasia tidak dikirim melalui kanal pribadi." |
| 2a | Bagian 5, baris Line Manager Legal dan Staff Legal | "Dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." dan idem untuk JA-09 | "Peran ini dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01, menunggu konfirmasi (K-13) (USULAN)." dan idem untuk JA-09. Rumusan sama dengan SNX-LEG-SOP-02; kedua nama ditulis sebagai nama peran |
| 2b | Bagian 11, baris SNX-HR-ORG-01 | "Line Manager Legal dan Staff Legal dipetakan ke JA-08 dan JA-09, menunggu konfirmasi (K-13)." | "Peran Line Manager Legal dan Staff Legal dipetakan ke jabatan Legal & Compliance (JA-08 dan JA-09) (USULAN, butir K-13)." Rumusan sama dengan SNX-LEG-SOP-01 dan 02 |
| 2c | Pemilik rekaman Legal | Tabel Rekaman: "pemilik Line Manager Legal" di seluruh baris; butir 4.26: Line Manager Legal pemilik rekaman, Staff Legal pencatat (USULAN) | Tidak diubah. Dokumen ini adalah SNX-LEG-SOP-03 sehingga menjadi acuan. Pembandingan: specs/LEG-SOP-01.json (pemilik Line Manager Legal di 9 baris rekaman) dan specs/LEG-SOP-02.json (pencatat Staff Legal, pemilik Line Manager Legal) sudah sama, jadi tidak ada selisih untuk diselaraskan |

Catatan: process_owner "Departemen Legal" (unit, sesuai sumber) berbeda dari "Line Manager Legal" di SNX-LEG-SOP-01 dan 02. Itu pemilik dokumen, bukan pemilik rekaman, dan di luar dua butir sweep; tetap dicatat di Open items 14.

Uji sesudah sweep (semua dari /home/claude/iso-run, keluaran ke /tmp/pen-LEG-SOP-03/):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-SOP-03.json /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx` sukses.
- `python3 -I tools/lint_doc.py /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx sop`: `"pass": true`, `"fails": []`, warn "42 butir (USULAN) menunggu ACC".
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx`: "All validations PASSED!".
- `python3 -I reports/orch/blankscan.py /tmp/pen-LEG-SOP-03/LEG-SOP-03.docx`: `ok	22	LEG-SOP-03.docx	[]`.
