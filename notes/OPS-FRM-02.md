# Catatan penyusun OPS-FRM-02: Project Risk Register

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-FRM-02.patch.json. Mode xlsx, aksi T1, nomor SNX-OPS-FRM-02 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber, audit_class B, wave W5. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-FRM-02.xlsx specs/OPS-FRM-02.patch.json /tmp/pen-OPS-FRM-02/out.xlsx` hasilnya `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 5 sheet, 1 gambar (Alur Proses), 7 data validation, 3 rentang conditional formatting, 310 rumus (Risk Register).

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-FRM-02_Project_Risk_Register.xlsx (127036 byte) | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D | 2026-10-13T06:09:14Z (get_file_metadata, dicek ulang hari ini, cocok dengan prompt; fileSize 127036 cocok dengan hasil dekode) | read_file_content (teks), download_file_content (xlsx didekode ke /tmp/src/OPS-FRM-02.xlsx; kerja di /tmp/pen-OPS-FRM-02/; semua 5 sheet dibaca dengan openpyxl, gambar image1.png dibuka) |
| Kriteria penerimaan | config/checklist.json baris 69 | (berkas ekspor checklist W0) | Description hanya nama berkas, jadi kriteria = substansi sumber + acuan ISO 9001:2015 "6.1, 8.1" dan ISO/IEC 27001:2022 "5.8" |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, bagian SNX-OPS-FRM-02 (baris 989 sampai 1235) | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir bagian 5 dicocokkan ulang ke berkas xlsx |
| Pendukung judul saja | SNX-ISMS-REG-02 (Information Security Risk Assessment Register), SNX-OPS-FRM-03 (Project Progress & Monitoring Report) | context/audit | Hanya untuk memastikan kode yang dirujuk sumber ada |

Sheet di sumber: Kontrol Dokumen, Alur Proses, Daftar, Risk Register, Matriks Risiko. Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Tujuan dokumen: satu workbook per proyek untuk mencatat, menilai, memantau risiko proyek, termasuk risiko keamanan informasi | Kontrol Dokumen B15: "Mencatat, menilai, dan memantau risiko proyek, termasuk risiko keamanan informasi selama proyek." dan B18: "Satu file per proyek; ganti nama menjadi FRM-02_<KodeProyek>.xlsx." | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |
| 2 | Penilaian: Skor = Likelihood x Impact, empat level, risiko Tinggi dan Kritis naik ke register ISMS | Matriks Risiko A3: "Skor = Likelihood x Impact. Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25"; Kontrol Dokumen B21: "Risiko berlevel Tinggi atau Kritis otomatis ditandai Ya pada kolom Naik ke ISMS dan wajib disalin ke SNX-ISMS-REG-02." | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |
| 3 | Penanganan per level, termasuk penerimaan risiko Kritis hanya oleh COO secara tertulis; pemilik dokumen Project Manager; masa simpan durasi kontrak + 3 tahun | Matriks Risiko B24: "Tindakan segera; dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis"; Kontrol Dokumen B10: "Project Manager"; B14: "Durasi kontrak + 3 tahun" | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |

Fakta lain yang dipakai, juga dari berkas yang sama: B9 "RESTRICTED (Internal)"; B12 "Klausul 6.1, 8.1"; B13 "Klausul atau kontrol Annex A 5.8"; B23 "Rencana mitigasi wajib dengan tenggat; dilaporkan ke Head of Operation dan dinaikkan ke register risiko ISMS"; B22 (Cara pakai 5) "Tinjau mingguan bersama laporan progres SNX-OPS-FRM-03."; formula kolom R baris 5 "=IF(H5="","",IF(H5>=10,"Ya","Tidak"))" (H = Skor, bukan P = Skor residual).

