# Catatan penyusun OPS-FRM-10: Root Cause Analysis & Corrective Action Report

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-FRM-10.json. Mode generic, aksi T1, wave W5, nomor SNX-OPS-FRM-10 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; isi RCA memuat data pelanggan), audit_class C1. Approval persis dari prompt dan config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. process_owner "Head of Operation" (jabatan tanpa nama, dari "Pemilik dokumen" sumber). status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Hasil uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-FRM-10.json /tmp/pen-OPS-FRM-10/OPS-FRM-10.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-OPS-FRM-10/OPS-FRM-10.docx generic` memberi `"pass": true`, `"fails": []`, satu warn "9 butir (USULAN) menunggu ACC". Validator OOXML skill docx atas hasil render: "All validations PASSED!". PDF hasil soffice 12 halaman, dilihat sebagai montase. tools/selftest.sh tidak saya jalankan (menulis ke /tmp/selftest yang dipakai bersama penyusun paralel); berkas tools dan template tidak saya ubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-10_RCA_Corrective_Action_Report.docx (140695 byte, berkas docx di Drive) | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS | 2026-10-13T06:09:03Z (get_file_metadata hari ini, cocok dengan prompt; fileSize 140695 cocok dengan hasil dekode) | read_file_content (teks penuh), download_file_content (didekode ke /tmp/pen-OPS-FRM-10/src.docx; zip dibuka dengan python3 -I; header, footer, comments, footnotes dibaca; gambar word/media/rId21.png dibuka) |
| Kriteria penerimaan | config/checklist.json baris dengan Description "SNX-OPS-FRM-10_RCA_Corrective_Action_Report.docx" | Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "10.2" dan ISO/IEC 27001:2022 "5.27" (dari prompt) |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, bagian SNX-OPS-FRM-10 (dari baris 2756, bagian 5 "Catatan kualitas dan celah") | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir dicocokkan ulang ke docx dan gambar |
| Pendukung (bahan, bukan sumber utama) | SNX-OPS-SOP-04 (Bagian 4, 5, 6, 7.5), SNX-OPS-SOP-05 (Bagian 4, 6.6, 7), SNX-OPS-FRM-09, SNX-OPS-FRM-08, SNX-OPS-FRM-04, SNX-OPS-SOP-02, SNX-ISMS-FRM-02, SNX-ISMS-REG-02 | salinan audit | Dibaca dari context/audit, bukan dari Drive terbaru; kutipan bisa basi bila tim sudah mengubah dokumen itu. Dipakai untuk definisi istilah, rujukan bagian, dan judul dokumen terkait |

Isi sumber: form kosong. Semua isian berupa sel kosong atau petunjuk dalam kurung siku; tidak ada data insiden nyata. Header dan footer hanya memuat nama PT, nomor, label RESTRICTED (Internal), dan judul. comments.xml dan footnotes.xml kosong.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | RCA wajib untuk empat pemicu dan dikirim ke pelanggan dalam batas waktu; tenggat 2 hari kerja berlaku untuk RCA insiden | "Template ini wajib untuk insiden P1 dan P2, insiden berulang, breach SLA, dan ketidaksesuaian audit, sesuai SNX-OPS-SOP-04 Bagian 7.5 dan ISO 9001 klausul 10.2. RCA insiden dikirim ke pelanggan via email paling lambat 2 hari kerja setelah layanan pulih." | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |
| 2 | Pemilik dokumen Head of Operation; acuan ISO 10.2 dan Annex A 5.27; retensi 5 tahun | "Pemilik dokumen \| Head of Operation"; "Acuan ISO 9001:2015 \| Klausul 10.2"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 5.27"; "Masa simpan record \| 5 tahun" | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |
| 3 | RCA ditutup hanya setelah tindakan terbukti efektif; urutan gambar menaruh "Setujui dan kirim" sebelum "Laksanakan tindakan" dan "Tindakan efektif?" | Judul gambar: "RCA ditutup hanya setelah tindakan terbukti efektif"; kotak: "Setujui dan kirim" dengan sub-label "Head of Operation, maksimal 2 hari kerja"; kotak "Tindakan lanjutan" dengan sub-label "kembali ke analisis" (word/media/rId21.png) | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |

## 2. Fakta penting lain dan kutipan verbatim

| # | Fakta di dokumen | Kutipan verbatim | Sumber (fileId) dan posisi |
|---|---|---|---|
| 1 | Insiden keamanan informasi juga dicatat di SNX-ISMS-FRM-02; fokus pada sistem dan proses | "Fokus pada sistem dan proses, bukan menyalahkan orang. Insiden keamanan informasi juga dicatat di SNX-ISMS-FRM-02." | 1XFMQDye..., Petunjuk pengisian |
| 2 | Sumber RCA di Bagian 1 | "[ ] Insiden · [ ] Breach SLA · [ ] Temuan audit · [ ] Keluhan pelanggan · [ ] Lainnya" | 1XFMQDye..., Bagian 1 |
| 3 | Referensi nomor | "[nomor tiket FRM-08, CR FRM-04, atau temuan audit]" | 1XFMQDye..., Bagian 1 |
| 4 | Dampak ke SLA | "[menit downtime yang dihitung, sisa anggaran]" | 1XFMQDye..., Bagian 3 |
| 5 | Metode analisis dan enam kategori fishbone | "Metode: [ ] 5 Why · [ ] Fishbone (Ishikawa) · [ ] Lainnya: [sebutkan]"; kategori "Manusia", "Proses atau prosedur", "Teknologi atau sistem", "Supplier atau pihak ketiga", "Lingkungan", "Pengukuran atau monitoring" | 1XFMQDye..., Bagian 5 |
| 6 | Tiga jenis tindakan | "Koreksi (memulihkan)", "Korektif (menghilangkan akar)", "Preventif (mencegah di tempat lain)" | 1XFMQDye..., Bagian 6 |
| 7 | Tindakan mengubah production lewat SOP-02; risiko baru ke REG-02 | "Tindakan yang mengubah production dijalankan melalui SNX-OPS-SOP-02. Risiko baru yang ditemukan ditambahkan ke SNX-ISMS-REG-02." | 1XFMQDye..., Bagian 6 |
| 8 | Kriteria efektif hanya contoh | "[misalnya tidak berulang dalam 90 hari, alert baru terbukti menangkap gejala]" | 1XFMQDye..., Bagian 7 |
| 9 | Komunikasi, termasuk rujukan jalur internal yang dibuang | "Lessons learned disetor ke knowledge base \| [nomor packet staging]" | 1XFMQDye..., Bagian 8 |
| 10 | Persetujuan RCA dan Pengesahan dokumen | "Disusun (Lead NOC atau Lead SOC)", "Disetujui (Head of Operation)"; Pengesahan: "Head of Operation", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | 1XFMQDye..., Bagian 9 dan Pengesahan |
| 11 | Dua baris riwayat revisi 00 | "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | 1XFMQDye..., Riwayat revisi |
| 12 | Insiden berulang (bukan dari FRM-10, dari SOP-04 salinan audit) | "Insiden berulang (3 kali atau lebih pada layanan yang sama dalam 30 hari) diperlakukan sebagai problem dan wajib RCA walau severity rendah." | SOP-04 Bagian 7.5 butir 3, 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG (salinan audit) |
| 13 | Definisi insiden | "Gangguan tidak terencana atau penurunan mutu layanan" | SOP-04 Bagian 4, 1p9vcA1Sj6xHIbpuIS1Lb8uBTisv2WeuG (salinan audit) |
| 14 | Definisi breach dan downtime yang dihitung; breach dianalisis dengan FRM-10 | "Pencapaian di bawah target kontrak dalam satu periode"; "Waktu layanan tidak tersedia, tidak termasuk window maintenance yang sudah dinotifikasi dan gangguan di luar tanggung jawab SINUX sesuai kontrak"; "Breach dicatat di SNX-OPS-FRM-09 dan dianalisis dengan SNX-OPS-FRM-10." | SOP-05 Bagian 4 dan 6.6, 1S4RFEDaTYU9mZYWjHHbYBfo8SRgBAq9- (salinan audit) |
| 15 | Sisa anggaran | "sisa anggaran = anggaran dikurangi downtime dihitung" | SNX-OPS-FRM-09, 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF (salinan audit) |
| 16 | Peran RCA di SOP-04 | "Lead NOC \| Pemilik SOP; eskalasi teknis kedua; menyusun RCA P1 dan P2"; "Service Delivery Manager \| Komunikasi formal ke pelanggan untuk P1 dan P2; memastikan RCA terkirim" | SOP-04 Bagian 5 (salinan audit) |
| 17 | Head of Operation menetapkan tindakan breach; RCA breach retensi 5 tahun | "Head of Operation menetapkan tindakan perbaikan beserta pemilik dan tenggat."; "RCA untuk breach \| SNX-OPS-FRM-10 \| 5 tahun" | SOP-05 Bagian 6.6 dan 7 (salinan audit) |

## 3. Isi spec (apa yang diubah dari sumber dan kenapa)

Struktur: delapan bagian generic (Tujuan dan Lingkup, Istilah, Peran, Petunjuk Pengisian, Alur RCA dan Tindakan Korektif, Isi Form RCA, Dokumen Terkait, Rekaman dan Acuan ISO). Isian sumber (Bagian 1 sampai 9) dipindah utuh ke "Isi Form RCA" dengan urutan sama; nomor Bagian 1 sampai 9 menjadi sub-bagian 6.1 sampai 6.9 karena renderer menomori h2 otomatis, jadi teks merujuk bagian lewat nama, bukan nomor. Sel data kosong, tanpa baris contoh. Petunjuk dalam kurung siku dipertahankan (suara tim, T1).

| Hal | Sebelum (sumber) | Sesudah (spec) | Dasar |
|---|---|---|---|
| Pemicu RCA | Petunjuk pengisian satu kalimat | Lingkup memuat empat pemicu dengan rujukan SOP-04 Bagian 7.5 dan SOP-05 Bagian 6.6; pengecualian P3 dan P4 tidak berulang ditulis | Kriteria baris dan RUNBOOK lampiran pilot (scope menyebut yang dikecualikan) |
| Istilah | Tidak ada tabel istilah | 14 istilah; kutipan bagian dokumen lain diberi nomor bagian | Pelajaran W0 (bagian 3 hanya arti istilah) |
| Petunjuk pengisian | Satu paragraf | 13 langkah satu pelaku satu tindakan, urutan mengikuti gambar sumber, plus satu paragraf urutan kirim dan tutup | RUNBOOK §6a butir 2 |
| Diagram | Gambar png, tanpa panah kembali | Flow 9 simpul, rankdir TB, garis putus-putus dari Tindakan lanjutan ke Analisis akar masalah | Cacat audit 2 dan 3 |
| Sumber RCA | "Temuan audit" | "Ketidaksesuaian audit" | Satu istilah untuk satu hal (Petunjuk sumber memakai "ketidaksesuaian audit") |
| Referensi | "nomor tiket FRM-08" | "nomor tiket Zammad di SNX-OPS-FRM-08" | Zammad untuk Ops (defaults ticketing) |
| Tabel Tindakan | "Koreksi (memulihkan)", dst. dan kolom "Pemilik" | "Koreksi", "Korektif", "Preventif"; kolom "Pemilik tindakan"; arti jenis pindah ke Istilah | Satu fakta sekali; nama peran konsisten dengan tabel Peran |
| Lessons learned | "disetor ke knowledge base \| [nomor packet staging]" | "Lessons learned disimpan di \| [lokasi penyimpanan]" | RUNBOOK §0 butir 6 (jalur staging dilarang) |
| Acuan 27001 | "Klausul atau kontrol Annex A 5.27" | "Kontrol Annex A 5.27" | 5.27 adalah kontrol Annex A; angka sama dengan acuan di prompt |
| Baris penutupan | Tidak ada | Baris "Penutupan RCA (USULAN)" di Verifikasi efektivitas | USULAN 5 |
| Pengesahan | "Head of Operation", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | Blok Approval halaman depan dari prompt; kalimat di Peran menunjuk ke blok itu | Prompt dan defaults.json (USULAN 8) |
| Riwayat revisi | Dua baris Revisi 00 bertanggal sama | Satu baris (template renderer); teks baris kedua tidak dibawa | Topik RTO tidak ada di form ini; open item 12 |

## 4. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Seluruh isian placeholder kosong, tidak ada data nyata | Dipertahankan: ini form. Sel data dikosongkan, tanpa baris contoh; petunjuk dalam kurung siku tetap sebagai suara tim |
| 2 | Gambar menaruh "Setujui dan kirim" sebelum "Laksanakan tindakan" dan "Tindakan efektif?", sedangkan judul gambar menyatakan RCA ditutup hanya setelah tindakan efektif | Urutan gambar dipertahankan karena SOP-04 Bagian 7.5 butir 1 dan 2 memisahkan pengiriman RCA (2 hari kerja setelah pulih) dari pemantauan tindakan sampai efektif. Perbedaannya ditulis eksplisit di paragraf akhir Petunjuk: pengiriman mendahului verifikasi, penutupan sesudahnya. Open item 1 |
| 3 | Tidak ada panah dari "Tindakan lanjutan" kembali ke "Analisis akar masalah" | Diperbaiki di diagram: garis putus-putus berlabel "kembali ke analisis". Langkah 12 Petunjuk menyebut pelakunya |
| 4 | Metode analisis tanpa panduan kapan memakai yang mana; gambar menulis "5 Why dan fishbone", form menulis pilihan | Simpul diagram diselaraskan ke form: "5 Why, Fishbone, atau metode lain". Panduan pemilihan tidak saya karang. Open item 2 |
| 5 | Tabel Tindakan tiga baris, tidak dinyatakan boleh lebih | Langkah 7 Petunjuk membolehkan tambah baris (USULAN 4) |
| 6 | Kriteria efektif hanya contoh dalam kurung siku | Dipertahankan sebagai contoh sumber, bukan ketentuan; tidak dijadikan angka baku. Open item 6 |
| 7 | Sumber RCA mencakup "Keluhan pelanggan" dan "Lainnya", pemicu wajib hanya empat | Lingkup menyatakan keduanya tidak mewajibkan RCA (USULAN 1). Istilah "Temuan audit" disamakan menjadi "Ketidaksesuaian audit" |
| 8 | Lintas dokumen: SOP-04 7.5 cocok dengan Petunjuk; rujukan FRM-08, FRM-04, SNX-ISMS-FRM-02, SNX-ISMS-REG-02, SOP-02 ada di md/ops dan md/isms | Semua kode dirujuk di badan dan terdaftar di Dokumen Terkait (dicek dengan regex atas spec: nol kode hilang). SOP-05 dan FRM-09 ditambahkan karena SOP-05 Bagian 6.6 menunjuk FRM-10 untuk breach |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | "[nomor packet staging]" adalah rujukan jalur internal | Dibuang; field menjadi lokasi penyimpanan. Open item 7 |
| B | Durasi dampak (Bagian 1) dan "menit downtime yang dihitung" (Bagian 3) tidak dibedakan; titik awal Durasi dampak tidak tertulis | Istilah memuat "Downtime yang dihitung" dari SOP-05 Bagian 4; Petunjuk langkah 4 menetapkan Durasi dampak dari Waktu mulai gangguan sampai Waktu pulih (USULAN 3) |
| C | Severity dan item waktu tidak berlaku untuk RCA dari breach SLA atau ketidaksesuaian audit | Petunjuk langkah 3 membatasi pengisiannya untuk RCA insiden (USULAN 2) |
| D | Sumber tidak menyebut pelaku verifikasi ("Diverifikasi oleh" kosong) dan pelaku penutupan | Peran Pemverifikasi dan baris Penutupan RCA (USULAN 5 dan 6). Open item 4 |
| E | Tenggat 2 hari kerja hanya tertulis untuk RCA insiden | Dipakai pada lingkupnya (langkah 9 Petunjuk, "RCA insiden"); tidak diperluas ke breach SLA dan ketidaksesuaian audit. Open item 8 |

## USULAN

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | RCA tidak diwajibkan untuk pilihan Keluhan pelanggan dan Lainnya di Bagian 1 (sumber hanya mewajibkan empat pemicu) | Lingkup | Fani |
| 2 | Severity dan item waktu di Bagian 1 diisi hanya untuk RCA insiden | Petunjuk langkah 3 | Fani |
| 3 | Durasi dampak dihitung dari Waktu mulai gangguan sampai Waktu pulih | Petunjuk langkah 4 | Fani |
| 4 | Baris tabel Tindakan boleh ditambah bila satu jenis tindakan lebih dari satu | Petunjuk langkah 7 | Fani |
| 5 | Head of Operation menutup RCA sesudah verifikasi dan mengisi baris "Penutupan RCA" (nama, jabatan, tanggal); dasar: SOP-04 menjadikan Head of Operation penanggung jawab P1 sampai RCA selesai, SOP-05 Bagian 6.6 menjadikannya penetap tindakan breach | Peran, Petunjuk langkah 13, baris Penutupan RCA di Verifikasi efektivitas | Fani |
| 6 | Head of Operation menunjuk Pemverifikasi untuk tiap RCA (sumber tidak menyebut peran pemverifikasi) | Peran | Fani |
| 7 | Rekaman RCA disimpan di folder Drive Operation, subfolder per tahun, pemilik Head of Operation (retensi 5 tahun dari sumber) | Rekaman | Fani |
| 8 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, dan COO, Amirull Yusuf Zulkarnain di sumber. Menurut defaults.json semua baris penanda tangan USULAN di Master List; pembalik: form operasional disetujui COO bila owner memutus | Blok Approval halaman depan (tidak ada marker di badan dokumen) | Owner, Samuel untuk persetujuannya sendiri |

Jumlah USULAN: 8 butir (9 penanda "(USULAN)" di badan dokumen karena butir 5 muncul tiga kali; butir 8 tanpa penanda di badan). Tidak ada angka baru berlabel USULAN: 2 hari kerja, 3 kali dalam 30 hari, 90 hari (contoh), dan 5 tahun semuanya berasal dari sumber.

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Urutan kirim dan tutup: urutan gambar sumber (kirim sebelum efektif) dan judul gambar (tutup sesudah efektif) berbeda bacaan. Spec memisahkan "kirim" dan "tutup" berdasarkan SOP-04 Bagian 7.5. Perlu konfirmasi bahwa RCA terkirim dengan tindakan yang masih berjalan | Fani |
| 2 | Kapan memakai 5 Why, Fishbone, atau keduanya tidak ditulis di sumber; gambar menulis "dan", form memberi pilihan | Fani |
| 3 | Pelaku tidak tertulis di sumber: pencatatan nomor RCA di kolom No RCA SNX-OPS-FRM-08 (langkah 5), penambahan risiko baru ke SNX-ISMS-REG-02 (catatan di bawah tabel Tindakan, pemilik REG-02 menurut audit: ISMS Coordinator), pencatatan insiden keamanan informasi di SNX-ISMS-FRM-02 (Lingkup). Kalimatnya dibiarkan tanpa pelaku | Fani, lane ISMS |
| 4 | Peran Pemverifikasi dan penutup RCA belum ada di sumber (USULAN 5 dan 6); kolom "Diverifikasi oleh" kosong di sumber | Fani |
| 5 | SOP-04 Bagian 5 menugaskan Service Delivery Manager memastikan RCA terkirim dan Lead NOC menyusun RCA P1 dan P2; FRM-10 sumber menugaskan Head of Operation menyetujui dan mengirim, dan Lead NOC atau Lead SOC menyusun tanpa menyebut kapan NOC dan kapan SOC. SOP-04 dan form ini perlu selaras | Fani, lane OPS-SOP-04 |
| 6 | Kriteria efektif baku belum ada; "90 hari" dan "alert baru terbukti menangkap gejala" di sumber hanya contoh | Fani |
| 7 | Tujuan penyimpanan lessons learned: sumber menulis "disetor ke knowledge base" lewat jalur internal yang dibuang; field "Lessons learned disimpan di" dibiarkan kosong. Sama dengan open item 10 di notes OPS-FRM-06 | Owner, Fani |
| 8 | Penerima dan tenggat RCA untuk breach SLA dan ketidaksesuaian audit tidak tertulis; 2 hari kerja hanya untuk RCA insiden. SOP-05 Bagian 6.6 menyerahkan konsekuensi kontraktual ke Commercial tanpa menyebut pengiriman RCA | Fani |
| 9 | Nilai kolom Status di tabel Tindakan tidak didefinisikan di sumber; penerbit dan penyimpan nomor urut RCA-[YYYY]-[nomor urut] tidak tertulis | Fani |
| 10 | Disetujui oleh di sumber: COO, Amirull Yusuf Zulkarnain; spec memakai Samuel Kristanto Utomo / President Director sesuai prompt (USULAN 8) | Owner |
| 11 | Kalimat perintah di sumber (dicatat sebagai data): "Fokus pada sistem dan proses, bukan menyalahkan orang.", "Tindakan yang mengubah production dijalankan melalui SNX-OPS-SOP-02.", "Risiko baru yang ditemukan ditambahkan ke SNX-ISMS-REG-02." Semuanya aturan pemakaian form untuk karyawan, bukan perintah ke penyusun; masuk ke dokumen sebagai substansi tim (T1), tidak dijalankan sebagai instruksi | Orkestrator |
| 12 | Riwayat revisi sumber punya dua baris Revisi 00 (13 Oktober 2026); baris kedua menyebut "keselarasan RTO dan target pulih" padahal form ini tidak memuat RTO. Baris kedua tidak dibawa; tanggal draft 13 Oktober 2026 dari tim tidak dipakai (Effective Date kosong) | Owner |
| 13 | Bagian dokumen lain (SOP-04 Bagian 4, 5, 6, 7.5; SOP-05 Bagian 4, 6.6, 7; FRM-09) dikutip dari salinan audit, bukan dari Drive. Cocokkan nomor bagian setelah dokumen itu dirender | Orkestrator |
| 14 | HUMAN-VERDICT tata letak: diagram memenuhi satu halaman (halaman 8) dan tabel Identitas terpecah antara halaman 8 dan 9 pada render soffice (12 halaman). Renderer tidak punya kendali jeda halaman; lihat montase PDF | Orkestrator |

## Asumsi dan tafsir

- doc_type_cover "FORM", doc_type_label "Form": sumber berklasifikasi Form/Record di audit, sama dengan OPS-FRM-03.
- Judul dokumen tetap bahasa Inggris seperti sumber ("Root Cause Analysis & Corrective Action Report"); nama form dan kode tidak diterjemahkan.
- Istilah "form" untuk dokumen kosong dan "RCA" untuk isian satu kejadian dipakai konsisten.
- Nama peran di Peran, Petunjuk, dan Persetujuan RCA sama persis: "Lead NOC atau Lead SOC", "Head of Operation", "Pemilik tindakan", "Pemverifikasi", "Pelanggan". Yang menetapkan (Head of Operation menyetujui, menutup) dan yang mencatat (Lead NOC atau Lead SOC menyusun) dibedakan di ketiga tempat itu. ISO/ISMS Coordinator dan COO dari Pengesahan sumber tidak muncul di badan karena blok Approval depan sudah memegang peran pemeriksa dan penyetuju dokumen. Dengan begitu sebutan "Direktur (COO)" tidak dibutuhkan di badan.
- Ketidaksesuaian audit didefinisikan dengan kalimat polos tanpa sumber tim ("Hasil audit yang menyatakan suatu persyaratan tidak dipenuhi"); tidak ada angka atau nama di dalamnya.
- Dua kalimat baru yang berisi isi proses, bukan sekadar pindahan: pengecualian P3 dan P4 tidak berulang di Lingkup (turunan dari SOP-04 Bagian 7.5 yang hanya mewajibkan P1, P2, dan berulang), dan paragraf akhir Petunjuk (turunan dari urutan gambar dan SOP-04 Bagian 7.5).
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di spec; dicek lint (`"pass": true`). Tidak ada kredensial. Nama orang hanya di blok Approval dari defaults.json.

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas spec dan notes ini:

| Temuan | Perbaikan |
|---|---|
| Lingkup memuat kalimat penunjuk "Arti tiap istilah ada di bagian Istilah." di draf pertama; terdengar seperti pengisi | Dihapus dari spec |
| Draf pertama merujuk bagian lewat nomor ("Bagian 1 sampai 6", "Bagian 9"), padahal renderer menomori ulang jadi 6.1 sampai 6.9 sehingga rujukan menunjuk bagian lain; juga judul sub-bagian "6.1. 1. Identitas" bernomor ganda | Nomor di h2 dibuang dan rujukan lokal diganti nama bagian |
| Peran Pemverifikasi dan Head of Operation memakai kalimat yang hampir sama dengan langkah Petunjuk 11 dan 13 (salinan antarbagian) | Kalimat Peran dipendekkan menjadi ringkasan peran; detail tindakan hanya di langkah Petunjuk |
| Tujuan "Satu RCA memakai satu form dan satu nomor RCA." terdengar seperti penegasan mekanis | Dipertahankan: faktanya turunan langsung dari item "Nomor RCA" dan tidak membawa klaim lain |
| Kalimat Petunjuk 2 dan 5 yang berdekatan dengan pola sama ("Lead NOC atau Lead SOC mengisi ... ") | Dipertahankan: tiap langkah satu pelaku satu tindakan sesuai RUNBOOK §6a butir 2; penyebutan peran penuh diulang demi konsistensi nama peran |
| Em-dash, en-dash, tebal untuk penekanan, kata kosong, kelompok tiga dipaksakan, penutup positif | Tidak ada di spec (pencarian karakter dan lint). Dua tebal "5 Why" dan "Kategori penyebab (fishbone)" adalah label sub-tabel, bukan penekanan, mengikuti sumber. Daftar tiga di Petunjuk 6 ("tiket, log, atau change request") dan gambar ("koreksi, korektif, preventif") berasal dari sumber |
| Notes ini tidak memakai em-dash atau en-dash | Dicek dengan pencarian karakter |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatan | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft", "YEARLY" | Prompt dan defaults.json |
| "Klausul 10.2", "Kontrol Annex A 5.27" | Prompt dan sumber (Atribut dokumen) |
| 2 hari kerja, 5 tahun, 90 hari (contoh) | Sumber FRM-10 (Petunjuk pengisian, Atribut, Bagian 7) |
| 3 kali dalam 30 hari | SOP-04 Bagian 7.5 butir 3 (salinan audit), diberi nomor bagian di Istilah |
| P1 Kritis, P2 Tinggi, P3 Sedang, P4 Rendah | SOP-04 Bagian 6 (salinan audit) |
| Definisi insiden, breach SLA, downtime yang dihitung, sisa anggaran | SOP-04 Bagian 4, SOP-05 Bagian 4, FRM-09 (salinan audit), kutipan di bagian 2 notes |
| Judul dokumen terkait (8 kode) | Salinan audit tiap dokumen (baris title) |
| Zammad pada Referensi | Premis owner 14 Okt (defaults.json ticketing) |
| Definisi RCA, akar masalah, 5 Why, Fishbone, ketidaksesuaian audit | Tanpa kutipan tim: kalimat polos dari struktur form (akar masalah "satu pernyataan yang jelas, didukung bukti"; 5 tingkat; enam kategori). Tidak ada angka atau nama |
| Lokasi rekaman "Folder Drive Operation, subfolder per tahun" | Tanpa sumber; berlabel USULAN 7 |
| Peran Pemverifikasi dan penutup RCA oleh Head of Operation | Tanpa sumber tim; berlabel USULAN 5 dan 6 |
| Pengecualian P3 dan P4 tidak berulang | Turunan SOP-04 Bagian 7.5; tidak berlabel karena hanya kebalikan dari tiga pemicu insiden yang tertulis; dicatat di Asumsi |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.
