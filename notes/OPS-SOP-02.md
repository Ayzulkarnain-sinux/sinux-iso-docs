# Catatan penyusun OPS-SOP-02: SOP Project Change Management

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-SOP-02.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-SOP-02 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C1, review_period YEARLY. Judul meta "Project Change Management" (renderer menambah "SOP" di Document Title). Uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-SOP-02.json /tmp/pen-OPS-SOP-02/OPS-SOP-02.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-OPS-SOP-02/OPS-SOP-02.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "12 butir (USULAN) menunggu ACC" (nol warn PIC SLA). Pratinjau PDF (soffice) 16 halaman dilihat: sampul, Identity, Revision, Approval, TOC, 11 bagian, dan diagram tampil; tidak ada sel kosong.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-SOP-02_SOP_Project_Change_Management.docx (171827 byte) | 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63 | 2026-10-13T06:09:04Z (get_file_metadata, dicek ulang hari ini, sama dengan prompt) | read_file_content (teks utuh); download_file_content (docx didekode ke /tmp/pen-OPS-SOP-02/src, 171827 byte sama dengan metadata). comments.xml dan footnotes.xml kosong, nol tracked change, nol teks tersembunyi, gambar word/media/rId23.png dibuka |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (bahan) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content (teks utuh) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (bahan) | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content (teks utuh) |
| Kriteria penerimaan | config/checklist.json baris 64, config/worklist.json baris OPS-SOP-02 | checklist modifiedTime tidak diukur ulang di sesi ini | Kolom Description hanya nama berkas, jadi kriteria = substansi SOP-02 sumber + acuan ISO 9001:2015 "6.3, 8.5.6" dan ISO/IEC 27001:2022 "8.32" |
| Pendukung repo (bukan Drive) | specs/HR-ORG-01.json (nama peran, K-09, K-10, K-11), config/defaults.json v21, notes/OPS-FRM-04.md, notes/ISMS-SOP-02.md, notes/OPS-FRM-03.md, notes/OPS-RPT-01.md, context/audit (bagian SNX-OPS-SOP-02) | repo kerja | Dipakai untuk keselarasan lintas dokumen; kutipan dari dokumen lain bisa basi bila dokumen itu berubah |

Catatan: POL-OPS-001 dan PRO-OPS-001 lebih baru (09:06Z) daripada SOP-02 (06:09Z). Keduanya berstatus DRAFT v0.1 dan hanya dipakai sebagai bahan untuk nama peran, definisi, dan pembanding. Isi SOP-02 tetap kriteria utama.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Syarat go-gate: lima syarat yang harus terpenuhi sebelum change production dieksekusi; di dokumen ini menjadi aturan di bagian 4 untuk change teknis | "Tidak ada perubahan production yang dieksekusi sebelum lima syarat ini terpenuhi:" (Bagian 4, diikuti lima butir approval tertulis plus ack pelanggan, backup atau snapshot dengan lokasi dicatat, rollback satu perintah atau satu langkah tertulis, eksekusi satu langkah satu waktu, before dan after terdokumentasi) | 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63 |
| 2 | Change Emergency boleh dieksekusi sebelum CR lengkap; CR dilengkapi dalam 1 hari kerja dan ditinjau Head of Operation; COO diberi tahu dalam 30 menit sejak eksekusi | "Lead on-duty boleh mengeksekusi sebelum CR lengkap, dengan tetap mengambil backup bila memungkinkan dan mencatat setiap langkah." dan "CR dilengkapi paling lambat 1 hari kerja setelahnya dan ditinjau Head of Operation." dan "COO diberi tahu dalam 30 menit sejak eksekusi." (Bagian 6.6) | 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63 |
| 3 | Pembagian jenis change berstatus USULAN di kebijakan induk, sehingga bagian 4 dan 8 memberi label (USULAN) pada jenis, kriteria, dan waktu notifikasi | "Pembagian jenis change adalah USULAN; prinsip go-gate di atasnya bersumber dari keputusan owner." (Bagian 7) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |

## 2. Fakta pendukung dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan (kalimat tim dipertahankan utuh) | "SOP ini mengendalikan setiap perubahan pada scope proyek dan pada environment production pelanggan maupun infrastruktur SINUX, agar perubahan dikaji, disetujui, dapat dikembalikan, dan terdokumentasi sebelum dieksekusi." (SOP-02, 1. Tujuan) | Bagian 1 |
| 2 | Dua jenis change dan pengecualian app-level | "Perubahan proyek: scope, jadwal, deliverable, atau sumber daya proyek yang sudah ber-baseline." dan "Tidak berlaku untuk perubahan app-level pelanggan yang menjadi tanggung jawab developer atau PIC pelanggan." (SOP-02, 2. Ruang lingkup) | Bagian 2 |
| 3 | Isi app-level pelanggan | "Di luar ruang lingkup: app-level pelanggan (isi WordPress, plugin, DB aplikasi, kode pelanggan), keputusan harga dan komersial, serta SOC POLRI (tanggung jawab POLRI)." (POL-OPS-001, 2) | Bagian 3, definisi App-level pelanggan |
| 4 | Jenis Normal | "Normal \| Dampak terbatas, butuh jadwal \| Resize VM, ubah konfigurasi web server, instal SSL, ubah rule WAF \| Lead plus ack pelanggan \| Minimal H-2" (SOP-02, 5) | Bagian 4 (kriteria dan notifikasi), bagian 5 (approver) |
| 5 | Jenis Major | "Major \| Dampak luas atau sulit dikembalikan \| Migrasi, upgrade versi platform, perubahan core network \| COO plus ack pelanggan \| Minimal H-5 dan pengingat H-0" (SOP-02, 5) | Bagian 4, bagian 5 |
| 6 | Jenis Proyek | "Proyek \| Perubahan scope, jadwal, atau deliverable proyek \| Tambah VM di luar BOQ, geser go-live \| Service Delivery Manager; harga oleh Commercial \| Tertulis ke PIC pelanggan" (SOP-02, 5) | Bagian 4, bagian 5 |
| 7 | Isi minimal CR dan pencatatan di FRM-04 | "Pengaju membuat change request di Service Hub dan mencatatnya di SNX-OPS-FRM-04 dengan nomor CR unik." dan "Isi minimal: tujuan, sistem atau mesin target, jenis change, langkah eksekusi, dampak ke layanan, risiko, rencana backup, perintah rollback, jadwal, dan pelaksana." (SOP-02, 6.1) | Butir 6.1 |
| 8 | Kajian keamanan oleh Lead SOC | "Change yang menyentuh kontrol keamanan (akses, rule WAF atau firewall, encryption, logging) dikaji juga oleh Lead SOC." (SOP-02, 6.2) | Butir 6.2, bagian 5 |
| 9 | Harga change proyek ke Commercial | "Change proyek yang mengubah harga diteruskan ke Commercial; Operation tidak menjanjikan tanggal sebelum Commercial menyetujui." (SOP-02, 6.2) | Butir 6.2 |
| 10 | Eksekusi: hostname, blok ukur lawan blok ubah, restart, delete, cPanel | "Setiap blok perintah diawali pemeriksaan hostname untuk memastikan mesin yang benar." / "Blok ubah terpisah dari blok ukur; satu langkah satu waktu." / "Restart VM pelanggan selalu didahului izin pelanggan." / "Delete VM bersifat unrecoverable dan butuh konfirmasi tertulis pelanggan dua kali." / "Di server cPanel, perintah yum install atau remove perl-* dilarang." (SOP-02, 6.4; di sumber tertulis dengan garis miring terbalik sebelum tanda bintang) | Butir 6.4 |
| 11 | Verifikasi, rollback, pencatatan, PIR | "Verifikasi gagal berarti rollback, bukan improvisasi. Rollback dicatat di CR." / "Catat before dan after, status akhir (Berhasil, Rollback, Gagal), dan waktu selesai di SNX-OPS-FRM-04." / "Change Major dan change yang berakhir rollback ditinjau ulang (post implementation review) dalam 5 hari kerja." (SOP-02, 6.5) | Butir 6.5, bagian 8 |
| 12 | Record dan masa simpan | "Change Request & Approval Log \| SNX-OPS-FRM-04 \| 3 tahun"; "Information Asset Register (pembaruan konfigurasi) \| SNX-ISMS-REG-01 \| Berlaku sampai digantikan"; "Laporan progres proyek (change proyek) \| SNX-OPS-FRM-03 \| Durasi kontrak + 3 tahun" (SOP-02, 7) | Bagian 11, tabel rekaman |
| 13 | Indikator kinerja | "Change dieksekusi dengan CR disetujui sebelum eksekusi (kecuali Emergency) \| 100%"; "Change tanpa rollback darurat \| 95%"; "CR Emergency dilengkapi dalam 1 hari kerja \| 100%"; "Insiden yang disebabkan change \| Dilaporkan bulanan, tren menurun" (SOP-02, 8) | Bagian 8 |
| 14 | Pemilik dokumen | "Pemilik dokumen \| Head of Operation" (SOP-02, tabel Atribut) | meta.process_owner (tanpa nama) |
| 15 | Acuan ISO | "Acuan ISO 9001:2015 \| Klausul 6.3, 8.5.6" dan "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 8.32" (SOP-02, tabel Atribut); "ISO 9001:2015 klausul 6.3 (perencanaan perubahan) dan 8.5.6 (pengendalian perubahan)." (Bagian 3) | Bagian 11 (Acuan standar), bagian 4 (tercermin) |
| 16 | Kebijakan induk go-gate | "P-04 \| Ubah production pelanggan hanya dengan go-gate lead atau owner plus ack, backup dulu, rollback satu perintah, satu langkah satu waktu, terdokumentasi." (POL-OPS-001, 4) | Bagian 4 (selaras P-04), bagian 11 |
| 17 | Pelaksana teknis = engineer atau analyst yang ditugaskan | "Pelaksana: engineer atau analyst yang ditugaskan · Akuntabel: approver sesuai jenis change (POL-OPS-001 §7) · Pemicu: setiap perubahan production pelanggan atau infra SINUX." (PRO-OPS-001, CHG-01) | Bagian 5, baris Pengaju dan Pelaksana |
| 18 | Pengaju change proyek | "Catat sebagai change of scope di Service Hub." (PRO-OPS-001, SDPM-05, Pelaksana Service Delivery Manager) | Bagian 5, baris Pengaju |
| 19 | Commercial = VP Commercial (Laras) | "P-06 \| Komersial: Operation tidak memberi harga, diskon, atau komitmen scope baru. Semua ke Commercial (Laras)." (POL-OPS-001, 4); premis owner: Laras Rasmawati = VP Commercial | Bagian 5, baris VP Commercial |
| 20 | Vantage eksternal | "Verifikasi posture publik dari vantage eksternal dan browser nyata, bukan dari dalam jaringan atau 127.0.0.1." (POL-OPS-001, P-09) | Bagian 3, definisi Vantage eksternal |
| 21 | KPI dilaporkan oleh Head of Operation | "laporan KPI divisi bulanan ke COO" (POL-OPS-001, 9.1, tanggung jawab Head of Operation) dan "target awal di bawah adalah USULAN dan dikalibrasi setelah 3 bulan data nyata, sebab baseline saat ini belum diukur." (POL-OPS-001, 11) | Bagian 5 (baris Head of Operation), bagian 8 |
| 22 | Tiket: Zammad untuk Ops | Owner 14 Okt (config/defaults.json): "sistem tiket zammad untuk ops, glpi untuk generalist". Sumber SOP-02 menulis "Service Hub" | Definisi Zammad, butir 6.1 |
| 23 | Head of Operation meninjau pelanggaran go-gate | "Pelanggaran P-03 (kredensial), P-04 (go-gate), atau P-05 (batas MSP) diperlakukan sebagai insiden internal, dicatat di Service Hub, dan ditinjau Head of Operation." (POL-OPS-001, 12) | Dasar pola untuk USULAN peninjau PIR |