## 2. Isi patch (yang berubah dan alasannya)

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Risk Register baris 5 dan 6 (clear_rows) | PR-001 dan PR-002, data dummy | Dikosongkan; rumus H, I, P, Q, R, validasi, dan format bersyarat tetap | Sumber: A2 "Baris biru muda = CONTOH"; aturan W5 "clear CONTOH" |
| Risk Register!A2 | "... dihitung otomatis. Baris biru muda = CONTOH." | "Skor, level, dan kolom Naik ke ISMS dihitung otomatis; kolom Naik ke ISMS memakai Skor, bukan Skor residual." | Kata CONTOH harus hilang (alat menolak bila masih ada); kalimat baru menjelaskan perilaku rumus kolom R, lihat USULAN 3 |
| Kontrol Dokumen!B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi 00, status Draft |
| Kontrol Dokumen!B11 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by, lihat USULAN 1 |
| Kontrol Dokumen!B13 | "Klausul atau kontrol Annex A 5.8" | "Annex A 5.8" | Acuan klausul baris ini "5.8"; kata "atau" menyisakan dua kemungkinan padahal 5.8 satu kontrol |
| Kontrol Dokumen!B21 | "Risiko berlevel Tinggi atau Kritis otomatis ditandai Ya pada kolom Naik ke ISMS dan wajib disalin ke SNX-ISMS-REG-02." | "Risiko berlevel Tinggi atau Kritis menurut Skor (bukan Skor residual) otomatis ditandai Ya di kolom Naik ke ISMS dan wajib disalin ke SNX-ISMS-REG-02." | Cacat audit "Naik ke ISMS memakai skor inheren", lihat USULAN 3 |
| Kontrol Dokumen!C31 | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| Kontrol Dokumen baris 32 (clear_rows) | Baris revisi kedua, "keselarasan RTO dan target pulih" | Dikosongkan | Cacat audit: frasa RTO tidak relevan dengan isi workbook; baris duplikat rev 00 pada tanggal sama; lihat USULAN 4 |
| Kontrol Dokumen baris 26 (clear_rows) | Legenda "Baris CONTOH: hapus atau timpa saat dipakai" | Dikosongkan | Tidak ada lagi baris contoh yang perlu dihapus atau ditimpa |
| Kontrol Dokumen!B36 | "Project Manager" | "Erik Dwi Yanto / Technical/Operation Engineer L1" | defaults prepared_reviewed.OPS, lihat USULAN 2 |
| Kontrol Dokumen!B37 | "ISO/ISMS Coordinator" | "Fani Fatullah / VP Tech Operation and Services" | defaults prepared_reviewed.OPS |
| Kontrol Dokumen!B38 | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | defaults approved_by |
| Matriks Risiko!B24 | "... dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis" | "... dilaporkan ke Direktur (COO); penerimaan risiko hanya oleh COO secara tertulis" | data_conflicts: sebutan pertama COO di badan dokumen = "Direktur (COO)"; B24 adalah sebutan pertama di badan sesudah B11 dan B38 diganti |
| B4, B5, B9, B10, B12, B14 | nilai sama | nilai sama (di-set ulang agar medan template tertulis eksplisit) | Nomor, Judul, Klasifikasi, Pemilik, Acuan 9001, Masa simpan |

Tidak diubah: tanggal draft "13 Oktober 2026" (B7, B31) dan "Ditetapkan saat pengesahan" (B8) adalah isi sumber, bukan tanggal yang saya isi. Kolom Tanda tangan dan Tanggal di blok Pengesahan (C36 sampai D38) tetap kosong. Status persetujuan "Menunggu" (E31) tetap. Kolom Disusun "Divisi Operation" (D31) tetap. Klasifikasi tidak berubah dari label sumber.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah)

| # | Cacat di audit | Penanganan | Alasan bila tidak diperbaiki |
|---|---|---|---|
| 1 | Data register adalah CONTOH (PR-001, PR-002) | Diperbaiki: baris 5 dan 6 dikosongkan, A2 dan legenda B26 dibersihkan | |
| 2 | Kolom Naik ke ISMS memakai skor inheren, Cara pakai butir 4 tidak menyebutnya | Diperbaiki di teks (B21, A2); rumus tidak diubah | Rumus bukan teks; mengubahnya jadi skor residual adalah keputusan substantif, lihat Open item 2 |
| 3 | Rumus level cocok dengan 25 sel Matriks Risiko | Tidak ada cacat. Dicek dengan skrip openpyxl sekali pakai (tidak disimpan): rumus kolom H, I, P, Q, R baris 5 sampai 66 cocok dengan pola baris 5 (0 menyimpang), dan 25 sel C6:G10 Matriks Risiko sama dengan hasil rumus (0 tidak cocok) | |
| 4 | Nilai Matriks Risiko teks statis, tidak ikut bila ambang rumus diubah | Tidak diperbaiki | Mengubahnya menjadi rumus mengubah struktur sheet; hasil hari ini benar. USULAN 8 |
| 5 | Tidak ada validasi residual kurang dari atau sama dengan inheren | Tidak diperbaiki | Alat patch tidak menambah validasi data; USULAN 6 |
| 6 | Status "Ditutup" tanpa kriteria penutupan tertulis | Tidak diperbaiki | Kriteria penutupan tidak ada di sumber; mengarang kriteria dilarang. USULAN 5 |
| 7 | Kolom register tidak memuat ID proyek, tanggal tinjau, tanggal tutup | Tidak diperbaiki | Alat patch tidak menambah kolom; proyek dikenali dari nama berkas FRM-02_<KodeProyek>.xlsx (Cara pakai 1). USULAN 7 |
| 8 | Rujukan SNX-ISMS-REG-02 dan SNX-OPS-FRM-03 | Tidak ada cacat; kedua kode ada di korpus audit (REG-02 = Information Security Risk Assessment Register, FRM-03 = Project Progress & Monitoring Report) | Keduanya masih QUEUED di ledger; nomor dipertahankan sesuai worklist |
| 9 | Riwayat revisi dua baris, frasa RTO tidak relevan; blok Pengesahan tanpa tanda tangan | Baris 32 dikosongkan; tanda tangan dan tanggal tetap kosong (batas keras) | |
| 10 | Tenggat PR-002 satu hari setelah pencatatan | Tidak berlaku lagi, baris contoh dihapus | |

