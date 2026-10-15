# Catatan penyusun ISMS-REG-02: Information Security Risk Assessment Register

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-REG-02.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-ISMS-REG-02 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; isinya risiko keamanan informasi Operation, sumber berlabel RESTRICTED (Internal)), audit_class C2. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-REG-02.xlsx specs/ISMS-REG-02.patch.json /tmp/pen-ISMS-REG-02/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), 4 data validation dan 1 aturan conditional formatting di Register Risiko (225 rumus), 1 aturan conditional formatting dan 5 rumus di Ringkasan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-REG-02_IS_Risk_Assessment_Register.xlsx (119823 byte, berkas xlsx di Drive) | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q | 2026-10-13T06:09:37Z (dicek ulang lewat get_file_metadata; fileSize 119823 sama dengan hasil dekode dan dengan "bytes: 119823" di salinan audit) | download_file_content (didekode ke /tmp/src/ISMS-REG-02.xlsx; kerja di /tmp/pen-ISMS-REG-02/); semua 6 sheet dibaca dengan python3 -I + openpyxl; gambar xl/media/image1.png dibuka |
| Kriteria penerimaan | config/worklist.json dan prompt tugas | | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "6.1" dan ISO/IEC 27001:2022 "6.1.2, 8.2" (sama dengan B12 dan B13 sumber) |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md, bagian SNX-ISMS-REG-02 (baris 1298 sampai 1516), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir dicocokkan ulang ke berkas xlsx dengan openpyxl |
| Pendukung | notes/ISMS-REG-01.md dan specs/HR-ORG-01.json (lane lain), context/audit bagian REG-01 dan REG-03 | repo ini, hasil kerja lane lain | Dibaca untuk konsistensi lintas dokumen; tidak ditulis ulang |

Sheet sumber: Kontrol Dokumen (A1:E38), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:C8), Register Risiko (A1:Q79, header baris 4, data baris 5 sampai 19, rumus sampai baris 79), Matriks Risiko (A1:G24), Ringkasan (A1:B8). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Skor = Likelihood x Impact pada skala 1 sampai 5; level dihitung otomatis dari skor dengan empat ambang | Matriks Risiko A3: "Skor = Likelihood x Impact. Rendah 1 sampai 4 · Sedang 5 sampai 9 · Tinggi 10 sampai 19 · Kritis 20 sampai 25". Register Risiko I5: `=IF(OR(G5="",H5=""),"",G5*H5)` | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |
| 2 | Level Rendah diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03; risiko Kritis dilaporkan ke COO dan hanya COO yang menerimanya, secara tertulis | Kontrol Dokumen B20: "Kriteria penerimaan: level Rendah dapat diterima pemilik risiko; Sedang ke atas wajib rencana penanganan di SNX-ISMS-REG-03." Matriks Risiko B24: "Tindakan segera; dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis" | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |
| 3 | Register berisi 15 risiko (ISR-001 sampai ISR-015) yang berstatus usulan awal Divisi Operation dan belum disetujui; penilaian ulang minimal tahunan, setelah insiden P1, dan setelah perubahan besar | Register Risiko A2: "Baris biru muda = usulan awal, bukan baris contoh: validasi lalu ubah kolom Catatan menjadi Disetujui." Q5 sampai Q19: "Usulan awal". Kontrol Dokumen B21: "Penilaian ulang minimal tahunan, setelah insiden P1, dan setelah perubahan besar." | 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q |