## 3. Pemetaan klausul ISO (kriteria)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 6.3 (Perencanaan perubahan) | Ya, "6.3 (Perencanaan perubahan)" | Paragraf pertama: CR diajukan, dikaji, dan disetujui sebelum eksekusi | 6.1, 6.2 |
| ISO 9001:2015 8.5.6 (Pengendalian perubahan) | Ya, "8.5.6 (Pengendalian perubahan)" | Paragraf go-gate dan lima syarat | 6.3 sampai 6.6 |
| ISO/IEC 27001:2022 Annex A 8.32 (Change management) | Ya, "Annex A 8.32 (Change management)" | Paragraf go-gate dan lima syarat; kajian keamanan oleh Lead SOC di butir 6.2 | 6.1 sampai 6.6 |

Nama klausul dalam kurung berasal dari bagian 3 Referensi sumber SOP-02. Sumber atribut menulis "Klausul atau kontrol Annex A 8.32"; dokumen ini menulis "Annex A 8.32" karena 8.32 adalah kontrol Annex A (sama dengan keputusan di notes/OPS-FRM-04.md).

## 4. Keputusan data

- Approval: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director, persis dari prompt dan config/defaults.json. Sumber menulis "Disusun oleh Head of Operation", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber (D2).
- Sebutan COO: "Direktur (COO)" pada sebutan pertama di badan dokumen (bagian 5, baris Approver), sesudahnya "COO" (dicek dengan pencarian atas teks docx: satu kemunculan "Direktur (COO)", lima "COO" sesudahnya, nol sebelumnya). Samuel tidak disebut di badan dokumen, jadi aturan "Direktur Utama" tidak terpakai.
- Process owner "Head of Operation" mengikuti "Pemilik dokumen" sumber, tanpa nama. Department "Operation" (department_labels OPS).
- Tiket: CR dibuat di Zammad (USULAN, USULAN 3) karena CR adalah pekerjaan Divisi Operation; keputusan sama dengan SNX-OPS-FRM-04 yang sudah DONE. Kata "Service Hub" dan "GLPI" tidak dipakai di dokumen ini.
- Vault dan PPN tidak relevan untuk SOP ini.

