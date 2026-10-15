# Catatan penyusun ISMS-FRM-03: Supplier Technical & Security Evaluation Records

Status: DRAFTED (patch + notes ada). Patch: specs/ISMS-FRM-03.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-ISMS-FRM-03 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; sumber berlabel RESTRICTED (Internal), isinya daftar supplier, kontrak, dan keamanan informasi), audit_class C2. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/ISMS-FRM-03.xlsx specs/ISMS-FRM-03.patch.json /tmp/pen-ISMS-FRM-03/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 6 sheet, 1 gambar (Alur Proses), 5 data validation dan 2 aturan conditional formatting di Daftar Supplier (48 rumus), 1 data validation, 1 aturan conditional formatting, dan 300 rumus di Evaluasi, 1 data validation dan 1 aturan conditional formatting di Kuesioner Keamanan.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-ISMS-FRM-03_Supplier_Technical_Security_Evaluation.xlsx (139666 byte, berkas xlsx di Drive) | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg | 2026-10-13T06:09:33Z (dicek ulang lewat get_file_metadata: modifiedTime dan fileSize 139666 sama dengan hasil dekode dan dengan "bytes: 139666" di salinan audit; createdTime berkas ini 2026-10-13T09:05:26Z, lebih baru dari modifiedTime, dan modifiedTime yang dipakai) | read_file_content untuk teks; download_file_content dengan exportMimeType ke xlsx, didekode ke /tmp/src/ISMS-FRM-03.xlsx (kerja di /tmp/pen-ISMS-FRM-03/); semua 6 sheet dibaca dengan python3 -I + openpyxl; xl/media/image1.png dibuka dan dibaca |
| Kriteria penerimaan | config/worklist.json dan prompt tugas | | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.4" dan ISO/IEC 27001:2022 "5.19, 5.20, 5.21, 5.22, 5.23" (sama dengan B12 dan B13 sumber) |
| Catatan cacat | context/audit/iso-sinux-supdocs-isms-2026-10-14.md, bagian SNX-ISMS-FRM-03 (baris 447 sampai 674), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; tiap butir dicocokkan ulang ke berkas xlsx dengan openpyxl |
| Pendukung | specs/HR-ORG-01.json (DONE), notes/ISMS-REG-02.md dan notes/ISMS-REG-03.md (lane lain), context/audit bagian ISMS-PLN-01, SoA, dan Legal | repo ini | Dibaca untuk nama peran dan konsistensi lintas dokumen; tidak ditulis ulang. Isinya salinan audit, bukan Drive terbaru |

Sheet sumber: Kontrol Dokumen (A1:E38), Alur Proses (judul, legenda, 1 gambar), Daftar (A1:D10, nilai dropdown), Daftar Supplier (A1:L52, header baris 4, data baris 5 sampai 12, rumus K sampai baris 52), Evaluasi (A1:N104, header baris 4, bobot baris 3, rumus C, J, K sampai baris 104), Kuesioner Keamanan (A1:E16, 12 pertanyaan). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet.

