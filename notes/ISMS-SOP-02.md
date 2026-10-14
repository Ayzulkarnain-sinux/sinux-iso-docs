# Catatan penyusun ISMS-SOP-02: SOP User Access Control & Authorization

Status: DRAFTED (spec + notes ada). Spec: specs/ISMS-SOP-02.json. Mode sop, aksi T1, nomor SNX-ISMS-SOP-02 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber, audit_class B, catatan worklist "PILOT format".

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-SOP-02_SOP_User_Access_Control_Authorization.docx (167959 byte) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT | 2026-10-13T06:09:01Z (get_file_metadata, dicek ulang hari ini) | read_file_content (teks), download_file_content (docx didekode di /tmp/pen-ISMS-SOP-02/, gambar diagram rId26.png dibuka, comments.xml dan footnotes.xml kosong) |
| Kriteria penerimaan | config/checklist.json baris 84 | checklist modifiedTime 2026-10-14T17:47:13.611Z | Description hanya nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001 "7.1.3" dan ISO/IEC 27001 "5.15, 5.16, 5.17, 5.18, 8.2, 8.3, 8.5" |
| Pendukung (bahan): SNX-ISMS-REG-04, REG-01, SOA-01, PRO-01, SOP-01, SOP-04, POL-OPS-001, SNX-OPS-SOP-02 dan FRM-06 (judul saja) | lihat context/audit | salinan audit 13 sampai 14 Okt | Dibaca lewat salinan context/audit (DATA), bukan dari Drive. POL-OPS-001 dan PRO-OPS-001 tidak dibuka di Drive; PRO-OPS-001 tidak dipakai |

Peringatan jujur: isi REG-04, REG-01, SOA-01 dalam notes ini dikutip dari salinan audit, bukan dari berkas Drive terbaru. Bila tim sudah mengubahnya, kutipan di bawah bisa basi.

## 2. Fakta penting dan kutipan sumber