Pemetaan peran sumber ke nama peran HR-ORG-01 (specs/HR-ORG-01.json: Struktur Divisi Operation dan Matriks Peran):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Head of Operation | Head of Operation | HR-ORG-01 (USULAN, belum ada pemegang, K-10; pemilik SOP menurut sumber) |
| Lead sub divisi | Lead NOC atau Lead SOC, sesuai sub divisi yang menjalankan change | HR-ORG-01 hanya punya Lead NOC dan Lead SOC; SD dan PM dipimpin Service Delivery Manager. Pemetaan tafsir |
| Lead on-duty | Lead NOC atau Lead SOC yang bertugas | Tafsir; POL-OPS-001 bagian 3: Lead di jam kantor plus on-call |
| Lead SOC | Lead SOC | HR-ORG-01 |
| COO | Direktur (COO), lalu COO | HR-ORG-01 JA-02 dan data_conflicts |
| Service Delivery Manager | Service Delivery Manager | HR-ORG-01 |
| Commercial | VP Commercial | HR-ORG-01 JA-03; POL-OPS-001 P-06 "Commercial (Laras)" |
| Pengaju | Pengaju (peran prosedur): NOC Engineer atau SOC Analyst untuk change teknis, Service Delivery Manager untuk change proyek | PRO-OPS-001 CHG-01 dan SDPM-05; kedua jabatan ada di HR-ORG-01 |
| Pelaksana (kolom CR di sumber) | Pelaksana (peran prosedur): NOC Engineer atau SOC Analyst yang ditugaskan di CR | PRO-OPS-001 CHG-01 |
| Approver | Approver (peran prosedur), pemegang per jenis ada di kolom Authority bagian 5 | SOP-02 bagian 5 dan 6.2 |
| Pelanggan, PIC pelanggan, developer pelanggan | Pelanggan, PIC pelanggan | Pihak luar; tidak ada di HR-ORG-01 |
| ISO/ISMS Coordinator | Tidak dipakai di badan | Hanya di blok Pengesahan sumber; blok itu diganti defaults |
| VP Tech Operation and Services | Tidak dipakai di badan | Hanya reviewer di blok Approval (defaults); lihat open item 2 |