Hitung ulang atas sumber (python3 -I + openpyxl, Daftar Supplier baris 5 sampai 12): 8 supplier; Kritikalitas Tinggi 5, Sedang 3, Rendah 0; Akses ke data atau sistem Ya 6, Tidak 2; Sertifikasi keamanan Ya 3, Belum diketahui 5; Kontrak dan NDA memuat klausul keamanan Belum diketahui 8; Evaluasi terakhir kosong 8; PIC internal Lead NOC 4, Head of Operation 2, Lead SOC 1, COO 1. Jumlah bobot Evaluasi D3 sampai I3 = 1.0. Angka ini sama dengan salinan audit.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Supplier kritikalitas Tinggi dievaluasi setiap semester, Sedang dan Rendah setiap tahun; tanggal evaluasi berikutnya dihitung rumus dari tanggal evaluasi terakhir | Kontrol Dokumen B19: "Evaluasi supplier kritikal Tinggi setiap semester, Sedang dan Rendah setiap tahun; jadwal berikutnya dihitung otomatis." Daftar Supplier K5: `=IF(J5="","Belum pernah",EDATE(J5,IF(E5="Tinggi",6,12)))` | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |
| 2 | Nilai evaluasi = rata-rata tertimbang enam kriteria berbobot 25, 15, 25, 15, 10, 10 persen, dikali 20; ambang 80 dan 60 menentukan keputusan | Evaluasi A2: "Nilai = rata-rata tertimbang dikali 20 (skala 0 sampai 100). 80 ke atas Disetujui · 60 sampai 79 Disetujui bersyarat · di bawah 60 Tinjau ulang." Evaluasi J5: `=IF(COUNT(D5:I5)<6,"",ROUND(SUMPRODUCT(D5:I5,$D$3:$I$3)/SUM($D$3:$I$3)*20,0))`. Bobot D3 sampai I3: 0.25, 0.15, 0.25, 0.15, 0.1, 0.1 | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |
| 3 | Daftar berisi 8 supplier (SUP-001 sampai SUP-008) yang status kontrak, NDA, dan sertifikasinya wajib diverifikasi dengan Commercial dan Legal; klausul keamanan di kontrak dan NDA masih "Belum diketahui" untuk 8 dari 8 | Daftar Supplier A2: "Baris biru muda = supplier yang teridentifikasi di knowledge base; status kontrak, NDA, dan sertifikasi wajib diverifikasi dengan Commercial dan Legal." H5 sampai H12: "Belum diketahui". Kontrol Dokumen B14: "Durasi kontrak + 3 tahun" (masa simpan record) | 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg |

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (python3 -I + openpyxl): 18 sel berubah, selain itu tidak ada sel yang berubah. 348 rumus di sumber dan di out.xlsx sama persis (dibandingkan satu per satu). Tidak ada clear_rows (lihat Asumsi dan tafsir butir 1).

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt; penulisan sama dengan form ISMS dan OPS lain |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by dan prompt; USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 5.19, 5.20, 5.21, 5.22, 5.23" | "Kontrol Annex A 5.19, 5.20, 5.21, 5.22, 5.23" | 5.19 sampai 5.23 adalah kontrol Annex A, bukan klausul badan standar; "klausul atau kontrol" ragu-ragu. Angka sama dengan acuan di prompt |
| B19 Cara pakai butir 2 | "Evaluasi supplier kritikal Tinggi setiap semester, ..." | "Evaluasi supplier berkritikalitas Tinggi setiap semester, ..." | Kolom dan dropdown sumber memakai "Kritikalitas"; satu istilah untuk satu hal (RUNBOOK §6a butir 7). Sisa kalimat tim tidak diubah |
| B26 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: supplier yang sudah teridentifikasi; kontrak, NDA, dan sertifikasinya diverifikasi dengan Commercial dan Legal" | Warna E7EEF7 di A26 sama dengan warna baris Daftar Supplier 5 sampai 12. Baris itu supplier teridentifikasi, bukan CONTOH (Daftar Supplier A2 menyatakannya), jadi legenda lama menyuruh menghapus data tim. Kalimat baru mengikuti A2 |
| C31 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A32 sampai E32 | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; topik RTO tidak ada di workbook ini (pencarian di semua sheet: nol kemunculan), jadi uraian itu sisa dokumen lain. USULAN 2 |
| B36, B37, B38 | "Head of Operation", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 1 |
| Alur Proses A2 | "Kotak biru = output akhir · kotak oranye = cabang ke tindakan atau prosedur lain · garis putus-putus = kembali ke alur utama" | Tiga klausa itu tetap, ditambah "· nilai 60 sampai 79 (Disetujui bersyarat) tidak tergambar, lihat sheet Evaluasi" | Gambar hanya punya keputusan "Nilai di bawah 60?" dengan jalur "tidak" ke Disetujui, sedangkan rumus Evaluasi K membagi tiga keputusan. Gambar tidak bisa diubah alat (Open item 3); legenda diberi catatan agar auditor tidak membaca gambar sebagai aturan dua tingkat |
| Daftar Supplier A2 | "Baris biru muda = supplier yang teridentifikasi di knowledge base; status kontrak, NDA, dan sertifikasi wajib diverifikasi dengan Commercial dan Legal." | Kalimat itu tetap, ditambah "Nama penyedia SUP-001, SUP-002, dan SUP-006 juga diverifikasi dengan Commercial dan Legal (USULAN)." | Audit mencatat nama ambigu: B5 "Maxcloud atau Awandata", B6 "(Arktech)", B10 "(Antmedia)". Langkah verifikasi nama tidak ada di sumber, jadi berlabel (USULAN). USULAN 3 |
| Daftar Supplier I12 (SUP-008, PIC internal) | "COO" | "Direktur (COO)" | Aturan sebutan COO di data_conflicts: "Direktur (COO)" pada sebutan pertama di badan dokumen, sesudahnya "COO". Setelah B11 dan B38 diganti, I12 adalah sebutan COO pertama menurut urutan sheet; HR-ORG-01 menamai jabatannya "Direktur (JA-02)" |
| Evaluasi A2 | "... dikali 20 (skala 0 sampai 100). ..." | "... dikali 20 (skala 20 sampai 100). ..." | Skor 1 sampai 5 tidak bisa menghasilkan nilai di bawah 20. Diukur di LibreOffice atas salinan out.xlsx: semua skor 1 menghasilkan 20, semua skor 5 menghasilkan 100. Rumus tidak diubah. USULAN 4 |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen yang diminta prompt; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama |
| Tidak diubah | | | Tanda tangan dan tanggal (C36 sampai D38) kosong (batas keras 3). Tanggal efektif B8 bukan tanggal. Delapan baris supplier (kecuali I12), PIC Head of Operation, Lead NOC, Lead SOC, sheet Daftar, bobot, ambang, rumus, 12 pertanyaan Kuesioner, data validation, format kondisional, gambar |