| # | Fakta di dokumen | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "SOP ini mengatur pemberian, perubahan, peninjauan, dan pencabutan hak akses ke sistem SINUX dan sistem pelanggan yang dikelola SINUX, berdasarkan prinsip least privilege dan need-to-know, agar hanya orang yang berwenang yang dapat mengakses informasi dan sistem." | Bagian 1 (kalimat tim dipertahankan utuh) |
| 2 | Scope | "Berlaku untuk seluruh akun manusia dan service account pada:" lalu daftar sistem internal dan sistem pelanggan | Bagian 2 |
| 3 | Satu orang satu akun, break-glass | "akun bersama (shared) dilarang, kecuali akun break-glass yang disimpan di password manager dan setiap pemakaiannya dicatat." | Bagian 4, definisi, pengecualian |
| 4 | Privileged lewat Jumphost | "Akses privileged (root, administrator, admin panel) diberikan terpisah dari akun harian dan hanya melalui Jumphost bila sistem mendukung." dan "Akses production pelanggan hanya melalui Jumphost SINUX yang merekam sesi." | Bagian 4, 6.7 |
| 5 | Permintaan di Service Hub | "Pemohon atau atasannya mengajukan permintaan di Service Hub (kategori Access atau Permission): nama, peran, sistem, tingkat akses, alasan, dan masa berlaku." | 6.1 langkah 1 |
| 6 | Approval privileged ke pelanggan | "Akses privileged ke sistem pelanggan butuh approval Head of Operation, dan bila kontrak mensyaratkan, persetujuan pelanggan." | 6.1 langkah 4, pengecualian |
| 7 | Mutasi 5 hari kerja | "akses lama yang tidak relevan dicabut paling lambat 5 hari kerja." | 6.4, SLA |
| 8 | Leaver | "Saat pemberhentian, semua akses dicabut paling lambat pada hari terakhir kerja; untuk pemberhentian mendadak, segera." | 6.5, SLA, pengecualian |
| 9 | MFA | "MFA wajib untuk email, password manager, Jumphost, console cloud, Cloudflare, dan semua akses dari internet ke sistem administratif bila sistem mendukung." | 6.2 langkah 1 |
| 10 | Password | "Password minimal 12 karakter, unik per sistem, disimpan hanya di password manager." | 6.2 langkah 2 dan 3 |
| 11 | Review | "akses privileged setiap triwulan, akses biasa setiap semester." dan "Temuan (akun yatim, hak berlebih, akun tidak aktif lebih dari 90 hari) ditindaklanjuti paling lambat 10 hari kerja." | 6.6, SLA, definisi |
| 12 | Service account | "kredensialnya dirotasi minimal tahunan atau saat pengelola berganti." | 6.6 langkah 5, SLA |
| 13 | Sampling log | "log ditinjau sampling triwulanan oleh Lead SOC." | 6.7 langkah 3, SLA, peran Lead SOC |
| 14 | Retensi | "User Access Register & Periodic Access Review | SNX-ISMS-REG-04 | 3 tahun", "Tiket permintaan akses | Service Hub | 3 tahun", "Log sesi Jumphost | Jumphost | Sesuai kapasitas, minimal 90 hari" | Bagian 11 |
| 15 | Target kinerja | "Akses dicabut pada hari terakhir kerja | 100%", "Review akses privileged triwulanan terlaksana | 100%", "Temuan review ditutup dalam 10 hari kerja | 95%", "Sistem administratif dengan MFA aktif | 100% dari sistem yang mendukung" | Bagian 8 (kolom SLA / Timing, tanpa slot KPI di template) |
| 16 | Pemilik dokumen | "Pemilik dokumen | Head of Operation" | meta.process_owner (tanpa nama) |
| 17 | Klasifikasi | "Klasifikasi | RESTRICTED (Internal)" | meta.classification; footer berlabel otomatis |
| 18 | Matriks akses | "Matriks ini acuan awal (USULAN); pemilik sistem menetapkan detailnya di SNX-ISMS-REG-04." | Bagian 4, empat baris peran + satu baris catatan |
| 19 | Vault | Sumber SOP-02 hanya menulis "password manager". Status dari defaults: "menunggu konfirmasi Ops" | Definisi Password manager |
| 20 | Tiket | Owner 14 Okt (config/defaults.json): "sistem tiket zammad untuk ops, glpi untuk generalist". REG-01 AST-002: "Tiket GMF dedicated dan permintaan internal" | Definisi Service Hub dan Zammad |

## 3. Pemetaan klausul ISO (kriteria)

| Klausul | Di bagian 11 | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 7.1.3 | Ya (acuan standar) | (tidak diminta; sistem tercakup di bagian 2) | |
| 27001 5.15 Access control | Ya | Least privilege, Need-to-know | 6.1 |
| 5.16 Identity management | Ya | Satu orang satu akun; setiap akun tercatat di REG-04 | 6.1, 6.3 |
| 5.17 Authentication information | Ya | Autentikasi, mengarah ke 6.2 | 6.2 |
| 5.18 Access rights | Ya | Least privilege; Hak akses | 6.4, 6.5, 6.6 |
| 8.2 Privileged access rights | Ya | Akses privileged | 6.7 |
| 8.3 Information access restriction | Ya | Need-to-know; matriks acuan (knowledge base: data di luar scope tidak tampil) | 6.1 |
| 8.5 Secure authentication | Ya | Autentikasi (MFA) | 6.2 |
| 8.18 (hanya di sumber 7.7 dan SoA) | Ya, sebagai tambahan | | 6.7 |

## 4. Keputusan data

- Approval: prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo, persis dari config/defaults.json. Sumber menulis "Disusun oleh Head of Operation", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain". Defaults mengalahkan sumber (D2). Badan dokumen tidak menyebut COO, jadi aturan "Direktur (COO)" tidak terpakai. Direktur Utama juga tidak disebut di badan.
- Department "Operation" (department_labels ISMS), padahal sumber menulis "Information Security".
- Tiket: izin akses tetap lewat Service Hub (GLPI) karena sumber menyebutnya; batas "generalist" belum dirinci owner, lihat open item 4.
- Vault: ditulis "password manager (vault)" dengan "Status operasional: menunggu konfirmasi Ops". Tidak ada klaim aktif atau belum live.
- Nama peran bagian 5 memakai peran sumber, ditambah Lead SOC, Pemohon, Pengguna akun (lihat tafsir). Atasan langsung pemohon dipendekkan jadi Atasan langsung agar PIC pendek dan konsisten; HR atau atasan jadi HR atau atasan langsung.