## 4. Asumsi

1. Sheet "Alur Proses" berisi gambar image1.png dan tidak bisa diedit alat patch; gambar dicek manual dan sejalan dengan sheet lain (tujuh kotak, satu keputusan "Tinggi atau Kritis?", SNX-ISMS-REG-02, SNX-OPS-FRM-03). Gambar tidak memuat nama orang atau sebutan COO. Tidak ada diagram yang perlu ditulis di spec.
2. Pemilik dokumen tetap "Project Manager" karena sumber menulisnya sebagai peran. Kolom "Disusun oleh" di blok Pengesahan sekarang berisi Erik Dwi Yanto sesuai defaults; dua peran itu tidak harus orang yang sama.
3. Tanggal draft dan tanggal revisi 13 Oktober 2026 dibiarkan karena berasal dari sumber (modifiedTime Drive 2026-10-13T06:09:14Z cocok).
4. Kalimat perintah di sumber (Cara pakai 1 sampai 5, legenda "Sel rumus: jangan diubah") adalah isi form untuk pengguna, bukan arahan ke penyusun. Tidak dijalankan sebagai instruksi; yang masih berlaku tetap dipertahankan sebagai isi dokumen. Tidak ada kalimat di sumber yang ditujukan ke penyusun atau alat.

## USULAN

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: Samuel Kristanto Utomo / President Director (default D2) menggantikan "COO, Amirull Yusuf Zulkarnain" di Kontrol Dokumen B11 dan B38. Sumber menulis COO sebagai penyetuju; defaults memberi pembalik "form operasional disetujui COO bila owner memutus". | owner |
| 2 | Disusun oleh Erik Dwi Yanto / Technical/Operation Engineer L1 dan Diperiksa oleh Fani Fatullah / VP Tech Operation and Services (defaults) menggantikan "Project Manager" dan "ISO/ISMS Coordinator" di B36 dan B37. | owner |
| 3 | Kalimat B21 dan A2 yang menyebut kolom Naik ke ISMS memakai Skor, bukan Skor residual. Isinya hanya menjelaskan rumus yang ada, tetapi kalimatnya tambahan penyusun. | Fani |
| 4 | Baris riwayat revisi kedua (rev 00 tanggal sama, frasa RTO) dikosongkan dan C31 memakai "Draft awal untuk review dan pengesahan". | Fani |
| 5 | Kriteria penutupan risiko (kapan status "Ditutup" boleh dipilih). Tidak diterapkan di berkas. | Fani |
| 6 | Validasi data agar Skor residual tidak melebihi Skor. Tidak diterapkan di berkas. | Fani |
| 7 | Kolom ID proyek, tanggal tinjau, dan tanggal tutup di Risk Register. Tidak diterapkan di berkas. | Fani |
| 8 | Matriks Risiko dihitung dari ambang yang sama dengan rumus Risk Register, atau diberi catatan bahwa nilainya tetap. Tidak diterapkan di berkas. | Fani |

Jumlah USULAN: 8 (empat diterapkan di berkas, empat hanya diusulkan).

## Open items