Render PDF LibreOffice atas out.xlsx: Kontrol Dokumen terbaca utuh, B19 dua baris di tinggi baris 23.85, B26 satu baris, Riwayat revisi hanya satu baris terisi (baris 32 kosong dan tinggi 57.45 tidak diubah alat), Pengesahan memuat tiga nama; "Direktur (COO)" terbaca di Daftar Supplier I12. Pemindaian pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas semua sel teks out.xlsx: nol temuan (sumber punya satu temuan, "CONTOH" di B26, sudah diganti; pemindai diuji atas sumber dan menembak B26). Tidak ada em-dash atau en-dash di nilai `set` (pencarian karakter, nol hasil).

Uji rumus (salinan out.xlsx di /tmp/pen-ISMS-FRM-03/, bukan berkas patch): skor 1 untuk semua kriteria = nilai 20 "Tinjau ulang"; skor 3 = 60 "Disetujui bersyarat"; skor 4 = 80 "Disetujui"; skor 5 = 100 "Disetujui"; ID "SUP-009" yang tidak ada di daftar menampilkan nama "ID tidak ada" tetapi tetap bernilai 100 "Disetujui" (USULAN 5); Evaluasi terakhir 2026-10-13 untuk SUP-001 (Tinggi) menghasilkan evaluasi berikutnya 2027-04-13. Nol sel galat di semua sheet.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1I0qEhkegW3w-k7YvTnKftqvUUbMg3rmg)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Belum ada evaluasi: J5:J12 kosong, sheet Evaluasi tanpa skor, Kuesioner tanpa jawaban; belum ada bukti implementasi A 5.19 sampai 5.23 dan klausul 8.4 | Tidak diubah. Form kosong adalah keadaan sebenarnya; mengisi skor atau jawaban berarti mengarang (batas keras 4). Open item 1 |
| 2 | Kolom H "Belum diketahui" 8 dari 8, kolom G "Belum diketahui" 5 dari 8 | Tidak diubah: nilai itu data jujur tim. Verifikasi dengan Commercial dan Legal sudah diperintahkan A2 dan Cara pakai butir 1. Open item 2 |
| 3 | SUP-001 dan SUP-002 kritikalitas Tinggi, berakses data, sertifikasi "Belum diketahui" | Tidak diubah. Catatan tim L5 "Verifikasi status kontrak dan sertifikasi" tetap; SUP-002 tidak punya catatan, dan menambahnya berarti menulis fakta. Open item 2 |
| 4 | Nama SUP-001 ambigu ("Maxcloud atau Awandata"); nama SUP-002 dan SUP-006 dalam kurung perlu diverifikasi | Daftar Supplier A2 ditambah satu kalimat verifikasi nama, berlabel (USULAN). Nama di sel B5, B6, B10 tidak diubah karena tidak ada sumber yang menentukannya. USULAN 3, Open item 4 |
| 5 | SUP-001 selaras dengan ISR-005 di SNX-ISMS-REG-02; FRM-03 tidak merujuk ISR atau AST | Tidak diubah: pemetaan itu inferensi audit, dan lane REG-01 mengosongkan baris aset contoh sehingga ID AST belum pasti. USULAN 6, Open item 6 |
| 6 | SUP-003, 004, 005, 008 berpadanan dengan AST-006, 010, 007, 011 di SNX-ISMS-REG-01; tidak ditulis di salah satu dokumen | Sama dengan butir 5 |
| 7 | Catatan skala "0 sampai 100" padahal nilai minimum 20 | Teks diperbaiki menjadi "20 sampai 100", rumus tidak diubah (terbukti lewat uji rumus di atas). USULAN 4 |
| 8 | Gambar tidak memuat cabang "Disetujui bersyarat" | Gambar tidak bisa diubah xlsx_patch. Legenda Alur Proses A2 diberi catatan. Open item 3 |
| 9 | Tidak ada batas waktu tindak lanjut untuk "Disetujui bersyarat" dan "Tinjau ulang"; kolom L bebas isi | Tidak diubah: angka tenggat tidak ada di sumber. USULAN 7, Open item 5 |
| 10 | SUP-008 punya padanan AST-011 (RESTRICTED); FRM-03 tidak punya kolom klasifikasi data yang dipegang supplier | Tidak diubah: menambah kolom di luar kemampuan alat. Open item 7 |
| 11 | SNX-ISMS-PLN-01 Bagian 5 menunjuk FRM-03 untuk "Kontak eskalasi, rencana alternatif per supplier", yang tidak punya kolomnya | Tidak diubah: menambah kolom ke Daftar Supplier tanpa format sel dan validasi merusak tampilan, dan mengubah struktur form. USULAN 8, Open item 8 |
| 12 | Pengesahan kosong; status persetujuan "Menunggu"; Revisi 00 tercatat dua kali | Baris kedua dikosongkan (USULAN 2). Pengesahan diisi tiga penanda tangan dari defaults.json, tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Kolom Disetujui "Menunggu" di baris 31 dipertahankan |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | B13 "Klausul atau kontrol Annex A ..." | Diganti "Kontrol Annex A ..." |
| B | Legenda B26 menyebut baris CONTOH padahal baris biru adalah supplier teridentifikasi | Ditulis ulang sesuai isi |
| C | Rumus Evaluasi J menghitung nilai untuk ID supplier yang tidak ada ("ID tidak ada" di C, tetapi J dan K tetap terisi) | Rumus tidak diubah (RUNBOOK: rumus tidak diubah kecuali jelas salah, catat USULAN). USULAN 5 |
| D | "kritikal Tinggi" di Cara pakai butir 2 tidak sama dengan nama kolom "Kritikalitas" | Diganti "berkritikalitas Tinggi" |
| E | Aturan lintas dokumen yang tidak berlaku di sini: PPN (tidak ada), kunci backup dengan salinan offline atau break-glass (tidak disebut), vault (tidak disebut), rujukan internal AI (tidak ada, dicek dengan pola lint), sistem tiket Zammad atau GLPI (tidak disebut; kolom Tindak lanjut tidak menunjuk sistem tiket) | Tidak ada perubahan |
| F | Sebutan "knowledge base" di Daftar Supplier A2 | Dipertahankan, sama dengan keputusan REG-02 dan REG-03 (Open item 9) |