Fakta pendukung yang tidak diubah: B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B10 "ISMS Coordinator" (Pemilik dokumen, jabatan tanpa nama); B14 "Berlaku sampai digantikan"; B22 "Usulan awal Divisi Operation dari riwayat operasi di knowledge base SINUX; wajib divalidasi ISMS Coordinator dan pemilik risiko." Hitung ulang atas out.xlsx lewat LibreOffice (xlsx ke xlsx, dibaca data_only): skor = L x H untuk 15 baris, Kritis 1 (ISR-002, skor 20), Tinggi 10, Sedang 4, Rendah 0, Total 15 di Ringkasan B4 sampai B8, penilaian ulang P5 = 2027-10-13, nol sel galat. Pemilik risiko: Head of Operation 6, Lead NOC 3, Lead SOC 3, Tech dan Product 1, Service Delivery Manager 1, ISMS Coordinator 1.

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (python3 -I + openpyxl): 17 sel berubah, selain itu tidak ada sel yang berubah. Tidak ada clear_rows (lihat Asumsi dan tafsir butir 1).

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt; penulisan sama dengan form OPS lain |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by dan prompt; USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 6.1.2, 8.2" | "Klausul 6.1.2, 8.2" | 6.1.2 dan 8.2 adalah klausul badan standar (penilaian risiko), bukan kontrol Annex A; "klausul atau kontrol" ragu-ragu. Angka sama dengan acuan di prompt |
| B26 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: usulan awal Divisi Operation, belum berstatus Disetujui" | Warna E7EEF7 di A26 sama dengan warna baris 5 sampai 19. Baris itu usulan awal, bukan CONTOH (A2 Register Risiko menyatakannya), jadi legenda lama menyuruh menghapus data tim |
| C31 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A32 sampai E32 | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; topik RTO tidak ada di workbook ini (pencarian di semua sheet: nol kemunculan). USULAN 2 |
| B36, B37, B38 | "ISMS Coordinator", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 1 |
| Alur Proses A2 | "Kotak biru = output akhir · kotak oranye = cabang ke tindakan atau prosedur lain · garis putus-putus = kembali ke alur utama" | Dua klausa pertama saja | Gambar hanya punya satu kotak biru, satu kotak oranye, dan garis penuh; tidak ada garis putus-putus, jadi klausa ketiga menunjuk sesuatu yang tidak ada. Gambar tidak bisa diubah alat (Open item 4) |
| Register Risiko A2 | "Baris biru muda = usulan awal, bukan baris contoh: validasi lalu ubah kolom Catatan menjadi Disetujui." | "Baris biru muda = usulan awal: validasi lalu ubah kolom Catatan menjadi Disetujui." | Penyangkalan "bukan baris contoh" tidak lagi perlu sesudah legenda B26 dan baris CONTOH dibersihkan dari teks; instruksi validasi tim tetap utuh |
| Register Risiko F5 (ISR-001, Kontrol eksisting) | "Password manager internal sudah dipasang, belum live" | "Vault sudah dipasang, belum live; menunggu konfirmasi Ops" | Aturan vault di defaults.json: status "menunggu konfirmasi Ops". Sebutan "Vault" memakai istilah yang sudah dipakai D5 di baris yang sama ("migrasi ke vault"); satu istilah untuk satu hal. Panjang teks dijaga supaya muat tiga baris (tinggi baris 35.05, dicek di render LibreOffice). Open item 3 |
| Matriks Risiko B24 (level Kritis) | "Tindakan segera; dilaporkan ke COO; penerimaan risiko hanya oleh COO secara tertulis" | "Tindakan segera; dilaporkan ke Direktur (COO); penerimaan risiko hanya oleh COO secara tertulis" | Aturan sebutan COO di data_conflicts: "Direktur (COO)" pada sebutan pertama di badan dokumen, sesudahnya "COO". Setelah B11 dan B38 diganti, B24 adalah sebutan COO pertama menurut urutan sheet; sebutan kedua dalam sel yang sama tetap "COO". Hanya dua baris teks, muat di tinggi baris 23.85 (dicek di render) |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen yang diminta prompt; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama |
| Tidak diubah | | | Tanda tangan dan tanggal (C36 sampai D38) kosong (batas keras 3). Tanggal efektif B8 bukan tanggal. 15 baris risiko (kecuali F5), sheet Daftar, sisa Matriks Risiko, Ringkasan, rumus, data validation, format kondisional, gambar. Tidak ada label (USULAN) di sel karena tidak ada angka atau fakta baru yang masuk sel |