## 5. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1JoSiwoM...)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Matriks acuan awal merujuk REG-04 yang tidak memuat matriks per sistem dan peran; dropdown Level REG-04 (Read-only, Operator, Admin, Privileged) tidak memuat istilah matriks (Agent, Group admin, Analyst, Collection) | Sebagian diperbaiki: kalimat diganti menjadi "Pemilik sistem menetapkan tingkat akses tiap akun; Administrator sistem mencatatnya di kolom Level akses SNX-ISMS-REG-04" (kolom itu ada di REG-04), dan 6.1 punya langkah penetapan level oleh Pemilik sistem serta pencatatan oleh Administrator sistem. Matriks tetap berlabel (USULAN). Selisih istilah menjadi open item untuk pemilik REG-04, tidak bisa diperbaiki dari dokumen ini |
| 2 | Diagram: cabang "Masih dibutuhkan? tidak" menjadi "Cabut akses pada hari terakhir kerja", padahal frasa itu hanya milik pemberhentian | Diperbaiki: diagram baru memisahkan jalur mutasi atau pemberhentian (5 hari kerja atau hari terakhir kerja) dan jalur review (ubah atau cabut paling lambat 10 hari kerja). Tenggat 10 hari untuk keputusan Ubah atau Cabut adalah tafsir, didukung REG-04 sheet Review Periodik (status "Terbuka" sampai tindak lanjut selesai) dan Cara pakai B21; lihat open item 6 |
| 3 | Tidak ada batas waktu pembuatan akun dan tidak ada SLA respons permintaan | Diisi sebagai (USULAN): pembuatan akun 1 hari kerja, keputusan permintaan 2 hari kerja sesudah konfirmasi atasan. Angka patokan, bukan sumber tim |
| 4 | Persetujuan pelanggan hanya bersyarat | Dipertahankan apa adanya (langkah 4 dan baris pengecualian). Tidak diubah menjadi wajib karena itu keputusan kontrak, bukan penyusun |
| 5 | Retensi log Jumphost minimal 90 hari vs sampling triwulanan | Tidak diperbaiki diam-diam: teks sumber dipertahankan, masuk open item 5 dengan opsi (retensi lebih panjang atau sampling lebih sering) untuk Head of Operation dan Lead SOC |
| 6 | Header ISO tidak memuat 8.18, butir 7.7 memakai "A 8.2, 8.18"; 5.15, 5.16, 8.3 tanpa butir bertanda | Diperbaiki sebagian: 7 klausul kriteria dicantumkan di bagian 11 dan dipetakan di bagian 4 (tabel bagian 3 di atas). 8.18 dipertahankan sebagai tambahan karena SoA memetakannya ke SOP-02; kecocokan isi 8.18 (utility program) dengan perekaman sesi privileged tidak saya nilai, open item 9 |
| 7 | Rujukan SNX-OPS-SOP-02, SNX-ISMS-SOP-04, REG-04, REG-01, SNX-OPS-FRM-06 | Semua ada di korpus; dicantumkan di bagian 11 dengan judul dari korpus |
| 8 | Peran Lead SOC dan Service Delivery Manager tidak ada di tabel peran; "SD dan PM" tanpa definisi | Lead SOC ditambahkan ke bagian 5 (dipakai di 6.7 dan SLA). "NOC, SOC, SD dan PM" didefinisikan dari POL-OPS-001. Service Delivery Manager tidak dipakai di SOP ini, jadi tidak ditambahkan |
| 9 | Pengesahan kosong, dua baris riwayat revisi bertanggal sama berstatus Menunggu | Teratasi oleh template: satu baris Revision 00, Effective Date kosong, Signature kosong |
| 10 | "ISO/ISMS Coordinator" vs "ISMS Coordinator" | Moot: pemeriksa memakai defaults (Fani); peran di badan dokumen "ISMS Coordinator" saja |
| 11 | Sheet "Periodic Review" vs nama asli "Review Periodik" di REG-04 | Diperbaiki: dokumen memakai "Review Periodik" |
| 12 | Masa simpan header "Berlaku sampai digantikan" vs tabel "3 tahun" | Template tidak punya field itu; hanya tabel bagian 11 yang berlaku (3 tahun, 3 tahun, minimal 90 hari) |
| 13 | Rujukan internal AI | Tidak ada di sumber SOP-02; lint lulus |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kalimat pasif sumber diberi pelaku dari tabel peran: Administrator sistem memberi akses vendor, mencatat akun pihak ketiga, merotasi kredensial, mencabut akses sementara tim proyek; Pengguna akun mengembalikan aset, melaporkan kredensial terpapar, mengganti kredensial awal; Pemilik sistem meninjau pemilik dan tujuan service account.
2. Kolom Authority tabel peran tidak ada di sumber. Isinya diturunkan dari kalimat sumber (mis. "approver", "sesuai approval", "pemohon akses tidak menyetujui aksesnya sendiri"). Kolom ISMS Coordinator dan Lead SOC paling tipis.
3. Titik awal 5 hari kerja mutasi dibaca dari mutasi itu sendiri ("sesudah mutasi"); sumber tidak menyebut titik awal.
4. Lokasi record REG-04 "Google Drive": sumber SOP-02 hanya memberi nomor; REG-04 adalah berkas Drive. Pemilik record Head of Operation diambil dari REG-01 (AST-001, AST-002, AST-004 dan REG-04: pemilik Head of Operation).
5. Pencatatan akun pihak ketiga di REG-04 dengan status personel "Vendor atau partner": sumber SOP-02 hanya menulis "dicatat sebagai akun pihak ketiga"; REG-04 punya nilai dropdown itu.
6. Baris pengecualian "Sistem tidak mendukung MFA" dan "Sistem tidak mendukung akses lewat Jumphost" dibaca dari frasa "bila sistem mendukung". Dokumen tidak menambahkan kontrol pengganti.
7. Pemilik sistem juga memutuskan penolakan dan mencatat alasan di tiket (diagram sumber: "Ditolak: catat alasan di tiket", pelaku tidak disebut).
8. Nama klausul Annex A dalam bagian 11 dari SoA (salinan audit); "7.1.3 (Infrastruktur)" dari standar ISO 9001:2015, bukan dari sumber tim.
9. Definisi umum (MFA, service account, akun yatim, hak berlebih) adalah penjelasan penyusun, bukan kalimat tim.
10. "Head of Operation meninjau dokumen ini setiap tahun": dari review_period YEARLY di defaults, pelaku dari "Pemilik SOP".
11. Putaran perbaikan: baris pengecualian bagian 9 diberi pelaku dari bagian 5. Pencatatan pemakaian akun break-glass oleh Pengguna akun adalah tafsir (sumber pasif, tanpa pelaku dan tanpa lokasi catatan).
12. Putaran perbaikan: langkah "Tetapkan level akses" oleh Pemilik sistem dan pencatatan level oleh Administrator sistem diturunkan dari "pemilik sistem menetapkan detailnya" dan "Administrator ... mencatat di register".
13. Putaran perbaikan: Lead NOC ditambahkan ke bagian 5 karena sumber menulis "approval Lead" untuk kolom "Lead NOC dan SOC"; kedua Lead diberi wewenang itu.
14. Putaran perbaikan: baris SLA "Tindak lanjut keputusan Ubah atau Cabut" memakai 10 hari kerja dari Cara pakai SNX-ISMS-REG-04 ("tindak lanjut maksimal 10 hari kerja"), bukan dari sumber SOP-02; target 95% tetap hanya pada "temuan review".