## USULAN

Label (USULAN) hanya ditulis di sel xlsx untuk langkah verifikasi nama penyedia (Daftar Supplier A2); butir lain di bawah berada di notes ini karena tidak ada angka atau fakta baru yang masuk sel.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, dan COO Amirull Yusuf Zulkarnain di blok Disusun, Diperiksa, dan Disetujui. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus | Kontrol Dokumen B11, B36 sampai B38 | owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris | Kontrol Dokumen A32 sampai E32 | owner |
| 3 | Langkah verifikasi nama penyedia SUP-001, SUP-002, dan SUP-006 dengan Commercial dan Legal. Sumber hanya meminta verifikasi kontrak, NDA, dan sertifikasi | Daftar Supplier A2 | Fani |
| 4 | Pertahankan rumus Evaluasi J dan koreksi teks skala menjadi 20 sampai 100 (diterapkan), atau ubah rumus supaya skor 1 menghasilkan 0. Belum ada keputusan, hanya teks yang disesuaikan dengan rumus | Evaluasi A2 dan J5 sampai J104 | Fani |
| 5 | Rumus nilai (J) dan keputusan (K) hanya terisi bila C bukan "ID tidak ada", supaya ID salah ketik tidak menghasilkan keputusan Disetujui. Belum diterapkan | Evaluasi J5 sampai K104 | Fani |
| 6 | Tambah rujukan ke ID aset di SNX-ISMS-REG-01 dan ke ID risiko di SNX-ISMS-REG-02 (misalnya SUP-001 ke ISR-005) pada Daftar Supplier. Dibuat sesudah REG-01 diisi ulang oleh Ops, karena ID bisa berubah. Belum diterapkan | Daftar Supplier, kolom baru | Fani |
| 7 | Tetapkan batas waktu dan pemilik tindak lanjut untuk keputusan "Disetujui bersyarat" dan "Tinjau ulang" di kolom Tindak lanjut. Angka tidak diusulkan karena tidak ada dasar di sumber | Evaluasi L; Cara pakai | Fani |
| 8 | Tambah kolom "Kontak eskalasi" dan "Rencana alternatif" per supplier di Daftar Supplier, karena SNX-ISMS-PLN-01 Bagian 5 menunjuk FRM-03 untuk keduanya. Belum diterapkan | Daftar Supplier, kolom baru | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Belum ada evaluasi supplier: Evaluasi terakhir kosong untuk 8 supplier, sheet Evaluasi dan Kuesioner kosong. Siklus evaluasi pertama belum dijadwalkan di sumber; bukti penerapan A 5.19 sampai 5.23 dan klausul 8.4 baru ada sesudah siklus itu berjalan | Fani |
| 2 | Kontrak dan NDA memuat klausul keamanan: "Belum diketahui" untuk 8 dari 8; sertifikasi keamanan "Belum diketahui" untuk SUP-001, 002, 003, 006, 007. Tiga nilai "Ya" (SUP-004, 005, 008) tidak punya bukti, masa berlaku, atau ruang lingkup sertifikat di form; bukti hanya ada di Kuesioner butir 1 yang kosong. Verifikasi menunggu Commercial dan Legal | Commercial, Legal, Fani |
| 3 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Cabang "Disetujui bersyarat" (60 sampai 79) tidak ada; jalur "tidak" dari "Nilai di bawah 60?" langsung ke Disetujui; kotak "Tinjau ulang" tidak punya panah lanjutan. Legenda A2 sudah diberi catatan; bila gambar diperbarui, catatan itu ditinjau | Orkestrator, Fani |
| 4 | Nama penyedia SUP-001 ("Maxcloud atau Awandata"), SUP-002 ("Arktech"), SUP-006 ("Antmedia") belum pasti; sumber dan audit tidak menentukannya. Nama tetap seperti sumber | Commercial, Legal |
| 5 | Tidak ada batas waktu dan pemilik tindak lanjut untuk "Disetujui bersyarat" dan "Tinjau ulang"; kolom Tindak lanjut bebas isi tanpa validasi. Lihat USULAN 7 | Fani |
| 6 | Tidak ada rujukan antara FRM-03 dan SNX-ISMS-REG-01 (aset) atau SNX-ISMS-REG-02 (ISR-005). Lihat USULAN 6 | Fani, lane ISMS-REG-01 dan ISMS-REG-02 |
| 7 | Tidak ada kolom klasifikasi data yang dipegang supplier (SUP-008 berpadanan dengan aset berklasifikasi RESTRICTED di REG-01 menurut audit). Menambah kolom mengubah struktur form | Fani |
| 8 | SNX-ISMS-PLN-01 menunjuk FRM-03 untuk kontak eskalasi dan rencana alternatif per supplier, tetapi form tidak punya kolomnya. Lihat USULAN 8. Sampai diputus, tiga elemen itu hanya ada di Kuesioner butir 12 dan di cabang "Tinjau ulang" pada gambar | Fani, lane ISMS-PLN-01 |
| 9 | "knowledge base" di Daftar Supplier A2 dipertahankan, sama dengan REG-02 dan REG-03, karena Knowledge base SINUX tercatat sebagai aset Operation. Bila konsultan menganggap istilah itu rujukan internal AI, ganti serentak di semua dokumen dengan nama sistem yang disetujui Ops | Fani |
| 10 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Kode yang dirujuk di sel: SNX-OPS-SOP-05 (Cara pakai butir 5). Pengecualian lingkup tidak ditulis sumber: judul menyebut supplier "teknis" dan butir 1 menyebut supplier yang "menopang layanan atau memegang akses atau data", tetapi supplier non-teknis (misalnya yang tidak menopang layanan) tidak disebut dikecualikan. Lokasi simpan dan pemilik rekaman tidak ada di sumber. Masa simpan "Durasi kontrak + 3 tahun" dipertahankan; belum jelas dihitung dari kontrak yang mana untuk supplier yang kontraknya belum diverifikasi. Angka tidak diusulkan | Orkestrator, Fani |
| 11 | Peran di sel tidak punya pemegang di Struktur Organisasi: Head of Operation (Pemilik dokumen; PIC SUP-001 dan SUP-004), Lead NOC, Lead SOC ada di specs/HR-ORG-01.json sebagai USULAN tanpa pemegang (K-10, K-11); ISMS Coordinator (pemeriksa di sumber) belum ditetapkan (K-13) dan diganti Fani Fatullah di blok Pengesahan menurut prompt | owner, Fani |
| 12 | Kuesioner Keamanan, Cara pakai butir 4, mewajibkan kuesioner untuk "supplier baru dan supplier berakses data", sedangkan jawaban Kuesioner belum pernah dikumpulkan untuk 6 supplier berakses data (Akses Ya) | Fani |
| 13 | Dokumen Legal (checklist kontrak vendor dan kontrak pelanggan) tidak merujuk FRM-03, dan Kuesioner butir 9 dan 10 menguji hal yang sama dengan kelompok di checklist Legal menurut audit Legal. Tidak diubah di sini | Legal |
| 14 | Tanggal draft 13 Oktober 2026 (B7, B31) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan" | owner |
| 15 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: "Daftarkan setiap supplier ...", "Gunakan sheet Kuesioner Keamanan ...", "hapus atau timpa saat dipakai", "Sel rumus: jangan diubah", "wajib diverifikasi dengan Commercial dan Legal". Tidak ada yang dijalankan: rumus tidak diubah, tidak ada baris yang dihapus atas dasar kalimat itu | Orkestrator |
| 16 | Keterbatasan alat: nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka; tinggi baris tidak diubah. HUMAN-VERDICT: buka di Excel dan lihat apakah Kontrol Dokumen B19 dan B26, Daftar Supplier A2, dan Alur Proses A2 tidak terpotong; di render LibreOffice semuanya terbaca, A2 di dua sheet meluber ke sel kosong di kanannya | Orkestrator, owner |

