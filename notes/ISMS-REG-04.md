# Catatan penyusun ISMS-REG-04: User Access Register & Periodic Access Review

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-REG-04.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-ISMS-REG-04 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; isinya register akun dan hak akses, sumber berlabel RESTRICTED (Internal)), audit_class B. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-REG-04.xlsx specs/ISMS-REG-04.patch.json /tmp/pen-ISMS-REG-04/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), 4 data validation dan 2 aturan conditional formatting di Register Akses (756 rumus), 1 data validation, 1 conditional formatting dan 201 rumus di Review Periodik, 7 rumus di Ringkasan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-REG-04_User_Access_Register_Periodic_Review.xlsx (159140 byte, berkas xlsx biasa di Drive, bukan Google Sheet) | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT | 2026-10-13T06:09:42Z (dicek lewat get_file_metadata; fileSize 159140 sama dengan hasil dekode dan dengan "bytes: 159140" di salinan audit) | download_file_content (didekode ke /tmp/src/ISMS-REG-04.xlsx; kerja di /tmp/pen-ISMS-REG-04/); semua 6 sheet dibaca dengan python3 -I + openpyxl; xl/media/image1.png dibuka |
| Kriteria penerimaan | prompt tugas | | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "7.1.3" dan ISO/IEC 27001:2022 "5.15, 5.18, 8.2" (sama dengan B12 dan B13 sumber) |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md, bagian SNX-ISMS-REG-04 (baris 1716 sampai 1913), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir dicocokkan ulang ke berkas xlsx dengan openpyxl |
| Pendukung | specs/HR-ORG-01.json, specs/ISMS-SOP-02.json, notes/ISMS-SOP-02.md, notes/ISMS-REG-02.md (lane lain), config/defaults.json | repo ini | Dibaca untuk nama peran dan konsistensi lintas dokumen; tidak ditulis ulang |

Sheet sumber: Kontrol Dokumen (A1:E37), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:E5, nilai dropdown), Register Akses (A1:S256, header baris 4, data baris 5 dan 6, rumus H, Q, R sampai baris 256), Review Periodik (A1:L205, header baris 4, satu baris isian di baris 5, rumus L sampai baris 205), Ringkasan (A1:B9). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet. Tidak ada sheet tersembunyi, komentar sel, nama terdefinisi, header atau footer cetak, ataupun kredensial di berkas ini.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Akun privileged (level Admin atau Privileged) ditinjau tiap 3 bulan, akun biasa tiap 6 bulan; tanggal Review berikutnya dihitung dari Review terakhir | Kontrol Dokumen B19: "Kolom Privileged, Review berikutnya, dan Cek dihitung otomatis: privileged ditinjau triwulanan, akses biasa semesteran." Register Akses Q5: `=IF(P5="","",EDATE(P5,IF(H5="Ya",3,6)))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |
| 2 | Hasil review dicatat di sheet Review Periodik dan tindak lanjutnya paling lama 10 hari kerja; keputusan hanya Tetap, Ubah, atau Cabut, dan status Terbuka bertahan sampai tanggal tindak lanjut diisi | Kontrol Dokumen B21: "Hasil review periodik dicatat di sheet Review Periodik; tindak lanjut maksimal 10 hari kerja." Review Periodik L5: `=IF(G5="","",IF(G5="Tetap","Selesai",IF(J5="","Terbuka","Selesai")))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |
| 3 | Kolom Cek menandai tiga kondisi pada akun berstatus Aktif (CABUT, KEDALUWARSA, REVIEW); Cara pakai sumber hanya menyebut dua | Kontrol Dokumen B20: "Cek = CABUT bila personel berstatus Keluar tetapi akun masih Aktif; Cek = REVIEW bila review terlambat." Register Akses R5: `=IF(A5="","",IF(AND(D5="Keluar",O5="Aktif"),"CABUT",IF(AND(M5<>"",M5<TODAY(),O5="Aktif"),"KEDALUWARSA",IF(AND(Q5<>"",Q5<TODAY(),O5="Aktif"),"REVIEW","OK"))))` | 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT |

Fakta pendukung: B14 "3 tahun" (masa simpan record, sama dengan Bagian 8 SOP-02 menurut salinan audit); B10 "Head of Operation" (Pemilik dokumen, jabatan tanpa nama); B15 "Register hak akses pengguna ke sistem internal dan sistem pelanggan, serta catatan review akses periodik sesuai SNX-ISMS-SOP-02."; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B12 "Klausul 7.1.3"; Daftar: Status personel Aktif, Mutasi, Keluar, Vendor atau partner; Level Read-only, Operator, Admin, Privileged; MFA Ya, Tidak, Tidak didukung. Hitung ulang atas out.xlsx lewat LibreOffice (xlsx ke xlsx, dibaca data_only): Ringkasan B3 sampai B9 bernilai 0 semua, nol sel galat, H5, Q5, R5 kosong.

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (python3 -I + openpyxl): 59 sel berubah (nilai atau warna isi), selain itu tidak ada sel yang berubah. Rumus, data validation, conditional formatting, sheet Daftar, Ringkasan, dan gambar tidak disentuh.

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Register Akses baris 5 dan 6 (clear_rows) | ACC-0001 (Jumphost, Operator) dan ACC-0002 (SIEM Wazuh [pelanggan], Admin, vendor), nama, tiket, dan pelanggan berupa placeholder, kolom Catatan "CONTOH" | Dikosongkan; warna isi biru muda diganti warna sel input (kuning) mengikuti baris 7; rumus H, Q, R tetap dan bernilai kosong | Baris CONTOH (S5, S6, A2). RUNBOOK §6: buang baris CONTOH dengan clear_rows, bukan hapus baris. Penanganan cacat butir 1 dan 3 |
| Review Periodik baris 5 (clear_rows) | 2026-Q4, Jumphost, ACC-0001, [nama personel], Operator, Head of Operation, Tetap, Sesuai peran, 2026-12-15 | Dikosongkan; warna isi mengikuti baris 6; rumus L tetap | Data dummy: merujuk ACC-0001 yang placeholder, bertanggal sesudah tanggal draft, dan berwarna biru muda seperti baris CONTOH. Sheet ini tidak berlabel CONTOH, jadi statusnya contoh adalah inferensi audit. USULAN 3 |
| Register Akses A2 | "Baris biru muda = CONTOH. Kolom abu-abu dihitung otomatis." | "Kolom abu-abu dihitung otomatis." | Baris biru muda sudah tidak ada. Kalimat kedua milik tim dipertahankan |
| Kontrol Dokumen baris 25 (clear_rows) | Legenda biru muda "Baris CONTOH: hapus atau timpa saat dipakai" | Dikosongkan (teks); kotak warna ikut warna baris 26 (abu) | Baris CONTOH sudah dihapus, jadi petunjuk "hapus atau timpa" tidak berlaku. Akibat kosmetik di Open item 7 |
| B6 Revisi | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt dan defaults.json; huruf kapital semua bukan penulisan status di defaults |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json approved_by. USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 5.15, 5.18, 8.2" | "Kontrol Annex A 5.15, 5.18, 8.2" | 5.15 Access control, 5.18 Access rights, 8.2 Privileged access rights adalah kontrol Annex A (tabel SoA di salinan audit memakai nama itu); "klausul atau kontrol" ragu-ragu. Angkanya sama dengan acuan di prompt. Awalan "Kontrol Annex A" juga mencegah 8.2 terbaca sebagai klausul 8.2 badan standar |
| B20 Cara pakai butir 3 | "Cek = CABUT bila personel berstatus Keluar tetapi akun masih Aktif; Cek = REVIEW bila review terlambat." | Sama, ditambah "Cek = KEDALUWARSA bila Berlaku sampai lewat;" di tengah | Rumus R sumber punya kondisi KEDALUWARSA yang tidak ada di Cara pakai (cacat audit butir 5). Satu klausa disisipkan dengan pola tim; kalimat lain tidak diubah. Render LibreOffice: tetap dua baris di tinggi baris 23,85 |
| C30 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt dan defaults.json |
| A31 sampai E31 (clear_rows) | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; topik RTO tidak ada di workbook ini (pencarian "RTO" dan "target pulih" di semua sheet: satu-satunya kemunculan adalah baris ini). USULAN 2 |
| B35, B36, B37 Pengesahan | "Head of Operation", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 1 |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen yang diminta; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama |
| Tidak diubah | | | Tanda tangan dan tanggal (C35 sampai D37) kosong (batas keras 3). Tanggal efektif B8 bukan tanggal. Tanggal draft B7 dari tim. Tujuan B15, Cara pakai butir 1, 2, 4, legenda sel input dan sel rumus, subjudul A2, Alur Proses A2 (cocok dengan gambar: kotak biru, kotak oranye, dan garis putus-putus ada di image1.png), sheet Daftar dan Ringkasan, semua rumus, data validation, format kondisional, gambar. Tidak ada label (USULAN) di sel karena tidak ada angka atau fakta baru yang masuk sel |