## 7. Daftar USULAN (lint menghitung 5 butir berlabel)

| # | Butir | Letak | Alasan | Pemutus |
|---|---|---|---|---|
| U1 | Matriks tingkat akses acuan per peran | Bagian 4 | Label dari sumber ("acuan awal (USULAN)"), dipertahankan | Pemilik sistem, Head of Operation |
| U2 | Keputusan permintaan akses 2 hari kerja sesudah konfirmasi atasan | Bagian 8 | Menutup cacat "tidak ada SLA respons"; angka tanpa sumber | Head of Operation, Fani |
| U3 | Pembuatan akun 1 hari kerja sesudah approval | Bagian 8 | Menutup cacat "tidak ada batas waktu pembuatan akun"; angka tanpa sumber | Head of Operation, Fani |
| U4 | Catatan hasil sampling log: Google Drive, pemilik Lead SOC | Bagian 11 | Sumber tidak menentukan rekaman sampling | Head of Operation, Lead SOC |
| U5 | Retensi catatan sampling 3 tahun | Bagian 11 | Disamakan dengan retensi REG-04 dan tiket | Head of Operation |

## 8. Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju dokumen: sumber COO (Amirull), template dan defaults Samuel. Defaults dipakai | Owner atau Samuel |
| 2 | Head of Operation belum dipetakan ke jabatan nyata (Struktur Organisasi HR-ORG-01 belum DONE); reviewer Fani = VP Tech Operation and Services. Pemilik SOP dan pemilik record tetap "Head of Operation" | Owner, Fani |
| 3 | Status password manager (vault): REG-01 "Aktif", REG-02 dan KB "belum live". SOP mewajibkan password disimpan di password manager; bila belum live, SOP belum bisa dipatuhi (REG-02 ISR-001 menyebut kredensial masih di Google Sheets dan Excel; RTP-001 target 2027-03-31) | Ops |
| 4 | Batas "generalist" lawan Ops untuk permintaan akses: sumber memakai Service Hub (GLPI); belum ada keputusan apakah staf Ops memakai Zammad. POL-OPS-001 P-08 masih "semua tiket di GLPI" | Owner |
| 5 | Log Jumphost minimal 90 hari tidak menjamin cakupan sampling triwulanan | Head of Operation, Lead SOC |
| 6 | Tenggat 10 hari kerja untuk keputusan Ubah atau Cabut hasil review adalah tafsir (sumber hanya menyebut "temuan") | Head of Operation |
| 7 | Siapa yang meminta persetujuan pelanggan (bila kontrak mensyaratkan) tidak ditentukan sumber | Head of Operation |
| 8 | Sumber hanya menulis "approval Lead" untuk restore production Acronis. Dokumen memakai "Lead NOC atau Lead SOC" dan kedua peran ada di bagian 5; tafsir ini perlu konfirmasi | Head of Operation |
| 9 | SoA SNX-ISMS-SOA-01 memetakan 8.18 dan 8.3 ke "SNX-ISMS-SOP-02 Bagian 7.7"; nomor butir kini 6.7. Kecocokan isi 8.18 belum dinilai | Konsultan SoA |
| 10 | REG-04: istilah Level (Read-only, Operator, Admin, Privileged) tidak sama dengan matriks; belum ada matriks per sistem dan peran | Pemilik REG-04 |
| 11 | Scope tidak menyebut pengecualian (mis. akun pengguna akhir di aplikasi pelanggan); sumber diam, tidak ditambahkan | Head of Operation |
| 12 | Sumber tidak menyebut pelaku pencabutan akun vendor yang masa berlakunya habis (REG-04 hanya menandai KEDALUWARSA) | Head of Operation |
| 13 | POL-OPS-001 P-03 membolehkan kredensial "lewat japri atau password manager"; SOP-02 melarang kirim lewat chat. SOP-02 yang diikuti | Head of Operation |
| 14 | POL-OPS-001 masih DRAFT dengan penomoran USULAN; kode di bagian 11 diganti nomor SNX bila sudah terbit | Fani |
| 15 | Dokumen tidak punya slot KPI di template; 4 target sumber dilebur ke kolom SLA / Timing bagian 8 | Aziz (template) |