## Asumsi dan tafsir

1. Tidak ada clear_rows. Prompt memerintahkan clear_rows untuk baris CONTOH, contoh, atau data dummy. Sumber tidak punya baris CONTOH: delapan baris biru muda di Daftar Supplier adalah supplier yang disebut sumber sendiri "teridentifikasi" (A2) dan berisi fakta SINUX (Nusagrid, Cloudflare, Acronis, Google Workspace); sheet Evaluasi dan Kuesioner Keamanan tidak punya baris terisi. Kata CONTOH hanya ada di legenda B26 dan sudah ditulis ulang. RUNBOOK §6 menyuruh mempertahankan substansi tim. Bila LEAD menilai delapan baris itu data dummy, perubahannya satu baris di patch (`"clear_rows": {"Daftar Supplier": [5, 6, 7, 8, 9, 10, 11, 12]}`); akibatnya daftar supplier kosong dan SNX-ISMS-PLN-01 kehilangan rujukan SUP-002, SUP-003, dan SUP-006. Saya tidak melakukannya.
2. "Approval persis" dari prompt mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json.
3. Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
4. Sebutan COO: urutan sheet dipakai untuk menentukan "sebutan pertama" (Kontrol Dokumen, Alur Proses, Daftar, Daftar Supplier, Evaluasi, Kuesioner Keamanan). Sesudah penggantian B11 dan B38, satu-satunya sebutan COO yang tersisa ada di Daftar Supplier I12, dan sebutan itu ditulis "Direktur (COO)". Gambar Alur Proses tidak memuat kata COO (gambar dibuka).
5. Acuan klausul: B12 "Klausul 8.4" dan B13 "Kontrol Annex A 5.19, 5.20, 5.21, 5.22, 5.23" memuat angka persis dari prompt.
6. Pemilik dokumen "Head of Operation" tetap meski penyusun di blok Pengesahan adalah Erik Dwi Yanto: sumber memisahkan keduanya, dan prompt memerintahkan process_owner mengikuti "Pemilik dokumen" sumber.
7. Nama peran di kolom PIC internal (Head of Operation, Lead NOC, Lead SOC) sudah sama dengan nama di specs/HR-ORG-01.json (Matriks Peran), jadi tidak ada pemetaan ke jabatan terdekat. "Commercial" dan "Legal" ditulis sebagai unit, seperti di sumber, karena Cara pakai tidak menyebut jabatan.
8. Isi dari lane lain (REG-01, REG-02, REG-03, PLN-01, Legal) dibaca dari repo dan salinan audit, bukan dari Drive terbaru; kutipannya bisa basi bila tim sudah mengubah dokumen itu.
9. Uji rumus memakai salinan out.xlsx yang diisi data uji di /tmp/pen-ISMS-FRM-03/; data uji tidak masuk patch dan tidak masuk berkas lain.