## 5. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 15FTuu06HTHoF-Vi0qzqvwmfQH5tEdT63)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, persetujuan "Menunggu", tanda tangan dan tanggal kosong, dua baris riwayat revisi bernomor sama | Teratasi oleh template: satu baris Revision 00 dengan deskripsi dari prompt, Document Status Draft, Effective Date kosong, Signature kosong. Tanggal draft tim (13 Oktober 2026) tidak dibawa |
| 2 | Jenis Standar, Normal, Major, Emergency tanpa label USULAN; jenis kelima Proyek tidak ada di POL-OPS-001 bagian 7 | Diperbaiki: paragraf di bagian 4 memberi label (USULAN) pada jenis, kriteria, dan waktu notifikasi; kata "Proyek" tetap sebagai jenis kelima karena sumber SOP-02 memuatnya. Selisih dengan POL masuk open item 7 |
| 3 | Tambahan SOP-02 yang tidak ada di POL dan PRO: kajian Lead SOC, PIR 5 hari kerja, CR Emergency 1 hari kerja dan ditinjau Head of Operation, status akhir Berhasil, Rollback, Gagal | Dipertahankan (T1; sumber SOP-02 sendiri, tidak dihapus). Pelaku PIR tidak disebut sumber, jadi dipasangkan ke Head of Operation dengan label (USULAN) (USULAN 5). Selisih dengan POL dan PRO masuk open item 8 |
| 4 | Notifikasi COO untuk Emergency: titik awal "sejak eksekusi" hanya di 6.6; baris tabel Bagian 5, POL, dan PRO tanpa titik awal | Diperbaiki sebagian: kalimat "dalam 30 menit sejak eksekusi" dipakai sama di butir 6.6, bagian 5 (baris COO), dan bagian 8. Apakah "sejak eksekusi" berarti sejak mulai atau selesai tidak ditentukan sumber; open item 5 |
| 5 | Approval Standar dan Normal "Lead sub divisi" dan "Lead plus ack pelanggan" selaras POL bagian 7, tetapi RACI POL bagian 10 menaruh Head of Operation sebagai "A" | Tidak diubah: teks SOP-02 dipertahankan dengan nama peran HR-ORG-01 (Lead NOC atau Lead SOC). Selisih RACI masuk open item 7 |
| 6 | Notifikasi "Minimal H-2" dan "Minimal H-5 dan pengingat H-0" tanpa satuan hari; PRO NOC-06 menulis "minimal 3 hari kerja sebelumnya" | Tidak diperbaiki diam-diam: definisi H-n menyatakan satuan belum ditetapkan. Angka 3 hari kerja dari PRO tidak dimasukkan karena lingkupnya pengajuan window maintenance, bukan notifikasi pelanggan. Open item 4 |
| 7 | Gambar sumber: kotak klasifikasi tanpa Proyek, tanpa jalur Emergency, kotak oranye tanpa panah keluar; "Ditolak atau revisi" lawan teks "Disetujui, Ditolak, atau Revisi" | Diperbaiki: diagram bagian 7 digambar ulang dari spec dengan jenis Proyek (harga ke VP Commercial), jalur Emergency, panah dari Ditolak atau Revisi kembali ke Pengaju, panah dari Rollback ke pencatatan, dan PIR. Gambar asli di berkas sumber tidak disentuh (di luar kewenangan) |
| 8 | Rujukan internal pada bagian 3 Referensi sumber dan pada subjudul gambar (dua kode dokumen internal AI) tidak dapat diverifikasi | Dibuang (RUNBOOK §0 butir 6). Padanan SNX: kebijakan P-04 di POL-OPS-001, dicantumkan di bagian 4 dan bagian 11 |
| 9 | Tidak ada tabel peran formal atau RACI | Diperbaiki: tabel peran bagian 5 dibuat dengan nama peran HR-ORG-01; kolom Authority memuat approver per jenis change, sehingga petunjuk SNX-OPS-FRM-04 A2 ("Approver sesuai SNX-OPS-SOP-02 Bagian 5") tetap benar |

Cacat tambahan yang saya temukan (di luar bagian 5 audit):

