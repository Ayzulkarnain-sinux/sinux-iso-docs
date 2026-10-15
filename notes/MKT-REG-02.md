# Catatan penyusun MKT-REG-02: Marketing Campaign & Activity Register

Status: DRAFTED (spec + notes ada). Spec: specs/MKT-REG-02.json. Mode generic (doc_type_cover "REGISTER", doc_type_label "Register"), aksi T2, wave W7, nomor SNX-MKT-REG-02 (nomor SNX lama dipertahankan), department Marketing, classification INTERNAL (worklist), audit_class None, review_period YEARLY, status Draft, revision 00, effective_date kosong, revision_desc "Draft awal untuk review dan pengesahan". Approval persis dari prompt: prepared "Zilly Dwinata / Brand & Marketing", reviewed "Laras Rasmawati / VP Commercial", approved "Samuel Kristanto Utomo / President Director". process_owner "VP Commercial": dokumen tanpa sumber memakai jabatan reviewer departemen, tanpa nama. Catatan worklist: kosong.

Perubahan cakupan di tengah penyusunan: draf pertama saya adalah register materi dan klaim (11 field minimum langsung di tabel). Orkestrator memutus sebaliknya: baris 58 tidak boleh menjadi register kedua untuk materi dan klaim, sebab SNX-MKT-REG-01 sudah memuatnya. Spec ditulis ulang sebagai register pelaksanaan campaign dan aktivitas: satu baris per campaign atau aktivitas, dengan kolom yang menautkan tiap materi eksternal ke ID Persetujuan Materi di SNX-MKT-REG-01. Semua angka uji di bawah berasal dari spec versi kedua ini. Versi pertama dibuang, tidak ada sisanya di repo.