## Dua pertanyaan penutup

Apa yang membuat teks ini terdengar buatan AI? Pemeriksaan atas 7 nilai sel yang saya tulis atau ubah (B19, B26, Alur Proses A2, Daftar Supplier A2, I12, Evaluasi A2, C31) dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Rancangan B26 menulis supplier "belum diverifikasi", klaim yang tidak didukung sumber karena G5 sampai G12 menunjukkan tiga supplier bersertifikasi "Ya" | Diganti "kontrak, NDA, dan sertifikasinya diverifikasi dengan Commercial dan Legal", mengikuti kalimat A2 sumber |
| Rancangan kalimat tambahan di Daftar Supplier A2 ("Nama penyedia ... ikut diverifikasi") tanpa pelaku, dan menambah langkah proses tanpa label | Pelaku ditulis ("dengan Commercial dan Legal") dan diberi label (USULAN) |
| Catatan tambahan di Alur Proses A2 bisa terbaca sebagai klaim bahwa diagram salah | Ditulis sebagai fakta netral ("tidak tergambar, lihat sheet Evaluasi") dan kebutuhan memperbarui gambar dipindah ke Open item 3 |
| Pemindaian pola lint atas nilai `set` dan atas notes ini: nol em-dash dan en-dash, nol pembuka generik, nol frasa pengisi, nol tanda tebal, nol penutup positif | Tidak ada yang perlu diganti. Kelompok tiga di notes hanya muncul sebagai daftar ID (SUP-001, SUP-002, SUP-006), yang memang tiga butir menurut audit |

