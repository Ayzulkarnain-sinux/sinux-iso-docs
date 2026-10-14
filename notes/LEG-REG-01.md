# Catatan penyusun LEG-REG-01: Company Licenses & Permits Register

Status: DRAFTED (spec + notes ada). Spec: specs/LEG-REG-01.json. Mode generic, aksi T1, wave W6, nomor SNX-LEG-REG-01 (nomor SNX dipertahankan), department Legal, klasifikasi RESTRICTED (Internal), audit_class B, doc_type_cover "REGISTER". Approval persis data baris: prepared "Staff Legal", reviewed "Line Manager Legal", approved "Samuel Kristanto Utomo / President Director". Status Draft, revision 00, effective_date kosong, review_period YEARLY. Process owner "Line Manager Legal" (sumber tidak punya baris "Pemilik dokumen"; lihat Asumsi 1 dan USULAN 2).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Company Licenses and Permits Register (Google Doc, 7059 byte) | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk | 2026-10-13T10:52:13.121Z (get_file_metadata di sesi ini; cocok dengan prompt) | read_file_content, dua kali (tanpa dan dengan includeComments); isi sama, tidak ada komentar di berkas. Tabel dan butir dibandingkan dengan transkripsi context/audit: sama |
| Kriteria penerimaan | config/checklist.json baris 40 | tidak diukur ulang | Description: "Dokumen berisikan daftar perizinan perusahaan yang mencakup jenis izin, nomor, masa berlaku, dan jadwal perpanjangan. (NIB, KBLI, Akta Pendirian, NPWP, Anggaran Dasar)". Kolom iso_9001 dan iso_27001 baris ini null |
| Pendukung: SOP Divisi Legal - SINUX.docx | 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb | 2026-10-13T10:54:39.480Z (dari notes/LEG-SOP-01.md; tidak diukur ulang di sesi ini) | read_file_content (teks utuh dibaca di sesi ini); dipakai untuk angka 90 hari pengingat perpanjangan izin dan peran verifikasi akta |
| Pendukung: Jobdesk Staff Legal - SINUX.docx | 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW | 2026-10-13T10:54:34.881Z (get_file_metadata di sesi ini) | contentSnippet get_file_metadata (teks utuh jobdesk); dipakai untuk rutinitas bulanan dan pemeliharaan register perizinan |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, K-03, K-13), specs/HR-JA-01.json (JA-09 rutinitas bulanan), specs/LEG-SOP-01.json (butir 4.24, prosedur 6.5 dan 6.6, bagian 8), config/defaults.json v21, config/worklist.json (kode REG-03, REG-04, SOP-03) | repo kerja | Kutipan dari dokumen lain bisa basi bila dokumen itu berubah |
| Catatan cacat | context/audit/iso-sinux-supdocs-legal-2026-10-14.md, bagian 001-LEGAL-SINUX-X-2026 (baris 8 sampai 160, bagian 5 baris 149 sampai 158) | salinan audit 13 Okt 2026 | DATA; dibandingkan dengan teks Drive terbaru |

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tabel register sumber kosong: tiga baris bernomor tanpa isi, dan tidak punya kolom jadwal perpanjangan, sehingga kolom itu ditambahkan sesuai kriteria (USULAN 4) | "No. \| Nama Dokumen \| Nomor Dokumen \| Instansi Penerbit \| Kegiatan Usaha/KBLI \| Tanggal Penerbitan \| Masa Berlaku \| Status \| Penanggung Jawab" lalu baris "1 \|   \|   \|   \|   \|   \|   \|   \|   \|", "2 ...", "3 ..." | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |
| Dokumen bermasa berlaku dipantau lewat tanggal kedaluwarsa dan ketentuan perpanjangan | "Dokumen yang memiliki masa berlaku dipantau berdasarkan tanggal kedaluwarsa serta ketentuan perpanjangan yang berlaku." (Pemantauan dan Tindak Lanjut, butir 2) | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |
| Pencantuman jenis dokumen tidak berarti wajib; kewajiban diverifikasi | "Pencantuman suatu jenis dokumen dalam daftar ini tidak dengan sendirinya menyatakan bahwa dokumen tersebut diwajibkan bagi perusahaan. Kewajiban masing-masing dokumen harus diverifikasi berdasarkan kondisi dan kegiatan usaha perusahaan." (Ruang Lingkup) | 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk |

## 2. Fakta pendukung dan kutipan

Kutipan sumber utama dari fileId 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk; penanda markdown dan garis miring terbalik di keluaran alat dibuang.

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Fungsi register | "Dokumen ini disusun sebagai sarana pencatatan, pemantauan, dan pengendalian atas perizinan, persetujuan, pendaftaran, serta dokumen legalitas lain yang dimiliki atau wajib dipenuhi oleh perusahaan sesuai dengan kegiatan usahanya dan ketentuan peraturan perundang-undangan yang berlaku." (Tujuan 1) | Tujuan |
| 2 | Hasil yang dijaga | "memastikan bahwa informasi mengenai legalitas perusahaan tercatat secara akurat, dapat ditelusuri, dan diperbaharui apabila terdapat perubahan yang relevan." (Tujuan 2) | Tujuan |
| 3 | Isi lingkup | "Akta pendirian dan akta perubahan perusahaan;", "Surat keputusan atau surat penerimaan pemberitahuan dari instansi yang berwenang;", "Nomor Induk Berusaha (NIB);", "Perizinan berusaha dan sertifikat standar melalui sistem OSS berbasis risiko, apabila dipersyaratkan;", "Nomor Pokok Wajib Pajak (NPWP) perusahaan;", "Perizinan, persetujuan, atau pendaftaran sektoral yang relevan; dan", "Dokumen legalitas lain yang diwajibkan berdasarkan kegiatan usaha, ketentuan hukum, atau persyaratan kontraktual yang berlaku." (Ruang Lingkup, "termasuk namun tidak terbatas pada") | Lingkup; baris 3 sampai 9 tabel Isi Register |
| 4 | Peran Departemen Legal | "Mengelola dan memperbarui daftar induk perizinan dan legalitas perusahaan." / "Memeriksa kelengkapan serta keakuratan informasi dokumen." / "Memantau masa berlaku dan kebutuhan pembaruan dokumen." / "Mengidentifikasi kekurangan dokumen dan mengkoordinasikan tindak lanjut yang diperlukan." / "Menyimpan atau mencatat lokasi penyimpanan bukti pendukung." (Tanggung Jawab, Departemen Legal dan Compliance 1 sampai 5) | Ketentuan 1, 2, 5, 6, 7; Peran |
| 5 | Peran Unit Kerja Terkait | "Menyampaikan dokumen dan informasi yang diperlukan kepada Departemen Legal." / "Menginformasikan perubahan kegiatan usaha atau kondisi perusahaan yang dapat mempengaruhi kewajiban perizinan." (Tanggung Jawab, Unit Kerja Terkait) | Ketentuan 3; Peran |
| 6 | Pejabat yang Berwenang | "Melakukan pemeriksaan atau persetujuan sesuai dengan mekanisme internal perusahaan yang berlaku." | Peran |
| 7 | Enam status | "Berlaku", "Perlu Diperbarui", "Kedaluwarsa", "Belum Diverifikasi", "Belum Tersedia", "Tidak Berlaku untuk Perusahaan" dengan arti seperti di tabel Keterangan Status Dokumen | Istilah, Status Dokumen |
| 8 | Tindak lanjut | "Dokumen yang belum tersedia atau belum diverifikasi dicatat dalam daftar dan ditindaklanjuti kepada pihak yang relevan." / "Setiap tindak lanjut mencantumkan tindakan yang diperlukan, penanggung jawab, dan target penyelesaian." (Pemantauan dan Tindak Lanjut 3 dan 4) | Ketentuan 7 dan 8; tabel Tindak Lanjut |
| 9 | Pembaruan register | "Daftar induk diperbarui apabila terdapat penerbitan, perubahan, pembaruan, pencabutan, atau perubahan status dokumen." (butir 5) | Ketentuan 9 |
| 10 | Bukti pendukung | "Bukti pendukung disimpan pada lokasi penyimpanan dokumen perusahaan yang ditetapkan dan dapat diakses oleh pihak yang berwenang." (butir 6) | Ketentuan 10; kolom Lokasi Bukti |
| 11 | Riwayat | "Hasil pemeriksaan dan tindak lanjut dicatat untuk memastikan riwayat pembaruan dapat ditelusuri." (butir 7) | Ketentuan 11; tabel Catatan Pemeriksaan |
| 12 | Pemeriksaan berkala tanpa frekuensi | "Departemen Legal melakukan pemeriksaan atas kelengkapan dan keakuratan daftar induk secara berkala." (butir 1) | Diganti frekuensi bulanan (butir 14 di bawah) |
| 13 | Isi register perizinan dan pengingat 90 hari (fileId 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb, 4.4 butir 3) | "Register perizinan memuat jenis izin, nomor, masa berlaku, dan penanggung jawab; pengingat perpanjangan 90 hari sebelum jatuh tempo." | Petunjuk Pengisian 5; Dokumen Terkait |
| 14 | Tinjauan bulanan atas register izin (fileId 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW, Rutinitas Bulanan; juga SNX-HR-JA-01 JA-09) | "Meninjau register kontrak dan izin; menandai yang jatuh tempo dalam 90 hari; menyiapkan bahan laporan bulanan" | Ketentuan 5; Kesimpulan |
| 15 | Staff Legal memelihara register perizinan (fileId 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW, Administrasi dan Pemantauan) | "Memelihara register permintaan, register kontrak, register perizinan, dan arsip dokumen." | Ketentuan 1; Peran |
| 16 | Line Manager Legal memverifikasi akta (fileId 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb, 4.4 butir 2) | "Perubahan data perusahaan (anggaran dasar, pengurus, alamat, KBLI): Staff menyiapkan berkas, notaris memproses, Line Manager memverifikasi akta sebelum dinyatakan selesai." | Ketentuan 2 |
| 17 | "SK Kemenkum" dipakai tim sebagai jenis dokumen (fileId 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW, Due Diligence) | "Melakukan due diligence dasar pihak lawan: akta, SK Kemenkum, NIB, NPWP, kewenangan penandatangan, dan pencarian direktori putusan Mahkamah Agung." | Baris 7 tabel Isi Register ("misalnya SK Kemenkum") |
| 18 | Register perizinan dan pengingat izin di SNX-LEG-SOP-01 | "Pengingat perpanjangan izin (6.6 langkah 9)" / "90 hari sebelum jatuh tempo" (specs/LEG-SOP-01.json, tabel SLA); butir 4.24 "folder Google Drive departemen Legal (USULAN)" | Ketentuan 10; Dokumen Terkait; Rekaman |

