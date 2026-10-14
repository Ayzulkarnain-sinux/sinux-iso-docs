# Catatan penyusun ISMS-REG-03: Information Security Risk Treatment Plan

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-REG-03.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-ISMS-REG-03 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C2. Process owner = "ISMS Coordinator" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-REG-03.xlsx specs/ISMS-REG-03.patch.json /tmp/pen-ISMS-REG-03/out.xlsx` memberi `"pass": true`, `"fails": []`.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-REG-03_IS_Risk_Treatment_Plan.xlsx (126916 byte) | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ | 2026-10-13T06:09:40Z (get_file_metadata, dicek hari ini, sama dengan data baris; fileSize 126916 sama dengan hasil dekode) | read_file_content (teks), download_file_content dengan exportMimeType xlsx (didekode ke /tmp/src/ISMS-REG-03.xlsx; kerja di /tmp/pen-ISMS-REG-03/), 4 sheet dibuka dengan python3 -I + openpyxl (nilai, rumus, warna isi, data validation, conditional formatting), gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/worklist.json dan config/checklist.json baris 81 | Description hanya nama berkas | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "6.1" dan ISO/IEC 27001:2022 "6.1.3, 8.3" (sama dengan B12 dan B13 sumber) |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md baris 1517 sampai 1714 (bagian 5 Catatan kualitas dan celah di baris 1703 sampai 1711) | salinan audit 13 sampai 14 Okt | DATA; tiap butir dicocokkan ulang ke berkas xlsx |
| Pendukung (lane lain) | notes/ISMS-REG-02.md, notes/ISMS-REG-01.md, specs/ISMS-REG-02.patch.json, specs/HR-ORG-01.json, config/defaults.json | repo ini | Dibaca untuk konsistensi lintas dokumen; tidak ditulis ulang. Isinya bisa basi bila tim sudah mengubah dokumen itu di Drive |

Empat sheet di sumber: Kontrol Dokumen (A1:E38), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:C6), Rencana Penanganan (A1:R59, header baris 4, data baris 5 sampai 19, rumus N dan O sampai baris 59). Sheet "Kontrol Dokumen" ada, jadi patch memakai `set`; tidak ada sheet yang ditambah.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Target tanggal dan nilai residual di 15 baris adalah usulan, ditetapkan bersama pemilik risiko | Rencana Penanganan!A2: "Target tanggal dan residual adalah usulan; ditetapkan bersama pemilik risiko." | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |
| 2 | Skor residual = L x I; level dihitung otomatis dengan ambang 5, 10, 20 | Rencana Penanganan!N5: `=IF(OR(L5="",M5=""),"",L5*M5)`; O5: `=IF(N5="","",IF(N5>=20,"Kritis",IF(N5>=10,"Tinggi",IF(N5>=5,"Sedang","Rendah"))))` | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |
| 3 | Risiko residual harus diterima pemilik risiko secara tertulis; kolom penerimaan masih kosong di 15 baris | Kontrol Dokumen!B20: "Risiko residual harus diterima pemilik risiko secara tertulis (kolom Diterima oleh dan Tanggal penerimaan)." | 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ |

Fakta pendukung yang tidak diubah: B10 "ISMS Coordinator" (Pemilik dokumen); B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B14 "Berlaku sampai digantikan"; B22 "Usulan awal Divisi Operation dari riwayat operasi di knowledge base SINUX; wajib divalidasi ISMS Coordinator dan pemilik risiko." Pengukuran atas out.xlsx (LibreOffice xlsx ke xlsx, dibaca data_only, dibandingkan dengan hitungan python L x I): 15 baris RTP-001 sampai RTP-015, level residual Tinggi 2 (RTP-002 skor 12, RTP-005 skor 10), Sedang 11, Rendah 2 (RTP-008 skor 3, RTP-015 skor 4), nol sel galat; Opsi semua Mitigasi; Status semua Belum mulai; target 2027-03-31 sebanyak 11 dan 2027-06-30 sebanyak 4; pemilik Head of Operation 6, Lead SOC 3, Lead NOC 3, Tech dan Product 1, Service Delivery Manager 1, ISMS Coordinator 1. Kolom I, P, Q, R kosong di baris 5 sampai 19 (dicek langsung). Ambang rumus sama dengan Matriks Risiko REG-02 yang dikutip di notes/ISMS-REG-02.md: "Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25".

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (python3 -I + openpyxl): 17 sel berubah, selain itu tidak ada sel yang berubah. Tidak ada clear_rows (lihat Asumsi dan tafsir butir 1).

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari data baris; penulisan sama dengan 7 patch lain, termasuk REG-02 |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by dan data baris. USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 6.1.3, 8.3" | "Klausul 6.1.3, 8.3" | 6.1.3 dan 8.3 adalah klausul badan standar (penanganan risiko), bukan kontrol Annex A; "klausul atau kontrol" ragu-ragu. Angka sama dengan acuan baris |
| B19 Cara pakai butir 2 | "Isi L dan I residual setelah tindakan selesai; level residual dihitung otomatis." | "L dan I residual berisi usulan; ubah setelah tindakan selesai. Level otomatis." | Butir lama bertentangan dengan 15 baris yang sudah berisi L dan I padahal Status "Belum mulai". Fakta usulan dari A2 Rencana Penanganan. Panjang dijaga di bawah 80 karakter karena tinggi baris 19 hanya satu baris. USULAN 7 |
| B20 Cara pakai butir 3 | "... (kolom Diterima oleh dan Tanggal penerimaan)." | "... (kolom Diterima oleh dan Tgl penerimaan)." | Header kolom Q berbunyi "Tgl penerimaan", bukan "Tanggal penerimaan" |
| B26 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: usulan awal Divisi Operation, belum divalidasi" | Warna E7EEF7 di A26 sama dengan warna baris 5 sampai 19. Baris itu usulan awal (A2 dan B22 sumber), bukan CONTOH, jadi legenda lama menyuruh menghapus data tim. Rumusan sejalan dengan B26 REG-02 |
| C31 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari data baris |
| A32 sampai E32 | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; kata RTO hanya muncul di C32 (pencarian semua sheet), tidak ada di isi workbook. USULAN 2 |
| B36, B37, B38 | "ISMS Coordinator", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari data baris dan defaults.json. Sumber memakai dua penamaan untuk penyusun dan pemeriksa; kini tiga penanda tangan berbeda. USULAN 1 |
| Alur Proses A2 | "Kotak biru = output akhir · kotak oranye = cabang ke tindakan atau prosedur lain · garis putus-putus = kembali ke alur utama" | Dua klausa pertama saja | image1.png dibuka: satu kotak biru (Penerimaan tertulis), satu kotak oranye (Tindakan tambahan), semua garis penuh; tidak ada garis putus-putus. Gambar tidak bisa diubah alat (Open item 3) |
| Rencana Penanganan A2 | "Target tanggal dan residual adalah usulan; ditetapkan bersama pemilik risiko." | Kalimat sama ditambah "Status vault (RTP-001, RTP-010): menunggu konfirmasi Ops." | Aturan vault di defaults.json: tiap penyebutan vault membawa status "menunggu konfirmasi Ops". Vault disebut di F5 dan F14; tinggi baris 5 (23.85) tidak muat tambahan di sel, jadi status ditulis sekali di catatan sheet dan menyebut baris yang terkena. Open item 2 |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber |
| Tidak diubah | | | Tanda tangan dan tanggal (C36 sampai D38) kosong (batas keras 3). B7 tanggal draft tim dan B8 bukan tanggal efektif. 15 baris RTP, sheet Daftar, rumus N dan O, data validation, conditional formatting, gambar, Cara pakai butir 1, 4, 5, legenda input dan rumus. Tidak ada label (USULAN) di sel karena tidak ada angka atau fakta baru yang masuk sel; semua USULAN ada di notes ini |

Render PDF LibreOffice atas out.xlsx (5 halaman): Kontrol Dokumen terbaca utuh, B19 satu baris, B26 satu baris, Riwayat revisi hanya satu baris terisi, Pengesahan memuat tiga nama; Rencana Penanganan A2 terbaca satu baris. Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas semua sel teks out.xlsx: nol temuan. Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter). Sumber punya satu temuan, "CONTOH" di B26, sudah diganti.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Semua target tanggal dan residual berlabel usulan, tidak ada yang final | Tidak diubah: status final adalah keputusan pemilik risiko, bukan penyusun (batas keras 3). A2 sheet dan legenda B26 kini menyatakan statusnya. USULAN 7 |
| 2 | L dan I residual terisi walau semua status "Belum mulai"; Cara pakai butir 2 menyuruh mengisi setelah tindakan selesai | Diperbaiki di B19 (nilai sekarang disebut usulan, diubah setelah tindakan selesai). Nilai L dan I tidak diubah. USULAN 7 |
| 3 | Kolom I, P, Q, R kosong di 15 baris; penerimaan tertulis belum ada | Tidak diisi: biaya, nama penerima, tanggal, dan bukti adalah data faktual tanpa sumber. Tidak ada angka diusulkan. Open item 4 |
| 4 | RTP-002 (awal Kritis, residual 12 Tinggi) dan RTP-005 (residual 10 Tinggi) tidak punya baris lanjutan; siapa yang menerima residual risiko awal Kritis tidak dinyatakan (REG-02 B24 menyebut COO) | Tidak bisa diperbaiki tanpa mengarang aturan. USULAN 3 dan 6, Open item 5 |
| 5 | Semua 15 risiko memakai opsi Mitigasi; Hindari, Transfer, Terima tidak terpakai | Bukan cacat isi, tidak diubah. Menambah opsi lain berarti mengarang keputusan. Open item 9 |
| 6 | Rujukan SNX-ISMS-SOP-05, PLN-01, FRM-01, REG-04, PRO-01 | Kelimanya ada di config/checklist.json (baris 89, 91, 87, 85, 79) dengan judul yang sejalan: Vulnerability & Patch Management, Business Continuity / IT Recovery Plan, Backup Log & Restore Testing Records, User Access Register & Periodic Access Review, Information Classification & Handling Procedure. Tidak diubah. Satu ketidakselarasan pelaku dicatat di Open item 6 |
| 7 | Pengesahan kosong; status "Menunggu"; revisi 00 dua kali | Baris kedua dikosongkan (USULAN 2). Tiga penanda tangan diisi dari defaults.json; tanda tangan dan tanggal dibiarkan kosong. "Menunggu" di E31 dipertahankan |
| 8 | Kolom C "Risiko" menggabungkan ancaman dan aset ("Ancaman: aset"); tidak ada kolom vulnerability | Tidak diubah: menambah kolom di luar kemampuan alat, dan mengganti judul kolom memutus kesejajaran dengan REG-02. Vulnerability ada di REG-02 dan terhubung lewat kolom Ref risiko. Open item 10 |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B13 "Klausul atau kontrol Annex A 6.1.3, 8.3" | Diganti "Klausul 6.1.3, 8.3" |
| B | Legenda B26 menyebut baris CONTOH padahal baris biru adalah usulan awal | Ditulis ulang sesuai isi |
| C | Legenda Alur Proses A2 menyebut garis putus-putus yang tidak ada di gambar | Klausa dihapus |
| D | Cara pakai butir 3 menyebut "Tanggal penerimaan", header kolom "Tgl penerimaan" | Disamakan dengan header |
| E | Vault disebut di F5 dan F14 tanpa status | Status ditulis sekali di Rencana Penanganan A2 |
| F | Aturan lintas dokumen yang tidak berlaku di sini: PPN (tidak ada), kunci backup dengan salinan offline atau break-glass (RTP-006 dan RTP-014 hanya menyebut uji restore dan backup immutable, tanpa kunci), rujukan internal AI (tidak ada, dicek dengan pola lint), GLPI dan Zammad (tidak disebut; "ticketing system" di C12, USULAN 5), sebutan COO (hilang bersama B11 dan B38, jadi "Direktur (COO)" tidak terpakai) | Tidak ada perubahan |

## USULAN

Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan ISMS Coordinator, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Pilih satu rumusan penerimaan residual: pemilik risiko menerima secara tertulis (Cara pakai butir 3 dan gambar), atau risiko yang awalnya Kritis (RTP-002) diterima COO secara tertulis mengikuti Matriks Risiko B24 REG-02. Sama dengan USULAN 3 di notes/ISMS-REG-02.md. Belum diterapkan | Kontrol Dokumen B20; Alur Proses; REG-02 Matriks B24 | owner (Amirull sebagai COO) |
| 4 | Ganti pemilik RTP-007 "Tech dan Product" (nama fungsi) dengan "Manager of Product Tech" (JA-05 di Struktur Organisasi, jabatan terdekat), serentak di REG-01, REG-02 K11, dan REG-03 H11 supaya tiga dokumen sama. Belum diterapkan karena REG-01 dan REG-02 masih memakai nama lama. Bila disetujui, tambahkan satu baris di patch: `"Rencana Penanganan!H11": "Manager of Product Tech"` | Rencana Penanganan H11 | Fani |
| 5 | Sebut sistem tiket pada risiko ISR-008 (RTP-008): Zammad untuk tiket Ops, atau Zammad dan GLPI. Sumber menulis "ticketing system" tanpa nama; batas "generalist" untuk GLPI belum dirinci owner. Belum diterapkan, sejajar dengan USULAN 6 di notes/ISMS-REG-02.md | Rencana Penanganan C12 | owner |
| 6 | Untuk residual Tinggi (RTP-002 skor 12, RTP-005 skor 10): tambah baris RTP lanjutan dengan tenggat, atau catat penerimaan tertulis di kolom P dan Q. Tidak diterapkan karena butuh tindakan dan tanggal baru yang tidak ada di sumber | Rencana Penanganan baris 6 dan 9 | Fani |
| 7 | Tafsir bahwa L dan I residual yang terisi adalah proyeksi (usulan), bukan nilai sesudah tindakan. Dasarnya A2 sheet dan catatan audit, bukan pernyataan eksplisit tim. Diterapkan di B19 dan B26 | Kontrol Dokumen B19, B26 | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Kode yang dirujuk di sel: SNX-ISMS-REG-02, SNX-ISMS-SOA-01, SNX-ISMS-SOP-05, SNX-ISMS-PLN-01, SNX-ISMS-FRM-01, SNX-ISMS-REG-04, SNX-ISMS-PRO-01; semua ada di config/checklist.json (baris 80, 82, 89, 91, 87, 85, 79). Pengecualian lingkup (risiko Rendah tidak masuk rencana) tersirat di gambar ("Risiko Sedang ke atas dari SNX-ISMS-REG-02") dan di kutipan REG-02 B20 pada notes/ISMS-REG-02.md ("level Rendah dapat diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03."), tetapi tidak tertulis di Kontrol Dokumen REG-03. Lokasi simpan dan pemilik rekaman tidak ada di sumber. Masa simpan "Berlaku sampai digantikan" dipertahankan; tidak ada masa simpan untuk bukti penerimaan risiko tertulis, dan angka tidak diusulkan karena tidak ada dasar | Orkestrator, Fani |
| 2 | Vault: RTP-001 menulis "migrasi ... ke vault" dan RTP-010 "kredensial hanya melalui vault". Di REG-01 sumber vault berstatus "Aktif", di REG-02 sumber "belum live" (CONTEXT-PACK butir 6). Kondisi hari ini tidak terukur. Sampai Ops mengonfirmasi, status "menunggu konfirmasi Ops" ditulis di A2 sheet Rencana Penanganan | Ops (Fani) |
| 3 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Panah "tidak" menuju "Tindakan tambahan, kembali ke opsi" tidak punya garis kembali. Gambar juga tidak menunjukkan jalur penerimaan risiko Kritis oleh COO (lihat USULAN 3). Legenda A2 sudah disesuaikan; bila gambar diperbarui, legenda ikut ditinjau | Orkestrator, Fani |
| 4 | Kolom I (Sumber daya atau biaya), P (Diterima oleh), Q (Tgl penerimaan), R (Bukti penyelesaian) kosong di 15 baris. Biaya, nama penerima, tanggal, dan bukti tidak ada di sumber, jadi dibiarkan kosong tanpa angka usulan | Ops (Fani), pemilik risiko |
| 5 | Siapa yang menerima residual RTP-002 dan RTP-005 (keduanya Tinggi) belum diatur: REG-02 B24 menyebut COO hanya untuk level Kritis, REG-03 menyebut pemilik risiko, dan tidak ada baris lanjutan. Lihat USULAN 3 dan 6 | owner, Fani |
| 6 | Pelaku advisory mingguan berbeda: RTP-003 berpemilik Lead NOC dan merujuk SNX-ISMS-SOP-05, sedangkan catatan audit mengutip SOP-05 Bagian 5 "Lead SOC menelaah sumber tersebut minimal mingguan". SOP-05 belum disusun di run ini (W2). Cocokkan pemilik RTP-003 atau bunyi SOP-05 saat SOP-05 selesai | Fani |
| 7 | Cara pakai butir 1 menulis "Satu baris per tindakan penanganan", sedangkan tiap baris RTP memuat dua sampai empat tindakan dan 15 RTP dipetakan satu-satu ke 15 ISR. Tidak diubah (T1, suara tim). Perlu diputus apakah satu risiko boleh punya beberapa baris RTP | Fani |
| 8 | "knowledge base SINUX" di Cara pakai butir 5 dipertahankan, sama dengan keputusan REG-02 (Open item 10 di notes/ISMS-REG-02.md). Bila konsultan menganggapnya rujukan internal AI, ganti serentak di REG-02 dan REG-03 dengan nama sistem yang disetujui Ops | Fani |
| 9 | Seluruh 15 RTP memakai opsi Mitigasi; Hindari, Transfer, Terima ada di dropdown tetapi tidak terpakai. Auditor kemungkinan menanyakan dasar pilihan itu | Fani |
| 10 | Kolom C "Risiko" memakai format "Ancaman: aset"; kolom vulnerability tidak ada di REG-03 (ada di REG-02). Tidak diubah | Fani |
| 11 | Peran pemilik: Head of Operation, Lead SOC, Lead NOC, Service Delivery Manager, dan ISMS Coordinator ada sebagai nama peran di specs/HR-ORG-01.json. Struktur Organisasi menandai Lead NOC dan Lead SOC belum punya pemegang (K-10) dan ISMS Coordinator belum ditetapkan (K-13), sehingga "pemilik risiko" yang harus menerima residual belum bisa dipetakan ke orang. "Tech dan Product" tidak ada di sana (USULAN 4) | owner, Fani |
| 12 | Tanggal draft 13 Oktober 2026 (B7, B31) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan". Target 31 Maret 2027 dan 30 Juni 2027 berlabel usulan di sumber | owner |
| 13 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: "hapus atau timpa saat dipakai" (B26), "jangan diubah" (B27), Cara pakai butir 1 sampai 5. Tidak ada yang dijalankan sebagai instruksi: baris biru tidak dihapus, rumus tidak diubah. B26 ditulis ulang atas dasar audit dan RUNBOOK, bukan karena kalimatnya | Orkestrator |
| 14 | Keterbatasan alat: nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka; tinggi baris tidak diubah, jadi baris 32 yang dikosongkan tetap setinggi 57.45. HUMAN-VERDICT: buka di Excel dan lihat apakah B19, B26, dan A2 sheet Rencana Penanganan tidak terpotong; di render LibreOffice semuanya terbaca | Orkestrator, owner |

## Asumsi dan tafsir

1. Tidak ada clear_rows. Tugas memerintahkan clear_rows untuk baris CONTOH, contoh, atau data dummy. Di sheet data tidak ada kata CONTOH (xlsx_patch tidak menemukan satu pun). 15 baris biru muda adalah usulan awal Divisi Operation (B22 dan A2 sumber), berisi fakta SINUX (Nusagrid, AegisWAF, fleet WHM, SNX-ISMS-SOP-05), dan dipetakan satu-satu ke ISR-001 sampai ISR-015 di REG-02. RUNBOOK §6 menyuruh mempertahankan substansi tim. Bila LEAD menilai baris itu data dummy, perubahannya satu baris di patch: `"clear_rows": {"Rencana Penanganan": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`; akibatnya REG-03 kosong dan rujukan RTP dari REG-02 tidak punya isi. Saya tidak melakukannya. Keputusan sama dengan REG-02.
2. "Approval persis" dari tugas mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json.
3. Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
4. Sebutan COO: setelah B11 dan B38 diganti, workbook tidak menyebut COO lagi (pencarian semua sheet, nol kemunculan), jadi aturan "Direktur (COO)" tidak terpakai. Direktur Utama hanya muncul di blok pengesahan sebagai "President Director".
5. Acuan klausul: B12 "Klausul 6.1" dan B13 "Klausul 6.1.3, 8.3" memuat angka persis dari tugas. Kolom G sheet Rencana Penanganan ("Kontrol Annex A") memakai nomor Annex A dan tidak diubah; 8.2 di RTP-009 adalah kontrol hak akses istimewa, bukan klausul penilaian risiko.
6. Pemilik dokumen "ISMS Coordinator" tetap meski penyusun di blok Pengesahan adalah Erik Dwi Yanto: sumber memisahkan keduanya, dan tugas memerintahkan process_owner mengikuti "Pemilik dokumen" sumber.
7. Pemetaan peran sumber ke Struktur Organisasi: lima dari enam nama pemilik di kolom H sudah sama dengan nama peran di HR-ORG-01. Yang keenam, "Tech dan Product", tidak diganti karena REG-01 dan REG-02 masih memakainya dan tiga dokumen harus sama (USULAN 4 menyebut jabatan terdekat).
8. Isi dari lane lain (REG-01, REG-02, HR-ORG-01, SOP-05) dibaca dari repo dan salinan audit, bukan dari Drive terbaru; kutipannya bisa basi bila tim sudah mengubah dokumen itu.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI? Pemeriksaan atas 6 nilai sel berisi teks yang saya tulis atau ubah (B19, B20, B26, C31, Rencana Penanganan A2, Alur Proses A2) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Draf awal B19 "L dan I residual saat ini usulan; tetapkan setelah tindakan selesai. Level dihitung otomatis." (92 karakter) terbaca wajar tetapi pecah jadi dua baris dan terpotong di tinggi baris 15 pada render | Diperpendek jadi "L dan I residual berisi usulan; ubah setelah tindakan selesai. Level otomatis." (78 karakter). "Level otomatis" terbaca telegrafis; dipertahankan karena gaya yang sama dengan butir tim lain dan satu fakta per kalimat |
| Kalimat vault di A2 "Status vault (RTP-001, RTP-010): menunggu konfirmasi Ops." bisa terbaca seperti catatan kaki birokratis | Dipertahankan: menyebut baris yang terkena dan satu status, tanpa kata penegas. Rumusan status diwajibkan aturan vault |
| Legenda B26 "Biru muda: usulan awal Divisi Operation, belum divalidasi" | Dipertahankan: rumusan satu klausa, kata "usulan awal" dan "Divisi Operation" dari B22 sumber |
| Notes ini panjang dan memakai banyak tabel | Dipertahankan: format notes diminta tugas; tiap sel tabel membawa fakta atau keputusan yang berbeda dan tidak ada ringkasan penutup |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust), kelompok tiga yang dipaksakan, ekor penegas | Tidak ada di nilai patch (pencarian karakter dan pola lint). Notes ini tidak memakai em-dash, en-dash, atau tebal |

Adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.ISMS dan approved_by; sama dengan data baris |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di data baris dan defaults.json |
| "Klausul 6.1" dan "Klausul 6.1.3, 8.3" | Data baris (acuan klausul); B12 dan B13 sumber |
| "L dan I residual berisi usulan; ubah setelah tindakan selesai. Level otomatis." | "Isi L dan I residual setelah tindakan selesai; level residual dihitung otomatis." (B19 sumber) dan A2 Rencana Penanganan ("residual adalah usulan"); tidak ada angka |
| "Tgl penerimaan" | Header Q4 sumber |
| "Biru muda: usulan awal Divisi Operation, belum divalidasi" | B22 Kontrol Dokumen sumber ("Usulan awal Divisi Operation ... wajib divalidasi"), warna E7EEF7 dari A26 dan baris 5 sampai 19 |
| "menunggu konfirmasi Ops" dan "RTP-001, RTP-010" di A2 | Aturan vault di defaults.json dan data baris; nomor RTP dari kolom A sumber, baris yang memuat kata vault (F5, F14) |
| Klausa Alur Proses A2 yang tersisa | A2 sumber, tanpa perubahan kata; klausa ketiga dibuang karena gambar tidak memuatnya (image1.png dibuka) |
| 17 sel berubah, 15 risiko, distribusi level, pemilik, target, modifiedTime, fileSize | Perbandingan sel, hitung ulang LibreOffice atas out.xlsx, get_file_metadata |
| Rujukan lane lain di notes (K-10, K-13, JA-05, USULAN 3 dan 6 REG-02, Open item 10 REG-02, baris checklist) | specs/HR-ORG-01.json, notes/ISMS-REG-02.md, config/checklist.json, salinan audit; hanya di notes, tidak di sel |

Tidak ada angka, nama, atau tanggal lain yang saya tambahkan ke sel.