## 9. Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan yang saya lakukan:
- Label "(Annex A ...)" muncul di hampir tiap prinsip bagian 4 dan di judul 6.2, 6.5, 6.7. Terdengar mekanis, tapi dipertahankan karena syarat kriteria menuntut kontrol tercermin di bagian 4. Saya batasi: prinsip tanpa kontrol yang jelas di sumber (segregation of duties, akses production pelanggan) tidak diberi label.
- Kolom Authority dan baris peran tambahan bisa terbaca seperti pengisi tabel. Saya pendekkan jadi satu klausa dari sumber dan mengakui di asumsi nomor 2 bahwa kolom itu turunan.
- "Persetujuan" dan "approval" berganti untuk hal yang sama. Saya seragamkan: approval untuk keputusan pemilik sistem dan Head of Operation (sesuai sumber), persetujuan hanya untuk pelanggan.
- Istilah "joiner, mover, leaver" dari ringkasan audit tidak saya pakai karena sumber memakai "mutasi" dan "pemberhentian".
- Tidak ada pembuka generik, penutup positif, "tidak pernah", "tanpa terkecuali", em-dash, tebal atau huruf kapital untuk penekanan. Kalimat Tujuan dan prinsip sumber dibiarkan utuh.
- Daftar matriks akses berupa kalimat berderet titik koma; itu bentuk terbaik tanpa slot tabel lima kolom di template. Terdengar padat, bukan buatan.
- Output langkah yang berulang ("Baris ... di SNX-ISMS-REG-04") sengaja sama, karena menyebut rekaman yang sama.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka tanpa sumber hanya empat, semuanya berlabel (USULAN): 2 hari kerja, 1 hari kerja, retensi 3 tahun catatan sampling, dan pemilik catatan sampling (Lead SOC). Kalimat "Pembuatan akun 1 hari kerja" memang sengaja ditandai.
- Semua angka lain dari sumber: 12 karakter, 90 hari, 5 hari kerja, 10 hari kerja, triwulan, semester, 100%, 95%, 3 tahun, minimal 90 hari.
- Nama orang hanya dari defaults (tiga penanda tangan). Tidak ada tanggal; Effective Date kosong; status Draft.
- Sistem semuanya dari scope sumber (Zammad, Service Hub GLPI, Nusametric, Overseer, Nusagrid, Acronis, Cloudflare, AegisWAF, WHM, cPanel). Tidak ada hostname atau alamat.
- Yang bukan dari sumber tim dan sudah dicatat di bagian 6: nama klausul Annex A dan "Infrastruktur" 7.1.3, definisi umum, pelaku kalimat pasif, kolom Authority, lokasi Google Drive untuk REG-04.
- Hal yang saya ubah setelah pemeriksaan: kata "Persetujuan" pada output 6.1 langkah 3 menjadi "Approval pemilik sistem"; istilah definisi "NOC, SOC, dan SD dan PM" menjadi "NOC, SOC, SD dan PM"; diagram dipendekkan labelnya agar terbaca di halaman.