Render PDF LibreOffice atas out.xlsx (halaman Kontrol Dokumen, diperbesar): Cara pakai butir 3 dua baris, Riwayat revisi hanya satu baris terisi, Pengesahan memuat tiga nama. Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas semua sel teks out.xlsx: nol temuan (sumber punya empat temuan "CONTOH": Kontrol Dokumen B25, Register Akses A2, S5, dan S6; semuanya sudah diganti atau dikosongkan). Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter).

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Register Akses hanya 2 baris CONTOH dengan placeholder; belum ada akun nyata, jadi ISR-009 dan RTP-009 belum punya bukti register terisi | Dua baris dikosongkan sesuai RUNBOOK §6. Akun nyata tidak dikarang. Pengisian oleh Ops adalah keputusan dan pekerjaan manusia (Open item 1) |
| 2 | Baris review 2026-Q4 bertanggal sesudah tanggal draft, berwarna biru muda tanpa label CONTOH; Review terakhir ACC-0001 (P5) 2026-10-01 tidak sama dengan tanggal review 2026-12-15 | Baris review dikosongkan bersama ACC-0001 (USULAN 3); selisih tanggal hilang karena kedua baris kosong. Cara pakai Review Periodik A2 ("perbarui kolom Review terakhir di Register Akses") tetap utuh |
| 3 | ACC-0002 Review terakhir 2026-09-01 sebelum tanggal draft, Review berikutnya 2026-12-01 | Hilang bersama baris CONTOH |
| 4 | Masa simpan 3 tahun berbeda dari REG-01, REG-02, REG-03, SOA-01 ("Berlaku sampai digantikan") | Tidak diubah: 3 tahun adalah angka sumber (B14) dan sama dengan Bagian 8 SOP-02 dan master list menurut salinan audit. Perbedaan dengan register lain mengikuti jenis rekaman, bukan kesalahan. Titik awal hitungan tidak tertulis di sumber: USULAN 6 |
| 5 | Kolom Cek hanya menilai akun Aktif; akun Dinonaktifkan atau Dicabut menghasilkan OK; TODAY() membuat nilai tersimpan berubah; Cara pakai tidak menyebut KEDALUWARSA | KEDALUWARSA ditambahkan ke Cara pakai (B20). Rumus tidak diubah: batasan akun Aktif tampak disengaja dan tidak jelas salah. TODAY() adalah sifat rumus; nilai dihitung ulang saat berkas dibuka (Open item 6) |
| 6 | Level "Privileged" ada di dropdown dan dihitung privileged bersama Admin; dropdown tidak memuat nilai matriks SOP-02 (Agent, Group admin, Analyst, Collection) | Tidak diubah: mengganti nilai dropdown mengubah data validation dan rumus H. USULAN 7, Open item 3 |
| 7 | SOP-02 menulis "sheet Periodic Review", sedangkan sheet di REG-04 bernama "Review Periodik" | Sudah diperbaiki di sisi SOP-02 (notes/ISMS-SOP-02.md butir 11: dokumen memakai "Review Periodik"). Nama sheet di sini tidak diubah |
| 8 | SOP-02 menyatakan matriks akses detail ditetapkan di REG-04, tetapi REG-04 hanya register per akun | Tidak diubah: matriks butuh sheet baru (alat menolak) dan isi yang tidak ada di sumber. SOP-02 sudah memberi matriks acuan awal berlabel USULAN. Open item 3 |
| 9 | Pengesahan kosong (C35:D37); status "Menunggu" (E30:E31); revisi 00 tercatat dua kali | Baris kedua dikosongkan (USULAN 2). Tiga penanda tangan diisi dari defaults.json (USULAN 1); tanda tangan dan tanggal dibiarkan kosong (batas keras 3). "Menunggu" di E30 dipertahankan |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B13 "Klausul atau kontrol Annex A 5.15, 5.18, 8.2" | Diganti "Kontrol Annex A 5.15, 5.18, 8.2" |
| B | Legenda B25 dan Register Akses A2 menyebut baris CONTOH yang sudah dihapus | B25 dikosongkan, A2 diperpendek |
| C | Kolom "Review berikutnya" kosong bila "Review terakhir" kosong, sehingga akun baru tanpa review tidak pernah ditandai REVIEW; Cara pakai tidak menyuruh mengisi Review terakhir saat akun dicatat. Pada kedua baris CONTOH sumber, Review terakhir sama dengan Tgl diberikan | Tidak diubah (rumus dan Cara pakai dua baris penuh). USULAN 4 |
| D | Ringkasan B5 "Akun aktif tanpa MFA" menghitung MFA = "Tidak" saja; nilai "Tidak didukung" ada di dropdown tetapi tidak terhitung | Tidak diubah (rumus). USULAN 8 |
| E | Aturan lintas dokumen yang tidak berlaku di sini: PPN (tidak ada), kunci backup (tidak disebut), vault (tidak disebut; "password manager" dan "vault" tidak muncul di workbook), rujukan internal AI (nol temuan pola lint), sebutan COO (sesudah B11 dan B37 diganti tidak ada lagi sebutan COO di sel mana pun, jadi aturan "Direktur (COO)" tidak terpakai), sebutan CEO (tidak ada) | Tidak ada perubahan |
| F | Tiket: kolom J "Ref tiket" tidak menyebut sistemnya; SOP-02 (lane lain) menulis permintaan akses diajukan di Service Hub (GLPI), sedangkan aturan owner: Zammad untuk Ops, GLPI untuk generalist | Tidak diubah: register tidak melanggar aturan karena tidak menyebut sistem; memutuskan sistem untuk kolom ini berarti memutuskan proses. USULAN 5 |