Render PDF LibreOffice atas out.xlsx: Kontrol Dokumen terbaca utuh, B26 satu baris, Riwayat revisi hanya satu baris terisi, Pengesahan memuat tiga nama; Register Risiko F5 tiga baris dan A2 satu baris; Matriks Risiko B24 dua baris. Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas semua sel teks out.xlsx: nol temuan (sumber punya satu temuan, "CONTOH" di B26, sudah diganti). Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter).

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Seluruh 15 risiko "Usulan awal", belum "Disetujui" | Tidak diubah: validasi oleh ISMS Coordinator dan pemilik risiko adalah keputusan manusia dan status persetujuan bukan wewenang penyusun (batas keras 3). Legenda dan A2 kini menyatakan statusnya. Open item 2 |
| 2 | ISR-002 (Kritis, skor 20): pemilik risiko Lead SOC, keputusan Mitigasi, padahal Matriks B24 mensyaratkan penerimaan oleh COO secara tertulis; tidak ada kolom tenggat dan skor sisa risiko | Sebutan COO diselaraskan ke "Direktur (COO)" (B24). Penerimaan tertulis dan tenggat tidak dibuat di sini, karena kolom Diterima oleh dan Tanggal penerimaan hanya ada di SNX-ISMS-REG-03 (Cara pakai butir 3 REG-03 di salinan audit) dan REG-03 menyebut penerimaan oleh pemilik risiko, bukan COO. Tidak bisa dipastikan dari sumber mana yang berlaku. USULAN 3, Open item 5 |
| 3 | Tidak ada risiko Rendah dan tidak ada keputusan selain Mitigasi; Hindari, Transfer, Terima tidak terpakai | Bukan cacat isi, tidak diubah. Menambah risiko Rendah atau mengganti keputusan berarti mengarang penilaian. Open item 8 |
| 4 | Satu pasang L dan I, tanpa skor inheren versus residual; gambar menyebut "kontrol eksisting diperhitungkan" | Tidak diubah: menambah kolom di luar kemampuan alat dan mengubah struktur register. Residual sudah ada di SNX-ISMS-REG-03 (L res, I res, Skor res, Level res). Pernyataan di Cara pakai bahwa L dan I di sini = kondisi dengan kontrol eksisting adalah USULAN 4 |
| 5 | Hanya 4 dari 15 risiko merujuk ID aset REG-01 (AST-001, AST-009, AST-005, AST-012), padahal Cara pakai butir 1 menyuruh merujuk | Tidak diubah: pemetaan kelompok ke ID aset adalah inferensi (audit sendiri menandainya begitu). Selain itu lane REG-01 sudah mengosongkan 12 baris aset AST-001 sampai AST-012 (notes/ISMS-REG-01.md), jadi ID yang kini dirujuk REG-02 belum ada isinya di REG-01 sampai Ops mengisi ulang. USULAN 5, Open item 1 |
| 6 | "Zimbra" di D7 (ISR-003) sedangkan REG-01 menamai AST-009 "Server email mail.nusagrid.co.id" tanpa Zimbra | Tidak diubah: Zimbra disebut juga di SNX-ISMS-SOP-05 (salinan audit), jadi fakta tim, hanya penamaan aset di REG-01 yang kurang. Open item 9 |
| 7 | Matriks B23 menyebut "register risiko ISMS" yang terpisah, dan register itu tidak ada | Tidak diubah: mengganti rujukan berarti memutuskan proses (apakah register ini sendiri yang dimaksud). USULAN 7 |
| 8 | Revisi 00 dua kali pada tanggal sama; pengesahan kosong; status "Menunggu" | Baris kedua dikosongkan (USULAN 2). Pengesahan diisi tiga penanda tangan dari defaults.json, tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Kolom Disetujui "Menunggu" di baris 31 dipertahankan |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B13 "Klausul atau kontrol Annex A 6.1.2, 8.2" | Diganti "Klausul 6.1.2, 8.2" |
| B | Legenda B26 menyebut baris CONTOH padahal baris biru adalah usulan awal | Ditulis ulang sesuai isi |
| C | Legenda Alur Proses A2 menyebut garis putus-putus yang tidak ada di gambar | Klausa dihapus |
| D | Kontrol eksisting ISR-001 dan aturan vault ("Aktif" di REG-01 versus "belum live" di register ini, CONTEXT-PACK butir 6) | F5 ditulis sesuai sumber ini dengan status "menunggu konfirmasi Ops" |
| E | Aturan lintas dokumen yang tidak berlaku di sini: PPN (tidak ada), kunci backup dengan salinan offline atau break-glass (register tidak menyebut kunci backup; ISR-006 hanya soal uji restore), rujukan internal AI (tidak ada, dicek dengan pola lint), tiket GLPI (tidak disebut; "ticketing system" di B12, USULAN 6) | Tidak ada perubahan |

