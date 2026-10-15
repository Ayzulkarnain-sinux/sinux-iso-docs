# Catatan penyusun MKT-REG-02: Marketing Campaign & Activity Register

Status: DRAFTED (spec + notes ada). Spec: specs/MKT-REG-02.json. Mode generic (doc_type_cover "REGISTER", doc_type_label "Register"), aksi T2, wave W7, nomor SNX-MKT-REG-02 (nomor SNX lama dipertahankan), department Marketing, classification INTERNAL (worklist), audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Zilly Dwinata / Brand & Marketing", reviewed "Laras Rasmawati / VP Commercial", approved "Samuel Kristanto Utomo / President Director". process_owner "VP Commercial": dokumen tanpa sumber memakai jabatan reviewer departemen, tanpa nama. Catatan worklist: kosong.

Perubahan cakupan di tengah penyusunan: draf pertama saya adalah register materi dan klaim (11 field minimum langsung di tabel). Orkestrator memutus sebaliknya: baris 58 tidak boleh menjadi register kedua untuk materi dan klaim, sebab SNX-MKT-REG-01 sudah memuatnya. Spec ditulis ulang sebagai register pelaksanaan campaign dan aktivitas: satu baris per campaign atau aktivitas, dengan kolom yang menautkan tiap materi eksternal ke ID Persetujuan Materi di SNX-MKT-REG-01. Semua angka uji di bawah berasal dari spec versi kedua ini. Versi pertama dibuang, tidak ada sisanya di repo.

Uji terakhir (spec versi kedua):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-REG-02.json /tmp/pen-MKT-REG-02/MKT-REG-02.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-02/MKT-REG-02.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "20 butir (USULAN) menunggu ACC" (sesudah sweep; lihat bagian Sweep).
- Tata letak: docx dikonversi ke PDF dengan soffice (11 halaman). Seluruh halaman dilihat sebagai montase 45 dpi; halaman 8 dan 9 (Tabel 1 sampai Tabel 3) dilihat lagi pada 70 dpi: header kolom terbaca utuh, tidak ada kata terpotong. Tabel 1 terpotong di batas halaman 8 dan 9 (tiga baris di halaman 8); renderer tidak punya kendali pindah halaman, jadi dibiarkan. Halaman lain tidak dilihat pada resolusi tinggi (UNMEASURED).
- Validator OOXML skill docx tidak dijalankan (UNMEASURED); lint menguji id bookmark ganda.
- Kecocokan kode SNX di badan dengan bagian Dokumen Terkait diperiksa dengan skrip kecil: 7 kode di badan, nol kode kurang, nol kode berlebih.
- Pemindaian teks spec untuk em-dash, en-dash, "tim", peran "Lead", "penyusun", "dokumen sumber", "draf ini", "pihak luar" (diseragamkan "pihak di luar SINUX"), dan kalimat ganda antarbagian: nol temuan. Satu kecocokan "Lead" adalah judul SNX-MKT-REG-03 ("Marketing Lead & Campaign Outcome Register"), bukan peran.
- Lint dan skrip hanya membuktikan format dan larangan pola. Kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.
- Diagram: tidak ada. Register tidak memerlukan diagram dan kriteria baris 58 tidak memintanya.

## 1. Sumber

Prompt menyatakan sumber: tidak ada (T2 tanpa sumber). Tidak ada fileId yang ditugaskan untuk baris ini. Alat Drive dimuat dan dipakai hanya untuk baca (get_file_metadata, read_file_content); nol tulis ke Drive. Berkas Drive dibaca karena register ini menyebut jabatan dan tingkat klasifikasi dari dokumen lain.

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| Checklist ISO SINUX - 2026, baris 58 (kriteria penerimaan) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY | 2026-10-14T17:47:13.611Z (get_file_metadata di sesi ini; sama dengan config/checklist.json) | config/checklist.json baris 58: `checked: false`, `fileId: null`, `link_url: null`, `iso_9001: null`, `iso_27001: null`. Tidak ada berkas tertaut dan tidak ada acuan klausul |
| SINUX_Job_Analysis_2026.docx (HR-JA-001, bagian JA-06) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z (get_file_metadata di sesi ini) | read_file_content, teks utuh dibaca di sesi ini; kutipan di bawah dari teks itu |
| SNX-ISMS-PRO-01_Information_Classification_Handling_Procedure.docx | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io | 2026-10-13T06:09:00Z (get_file_metadata di sesi ini) | read_file_content, teks utuh dibaca di sesi ini |
| Pendukung repo (bukan Drive): specs/MKT-REG-01.json, specs/MKT-RPT-01.json, specs/MKT-REG-03.json | - | repo kerja, dibaca saat menyusun versi kedua | Dibaca sebagai DATA untuk menyelaraskan istilah (Materi, Channel, Disetujui, Terbit, Tanggal Persetujuan, Kode Aktivitas, Campaign Asal) dan nomor butir. Ketiganya masih Draft dan ditulis lane lain; kutipan darinya bisa basi |
| Pendukung repo: config/defaults.json v21, config/worklist.json, specs/HR-ORG-01.json (DONE), specs/COM-SOP-02.json (judul), specs/COM-REG-01.json (pola register T2) | - | repo kerja | Nama jabatan, judul dokumen, pola struktur |

Kalimat perintah kepada AI di semua sumber yang dibaca: nihil. Kalimat kewajiban di sumber ("Pemilik informasi menetapkan ...") adalah isi dokumen, bukan instruksi untuk penyusun. Pesan orkestrator tentang cakupan diperlakukan sebagai arahan kerja yang sah, bukan sebagai sumber fakta.

Pemetaan kriteria baris 58 ke dokumen. Sejak keputusan cakupan, unsur materi dan klaim dipenuhi lewat tautan ke SNX-MKT-REG-01, bukan dengan menyalin kolomnya:

| Unsur Description | Di MKT-REG-02 | Di SNX-MKT-REG-01 (lewat ID Persetujuan Materi) |
|---|---|---|
| Mengendalikan materi dan konten pemasaran eksternal: company profile, website, social media, product brochure, presentation deck, campaign material, event collateral | Ruang Lingkup (tujuh jenis persis seperti kriteria); Tabel 3 kolom Jenis Konten/Channel (Cara Mengisi 6.11); Ketentuan 4.4 sampai 4.9 | Ruang Lingkup REG-01 memuat tujuh jenis yang sama |
| Keakuratan informasi dan validasi klaim sebelum dipublikasikan | Ketentuan 4.5 (materi dipakai hanya bila Disetujui atau Terbit), 4.6, 4.7, 4.8 | Tabel 4 Klaim dan Bukti Pendukung; butir 4.13 (Approver tidak menyetujui klaim tanpa bukti) |
| Nama materi | tidak ada (sengaja, tanpa duplikasi) | Tabel 1 kolom Nama Materi |
| Jenis konten/channel | Tabel 3 kolom Jenis Konten/Channel (menumpuk dengan REG-01; open item 2) | Tabel 1 kolom Jenis Konten dan Channel |
| Produk/layanan terkait | Tabel 1 kolom Produk/Layanan Terkait, pada tingkat campaign atau aktivitas | Tabel 1 kolom Produk atau Layanan Terkait, pada tingkat materi (lihat open item 2) |
| Versi | tidak ada | Tabel 1 kolom Versi |
| Klaim yang perlu diverifikasi; sumber/bukti pendukung | tidak ada | Tabel 4 kolom Klaim yang Perlu Diverifikasi dan Sumber atau Bukti Pendukung; hasil di Tabel 5 |
| PIC | Tabel 1 kolom PIC (PIC campaign atau aktivitas) | Tabel 2 kolom PIC (PIC materi) |
| Reviewer/approver; tanggal persetujuan | tidak ada; Tabel 3 kolom Tanggal Pengecekan Persetujuan mencatat kapan Brand & Marketing mengecek baris itu | Tabel 2 kolom Reviewer, Approver, Tanggal Persetujuan |
| Status publikasi | tidak ada | Tabel 3 kolom Status Publikasi |
| Lokasi file final | tidak ada | Tabel 1 kolom Lokasi File Final |
| Bukti: materi final yang telah disetujui; bukti verifikasi klaim yang relevan; catatan persetujuan sebelum dipublikasikan | Tujuan kalimat 3; Rekaman baris 2 (lokasi dan pemilik mengikuti REG-01) | Tabel 1 kolom Lokasi File Final; Tabel 4 dan Tabel 5 (bukti verifikasi); Tabel 2 kolom Bukti Persetujuan |
| Klausul ISO (checklist tidak memberi acuan) | Bagian Acuan ISO, satu label "(USULAN, perlu konfirmasi konsultan)" | tidak berlaku |

Penilaian manusia: apakah tautan ke REG-01 memenuhi Description baris 58 tanpa menyalin field minimumnya adalah keputusan cakupan orkestrator. Pemenuhan penuh tiap field oleh REG-02 sendiri tidak bisa dibuktikan mesin. Owner atau verifikator menilai (open item 1).

Kolom di luar kriteria: Nama Campaign atau Aktivitas, Jenis, Tanggal Mulai, Tanggal Selesai, Status, Kode Aktivitas (Tabel 1 dan 2); No Campaign atau Aktivitas, ID Persetujuan Materi, Tanggal Pengecekan Persetujuan (Tabel 3). Kolom itu mengikuti judul baris 58 dan arahan orkestrator; semuanya masuk USULAN 1.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Kriteria baris 58 meminta kendali materi eksternal, validasi klaim sebelum publikasi, sebelas field, dan tiga bukti. Dasar seluruh pemetaan, termasuk alasan bagian Rekaman menunjuk ke REG-01 | "Mengendalikan materi dan konten pemasaran yang digunakan untuk kebutuhan eksternal, termasuk company profile, website, social media, product brochure, presentation deck, campaign material, dan event collateral, serta memastikan keakuratan informasi dan validasi klaim produk/layanan sebelum dipublikasikan." dan "Bukti: materi final yang telah disetujui, bukti verifikasi klaim yang relevan, serta catatan persetujuan sebelum dipublikasikan." (checklist baris 58, kolom Description) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY (checklist; baris 58 sendiri `fileId: null`) |
| Brand & Marketing (JA-06) mengelola event, webinar, dan campaign, dan hanya menjadwalkan publikasi setelah persetujuan. Dasar jenis Campaign, Event, Webinar, peran Brand & Marketing sebagai pencatat, dan Ketentuan 4.5 | "Mengelola event/webinar/campaign serta koordinasi vendor bila ada." (A. Uraian Jabatan butir 4) dan "Menjadwalkan publikasi setelah persetujuan" (E. Wewenang butir 2) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| Tingkat INTERNAL berlaku untuk informasi tanpa label dan untuk dokumen yang tidak untuk pihak luar. Dasar Ketentuan 4.10 (register berklasifikasi INTERNAL) | "INTERNAL \| Untuk seluruh karyawan dan kontraktor SINUX; tidak untuk pihak luar tanpa alasan bisnis \| SOP umum, jadwal shift, pengumuman internal, template \| Kecil, memalukan atau merugikan ringan" (bagian 4) dan "Informasi PUBLIC dan INTERNAL boleh tanpa label; tanpa label dianggap INTERNAL." (bagian 5) | 1h5PtuUGE8UDPbwPtccUQ8pgwgAoW64Io |

Fakta pendukung (dari spec repo yang masih Draft, bukan Drive; tanpa fileId):

| # | Fakta di dokumen | Kutipan verbatim | Posisi |
|---|---|---|---|
| 1 | ID Persetujuan Materi = nomor baris, satu versi satu materi satu channel (Definisi; Ketentuan 4.9) | "4.1 Satu baris mencatat satu versi dari satu materi di satu channel. Tabel 1 sampai Tabel 3 memakai nomor baris yang sama (USULAN)." | specs/MKT-REG-01.json, Dasar dan Ketentuan 4.1 |
| 2 | Klaim tanpa bukti tidak lolos persetujuan (Ketentuan 4.6) | "4.13 Approver tidak menyetujui versi yang masih memuat klaim tanpa bukti pendukung, atau klaim yang Pemverifikasi tolak (USULAN)." | specs/MKT-REG-01.json 4.13; berstatus USULAN di dokumen itu, sehingga kalimat turunan di REG-02 4.6 diberi label |
| 3 | Versi baru memakai baris baru (Ketentuan 4.9) | "4.8 Perubahan isi pada versi yang sudah Disetujui atau Terbit membuat versi baru, dengan baris baru dan persetujuan baru." | specs/MKT-REG-01.json 4.8 |
| 4 | Klasifikasi materi ditetapkan Approver (Ketentuan 4.10) | "4.5 Materi berklasifikasi INTERNAL sampai Approver menetapkan PUBLIC saat menyetujui versinya." | specs/MKT-REG-01.json 4.5 |
| 5 | Kolom Campaign Asal di REG-03 merujuk nama campaign di register ini (Ketentuan 4.3) | "6.5 Brand & Marketing menulis nama campaign di kolom Campaign Asal persis seperti di SNX-MKT-REG-02, atau Tanpa campaign bila lead tidak berasal dari campaign (butir 4.13)." | specs/MKT-REG-03.json 6.5 |
| 6 | Aktivitas di RPT-01 punya Kode, jadwal, dan PIC (kolom Kode Aktivitas, Tabel 2) | Header tabel: ['Kode', 'Aktivitas', 'Marketing Objective', 'Channel', 'Mulai', 'Selesai', 'PIC'] | specs/MKT-RPT-01.json, Isi Laporan |
| 7 | Atasan langsung Brand & Marketing adalah VP Commercial (dasar VP Commercial sebagai pemilik register) | "Atasan Langsung \| Commercial – Laras Rasmawati" (tabel JA-06) | fileId 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |

## 2. Asumsi

1. Register ini struktur kosong. Sel data kosong; tidak ada baris contoh, tidak ada nama campaign, tidak ada nama produk. Yang berisi hanya nomor baris.
2. Jabatan di bagian Peran dipetakan ke daftar jabatan SNX-HR-ORG-01: Brand & Marketing (JA-06) dan VP Commercial (JA-03). Peran Reviewer, Approver, dan Pemverifikasi atas materi tidak diulang di register ini; Peran menunjuk SNX-MKT-REG-01. Peran sumber yang tidak ada di daftar jabatan: nihil.
3. Judul "Campaign & Activity Register" dibaca sebagai register pelaksanaan campaign dan aktivitas, mengikuti arahan orkestrator. "Aktivitas" dalam register ini berarti kegiatan di luar campaign (event, webinar), karena JA-06 uraian 4 menyebut "event/webinar/campaign" berdampingan. SNX-MKT-RPT-01 memakai "Aktivitas" lebih luas (campaign, konten, event, webinar); beda cakupan istilah itu dicatat di open item 4.
4. Definisi Campaign dan Aktivitas adalah rumusan netral penyusun, tanpa sumber persis. JA-06 uraian 4 hanya menyebut ketiga kata itu. Definisi tidak membawa fakta SINUX, jadi tidak diberi label (USULAN).
5. ID Persetujuan Materi dibaca sebagai nomor yang tertulis di kolom ID Tabel 1 SNX-MKT-REG-01 untuk satu versi dari satu materi di satu channel. REG-01 menyebutnya "ID persetujuan"; register ini memakai "ID Persetujuan Materi" (open item 6).
6. Materi dipakai campaign atau aktivitas hanya bila baris REG-01 berstatus Disetujui atau Terbit dan Tanggal Persetujuannya terisi (USULAN 7). "Terbit" dipakai karena materi yang sudah tayang sebelumnya juga boleh dipakai ulang campaign baru. Sumber diam.
7. Kolom Status memakai empat nilai (Direncanakan, Berjalan, Selesai, Dibatalkan). SNX-MKT-RPT-01 memakai tiga nilai berbeda untuk Status Pelaksanaan bulanan (Terlaksana, Tertunda, Dibatalkan). Nama kolom sengaja "Status" supaya tidak bentrok; nilai tidak diselaraskan (open item 4).
8. "Direktur (COO)" dan "COO" tidak muncul di badan dokumen, jadi aturan sebutan pertama tidak terpicu. Samuel di badan dokumen ditulis "Direktur Utama" (Peran dan Kesimpulan).
9. Angka: tidak ada angka dari sumber yang disalin. "10 baris" adalah ukuran tata letak mengikuti specs/COM-REG-01.json, bukan klaim tentang SINUX. Empat nilai status dan empat nilai jenis adalah pilihan isi register.
10. Klasifikasi INTERNAL dari worklist. Register tidak memuat isi materi atau klaim, hanya nama campaign, tanggal, status, dan nomor baris REG-01.
11. Ejaan: "Zilly Dwinata" mengikuti config/defaults.json dan HR-JA-001. KPI COMMERCIAL & MARKETING.xlsx menulis "Zily" di nama sheet; tidak dipakai.

## USULAN

Lint menghitung 21 kemunculan "(USULAN)" ditambah satu "(USULAN, perlu konfirmasi konsultan)" di spec. Dikelompokkan menjadi 17 butir. Kolom pemutus memakai kelompok owner, Samuel, Aziz, FAT, Legal, atau Fani.

| # | Butir USULAN | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Struktur kolom dan tiga tabel, termasuk kolom di luar kriteria: Nama Campaign atau Aktivitas, Jenis, Tanggal Mulai, Tanggal Selesai, Status, Kode Aktivitas, No Campaign atau Aktivitas, ID Persetujuan Materi, Tanggal Pengecekan Persetujuan; ukuran awal 10 baris | Isi Register; Peran (VP Commercial menetapkan struktur) | owner ; diubah W9: kolom Jenis, Kode Aktivitas, Produk/Layanan, dan Tabel 3 dihapus; Tabel 1 dan 2 berisi kolom daftar A8 |
| 2 | Batas cakupan REG-01 lawan REG-02: REG-01 memuat tiap versi materi beserta klaimnya, register ini memuat campaign dan aktivitas yang memakai materi dan hanya ID Persetujuan Materi | Ruang Lingkup paragraf 2 | owner ; diubah W9: A8 diputus owner; REG-01 satu-satunya register materi, konten, dan persetujuan klaim |
| 3 | Pengecualian: persetujuan materi dan verifikasi klaim ke SNX-MKT-REG-01; rencana, anggaran, target, dan evaluasi hasil ke SNX-MKT-RPT-01; serah terima lead dan hasil campaign berupa lead ke SNX-MKT-REG-03 | Ruang Lingkup tabel; Dokumen Terkait | owner ; diubah W9: batas sudah diputus (A8), label USULAN pada batas dihapus; REG-03 merujuk nama Aktivitas |
| 4 | Brand & Marketing mencatat campaign atau aktivitas di Tabel 1 sebelum dijalankan | Ketentuan 4.2 | owner ; diubah W9: istilah menjadi Aktivitas |
| 5 | Nama campaign atau aktivitas ditulis dengan satu ejaan tetap, dan SNX-MKT-REG-03 merujuknya di kolom Campaign Asal | Ketentuan 4.3; Dokumen Terkait | owner ; diubah W9: istilah menjadi nama Aktivitas |
| 6 | Brand & Marketing mencatat tiap materi yang dipakai di Tabel 3 dengan ID Persetujuan Materi | Ketentuan 4.4; Cara Mengisi 6.10, 6.13 | owner ; diubah W9: ID Persetujuan Materi ditulis di Tabel 1 (Cara Mengisi 6.7); Tabel 3 dihapus |
| 7 | Materi dipakai hanya bila baris REG-01 berstatus Disetujui atau Terbit dan Tanggal Persetujuan terisi (kalimat 2 dari 4.5, wewenang JA-06 untuk menjadwalkan publikasi setelah persetujuan, bersumber) | Ketentuan 4.5 kalimat 1 | owner |
| 8 | Klaim materi sudah diverifikasi saat baris REG-01 Disetujui atau Terbit (turunan dari REG-01 butir 4.13, yang berstatus USULAN di dokumen itu) | Ketentuan 4.6 kalimat 2 | owner ; ditutup W9: butir 4.6 diganti; register tidak mencatat klaim dan hanya menelusuri validasi klaim di REG-01 |
| 9 | Brand & Marketing mengecek baris REG-01 sebelum materi dipakai dan menulis tanggal pengecekan | Ketentuan 4.7; Cara Mengisi 6.14 | owner ; diubah W9: tanggal pengecekan dihapus (kolom di luar daftar A8); ketentuan 4.7 tetap, tanpa Cara Mengisi 6.14 |
| 10 | Materi yang ternyata dipakai tanpa persetujuan: Brand & Marketing menghentikan pemakaian dan melapor, VP Commercial memutuskan tindak lanjut | Ketentuan 4.8 | owner |
| 11 | Beralih ke versi baru = baris baru di Tabel 3 sesudah versi itu Disetujui, baris lama tidak dihapus | Ketentuan 4.9 | owner ; diubah W9: ID versi baru ditambah di Tabel 1 (Ketentuan 4.9, Cara Mengisi 6.7), bukan baris baru di Tabel 3 |
| 12 | Register berklasifikasi INTERNAL | Ketentuan 4.10; Acuan ISO | owner |
| 13 | Folder Google Drive departemen Commercial (sama dengan SNX-MKT-REG-01; unit JA-06 adalah Commercial) sebagai lokasi simpan, jalur folder belum ditetapkan; pemilik VP Commercial; pencatat Brand & Marketing | Ketentuan 4.11; Rekaman baris 1 | owner |
| 14 | Retensi register: "Belum ditetapkan", tanpa angka; retensi materi, bukti, dan catatan persetujuan "Mengikuti SNX-MKT-REG-01" | Rekaman | Legal |
| 15 | Pembagian tugas Brand & Marketing dan VP Commercial; VP Commercial sebagai pemilik register (process_owner); tinjauan tahunan oleh VP Commercial | Peran; Kesimpulan; meta process_owner | owner |
| 16 | Nilai kolom Jenis (Campaign, Event, Webinar, Lainnya) dan nilai kolom Status (empat nilai) | Cara Mengisi 6.3, 6.8; Definisi Status Campaign atau Aktivitas | owner ; diubah W9: kolom Jenis dihapus; tersisa nilai kolom Status (Cara Mengisi 6.10, Definisi Status Aktivitas) |
| 17 | Lima klausul acuan: ISO 9001:2015 7.4, 8.2.1, 8.2.2, 7.5.3; ISO/IEC 27001:2022 Annex A 5.12. Satu label "(USULAN, perlu konfirmasi konsultan)". Klausul 8.2.2 dipilih karena memuat kewajiban memastikan SINUX dapat memenuhi klaim produk dan layanan yang ditawarkan; di register ini kaitannya lewat tautan ke REG-01 | Acuan ISO | owner (lewat konsultan) ; diubah W9: 8.2.1 dan 8.2.2 merujuk Tabel 1, bukan Tabel 3 |