## USULAN

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
| 8 | Hitung juga MFA "Tidak didukung" di Ringkasan, atau tambahkan baris indikator terpisah | Ringkasan B5 | Belum | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Register Akses kosong sesudah baris CONTOH dihapus. Ops harus mengisi akun nyata (satu baris per akun per sistem, tanpa password atau token) sebelum audit; ISR-009 di REG-02 dan RTP-009 di REG-03 ("Terapkan SNX-ISMS-REG-04 dan review akses privileged triwulanan", menurut salinan audit) belum punya register terisi sebagai bukti. HUMAN-VERDICT: kecukupan isi register terhadap daftar akun sistem sebenarnya tidak bisa dibuktikan dari berkas ini | Fani, Ops |
| 2 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Sumber tidak menyebut yang dikecualikan dari register (misalnya sistem atau jenis akun yang tidak dicatat), lokasi simpan, maupun pemilik rekaman selain "Pemilik dokumen Head of Operation". Kode yang dirujuk di sel: SNX-ISMS-SOP-02 (B15). Masa simpan 3 tahun dipertahankan | Orkestrator, Fani |
| 3 | Dropdown Level (Read-only, Operator, Admin, Privileged) tidak sama dengan istilah matriks SOP-02, dan REG-04 tidak punya matriks per sistem dan peran padahal SOP-02 menyerahkan detailnya ke sini. Lihat USULAN 7 | Fani |
| 4 | Pemetaan peran sumber ke nama peran HR-ORG-01: "Head of Operation" persis sama (pemilik dokumen B10; HR-ORG-01 menandainya USULAN tanpa pemegang, K-10 dan K-11, dan hubungannya dengan VP Tech Operation and Services belum ditetapkan, K-09). "ISO/ISMS Coordinator" (pemeriksa di sumber) dan "COO" (penyetuju di sumber) diganti oleh tiga penanda tangan defaults.json; HR-ORG-01 menulis ISMS Coordinator "belum ditetapkan" (K-13). Header Review Periodik F4 "Reviewer (pemilik sistem)" dan K4 "Pelaksana tindak lanjut" tidak punya padanan jabatan di HR-ORG-01; SOP-02 memakai "Pemilik sistem" dan "Administrator sistem". Header tidak diubah (suara tim) | Fani, owner |
| 5 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Kotak "Tindak lanjut" tidak menyebut pelaku, dan gambar tidak menunjukkan siapa memutuskan "Cabut atau ubah?". Legenda Alur Proses A2 cocok dengan gambar, jadi tidak diubah; bila gambar diperbarui, legenda ikut ditinjau | Orkestrator, Fani |
| 6 | Kolom Cek hanya menilai akun berstatus Aktif (akun Dinonaktifkan atau Dicabut selalu OK, termasuk personel Keluar yang akunnya baru Dinonaktifkan). Cara pakai butir 3 sekarang menyebut tiga kondisi tetapi syarat "akun masih Aktif" tertulis hanya pada CABUT. Rumus memakai TODAY(), jadi nilai Cek dan Ringkasan berubah tiap hari | Fani |
| 7 | Keterbatasan alat dan kosmetik. Nilai rumus belum tersimpan di out.xlsx (openpyxl); Excel dan LibreOffice menghitung ulang saat dibuka. Tinggi baris tidak diubah: baris 5 dan 6 Register Akses tetap setinggi 23,85 dan baris 31 Kontrol Dokumen tetap kosong setinggi 57,45. Legenda warna kini punya satu kotak abu tanpa label di atas kotak abu "Sel rumus" (baris 25 menyalin warna baris 26). HUMAN-VERDICT: buka di Excel dan nilai apakah ini mengganggu | Orkestrator, owner |
| 8 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: Cara pakai butir 1 sampai 4 ("Jangan pernah menulis password atau token di file ini."), "Sel rumus: jangan diubah", "Baris CONTOH: hapus atau timpa saat dipakai". Tidak ada yang dijalankan sebagai instruksi kepada penyusun; butir CONTOH hilang karena baris CONTOH dikosongkan menurut RUNBOOK, butir lainnya tidak diubah | Orkestrator |
| 9 | Tanggal draft 13 Oktober 2026 (B7, B30) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan" | owner |
| 10 | Tidak ada tiket Zammad atau GLPI, vault, kunci backup, ataupun PPN di workbook ini; aturan lintas dokumen tentang itu tidak berlaku. Sistem tiket untuk kolom Ref tiket: lihat USULAN 5 | owner |