## 10. Hasil uji sendiri

- render_sop.py: sukses, 15 halaman (LibreOffice), diagram TB 12 simpul dan 5 lane.
- lint_doc.py sop: pass true, fails kosong, warns hanya "5 butir (USULAN) menunggu ACC" (nol warns PIC SLA).
- Validasi OOXML (/mnt/skills/public/docx/scripts/office/validate.py): All validations PASSED.
- Langkah prosedur: 35 langkah, kata terpanjang 21 (batas 25).
- Berkas keluaran uji: /tmp/pen-ISMS-SOP-02/ISMS-SOP-02.docx (bukan hasil final, render final oleh orkestrator ke out/08_ISMS).

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Pencabutan akses saat pemberhentian paling lambat hari terakhir kerja, mendadak segera | "Saat pemberhentian, semua akses dicabut paling lambat pada hari terakhir kerja; untuk pemberhentian mendadak, segera." (Bagian 7.5) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |
| 2 | Review akses privileged triwulanan, akses biasa semesteran | "akses privileged setiap triwulan, akses biasa setiap semester." (Bagian 7.6) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |
| 3 | Akses privileged ke sistem pelanggan butuh approval Head of Operation, plus persetujuan pelanggan bila kontrak mensyaratkan | "Akses privileged ke sistem pelanggan butuh approval Head of Operation, dan bila kontrak mensyaratkan, persetujuan pelanggan." (Bagian 7.1) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |

## USULAN

| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Matriks tingkat akses acuan per peran (label USULAN dari sumber) | Bagian 4 | Fani |
| U2 | Keputusan permintaan akses 2 hari kerja sesudah atasan mengonfirmasi | Bagian 8 | Fani |
| U3 | Pembuatan akun 1 hari kerja sesudah approval | Bagian 8 | Fani |
| U4 | Catatan hasil sampling log sesi privileged disimpan di Google Drive, pemilik Lead SOC | Bagian 11 | Fani |
| U5 | Retensi catatan sampling 3 tahun | Bagian 11 | Fani |

Jumlah USULAN berlabel di dokumen: 5 (sama dengan hitungan lint). Putaran perbaikan tidak menambah USULAN.

## Open items

Ringkasan open items sebelumnya (rinci di bagian 8 di atas) dan butir baru dari putaran perbaikan.

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber COO, defaults Samuel (defaults dipakai) | owner, Samuel |
| 2 | Head of Operation belum dipetakan ke jabatan nyata (HR-ORG-01 belum DONE) | owner, Fani |
| 3 | Status password manager (vault) belum terkonfirmasi; SOP mewajibkan password disimpan di sana | Ops (Fani) |
| 4 | Batas Service Hub (GLPI) lawan Zammad untuk permintaan akses | owner |
| 5 | Log Jumphost minimal 90 hari tidak menjamin cakupan sampling triwulanan | Fani |
| 6 | Tenggat 10 hari kerja untuk Ubah atau Cabut hasil review: dasar REG-04, bukan SOP-02 sumber; target 95% hanya untuk temuan | Fani |
| 7 | Pelaku permintaan persetujuan pelanggan tidak disebut sumber | Fani |
| 8 | "approval Lead" restore Acronis: ditulis "Lead NOC atau Lead SOC", tafsir perlu konfirmasi | Fani |
| 9 | SoA SNX-ISMS-SOA-01 memetakan 8.18 dan 8.3 ke "Bagian 7.7" yang kini butir 6.7; kecocokan isi 8.18 belum dinilai | konsultan SoA, Fani |
| 10 | REG-04: istilah Level tidak sama dengan matriks; belum ada matriks per sistem dan peran | Fani |
| 11 | Scope tanpa pengecualian tertulis; pelaku pencabutan akun vendor yang kedaluwarsa tidak disebut | Fani |
| 12 | POL-OPS-001 P-03 membolehkan kredensial lewat japri, SOP-02 melarang chat; POL-OPS-001 masih DRAFT dengan nomor USULAN | Fani |
| 13 | Template tidak punya slot KPI; 4 target sumber dilebur ke bagian 8 | Aziz |
| 14 (baru) | Kontrol pengganti saat sistem internal tidak mendukung akses privileged lewat Jumphost tidak disebut sumber. Baris pengecualian hanya menyatakan akses langsung dengan akun terpisah dari akun harian; tidak ada kontrol karangan | Fani |
| 15 (baru) | Pencatatan pemakaian akun break-glass: sumber hanya menulis "setiap pemakaiannya dicatat"; pelaku (Pengguna akun) dan lokasi catatan tidak disebut | Fani |
| 16 (baru) | Istilah dipilih penyusun agar konsisten: "mutasi" (bukan "perpindahan peran") dan "sistem tiket" (bukan "ticketing system"). Kata "ticketing system" dan "ticketing" tetap dipakai sumber | Aziz, Fani |
| 17 (baru) | Pelaku penetapan level akses (Pemilik sistem) dan pencatatannya (Administrator sistem) adalah tafsir dari dua kalimat sumber | Fani |
| 18 (baru) | Judul "Statement of Applicability (SoA)" untuk SNX-ISMS-SOA-01 di bagian 11 diambil dari salinan audit, bukan dari berkas Drive | konsultan SoA |