## USULAN

Label (USULAN) tidak ditulis di sel xlsx karena tidak ada angka atau fakta baru yang masuk sel; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan ISMS Coordinator, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Pilih satu rumusan penerimaan risiko Kritis: dicatat sebagai penerimaan tertulis COO di kolom Diterima oleh dan Tanggal penerimaan SNX-ISMS-REG-03, atau Matriks B24 diubah mengikuti REG-03. Belum diterapkan | Matriks Risiko B24; REG-03 Cara pakai butir 3 | owner (Amirull sebagai COO) |
| 4 | Tambah satu kalimat Cara pakai: L dan I di register ini dinilai dengan kontrol eksisting diperhitungkan, risiko sisa dinilai di SNX-ISMS-REG-03. Belum diterapkan karena baris butir 1 sampai 5 hanya muat dua baris teks | Kontrol Dokumen Cara pakai | Fani |
| 5 | Rujuk ID aset REG-01: ISR-006 ke AST-007 (Acronis), ISR-008 ke AST-002, AST-003, AST-006. Dibuat sesudah REG-01 diisi ulang oleh Ops, karena ID bisa berubah. Belum diterapkan | Register Risiko B10 dan B12 | Fani |
| 6 | Sebut sistem tiket pada ISR-008: Zammad (tiket Ops) atau Zammad dan GLPI. Sumber menulis "ticketing system" tanpa nama. Batas "generalist" untuk GLPI belum dirinci owner. Belum diterapkan | Register Risiko B12 | owner |
| 7 | Ganti "dinaikkan ke register risiko ISMS" dengan rujukan yang ada, misalnya "dicatat di SNX-ISMS-REG-02 dengan rencana di SNX-ISMS-REG-03". Belum diterapkan | Matriks Risiko B23 | Fani |
| 8 | Ganti pemilik risiko ISR-007 "Tech dan Product" (nama fungsi) dengan nama peran dari Struktur Organisasi, serentak di REG-01 (E9 sumber), REG-02 (K11), dan REG-03 (H11) supaya tiga dokumen sama. Belum diterapkan | Register Risiko K11 | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Register Risiko merujuk AST-001, AST-005, AST-009, AST-012, sedangkan lane REG-01 mengosongkan 12 baris aset itu karena bertanda CONTOH. Rujukan baru valid sesudah Ops mengisi ulang REG-01 dengan ID yang sama; ID, nama, dan pemilik harus dicocokkan saat itu | Fani, lane ISMS-REG-01 |
| 2 | 15 risiko belum divalidasi (Catatan tetap "Usulan awal"). Validator yang disebut sumber, ISMS Coordinator, belum dipetakan ke jabatan atau orang (HR-ORG-01 tidak menetapkannya); pemilik risiko Head of Operation berhubungan dengan VP Tech Operation and Services belum ditetapkan (K-09 di HR-ORG-01) | Fani, owner |
| 3 | Vault: ISR-001 menulis "belum live"; REG-01 sumber menulis AST-001 vault.sinux.co.id berstatus "Aktif". Kondisi hari ini tidak terukur. Sampai Ops mengonfirmasi, F5 memuat "menunggu konfirmasi Ops" | Ops (Fani) |
| 4 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Kotak "Terima risiko" tidak punya panah lanjutan, dan gambar tidak menunjukkan jalur risiko Kritis ke COO (hanya cabang Rendah dan bukan Rendah). Legenda A2 sudah disesuaikan; bila gambar diperbarui, legenda ikut ditinjau | Orkestrator, Fani |
| 5 | Penerimaan risiko Kritis: Matriks B24 mensyaratkan penerimaan tertulis COO, REG-03 menyebut penerimaan residual oleh pemilik risiko, dan ISR-002 berpemilik Lead SOC. Belum ada aturan yang menyatukan, dan register tidak punya kolom tenggat. Lihat USULAN 3 | owner |
| 6 | Format xlsx tidak punya bagian Dokumen terkait, tabel rekaman (lokasi, pemilik), ataupun scope. Kode yang dirujuk di sel: SNX-ISMS-REG-01, SNX-ISMS-REG-03; di gambar sama. Lokasi simpan dan pemilik rekaman tidak ada di sumber. Masa simpan "Berlaku sampai digantikan" dipertahankan; tidak ada masa simpan untuk versi lama register maupun untuk penerimaan risiko tertulis. Angka tidak diusulkan karena tidak ada dasar | Orkestrator, Fani |
| 7 | Singkatan yang tidak diuraikan di workbook: C, I, A (kolom CIA), "P1" (Cara pakai butir 4, gambar), dan huruf "I" yang dipakai dua arti (Impact di kolom H, Integrity di kolom E). Tidak diubah karena baris Cara pakai hanya muat dua baris dan alat tidak mengubah tinggi baris. HUMAN-VERDICT: apakah auditor perlu uraian ini di Kontrol Dokumen | Fani |
| 8 | Tidak ada risiko Rendah dan semua keputusan Mitigasi; opsi Hindari, Transfer, Terima ada di dropdown tetapi tidak terpakai. Auditor kemungkinan menanyakan dasar memilih Mitigasi untuk semua baris | Fani |
| 9 | Zimbra (D7) tidak tersebut di penamaan AST-009 pada REG-01 ("Server email mail.nusagrid.co.id"). Zimbra disebut di SNX-ISMS-SOP-05 menurut salinan audit, bukan dari Drive terbaru | Fani, lane ISMS-REG-01 |
| 10 | "knowledge base SINUX" di Cara pakai butir 5 dan kolom Kontrol eksisting dipertahankan karena Knowledge base SINUX adalah aset Operation (AST-008 di REG-01) dan ISR-011 menyebutnya sebagai kontrol. Bila konsultan menganggap istilah itu rujukan internal AI, ganti dengan nama sistem yang disetujui Ops | Fani |
| 11 | Tanggal draft 13 Oktober 2026 (B7, B31) dan Tgl penilaian semua 2026-10-13 (O5 sampai O19) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Penilaian ulang otomatis 2027-10-13. Tanggal efektif tetap "Ditetapkan saat pengesahan" | owner |
| 12 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: "validasi lalu ubah kolom Catatan menjadi Disetujui", "Sel rumus: jangan diubah", Cara pakai butir 1 sampai 5. Tidak ada yang dijalankan: status Disetujui tidak diubah, rumus tidak diubah | Orkestrator |
| 13 | Keterbatasan alat: nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka; tinggi baris tidak diubah. HUMAN-VERDICT: buka di Excel dan lihat apakah Register Risiko F5, Matriks B24, dan Kontrol Dokumen B26 tidak terpotong; di render LibreOffice semuanya terbaca | Orkestrator, owner |