| # | Temuan | Penanganan |
|---|---|---|
| A | Go-gate di sumber berbunyi "Tidak ada perubahan production yang dieksekusi sebelum lima syarat ini terpenuhi", padahal butir 6.6 membolehkan Emergency dieksekusi sebelum CR lengkap dan KPI memberi "kecuali Emergency" | Diperbaiki: bagian 4 memberi pengecualian Emergency dan menunjuk bagian 9; bagian 9 baris pertama memuat penanganannya |
| B | Atribut sumber "Masa simpan record: Berlaku sampai digantikan" bertentangan dengan tabel Record (3 tahun, dan lain-lain) | Template tidak punya field itu; hanya tabel bagian 11 yang berlaku, memakai nilai tabel sumber |
| C | Kolom Hasil di SNX-OPS-FRM-04 memuat Dibatalkan, SOP-02 hanya Berhasil, Rollback, Gagal | Tidak diubah (kalimat tim jelas). Open item 9 |
| D | "Kontrol positif" dipakai tanpa definisi | Didefinisikan dengan label (USULAN) (USULAN 4) |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. "perubahan production" di Bagian 4 sumber dibaca sama dengan "perubahan teknis" di Bagian 2 sumber; bagian 4 dokumen ini memakai "change teknis". POL-OPS-001 bagian 7 ("production pelanggan atau infra SINUX") mendukung bacaan ini.
2. Go-gate tidak dinyatakan berlaku untuk change proyek; sumber hanya menyebut perubahan production. Dokumen memakai "change teknis" dan tidak menulis pengecualian eksplisit untuk change proyek.
3. Kalimat pasif sumber diberi pelaku: Pelaksana (blok ukur, backup, hostname, verifikasi, rollback, pencatatan, pembaruan REG-01, notifikasi pelanggan) dari PRO-OPS-001 CHG-01 dan NOC-06; Approver memastikan ack pelanggan (tafsir dari butir 1 go-gate dan kolom Approver "Lead plus ack pelanggan"); Lead NOC atau Lead SOC memberi tahu COO, memberi tahu pelanggan, dan melengkapi CR Emergency (tafsir dari subjek "Lead on-duty" di 6.6 butir 1); Service Delivery Manager meneruskan change proyek ke VP Commercial (dari PRO-OPS-001 SDPM-05).
4. Pelaku notifikasi pelanggan untuk change proyek tidak disebut sumber; dokumen memakai Pelaksana (butir 6.3). Open item 6.
5. SLA indikator kinerja (bagian 8): PIC Head of Operation diambil dari tanggung jawab "laporan KPI divisi bulanan ke COO" di POL-OPS-001 9.1; sumber SOP-02 tidak memberi PIC.
6. Lokasi rekaman: sumber SOP-02 hanya memberi nomor dan masa simpan. Kolom lokasi memakai "Berkas SNX-OPS-FRM-04" dan "Berkas SNX-ISMS-REG-01" (tanpa menyebut folder atau Drive), pemilik Head of Operation dari "Pemilik dokumen" di FRM-04 dan REG-01 (notes/ISMS-REG-01.md); FRM-03 memakai "Folder proyek; pemilik sesuai SNX-OPS-FRM-03" dari notes/OPS-FRM-03.md (sumber FRM-03: folder proyek, pemilik Project Manager).
7. Definisi umum (Baseline, BOQ, Rollback, Off-office-hour, Blok ubah, Blok ukur, H-n, PIR, Ack pelanggan, PIC pelanggan) adalah penjelasan penyusun, bukan kalimat tim. NOC dan SOC dikutip dari definisi di specs/HR-ORG-01.json.
8. Frekuensi tinjauan SOP "setiap tahun" berasal dari review_period YEARLY di config/defaults.json. POL-OPS-001 dan PRO-OPS-001 menulis siklus review 6 bulan untuk dokumen mereka sendiri.
9. Contoh jenis change (rule firewall Accept, reset password, resize VM, dan seterusnya) disalin dari tabel Bagian 5 sumber; "PIC pelanggan" ditambahkan pada contoh reset password agar jelas pemintanya adalah PIC di sisi pelanggan (sumber menulis "atas permintaan PIC").
10. Tanda "/" di kolom PIC ("Lead NOC / Lead SOC") berarti Lead yang bertugas pada change itu; lint memecahnya sebagai dua peran.
11. Kalimat bernada perintah di sumber (langkah prosedur, dan butir kotak centang keputusan di POL-OPS-001 bagian 13) diperlakukan sebagai isi dokumen atau keputusan untuk pemilik, bukan instruksi untuk penyusun. Tidak ada kalimat di sumber yang ditujukan ke penyusun atau AI.

## USULAN