Tautan Kode Aktivitas ke SNX-MKT-RPT-01 (Tabel 2, Cara Mengisi 6.9, Dokumen Terkait) termasuk dalam USULAN 1 dan 3. Diubah W9: tautan Kode Aktivitas dihapus; Lint menghitung 17 butir USULAN sesudah W9 (angka 21 di paragraf atas dari sebelum W9).

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Description baris 58 mirip baris 57 tetapi tidak identik (terukur); cakupan diputus owner. Catatan pengukuran: teks di config/checklist.json tidak identik. Baris 58 lebih panjang dan menambah hal yang tidak ada di baris 57: validasi klaim produk/layanan sebelum publikasi; field produk/layanan terkait, jenis konten (baris 57 hanya channel), klaim yang perlu diverifikasi, dan sumber/bukti pendukung; serta bukti verifikasi klaim. Judul baris 58 ("Campaign & Activity") tidak dibahas Description-nya sama sekali. Spec ini mengikuti arahan orkestrator (campaign dan aktivitas, materi lewat tautan ke REG-01), sehingga pemenuhan field minimum bergantung pada REG-01. Bila owner memutus REG-02 harus memenuhi Description-nya sendiri, struktur lama (materi dan klaim langsung di tabel) harus dibuat ulang | owner ; ditutup W9: owner memutus A8 (REG-01 satu-satunya register materi, konten, dan persetujuan klaim; REG-02 hanya pelaksanaan Aktivitas). Temuan baris 58 pindah ke open item 9 |
| 2 | Penumpukan isi dengan SNX-MKT-REG-01 yang tersisa: spec REG-01 sekarang punya kolom Jenis Konten, Channel, dan Produk atau Layanan Terkait per materi (Tabel 1). Register ini masih punya kolom Jenis Konten/Channel per materi (Tabel 3) dan Produk/Layanan Terkait per campaign atau aktivitas (Tabel 1). Struktur tidak diubah di putaran sweep karena arahan melarangnya. Pilihan: hapus kolom Jenis Konten/Channel dari Tabel 3 (REG-01 sudah memuatnya lewat ID), atau pertahankan sebagai bantu baca | owner ; ditutup W9: kolom Jenis Konten/Channel (Tabel 3) dan Produk/Layanan Terkait dihapus dari REG-02 |
| 3 | Penyelarasan dokumen lane lain sudah terjadi sebagian: REG-01 (Dokumen Terkait dan Ruang Lingkup), RPT-01, dan REG-03 sudah memakai REG-02 sebagai register pelaksanaan campaign dan aktivitas. Yang belum diperiksa ulang: kalimat tiap dokumen itu tentang REG-02 terhadap batas di Ruang Lingkup register ini, termasuk kalimat REG-03 "Perencanaan dan pelaksanaan campaign dan aktivitas marketing" (register ini hanya memuat pelaksanaan; rencana ada di RPT-01) | orkestrator ; ditutup W9: kalimat tentang REG-02 di REG-01, REG-03, dan RPT-01 diselaraskan lewat A8 |
| 4 | Irisan dengan SNX-MKT-RPT-01: Aktivitas beserta jadwal mulai, selesai, PIC, dan status pelaksanaan tercatat di kedua dokumen (Tabel Aktivitas dan tabel Pelaksanaan di RPT-01; Tabel 1 dan 2 di sini). Kolom Kode Aktivitas menautkan keduanya, tetapi belum diputus mana yang menjadi induk. Nilai status juga beda (Terlaksana, Tertunda, Dibatalkan di RPT-01; Direncanakan, Berjalan, Selesai, Dibatalkan di sini), dan cakupan kata "Aktivitas" beda (asumsi 3) | owner ; ditutup W9: irisan RPT-01 diputus A8 (RPT-01 memuat rencana dan tinjauan, REG-02 pelaksanaan; Aktivitas satu arti; Dibatalkan dihitung terpisah dari belum Selesai); kolom Kode Aktivitas dihapus ; R2: istilah Aktivitas dan definisi Channel diseragamkan dengan RPT-01 |
| 5 | Rujukan butir SNX-MKT-REG-01 (4.1, 4.5, 4.8, 4.13) dan nama kolom (Tanggal Persetujuan) memakai spec Draft. Periksa ulang sesudah REG-01 final | owner ; tetap terbuka; W9 menambah rujukan REG-01 butir 4.10 sampai 4.13 (butir 4.6 baru) |
| 6 | Istilah beda antardokumen: REG-01 memakai "ID persetujuan" (kolom ID, dan kolom ID Materi di Tabel 4), register ini memakai "ID Persetujuan Materi". Belum diseragamkan karena di luar butir sweep. Bila owner memutus satu istilah, definisi, judul kolom Tabel 3, dan Cara Mengisi 6.13 diganti | owner ; tetap terbuka, diubah W9: "ID Persetujuan Materi" kini judul kolom Tabel 1 dan Cara Mengisi 6.7 (Tabel 3 dan 6.13 sudah dihapus) |
| 7 | Retensi rekaman dan jalur folder Commercial di Google Drive (USULAN 13 dan 14) belum ada keputusan tertulis | Legal, owner |
| 8 | Kolom Kode Aktivitas mengandaikan tiap aktivitas di SNX-MKT-RPT-01 punya Kode unik. Spec RPT-01 punya kolom Kode, tetapi aturan penomorannya belum diperiksa | owner ; ditutup W9: kolom Kode Aktivitas dihapus; RPT-01 menunjuk REG-02 lewat kolom Rujukan Catatan (nomor baris Tabel 1) |

