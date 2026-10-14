# REVIEW-W5 (2026-10-14T22:05:40Z)

## SNX-OPS-FRM-01 Project Plan Scope Timeline
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-01 Project Plan Scope Timeline (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-01_Project_Plan_Scope_Timeline.xlsx (1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3, modifiedTime 2026-10-13T06:09:12Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Gate G1 dimiliki Service Delivery Manager dan lolos hanya bila tidak ada butir Belum | "Pemilik gate: Service Delivery Manager. Gate LOLOS bila tidak ada butir berstatus Belum." (Checklist G1!A2) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |
| Pemilik dokumen adalah peran Project Manager | "Pemilik dokumen" / "Project Manager" (Kontrol Dokumen!A10, B10) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |
| Masa simpan record per proyek | "Masa simpan record" / "Durasi kontrak + 3 tahun" (Kontrol Dokumen!A14, B14) | 1q0cl8mLlUDJ-7nvnzozSbjJhE46-Jk-3 |

### USULAN
| # | Butir | Status di berkas | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga nama di blok Pengesahan dan B11: Erik Dwi Yanto (Disusun), Fani Fatullah (Diperiksa), Samuel Kristanto Utomo (Disetujui). Sumber menulis peran saja ("Project Manager", "ISO/ISMS Coordinator") dan COO sebagai penyetuju. Defaults menandai semua baris ini USULAN, dengan pembalik "form operasional disetujui COO bila owner memutus" | Diterapkan | owner (nama penyetuju: owner atau Samuel) |
| 2 | Pemilik dokumen ditulis sebagai peran "Project Manager" (jabatan tanpa nama, sesuai sumber). Pemetaan peran itu ke jabatan nyata belum ada | Diterapkan apa adanya | Fani |
| 3 | Rumus C14 Checklist G1 dibuat menahan gate bila ada butir kosong: `=IF(COUNTIF(C5:C12,"Lolos")+COUNTIF(C5:C12,"Tidak berlaku")=8,"LOLOS","TAHAN")` | Tidak diterapkan | Fani |
| 4 | Penanda bila total bobot WBS (J2) bukan 100, mis. conditional formatting pada J2 | Tidak diterapkan | Fani |
| 5 | Garis putus-putus dari "Kembalikan ke Commercial" kembali ke "Isi Checklist G1" pada gambar Alur Proses. Sumber tidak menyebut apa yang terjadi sesudah paket dikembalikan; tujuan panah itu tafsir | Tidak diterapkan | Fani |

Tidak ada angka baru dari saya di berkas hasil. Angka 8 di butir 3 adalah jumlah butir G1 di sumber.

### Open items
1. Tanggal draft "13 Oktober 2026" (B7) dan tanggal baris riwayat revisi (B31) dipertahankan dari sumber. Tidak ada tanggal baru yang saya tulis dan tanggal efektif tetap "Ditetapkan saat pengesahan". Owner memutus apakah tanggal draft perlu diganti tanggal draft revisi ini.
2. Gambar Alur Proses (image1.png) tidak bisa disunting xlsx_patch. Kotak "Kembalikan ke Commercial" tidak punya jalan kembali, dan teks gambar tidak menyebut siapa yang menindaklanjuti. Perlu keputusan pemilik dokumen (USULAN 5) lalu gambar baru lewat LEAD atau tim.
3. GAP alat (kosmetik): clear_rows menghapus isian warna sel yang dikosongkan, sehingga baris 5 sampai 9 WBS, baris 5 Milestone, dan baris 5 Stakeholder berwarna polos, sedangkan baris kosong lain di sheet yang sama berwarna kuning input (FFF2CC). Sel rumus tidak terpengaruh. Perbaikannya di tools/xlsx_patch.py (memulihkan FFF2CC pada sel input yang dikosongkan), di luar batas tulis saya. Conditional formatting membaca nilai sel, bukan isian warna, jadi fungsi form tidak berubah. Belum dilihat di Excel; hanya konversi LibreOffice yang berhasil.
4. Rujukan "SNX-OPS-SOP-01 Bagian 6.4" (B21) benar terhadap sumber SOP-01. SOP-01 akan dirender ulang ke 11 bagian template (W2); orkestrator perlu memeriksa bahwa pembaruan progres mingguan tetap ada di butir 6.4 spec OPS-SOP-01, atau mengubah rujukan ini.
5. Checklist G1 di FRM-01 memuat 8 butir, G1 di PRO-OPS-001 8.2 memuat 7 butir tanpa butir klasifikasi data (catatan audit). Pemilik dokumen memutus daftar mana yang berlaku. Dokumen ini memakai 8 butir karena butir 8 menjadi dasar acuan 27001 5.8.
6. Nama peran Project Manager, Service Delivery Manager, dan Commercial (di gambar) belum dicocokkan dengan HR-ORG-01 (status IN_PROGRESS di ledger saat saya menyusun). Cocokkan setelah HR-ORG-01 DO

## SNX-OPS-FRM-02 Project Risk Register
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-02 Project Risk Register (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-02_Project_Risk_Register.xlsx (1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D, modifiedTime 2026-10-13T06:09:14Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Tujuan dokumen: satu workbook per proyek untuk mencatat, menilai, memantau risiko proyek, termasuk risiko keamanan informasi | Kontrol Dokumen B15: "Mencatat, menilai, dan memantau risiko proyek, termasuk risiko keamanan informasi selama proyek." dan B18: "Satu file per proyek; ganti nama menjadi FRM-02_<KodeProyek>.xlsx." | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |
| 2 | Penilaian: Skor = Likelihood x Impact, empat level, risiko Tinggi dan Kritis naik ke register ISMS | Matriks Risiko A3: "Skor = Likelihood x Impact. Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25"; Kontrol Dokumen B21: "Risiko berlevel Tinggi atau Kritis otomatis ditandai Ya pada kolom Naik ke ISMS dan wajib disalin ke SNX-ISMS-REG-02." | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |
| 3 | Penanganan per level, termasuk penerimaan risiko Kritis hanya oleh COO secara tertulis; pemilik dokumen Project Manager; masa simpan durasi kontrak + 3 tahun | Matriks Risiko B24: "Tindakan segera; dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis"; Kontrol Dokumen B10: "Project Manager"; B14: "Durasi kontrak + 3 tahun" | 1XvfQ5yYx4H8Y-rgJUKyngfZfn7909L2D |

Fakta lain yang dipakai, juga dari berkas yang sama: B9 "RESTRICTED (Internal)"; B12 "Klausul 6.1, 8.1"; B13 "Klausul atau kontrol Annex A 5.8"; B23 "Rencana mitigasi wajib dengan tenggat; dilaporkan ke Head of Operation dan dinaikkan ke register risiko ISMS"; B22 (Cara pakai 5) "Tinjau mingguan bersama laporan progres SNX-OPS-FRM-03."; formula kolom R baris 5 "=IF(H5="","",IF(H5>=10,"Ya","Tidak"))" (H = Skor, bukan P = Skor residual).

### USULAN
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

### Open items
1. Sebutan peran penerima laporan risiko Tinggi: sumber menulis "Head of Operation" (Matriks Risiko B23), sedangkan premis dan defaults menamai Fani Fatullah "VP Tech Operation and Services". Teks sumber dipertahankan; pemetaan peran ke orang belum ada. Pemutus: owner atau Fani.
2. Naik ke ISMS dihitung dari Skor awal (rumus kolom R memakai H). Apakah yang dimaksud tim Skor awal atau Skor residual tidak tertulis. Rumus dibiarkan; teks sekarang menyebut perilaku nyatanya. Pemutus: Fani.
3. Sumber tidak menyebut pelaku untuk dua langkah: penyalinan risiko Tinggi atau Kritis ke SNX-ISMS-REG-02 (Cara pakai 4) dan tinjauan mingguan bersama SNX-OPS-FRM-03 (Cara pakai 5). Pelaku tidak diisi karena tidak ada sumber. Pemutus: Fani.
4. "Project Manager", "Service Delivery Manager" (sudah terhapus bersama contoh), dan "Head of Operation" belum dicocokkan dengan tabel peran HR-ORG-01 (berstatus IN_PROGRESS di ledger saat notes ini ditulis). Pemilik dokumen tetap "Project Manager". Cek ulang setelah HR-ORG-01 DONE.
5. Batasan alat xlsx_patch (di luar bidang tulis saya, tools/ milik LEAD): clear_rows juga menghapus warna isi sel input. Akibatnya sel input Risk Register baris 5 dan 6 tidak lagi kuning input (FFF2CC, seperti baris 7 sampai 66) dan sel swatch A26 di legenda Kontrol Dokumen menjadi kotak kosong bergaris. Fungsi tidak berubah. Perlu keputusan LEAD: tech_fix alat atau terima.
6. Penerimaan risiko Kritis tetap "hanya oleh COO" (sumber), sementara penyetuju dokumen memakai President Director (default). Dua hal berbeda, dicatat agar owner bisa melihat kalau pembalik D2 dipakai.
7. Nama berkas yang dianjurkan Cara pakai 1 ("FRM-02_<KodeProyek>.xlsx") tidak memakai awalan SNX-OPS. Dipertahankan sebagai suara tim (T1). Konfirmasi: Fani.
8. Nama keluaran berkas: RUNBOOK §1 memint

## SNX-OPS-FRM-03 Project Progress Monitoring Report
- State: DONE; lint: True; verifikasi: None; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-FRM-03 Project Progress Monitoring Report (Rev00 DRAFT).docx
- Sumber: SNX-OPS-FRM-03_Project_Progress_Monitoring_Report.docx (147U5gBLjtLKHau5cQbLUym8iInh2b_RR, modifiedTime 2026-10-13T06:09:02Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Project Manager | "Pemilik dokumen" / "Project Manager" (tabel Atribut, baris data ke-7) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |
| Arti tiga status laporan | "Panduan status: Hijau = sesuai baseline; Kuning = deviasi bisa dipulihkan tanpa mengubah baseline; Merah = butuh keputusan pelanggan atau COO." (di bawah tabel Ringkasan status) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |
| Masa simpan record | "Masa simpan record" / "Durasi kontrak + 3 tahun" (tabel Atribut, baris data ke-11) | 147U5gBLjtLKHau5cQbLUym8iInh2b_RR |

### USULAN
| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Deviasi jadwal lebih dari 1 minggu dari baseline = status Merah (angka dari SOP-01 butir 6.4.5, dipakai pada ambang status laporan; sumber FRM-03 tanpa angka) | Isi Laporan, Ringkasan status (berlabel "(USULAN)") | Fani |
| 2 | Tiga penanda tangan: prepared Erik Dwi Yanto, reviewed Fani Fatullah, approved Samuel Kristanto Utomo, menggantikan Disusun "Project Manager", Diperiksa "ISO/ISMS Coordinator", Disetujui "COO, Amirull Yusuf Zulkarnain" di sumber (config/defaults.json D2; pembalik: form operasional disetujui COO bila owner memutus) | Blok Approval halaman depan | owner |
| 3 | Kolom Bukti memakai "tiket Zammad" | Isi Laporan, Pekerjaan periode ini | owner |
| 4 | Pelaku Project Manager untuk eskalasi, pengiriman, penyimpanan PDF, dan kepemilikan rekaman | Peran, Rekaman | Fani |
| 5 | Arti Baseline, Milestone, dan Go-gate hasil tafsir lintas dokumen | Istilah | Fani |

### Open items
1. Aturan menentukan status Keseluruhan dan ambang Kuning dan Merah untuk Scope, Mutu, Risiko dan isu, Keamanan informasi tidak ada di sumber. Penentu: Fani.
2. Klasifikasi RESTRICTED (Internal) dengan pembagian ke pelanggan: sumber tidak menyebut label atau persetujuan untuk salinan yang keluar. Penentu: owner atau Fani.
3. Hubungan eskalasi status Merah (Head of Operation dan COO menurut diagram; "butuh keputusan pelanggan atau COO" menurut panduan status) dengan SOP-01 butir 6.4.3 (risiko Tinggi atau Kritis ke Head of Operation) dan 6.4.5 (deviasi lebih dari 1 minggu ke COO) tidak dinyatakan. Penentu: Fani.
4. Proyek mana yang wajib memakai FRM-03 (semua proyek atau yang punya workbook SNX-OPS-FRM-01) tidak dinyatakan. Penentu: Fani.
5. Batas sistem tiket: audit FRM-04 menulis "CR juga dibuat di Service Hub" (GLPI), sedangkan data owner menyebut Zammad untuk Ops. Kolom Bukti sudah ditulis "tiket Zammad"; konfirmasi untuk tiket dan CR. Penentu: owner.
6. Penyetuju dokumen: sumber menulis COO, Amirull Yusuf Zulkarnain; data baris menetapkan Samuel Kristanto Utomo / President Director. Konfirmasi pembalik D2. Penentu: owner.
7. Nilai status milestone diambil dari FRM-01 sheet Daftar (salinan audit). Bila tim mengubah daftar itu, selaraskan paragraf di Progres milestone. Penentu: Fani.
8. Kalimat perintah di sumber ("Teks dalam kurung siku adalah petunjuk dan dihapus saat diisi", "Simpan sebagai PDF ...") adalah isi form untuk Project Manager, bukan perintah ke penyusun. Dipakai sebagai isi dokumen, tidak dijalankan. Tidak ada kalimat perintah lain yang menyasar penyusun.
9. Tata letak: tabel Peran, judul tabel Identitas laporan, dan tabel Distribusi terpotong antarhalaman di pratinjau LibreOffice. Efek renderer; tidak diubah (di luar batas tulis).

## SNX-OPS-FRM-04 Change Request Approval Log
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-04 Change Request Approval Log (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-04_Change_Request_Approval_Log.xlsx (1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ, modifiedTime 2026-10-13T06:09:17Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini adalah rekap audit untuk semua change request; CR juga dibuat sebagai tiket di sistem lain | "Satu nomor CR per perubahan: CR-YYYY-NNNN. CR juga dibuat di Service Hub; log ini menjadi rekap audit." (Kontrol Dokumen B18) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |
| 2 | Go-gate dan PIR dihitung otomatis; PIR ditinjau dalam 5 hari kerja | "Kolom Go-gate otomatis CEK bila backup, rollback, atau approval belum lengkap (kecuali Emergency)." dan "Kolom PIR otomatis Ya untuk change Major atau yang berakhir rollback; tinjau dalam 5 hari kerja." (B19, B20) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |
| 3 | Masa simpan 3 tahun, klasifikasi RESTRICTED (Internal), pemilik dokumen Head of Operation, acuan ISO 8.5.6 dan 8.32 | "Masa simpan record \| 3 tahun"; "Klasifikasi \| RESTRICTED (Internal)"; "Pemilik dokumen \| Head of Operation"; "Acuan ISO 9001:2015 \| Klausul 8.5.6"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 8.32" (B14, B9, B10, B12, B13) | 1u5P_nturbvTvvi3hSrCy3ZfAIyiXCqWZ |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Baris CONTOH satu-satunya | "Baris CONTOH: hapus atau timpa saat dipakai" (Kontrol Dokumen B25); "Approver sesuai SNX-OPS-SOP-02 Bagian 5. Baris biru muda = CONTOH." (Change Log A2); U5 = "CONTOH" | Change Log baris 5 (CR-2026-0001); baris 6 sampai 155 hanya rumus S dan T |
| Penanda tangan sumber | "Disusun oleh \| Head of Operation", "Diperiksa oleh \| ISO/ISMS Coordinator", "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Kontrol Dokumen B35 sampai B37, B11 |
| Riwayat revisi sumber | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" dan "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris,

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | CR dibuat sebagai tiket di Zammad (bukan Service Hub/GLPI) karena CR adalah pekerjaan Ops. Sumber menulis Service Hub, ditulis sebelum keputusan owner 14 Okt. Batas "generalist" belum dirinci owner | Kontrol Dokumen B18, berlabel (USULAN) di sel | Owner, dengan Fani |
| 2 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, COO. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 3 | Pemilik dokumen tetap "Head of Operation" sesuai sumber. Peran ini tidak sama dengan jabatan Fani (VP Tech Operation and Services); pemetaan peran ke orang belum diputus | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Go-gate memeriksa Ack pelanggan. Rumus: `=IF(A5="","",IF(F5="Emergency","Emergency",IF(AND(I5<>"",J5<>"",L5="Disetujui",OR(N5="Ya",N5="Tidak perlu")),"OK","CEK")))`, diterapkan ke S5 sampai S155 | Change Log kolom S (belum diterapkan) | Fani |
| 6 | Samakan label dan rumus persentase: ganti F6 menjadi "Tanpa rollback (%)" bersama KPI di SOP-02 dan tabel KPI Ops, atau batasi rumus ke jenis Emergency. Samakan juga A13 dengan B13 (temuan A) | Ringkasan F6, A13, B13 (belum diterapkan) | Fani |
| 7 | Tambah kolom Tgl PIR dan Status PIR agar batas 5 hari kerja bisa diukur | Change Log (belum diterapkan) | Fani |

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Go-gate OK tidak berarti Ack pelanggan sudah ada, padahal SOP-02 sumber mensyaratkannya bila menyentuh layanan pelanggan. Putuskan rumus USULAN 5 atau terima celah | Fani |
| 2 | Label "Tanpa rollback darurat (%)" tidak sepadan dengan rumus; nama yang sama dipakai sebagai KPI di SOP-02 dan tabel KPI Ops. Selaraskan ketiganya serentak (USULAN 6) | Fani |
| 3 | Ringkasan A13 vs B13 (temuan A di bagian 3) | Fani |
| 4 | Jumlah vs Berhasil+Rollback+Gagal: CR berhasil Dibatalkan atau tanpa Hasil hanya masuk Jumlah | Fani |
| 5 | Tidak ada kolom tanggal atau status PIR (USULAN 7) | Fani |
| 6 | A2 menunjuk "SNX-OPS-SOP-02 Bagian 5". Cocokkan nomor bagian dan isi kolom Approver setelah SOP-02 selesai dirender; SOP-02 dan FRM-04 harus sama soal sistem tiket (Zammad atau Service Hub) | Orkestrator (lane OPS-SOP-02) |
| 7 | Peran "Head of Operation" sebagai pemilik dokumen dan "ISO/ISMS Coordinator" sebagai pemeriksa di sumber belum dipetakan ke orang; Fani dipakai sebagai pemeriksa karena defaults | Fani, owner |
| 8 | Gambar di Alur Proses tidak bisa diubah lewat xlsx_patch; cabang "Ditolak atau revisi" tanpa lanjutan tetap ada di diagram | Orkestrator (butuh entri LEAD bila gambar harus diganti) |
| 9 | Keterbatasan alat: clear_rows menghapus warna isi baris 5, sehingga A5 sampai R5 dan U5 tanpa warna sedangkan baris 6 sampai 155 berwarna kuning input. Kotak legenda A25 tetap biru. Nilai rumus belum tersimpan di out.xlsx (openpyxl); Excel dan LibreOffice menghitung ulang saat dibuka (diverifikasi LibreOffice: Ringkasan nol). Putuskan terima atau tech_fix alat | Orkestrator |
| 10 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti agar tidak ada tanggal karangan. Tanggal efektif 

## SNX-OPS-FRM-05 Testing UAT Quality Verification
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-05 Testing UAT Quality Verification (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-05_Testing_UAT_Quality_Verification.xlsx (1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs, modifiedTime 2026-10-13T06:09:19Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini merekam rencana uji, kasus uji, defect, dan persetujuan UAT, dan menjadi dasar BAST pada gate G2 | "Merekam rencana uji, eksekusi kasus uji, defect, dan persetujuan UAT sebagai dasar BAST (gate G2)." (Kontrol Dokumen B15) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |
| 2 | Rekomendasi UAT dihitung otomatis dari tiga angka (defect berat, kasus Belum, kasus Gagal); petunjuk sumber hanya menyebut defect berat | `=IF(B3=0,"",IF(AND(B9=0,B7=0,B5=0),"SIAP UAT DITANDATANGANI","BELUM SIAP"))` (Ringkasan dan Persetujuan B10) dan "Sheet Ringkasan dan Persetujuan menghitung tingkat kelulusan; UAT ditandatangani bila tidak ada defect Kritis atau Tinggi terbuka." (Kontrol Dokumen B21) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |
| 3 | Pemilik dokumen adalah peran Project Manager; klasifikasi RESTRICTED (Internal); masa simpan durasi kontrak ditambah 3 tahun | "Pemilik dokumen" / "Project Manager" (A10, B10); "Klasifikasi" / "RESTRICTED (Internal)" (A9, B9); "Masa simpan record" / "Durasi kontrak + 3 tahun" (A14, B14) | 1mTi4unyn2xST8h_ChsS_2w1xTWzSBROs |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Isi Kasus Uji dan Defect adalah data contoh | "Baris biru muda = CONTOH." (Kasus Uji A2); "Baris CONTOH: hapus atau timpa saat dipakai" (Kontrol Dokumen B25) | Kasus Uji baris 5 sampai 7 (TC-001 sampai TC-003, penguji "[penguji]", tanggal 18-Nov-2026); Defect baris 5 (DF-001). Baris 8 sampai 87 dan 6 sampai 45 kosong |
| Kriteria lulus di sumber hanya contoh | "Contoh: 100% kasus Kritis lolos, minimal 95% total kasus lolos, tidak ada defect Kritis atau Tinggi terbuka" | Rencana Uji B8 |
| Rumus defect berat menghitung dua status | Empat COUNTIFS dijumlahkan: Kritis dan 

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tetapkan kriteria lulus baku. Sumber hanya punya contoh "100% kasus Kritis lolos, minimal 95% total kasus lolos, tidak ada defect Kritis atau Tinggi terbuka"; sel dikosongkan. Bila ambang itu mau dipakai, form butuh kolom Severity di Kasus Uji dan rumus tambahan | Rencana Uji B8 (dikosongkan), Kasus Uji dan Ringkasan (belum diubah) | Fani |
| 2 | Tambah langkah: kasus yang lolos retest diubah statusnya dari Gagal menjadi Lolos, agar rekomendasi bisa menjadi SIAP. Ditulis di sel dengan label (USULAN) | Kasus Uji A2 | Fani |
| 3 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Project Manager, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Teks mengikuti rumus, bukan sebaliknya: label A9, aturan Defect A2, dan petunjuk B21 disamakan dengan perilaku rumus B9 dan B10 (Terbuka atau Diperbaiki; tiga syarat SIAP). Pilihan lain: ubah rumus agar sesuai teks lama | Ringkasan dan Persetujuan A9, Defect A2, Kontrol Dokumen B21 (sudah diterapkan di teks) | Fani |
| 6 | Pemilik dokumen tetap "Project Manager" sesuai sumber. Peran ini belum dipetakan ke orang; Erik Dwi Yanto tercantum sebagai penyusun dari defaults | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 7 | Tambahkan rujukan ke SNX-OPS-FRM-04 untuk defect yang diperbaiki lewat change request (sumber contoh: "Perbaikan melalui CR") | Cara pakai atau judul kolom Catatan di Defect (

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Gambar di Alur Proses tidak bisa diubah lewat xlsx_patch: cabang "Belum siap (tunggu defect ditutup)" tetap tanpa panah kembali ke alur. Butuh entri LEAD bila gambar harus diganti | Orkestrator |
| 2 | Rumus rekomendasi tidak memakai ambang 95% dan 100% Kritis, dan Kasus Uji tidak punya kolom Severity. Putuskan USULAN 1 atau terima bahwa kriteria lulus hanya ditulis per proyek di Rencana Uji B8 tanpa dihitung form | Fani |
| 3 | Defect Kritis atau Tinggi berstatus "Diterima sebagai isu sisa" tidak menahan UAT dan sumber tidak menyebut siapa yang boleh menerimanya. Tetapkan peran penerima | Fani |
| 4 | Blok Keputusan UAT (tiga kotak centang) dan tiga baris tanda tangan tidak menyebut siapa yang memutus. Sumber hanya menyebut tiga peran penanda tangan | Fani |
| 5 | Istilah "Penguji pelanggan" (Rencana Uji A10) dan "Perwakilan pelanggan" (Ringkasan A17): satu peran atau dua? Samakan bila satu | Fani |
| 6 | Masa simpan FRM-05 (durasi kontrak + 3 tahun) berbeda dari FRM-06 (durasi kontrak + 5 tahun, salinan audit). FRM-05 adalah prasyarat BAST di FRM-06, jadi dua angka itu dilihat auditor berdampingan (USULAN 8) | Fani, dengan Legal |
| 7 | Rujukan "project charter (SNX-OPS-FRM-01)" di B19 dan kolom kriteria penerimaan di FRM-01 (audit baris 883, "Kriteria penerimaan (dasar UAT)"): cocokkan nama sheet dan sel setelah FRM-01 final | Orkestrator (lane OPS-FRM-01) |
| 8 | Format ID kasus uji dan defect tidak tertulis di form setelah baris contoh dikosongkan. Tambah petunjuk format hanya bila tim memutus polanya | Fani |
| 9 | Keterbatasan alat: tinggi baris tidak bisa diubah, kotak legenda A25 tetap biru walau tidak ada baris biru lagi, dan nilai rumus belum tersimpan di out.xlsx (openpyxl); Excel dan LibreOffice menghitung ulang

## SNX-OPS-FRM-06 Project Handover BAST Closure Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 1; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-FRM-06 Project Handover BAST Closure Report (Rev00 DRAFT).docx
- Sumber: SNX-OPS-FRM-06_Project_Handover_BAST_Closure_Report.docx (1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb, modifiedTime 2026-10-13T06:09:02Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Form ini satu dokumen tiga bagian: BAST ke pelanggan (G2), checklist serah terima SD dan PM ke Operation (G3), dan laporan penutupan proyek | "Bagian A, Berita Acara Serah Terima (BAST) implementasi kepada pelanggan (gate G2)." / "Bagian B, checklist serah terima internal dari SD dan PM ke Operation (gate G3)." / "Bagian C, laporan penutupan proyek (closure report)." (Petunjuk pengisian) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |
| 2 | Layanan baru BAU bila semua butir G3 Lolos atau Tidak berlaku; Operation boleh menolak secara tertulis dan layanan tetap hypercare dengan pemilik SD dan PM | "Layanan dinyatakan BAU hanya bila semua butir berstatus Lolos atau Tidak berlaku. Operation berhak menolak serah terima secara tertulis bila checklist belum lengkap; selama itu layanan berstatus hypercare dengan pemilik SD dan PM." (Bagian B) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |
| 3 | Pemilik dokumen adalah Service Delivery Manager; klasifikasi RESTRICTED (Internal); masa simpan record durasi kontrak ditambah 5 tahun | "Pemilik dokumen \| Service Delivery Manager"; "Klasifikasi \| RESTRICTED (Internal)"; "Masa simpan record \| Durasi kontrak + 5 tahun" (tabel Atribut) | 1BPtjct3hNbhlUILJ7FTm4EX-_Vhk-KUb |

Fakta pendukung yang dipakai di keputusan:

| Fakta | Kutipan verbatim | Posisi |
|---|---|---|
| Aturan pelanggan pemerintah | "Untuk pelanggan pemerintah melalui main contractor, BAST dibuat atas nama SINUX, versi original disimpan di Drive, dan periode ditetapkan main contractor. Dokumen teknis untuk pelanggan pemerintah tanpa harga, diskon, tier, maupun roadmap komersil." | Petunjuk pengisian. Jadi P3 dan P4 |
| Prasyarat Bagian A | Kotak "UAT lolos" dengan sub-label "SNX-OPS-FRM-05 ditandatangani" mendahului

### USULAN
Sepuluh butir berlabel (USULAN) di spec. Tiap butir punya pemutus yang disarankan.

| # | Butir USULAN | Lokasi di spec | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Zammad sebagai ticketing system Operation untuk form ini (sumber: "Zammad atau Service Hub") | Definisi, Ticketing system; dipakai Bagian B butir 1 dan 9 | Owner, dengan Fani |
| 2 | P9: unsur SIEM yang tidak berlaku pada butir 3, dan butir 4 Tidak berlaku, diberi alasan di kolom Bukti atau referensi | Ketentuan P9; Penanganan Pengecualian baris 3 dan 4 | Fani |
| 3 | P10: kolom Bukti atau referensi berisi nama dan letak rekaman, bukan isi kredensial | Ketentuan P10 | Fani |
| 4 | Project Manager mengisi Bagian A | Peran, baris Project Manager | Fani |
| 5 | Head of Operation menolak serah terima G3 | Peran, baris Head of Operation; Penanganan Pengecualian baris 1 | Fani |
| 6 | Garis balik hypercare ke Bagian B dan keputusan G3 ulang pada form yang sama | Diagram (label garis dan keterangan Gambar 1); Penanganan Pengecualian baris 2 | Fani |
| 7 | Folder checklist G3 dan laporan penutupan sama dengan folder BAST | Rekaman dan Retensi, paragraf pembuka dan dua baris tabel | Fani |
| 8 | Service Delivery Manager sebagai pemilik semua rekaman form ini | Rekaman dan Retensi, paragraf pembuka dan kolom Lokasi dan pemilik | Fani |
| 9 | Tanpa layanan SOC, briefing serah terima (butir 11) cukup ke Lead NOC | Penanganan Pengecualian baris 5 | Fani |
| 10 | Service Delivery dan Project Management dipetakan ke Service Delivery Manager dan Project Manager | Definisi, SD dan PM; dipakai Peran dan Penanganan Pengecualian | Fani |

Label (USULAN) juga muncul di baris definisi "(USULAN)", di Kesimpulan, dan di paragraf pembuka bagian Peran; ketiganya bukan butir baru.

### Open items
| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults.approved_by mengunci Samuel Kristanto Utomo / President Director, dengan pembalik "form operasional disetujui COO bila owner memutus". Spec memakai defaults | Owner |
| 2 | Masa simpan: form ini "Durasi kontrak + 5 tahun", sedangkan FRM-01, FRM-02, FRM-03, FRM-05 yang diarsipkan bersamanya di Bagian C memakai "Durasi kontrak + 3 tahun". Angka 5 tahun dipakai hanya untuk tiga rekaman form ini | Owner, dengan Fani |
| 3 | Checklist G3 di form ini 11 butir, di PRO-OPS-001 §8.2 delapan butir. Butir 2, 8, 10 tidak punya padanan. Form ini tidak diubah; PRO-OPS-001 perlu diselaraskan atau form diakui sebagai versi lengkap | Fani |
| 4 | Pemilik hypercare: form ini dan POL-OPS-001 menulis SD dan PM; PRO-OPS-001 §8.1 baris 10 dan POL-OPS-001 bagian 9.2 menulis Lead NOC. Form ini mengikuti sumbernya sendiri | Fani |
| 5 | "Head of Operation" belum punya pemegang (HR-ORG-01 K-10); hubungannya dengan VP Tech Operation and Services belum ditetapkan (K-09). Form ini memakai nama peran dari sumber | Owner, dengan Fani |
| 6 | Durasi hypercare tidak ada di form ini. POL-OPS-001 menulis 2 minggu berlabel USULAN. Tidak dipindah ke form ini | Fani |
| 7 | Sumber menulis "Operation berhak menolak" tanpa menunjuk peran. Spec menaruhnya pada Head of Operation (USULAN 5); POL-OPS-001 menulis wewenang "menolak serah terima G3" pada Head of Operation (audit baris 165) | Fani |
| 8 | "periode ditetapkan main contractor" (P3): periode pelaksanaan, periode layanan atau garansi, atau keduanya, tidak dirinci | Fani |
| 9 | Penanda tangan Pihak Pertama pada BAST (nama dan jabatan di SINUX) tidak ditunjuk perannya di sumber | Fani |
| 10 | Tempat lessons learned: 

## SNX-OPS-FRM-07 Maintenance Schedule Service Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-07 Maintenance Schedule Service Report (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-07_Maintenance_Schedule_Service_Report.xlsx (1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB, modifiedTime 2026-10-13T06:09:21Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Kepatuhan PM dihitung otomatis sebagai S dibagi jumlah bulan berkode R, S, atau T | "Per aktivitas, isi bulan dengan kode: R = rencana, S = selesai, T = tertunda. Kepatuhan dihitung otomatis (S dibagi R+S+T)." (Kontrol Dokumen B19); rumus `=IF(R6=0,"",S6/R6)` (Jadwal PM T6) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |
| 2 | Service Report hanya untuk PM atau CM yang mengubah sistem, dengan nomor tiket atau CR | "Setiap pelaksanaan PM atau CM yang mengubah sistem dicatat di Service Report beserta nomor tiket atau CR." (Kontrol Dokumen B20) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |
| 3 | Pemilik dokumen Lead NOC, record disimpan 3 tahun, klasifikasi RESTRICTED (Internal), acuan klausul 7.1.3, 8.5.1 dan Annex A 7.13 | "Pemilik dokumen \| Lead NOC"; "Masa simpan record \| 3 tahun"; "Klasifikasi \| RESTRICTED (Internal)"; "Acuan ISO 9001:2015 \| Klausul 7.1.3, 8.5.1"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 7.13" (B10, B14, B9, B12, B13) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB |

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Ganti definisi Kepatuhan menjadi S dibagi (S + T), dengan aturan bahwa Lead NOC mengubah bulan yang lewat tanpa pelaksanaan dari R menjadi T. Rumus baris 6: `=IF(S6+COUNTIF(F6:Q6,"T")=0,"",S6/(S6+COUNTIF(F6:Q6,"T")))`; T47: `=IF(SUM(S6:S45)+COUNTIF(F6:Q45,"T")=0,"",SUM(S6:S45)/(SUM(S6:S45)+COUNTIF(F6:Q45,"T")))`. Diuji di salinan kerja dengan LibreOffice: Januari S dan Februari T pada baris 6 memberi 50%, S saja memberi 100%, keseluruhan 87,5% pada skenario uji. Belum diterapkan | Jadwal PM T6 sampai T45 dan T47; Cara pakai butir 2 | Fani |
| 2 | Setelah USULAN 1 diputus: tulis ambang 95% sebagai butir Cara pakai ke-5 dan beri conditional formatting pada T6 sampai T14 dan T47. Belum diterapkan | Kontrol Dokumen, Jadwal PM | Fani |
| 3 | Tambah baris uji restore triwulanan untuk sistem internal kritis, mengikuti SNX-ISMS-SOP-03 Bagian 7.4 (salinan audit). PIC belum ada di sumber. Belum diterapkan | Jadwal PM baris 15 | Fani |
| 4 | Tambah kolom Tgl tindak lanjut dan Penerima eskalasi di Service Report untuk status Tindak lanjut dan Eskalasi. Belum diterapkan | Service Report, kolom baru | Fani |
| 5 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris. Sudah diterapkan | Kontrol Dokumen A31 sampai E31 | Owner |
| 6 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Lead NOC, ISO/ISMS Coordinator, COO. Semua baris ini USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus. Sudah diterapkan | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Definisi Kepatuhan membuat angkanya 7,87% pada bulan pertama walau semua pekerjaan Januari selesai (temuan A). Putuskan USULAN 1 atau terima pembacaan "progres terhadap rencana tahunan". SNX-OPS-SOP-03 Bagian 9 dan SNX-OPS-RPT-01 KPI 5 memakai istilah dan target yang sama, jadi ketiganya harus selaras | Fani |
| 2 | Ambang 95% hanya ada di gambar Alur Proses, SOP-03 Bagian 9, dan RPT-01. Gambar tidak bisa diubah lewat xlsx_patch; bila ambang berubah, gambar perlu diganti lewat entri LEAD | Fani; orkestrator |
| 3 | Aktivitas harian dan mingguan dicatat satu siklus per bulan, jadi pelaksanaan per shift atau per minggu tidak terlihat di kepatuhan. Terima batas ini atau tetapkan cara mengukurnya | Fani |
| 4 | Uji restore triwulanan sistem internal tidak ada di Jadwal PM (temuan B, USULAN 3) | Fani |
| 5 | Service Report tidak punya tempat mencatat tanggal tindak lanjut atau penerima eskalasi (USULAN 4) | Fani |
| 6 | Cara pakai butir 4 menyebut "menandatangani kolom verifikasi", padahal kolom itu hanya ada di Service Report dan tidak ada kolom tanda tangan di Jadwal PM (temuan D) | Fani |
| 7 | Peran "Lead NOC" (pemilik dokumen), "NOC Engineer", "Lead SOC", dan "Head of Operation" belum dipetakan ke nama. "Head of Operation" tidak sama dengan jabatan Fani (VP Tech Operation and Services). "ISO/ISMS Coordinator" sebagai pemeriksa di sumber digantikan Fani oleh defaults | Fani, owner |
| 8 | Nomor tiket di Service Report ditulis "Zammad" (asumsi 4). Bila ada pekerjaan PM atau CM yang tiketnya di GLPI (generalist), batas ini belum dirinci owner | Owner |
| 9 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti agar tidak ada tanggal karangan. Tanggal efektif tetap "Ditetapkan sa

## SNX-OPS-FRM-08 Technical Ticket Incident Register
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-08 Technical Ticket Incident Register (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-08_Technical_Ticket_Incident_Register.xlsx (1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz, modifiedTime 2026-10-13T06:09:23Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Register adalah rekap audit untuk semua tiket teknis dan insiden; tiket hidup di sistem ticketing, ekspornya boleh ditempel | Kontrol Dokumen B15: "Register seluruh tiket teknis dan insiden dengan waktu Ack dan pemulihan, status SLA, dan tautan RCA sesuai SNX-OPS-SOP-04." dan B18: "Tiket operasional hidup di Zammad (Nusagrid) atau Service Hub GLPI (GMF dan internal). Register ini adalah rekap audit; ekspor dari ticketing system boleh ditempel di sheet Register dengan kolom yang sama." | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |
| 2 | Target Ack dan update per severity berasal dari SOP-04; target pulih berlabel USULAN; jam kerja dihitung sebagai jam kalender | Target Severity A2: "Ack dan update dari SNX-OPS-SOP-04. Target pemulihan = USULAN internal; komitmen ke pelanggan mengikuti kontrak. Jam kerja dihitung sebagai jam kalender untuk penyederhanaan." Nilai B5:B8 (Ack menit) 15, 30, 120, 1440; C5:C8 (update menit) 60, 180, 1440, "Saat selesai"; D4 "Target pulih (jam), USULAN" dengan D5:D8 4, 8, 24, 72 | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |
| 3 | RCA wajib untuk P1 dan P2 dengan nomor dari FRM-10; ambang KPI 95% hanya untuk Ack P1 dan P2 | Kontrol Dokumen B21: "Kolom RCA wajib otomatis Ya untuk P1 dan P2; isi nomor RCA dari SNX-OPS-FRM-10." Ringkasan A11: "P1 dan P2 di-ack sesuai target (KPI 95%)" | 1E0-sXiP8r-lS34-PVvt3RYRT04O56Lnz |

Fakta pendukung yang tidak diubah: Kontrol Dokumen B9 "RESTRICTED (Internal)"; B10 "Lead NOC"; B12 "Klausul 8.5.1, 8.7, 9.1.1"; B14 "3 tahun"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan". Rumus Register (identik tiap baris 5 sampai 305, tidak diubah): P `=IF(G5="","",IF(OR(G5="P1",G5="P2"),"Ya","Tidak"))`; S `=IF(OR(I5="",J5=""),"",ROUND((J5-I5

### USULAN
| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiket Ops dibuat di Zammad dan tiket generalist di Service Hub GLPI. Sumber tim menyebut GMF dan internal sebagai cakupan Service Hub; batas "generalist" belum dirinci owner | Kontrol Dokumen B18 (berlabel USULAN di sel) | Owner, dengan Fani |
| 2 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Lead NOC, ISO/ISMS Coordinator, COO. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Owner (Samuel untuk persetujuannya sendiri) |
| 3 | Pemilik dokumen tetap "Lead NOC" sesuai sumber. Peran ini belum dipetakan ke jabatan; Fani dipakai sebagai pemeriksa karena defaults | Kontrol Dokumen B10 (tidak diubah) | Fani |
| 4 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Owner |
| 5 | Penjaga rumus agar Severity kosong tidak memberi #N/A. U5 menjadi `=IF(OR(S5="",G5=""),"",IF(S5<=INDEX('Target Severity'!$B$5:$B$8,MATCH(G5,'Target Severity'!$A$5:$A$8,0)),"Ya","Tidak"))`; V5 dengan T5 dan kolom D analog; berlaku baris 5 sampai 305 | Register kolom U dan V (belum diterapkan) | Fani |
| 6 | Penanda tiket yang belum di-ack atau belum pulih melewati target, supaya tidak lolos dari hitungan pelanggaran | Register, kolom baru (belum diterapkan) | Fani |
| 7 | Baris KPI "Pulih sesuai target" di Ringkasan, padanan baris 11; angka ambang tidak diusulkan karena tidak ada sumber | Ringkasan (belum diterapkan) | Fani |
| 8 | Kolom "Tgl kirim RCA" di Register agar KPI "RCA P1 dan P2 terkirim dalam 2 hari kerja" (RPT-01) bisa dihitung dari register ini | Register, kolom baru (belum diterapkan) | Fani |

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Pembagian Zammad dan Service Hub GLPI untuk tiket GMF dan internal. SOP-04 sumber menulis "Service Hub untuk GMF dan internal" (7.1 butir 1), FRM-08 sumber sama; premis owner memberi Zammad untuk Ops. SOP-04, FRM-09, dan form ini harus sama | Owner, Fani, lane OPS-SOP-04 |
| 2 | Target Ack P3 dan P4 dihitung sebagai jam kalender sedangkan SOP-04 menulis jam kerja; ML-00 no. 10 masih Terbuka karena kalender kerja belum ditetapkan | Fani |
| 3 | RPT-01 KPI no. 14 butuh tanggal kirim RCA; register tidak punya kolomnya (USULAN 8) | Fani |
| 4 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch: tidak ada cabang tiket Keamanan, dan kotak pertama masih "Zammad atau Service Hub". Butuh entri LEAD bila gambar harus diganti | Orkestrator |
| 5 | Register A2 menautkan tiket Keamanan ke SNX-ISMS-FRM-02 berdasarkan SOP-04 7.2 dan ISMS-SOP-01 Bagian 8. Pelaku pencatat di FRM-02 tidak tertulis di sumber; cocokkan setelah ISMS-SOP-01 dirender | Orkestrator (lane ISMS-SOP-01) |
| 6 | Peran "Lead NOC" sebagai pemilik dokumen belum dipetakan ke jabatan (matriks peran dan SK penunjukan belum ada) | Fani, owner |
| 7 | Keterbatasan alat: kotak legenda A25 tetap biru; nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka. Tinggi baris B18 tetap, teks 3 baris pas di render LibreOffice; HUMAN-VERDICT: lihat di Excel apakah baris B18 terpotong | Orkestrator, owner |
| 8 | Periode default Ringkasan 1 sampai 30 November 2026 (B3 dan B4) lebih akhir dari tanggal draft; sel input, perlu diisi ulang tiap periode | Fani |
| 9 | Masa simpan 3 tahun (sumber) berbeda dari 5 tahun untuk SNX-OPS-FRM-10 dan SNX-ISMS-FRM-02 yang ditautkan; tidak diubah | Fani |
| 10 | Kalimat perintah di sumber ditujukan ke p

## SNX-OPS-FRM-09 SLA Performance Monitoring Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-FRM-09 SLA Performance Monitoring Report (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-FRM-09_SLA_Performance_Monitoring_Report.xlsx (14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF, modifiedTime 2026-10-13T06:09:25Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Workbook ini adalah tempat parameter SLA, log downtime, dan laporan availability bulanan; dasar prosedurnya SNX-OPS-SOP-05 | Kontrol Dokumen B15: "Parameter SLA per pelanggan, log downtime, dan laporan availability bulanan sesuai SNX-OPS-SOP-05." | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |
| 2 | Semua downtime dicatat; yang dikeluarkan dari hitungan hanya yang punya bukti notifikasi maintenance atau pengecualian kontrak. Availability = 1 dikurangi downtime dihitung dibagi menit kalender dalam bulan | Kontrol Dokumen B19: "Catat setiap downtime di Downtime Log; kolom Dihitung = Tidak hanya bila ada bukti notifikasi maintenance atau pengecualian kontrak." Laporan Bulanan B5: `=DAY(B4)*1440`; E8: `=IF(A8="","",1-D8/$B$5)` | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |
| 3 | Laporan dikirim ke pelanggan paling lambat hari kerja ke-5; pemilik dokumen Service Delivery Manager; masa simpan 3 tahun | Kontrol Dokumen B22: "Laporan dikirim ke pelanggan paling lambat hari kerja ke-5." B10: "Service Delivery Manager". B14: "3 tahun" | 14o0dFUVZU-ieDbrLFQXTzwmNIL4SAftF |

Fakta pendukung yang tidak diubah: B9 "RESTRICTED (Internal)"; B12 "Klausul 9.1.1, 9.1.2, 9.1.3"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; Laporan Bulanan A49 "Disusun (Service Delivery Manager)" dan A50 "Diperiksa (Head of Operation)"; status Tercapai atau Breach di F8 `=IF(A8="","",IF(E8>=C8,"Tercapai","Breach"))`; anggaran downtime G8 `=IF(A8="","",ROUND($B$5*(1-C8),1))`. Hasil pemindaian rumus: rumus di seluruh workbook hanya merujuk kolom B, C, D sheet Parameter SLA dan kolom B, C, D, F, G sheet Downtime Log.

### USULAN
Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Service Delivery Manager, ISO/ISMS Coordinator, COO. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | Owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | Owner |
| 3 | Penanda peringatan dini di Laporan Bulanan: tandai baris bila downtime dihitung melewati 50% anggaran (ambang dari SOP-05, nilai menit tidak ada di sumber). Belum diterapkan | Laporan Bulanan kolom H, format kondisional baru | Fani |
| 4 | Availability memperhitungkan kolom Jam layanan, atau dokumen menyatakan bahwa semua SLA diukur 24x7. Selama belum diputus, Parameter SLA A2 hanya menyatakan perilaku rumus yang ada. Belum diterapkan | Laporan Bulanan kolom D dan E, Parameter SLA kolom E | Fani |
| 5 | Daftar pilihan Pelanggan dan Layanan di Downtime Log yang mengambil dari Parameter SLA, dan pemeriksaan kombinasi unik. Belum diterapkan | Downtime Log kolom B dan C, Parameter SLA kolom B dan C | Fani |
| 6 | Alasan pengecualian dipilih dari kolom Pengecualian kontrak di Parameter SLA, bukan teks bebas. Belum diterapkan | Downtime Log kolom I | Fani |
| 7 | Status Response SLA terhadap ambang; ambang 95% sudah ada di SNX-OPS-FRM-08, angka baru tidak diusulkan. Belum diterapkan | Laporan Bulanan kolom K | Fani |

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Pemilik dokumen "Service Delivery Manager" (B10), "Disusun (Service Delivery Manager)" dan "Diperiksa (Head of Operation)" (Laporan Bulanan A49 dan A50) belum dipetakan ke jabatan atau orang; peran ini berbeda dari penanda tangan Kontrol Dokumen (Erik, Fani). Matriks peran dan SK penunjukan belum ada | Fani, owner |
| 2 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Isinya tidak salah terhadap SOP-05, tetapi form tidak punya kolom pencatat "info Commercial" dan tidak ada pemicu otomatis dari status Breach ke RCA | Orkestrator, Fani |
| 3 | Penyebab "Upstream atau supplier" (Daftar B3): SOP-05 Bagian 4 mengecualikan "gangguan di luar tanggung jawab SINUX sesuai kontrak". Belum tertulis kapan gangguan upstream dihitung dan kapan dikecualikan; contoh sumber memberi "Ya" | Fani, Legal |
| 4 | Laporan Bulanan B3 (periode, sel input) berisi 01-Nov-2026 dan perlu diisi ulang tiap periode. Bila owner ingin sel kosong, B4 dan B5 perlu penjaga rumus | Fani |
| 5 | Downtime yang melintasi pergantian bulan dihitung seluruhnya di bulan Mulai (rumus sumber); aturan pemecahan belum ada di sumber | Fani |
| 6 | SOP-05 (salinan audit) Bagian 6.2 butir 2 menulis "Zammad untuk Nusagrid, Service Hub untuk GMF dan internal", sedangkan premis owner memberi Zammad untuk Ops dan GLPI untuk generalist. FRM-09 tidak menyebut sistem tiket (hanya kolom "Ref tiket atau CR" dan rujukan ke FRM-08), jadi tidak ada yang diubah di sini; SOP-05, FRM-08, dan form ini harus sama | Owner, lane OPS-SOP-05 dan OPS-FRM-08 |
| 7 | Format xlsx tidak punya bagian Dokumen terkait, tabel rekaman (lokasi, pemilik), ataupun scope. Kode yang dirujuk di sel: SNX-OPS-SOP-05, SNX-OPS-FRM-08; di gambar: FRM-10. Lokasi simpan dan pemilik rekaman tidak ada di sumber; m

## SNX-OPS-FRM-10 RCA Corrective Action Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: PASSED
- Berkas: out/07_Ops/SNX-OPS-FRM-10 RCA Corrective Action Report (Rev00 DRAFT).docx
- Sumber: SNX-OPS-FRM-10_RCA_Corrective_Action_Report.docx (1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS, modifiedTime 2026-10-13T06:09:03Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | RCA wajib untuk empat pemicu dan dikirim ke pelanggan dalam batas waktu; tenggat 2 hari kerja berlaku untuk RCA insiden | "Template ini wajib untuk insiden P1 dan P2, insiden berulang, breach SLA, dan ketidaksesuaian audit, sesuai SNX-OPS-SOP-04 Bagian 7.5 dan ISO 9001 klausul 10.2. RCA insiden dikirim ke pelanggan via email paling lambat 2 hari kerja setelah layanan pulih." | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |
| 2 | Pemilik dokumen Head of Operation; acuan ISO 10.2 dan Annex A 5.27; retensi 5 tahun | "Pemilik dokumen \| Head of Operation"; "Acuan ISO 9001:2015 \| Klausul 10.2"; "Acuan ISO/IEC 27001:2022 \| Klausul atau kontrol Annex A 5.27"; "Masa simpan record \| 5 tahun" | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |
| 3 | RCA ditutup hanya setelah tindakan terbukti efektif; urutan gambar menaruh "Setujui dan kirim" sebelum "Laksanakan tindakan" dan "Tindakan efektif?" | Judul gambar: "RCA ditutup hanya setelah tindakan terbukti efektif"; kotak: "Setujui dan kirim" dengan sub-label "Head of Operation, maksimal 2 hari kerja"; kotak "Tindakan lanjutan" dengan sub-label "kembali ke analisis" (word/media/rId21.png) | 1XFMQDye_WWWomRpwmT6KGMRdi4EVbRsS |

### USULAN
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

Jumlah USULAN: 8 butir (9 penanda "(USULAN)" di badan dokumen karena butir 5 muncul tiga kali; butir 8 tanpa penanda di badan). Tidak ada angka baru berlabel USULAN: 2 hari kerja, 3 kali dalam 30 hari, 90 hari (contoh), dan 5 tahun 

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Urutan kirim dan tutup: urutan gambar sumber (kirim sebelum efektif) dan judul gambar (tutup sesudah efektif) berbeda bacaan. Spec memisahkan "kirim" dan "tutup" berdasarkan SOP-04 Bagian 7.5. Perlu konfirmasi bahwa RCA terkirim dengan tindakan yang masih berjalan | Fani |
| 2 | Kapan memakai 5 Why, Fishbone, atau keduanya tidak ditulis di sumber; gambar menulis "dan", form memberi pilihan | Fani |
| 3 | Pelaku tidak tertulis di sumber: pencatatan nomor RCA di kolom No RCA SNX-OPS-FRM-08 (langkah 5), penambahan risiko baru ke SNX-ISMS-REG-02 (catatan di bawah tabel Tindakan, pemilik REG-02 menurut audit: ISMS Coordinator), pencatatan insiden keamanan informasi di SNX-ISMS-FRM-02 (Lingkup). Kalimatnya dibiarkan tanpa pelaku | Fani, lane ISMS |
| 4 | Peran Pemverifikasi dan penutup RCA belum ada di sumber (USULAN 5 dan 6); kolom "Diverifikasi oleh" kosong di sumber | Fani |
| 5 | SOP-04 Bagian 5 menugaskan Service Delivery Manager memastikan RCA terkirim dan Lead NOC menyusun RCA P1 dan P2; FRM-10 sumber menugaskan Head of Operation menyetujui dan mengirim, dan Lead NOC atau Lead SOC menyusun tanpa menyebut kapan NOC dan kapan SOC. SOP-04 dan form ini perlu selaras | Fani, lane OPS-SOP-04 |
| 6 | Kriteria efektif baku belum ada; "90 hari" dan "alert baru terbukti menangkap gejala" di sumber hanya contoh | Fani |
| 7 | Tujuan penyimpanan lessons learned: sumber menulis "disetor ke knowledge base" lewat jalur internal yang dibuang; field "Lessons learned disimpan di" dibiarkan kosong. Sama dengan open item 10 di notes OPS-FRM-06 | Owner, Fani |
| 8 | Penerima dan tenggat RCA untuk breach SLA dan ketidaksesuaian audit tidak tertulis; 2 hari kerja hanya untuk RCA insiden. SOP-05 Bagian 6.6 menyerahkan konsekuensi kontraktual ke Co

## SNX-OPS-RPT-01 Operations KPI Performance Report
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/07_Ops/SNX-OPS-RPT-01 Operations KPI Performance Report (Rev00 DRAFT).xlsx
- Sumber: SNX-OPS-RPT-01_Operations_KPI_Performance_Report.xlsx (1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO, modifiedTime 2026-10-13T06:09:47Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Workbook ini adalah laporan bulanan KPI dan kinerja Divisi Operation, dipakai sebagai masukan pemantauan klausul 9.1 dan tinjauan manajemen klausul 9.3.2 | Kontrol Dokumen B15: "Laporan bulanan KPI dan kinerja Divisi Operation, masukan pemantauan klausul 9.1 dan tinjauan manajemen klausul 9.3.2." | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |
| 2 | Sheet KPI memuat 17 KPI (NOC 6, SOC 4, SD dan PM 4, ISMS 2, Semua 1), masing-masing dengan arah, target, dan sumber data; status dihitung dari bulan terakhir yang terisi, bukan dari rata-rata YTD | KPI C6: "Availability layanan yang dikelola", D6: "≥", E6: 0.999, F6: "SNX-OPS-FRM-09". KPI U6: `=IF(T6="","Belum diukur",IF(D6="≥",IF(T6>=E6,"Tercapai","Di bawah target"),IF(T6<=E6,"Tercapai","Di bawah target")))`. T6: `=IF(COUNT(G6:R6)=0,"",LOOKUP(2,1/(G6:R6<>""),G6:R6))` | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |
| 3 | Nilai aktual diisi setiap awal bulan untuk bulan sebelumnya; target adalah target awal yang dikalibrasi setelah 3 bulan data; masa simpan record 3 tahun; pemilik dokumen Head of Operation | Kontrol Dokumen B19: "Setiap awal bulan, isi nilai aktual bulan sebelumnya dari sumber data di kolom Sumber. Persentase ditulis sebagai pecahan (0.95 = 95%)." B22: "Target adalah target awal dan dikalibrasi setelah 3 bulan data." B14: "3 tahun". B10: "Head of Operation" | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |

Fakta pendukung yang tidak diubah: B2 "PT Strategi Integrasi Nusantara (SINUX) · Divisi Operation"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B9 "RESTRICTED (Internal)"; B12 "Klausul 9.1, 9.3.2"; KPI B3 = 2027; seluruh 17 baris KPI (nama, arah, target, sumber) dan rumus S, T, U, U24; Narasi Bulanan A1 sampai A16 kecuali A9. Sel nilai

### USULAN
Label (USULAN) tidak ditulis di sel xlsx karena sel yang berubah tidak memuat angka atau fakta baru; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, COO di sumber. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus. Diterapkan | Kontrol Dokumen B11, B36 sampai B38 | Owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris. Diterapkan | Kontrol Dokumen A32 sampai E32 | Owner |
| 3 | Target 17 KPI diperlakukan sebagai usulan awal sampai disahkan. Salinan audit mencatat butir 2 di Keputusan dan Gap SNX-OPS-ML-00 ("Sahkan target berlabel USULAN") tanpa menyebut target KPI. Belum diterapkan | KPI E6:E22, Cara pakai butir 5 | Fani |
| 4 | Definisi operasional per KPI (rumus numerator dan denominator, frekuensi, pemilik KPI) sebagai kolom atau sheet baru. Kolom "Rumus indikator" di salinan audit adalah inferensi, bukan isi sumber. Belum diterapkan | KPI sheet atau sheet baru | Fani |
| 5 | KPI 6: samakan nama KPI dengan rumus kolom "Tanpa rollback darurat" di SNX-OPS-FRM-04 (berlaku untuk semua jenis change), atau jadikan rumus itu khusus change darurat. Belum diterapkan | KPI C11, SNX-OPS-FRM-04 Ringkasan | Fani |
| 6 | KPI 10: Rata-rata YTD diganti jumlah kejadian, atau dikecualikan dari rata-rata, karena KPI ini hitungan bertarget 0. Belum diterapkan | KPI S15 | Fani |
| 7 | KPI 15: aturan pengisian bulan tanpa kegiatan untuk KPI triwulanan, misalnya kolom bulan review saja yang diisi. Belum diterapkan | KPI baris 20, Cara pakai butir 2 

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Kotak pertama menulis "FRM-01 sampai FRM-09, register", sedangkan KPI 14 bersumber SNX-OPS-FRM-10 dan KPI 3, 4, 7, 9, 10 bersumber SNX-ISMS-FRM-01 dan SNX-ISMS-FRM-02. Gambar juga memakai "COO" saja tanpa "Direktur (COO)" | Orkestrator, Fani |
| 2 | Tiga sumber KPI tanpa nomor dokumen: "Shift Log" (F22), "Tiket vulnerability" (F13), dan "SIEM" (F12). Sumber tidak menyebut sistem tiket untuk "Tiket vulnerability"; aturan tiket Zammad untuk Ops belum bisa diterapkan tanpa memastikan lingkupnya, jadi tidak ada sistem yang ditambahkan | Fani |
| 3 | KPI 14 butuh tanggal kirim RCA; register SNX-OPS-FRM-08 tidak punya kolomnya (USULAN 8 di notes/OPS-FRM-08.md) | Fani |
| 4 | Pemilik dokumen "Head of Operation" (B10) tidak sama dengan pemeriksa Fani Fatullah (VP Tech Operation and Services). HR-ORG-01 K-09 mencatat hubungan kedua jabatan belum ditetapkan, dan belum ada pemegang bernama untuk Head of Operation. Narasi Bulanan A16 tetap "Diperiksa oleh COO dan tanggal" menurut sumber, berbeda dari penyetuju dokumen di B11 | Fani, owner |
| 5 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Sumber tidak menyebut yang dikecualikan dari laporan, lokasi simpan, maupun pemilik rekaman; masa simpan 3 tahun dari sumber. Kode yang dirujuk di kolom Sumber: SNX-OPS-FRM-01, FRM-04, FRM-07, FRM-08, FRM-09, FRM-10, SNX-ISMS-FRM-01, FRM-02, REG-03, REG-04 (semua ada di config/worklist.json) | Orkestrator, Fani |
| 6 | KPI B3 = 2027 berasal dari tim, sedangkan tanggal draft 13 Oktober 2026. Tidak diubah; perlu konfirmasi bahwa 2027 adalah tahun pelaporan pertama | Fani |
| 7 | Tanggal draft 13 Oktober 2026 (B7 dan B31) berasal dari tim dan lebih awa

## SNX-ISMS-REG-01 Information Asset Register
- State: DONE; lint: True; verifikasi: None; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-REG-01 Information Asset Register (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-REG-01_Information_Asset_Register.xlsx (1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP, modifiedTime 2026-10-13T06:09:35Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Head of Operation | "Pemilik dokumen" / "Head of Operation" (Kontrol Dokumen!A10, B10) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |
| Nilai aset diambil dari nilai tertinggi C, I, A; kritikalitas tiga tingkat | "Nilai aset = nilai tertinggi dari C, I, A. Kritikalitas: 3 Tinggi, 2 Sedang, 1 Rendah." (Register Aset!A2) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |
| Review aset tiap 6 bulan dan aset baru didaftarkan paling lambat saat mulai dipakai | "Review berikutnya dihitung otomatis 6 bulan setelah review terakhir; baris merah berarti review terlambat." (Kontrol Dokumen!B21) dan "Daftarkan setiap aset baru paling lambat saat mulai dipakai; aset pelanggan wajib sebelum gate G3." (B18) | 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP |

### USULAN
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Kata "baris merah" di Kontrol Dokumen!B21 dan di gambar Alur Proses tidak cocok dengan aturan warna: yang merah hanya sel Review berikutnya, dan hanya bila status Aktif. Usulan ganti jadi "sel Review berikutnya berwarna merah bila tanggalnya lewat dan status Aktif". Tidak saya ubah karena gambar tidak bisa disunting alat dan teks sel akan berbeda dari gambar | Fani |
| 2 | Dropdown Klasifikasi (Daftar!B4) berisi "RESTRICTED", sedangkan tingkat SNX-ISMS-PRO-01 dan label dokumen berbunyi "RESTRICTED (Internal)". Usulan samakan nilainya sekaligus aturan warna kolom H (yang mencocokkan teks "RESTRICTED"), supaya warna kuning tidak hilang | Fani |

### Open items
| # | Butir | Pemutus atau pelaksana |
|---|---|---|
| 1 | Register Aset kini kosong: 12 aset kandidat (bagian 6) dihapus karena bertanda CONTOH. Ops memverifikasi pemilik, klasifikasi, C/I/A, CI, Backup, Monitoring, lalu mengisi ulang. Sebelum dipakai audit, isi harus ada; kandidat AST-010 dan AST-011 bernilai 3 tetapi Backup "Tidak". Aset pelanggan belum ada satu baris pun (Cara pakai butir 1: wajib sebelum gate G3) | Fani (Ops mengisi) |
| 2 | Pemilik aset AST-005 ditulis "Tech dan Product" (nama fungsi). Saat diisi ulang, pakai nama peran dari Struktur Organisasi (HR-ORG-01); peran yang sudah ada di sana antara lain Head of Operation dan Lead NOC | Fani |
| 3 | Vault: kandidat AST-001 menulis vault.sinux.co.id. Sesuai aturan vault, statusnya "menunggu konfirmasi Ops"; tidak ada baris vault di dokumen sekarang | Ops (Fani) |
| 4 | Tiket: kandidat AST-002 (GLPI, "Tiket GMF dedicated dan permintaan internal") dan AST-003 (Zammad, "Tiket pelanggan Nusagrid (WhatsApp, telepon)"). Batas "generalist" untuk GLPI belum dirinci owner, jadi pembagian dua sistem ini belum bisa dipastikan dari sumber | owner |
| 5 | Pemetaan acuan 5.10 dan 5.11: workbook ini tidak punya kolom pemakaian wajar atau pengembalian aset. Di SNX-ISMS-SOP-04 kedua kontrol itu ada (6.2 dan 6.4). Konfirmasi bahwa acuan 5.10 dan 5.11 di Kontrol Dokumen REG-01 cukup lewat SOP-04, atau tambah kolom (alat xlsx tidak bisa menambah kolom) | Fani, konsultan SoA |
| 6 | Hubungan Head of Operation (pemilik dokumen dan pemilik banyak aset) dengan VP Tech Operation and Services belum ditetapkan di Struktur Organisasi (butir K-09 di spec HR-ORG-01). Pemilik dokumen tetap "Head of Operation" mengikuti sumber | owner |
| 7 | Tidak ada sel untuk masa tinjau dokumen (YEARLY) di Kontrol Dokumen, jadi nilai itu tidak terce
- Baris CONTOH AST-001 sampai AST-012 dikosongkan; ISMS-REG-02 dan REG-03 masih merujuk ID AST itu. Ops mengisi ulang register aset dengan ID yang sama atau memperbarui rujukan.

## SNX-ISMS-REG-02 IS Risk Assessment Register
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-REG-02 IS Risk Assessment Register (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-REG-02_IS_Risk_Assessment_Register.xlsx (1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q, modifiedTime 2026-10-13T06:09:37Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Skor = Likelihood x Impact pada skala 1 sampai 5; level dihitung otomatis dari skor dengan empat ambang | Matriks Risiko A3: "Skor = Likelihood x Impact. Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25". Register Risiko I5: `=IF(OR(G5="",H5=""),"",G5*H5)` | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |
| 2 | Level Rendah diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03; risiko Kritis dilaporkan ke COO dan hanya COO yang menerimanya, secara tertulis | Kontrol Dokumen B20: "Kriteria penerimaan: level Rendah dapat diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03." Matriks Risiko B24: "Tindakan segera; dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis" | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |
| 3 | Register berisi 15 risiko (ISR-001 sampai ISR-015) yang berstatus usulan awal Divisi Operation dan belum disetujui; penilaian ulang minimal tahunan, setelah insiden P1, dan setelah perubahan besar | Register Risiko A2: "Baris biru muda = usulan awal, bukan baris contoh: validasi lalu ubah kolom Catatan menjadi Disetujui." Q5 sampai Q19: "Usulan awal". Kontrol Dokumen B21: "Penilaian ulang minimal tahunan, setelah insiden P1, dan setelah perubahan besar." | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |

Fakta pendukung yang tidak diubah: B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B10 "ISMS Coordinator" (Pemilik dokumen, jabatan tanpa nama); B14 "Berlaku sampai digantikan"; B22 "Usulan awal Divisi Operation dari riwayat operasi di knowledge base SINUX; wajib divalidasi ISMS Coordinator dan pemilik risiko." Hitung ulang atas out.xlsx lewat LibreOffice (xlsx ke xlsx, dibaca data_only

### USULAN
Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan ISMS Coordinator, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Pilih satu rumusan penerimaan risiko Kritis: dicatat sebagai penerimaan tertulis COO di kolom Diterima oleh dan Tanggal penerimaan SNX-ISMS-REG-03, atau Matriks B24 diubah mengikuti REG-03. Belum diterapkan | Matriks Risiko B24; REG-03 Cara pakai butir 3 | owner (Amirull sebagai COO) |
| 4 | Tambah satu kalimat Cara pakai: L dan I di register ini dinilai dengan kontrol eksisting diperhitungkan, risiko sisa dinilai di SNX-ISMS-REG-03. Belum diterapkan karena baris butir 1 sampai 5 hanya muat dua baris teks | Kontrol Dokumen Cara pakai | Fani |
| 5 | Rujuk ID aset REG-01: ISR-006 ke AST-007 (Acronis), ISR-008 ke AST-002, AST-003, AST-006. Dibuat sesudah REG-01 diisi ulang oleh Ops, karena ID bisa berubah. Belum diterapkan | Register Risiko B10 dan B12 | Fani |
| 6 | Sebut sistem tiket pada ISR-008: Zammad (tiket Ops) atau Zammad dan GLPI. Sumber menulis "ticketing system" tanpa nama. Batas "generalist" untuk GLPI belum dirinci owner. Belum diterapkan | Register Risiko B12 | owner |
| 7 | Ganti "dinaikkan ke register risiko ISMS" dengan rujukan yang ada, misalnya "dicat

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Register Risiko merujuk AST-001, AST-005, AST-009, AST-012, sedangkan lane REG-01 mengosongkan 12 baris aset itu karena bertanda CONTOH. Rujukan baru valid sesudah Ops mengisi ulang REG-01 dengan ID yang sama; ID, nama, dan pemilik harus dicocokkan saat itu | Fani, lane ISMS-REG-01 |
| 2 | 15 risiko belum divalidasi (Catatan tetap "Usulan awal"). Validator yang disebut sumber, ISMS Coordinator, belum dipetakan ke jabatan atau orang (HR-ORG-01 tidak menetapkannya); pemilik risiko Head of Operation berhubungan dengan VP Tech Operation and Services belum ditetapkan (K-09 di HR-ORG-01) | Fani, owner |
| 3 | Vault: ISR-001 menulis "belum live"; REG-01 sumber menulis AST-001 vault.sinux.co.id berstatus "Aktif". Kondisi hari ini tidak terukur. Sampai Ops mengonfirmasi, F5 memuat "menunggu konfirmasi Ops" | Ops (Fani) |
| 4 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Kotak "Terima risiko" tidak punya panah lanjutan, dan gambar tidak menunjukkan jalur risiko Kritis ke COO (hanya cabang Rendah dan bukan Rendah). Legenda A2 sudah disesuaikan; bila gambar diperbarui, legenda ikut ditinjau | Orkestrator, Fani |
| 5 | Penerimaan risiko Kritis: Matriks B24 mensyaratkan penerimaan tertulis COO, REG-03 menyebut penerimaan residual oleh pemilik risiko, dan ISR-002 berpemilik Lead SOC. Belum ada aturan yang menyatukan, dan register tidak punya kolom tenggat. Lihat USULAN 3 | owner |
| 6 | Format xlsx tidak punya bagian Dokumen terkait, tabel rekaman (lokasi, pemilik), ataupun scope. Kode yang dirujuk di sel: SNX-ISMS-REG-01, SNX-ISMS-REG-03; di gambar sama. Lokasi simpan dan pemilik rekaman tidak ada di sumber. Masa simpan "Berlaku sampai digantikan" dipertahankan; tidak ada masa simpan untuk versi lama register maupun untuk pener
- Merujuk AST-001/005/009/012 yang di REG-01 sudah dikosongkan (baris CONTOH); valid setelah Ops mengisi ulang REG-01.

## SNX-ISMS-REG-03 IS Risk Treatment Plan
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-REG-03 IS Risk Treatment Plan (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-REG-03_IS_Risk_Treatment_Plan.xlsx (1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ, modifiedTime 2026-10-13T06:09:40Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Target tanggal dan nilai residual di 15 baris adalah usulan, ditetapkan bersama pemilik risiko | Rencana Penanganan!A2: "Target tanggal dan residual adalah usulan; ditetapkan bersama pemilik risiko." | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |
| 2 | Skor residual = L x I; level dihitung otomatis dengan ambang 5, 10, 20 | Rencana Penanganan!N5: `=IF(OR(L5="",M5=""),"",L5*M5)`; O5: `=IF(N5="","",IF(N5>=20,"Kritis",IF(N5>=10,"Tinggi",IF(N5>=5,"Sedang","Rendah"))))` | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |
| 3 | Risiko residual harus diterima pemilik risiko secara tertulis; kolom penerimaan masih kosong di 15 baris | Kontrol Dokumen!B20: "Risiko residual harus diterima pemilik risiko secara tertulis (kolom Diterima oleh dan Tanggal penerimaan)." | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |

Fakta pendukung yang tidak diubah: B10 "ISMS Coordinator" (Pemilik dokumen); B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B14 "Berlaku sampai digantikan"; B22 "Usulan awal Divisi Operation dari riwayat operasi di knowledge base SINUX; wajib divalidasi ISMS Coordinator dan pemilik risiko." Pengukuran atas out.xlsx (LibreOffice xlsx ke xlsx, dibaca data_only, dibandingkan dengan hitungan python L x I): 15 baris RTP-001 sampai RTP-015, level residual Tinggi 2 (RTP-002 skor 12, RTP-005 skor 10), Sedang 11, Rendah 2 (RTP-008 skor 3, RTP-015 skor 4), nol sel galat; Opsi semua Mitigasi; Status semua Belum mulai; target 2027-03-31 sebanyak 11 dan 2027-06-30 sebanyak 4; pemilik Head of Operation 6, Lead SOC 3, Lead NOC 3, Tech dan Product 1, Service Delivery Manager 1, ISMS Coordinator 1. Kolom I, P, Q, R kosong di baris 5 sampai 19 (dicek langsung). Ambang rumus sama dengan Matriks Risiko REG-02 yang dikutip d

### USULAN
Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan ISMS Coordinator, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Pilih satu rumusan penerimaan residual: pemilik risiko menerima secara tertulis (Cara pakai butir 3 dan gambar), atau risiko yang awalnya Kritis (RTP-002) diterima COO secara tertulis mengikuti Matriks Risiko B24 REG-02. Sama dengan USULAN 3 di notes/ISMS-REG-02.md. Belum diterapkan | Kontrol Dokumen B20; Alur Proses; REG-02 Matriks B24 | owner (Amirull sebagai COO) |
| 4 | Ganti pemilik RTP-007 "Tech dan Product" (nama fungsi) dengan "Manager of Product Tech" (JA-05 di Struktur Organisasi, jabatan terdekat), serentak di REG-01, REG-02 K11, dan REG-03 H11 supaya tiga dokumen sama. Belum diterapkan karena REG-01 dan REG-02 masih memakai nama lama. Bila disetujui, tambahkan satu baris di patch: `"Rencana Penanganan!H11": "Manager of Product Tech"` | Rencana Penanganan H11 | Fani |
| 5 | Sebut sistem tiket pada risiko ISR-008 (RTP-008): Zammad untuk tiket Ops, atau Zammad dan GLPI. Sumber menulis "ticketing system" tanpa nama; batas "generalist" untuk GLPI belum dirinci owner. Belum diterapkan, sejajar dengan USULAN 6 di notes/ISMS-REG-02.md | Rencana Penanganan C12 | o

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Kode yang dirujuk di sel: SNX-ISMS-REG-02, SNX-ISMS-SOA-01, SNX-ISMS-SOP-05, SNX-ISMS-PLN-01, SNX-ISMS-FRM-01, SNX-ISMS-REG-04, SNX-ISMS-PRO-01; semua ada di config/checklist.json (baris 80, 82, 89, 91, 87, 85, 79). Pengecualian lingkup (risiko Rendah tidak masuk rencana) tersirat di gambar ("Risiko Sedang ke atas dari SNX-ISMS-REG-02") dan di kutipan REG-02 B20 pada notes/ISMS-REG-02.md ("level Rendah dapat diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03."), tetapi tidak tertulis di Kontrol Dokumen REG-03. Lokasi simpan dan pemilik rekaman tidak ada di sumber. Masa simpan "Berlaku sampai digantikan" dipertahankan; tidak ada masa simpan untuk bukti penerimaan risiko tertulis, dan angka tidak diusulkan karena tidak ada dasar | Orkestrator, Fani |
| 2 | Vault: RTP-001 menulis "migrasi ... ke vault" dan RTP-010 "kredensial hanya melalui vault". Di REG-01 sumber vault berstatus "Aktif", di REG-02 sumber "belum live" (CONTEXT-PACK butir 6). Kondisi hari ini tidak terukur. Sampai Ops mengonfirmasi, status "menunggu konfirmasi Ops" ditulis di A2 sheet Rencana Penanganan | Ops (Fani) |
| 3 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Panah "tidak" menuju "Tindakan tambahan, kembali ke opsi" tidak punya garis kembali. Gambar juga tidak menunjukkan jalur penerimaan risiko Kritis oleh COO (lihat USULAN 3). Legenda A2 sudah disesuaikan; bila gambar diperbarui, legenda ikut ditinjau | Orkestrator, Fani |
| 4 | Kolom I (Sumber daya atau biaya), P (Diterima oleh), Q (Tgl penerimaan), R (Bukti penyelesaian) kosong di 15 baris. Biaya, nama penerima, tanggal, dan bukti tidak ada di sumber, jadi dibiarkan
- 15 baris biru dipertahankan sebagai usulan awal tim (bukan CONTOH), konsisten dengan REG-02; LEAD/Fani memutus bila dianggap dummy.

## SNX-ISMS-REG-04 User Access Register Periodic Review
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-REG-04 User Access Register Periodic Review (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-REG-04_User_Access_Register_Periodic_Review.xlsx (14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT, modifiedTime 2026-10-13T06:09:42Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Akun privileged (level Admin atau Privileged) ditinjau tiap 3 bulan, akun biasa tiap 6 bulan; tanggal Review berikutnya dihitung dari Review terakhir | Kontrol Dokumen B19: "Kolom Privileged, Review berikutnya, dan Cek dihitung otomatis: privileged ditinjau triwulanan, akses biasa semesteran." Register Akses Q5: `=IF(P5="","",EDATE(P5,IF(H5="Ya",3,6)))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |
| 2 | Hasil review dicatat di sheet Review Periodik dan tindak lanjutnya paling lama 10 hari kerja; keputusan hanya Tetap, Ubah, atau Cabut, dan status Terbuka bertahan sampai tanggal tindak lanjut diisi | Kontrol Dokumen B21: "Hasil review periodik dicatat di sheet Review Periodik; tindak lanjut maksimal 10 hari kerja." Review Periodik L5: `=IF(G5="","",IF(G5="Tetap","Selesai",IF(J5="","Terbuka","Selesai")))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |
| 3 | Kolom Cek menandai tiga kondisi pada akun berstatus Aktif (CABUT, KEDALUWARSA, REVIEW); Cara pakai sumber hanya menyebut dua | Kontrol Dokumen B20: "Cek = CABUT bila personel berstatus Keluar tetapi akun masih Aktif; Cek = REVIEW bila review terlambat." Register Akses R5: `=IF(A5="","",IF(AND(D5="Keluar",O5="Aktif"),"CABUT",IF(AND(M5<>"",M5<TODAY(),O5="Aktif"),"KEDALUWARSA",IF(AND(Q5<>"",Q5<TODAY(),O5="Aktif"),"REVIEW","OK"))))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |

Fakta pendukung: B14 "3 tahun" (masa simpan record, sama dengan Bagian 8 SOP-02 menurut salinan audit); B10 "Head of Operation" (Pemilik dokumen, jabatan tanpa nama); B15 "Register hak akses pengguna ke sistem internal dan sistem pelanggan, serta catatan review akses periodik sesuai SNX-ISMS-SOP-02."; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B12 "Klausul 7.1.3"; Daft

### USULAN
Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Diterapkan | Pemutus yang disarankan |
|---|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B35 sampai B37 | Ya | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A31 sampai E31 | Ya | owner |
| 3 | Baris Review Periodik 5 diperlakukan sebagai data contoh dan dikosongkan. Bila tim menganggapnya riwayat nyata, kembalikan dengan menghapus `"Review Periodik": [5]` dari patch | Review Periodik baris 5 | Ya | Fani |
| 4 | Tambah satu kalimat Cara pakai: Review terakhir diisi dengan Tgl diberikan saat akun baru dicatat, supaya Review berikutnya terhitung | Kontrol Dokumen Cara pakai | Belum (butir 1 sampai 4 hanya muat satu atau dua baris teks) | Fani |
| 5 | Sebut sistem tiket pada kolom Ref tiket atau Cara pakai butir 1: Zammad untuk tiket Ops, GLPI (Service Hub) untuk generalist; batas "generalist" belum dirinci owner | Register Akses J4; Cara pakai | Belum | owner |
| 6 | Tulis titik awal hitungan masa simpan 3 tahun (sumber hanya menulis "3 tahun") | Kontrol Dokumen B14 | Belum | Fani |
| 7 | Samakan nilai Level akses dengan matriks SOP-02 (Agent, Group admin, Analyst, Collection), atau tambah matriks akses per sistem dan peran sebagai sheet baru | Daftar B2:B5; sheet baru | Belum | Fani |
| 8 | Hitung juga MFA "Tidak didukung" di Ring

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Register Akses kosong sesudah baris CONTOH dihapus. Ops harus mengisi akun nyata (satu baris per akun per sistem, tanpa password atau token) sebelum audit; ISR-009 di REG-02 dan RTP-009 di REG-03 ("Terapkan SNX-ISMS-REG-04 dan review akses privileged triwulanan", menurut salinan audit) belum punya register terisi sebagai bukti. HUMAN-VERDICT: kecukupan isi register terhadap daftar akun sistem sebenarnya tidak bisa dibuktikan dari berkas ini | Fani, Ops |
| 2 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Sumber tidak menyebut yang dikecualikan dari register (misalnya sistem atau jenis akun yang tidak dicatat), lokasi simpan, maupun pemilik rekaman selain "Pemilik dokumen Head of Operation". Kode yang dirujuk di sel: SNX-ISMS-SOP-02 (B15). Masa simpan 3 tahun dipertahankan | Orkestrator, Fani |
| 3 | Dropdown Level (Read-only, Operator, Admin, Privileged) tidak sama dengan istilah matriks SOP-02, dan REG-04 tidak punya matriks per sistem dan peran padahal SOP-02 menyerahkan detailnya ke sini. Lihat USULAN 7 | Fani |
| 4 | Pemetaan peran sumber ke nama peran HR-ORG-01: "Head of Operation" persis sama (pemilik dokumen B10; HR-ORG-01 menandainya USULAN tanpa pemegang, K-10 dan K-11, dan hubungannya dengan VP Tech Operation and Services belum ditetapkan, K-09). "ISO/ISMS Coordinator" (pemeriksa di sumber) dan "COO" (penyetuju di sumber) diganti oleh tiga penanda tangan defaults.json; HR-ORG-01 menulis ISMS Coordinator "belum ditetapkan" (K-13). Header Review Periodik F4 "Reviewer (pemilik sistem)" dan K4 "Pelaksana tindak lanjut" tidak punya padanan jabatan di HR-ORG-01; SOP-02 memakai "Pemilik sistem" dan "Administrator sistem". Header tidak diubah (suara tim) | Fani, owner |
| 5 |

## SNX-ISMS-FRM-01 Backup Log Restore Testing Records
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-FRM-01 Backup Log Restore Testing Records (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-FRM-01_Backup_Log_Restore_Testing_Records.xlsx (1J436lMZJSgowkEeMD6m45N70h7Go6_ZV, modifiedTime 2026-10-13T06:09:28Z)

### Fakta kunci
| Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|
| Pemilik dokumen adalah peran Lead NOC; masa simpan record 3 tahun | "Pemilik dokumen" / "Lead NOC" (Kontrol Dokumen!A10, B10); "Masa simpan record" / "3 tahun" (Kontrol Dokumen!A14, B14) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |
| Status Gagal dua kali berturut menjadi tiket P2 | "Shift malam mengisi Backup Log setiap hari; status Gagal dua kali berturut menjadi tiket P2." (Kontrol Dokumen!B19) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |
| Restore ke produksi butuh dua persetujuan | "Durasi, RTO, dan kepatuhan dihitung otomatis. Restore ke produksi butuh approval Lead NOC dan persetujuan pelanggan." (Restore Record!A2) | 1J436lMZJSgowkEeMD6m45N70h7Go6_ZV |

### USULAN
| # | Butir | Status di berkas | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga nama di blok Pengesahan dan B11: Erik Dwi Yanto (Disusun), Fani Fatullah (Diperiksa), Samuel Kristanto Utomo (Disetujui). Sumber menulis peran saja ("Lead NOC", "ISO/ISMS Coordinator") dan COO sebagai penyetuju. Defaults menandai baris ini USULAN, dengan pembalik "form operasional disetujui COO bila owner memutus" | Diterapkan | owner (nama penyetuju: owner atau Samuel) |
| 2 | Peran "Shift malam" di B19 dipetakan ke NOC Engineer. Dasarnya SOP-03 Bagian 5 (NOC Engineer "mengisi log") dan HR-ORG-01 (NOC Engineer, pola shift); jabatan itu USULAN di sumbernya dan belum ada pemegang | Diterapkan di B19 | Fani |
| 3 | Sistem tiket P2 backup = Zammad. Premis owner menyebut Zammad untuk Ops; saya menafsirkan tiket P2 backup sebagai tiket Ops karena pemilik dokumen adalah Lead NOC. Sumber tidak menyebut sistem tiket | Diterapkan di B19 | Fani |
| 4 | Salinan offline (break-glass) kunci enkripsi backup di luar password manager. Sumber tidak menyebut salinan itu; aturan lintas dokumen meminta label USULAN | Diterapkan di Daftar Job!A2 | Fani |
| 5 | Wadah ukur untuk KPI SOP-03 yang belum punya tempat di Ringkasan: "Uji restore bulanan terlaksana per pelanggan backup" 100%, "Waktu restore uji dalam RTO" 100% (persentase dari B11 dibagi B8), dan kolom percobaan ke berapa untuk "Uji restore berhasil pada percobaan pertama" 95% | Tidak diterapkan | Fani |
| 6 | Pemeriksaan otomatis kepatuhan RPO di Daftar Job dan tanggal kedaluwarsa retensi (kolom F sudah memuat retensi dalam hari) | Tidak diterapkan | Fani |
| 7 | Kapasitas baris dibanding masa simpan 3 tahun: Backup Log hanya sampai baris 606 (602 baris, satu baris per job per pemeriksaan), Restore Record sampai baris 155, dan rumus Ringkasan be

### Open items
1. Tanggal draft "13 Oktober 2026" (Kontrol Dokumen!B7) dan tanggal baris riwayat revisi (B30) dipertahankan dari sumber. Saya tidak menulis tanggal baru, dan tanggal efektif tetap "Ditetapkan saat pengesahan". Owner memutus apakah tanggal draft diganti tanggal draft revisi ini.
2. Sheet Kontrol Dokumen tidak punya baris Status terpisah; "00 (DRAFT)" di B6 memuat Revisi dan Status sekaligus dan dipertahankan. Menambah baris butuh perubahan tata letak yang tidak bisa dilakukan patch.
3. GAP alat (kosmetik): clear_rows pada baris legenda 25 menyalin warna dari baris 26, sehingga sel A25 kini abu-abu tanpa label, di atas "Sel rumus: jangan diubah" yang juga abu-abu. Biru muda (E7EEF7) tidak dipakai lagi di workbook. Fungsi form tidak berubah. Perbaikannya di tools/xlsx_patch.py atau lewat LEAD; di luar batas tulis saya. Belum dilihat di Excel; hanya konversi LibreOffice yang berhasil.
4. Ringkasan!B3 berisi 1 November 2026. Itu sel pilihan bulan, bukan baris bertanda CONTOH, dan semua rumus Ringkasan bergantung padanya, jadi dipertahankan. Tanggalnya jatuh sesudah tanggal draft; pengguna menggantinya tiap bulan. Pemilik dokumen memutus apakah nilai awalnya perlu diganti.
5. SOP-03 butir 7.3.3 menyebut "sheet Restore Test dan Request", sedangkan sheet di form ini "Restore Record". Perlu penyelarasan di SOP-03 (lane ISMS-SOP-03); nama sheet di form tidak saya ubah karena rumus Ringkasan merujuknya.
6. Jenis restore di Daftar!E2:E4 ada tiga ("Uji berkala", "Permintaan pelanggan", "Pemulihan insiden"), sedangkan Tujuan (B15) dan Cara pakai butir 3 hanya menyebut uji berkala dan permintaan. Teks tim dipertahankan; pemilik dokumen memutus apakah pemulihan insiden ikut disebut.
7. Dropdown Shift berisi Shift 1, Shift 2, Shift 3, sedangkan Cara pakai menyebut shift malam. Baris co

## SNX-ISMS-FRM-02 Security Incident Investigation Records
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-FRM-02 Security Incident Investigation Records (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-FRM-02_Security_Incident_Investigation_Records.xlsx (1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2, modifiedTime 2026-10-13T06:09:30Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Notifikasi PDP: bila data pribadi terlibat, kolom menandai kajian dengan batas 3 x 24 jam dari waktu deteksi; keputusan ada di COO dan Legal | Kontrol Dokumen B20: "Bila data pribadi terlibat, kolom Notifikasi PDP otomatis menandai kewajiban pemberitahuan maksimal 3 x 24 jam (keputusan COO dan Legal)." Register P5: `=IF(J5="Ya","WAJIB DIKAJI, maksimal "&TEXT(B5+3,"dd-mmm hh:mm"),IF(J5="","","Tidak"))` | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |
| 2 | Insiden P1 dan P2 memakai lembar investigasi per insiden; setiap bukti dicatat di Chain of Custody dengan hash SHA-256 yang diverifikasi tiap perpindahan | Kontrol Dokumen B21: "Untuk insiden P1 dan P2, salin sheet Investigasi per insiden dan isi Chain of Custody untuk setiap bukti." Chain of Custody A2: "Satu baris per perpindahan atau tindakan atas bukti. Hash SHA-256 dihitung saat pengumpulan dan diverifikasi setiap perpindahan." | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |
| 3 | Pemilik dokumen Lead SOC; masa simpan 5 tahun; acuan ISO 9001 klausul 10.2 dan Annex A 5.25 sampai 5.28 | Kontrol Dokumen B10: "Lead SOC"; B14: "5 tahun"; B12: "Klausul 10.2"; B13: "Klausul atau kontrol Annex A 5.25, 5.26, 5.27, 5.28" | 1ILWYIkwaqe3SkpTsEPzY_IB-HMqCqui2 |

Fakta lain dari berkas yang sama: Kontrol Dokumen B15 "Register insiden keamanan informasi, catatan investigasi, dan chain of custody bukti sesuai SNX-ISMS-SOP-01."; B9 "RESTRICTED (Internal)"; Register N5 `=IF(OR(B5="",L5=""),"",ROUND((L5-B5)*24,1))` dan O5 `=IF(OR(B5="",M5=""),"",ROUND((M5-B5)*24,1))`; Daftar kolom B "P1", "P2", "P3", "P4"; Register A4 "ID insiden" dengan Cara pakai B18 "nomor SIR-YYYY-NNN". Rujukan severity di audit SOP-01 (DATA): "2. Event yang terkonfirmasi menjadi insiden dan diberi severity:" d

### USULAN
| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: Samuel Kristanto Utomo / President Director (default D2) menggantikan "COO, Amirull Yusuf Zulkarnain" di Kontrol Dokumen B11 dan B38. Defaults memberi pembalik "form operasional disetujui COO bila owner memutuskan". | owner |
| 2 | Disusun oleh Erik Dwi Yanto / Technical/Operation Engineer L1 dan Diperiksa oleh Fani Fatullah / VP Tech Operation and Services (defaults) menggantikan "Lead SOC" dan "ISO/ISMS Coordinator" di B36 dan B37. | owner |
| 3 | Kalimat B15 yang menunjuk SNX-ISMS-SOP-01 sebagai tempat definisi severity P1 sampai P4. Dasarnya salinan audit SOP-01 (Bagian 8 butir 2); SOP-01 belum punya spec di repo ini dan belum dibaca langsung dari Drive. | Fani |
| 4 | Kalimat B20 yang menulis "menandai wajib dikaji" dan "dari waktu deteksi" menggantikan "menandai kewajiban pemberitahuan". Isinya hanya menjelaskan rumus P, tetapi kalimatnya tambahan penyusun. | Legal |
| 5 | Kalimat B19 yang menyebut hasil jam dibulatkan 1 desimal. Isinya menjelaskan ROUND(...,1) yang sudah ada. | Fani |
| 6 | B22 tanpa nama SKILL_ dan tanpa nomor dokumen: "format laporan insiden baku". Perlu nomor SNX atau lokasi format laporan insiden untuk pelanggan. | Fani |
| 7 | Baris riwayat revisi kedua (rev 00 tanggal sama, frasa RTO) dikosongkan dan C31 memakai "Draft awal untuk review dan pengesahan". | Fani |
| 8 | Titik awal batas 3 x 24 jam: form menghitung dari waktu deteksi, SOP-01 Bagian 11 butir 2 menulis "paling lambat 3 x 24 jam sejak diketahui". Tidak diterapkan di rumus. | Legal |
| 9 | Kolom waktu pemberitahuan aktual ke lembaga berwenang dan ke subjek data di Register (sekarang hanya "Tgl info pelanggan"). Tidak diterapkan di berkas. | Legal |
| 10 | Target waktu pulih insiden keamanan (RTO). Tidak

### Open items
| # | Butir | Pemutus / pemilik |
|---|---|---|
| 1 | Gambar "Alur Proses" memakai sebutan "COO dan Legal" pada kotak Kaji notifikasi PDP, tanpa bentuk "Direktur (COO)". Alat patch tidak mengedit gambar; gambar harus dibuat ulang bila sebutannya mau diseragamkan. | LEAD ISO / owner |
| 2 | Efek samping clear_rows pada legenda warna: baris 26 dikosongkan, tetapi kotak warna A26 berubah mengikuti kotak A27 (abu-abu), sehingga ada dua kotak abu-abu bersebelahan dengan satu label "Sel rumus: jangan diubah". Kosmetik; alat patch tidak bisa menghapus warna tanpa meniru baris bawahnya. | LEAD ISO (tech_fix xlsx_patch) |
| 3 | Alat patch tidak mengubah tinggi baris. Teks B15, B19, B20 dipendekkan agar muat dalam tinggi baris yang ada (dicek dengan render soffice). | LEAD ISO |
| 4 | Format laporan insiden untuk pelanggan tidak punya nomor SNX dan isinya tidak ada di korpus (sumber menyebutnya "format beku"). Lihat USULAN 6. | Fani |
| 5 | Peran tanpa pemegang: Lead SOC (K-10), ISMS Coordinator (K-13). "Incident Commander" tidak ada di HR-ORG-01. | owner |
| 6 | SNX-ISMS-SOP-01 belum punya spec di repo ini. Verifikator perlu mencocokkan pointer severity di B15 dengan SOP-01 hasil draf W2. | LEAD ISO |
| 7 | Tanggal draft 13 Oktober 2026 dipertahankan dari sumber; tanggal efektif dan tanda tangan kosong sampai pengesahan. | owner |
| 8 | Masa simpan 5 tahun berbeda dari beberapa dokumen ISMS dan Ops lain; tidak diubah. Penyeragaman masa simpan antardokumen belum diputus. | Fani |
| 9 | Dasar hukum PDP tidak disebut di form (UU PDP disebut di SOP-01 menurut audit). Tidak ditambahkan karena sumber form diam. Lihat USULAN 8 dan 9. | Legal |

## SNX-ISMS-FRM-03 Supplier Technical Security Evaluation
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 0; OOXML: -
- Berkas: out/08_ISMS/SNX-ISMS-FRM-03 Supplier Technical Security Evaluation (Rev00 DRAFT).xlsx
- Sumber: SNX-ISMS-FRM-03_Supplier_Technical_Security_Evaluation.xlsx (1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg, modifiedTime 2026-10-13T06:09:33Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Supplier kritikalitas Tinggi dievaluasi setiap semester, Sedang dan Rendah setiap tahun; tanggal evaluasi berikutnya dihitung rumus dari tanggal evaluasi terakhir | Kontrol Dokumen B19: "Evaluasi supplier kritikal Tinggi setiap semester, Sedang dan Rendah setiap tahun; jadwal berikutnya dihitung otomatis." Daftar Supplier K5: `=IF(J5="","Belum pernah",EDATE(J5,IF(E5="Tinggi",6,12)))` | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |
| 2 | Nilai evaluasi = rata-rata tertimbang enam kriteria berbobot 25, 15, 25, 15, 10, 10 persen, dikali 20; ambang 80 dan 60 menentukan keputusan | Evaluasi A2: "Nilai = rata-rata tertimbang dikali 20 (skala 0 sampai 100). 80 ke atas Disetujui · 60 sampai 79 Disetujui bersyarat · di bawah 60 Tinjau ulang." Evaluasi J5: `=IF(COUNT(D5:I5)<6,"",ROUND(SUMPRODUCT(D5:I5,$D$3:$I$3)/SUM($D$3:$I$3)*20,0))`. Bobot D3 sampai I3: 0.25, 0.15, 0.25, 0.15, 0.1, 0.1 | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |
| 3 | Daftar berisi 8 supplier (SUP-001 sampai SUP-008) yang status kontrak, NDA, dan sertifikasinya wajib diverifikasi dengan Commercial dan Legal; klausul keamanan di kontrak dan NDA masih "Belum diketahui" untuk 8 dari 8 | Daftar Supplier A2: "Baris biru muda = supplier yang teridentifikasi di knowledge base; status kontrak, NDA, dan sertifikasi wajib diverifikasi dengan Commercial dan Legal." H5 sampai H12: "Belum diketahui". Kontrol Dokumen B14: "Durasi kontrak + 3 tahun" (masa simpan record) | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |

### USULAN
Label (USULAN) hanya ditulis di sel xlsx untuk langkah verifikasi nama penyedia (Daftar Supplier A2); butir lain di bawah berada di notes ini karena tidak ada angka atau fakta baru yang masuk sel.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain di blok Disusun, Diperiksa, dan Disetujui. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Langkah verifikasi nama penyedia SUP-001, SUP-002, dan SUP-006 dengan Commercial dan Legal. Sumber hanya meminta verifikasi kontrak, NDA, dan sertifikasi | Daftar Supplier A2 | Fani |
| 4 | Pertahankan rumus Evaluasi J dan koreksi teks skala menjadi 20 sampai 100 (diterapkan), atau ubah rumus supaya skor 1 menghasilkan 0. Belum ada keputusan, hanya teks yang disesuaikan dengan rumus | Evaluasi A2 dan J5 sampai J104 | Fani |
| 5 | Rumus nilai (J) dan keputusan (K) hanya terisi bila C bukan "ID tidak ada", supaya ID salah ketik tidak menghasilkan keputusan Disetujui. Belum diterapkan | Evaluasi J5 sampai K104 | Fani |
| 6 | Tambah rujukan ke ID aset di SNX-ISMS-REG-01 dan ke ID risiko di SNX-ISMS-REG-02 (misalnya SUP-001 ke ISR-005) pada Daftar Supplier. Dibuat sesudah REG-01 diisi ulang oleh Ops, karena ID bisa berubah. Belum diterapkan | Daftar Supplier, kolom baru | Fani |
| 7 | Tetapkan batas waktu dan pemilik tindak lanjut untuk keputusan "Disetujui bersyarat" dan

### Open items
| # | Open item | Untuk |
|---|---|---|
| 1 | Belum ada evaluasi supplier: Evaluasi terakhir kosong untuk 8 supplier, sheet Evaluasi dan Kuesioner kosong. Siklus evaluasi pertama belum dijadwalkan di sumber; bukti penerapan A 5.19 sampai 5.23 dan klausul 8.4 baru ada sesudah siklus itu berjalan | Fani |
| 2 | Kontrak dan NDA memuat klausul keamanan: "Belum diketahui" untuk 8 dari 8; sertifikasi keamanan "Belum diketahui" untuk SUP-001, 002, 003, 006, 007. Tiga nilai "Ya" (SUP-004, 005, 008) tidak punya bukti, masa berlaku, atau ruang lingkup sertifikat di form; bukti hanya ada di Kuesioner butir 1 yang kosong. Verifikasi menunggu Commercial dan Legal | Commercial, Legal, Fani |
| 3 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Cabang "Disetujui bersyarat" (60 sampai 79) tidak ada; jalur "tidak" dari "Nilai di bawah 60?" langsung ke Disetujui; kotak "Tinjau ulang" tidak punya panah lanjutan. Legenda A2 sudah diberi catatan; bila gambar diperbarui, catatan itu ditinjau | Orkestrator, Fani |
| 4 | Nama penyedia SUP-001 ("Maxcloud atau Awandata"), SUP-002 ("Arktech"), SUP-006 ("Antmedia") belum pasti; sumber dan audit tidak menentukannya. Nama tetap seperti sumber | Commercial, Legal |
| 5 | Tidak ada batas waktu dan pemilik tindak lanjut untuk "Disetujui bersyarat" dan "Tinjau ulang"; kolom Tindak lanjut bebas isi tanpa validasi. Lihat USULAN 7 | Fani |
| 6 | Tidak ada rujukan antara FRM-03 dan SNX-ISMS-REG-01 (aset) atau SNX-ISMS-REG-02 (ISR-005). Lihat USULAN 6 | Fani, lane ISMS-REG-01 dan ISMS-REG-02 |
| 7 | Tidak ada kolom klasifikasi data yang dipegang supplier (SUP-008 berpadanan dengan aset berklasifikasi RESTRICTED di REG-01 menurut audit). Menambah kolom mengubah struktur form | Fani |
| 8 | SNX-ISMS-PLN-01 menunjuk FRM-03 untuk kontak eskalasi dan renc