Lint menghitung 12 kemunculan label (USULAN), dikelompokkan menjadi 6 butir.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Pembagian jenis change (Standar, Normal, Major, Emergency, Proyek), kriteria, approver per jenis, dan waktu notifikasi pelanggan (H-2, H-5 dengan pengingat H-0, saat itu juga). Label berasal dari POL-OPS-001 bagian 7; jenis Proyek hanya ada di SOP-02 | Bagian 4; bagian 5 (Authority); bagian 8 (tiga baris notifikasi) | owner (Direktur, COO); kelas C1 menuntut ACC COO |
| 2 | Pemberitahuan ke COO dalam 30 menit sejak eksekusi untuk change Emergency (titik awal belum tegas) | Butir 6.6; bagian 8 | owner |
| 3 | CR dibuat di Zammad, bukan Service Hub (GLPI) seperti tertulis di sumber, karena CR adalah pekerjaan Divisi Operation. Sama dengan keputusan di SNX-OPS-FRM-04. Batas "generalist" belum dirinci owner | Definisi Zammad; butir 6.1 | owner, dengan Fani |
| 4 | Arti "kontrol positif": pemeriksaan yang membuktikan hasil change yang diharapkan benar-benar terjadi. Sumber memakai istilah itu tanpa definisi | Bagian 3 | Fani |
| 5 | Peninjau PIR change Major dan change yang berakhir rollback adalah Head of Operation. Sumber hanya menyebut tinjauan dalam 5 hari kerja tanpa pelaku; pola: Head of Operation meninjau CR Emergency (6.6) dan pelanggaran go-gate (POL-OPS-001 12) | Bagian 5 (baris Head of Operation); butir 6.5 langkah terakhir | Fani |
| 6 | Target indikator kinerja: 100%, 95%, 100%, tren menurun. POL-OPS-001 bagian 11 menyatakan target awal berstatus USULAN dan dikalibrasi setelah 3 bulan data; tiga dari empat target hanya ada di SOP-02 | Bagian 8 (empat baris indikator) | owner |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Penanda tangan: sumber menulis Disusun Head of Operation, Diperiksa ISO/ISMS Coordinator, Disetujui COO (Amirull Yusuf Zulkarnain). Dokumen memakai Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo sesuai defaults (D2). Semua baris ini USULAN di Master List | owner atau Samuel |
| 2 | Head of Operation belum punya pemegang (HR-ORG-01 K-10) dan hubungannya dengan VP Tech Operation and Services belum ditetapkan (K-09). Matriks Peran HR-ORG-01 menaruh tanggung jawab atas "perubahan teknis" pada VP Tech Operation and Services, sedangkan SOP-02 tidak menyebutnya sebagai approver atau tempat eskalasi change Major. Pemilik SOP tetap "Head of Operation" mengikuti sumber | owner, Fani |
| 3 | Batas Ops lawan generalist untuk sistem tiket belum dirinci; POL-OPS-001 P-08 masih menulis semua tiket di GLPI. SOP-02 memakai Zammad (USULAN 3) | owner |
| 4 | Satuan hari pada H-2, H-5, H-0 (kalender atau kerja) belum ditetapkan. PRO-OPS-001 NOC-06 menulis pengajuan CR untuk window maintenance minimal 3 hari kerja sebelumnya, angka yang tidak ada di SOP-02; apakah berlaku untuk change Normal dan Major perlu diputus | owner, Fani |
| 5 | Titik awal 30 menit untuk pemberitahuan COO: sejak eksekusi dimulai atau selesai. POL, PRO, dan tabel Bagian 5 sumber tanpa titik awal | owner |
| 6 | Pelaku yang tidak disebut sumber dan ditafsir dokumen: notifikasi pelanggan (terutama change proyek), memastikan ack pelanggan, melengkapi CR Emergency, memberi tahu COO dan pelanggan pada Emergency, memperbarui SNX-ISMS-REG-01, dan melaporkan indikator bagian 8. Pemetaan Pengaju dan Pelaksana ke NOC Engineer, SOC Analyst, dan Service Delivery Manager mengikuti PRO-OPS-001 | Fani |
| 7 | Selisih dengan POL-OPS-001: (a) POL bagian 7 hanya empat jenis tanpa Proyek; (b) RACI bagian 10 menaruh Head of Operation sebagai "A" untuk change Standar dan Normal, sedangkan SOP-02 memberi persetujuan ke Lead; (c) bagian 9.1 POL memberi Head of Operation wewenang menyetujui change Normal lintas sub divisi, tidak ada di SOP-02; (d) bagian 12 POL mengatur pengecualian atas P-04 (go-gate) dengan persetujuan COO (USULAN), SOP-02 hanya mengatur Emergency; (e) bagian 13 POL menugaskan COO mengesahkan jenis change dan belum diputus | owner, Fani |
| 8 | Tambahan SOP-02 yang tidak ada di POL dan PRO: kajian Lead SOC, PIR 5 hari kerja, CR Emergency 1 hari kerja, status akhir Berhasil, Rollback, Gagal. Dipertahankan; POL dan PRO perlu diselaraskan atau tambahan itu disahkan | owner |
| 9 | SNX-OPS-FRM-04: kolom Hasil memuat Dibatalkan sedangkan SOP-02 menulis tiga status akhir; kolom Approver per jenis kini ada di tabel peran bagian 5 dan kriteria jenis di bagian 4 (cocokkan petunjuk A2 FRM-04); FRM-04 tidak memiliki kolom hasil PIR; rumus Go-gate FRM-04 tidak memeriksa ack pelanggan (lihat open item 1 di notes/OPS-FRM-04.md) | Orkestrator, Fani |
| 10 | Wadah laporan bulanan untuk empat indikator bagian 8 tidak disebut sumber. SNX-OPS-RPT-01 memuat KPI "Change tanpa rollback darurat" (nama dan rumusnya dipersoalkan di notes/OPS-RPT-01.md); tiga indikator lain belum punya baris KPI. Lokasi dan retensi catatan PIR dan tiket CR di Zammad tidak ditetapkan sumber, tidak ditulis di tabel rekaman | Fani |
| 11 | Lokasi simpan rekaman FRM-04 dan REG-01 (folder atau sistem) belum ditetapkan sumber; tabel rekaman bagian 11 menulis nama berkas dan pemilik saja | Fani |
| 12 | Satu fakta bergantung pada dokumen lain yang masih DRAFT: nama NOC, SOC, dan jabatan Divisi Operation dari HR-ORG-01 (semua USULAN, K-10); P1 dan P-04 dari POL-OPS-001 DRAFT v0.1 yang sendiri meminta pengesahan COO | owner |

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas spec (pencarian pola atas frasa terlarang RUNBOOK §6a dan permintaan owner: pada intinya, yang terpenting, secara fundamental, tanpa terkecuali, tanpa kompromi, dari hulu ke hilir, dalam rangka, adapun, perlu diketahui, dikarenakan, dapat berpotensi, praktik terbaik, para ahli, sistem memutuskan, tebal, tanda kutip; ditambah baca ulang):