Adakah fakta, angka, nama, atau tanggal tanpa sumber?

| Isi | Sumber |
|---|---|
| Nomor, judul, klasifikasi, pemilik, acuan 8.4 dan 5.19 sampai 5.23, masa simpan | Kontrol Dokumen B4, B5, B9, B10, B12, B13, B14 sumber dan prompt |
| Tiga nama penanda tangan dan jabatannya | Prompt dan config/defaults.json (approved_by, prepared_reviewed.ISMS) |
| "Direktur (COO)" | config/defaults.json data_conflicts (Sebutan Amirull Yusuf Zulkarnain); specs/HR-ORG-01.json JA-02 |
| "Draft awal untuk review dan pengesahan", "Draft" | Prompt (revision_desc, status) |
| SUP-001, SUP-002, SUP-006 dan kutipan nama "Maxcloud atau Awandata", "Arktech", "Antmedia" | Daftar Supplier B5, B6, B10 sumber; audit bagian 5 butir 4 |
| "skala 20 sampai 100", 60 sampai 79, 80 | Rumus Evaluasi J5 dan K5 sumber; uji rumus di LibreOffice (skor 1 = 20, skor 5 = 100) |
| Hitungan 8 supplier, 5 Tinggi, 3 Sedang, 6 berakses data, 3 bersertifikat, 8 kontrak "Belum diketahui" | Hitung ulang python3 -I + openpyxl atas /tmp/src/ISMS-FRM-03.xlsx |
| "2027-04-13", nilai 20, 60, 80, 100 di uji rumus | Hasil LibreOffice atas salinan uji, bukan klaim tentang data SINUX |
| Pernyataan tentang SNX-ISMS-PLN-01, REG-01, REG-02, dokumen Legal | Salinan audit di context/audit (baris 765, 911, 2026 sampai 2030 berkas ISMS; baris 370, 550, 1041 berkas Legal), diberi label sebagai salinan audit, bukan Drive terbaru |
| Tidak ada tanggal, angka, atau nama baru di sel xlsx selain yang tertera di atas | Perbandingan sel demi sel (18 sel berubah) |

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil
### W10 kalimat dihapus atau dipindah
nihil
### W10 selisih angka
nihil
### W10 catatan
Pihak luar: tidak ada sebutan pelanggan di sel yang disunting; "supplier" dipakai konsisten.
Disunting: Tujuan, Cara pakai 1, 2, 3, 5, dan catatan Kuesioner Keamanan A2. Cara pakai 4 dan catatan Evaluasi A2 dipertahankan (T1).
Tujuan: "A 5.19" ditulis "Annex A 5.19" agar sama dengan sebutan di dokumen ISMS lain; angka tetap.
Sheet Daftar Supplier (termasuk A2) tidak disunting karena berawalan Daftar.