## Penanganan cacat context/audit

`grep -n "Marketing Campaign & Activity " context/audit/*.md` tidak menemukan baris (nol kecocokan). Pencarian lebih longgar `grep -n -i -E "Campaign & Activity|Claims Approval|Marketing Content" context/audit/*.md` juga nol kecocokan. Berarti tidak ada bagian audit untuk dokumen ini dan tidak ada bagian 5 Catatan kualitas dan celah yang menyangkut baris 58; checklist baris 58 tidak punya fileId.

Cacat dari dokumen terdekat, dicek terhadap register ini:

| Cacat tercatat | Dokumen | Penanganan |
|---|---|---|
| Klaim Sales Playbook tidak seragam atau tanpa dasar (TCO, SLA, respons, sertifikasi) | Sales Playbook (fileId 1RVxuhUAFVTqwbtArb9uG4i2paG7Ph35w), audit commercial baris 725 sampai 735 | Tidak diperbaiki di register ini. Playbook bukan materi eksternal, dan verifikasi klaim ada di SNX-MKT-REG-01, bukan di sini. Tidak ada baris klaim yang diisi |
| Nama "Zilly" vs "Zily" | KPI COMMERCIAL & MARKETING.xlsx (fileId 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb), audit commercial baris 543 | Tidak relevan ke isi register; ejaan "Zilly Dwinata" mengikuti defaults (asumsi 11) |
| Tidak ada berkas company profile di ledger audit; slide 10 Sales Onboarding hanya merujuk company profile | audit commercial baris 346 | Company profile tetap disebut sebagai satu jenis materi (kriteria baris 58 menyebutnya). Register tidak mengasumsikan berkasnya ada |

## Jawaban dua pertanyaan sebelum selesai

**Apa yang membuat teks ini terdengar buatan AI**

1. Lima belas langkah Cara Mengisi dibuka "Brand & Marketing menulis". Itu akibat aturan satu langkah satu pelaku, tetapi terdengar seperti keluaran mesin. Dibiarkan, karena menggabungkan langkah melanggar aturan satu tindakan per langkah. Satu langkah (6.10) dipecah menjadi dua kalimat pendek agar tidak lebih dari sekitar 25 kata per kalimat.
2. Label "(USULAN)" muncul sangat sering. Itu sengaja: tiap aturan tanpa sumber memang berstatus usulan, dan label itu yang dipakai untuk daftar ACC.
3. Frasa "Yang dijaga:", "berstatus (USULAN)", dan susunan Tujuan sampai Kesimpulan mengikuti pola register T2 lain di repo. Itu konsistensi antardokumen, bukan gaya penyusun.
4. Kalimat kedua butir 4.6 ("Karena itu klaim materi ... sudah diverifikasi") terbaca sebagai kepastian, padahal turunan dari butir REG-01 yang sendiri berstatus USULAN. Diperbaiki: diberi label (USULAN).
5. Benda sebagai pelaku: "Tabel 3 menautkan tiap materi ...", "SNX-MKT-REG-01 mencatat ...", dan baris Dokumen Terkait yang dibuka "Mencatat ...". Diperbaiki menjadi "Tabel 3 memuat tautan ...", "SNX-MKT-REG-01 memuat ...", "Memuat ...", dan "Register ini ... untuk materi hanya memuat ID Persetujuan Materi".
6. Dua istilah untuk satu hal: "pihak luar" dan "pihak di luar SINUX". Diseragamkan menjadi "pihak di luar SINUX". "Campaign atau aktivitas" dipertahankan sebagai pasangan tetap dengan definisi terpisah.
7. Tidak ada em-dash, en-dash, tebal, huruf kapital penekan, tanda kutip penekan, atau penutup positif. Kesimpulan dua kalimat tanpa pujian.

**Adakah fakta, angka, nama, atau tanggal tanpa sumber**

| Butir di dokumen | Sumber atau status |
|---|---|
| Nama orang: Zilly Dwinata, Laras Rasmawati, Samuel Kristanto Utomo | Prompt dan config/defaults.json (blok Approval). Tidak ada nama lain di badan dokumen |
| Nama jabatan: Brand & Marketing, VP Commercial, Direktur Utama | SNX-HR-ORG-01 dan HR-JA-001. Penugasan Brand & Marketing sebagai pencatat dan VP Commercial sebagai pemutus tindak lanjut: USULAN 8 sampai 10 dan 15 |
| Tujuh jenis materi | Checklist baris 58 (kutipan di Fakta kunci). Nilai "Lainnya": USULAN 16 |
| Campaign, event, webinar; wewenang JA-06 menjadwalkan publikasi setelah persetujuan | HR-JA-001 JA-06 uraian 4 dan wewenang 2 (kutipan di Fakta kunci) |
| Nomor butir SNX-MKT-REG-01 (4.1, 4.5, 4.8, 4.13), status Disetujui dan Terbit, kolom Tanggal Persetujuan | Spec REG-01 yang berstatus Draft (fakta pendukung 1 sampai 4); bisa berubah (open item 5) |
| Kode Aktivitas, nama campaign sebagai kunci Campaign Asal | Spec RPT-01 dan REG-03 yang berstatus Draft (fakta pendukung 5 dan 6); open item 4 dan 8 |
| Tingkat INTERNAL | SNX-ISMS-PRO-01 (kutipan di Fakta kunci). Penerapan ke register: USULAN 12 |
| Folder Google Drive departemen Marketing | Tanpa sumber; USULAN 13 |
| Klausul ISO | Tanpa acuan di checklist; USULAN 17 dengan label konsultan |
| Angka: 10 baris, empat nilai status, empat nilai jenis | Pilihan tata letak dan isi register, bukan fakta tentang SINUX. Tidak ada angka kinerja, SLA, harga, persentase, atau tanggal dari sumber yang disalin |
| Tanggal | Nol tanggal di dokumen; effective_date kosong; tabel isian kosong |
| Retensi | Tertulis "Belum ditetapkan" atau "Mengikuti SNX-MKT-REG-01"; tidak ada angka |
| Definisi Campaign dan Aktivitas | Rumusan netral tanpa sumber persis (asumsi 4) |