## Asumsi dan tafsir

1. Baris Review Periodik 5 diperlakukan sebagai data dummy walau tidak berlabel CONTOH. Alasannya tiga: merujuk ACC-0001 yang placeholder, nama "[nama personel]", dan tanggal 2026-12-15 jatuh sesudah tanggal draft. Bila ACC-0001 dikosongkan dan baris ini dibiarkan, review menunjuk akun yang tidak ada.
2. "Approval persis" dari prompt mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json.
3. Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
4. Pemilik dokumen tetap "Head of Operation" walau penyusun di blok Pengesahan Erik Dwi Yanto: sumber memisahkan keduanya, dan prompt memerintahkan process_owner mengikuti "Pemilik dokumen" sumber.
5. Acuan klausul: B12 "Klausul 7.1.3" dan B13 "Kontrol Annex A 5.15, 5.18, 8.2" memuat angka persis dari prompt. Awalan "Kontrol Annex A" untuk 27001 adalah tafsir penyusun berdasarkan nama kontrol di tabel SoA salinan audit, bukan kata dari prompt.
6. Isi dari lane lain (HR-ORG-01, SOP-02, REG-02, SoA, REG-03) dibaca dari repo dan salinan audit, bukan dari Drive terbaru; kutipannya bisa basi bila tim sudah mengubah dokumen itu.
7. "Berlaku sampai" di B20 mengacu ke kolom M Register Akses (header "Berlaku sampai"), yaitu tanggal kedaluwarsa akses; tidak ada makna lain yang dipakai.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI? Pemeriksaan atas 9 nilai sel teks yang saya tulis atau ubah (B6, B11, B13, B20, C30, B35 sampai B37, Register Akses A2) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| B20 mengulang "Cek =" tiga kali dan terbaca mekanis | Dipertahankan: dua pengulangan pertama milik tim, klausa KEDALUWARSA disisipkan dengan pola yang sama supaya suara tim utuh (T1), tanpa kata penghubung baru |
| "Kontrol Annex A 5.15, 5.18, 8.2" terbaca seperti daftar tiga yang dipaksakan | Dipertahankan: tiga nomor itu adalah acuan persis dari prompt dan B13 sumber, bukan pilihan penyusun |
| Register Akses A2 hasil pemangkasan bisa terbaca telegrafis | Dipertahankan: tinggal kalimat tim yang utuh dan jelas, satu fakta |
| "Jangan pernah menulis password atau token" di Cara pakai butir 1 mengandung "pernah" sebagai penegas | Tidak diubah (T1): kalimat tim yang jelas, aturan keamanan, bukan tambahan penyusun |
| Notes ini panjang dan memakai banyak tabel | Dipertahankan: format notes diminta prompt; tiap sel membawa fakta atau keputusan yang berbeda dan tidak ada ringkasan penutup |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust), kelompok tiga yang dipaksakan, penutup positif | Tidak ada di nilai patch (pencarian karakter dan pola lint, nol temuan). Notes ini tidak memakai em-dash, en-dash, atau tebal; kata CABUT, KEDALUWARSA, REVIEW, OK adalah nilai kolom Cek, bukan penekanan |

Adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.ISMS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di prompt dan defaults.json |
| "Klausul 7.1.3" dan "Kontrol Annex A 5.15, 5.18, 8.2" | Prompt (acuan klausul baris ini); B12 dan B13 sumber. Nama kontrol (Access control, Access rights, Privileged access rights) dari tabel SoA salinan audit, hanya di notes |
| "Cek = KEDALUWARSA bila Berlaku sampai lewat" | Rumus R5 sumber (`M5<>"",M5<TODAY(),O5="Aktif"`) dan header M4 "Berlaku sampai" |
| "Kolom abu-abu dihitung otomatis." | Kalimat kedua A2 sumber, tanpa perubahan kata |
| "3 tahun", "Head of Operation", "13 Oktober 2026", "Ditetapkan saat pengesahan", "Klausul 7.1.3" | Tidak diubah dari sumber (B14, B10, B7, B8, B12) |
| 59 sel berubah, 756 dan 201 rumus, nilai Ringkasan 0 | Perbandingan sel dan hitung ulang LibreOffice atas out.xlsx |
| modifiedTime, fileSize | get_file_metadata atas fileId sumber |
| Rujukan lane lain di notes (K-09, K-10, K-11, K-13, butir 11 notes SOP-02, nama sistem tiket SOP-02, ISR-009, RTP-009) | specs/HR-ORG-01.json, specs/ISMS-SOP-02.json, notes/ISMS-SOP-02.md, salinan audit; hanya di notes, tidak di sel |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: "pelanggan".
Disunting: Tujuan, Cara pakai 1 sampai 4, catatan Register Akses A2 dan Review Periodik A2.
Cara pakai 3: skrip istilah mekanis mengubah "Berlaku sampai lewat" (artinya tanggal sudah terlampaui) menjadi "Berlaku sampai melalui"; dikoreksi menjadi "tanggal Berlaku sampai sudah terlampaui". Arti kembali seperti bed1bb6.
Cara pakai 2: "privileged ditinjau triwulanan, akses biasa semesteran" menjadi "Review akses privileged dilakukan setiap triwulan, akses biasa setiap semester"; arti tetap.