1. Sebutan peran penerima laporan risiko Tinggi: sumber menulis "Head of Operation" (Matriks Risiko B23), sedangkan premis dan defaults menamai Fani Fatullah "VP Tech Operation and Services". Teks sumber dipertahankan; pemetaan peran ke orang belum ada. Pemutus: owner atau Fani.
2. Naik ke ISMS dihitung dari Skor awal (rumus kolom R memakai H). Apakah yang dimaksud tim Skor awal atau Skor residual tidak tertulis. Rumus dibiarkan; teks sekarang menyebut perilaku nyatanya. Pemutus: Fani.
3. Sumber tidak menyebut pelaku untuk dua langkah: penyalinan risiko Tinggi atau Kritis ke SNX-ISMS-REG-02 (Cara pakai 4) dan tinjauan mingguan bersama SNX-OPS-FRM-03 (Cara pakai 5). Pelaku tidak diisi karena tidak ada sumber. Pemutus: Fani.
4. "Project Manager", "Service Delivery Manager" (sudah terhapus bersama contoh), dan "Head of Operation" belum dicocokkan dengan tabel peran HR-ORG-01 (berstatus IN_PROGRESS di ledger saat notes ini ditulis). Pemilik dokumen tetap "Project Manager". Cek ulang setelah HR-ORG-01 DONE.
5. Batasan alat xlsx_patch (di luar bidang tulis saya, tools/ milik LEAD): clear_rows juga menghapus warna isi sel input. Akibatnya sel input Risk Register baris 5 dan 6 tidak lagi kuning input (FFF2CC, seperti baris 7 sampai 66) dan sel swatch A26 di legenda Kontrol Dokumen menjadi kotak kosong bergaris. Fungsi tidak berubah. Perlu keputusan LEAD: tech_fix alat atau terima.
6. Penerimaan risiko Kritis tetap "hanya oleh COO" (sumber), sementara penyetuju dokumen memakai President Director (default). Dua hal berbeda, dicatat agar owner bisa melihat kalau pembalik D2 dipakai.
7. Nama berkas yang dianjurkan Cara pakai 1 ("FRM-02_<KodeProyek>.xlsx") tidak memakai awalan SNX-OPS. Dipertahankan sebagai suara tim (T1). Konfirmasi: Fani.
8. Nama keluaran berkas: RUNBOOK §1 meminta untuk W5 <Judul> = judul berkas sumber; orkestrator yang menentukan nama akhir, patch tidak memuatnya.

## Jawaban dua pertanyaan penutup

1. Apa yang membuat teks ini terdengar buatan AI? Draf pertama saya punya satu kalimat yang memberi kata kerja manusia pada benda: "Kolom Naik ke ISMS membaca Skor". Saya ganti menjadi "memakai Skor". Draf pertama B21 juga menghilangkan kata "otomatis" dari kalimat tim, yang membuat pelakunya samar; kata itu saya kembalikan. Kalimat patch lain adalah kalimat tim yang hanya diperbaiki ejaan atau rujukannya, jadi tidak ada kalimat baru yang berpola kelompok tiga, penutup positif, atau ekor penegas. Yang masih tersisa dari suara tim dan sengaja dipertahankan (T1): "Tulis risiko dalam pola sebab, kejadian, dampak" dan tujuan dokumen yang memuat tiga kata kerja. Keduanya jelas dan berasal dari sumber.
2. Adakah fakta, angka, nama, atau tanggal tanpa sumber? Tidak ada yang ditambahkan. Nama dan jabatan penanda tangan berasal dari config/defaults.json (approved_by, prepared_reviewed.OPS, data_conflicts) dan diberi label USULAN 1 dan 2. Angka (10 sebagai ambang Naik ke ISMS, 6.1, 8.1, 5.8, 3 tahun) berasal dari sumber (B21 melalui rumus kolom R, Matriks Risiko A3, B12, B13, B14). Tanggal 13 Oktober 2026 berasal dari sumber. Satu hal yang saya beri keterangan: "Annex A 5.8" ditulis dari acuan klausul baris ini dan B13 sumber ("Annex A 5.8"), bukan dari standar ISO langsung; saya tidak menulis judul kontrolnya karena tidak ada di sumber.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan" (sebutan yang sudah dipakai di Matriks Risiko; sheet itu tidak disunting).
Yang disunting hanya Tujuan, Cara pakai 1 sampai 5, dan catatan Risk Register A2; kalimat lain dipertahankan (T1).
Cara pakai 4 dipecah dua kalimat; arti tetap (otomatis Ya dari Skor, wajib disalin ke SNX-ISMS-REG-02).