Sesudah dua pertanyaan itu dijawab, teks spec diperbaiki sesuai butir 4 sampai 6, spec dirender ulang, dan lint dijalankan ulang: `"pass": true`, `"fails": []`.

## Sweep

Putaran penghalusan sesudah DONE. Batas tulis: specs/MKT-REG-02.json dan notes/MKT-REG-02.md. Sepuluh baris teks spec berubah (satu butir per baris di bawah); fakta, angka, nama, dan struktur tabel tidak berubah (meta identik, jumlah baris teks 117 sebelum dan sesudah). Sumber perbandingan: specs/MKT-REG-01.json versi sekarang dan qa/MKT-REG-02.verify.json.

| # | Letak | Sebelum | Sesudah |
|---|---|---|---|
| 1 | Tujuan, kalimat 3 | "... tersimpan di SNX-MKT-REG-01 dan ditelusuri dari register ini lewat ID itu." | "... tersimpan di lokasi yang tercatat di SNX-MKT-REG-01, dan ditelusuri dari register ini lewat ID itu." (REG-01 hanya mencatat lokasi; berkasnya di tempat lain) |
| 2 | Ketentuan 4.6 | "Approver tidak menyetujui versi yang masih memuat klaim tanpa bukti pendukung, atau klaim yang Pemverifikasi tolak (SNX-MKT-REG-01 butir 4.13)." | "... klaim tanpa sumber atau bukti pendukung, klaim tanpa hasil verifikasi, atau klaim yang Pemverifikasi tolak (SNX-MKT-REG-01 butir 4.13)." Kalimat kedua (turunan, berlabel USULAN) tidak berubah dan kini sah karena frasa "klaim tanpa hasil verifikasi" ada di REG-01 4.13 |
| 3 | Rekaman, baris 1 | "Folder Google Drive departemen Marketing. Pemilik: ..." | "Folder Google Drive departemen Commercial; jalur folder belum ditetapkan. Pemilik: ..." Diselaraskan dengan REG-01 dan unit JA-06 (Commercial). Keputusan tetap USULAN 13, pemutus owner |
| 4 | Ruang Lingkup, paragraf 2 | "Batas dengan SNX-MKT-REG-01 (USULAN): SNX-MKT-REG-01 memuat tiap versi materi eksternal, yaitu nama materi, channel, ... serta klaim dan bukti pendukungnya. Register ini mencatat campaign dan aktivitas ... untuk materi hanya memuat ID Persetujuan Materi ..." | "Batas dokumen Marketing (USULAN, pemutus owner):" empat kalimat, satu per dokumen: RPT-01 = rencana pemasaran dan tinjauan kinerja (sasaran, audiens, positioning, channel, rencana aktivitas, KPI, realisasi, evaluasi, tindakan korektif); REG-01 = persetujuan materi eksternal dan validasi klaim; register ini = pelaksanaan campaign dan aktivitas beserta tautan ke ID persetujuan di REG-01; REG-03 = hasil lead dan serah terima ke Sales, merujuk nama campaign di register ini |
| 5 | Ruang Lingkup, pengecualian baris 2 | "Persetujuan materi dan verifikasi klaim \| Dicatat di SNX-MKT-REG-01. Register ini hanya menautkannya (USULAN)." | "Persetujuan materi eksternal dan validasi klaim \| Dicatat di SNX-MKT-REG-01. Register ini hanya memuat tautan ke ID persetujuan di sana (USULAN)." |
| 6 | Ruang Lingkup, pengecualian baris 4 | "Rencana, anggaran, target, dan evaluasi hasil marketing \| Dicatat di SNX-MKT-RPT-01 (USULAN)." | "Rencana pemasaran dan tinjauan kinerja: sasaran, audiens, positioning, channel, rencana aktivitas, KPI, realisasi, evaluasi, dan tindakan korektif \| Dicatat di SNX-MKT-RPT-01 (USULAN)." Kata "anggaran" dan "target" dihapus karena tidak ada di batas yang diputus orkestrator |
| 7 | Ruang Lingkup, pengecualian baris 5 | "Serah terima lead kepada Sales dan hasil campaign berupa lead \| Dicatat di SNX-MKT-REG-03 (USULAN)." | "Hasil lead dan serah terima ke Sales \| Dicatat di SNX-MKT-REG-03, yang merujuk nama campaign di Tabel 1 register ini (USULAN)." |
| 8 | Dokumen Terkait, SNX-MKT-REG-01 | "Memuat persetujuan tiap versi materi eksternal dan verifikasi klaimnya. ... tautan materi ... ke ID Persetujuan Materi di sana (USULAN)." | "Memuat persetujuan materi eksternal dan validasi klaim. Register ini memuat tautan tiap materi yang dipakai campaign dan aktivitas ke ID persetujuan di sana (USULAN)." |
| 9 | Dokumen Terkait, SNX-MKT-REG-03 | "Memuat hasil marketing yang diteruskan kepada Sales, yang dikecualikan ..." | "Memuat hasil lead dan serah terima ke Sales, yang dikecualikan dari register ini. Kolom Campaign Asal di sana merujuk nama campaign di Tabel 1 register ini (USULAN)." |
| 10 | Dokumen Terkait, SNX-MKT-RPT-01 | "Memuat rencana, anggaran, target, dan evaluasi hasil marketing, yang dikecualikan ..." | "Memuat rencana pemasaran dan tinjauan kinerja, yang dikecualikan dari register ini. Kolom Kode Aktivitas di Tabel 2 memuat tautan ke aktivitas di sana (USULAN)." |

Butir sweep 1 "open item 2-3 notes basi": open item 2 dan 3 ditulis ulang (kolom REG-01 sudah ada; penyelarasan dokumen lain sudah sebagian). Open item 6 dan 7, asumsi 5, USULAN 13, dan empat baris tabel pemetaan kriteria ikut diperbarui karena memuat klaim basi yang sama.