## 3. Hasil uji

Perintah render: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/LEG-REG-01.json /tmp/pen-LEG-REG-01/LEG-REG-01.docx` (berhasil, tanpa galat).

Perintah lint: `python3 -I tools/lint_doc.py /tmp/pen-LEG-REG-01/LEG-REG-01.docx generic`

Hasil terakhir: `"pass": true`, `"fails": []`, `"warns": ["10 butir (USULAN) menunggu ACC"]`. Putaran render pertama sudah lulus lint; putaran berikutnya hanya memperbaiki tata letak tabel register (judul kolom terpotong di tengah kata) dan memecah kalimat lingkup 55 kata menjadi tiga kalimat. Pratinjau PDF (soffice, 11 halaman) dilihat lewat contact sheet dan halaman 8 sampai 9 resolusi penuh: sampul, Identity, Revision, Approval, TOC, dan sembilan bagian tampil; tabel Daftar Perizinan (6 kolom) dan Penerbitan, Penanggung Jawab, dan Lokasi Bukti (6 kolom) terbaca tanpa kata terpotong. Pemeriksaan tambahan: tidak ada em-dash maupun en-dash di spec; "Direktur (COO)" dan "COO" tidak dipakai (sumber tidak menyebut COO); Samuel di badan dokumen ditulis "Direktur Utama" (Kesimpulan); tidak ada nama orang di badan; tidak ada kata "penyusun", "dokumen sumber", "sumber tim", atau "draf ini" di badan. `python3 -I tools/lint_spot.py tools/lint_doc.py` memberi GAGAL 0.

## 4. Susunan dokumen dan alasan

| Bagian di docx hasil | Asal | Catatan |
|---|---|---|
| 1 Tujuan dan Lingkup | Tujuan 1 dan 2, Ruang Lingkup sumber | Daftar lingkup sumber dijadikan dua kalimat. Pengecualian (kontrak dan daftar peraturan) ditulis berlabel USULAN karena sumber diam (USULAN 9) |
| 2 Istilah | Istilah di spec; Keterangan Status Dokumen sumber | Hanya arti istilah dan arti status. Aturan ada di bagian 3. "Belum Tersedia" ditulis ulang agar tidak melingkar (lihat bagian 5 butir 9) |
| 3 Ketentuan Pengelolaan | Tanggung Jawab, Pemantauan dan Tindak Lanjut sumber | 11 butir, tiap butir satu pelaku. Pelaku Departemen Legal dipecah menjadi Staff Legal dan Line Manager Legal (USULAN 3) |
| 4 Peran | Tanggung Jawab sumber | Lima peran. Isi tugas merujuk nomor butir Ketentuan, tidak menyalin kalimat |
| 5 Petunjuk Pengisian | Kolom tabel sumber + kriteria | Sembilan butir. Tabel tanpa baris contoh; sel data kosong |
| 6 Isi Register | Bagian V sumber + kriteria | Tabel 6.1 memuat jenis izin, nomor, masa berlaku, jadwal perpanjangan, status. Tabel 6.2 memuat instansi penerbit, kegiatan usaha/KBLI, tanggal penerbitan, penanggung jawab, lokasi bukti. Dipecah dua karena tujuh kolom lebih membuat judul kolom terpotong di lebar 16 cm. Tabel 6.3 Tindak Lanjut dan 6.4 Catatan Pemeriksaan ditambah (cacat 4, 5) |
| 7 Dokumen Terkait | Kode yang disebut di badan | Enam kode ditambah SNX-LEG-REG-04 dan nomor lama |
| 8 Rekaman dan Acuan ISO | Ketentuan 10 dan 11 | Retensi "Belum ditetapkan" mengikuti SNX-LEG-SOP-01 butir 4.27; klausul berlabel satu kali |
| 9 Kesimpulan | Status dokumen, review_period | Dua kalimat |

Blok sumber yang tidak dibawa ke badan: Identitas Dokumen (diganti halaman Identity), Catatan Pemeriksaan dan Persetujuan (diganti blok Approval template, dengan tanda tangan dan tanggal kosong), Riwayat Perubahan Dokumen (diganti Revision History template, satu baris revisi 00), teks "[sengaja dikosongkan]", dan halaman akhir kosong.

Kriteria penerimaan, unsur demi unsur:

| Unsur kriteria | Letak di dokumen |
|---|---|
| Daftar perizinan perusahaan | Bagian 6, tabel 6.1 dan 6.2, baris 1 sampai 11 |
| Jenis izin | Kolom Jenis Izin, tabel 6.1 |
| Nomor | Kolom Nomor, tabel 6.1 |
| Masa berlaku | Kolom Masa Berlaku, tabel 6.1 |
| Jadwal perpanjangan | Kolom Jadwal Perpanjangan, tabel 6.1; Petunjuk Pengisian 5; Ketentuan 6 |
| NIB, KBLI, Akta Pendirian, NPWP, Anggaran Dasar | Baris 1 sampai 5 tabel 6.1, urut seperti di kriteria |

## 5. Penanganan cacat context/audit (bagian 5, fileId 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk)

Perintah: `grep -n 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk context/audit/*.md` (baris 15 dan 138 file legal, baris 82 file sintesis).

| # | Cacat di audit | Penanganan |
|---|---|---|
| 1 | Template kosong: tabel Bagian V berisi 3 baris tanpa data, belum ada NIB, NPWP, akta, SK, sertifikat OSS, atau izin sektoral | Sel data tetap kosong (tidak ada sumber; batas keras 4). Struktur kolom dan baris jenis dokumen disiapkan, termasuk lima jenis di kriteria. Isi nyata = open item 1 untuk Legal |
| 2 | Tanggal Penerbitan "[tanggal]" dan "[Nama/Jabatan]" placeholder; tanda tangan dan riwayat kosong | Tidak dibawa. Nama penanda tangan dari data baris; tanda tangan dan tanggal efektif kosong; satu baris revisi 00 dari revision_desc |
| 3 | Frekuensi pemeriksaan hanya "berkala", sedangkan SOP Divisi Legal 4.4 menyebut pengingat 90 hari dan Jobdesk Staff Legal tinjauan bulanan | Diperbaiki: Ketentuan 5 memakai tinjauan bulanan dan penandaan izin dalam 90 hari; Petunjuk Pengisian 5 memakai pengingat 90 hari. Konflik 90 hari dengan Jobdesk "90, 60, dan 30 hari" = open item 2 |
| 4 | Tidak ada kolom lokasi bukti, padahal IV.A.5 dan VII.F mensyaratkannya | Diperbaiki: kolom Lokasi Bukti di tabel 6.2; Ketentuan 10 menunjuk folder Google Drive departemen Legal (USULAN 8) |
| 5 | Tidak ada kolom tindak lanjut (tindakan, penanggung jawab, target), padahal VII.D mewajibkannya | Diperbaiki: tabel 6.3 Tindak Lanjut dengan tiga unsur itu; Ketentuan 8 |
| 6 | "[sengaja dikosongkan]" di halaman 2 dan halaman 6 kosong | Tidak dibawa; dicatat di bagian 4 |
| 7 | Nomor "001/LEGAL/SINUX/X/2026" memakai skema berbeda dari dokumen SINUX lain | Diperbaiki: nomor SNX-LEG-REG-01 (data baris). Nomor lama dicatat di Dokumen Terkait berlabel USULAN (USULAN 13) |
| 8 | Nama dokumen ganda: "Company Licenses and Permits Register" dan "Daftar Perizinan Perusahaan dan Legal Perusahaan" | Diperbaiki: satu nama, "Company Licenses & Permits Register" (judul di worklist). Nama Indonesia tidak dipakai |
| 9 | (temuan penyusun, bukan dari audit) Status "Belum Tersedia" didefinisikan dengan kata "belum tersedia" | Diperbaiki: "Dokumen yang relevan belum ditemukan atau belum dimiliki SINUX." Arti lima status lain dibawa apa adanya, dengan "Tidak Berlaku untuk Perusahaan" diberi titik di akhir |
| 10 | (temuan penyusun) Sumber memakai "daftar induk", "daftar", dan "dokumen ini" untuk satu hal | Diperbaiki: satu istilah, "register" |

Ejaan sumber yang dibakukan: "diperbaharui" menjadi "diperbarui", "mempengaruhi" menjadi "memengaruhi", "mengkoordinasikan" tidak dipakai.

## Asumsi

1. Process owner "Line Manager Legal". Sumber tidak punya baris "Pemilik dokumen"; yang ada hanya "Unit Kerja: Legal dan Compliance" (nama departemen, bukan jabatan). Dipakai jabatan reviewer departemen Legal tanpa nama, sama dengan SNX-LEG-SOP-01 yang menulis pemilik SOP Line Manager Legal.
2. Baris awal tabel register diisi nama jenis dokumen saja: lima dari kriteria (NIB, KBLI, Akta Pendirian, NPWP, Anggaran Dasar, urut seperti di kriteria) dan empat dari lingkup sumber (akta perubahan; surat keputusan atau penerimaan pemberitahuan; perizinan berusaha dan sertifikat standar OSS; izin sektoral). Itu nama kategori, bukan data. Nomor, tanggal, masa berlaku, status, dan penanggung jawab kosong.
3. "Departemen Legal dan Compliance" di sumber dibaca sebagai Departemen Legal (Line Manager Legal dan Staff Legal), memakai istilah SNX-LEG-SOP-01. Fungsi Compliance berada pada jabatan Legal & Compliance menurut SNX-HR-ORG-01, jadi tidak diberi peran terpisah.
4. Staff Legal = jabatan Legal & Compliance JA-09 dan Line Manager Legal = JA-08 menurut Matriks Peran SNX-HR-ORG-01 (butir K-13, pemetaan USULAN; atasan JA-08 menunggu konfirmasi K-03). Atasan Line Manager Legal tidak disebut di badan dokumen.
5. "Penanggung jawab izin" dibuat sebagai peran, karena Staff Legal mengirim pengingat kepada penanggung jawab izin (SNX-LEG-SOP-01 prosedur 6.6) dan sumber register punya kolom Penanggung Jawab tanpa penjelasan.
6. Angka 90 hari dari SOP Divisi Legal 4.4 butir 3 berlaku untuk register perizinan, yaitu lingkup yang sama dengan dokumen ini. Tidak dipakai untuk aktivitas lain.
7. Tinjauan bulanan atas register izin dari Jobdesk Staff Legal (JA-09) dipakai pada Staff Legal. Kontrak di register kontrak tidak masuk dokumen ini.
8. Klasifikasi RESTRICTED (Internal) dari data baris; label di footer dipasang renderer.
9. "Dokumen tanpa masa berlaku" ditangani dengan instruksi mengisi "tidak ada masa berlaku". Tidak ada klaim di dokumen bahwa NIB, NPWP, atau akta punya atau tidak punya masa berlaku; sumber diam dan itu urusan hukum yang diputus Legal.
10. Pada baris 7 ditambahkan "(misalnya SK Kemenkum)" karena Jobdesk Staff Legal memakai istilah itu untuk jenis dokumen yang sama; lingkup sumber hanya menulis "Surat keputusan atau surat penerimaan pemberitahuan dari instansi yang berwenang".
11. Diagram tidak dibuat: sumber tidak punya diagram (audit membuka halaman 1 sampai 6, hanya teks dan tabel), dan kriteria tidak meminta alur.

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan: prepared Staff Legal, reviewed Line Manager Legal, approved Samuel Kristanto Utomo / President Director; sumber menulis "[Nama/Jabatan]" tanpa isi (config/defaults.json D2) | Blok Approval halaman depan | owner |
| 2 | Process owner = Line Manager Legal (sumber tanpa "Pemilik dokumen") | Identity; Peran | Legal |
| 3 | Pembagian peran: Staff Legal mencatat, memperbarui, memantau; Line Manager Legal memeriksa isi register dan memverifikasi akta. Sumber hanya menyebut "Departemen Legal dan Compliance" | Ketentuan 1, 2; Peran | Legal |
| 4 | Kolom Jadwal Perpanjangan (tanggal pengingat dan tanggal target pengajuan perpanjangan). Kolom dituntut kriteria; sumber tidak punya kolom itu dan tanggal target pengajuan tidak ada di sumber mana pun | Istilah; Petunjuk Pengisian 5; tabel 6.1 | Legal |
| 5 | Kolom Lokasi Bukti, tabel Tindak Lanjut, dan tabel Catatan Pemeriksaan, untuk menutup cacat 4 dan 5 serta butir sumber VII.G | Bagian 6, tabel 6.2 sampai 6.4 | Legal |
| 6 | Kolom Penanggung Jawab ditulis nama jabatan menurut SNX-HR-ORG-01, bukan nama orang | Petunjuk Pengisian 7 | Legal |
| 7 | Status Perlu Diperbarui dan Kedaluwarsa juga memicu tindak lanjut (sumber hanya menyebut Belum Tersedia dan Belum Diverifikasi) | Ketentuan 7 | Legal |
| 8 | Folder Google Drive departemen Legal sebagai lokasi bukti pendukung dan register (mengikuti SNX-LEG-SOP-01 butir 4.24 yang juga USULAN) | Ketentuan 10; Rekaman | Legal |
| 9 | Pengecualian lingkup: kontrak dengan pelanggan atau vendor (register kontrak di SNX-LEG-SOP-01) dan daftar peraturan (SNX-LEG-REG-03); sumber tidak menyebut pengecualian | Lingkup | Legal |
| 10 | Pemilihan sembilan jenis dokumen pada baris awal tabel, termasuk "Akta perubahan" dan "Anggaran Dasar" sebagai baris sendiri | Tabel 6.1 dan 6.2 | Legal |
| 11 | Peran Pejabat yang Berwenang dibawa dari sumber tanpa dipetakan ke jabatan | Peran | Legal |
| 12 | Nomor lama 001/LEGAL/SINUX/X/2026 digantikan SNX-LEG-REG-01 | Dokumen Terkait | Legal |
| 13 | Batas pencatatan dengan SNX-LEG-REG-04 untuk Akta Pendirian dan Anggaran Dasar (kriteria baris 40 dan baris 39 sama-sama menyebut dokumen korporasi) | Dokumen Terkait | Legal |
| 14 | Retensi register dan bukti pendukung belum ditetapkan; usulan penetapan di SNX-LEG-SOP-03 (USULAN di SNX-LEG-SOP-01 butir 4.27) | Rekaman | Legal |
| 15 | Acuan klausul ISO: ISO 9001:2015 4.2 dan 7.5.3; ISO/IEC 27001:2022 Annex A 5.31 dan 5.33. Checklist tidak memberi acuan untuk baris ini; label "(USULAN, perlu konfirmasi konsultan)" dipasang satu kali di bagian Acuan ISO | Rekaman dan Acuan ISO | owner (setelah konfirmasi konsultan) |

## Open items

1. Semua sel data register kosong: nomor NIB, kode KBLI, nomor akta, Anggaran Dasar, NPWP, instansi, tanggal, masa berlaku, status, penanggung jawab, dan lokasi bukti tidak ada di sumber (tabel sumber hanya tiga baris kosong). Register belum bisa jadi bukti audit sampai Legal mengisinya dari dokumen asli. Penentu: Legal.
2. Konflik angka pengingat izin: SOP Divisi Legal 4.4 butir 3 menulis "pengingat perpanjangan 90 hari sebelum jatuh tempo" (kepada penanggung jawab izin menurut SNX-LEG-SOP-01), sedangkan Jobdesk Staff Legal menulis "Mengirim pengingat jatuh tempo kontrak dan izin kepada PIC bisnis pada 90, 60, dan 30 hari sebelumnya". Dokumen memakai 90 hari. Penentu: Legal.
3. Frekuensi pemeriksaan: sumber register hanya "secara berkala"; tinjauan bulanan berasal dari Jobdesk Staff Legal dan SNX-HR-JA-01. Dokumen memakai bulanan. Penentu: Legal.
4. Batas waktu memperbarui register setelah ada penerbitan, perubahan, atau pencabutan tidak ada di sumber (register kontrak punya batas 2 hari kerja, tidak dipakai di sini). Penentu: Legal.
5. Jabatan Pejabat yang Berwenang untuk pemeriksaan atau persetujuan tidak ditetapkan sumber. Penentu: Legal.
6. Penanggung jawab izin per jenis dokumen (misalnya NPWP: Legal, Finance, atau Accounting & Tax) tidak ada di sumber. Penentu: Legal dan FAT.
7. KBLI bukan izin tersendiri. Kriteria menyebutnya sebagai jenis, jadi dicatat sebagai baris 2. Apakah KBLI dicatat per NIB atau per kegiatan usaha, dan apakah Anggaran Dasar dicatat terpisah dari Akta Pendirian, tidak dinyatakan sumber. Penentu: Legal.
8. Batas dengan SNX-LEG-REG-04 (Company Legal Documents Register): kedua dokumen bisa memuat Akta Pendirian dan Anggaran Dasar, dan SNX-LEG-REG-04 juga memuat masa berlaku. Perlu diputuskan satu dokumen sebagai pemilik tiap jenis. Penentu: Legal.
9. Periode retensi dokumen legal belum ditetapkan (SNX-LEG-SOP-01 butir 4.27). Penentu: Legal.
10. Kriteria menyebut "jadwal perpanjangan"; sumber hanya punya "Masa Berlaku" dan "ketentuan perpanjangan yang berlaku" tanpa menyebut ketentuannya. Isi ketentuan perpanjangan per izin (instansi, prosedur, lead time) tidak ada di sumber. Penentu: Legal.
11. Kalimat perintah di sumber: tidak ada yang menyasar penyusun. Kalimat seperti "Dokumen ini disusun sebagai sarana pencatatan ..." deskriptif dan dipakai sebagai isi. Teks "[sengaja dikosongkan]" tidak dibawa.
12. Tracked change dan teks tersembunyi di berkas Drive tidak diuji (read_file_content tidak menampilkannya); komentar Drive diminta dan tidak ada.
13. Kutipan dari SNX-LEG-SOP-01, SNX-HR-JA-01, dan SNX-HR-ORG-01 diambil dari specs di repo, bukan dari dokumen final; selaraskan bila dokumen itu berubah. modifiedTime SOP Divisi Legal tidak diukur ulang di sesi ini.

## 6. Pemeriksaan mutu (dua pertanyaan)

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI? Temuan pada draf pertama dan perbaikannya:

| Temuan | Perbaikan |
|---|---|
| Kalimat lingkup 55 kata berisi tujuh jenis dokumen dalam satu napas, bentuk daftar yang bisa ditempel di perusahaan mana pun | Dipecah menjadi tiga kalimat; daftar dipertahankan karena itu isi lingkup sumber |
| Tabel register tujuh kolom: judul kolom terpotong di tengah kata ("Penanggung Jawab" menjadi "Penanggun g Jawab"), tampak tidak dirawat | Dipecah menjadi dua tabel enam kolom, lebar kolom diuji lewat PDF |
| Sumber memakai "daftar induk", "daftar", dan "dokumen ini" untuk satu hal | Satu istilah "register" di seluruh dokumen |
| Definisi "Belum Tersedia" memakai kata yang didefinisikan | Ditulis ulang: "belum ditemukan atau belum dimiliki SINUX" |
| Kelompok tiga yang dipaksakan | Dicek: tidak ada yang ditambahkan. Daftar yang ada berasal dari sumber (tujuh jenis lingkup, enam status, lima tugas Departemen Legal) atau struktur data (sembilan petunjuk, sebelas butir) |
| Benda diberi kata kerja manusia ("register memutuskan") | Dicek: tidak ada; "Register ini mencatat" dan "Register mencakup" bersifat deskriptif, tindakan selalu punya pelaku peran |
| Pasif tanpa pelaku untuk hal yang pelakunya diketahui ("Bukti pendukung disimpan ...") | Dipertahankan hanya di Ketentuan 10 karena pelaku penyimpanan sudah ada di Ketentuan 1 dan kalimat berikutnya menyebut Staff Legal menulis lokasinya |
| Penutup positif generik, frasa pengisi, penegasan kosong, tebal, huruf kapital atau tanda kutip untuk penekanan, em-dash dan en-dash | Nol temuan (lint gaya pass; en-dash dicari di spec: nol) |
| Kesimpulan | Dua kalimat tentang status dan peninjauan, tanpa pujian |

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir | Sumber atau status |
|---|---|
| "90 hari" (pengingat perpanjangan dan penandaan izin) | SOP Divisi Legal 4.4 butir 3 dan Jobdesk Staff Legal Rutinitas Bulanan; dipakai pada lingkup register perizinan. Konflik dengan "90, 60, dan 30 hari" di Jobdesk = open item 2 |
| "setiap bulan" (tinjauan register) dan "setiap tahun" (peninjauan dokumen) | Jobdesk Staff Legal dan SNX-HR-JA-01 JA-09; data baris review_period YEARLY |
| "enam status", "sembilan jenis", "baris 1 sampai 9", "baris 10 dan 11" | Enam status dari sumber; sisanya struktur tabel buatan sendiri, bukan fakta |
| Tanggal target pengajuan perpanjangan | Tidak ada di sumber; berlabel (USULAN 4) |
| Nama orang | Hanya Samuel Kristanto Utomo di blok Approval (data baris). Badan dokumen tanpa nama orang |
| Nama peran Line Manager Legal dan Staff Legal | specs/HR-ORG-01.json Matriks Peran (USULAN, K-13) |
| "SK Kemenkum" | Jobdesk Staff Legal, Due Diligence |
| "folder Google Drive departemen Legal" | SNX-LEG-SOP-01 butir 4.24 (USULAN) |
| Kode SNX-LEG-REG-03, SNX-LEG-REG-04, SNX-LEG-SOP-03 dan deskripsinya | config/worklist.json dan config/checklist.json baris 35 dan 39 (deskripsi checklist, bukan isi dokumen final) |
| Klausul ISO 9001:2015 4.2 dan 7.5.3; 27001:2022 Annex A 5.31 dan 5.33 | Tidak ada di checklist; praktik umum ISO, berlabel "(USULAN, perlu konfirmasi konsultan)" |
| Klaim "Perizinan dan legalitas adalah persyaratan instansi berwenang yang relevan bagi kegiatan usaha SINUX" (Acuan ISO 4.2) | Tafsir hubungan klausul, bukan fakta SINUX baru; ikut label USULAN klausul |
| Tanggal | Tidak ada tanggal di dokumen hasil; tanggal penerbitan "[tanggal]" sumber tidak dibawa; tanggal efektif kosong |