| Temuan | Perbaikan |
|---|---|
| Baris Lead NOC dan Lead SOC di tabel peran terlalu panjang dan memakai kalimat pembuka yang sama ("Menjalankan peran Approver untuk change dari sub divisi ...") | Dipersingkat; kalimat "Pada change Emergency SOC, menjalankan tugas yang sama dengan Lead NOC" menggantikan daftar yang diulang |
| Delapan dari sepuluh baris SLA berlabel (USULAN) di draf pertama, terbaca seperti lindung nilai | Label "(USULAN)" pada "Saat itu juga" dihapus karena bukan angka; kini tujuh dari sepuluh baris berlabel. Label dipertahankan pada angka karena POL-OPS-001 sendiri menyebut jenis change dan target KPI berstatus USULAN |
| Lima butir "Syarat 1" sampai "Syarat 5" berpola sama | Dipertahankan: itu daftar lima syarat dari tim, satu kalimat per syarat, dan kalimat tim yang jelas tidak diganti agar terdengar rapi |
| Kata "Lead" tanpa keterangan dan "tim" | Dicari dengan pola atas spec: nol kemunculan "Lead" tanpa NOC atau SOC, nol "tim" |
| Em-dash, en-dash, tebal, tanda kutip penekanan, frasa pengisi, ekor penegas, rentang palsu, penutup positif | Dicari dengan pola atas spec dan notes ini: nol. Kesimpulan dua kalimat, tanpa pujian |
| Frasa "ditentukan menurut jenis change, di kolom Authority baris ..." di baris Approver agak kaku | Dibiarkan karena menunjuk tempat satu fakta (approver per jenis) disebut sekali; membuat tabel kedua menyalin fakta itu |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber atau status |
|---|---|
| H-2, H-5, H-0, 30 menit, 1 hari kerja, 5 hari kerja, 100%, 95%, "dua kali", "lima syarat", masa simpan 3 tahun, "Durasi kontrak + 3 tahun", "Berlaku sampai digantikan" | SOP-02 sumber (kutipan di bagian 2); label USULAN mengikuti POL-OPS-001 |
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatan; YEARLY; "Draft awal untuk review dan pengesahan" | Prompt dan config/defaults.json |
| 6.3, 8.5.6, 8.32 dan namanya | Prompt dan sumber SOP-02 bagian 3 |
| Zammad | Kata owner 14 Okt di defaults; penerapan ke CR berlabel USULAN |
| 127.0.0.1, P-04, P1, DRAFT v0.1 | POL-OPS-001 dan PRO-OPS-001 |
| Pemetaan Pengaju, Pelaksana, Lead sub divisi, Lead on-duty, Commercial ke nama peran | Tafsir dari PRO-OPS-001, POL-OPS-001, dan HR-ORG-01; tercatat di bagian 4 dan open item 6; PIR berlabel USULAN |
| Definisi Baseline, BOQ, Rollback, Off-office-hour, Blok ubah, Blok ukur, H-n, PIR, Ack pelanggan, PIC pelanggan | Penjelasan penyusun tanpa angka atau nama baru; Kontrol positif berlabel USULAN |
| "Google Drive" sebagai lokasi simpan | Ada di draf pertama; dihapus karena tidak bersumber. Kolom lokasi kini memakai nama berkas dan pemilik dari sumber (open item 11) |
| PIC indikator kinerja Head of Operation | Tafsir dari POL-OPS-001 9.1; open item 6 |
Tidak ada tanggal, nomor izin, harga, atau nama orang lain yang ditambahkan. Tanggal draft tim (13 Oktober 2026) tidak dibawa; Effective Date kosong.