## Asumsi dan tafsir

1. Tidak ada clear_rows. Prompt memerintahkan clear_rows untuk baris CONTOH, contoh, atau data dummy. Sumber tidak punya baris CONTOH: 15 baris di Register Risiko berwarna biru muda adalah risiko usulan Divisi Operation yang disebut sumber sendiri "bukan baris contoh" (A2) dan berisi fakta SINUX (Zimbra, Nusagrid, AegisWAF, Acronis, ImunifyAV, jumphost). Selain itu ke-15 baris dipetakan 1:1 ke RTP-001 sampai RTP-015 di SNX-ISMS-REG-03 menurut salinan audit. RUNBOOK §6 menyuruh mempertahankan substansi tim. Bila LEAD menilai baris itu data dummy, perubahannya satu baris di patch (`"clear_rows": {"Register Risiko": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}`); akibatnya Ringkasan jadi nol dan REG-03 kehilangan rujukan. Saya tidak melakukannya.
2. "Approval persis" dari prompt mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json.
3. Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
4. Sebutan COO: urutan sheet dipakai untuk menentukan "sebutan pertama" (Kontrol Dokumen, Alur Proses, Daftar, Register Risiko, Matriks Risiko, Ringkasan). Sesudah penggantian B11 dan B38, satu-satunya sebutan COO yang tersisa ada di Matriks Risiko B24.
5. Acuan klausul: B12 "Klausul 6.1" dan B13 "Klausul 6.1.2, 8.2" memuat angka persis dari prompt. Kolom L Register Risiko ("Kontrol Annex A") memakai nomor Annex A, misalnya ISR-009 "5.15, 5.18, 8.2" (8.2 di sini adalah kontrol hak akses istimewa, bukan klausul penilaian risiko); tidak diubah.
6. Pemilik dokumen "ISMS Coordinator" tetap meski penyusun di blok Pengesahan adalah Erik Dwi Yanto: sumber memisahkan keduanya, dan prompt memerintahkan process_owner mengikuti "Pemilik dokumen" sumber.
7. Isi dari lane lain (REG-01, HR-ORG-01, SOP-05, REG-03) dibaca dari repo dan salinan audit, bukan dari Drive terbaru; kutipannya bisa basi bila tim sudah mengubah dokumen itu.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI? Pemeriksaan atas 11 nilai sel berisi teks yang saya tulis atau ubah dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Draf awal F5 memuat "Password manager internal (vault) sudah dipasang, belum live; menunggu konfirmasi Ops" (85 karakter) yang terbaca seperti keterangan berlapis dan terpotong di tinggi baris | Diperpendek jadi "Vault sudah dipasang, belum live; menunggu konfirmasi Ops", memakai istilah D5 |
| Legenda B26 dan A2 bisa terbaca telegrafis | Dipertahankan: kalimat sama gayanya dengan dua butir legenda lain milik tim, satu fakta per kalimat, tanpa penegas atau penutup |
| Parentesis "Direktur (COO)" terbaca seperti glosarium | Dipertahankan karena aturan data_conflicts mewajibkannya pada sebutan pertama |
| Notes ini panjang dan memakai banyak tabel | Dipertahankan: format notes diminta prompt; isi tiap sel tabel membawa fakta atau keputusan yang berbeda dan tidak ada ringkasan penutup |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust), kelompok tiga yang dipaksakan | Tidak ada di nilai patch (pencarian karakter dan pola lint). Notes ini tidak memakai em-dash, en-dash, atau tebal |

Adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.ISMS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di prompt dan defaults.json |
| "Klausul 6.1" dan "Klausul 6.1.2, 8.2" | Prompt (acuan klausul baris ini); B12 dan B13 sumber |
| "Direktur (COO)" | data_conflicts di defaults.json (sebutan Amirull Yusuf Zulkarnain); nama tidak ditulis di sel |
| "menunggu konfirmasi Ops" dan "Vault" di F5 | Aturan vault di prompt dan defaults.json; "sudah dipasang, belum live" dari F5 sumber; "vault" dari D5 sumber |
| "Biru muda: usulan awal Divisi Operation, belum berstatus Disetujui" | A2 Register Risiko ("usulan awal"), B22 Kontrol Dokumen ("Usulan awal Divisi Operation"), warna E7EEF7 dari A26 dan baris 5 sampai 19 |
| Klausa Alur Proses A2 yang tersisa | Sumber A2, tanpa perubahan kata; klausa ketiga dibuang karena gambar tidak memuatnya (image1.png dibuka) |
| 17 sel berubah, 15 risiko, distribusi level, pemilik risiko, tanggal 2027-10-13 | Perbandingan sel dan hitung ulang LibreOffice atas out.xlsx, data sumber G, H, K, O |
| modifiedTime dan fileSize | get_file_metadata atas fileId sumber |
| Rujukan lane lain di notes (12 baris aset dikosongkan, AST-007, AST-002, AST-003, AST-006, K-09, RTP 1:1) | notes/ISMS-REG-01.md, specs/HR-ORG-01.json, salinan audit REG-01 dan REG-03; hanya di notes, tidak di sel |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: tidak muncul di sel yang disunting. Istilah "pemilik risiko" dipertahankan agar sama dengan header kolom Pemilik risiko dan SOP ISMS.
Disunting: Tujuan, Cara pakai 1 sampai 5, dan catatan Register Risiko A2. Legenda dipertahankan (T1).
Cara pakai 5 (usulan awal) ditulis sama persis dengan Cara pakai 5 SNX-ISMS-REG-03 supaya konsisten.
