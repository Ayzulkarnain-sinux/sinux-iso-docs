# Catatan penyusun FAT-SOP-01: SOP Billing & Invoicing

Status: DRAFTED (spec + notes ada). Spec: specs/FAT-SOP-01.json. Mode sop, aksi T1, wave W3, nomor SNX-FAT-SOP-01 (nomor SNX lama dipertahankan), department Finance, Accounting & Tax, classification INTERNAL (worklist), audit_class C2, review_period YEARLY, status Draft, revision 00, effective_date kosong.

Uji terakhir: `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/FAT-SOP-01.json /tmp/pen-FAT-SOP-01/FAT-SOP-01.docx` lalu `python3 -I tools/lint_doc.py /tmp/pen-FAT-SOP-01/FAT-SOP-01.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "6 butir (USULAN) menunggu ACC" (nol warn PIC SLA). Validator OOXML skill docx (`/mnt/skills/public/docx/scripts/office/validate.py`): "All validations PASSED!". Pratinjau PDF (soffice) 16 halaman; halaman 13 dilihat: diagram 17 simpul, rankdir TB, muat satu halaman, semua label terbaca. Lint dan validator hanya membuktikan format dan larangan pola; kebenaran isi terhadap sumber diperiksa manual lewat tabel di bawah.

Putaran perbaikan 1 (dari orkestrator, verifikator PASS): (1) Bagian 9 dan scope menyebut SOP Account Receivable & Collection sedang dalam peninjauan, tidak lagi "belum berdokumen"; (2) lima frasa meta "dokumen sumber" diganti nama dokumen ("SOP Billing dan Invoicing versi tim") atau dihapus; (3) nonblocking verifikator yang murah ikut dikerjakan: Autentikasi dua faktor (baku), bukti persetujuan perubahan invoice di arsip digital FAT pada tabel rekaman, NPWP klien di lampiran langkah 6.1.4, klausul 8.6 di bagian 11, butir 4.7 dengan pelaku Finance Staff. Tidak dikerjakan karena butuh keputusan FAT: nonblocking tempat catat tanggal penerimaan (open item 3), tumpang tindih e-Faktur dengan SNX-FAT-SOP-05 (open item 14). Render ulang: pass true, fails kosong, warn hanya "6 butir (USULAN)"; OOXML PASSED.

Putaran perbaikan 2 (verifikator PASS): (1) Retensi Register Penagihan dan Penjualan, persetujuan tertulis, dan log ketidaksesuaian kini "Minimal 10 tahun". Kutipan sumber 8.2: "Seluruh arsip dokumen penagihan dan bukti perpajakan wajib disimpan selama minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001." Dasar "sesuai ketentuan perpajakan dan audit ISO" tetap tidak dibawa (cacat tambahan C). (2) Overdue: sumber 5.3 menulis "akan masuk ke dalam kategori Overdue", bukan status Register, sedangkan daftar status Register di 8.2 hanya "(Draf, Terkirim, Lunas, atau Cancel)". Karena sumber tidak menyebut Overdue sebagai status, tidak ditambahkan ke butir 4.13 dan tidak diberi USULAN; kata "status Overdue" di definisi dan butir 4.8 diganti "kategori Overdue" agar sama dengan sumber. (3) Nonblocking yang murah: butir 4.9 dan 4.11 masuk daftar pelaku USULAN di 4.15; langkah "Pastikan" diganti tindakan konkret (6.1.2 cek respons Google Form, 6.4.5 konfirmasi ke klien); Purpose menyebut Register dan arsip digital FAT, bukan "tepat waktu" dan "dengan aman"; alias AR Tracker dibuang karena tidak dipakai; "data penagihan klien" diganti "data invoice klien" agar tidak bentrok dengan "Data master klien". Tidak dikerjakan: tempat catat tanggal penerimaan (open item 3), pelaku akses butir 4.10 (open item 16), pembersihan catatan penyusunan (open item 17), urutan e-Faktur (open item 2). Render ulang: pass true, fails kosong, warn hanya "6 butir (USULAN)"; OOXML PASSED.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| 1. SOP Billing and Invoicing (Google Doc, 139861 byte) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI | 2026-10-14T08:06:56.942Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content dua kali (tanpa dan dengan includeComments: nol komentar). Dokumen Google native, jadi tidak ada docx untuk didekode; download_file_content tidak dipakai. Tabel metadata dan pengesahan terbaca di teks. Satu gambar di kop tidak dibuka (catatan audit: logo SINUX, UNMEASURED di sesi ini) |
| Kriteria penerimaan | config/checklist.json baris 23 | checklist tidak diukur ulang | Description: "SOP ini menjelaskan proses penerbitan invoce kepada customer/klien". Dipenuhi di Purpose (kalimat pertama), Scope, dan seluruh bagian 6. Ejaan "invoce" di checklist tidak dibawa; dokumen memakai "invoice" dan "klien" (sumber memakai klien, bukan customer atau pelanggan) |
| Pendukung repo (bukan Drive) | config/defaults.json v21, specs/HR-ORG-01.json (daftar jabatan, matriks peran, K-13), specs/HR-JA-01.json (JA-07, JA-10, JA-11), context/audit/iso-sinux-supdocs-fat-2026-10-14.md bagian FAT-SOP-Billing-Invoicing (bagian 5 Catatan kualitas dan celah), specs/ISMS-PRO-01.json (tingkat RESTRICTED) | repo kerja | Dibaca sebagai DATA. Kutipan dari spec lain bisa basi bila dokumen itu berubah |

Kalimat perintah kepada AI di sumber: nihil. Sumber memuat kalimat kewajiban untuk karyawan (misal "wajib"), itu isi SOP, bukan instruksi untuk saya.

## Fakta kunci

| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Tujuan utama: nominal invoice mengikuti PKS, PO, dan BAST yang sah (Purpose dan butir 4.1) | "Memastikan seluruh tagihan (invoice) diterbitkan dengan nominal yang 100% akurat berdasarkan Perjanjian Kerja Sama (PKS), Purchase Order (PO), dan Berita Acara Serah Terima (BAST) yang sah." (1.2 butir 1) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| Validasi tiga arah sebelum e-Faktur Pajak (butir 4.3 dan 6.2) | "Setiap draf invoice wajib melalui proses validasi 3 arah (3-way matching) antara nominal PKS, acuan PO, dan bukti penyerahan BAST sebelum e-Faktur Pajak diterbitkan." (7.2) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |
| Pemisahan pembuat dan penyetuju: Finance Staff tidak mengirim invoice tanpa persetujuan Finance Lead (butir 4.4) | "Staff Finance dilarang keras menerbitkan atau mengirimkan invoice kepada klien tanpa persetujuan (approval) tertulis dari Finance Lead." (4.2) | 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI |

Fakta penting lain (kutipan tanpa penanda tebal; sumber memakai tebal di beberapa tempat):

| # | Fakta di dokumen | Kutipan verbatim sumber | Posisi |
|---|---|---|---|
| 1 | Cakupan transaksi | "SOP ini mencakup seluruh proses penagihan atas penjualan jasa dan pekerjaan proyek perusahaan, meliputi:" lalu "Proyek Pengembangan Sistem & Layanan IT (IT Service Development)." dan "Layanan Konsultasi dan Pekerjaan Berbasis Retainer/Kontrak Periodik" | 2.2, Scope |
| 2 | Syarat dokumen pendukung | "Tagihan hanya dapat diproses dan diterbitkan apabila 4 dokumen pendukung utama telah lengkap dan tervalidasi:" (PKS, PO/SPK, BAST, NPWP Klien) | 5.1, definisi dan butir 4.1 |
| 3 | Data master klien dan Google Form | "Sebelum permohonan penagihan diproses, Tim Sales wajib memastikan klien telah mengisi Google Form Data Subskripsi Klien." | 5.1, butir 4.2 |
| 4 | Tarif PPN (rumusan di dokumen: 12%, USULAN) | "Seluruh penyerahan Jasa Kena Pajak (JKP) dikenakan PPN sebesar 12% sesuai ketentuan peraturan perundang-undangan perpajakan yang berlaku." dan, bertentangan, "penerbitan e-Faktur Pajak (PPN 11%) via portal CoreTax DJP" | 5.2 dan 1.2 butir 3, butir 4.5 |
| 5 | PPh Pasal 23 | "Transaksi penyerahan jasa dipotong PPh Pasal 23 sebesar 2% oleh pihak klien sebagai pemotong pajak." | 5.2, butir 4.6 |
| 6 | Urutan e-Faktur sebelum draf invoice | "Staff Finance mengakses portal CoreTax DJP untuk menerbitkan e-Faktur Pajak Keluar dengan besaran PPN 12% sesuai DPP transaction." (6.2), disusul 6.3 "Finance Lead melakukan verifikasi menyeluruh atas draf invoice, e-Faktur, dan seluruh dokumen pendukung" | 6.2 dan 6.3, butir 6.2 dan 6.3 |
| 7 | Pengiriman soft copy dan hard copy | "Pengiriman berkas fisik (cetak resmi bertanda tangan dan berstempel) melalui kurir hanya dilakukan jika secara eksplisit dipersyaratkan dalam PKS / Kontrak dengan klien." | 5.3, butir 4.7 |
| 8 | TOP standar dan titik awal (sumber tiga versi) | "Standar jangka waktu pembayaran tagihan adalah 14 hari kalender terhitung sejak tanggal invoice resmi dikirimkan kepada klien." (5.3); "terhitung sejak tanggal invoice diterbitkan hingga tanggal jatuh tempo" (3.1); "mencatat tanggal penerimaan resmi sebagai acuan perhitungan tanggal jatuh tempo (TOP)" (6.4) | butir 4.8 |
| 9 | TOP di atas standar | "Penetapan TOP di atas 14 hari kalender wajib mendapatkan persetujuan tertulis dari CEO (Samuel Utomo) sebelum PKS atau PO disepakati." (5.3) dan "draf invoice wajib diteruskan kepada CEO (Samuel Utomo) untuk persetujuan khusus." (6.3) | butir 4.8 dan 6.3 |
| 10 | Batas wewenang Finance Lead | "Finance Lead tidak berwenang mengubah atau memperpanjang jatuh tempo pembayaran klien melebihi 14 hari kalender tanpa persetujuan langsung dari CEO (Samuel Utomo)." | 4.2, butir 4.8 |
| 11 | Jejak audit perubahan | "Setiap perubahan nominal, revisi tanggal, atau pembatalan invoice yang telah disetujui wajib dicatat alasan perubahan beserta bukti persetujuannya dalam sistem pengarsipan." | 4.2, butir 4.9 |
| 12 | Klasifikasi dan akses | "Seluruh dokumen keuangan, daftar harga (rate card), data tagihan klien, dan informasi rekening bank diklasifikasikan sebagai dokumen Rahasia (Confidential)." dan "Akses terhadap folder Google Drive FAT dan Register Penagihan di Google Sheets dibatasi secara ketat hanya untuk personel FAT dan CEO." | 7.1, butir 4.10 |
| 13 | 2FA dan PDF terkunci | "Akun portal CoreTax DJP dan KlikBCA Bisnis wajib menggunakan Otentikasi Dua Faktor (2FA) dan tidak boleh dibagikan kepada pihak yang tidak berkepentingan." dan "Pembagian dokumen tagihan secara digital kepada pihak eksternal/klien wajib menggunakan format PDF terkunci yang tidak dapat diubah (non-editable)." | 7.1, butir 4.7 dan 4.11 |
| 14 | Revisi dan pembatalan | "Jika terdapat kesalahan data atau penolakan tagihan dari klien, Staff Finance wajib menerbitkan Surat Pembatalan / Revisi Invoice serta Faktur Pajak Pengganti melalui portal CoreTax DJP setelah mendapat persetujuan Finance Lead." | 7.2, bagian 9 |
| 15 | Log ketidaksesuaian | "Seluruh riwayat pembatalan dan revisi wajib dicatat dalam log ketidaksesuaian sebagai bahan evaluasi kendali mutu bulanan." | 7.2, butir 4.14 |
| 16 | Arsip digital dan struktur folder | "Seluruh berkas penagihan (Invoice, e-Faktur, PKS, PO, BAST) wajib disimpan dalam format digital (.pdf) di folder Google Drive Departemen FAT." dan "Struktur penamaan folder wajib menggunakan format: [Tahun] / [Nama Klien] / [Nomor Invoice]." | 8.2, butir 4.12 |
| 17 | Register dan status | "Staff Finance wajib memperbarui lembar kerja Google Sheets Register Penagihan & Penjualan secara real-time setiap kali ada perubahan status invoice (Draf, Terkirim, Lunas, atau Cancel)." | 8.2, butir 4.13 |
| 18 | Retensi 10 tahun dan pemusnahan | "Seluruh arsip dokumen penagihan dan bukti perpajakan wajib disimpan selama minimal 10 (sepuluh) tahun sesuai ketentuan perpajakan dan audit ISO 9001 / ISO 27001." dan "pemusnahan dokumen wajib dicatat dalam Berita Acara Pemusnahan Dokumen dengan persetujuan Finance Lead dan CEO." | 8.2, bagian 11 dan butir 4.16 |
| 19 | Pemantauan harian | "Tim Finance melakukan pemantauan harian atas arus kas masuk melalui KlikBCA Bisnis dan melakukan rekonsiliasi piutang setelah pembayaran diterima dari klien." | 6.5, butir 6.5 dan bagian 8 |
| 20 | Overdue | "Invoice yang melewati batas waktu jatuh tempo akan masuk ke dalam kategori Overdue dan diproses sesuai prosedur pemantauan piutang (Accounts Receivable)." | 5.3, bagian 9 |
| 21 | Pengajuan oleh Project Manager | "Project Manager mengajukan permohonan penagihan ke Tim Finance dengan melampirkan BAST yang sudah ditandatangani, acuan PO, PKS, dan mengonfirmasi bahwa data master klien pada Master Sales Sheet / Google Form sudah terisi lengkap." | 6.1, butir 6.1 |
| 22 | Klausul ISO di sumber (dipakai sebagai bahan daftar USULAN) | "ISO 9001:2015 (Sistem Manajemen Mutu): Klausa 8.2 (Persyaratan Produk & Jasa) dan Klausa 8.5 (Pengendalian Operasional Penagihan)." dan "Lampiran A.5.33 (Perlindungan & Kerahasiaan Catatan Keuangan)." | 1.1, bagian 11 |

## 2. Keputusan data dan pemetaan peran

- Approval persis dari prompt dan config/defaults.json: prepared Finance Staff, reviewed Finance Lead, approved Samuel Kristanto Utomo / President Director. Sumber memasang Samuel Kristanto Utomo di ketiga kolom; digantikan.
- process_owner "Finance Lead". Sumber tidak punya medan "Pemilik dokumen"; front matter audit hanya menulis pemilik "Departemen FAT; disusun oleh Samuel Kristanto Utomo (Direktur Utama)". Aturan defaults untuk dokumen tanpa medan itu: jabatan pada kolom reviewed departemen, tanpa nama. USULAN 7.
- Sebutan Samuel di badan dokumen: Direktur Utama (sumber menulis CEO). Nama Samuel tidak muncul di badan, hanya di blok Approved By. COO tidak disebut di sumber, jadi aturan "Direktur (COO)" tidak terpakai (dicek: nol "COO" di docx).
- Tiket (Zammad atau GLPI) dan vault: sumber tidak menyebutnya, jadi tidak muncul di dokumen. Tidak ada kredensial; akun CoreTax DJP dan KlikBCA Bisnis hanya disebut sebagai sistem.
- Klasifikasi dokumen INTERNAL mengikuti worklist; sumber menyebut dokumen keuangan sebagai "Rahasia (Confidential)", istilah yang bukan tingkat SNX-ISMS-PRO-01. Pemetaannya ke RESTRICTED (Internal) ada di butir 4.10 sebagai USULAN 3. Dokumen SOP ini sendiri tetap INTERNAL.

Pemetaan peran sumber ke nama peran di bagian 5 (basis: specs/HR-ORG-01.json):

| Peran di sumber | Nama di dokumen | Dasar |
|---|---|---|
| Tim Sales | Business Development | HR-ORG-01 tidak punya jabatan Sales; JA-07 Business Development (Commercial) punya tugas "serah terima kontrak/PO dan memonitor billing atau collection bersama fungsi terkait" (HR-JA-01). Tafsir, USULAN 5 |
| Pengaju (User / Project Manager) | Project Manager | Matriks peran HR-ORG-01: pemilik gate UAT dan BAST G2, USULAN, belum ada pemegang (K-10). Kata "User" dibuang agar satu istilah |
| Pembuat (Maker / Staff Finance) | Finance Staff | Matriks peran HR-ORG-01: belum dipetakan (K-13) |
| Pemeriksa (Checker / Finance Lead) | Finance Lead | Sama, K-13 |
| Penyetuju (Approver / CEO - Samuel Utomo) | Direktur Utama | HR-ORG-01 JA-01 dan data_conflicts |
| Tim Finance (5.2, 6.5) | Finance Staff | Tafsir: pelaku pada langkah yang sama di 6.x adalah Staff Finance |
| Tim FAT, personel FAT | tetap "personel FAT" di butir 4.10 | Kelompok akses, bukan peran prosedur |
| PIC AP, PIC Finance/AP, PIC Proyek | PIC Finance/AP klien, PIC Proyek klien | Sumber memakai dua sebutan untuk kontak yang sama; satu bentuk dipakai |
| Sebutan "Pembuat", "Pemeriksa", "Penyetuju", "Pengaju" | tidak dipakai | Nama jabatan dipakai langsung agar satu istilah per peran |

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Kontrol dokumen kosong; judul tabel beda dengan judul sampul | Teratasi oleh template: nomor SNX-FAT-SOP-01, Draft, rev 00, tanggal kosong, Document Title "Finance, Accounting & Tax - SOP Billing & Invoicing". Medan Perusahaan di sumber diganti Company Name template |
| 2 | Satu orang di Disusun, Diperiksa, Disetujui | Diperbaiki: tiga penanda tangan berbeda (defaults) |
| 3 | Ejaan Samuel dan sebutan CEO lawan Direktur Utama | Diperbaiki: Kristanto di blok Approved By; Direktur Utama di badan (data_conflicts) |
| 4 | PPN 11% di 1.2 lawan 12% di sepuluh tempat | Diperbaiki: satu rumusan di butir 4.5, "PPN 12% (USULAN)"; bagian lain menyebut PPN tanpa angka dan merujuk 4.5. Angka 11% dibuang. FAT belum memutus, jadi tetap USULAN 1 |
| 5 | Titik awal TOP tiga versi (diterbitkan, dikirim, diterima) | Dipilih satu: sejak tanggal invoice (USULAN 2, butir 4.8). Alasan: 3.1 memakai tanggal invoice dan 6.2 menaruh tanggal jatuh tempo di draf invoice, yang hanya mungkin bila titik awalnya sudah diketahui saat draf disusun. Tanggal penerimaan (6.4) tetap dicatat sebagai bukti penerimaan, bukan titik awal. Keputusan ini mengubah fungsi langkah 6.4 di sumber; FAT yang memutus |
| 6 | "4 dokumen pendukung" didefinisikan tiga cara; 8.1 mendaftar lima | Diperbaiki: empat dokumen = PKS, PO/SPK, BAST, NPWP klien (5.1 dan 9.2 sepakat), didefinisikan sekali di bagian 3. Hasil Google Form dipisah sebagai syarat data master klien (butir 4.2). e-Faktur Pajak adalah keluaran proses, bukan syarat, dan tetap ada di daftar arsip (butir 4.12). Putaran 1: NPWP klien ditambahkan ke lampiran langkah 6.1.4 dan diagram, mengikuti 9.2 sumber ("Project Manager melengkapi PKS, PO, BAST, dan NPWP Klien") |
| 7 | Urutan: 3-way matching sebelum e-Faktur (7.2), e-Faktur sebelum approval Finance Lead (6.2 dan 6.3), e-Faktur "pada saat penerbitan invoice" (5.2) | Sebagian diperbaiki: 3-way matching dipasang sebelum e-Faktur sebagai langkah pertama butir 6.2, dan diterapkan atas permohonan penagihan (bukan atas draf invoice, karena draf di sumber baru dibuat sesudah e-Faktur). Urutan e-Faktur lalu approval Finance Lead tidak dibalik karena menyangkut keputusan pajak; Faktur Pajak Pengganti ditangani di bagian 9. Risiko ada di open item 2 |
| 8 | Tidak ada SLA waktu per tahap; tidak ada prosedur Overdue; tidak ada collection | Tabel SLA hanya memuat angka sumber (pemantauan harian, pembaruan register saat status berubah, evaluasi log bulanan). Overdue dikecualikan dari scope dan ditulis di bagian 9 tanpa kontrol baru; rujukannya SOP Account Receivable & Collection (checklist baris 24, status on review, belum bernomor), sehingga dokumen menulis "sedang dalam peninjauan", bukan "belum berdokumen" (koreksi putaran 1). Open item 4 dan 6 |
| 9 | Lampiran 1 sampai 4 dirujuk tanpa isi; gambar hanya logo | Lampiran 1, 2, 4 dicantumkan di Dokumen terkait sebagai "Belum bernomor" dengan sebutan "SOP Billing dan Invoicing versi tim" (isi tidak ada, open item 12). Lampiran 3 (flowchart) digantikan diagram bagian 7 yang saya turunkan dari teks sumber, tanpa cabang yang tidak ada di teks: cabang "Tidak sesuai" berhenti di bagian 9 dan tidak kembali ke penyusunan draf (sumber tidak menyatakannya) |
| 10 | Scope tidak menyebut penjualan perangkat atau lisensi | Tidak diputus: scope menulis dua jenis transaksi dari sumber, dan penjualan lain masuk open item 7. Pengecualian yang ditulis berasal dari kriteria baris (invoice kepada klien): invoice masuk dari vendor, pelaporan pajak, tindak lanjut Overdue |
| 11 | Finance Lead tunggal; tidak ada pengganti; Finance Lead dan Finance Staff tidak ada di HR-JA-001 | Tidak ada kontrol pengganti yang dikarang (aturan RUNBOOK §6 dan prompt: hanya bila ada di sumber). Peran dipakai apa adanya dengan catatan "belum dipetakan (K-13)" di tabel peran. Open item 5 |
| 12 | Dokumen berlabel Rahasia, SOP sendiri tanpa klasifikasi | Diperbaiki: INTERNAL untuk SOP, RESTRICTED (Internal) untuk data yang diatur (butir 4.10, USULAN 3) |
| 13 | Istilah "Klausa" dan "Lampiran A.5.33"; tidak ada pemetaan klausul lain | Diperbaiki: bagian 11 memuat 7.5.3, 8.2, 8.5, 8.6 (ditambah putaran 1 atas saran verifikator), Annex A 5.12, 5.15, 5.33, 8.5 dengan satu label "(USULAN, dikonfirmasi konsultan)". Judul klausul berasal dari pengetahuan standar penyusun, bukan teks sumber, dan tidak dicocokkan dengan teks standar (UNMEASURED) |
| 14 | Sisa "$\rightarrow$" di 9.2 | Tidak dibawa. Bagian 9.2 sumber (ringkasan alur) tidak disalin karena mengulang butir 6 |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Tujuan 2 sumber menjanjikan "pengakuan pendapatan (revenue recognition)" tetapi tidak ada langkah akuntansi di prosedur | Tidak dibawa ke Purpose; Purpose hanya menjanjikan yang punya langkah. Bila FAT ingin pengakuan pendapatan masuk SOP ini, itu proses baru (open item 13) |
| B | Persetujuan TOP lebih dari 14 hari: 5.3 "sebelum PKS atau PO disepakati", 6.3 "draf invoice diteruskan ke CEO" | Dua-duanya dipertahankan (butir 4.8 dan 6.3). Open item 9 |
| C | Retensi 10 tahun diberi dasar "ketentuan perpajakan dan audit ISO 9001 / ISO 27001" | Dasar itu tidak dibawa; hanya "Minimal 10 tahun". Sumber tidak mengutip pasal, dan penyusun tidak punya sumber bahwa ISO menetapkan masa simpan. Open item 11 |
| D | Frasa penekan di sumber: "tanpa terkecuali", "dilarang keras", "terpercaya", "secara ketat" | Dibuang; aturannya tetap |
| E | "Invoice", "Surat Tagihan", "tagihan", "penagihan" bergantian untuk dokumen dan kegiatan | Satu istilah: invoice (dokumen), penagihan (kegiatan), berkas penagihan (kumpulan berkas). "Respon" jadi "respons" (baku) |
| F | Staff Finance membubuhkan tanda tangan dan stempel pada invoice cetak (6.4) | Dipertahankan sesuai sumber (langkah 6.4.3). Hak tanda tangan menurut HR-ORG-01 ada di Authority Matrix yang belum bernomor. Open item 10 |
| G | "Sistem pengarsipan" di 4.2 tidak dijelaskan | Dibaca sama dengan arsip digital FAT di 8.2 (butir 4.9). Tafsir |

## 4. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kalimat pasif sumber diberi pelaku: Finance Staff untuk pencocokan tiga arah, penyimpanan arsip, pencatatan log, dan pencatatan pemusnahan; Finance Lead untuk evaluasi log bulanan dan pemilik rekaman. Semuanya dikumpulkan dalam butir 4.15 dengan satu label (USULAN 4). Putaran 1 menambahkan pemantauan Overdue oleh Finance Staff (sumber 5.3 pasif) ke daftar itu.
2. Langkah 6.1.6 Finance Staff memeriksa dokumen pendukung dan data (sumber 6.1 hanya menyebut data; 5.1 mensyaratkan dokumen lengkap dan tervalidasi tanpa menyebut pelaku).
3. Bukti Potong PPh Pasal 23 diberi masa simpan "Minimal 10 tahun" karena masuk "bukti perpajakan" di 8.2. Lokasi berkasnya tidak disebut sumber.
4. "Tim Finance" di 5.2 dan 6.5 dibaca sebagai Finance Staff.
5. Kolom Register dan Master Sales Sheet: sumber menyebut Register sebagai lembar Google Sheets; platform Master Sales Sheet tidak disebut, jadi tidak ditulis.
6. Definisi umum (2FA, DPP, Faktur Pajak Pengganti, Klien, Overdue, Piutang usaha) adalah penjelasan penyusun, bukan kalimat tim.
7. Pengecualian scope "invoice yang SINUX terima dari vendor" saya tarik dari pembedaan terhadap baris checklist FAT lain (SOP Payment and Disbursement Approval, status "on review", belum bernomor), bukan dari sumber. SNX-FAT-SOP-05 dipakai karena sudah bernomor di worklist.
9. Putaran 2: masa simpan "Minimal 10 tahun" dipakai untuk Register Penagihan dan Penjualan, persetujuan tertulis, dan log ketidaksesuaian karena ketiganya dibaca sebagai bagian dari "arsip dokumen penagihan" di 8.2. Master Sales Sheet (data master, bukan dokumen penagihan) dan Berita Acara Pemusnahan Dokumen (tidak disebut sumber) tetap "Belum ditetapkan".
8. Untuk PPN: pengetahuan umum penyusun (UNMEASURED, tidak diverifikasi ke peraturan dan tidak masuk dokumen) menyebut bahwa tarif 12% dan dasar pengenaannya bisa berbeda antara barang mewah dan jasa lain. Itu alasan angka 12% tetap USULAN dan diserahkan ke FAT atau konsultan pajak.

## USULAN

Enam butir bertanda "(USULAN)" di dokumen (lint menghitung enam, termasuk baris definisi label itu sendiri) ditambah label klausul ISO dan process_owner. Total tujuh butir keputusan.

| # | Butir USULAN | Di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Rumusan tunggal PPN 12% menggantikan 11% di satu tempat sumber | Butir 4.5 | FAT (dengan konsultan pajak) |
| 2 | Titik awal TOP = tanggal invoice | Butir 4.8 | FAT |
| 3 | Data keuangan, daftar harga, data penagihan klien, dan rekening bank = RESTRICTED (Internal) menggantikan "Rahasia (Confidential)" | Butir 4.10 | Fani (pemilik skema SNX-ISMS-PRO-01 di sisi Operation dan ISMS) |
| 4 | Penetapan pelaku pada butir 4.3, 4.9, 4.11, 4.12, 4.14, 4.16, pemantauan Overdue (bagian 9), dan Finance Lead sebagai pemilik rekaman | Butir 4.15 dan tabel rekaman | FAT, dikukuhkan owner |
| 5 | Tim Sales dipetakan ke Business Development | Tabel peran bagian 5 | owner |
| 6 | Daftar klausul ISO 9001:2015 (7.5.3, 8.2, 8.5, 8.6) dan ISO/IEC 27001:2022 (Annex A 5.12, 5.15, 5.33, 8.5), label "(USULAN, dikonfirmasi konsultan)" | Bagian 11, Acuan standar | owner, diteruskan ke konsultan |
| 7 | Process owner = Finance Lead (sumber tanpa "Pemilik dokumen") | Identity Document | owner |

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Rumusan tarif PPN: 12% atau 11%, dan dasar pengenaannya. Sumber menulis keduanya. Perlu keputusan tertulis agar USULAN 1 bisa dicabut | FAT |
| 2 | e-Faktur Pajak terbit sebelum approval Finance Lead (butir 6.2 lalu 6.3), padahal Finance Staff dilarang menerbitkan invoice tanpa approval (butir 4.4) dan koreksi butuh Faktur Pajak Pengganti. Apakah approval dipindah sebelum e-Faktur | FAT |
| 3 | Titik awal TOP (USULAN 2) dan lokasi pencatatan tanggal penerimaan (butir 6.4.6): sumber tidak menyebut tempatnya | FAT |
| 4 | Tidak ada target waktu per tahap penerbitan invoice (pengajuan, e-Faktur, pemeriksaan, pengiriman). SOP Tax di folder yang sama memakai 1 hari per langkah; angka itu tidak saya pakai di sini karena lingkupnya lain | FAT |
| 5 | Finance Lead berhalangan: pengganti tidak diatur. Finance Lead dan Finance Staff belum dipetakan ke jabatan (HR-ORG-01 K-13) | owner |
| 6 | Tindak lanjut invoice Overdue: "prosedur pemantauan piutang" di sumber adalah SOP Account Receivable & Collection (checklist baris 24), status on review dan belum bernomor. Dokumen menyebutnya dengan judul; kode SNX perlu ditambahkan ke bagian 2, 9, dan 11 setelah terbit | FAT |
| 7 | Penjualan perangkat atau lisensi tidak disebut di scope sumber. Masuk SOP ini atau tidak | FAT |
| 8 | Permohonan penagihan yang tidak lengkap: sumber hanya melarang memproses, tanpa menyebut siapa memberi tahu Project Manager dan dalam berapa lama | FAT |
| 9 | Persetujuan Direktur Utama atas TOP lebih dari standar: sebelum PKS atau PO disepakati (5.3) atau saat draf invoice (6.3). Keduanya dipertahankan | FAT dan Samuel |
| 10 | Staff Finance menandatangani dan menstempel invoice cetak (sumber 6.4). Apakah itu sesuai Authority Matrix yang belum bernomor | Samuel |
| 11 | Lokasi rekaman selain arsip PDF (persetujuan tertulis, Register, Master Sales Sheet, log, Berita Acara Pemusnahan Dokumen) belum ditetapkan, dan masa simpan Master Sales Sheet serta Berita Acara Pemusnahan Dokumen juga belum. Dasar hukum retensi 10 tahun belum dikutip, dan FAT perlu menegaskan bahwa Register, persetujuan tertulis, dan log termasuk "arsip dokumen penagihan" (lihat koreksi putaran 2) | FAT dan Legal |
| 12 | Lampiran 1 (Form Permohonan Penagihan), 2 (Templat Invoice Resmi FAT), dan 4 (Format Register) tidak ada isinya di sumber. Lampiran 3 digantikan diagram bagian 7 yang diturunkan dari teks; perlu disahkan FAT | FAT |
| 13 | Tujuan "pengakuan pendapatan" di sumber tidak punya langkah. Bila diinginkan, perlu proses baru atau rujukan ke SOP akuntansi | FAT |
| 14 | SNX-FAT-SOP-05 (Tax) juga menyebut Faktur Pajak Keluaran dalam scope-nya; penerbitan e-Faktur di dokumen ini perlu diselaraskan dengan dokumen itu agar tidak ganda | FAT |
| 15 | Konfirmasi ejaan dan sebutan Samuel (Kristanto, Direktur Utama; sumber memakai CEO) dan kolom pengesahan sumber yang memasang satu orang di tiga peran | owner atau Samuel |
| 16 | Pembatasan akses folder Google Drive Departemen FAT dan Register (butir 4.10): sumber tidak menyebut siapa yang memberi dan mencabut akses. Tidak ditulis karena butuh pelaku baru (FAT). | FAT |
| 17 | Sebelum pengesahan, catatan penyusunan di badan dokumen (label USULAN, "versi tim", "isinya belum tersedia", butir 4.15) perlu dibersihkan atau diputus supaya tidak terbaca sebagai kebijakan (saran verifikator putaran 2). | FAT dan owner |

## 5. Dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama punya empat tanda, tiga sudah saya perbaiki dan satu saya biarkan:
   - Kalimat "Peran dari dokumen sumber; belum dipetakan ke jabatan..." muncul dua kali di tabel peran dengan kata yang sama. Diperbaiki: dipersingkat menjadi "Belum dipetakan ke jabatan di SNX-HR-ORG-01 (butir K-13)."
   - Butir 4.3 dan langkah 6.2.1 menyalin kalimat 3-way matching yang sudah ada di definisi, dan butir 4.3 menulis "pada setiap draf invoice sebelum e-Faktur" yang bertabrakan dengan urutan 6.2 (draf dibuat sesudah e-Faktur). Diperbaiki: definisi memegang artinya, butir 4.3 memegang aturan atas permohonan penagihan, langkah hanya merujuk.
   - Butir 4.1 dan 4.11 memakai bentuk pasif tanpa pelaku ("Invoice hanya diproses...", "Akun ... memakai 2FA"), dan 2FA dan PDF terkunci bercampur dalam satu butir. Diperbaiki: pelaku Finance Staff, PDF terkunci dipindah ke butir 4.7.
   - Dibiarkan: hampir semua butir kebijakan dibuka dengan "Finance Staff" dan kolom Output memakai pola "Hasil pemeriksaan ...". Itu mengikuti sumber (pelaku tunggal per langkah) dan menjadi nama rekaman; mengganti variasi hanya agar terdengar manusiawi bisa mengaburkan pelaku. Satu lagi sisa: daftar titik koma yang padat di sel tanggung jawab Finance Staff dan Finance Lead mengikuti pola kalimat sumber 4.1.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Diperiksa satu per satu terhadap tabel Fakta kunci dan tabel peran:
   - Angka: 14 hari kalender, 10 tahun, 2%, 12% berasal dari sumber (12% berlabel USULAN). Tidak ada angka lain di dokumen. Satu angka dari draf pertama, baris SLA "pemantauan pelunasan terhadap jatuh tempo", saya hapus karena duplikat dan menambah aktivitas yang tidak disebut sumber.
   - Nama: Samuel Kristanto Utomo hanya di blok Approved By (defaults). Tidak ada nama orang lain. Nama peran dari HR-ORG-01; Business Development adalah tafsir (USULAN 5).
   - Tanggal: nol.
   - Tanpa sumber tertulis tetapi ada di dokumen: judul klausul ISO (pengetahuan standar penyusun, UNMEASURED, di bawah label USULAN); pembedaan pengecualian scope terhadap invoice vendor (tafsir dari kriteria baris); definisi umum 2FA, DPP, Faktur Pajak Pengganti, Klien; penunjukan pelaku di butir 4.15 (USULAN 4); klasifikasi RESTRICTED (Internal) (USULAN 3).