Tidak diubah karena di luar butir sweep, menunggu keputusan orkestrator (temuan nonblocking pemeriksa di qa/MKT-REG-02.verify.json):
- Tabel Peran, baris Brand & Marketing: rujukan butir tidak memuat 4.8, padahal sel itu menyebut menghentikan pemakaian materi tanpa persetujuan.
- Ketentuan 4.7 dan 4.8: tidak ada pemicu pengecekan ulang bila baris REG-01 berubah menjadi Ditarik saat campaign masih Berjalan.
- Cara Mengisi 6.11 dan 6.12 dan Tabel 3: jenis konten dan channel satu sel, dan "bila materi punya channel" tidak sejalan dengan REG-01 butir 4.1 (satu baris satu channel). Terkait open item 2.
- Istilah "ID Persetujuan Materi" lawan "ID persetujuan" (open item 6).
- Pasangan "campaign atau aktivitas" yang berat di 24 baris, dua pasif tanpa pelaku, dan satu pergeseran makna di pengecualian materi internal ("dipakai pihak di luar SINUX" maksudnya "dipakai untuk pihak di luar SINUX").

Uji sesudah sweep (semua dijalankan pada spec versi sweep):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-REG-02.json /tmp/pen-MKT-REG-02/MKT-REG-02.docx`: selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-02/MKT-REG-02.docx generic`: `"pass": true`, `"fails": []`, satu warn "20 butir (USULAN) menunggu ACC".
- `python3 /mnt/skills/public/docx/scripts/office/validate.py /tmp/pen-MKT-REG-02/MKT-REG-02.docx`: "All validations PASSED!" (386 paragraf).
- `python3 -I reports/orch/blankscan.py /tmp/pen-MKT-REG-02/MKT-REG-02.docx`: `ok 11 MKT-REG-02.docx []` (nol halaman kosong).
- Skrip kecil: 7 kode SNX di badan, nol kurang, nol berlebih di Dokumen Terkait; nol em-dash dan en-dash.

## ISO-W9

Putaran ISO-W9 (LEAD G-3 A8, B2; owner GO). Batas tulis: specs/MKT-REG-02.json dan notes/MKT-REG-02.md. Meta dan blok approval tidak berubah (sudah sama dengan defaults v22 MKT). Rujukan silang yang diubah ada di baris tabel di bawah; nomor butir REG-01 yang dirujuk (4.1, 4.5, 4.8, 4.10 sampai 4.13) ada dan cocok isinya di spec REG-01.

| Butir | Sebelum | Sesudah |
|---|---|---|
| Tujuan kalimat 1 | pelaksanaan campaign dan aktivitas, satu baris per campaign atau aktivitas, beserta materi eksternal | pelaksanaan Aktivitas, satu baris per Aktivitas: nama, tujuan, Channel, jadwal, PIC, Budget, status, ID Persetujuan Materi, hasil singkat |
| Tujuan kalimat 2 | persetujuan dan verifikasi klaim | REG-01 disebut satu-satunya register materi, konten, dan persetujuan klaim; persetujuan dan validasi klaim |
| Ruang Lingkup paragraf 1 | campaign dan aktivitas beserta materi eksternal yang dipakainya | Aktivitas; untuk materi eksternal register ini hanya memuat ID Persetujuan Materi |
| Ruang Lingkup paragraf 2 | "Batas dokumen Marketing (USULAN, pemutus owner)": REG-01 memuat persetujuan; register ini memuat tautan materi | label USULAN dihapus (batas sudah diputus); RPT-01 diisi dari REG-02 dan REG-03; REG-01 satu-satunya register materi, konten, persetujuan klaim; REG-02 hanya pelaksanaan Aktivitas dengan ID Persetujuan Materi |
| Pengecualian baris 2 | "hanya memuat tautan ke ID persetujuan di sana (USULAN)" | "satu-satunya register materi, konten, dan persetujuan klaim ... hanya memuat ID Persetujuan Materi dari sana" |
| Pengecualian baris 4 dan 5 | label (USULAN) pada RPT-01 dan REG-03; "nama campaign" | label dihapus; REG-03 merujuk nama Aktivitas lewat kolom Campaign Asal |
| Definisi Aktivitas | kegiatan di luar campaign saja | campaign, atau kegiatan di luar campaign; satu Aktivitas = satu baris Tabel 1 (kata sama dengan RPT-01) |
| Definisi Budget | tidak ada | baris baru, sama dengan RPT-01 |
| Definisi Channel dan PIC | materi tampil; "campaign atau aktivitas" | Channel sebuah Aktivitas (sama dengan RPT-01); PIC satu Aktivitas |
| 3.1 judul dan intro | Status Campaign atau Aktivitas | Status Aktivitas; Direncanakan atau Berjalan = belum Selesai; Dibatalkan dihitung terpisah dari belum Selesai |
| 3.1 nilai status (4 baris) | "Campaign atau aktivitas ..." | "Aktivitas ..." |
| 4.1 | Tabel 1, 2, dan 3 | Tabel 1 dan 2 |
| 4.2 sampai 4.3 | campaign atau aktivitas | Aktivitas |
| 4.4 | mencatat materi di Tabel 3 | menulis ID Persetujuan Materi di Tabel 1; register tidak memuat nama, jenis, versi, klaim, atau persetujuan materi |
| 4.6 | Approver tidak menyetujui versi dengan klaim tanpa bukti ... klaim sudah diverifikasi (USULAN) | Brand & Marketing menelusuri persetujuan dan validasi klaim di REG-01 lewat ID; register tidak mencatat klaim (REG-01 butir 4.10 sampai 4.13) |
| 4.7 | menulis tanggal pengecekan di Tabel 3 | tanggal pengecekan dihapus |
| 4.9 | baris baru di Tabel 3 | ID versi baru ditambah di Tabel 1; ID lama tidak dihapus |
| Peran Brand & Marketing | PIC campaign atau aktivitas; mencatat materi di Tabel 3 | PIC Aktivitas; menulis ID Persetujuan Materi di Tabel 1 |
| Cara Mengisi | 6.1 sampai 6.15 (Jenis, Produk/Layanan, Kode Aktivitas, 6.10 sampai 6.14 untuk Tabel 3) | 6.1 sampai 6.12: tambah Tujuan (6.3), Channel (6.4), Budget (6.6), ID Persetujuan Materi (6.7), Hasil Singkat (6.11); hapus Jenis, Produk/Layanan, Kode Aktivitas, kolom materi |
| Tabel 1 | No, Nama Campaign atau Aktivitas, Jenis, Produk/Layanan Terkait, PIC | No, Nama Aktivitas, Tujuan, Channel, PIC, Budget, ID Persetujuan Materi (SNX-MKT-REG-01) |
| Tabel 2 | No, Tanggal Mulai, Tanggal Selesai, Status, Kode Aktivitas | No, Tanggal Mulai, Tanggal Selesai, Status, Hasil Singkat |
| Tabel 3 | Materi yang Dipakai (5 kolom) | dihapus |
| Isi Register intro | ketiga tabel; Tabel 1 sampai Tabel 3 | kedua tabel; Tabel 1 dan Tabel 2 |
| Rekaman dan Acuan ISO | Tabel 1 sampai Tabel 3; 8.2.1 dan 8.2.2 merujuk Tabel 3 | Tabel 1 dan Tabel 2; merujuk Tabel 1 |
| Dokumen Terkait REG-01, REG-03, RPT-01 | tautan materi; Kode Aktivitas; label USULAN | ID Persetujuan Materi; RPT-01 diisi lewat Rujukan Catatan di tabel B2; label USULAN pada batas dihapus |