Uji terakhir (spec versi kedua):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/MKT-REG-02.json /tmp/pen-MKT-REG-02/MKT-REG-02.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-MKT-REG-02/MKT-REG-02.docx generic` memberi `"pass": true`, `"fails": []`, satu warn: "21 butir (USULAN) menunggu ACC".
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
| Jenis konten/channel | Tabel 3 kolom Jenis Konten/Channel | Tabel 1 kolom Channel |
| Produk/layanan terkait | Tabel 1 kolom Produk/Layanan Terkait, pada tingkat campaign atau aktivitas | tidak ada kolom ini di spec REG-01 saat ini (lihat open item 2) |
| Versi | tidak ada | Tabel 1 kolom Versi |
| Klaim yang perlu diverifikasi; sumber/bukti pendukung | tidak ada | Tabel 4 kolom Klaim dan Bukti Pendukung |
| PIC | Tabel 1 kolom PIC (PIC campaign atau aktivitas) | Tabel 2 kolom PIC (PIC materi) |
| Reviewer/approver; tanggal persetujuan | tidak ada; Tabel 3 kolom Tanggal Pengecekan Persetujuan mencatat kapan Brand & Marketing mengecek baris itu | Tabel 2 kolom Reviewer, Approver, Tanggal Persetujuan |
| Status publikasi | tidak ada | Tabel 3 kolom Status Publikasi |
| Lokasi file final | tidak ada | Tabel 1 kolom Lokasi File Final |
| Bukti: materi final yang telah disetujui; bukti verifikasi klaim yang relevan; catatan persetujuan sebelum dipublikasikan | Tujuan kalimat 3; Rekaman baris 2 (lokasi dan pemilik mengikuti REG-01) | Lokasi File Final; Tabel 4; kolom Bukti Persetujuan |
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
5. ID Persetujuan Materi dibaca sebagai nomor baris Tabel 1 SNX-MKT-REG-01, karena spec REG-01 saat ini tidak punya kolom ID atau kode tersendiri. Bila REG-01 menambah kode, definisi di register ini diganti (open item 6).
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
| 1 | Struktur kolom dan tiga tabel, termasuk kolom di luar kriteria: Nama Campaign atau Aktivitas, Jenis, Tanggal Mulai, Tanggal Selesai, Status, Kode Aktivitas, No Campaign atau Aktivitas, ID Persetujuan Materi, Tanggal Pengecekan Persetujuan; ukuran awal 10 baris | Isi Register; Peran (VP Commercial menetapkan struktur) | owner |
| 2 | Batas cakupan REG-01 lawan REG-02: REG-01 memuat tiap versi materi beserta klaimnya, register ini memuat campaign dan aktivitas yang memakai materi dan hanya ID Persetujuan Materi | Ruang Lingkup paragraf 2 | owner |
| 3 | Pengecualian: persetujuan materi dan verifikasi klaim ke SNX-MKT-REG-01; rencana, anggaran, target, dan evaluasi hasil ke SNX-MKT-RPT-01; serah terima lead dan hasil campaign berupa lead ke SNX-MKT-REG-03 | Ruang Lingkup tabel; Dokumen Terkait | owner |
| 4 | Brand & Marketing mencatat campaign atau aktivitas di Tabel 1 sebelum dijalankan | Ketentuan 4.2 | owner |
| 5 | Nama campaign atau aktivitas ditulis dengan satu ejaan tetap, dan SNX-MKT-REG-03 merujuknya di kolom Campaign Asal | Ketentuan 4.3; Dokumen Terkait | owner |
| 6 | Brand & Marketing mencatat tiap materi yang dipakai di Tabel 3 dengan ID Persetujuan Materi | Ketentuan 4.4; Cara Mengisi 6.10, 6.13 | owner |
| 7 | Materi dipakai hanya bila baris REG-01 berstatus Disetujui atau Terbit dan Tanggal Persetujuan terisi (kalimat 2 dari 4.5, wewenang JA-06 untuk menjadwalkan publikasi setelah persetujuan, bersumber) | Ketentuan 4.5 kalimat 1 | owner |
| 8 | Klaim materi sudah diverifikasi saat baris REG-01 Disetujui atau Terbit (turunan dari REG-01 butir 4.13, yang berstatus USULAN di dokumen itu) | Ketentuan 4.6 kalimat 2 | owner |
| 9 | Brand & Marketing mengecek baris REG-01 sebelum materi dipakai dan menulis tanggal pengecekan | Ketentuan 4.7; Cara Mengisi 6.14 | owner |
| 10 | Materi yang ternyata dipakai tanpa persetujuan: Brand & Marketing menghentikan pemakaian dan melapor, VP Commercial memutuskan tindak lanjut | Ketentuan 4.8 | owner |
| 11 | Beralih ke versi baru = baris baru di Tabel 3 sesudah versi itu Disetujui, baris lama tidak dihapus | Ketentuan 4.9 | owner |
| 12 | Register berklasifikasi INTERNAL | Ketentuan 4.10; Acuan ISO | owner |
| 13 | Folder Google Drive departemen Marketing sebagai lokasi simpan; pemilik VP Commercial; pencatat Brand & Marketing | Ketentuan 4.11; Rekaman baris 1 | owner |
| 14 | Retensi register: "Belum ditetapkan", tanpa angka; retensi materi, bukti, dan catatan persetujuan "Mengikuti SNX-MKT-REG-01" | Rekaman | Legal |
| 15 | Pembagian tugas Brand & Marketing dan VP Commercial; VP Commercial sebagai pemilik register (process_owner); tinjauan tahunan oleh VP Commercial | Peran; Kesimpulan; meta process_owner | owner |
| 16 | Nilai kolom Jenis (Campaign, Event, Webinar, Lainnya) dan nilai kolom Status (empat nilai) | Cara Mengisi 6.3, 6.8; Definisi Status Campaign atau Aktivitas | owner |
| 17 | Lima klausul acuan: ISO 9001:2015 7.4, 8.2.1, 8.2.2, 7.5.3; ISO/IEC 27001:2022 Annex A 5.12. Satu label "(USULAN, perlu konfirmasi konsultan)". Klausul 8.2.2 dipilih karena memuat kewajiban memastikan SINUX dapat memenuhi klaim produk dan layanan yang ditawarkan; di register ini kaitannya lewat tautan ke REG-01 | Acuan ISO | owner (lewat konsultan) |

Tautan Kode Aktivitas ke SNX-MKT-RPT-01 (Tabel 2, Cara Mengisi 6.9, Dokumen Terkait) termasuk dalam USULAN 1 dan 3.

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Description baris 58 identik dengan baris 57; cakupan diputus owner. Catatan pengukuran: teks di config/checklist.json tidak identik. Baris 58 lebih panjang dan menambah hal yang tidak ada di baris 57: validasi klaim produk/layanan sebelum publikasi; field produk/layanan terkait, jenis konten (baris 57 hanya channel), klaim yang perlu diverifikasi, dan sumber/bukti pendukung; serta bukti verifikasi klaim. Judul baris 58 ("Campaign & Activity") tidak dibahas Description-nya sama sekali. Spec ini mengikuti arahan orkestrator (campaign dan aktivitas, materi lewat tautan ke REG-01), sehingga pemenuhan field minimum bergantung pada REG-01. Bila owner memutus REG-02 harus memenuhi Description-nya sendiri, struktur lama (materi dan klaim langsung di tabel) harus dibuat ulang | owner |
| 2 | Spec SNX-MKT-REG-01 saat ini tidak punya kolom Produk/Layanan Terkait dan tidak punya kolom jenis konten (hanya Channel). Register ini memuat produk/layanan pada tingkat campaign atau aktivitas (Tabel 1) dan jenis konten per materi (Tabel 3). Bila produk/layanan harus tercatat per materi, kolomnya ditambah di REG-01 | owner |
| 3 | Dokumen lane lain masih menggambarkan REG-02 dengan cakupan lama dan perlu disesuaikan oleh orkestrator (di luar batas tulis saya): specs/MKT-REG-01.json bagian Dokumen Terkait, baris SNX-MKT-REG-02 ("Register materi pemasaran yang beririsan dengan register ini"); specs/MKT-RPT-01.json bagian Ruang Lingkup, baris pengecualian pertama ("Ada di SNX-MKT-REG-01 dan SNX-MKT-REG-02 ... persetujuan materi eksternal ... validasi klaim"), dan bagian Dokumen Terkait baris SNX-MKT-REG-02; specs/MKT-REG-03.json bagian Ruang Lingkup menulis "Perencanaan dan pelaksanaan campaign dan aktivitas marketing" sebagai lingkup REG-02, padahal register ini memuat pelaksanaan saja dan rencana ada di SNX-MKT-RPT-01 | orkestrator, owner |
| 4 | Irisan dengan SNX-MKT-RPT-01: Aktivitas beserta jadwal mulai, selesai, PIC, dan status pelaksanaan tercatat di kedua dokumen (Tabel Aktivitas dan tabel Pelaksanaan di RPT-01; Tabel 1 dan 2 di sini). Kolom Kode Aktivitas menautkan keduanya, tetapi belum diputus mana yang menjadi induk. Nilai status juga beda (Terlaksana, Tertunda, Dibatalkan di RPT-01; Direncanakan, Berjalan, Selesai, Dibatalkan di sini), dan cakupan kata "Aktivitas" beda (asumsi 3) | owner |
| 5 | Rujukan butir SNX-MKT-REG-01 (4.1, 4.5, 4.8, 4.13) dan nama kolom (Tanggal Persetujuan) memakai spec Draft. Periksa ulang sesudah REG-01 final | owner |
| 6 | ID Persetujuan Materi dibaca sebagai nomor baris Tabel 1 REG-01 (asumsi 5). Bila REG-01 memberi kode atau ID tersendiri, definisi dan judul kolom Tabel 3 diganti | owner |
| 7 | Retensi rekaman dan lokasi folder Marketing di Google Drive (USULAN 13 dan 14) belum ada keputusan tertulis | Legal, owner |
| 8 | Kolom Kode Aktivitas mengandaikan tiap aktivitas di SNX-MKT-RPT-01 punya Kode unik. Spec RPT-01 punya kolom Kode, tetapi aturan penomorannya belum diperiksa | owner |

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