Open item yang ditutup atau diubah W9: lihat kolom Pemutus pada tabel Open items (status ditambah di baris lama, tidak ada baris dihapus). Open item baru:

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 9 | Description checklist baris 58 berisi pengendalian materi baris 57 yang diperluas dengan validasi klaim, bukan pelaksanaan campaign sesuai judulnya (Marketing Campaign & Activity Register); perlu dibetulkan Brand & Marketing. Pengukuran: teks baris 58 tidak identik dengan baris 57. | Brand & Marketing |
| 10 | Kolom Jenis dihapus (tidak ada di daftar A8), sehingga campaign, event, dan webinar tidak dibedakan di Tabel 1. REG-03 kolom Campaign Asal kini menerima nama Aktivitas apa pun di Tabel 1. Bila perlu pembeda, owner menambah kolom | owner |
| 11 | Kolom "anggaran bila ada" dari A8 ditulis Budget (istilah RPT-01) dengan nilai Tidak Ada Budget untuk Aktivitas tanpa dana (USULAN 6.6). Kolom Tujuan, Hasil Singkat, dan pemisah koma pada ID Persetujuan Materi juga USULAN | owner |
| 12 | A3 (garis lapor JA-03 dan JA-04): dokumen ini tidak menyebut atasan atau garis lapor keduanya, jadi tidak ada yang diselaraskan. Kalimat "atasan langsung Brand & Marketing" menyangkut JA-06 dan tidak berubah | - |

Uji (spec W9): `python3 -I tools/render_sop.py ...`, `python3 -I tools/lint_doc.py ... generic`: pass true, fails kosong, 17 butir USULAN; `validate.py`: All validations PASSED; `blankscan.py`: ok 11 halaman []; `python3 -I reports/orch/w9diff.py MKT-REG-02`: diff hanya baris di tabel di atas.

### ISO-W9 R2

| Butir | Sebelum | Sesudah |
|---|---|---|
| R2 butir 1, Peran Brand & Marketing | "(butir 4.2 sampai 4.5, 4.7, 4.9, dan 4.11)" | "(butir 4.2 sampai 4.7, 4.9, dan 4.11)"; butir 4.6 ditambah karena Brand & Marketing menelusuri persetujuan dan validasi klaim di REG-01 |
| R2 butir 2, definisi Channel | "Tempat sebuah Aktivitas menampilkan atau membagikan materi kepada pihak di luar SINUX, ..." | "Tempat materi Aktivitas ditampilkan atau dibagikan Brand & Marketing kepada pihak di luar SINUX, ..."; identik dengan SNX-MKT-RPT-01 |
| R2 butir 2, Cara Mengisi 6.4 | "satu channel atau lebih tempat Aktivitas menampilkan atau membagikan materi di kolom Channel" | "satu channel atau lebih tempat materi Aktivitas ditampilkan atau dibagikan di kolom Channel" |

Hygiene R2 butir 4: baris USULAN 1 sampai 6, 8, 9, 11, 16, 17 dan Open items 4 kini memuat "diubah W9" atau "ditutup W9" di barisnya sendiri; hitungan label USULAN dikoreksi.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
- Butir 6.7 asli: "6.7 Brand & Marketing menulis nomor baris materi dari Tabel 1 SNX-MKT-REG-01 di kolom ID Persetujuan Materi (butir 4.4, 4.5, 4.7, dan 4.9). Bila Aktivitas memakai lebih dari satu materi, Brand & Marketing memisahkan nomornya dengan koma (USULAN)." Label dihapus karena instruksi pengisian mekanis (pemisah koma), STYLE §3.6. Selisih usul_butir 6.7 berasal dari penghapusan ini.
### W10 kalimat dihapus atau dipindah
- Tabel Peran, Brand & Marketing: "(butir 4.2 sampai 4.7, 4.9, dan 4.11)" dihapus; "Tugas mengelola event, webinar, dan campaign ada di uraian JA-06 butir 4." ditulis sebagai fakta: "Mengelola event, webinar, dan campaign sesuai uraian JA-06 butir 4."
- Tabel Peran, VP Commercial: "(butir 4.8)" dan "(bagian Isi Register)" dihapus.
- Peran, paragraf pembuka: "Pembagian tugas berikut berstatus (USULAN)." dipindah ke akhir paragraf; "bukan di register ini" dihapus (sudah tersirat).
- Cara Mengisi: "(butir 4.1 dan 4.2)" di 6.1 dan "(butir 4.3)" di 6.2 dihapus (6.2 kini memuat faktanya: ejaan yang tetap); di 6.7 rujukan dipadatkan menjadi "(butir 4.4)".
- Rekaman, register: "Klasifikasi menurut butir 4.10." ditulis faktanya: "Klasifikasi: INTERNAL (butir 4.10)."
### W10 selisih angka
- usul_butir "6.7": label (USULAN) mekanis dihapus, lihat W10 label dihapus.
### W10 catatan
- Pihak luar: "customer" (satu-satunya sebutan di dokumen ini).
- "Aktivitas" dipakai dalam satu arti (definisi di bagian Definisi); "rencana aktivitas" di daftar isi SNX-MKT-RPT-01 ditulis "rencana Aktivitas". Status Dibatalkan tetap dihitung terpisah dari belum Selesai (G-3 A8).
- Istilah Marketing English: claim (jembatan "claim (klaim)" di Tujuan), content, campaign, lead; "Record (rekaman)" di butir 4.11.
- Butir 4.4, 4.5, 4.10 disusun ulang agar satu label (USULAN) di akhir butir tetap menempel pada kalimat yang berstatus usulan.
- Lebar kolom Tabel 1 diatur ulang (ID Persetujuan Materi 3,0 cm) dan baris isian min_row_cm 0.8; halaman 11 dan ISI halaman 8 tetap.

### W10 putaran perbaikan 1 (worker, temuan qa/MKT-REG-02.w10.r1.json)
- "6.2 Di kolom Nama Aktivitas, tulis nama Aktivitas dengan ejaan yang tetap." ditambah label (USULAN) di akhir: fakta ini menggantikan rujukan ke butir berlabel (USULAN) (usul_butir 6.2).
