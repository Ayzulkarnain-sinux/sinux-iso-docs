# Catatan penyusun OPS-RPT-01: Operations KPI & Performance Monitoring Report

Status: DRAFTED (patch + notes ada). Patch: specs/OPS-RPT-01.patch.json. Mode xlsx, aksi T1, wave W5, nomor SNX-OPS-RPT-01 (nomor lama dipertahankan), department Operation, classification RESTRICTED (Internal) mengikuti label sumber (worklist null; sel B9 sumber sudah menulis label itu), audit_class C1. Uji terakhir: `python3 -I tools/xlsx_patch.py /tmp/src/OPS-RPT-01.xlsx specs/OPS-RPT-01.patch.json /tmp/pen-OPS-RPT-01/out.xlsx` memberi `"pass": true`, `"fails": []`. Fitur sebelum dan sesudah sama: 4 sheet, 1 gambar (Alur Proses), 2 rentang conditional formatting dan 52 rumus di sheet KPI.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-RPT-01_Operations_KPI_Performance_Report.xlsx (110990 byte, berkas xlsx di Drive) | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO | 2026-10-13T06:09:47Z (dicek ulang lewat get_file_metadata: modifiedTime dan fileSize 110990 sama dengan prompt dan salinan audit) | read_file_content (teks), download_file_content (didekode ke /tmp/src/OPS-RPT-01.xlsx, 110990 byte; kerja di /tmp/pen-OPS-RPT-01/; 4 sheet dibaca dengan python3 -I + openpyxl; xl/media/image1.png dibuka) |
| Kriteria penerimaan | config/worklist.json baris OPS-RPT-01 | | Kolom Description hanya nama berkas, jadi kriteria = substansi sumber tim + acuan ISO 9001:2015 "9.1, 9.3.2" dan ISO/IEC 27001:2022 "9.1" dari prompt |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md, bagian SNX-OPS-RPT-01 (baris 3389 sampai 3592), bagian 5 Catatan kualitas dan celah | salinan audit 13 sampai 14 Okt | Dibaca sebagai DATA; butir yang menyangkut isi berkas dicocokkan ulang ke xlsx dengan openpyxl |
| Pendukung | notes/OPS-FRM-08.md, notes/OPS-FRM-04.md, specs/HR-ORG-01.json (K-09), context/audit bagian SNX-ISMS-REG-03 | repo kerja, bukan Drive | Dipakai hanya untuk memeriksa konsistensi lintas dokumen; kutipan bisa basi bila tim mengubah dokumen itu |

Sheet sumber: Kontrol Dokumen (A1:E38), Alur Proses (judul, legenda, 1 gambar), KPI (A1:U24, 17 baris KPI di baris 6 sampai 22), Narasi Bulanan (A1:B16, 14 label). Sheet "Kontrol Dokumen" ada, jadi patch dibuat sesuai RUNBOOK §7 mode xlsx tanpa menambah sheet. Tidak ada sheet "Daftar" dan tidak ada data validation.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Workbook ini adalah laporan bulanan KPI dan kinerja Divisi Operation, dipakai sebagai masukan pemantauan klausul 9.1 dan tinjauan manajemen klausul 9.3.2 | Kontrol Dokumen B15: "Laporan bulanan KPI dan kinerja Divisi Operation, masukan pemantauan klausul 9.1 dan tinjauan manajemen klausul 9.3.2." | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |
| 2 | Sheet KPI memuat 17 KPI (NOC 6, SOC 4, SD dan PM 4, ISMS 2, Semua 1), masing-masing dengan arah, target, dan sumber data; status dihitung dari bulan terakhir yang terisi, bukan dari rata-rata YTD | KPI C6: "Availability layanan yang dikelola", D6: "≥", E6: 0.999, F6: "SNX-OPS-FRM-09". KPI U6: `=IF(T6="","Belum diukur",IF(D6="≥",IF(T6>=E6,"Tercapai","Di bawah target"),IF(T6<=E6,"Tercapai","Di bawah target")))`. T6: `=IF(COUNT(G6:R6)=0,"",LOOKUP(2,1/(G6:R6<>""),G6:R6))` | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |
| 3 | Nilai aktual diisi setiap awal bulan untuk bulan sebelumnya; target adalah target awal yang dikalibrasi setelah 3 bulan data; masa simpan record 3 tahun; pemilik dokumen Head of Operation | Kontrol Dokumen B19: "Setiap awal bulan, isi nilai aktual bulan sebelumnya dari sumber data di kolom Sumber. Persentase ditulis sebagai pecahan (0.95 = 95%)." B22: "Target adalah target awal dan dikalibrasi setelah 3 bulan data." B14: "3 tahun". B10: "Head of Operation" | 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO |

Fakta pendukung yang tidak diubah: B2 "PT Strategi Integrasi Nusantara (SINUX) · Divisi Operation"; B7 "13 Oktober 2026" (tanggal draft tim); B8 "Ditetapkan saat pengesahan"; B9 "RESTRICTED (Internal)"; B12 "Klausul 9.1, 9.3.2"; KPI B3 = 2027; seluruh 17 baris KPI (nama, arah, target, sumber) dan rumus S, T, U, U24; Narasi Bulanan A1 sampai A16 kecuali A9. Sel nilai bulanan G6:R22 kosong semua (dicek: 0 sel terisi), jadi workbook ini template tanpa data realisasi.

## 2. Isi patch (apa yang diubah dan kenapa)

Daftar sel berasal dari pembandingan sumber dan out.xlsx sel demi sel (script openpyxl, python3 -I): 15 sel berubah, tidak ada yang lain.

| Sel | Sebelum | Sesudah | Dasar |
|---|---|---|---|
| clear_rows | tidak ada | `{}` (kosong) | Tidak ada baris CONTOH atau data dummy. Pemeriksaan semua sel sumber dengan pola contoh/CONTOH (tak peka huruf): hanya legenda B26 yang memuatnya. Sheet KPI berisi 17 definisi KPI nyata dari tim, bukan baris contoh, dan G6:R22 sudah kosong. Mengosongkan salah satunya akan menghapus substansi tim |
| Kontrol Dokumen B6 | "00 (DRAFT)" | "00 (Draft)" | Revisi "00" dan status "Draft" dari prompt; penulisan sama dengan form OPS lain |
| B11 Disetujui oleh | "COO, Amirull Yusuf Zulkarnain" | "Samuel Kristanto Utomo / President Director" | config/defaults.json approved_by; USULAN 1 |
| B13 Acuan ISO/IEC 27001:2022 | "Klausul atau kontrol Annex A 9.1" | "Klausul 9.1" | Prompt menetapkan acuan 9.1. 9.1 adalah klausul utama ISO/IEC 27001:2022 (pemantauan, pengukuran, analisis, evaluasi), bukan kontrol Annex A; "klausul atau kontrol" ragu-ragu. Angka sama dengan sumber |
| B21 Cara pakai 4 | "Isi sheet Narasi Bulanan sebagai ringkasan untuk COO dan bahan tinjauan manajemen." | "Isi sheet Narasi Bulanan sebagai ringkasan untuk Direktur (COO) dan bahan tinjauan manajemen." | data_conflicts: sebutan pertama COO di badan dokumen = "Direktur (COO)". Sesudah B11 dan B38 diganti, B21 adalah sebutan pertama berurutan sheet. Sebutan berikutnya (Narasi Bulanan A1 dan A16) tetap "COO" |
| B26 legenda | "Baris CONTOH: hapus atau timpa saat dipakai" | "Biru muda: tidak dipakai, tidak ada baris contoh" | RUNBOOK §0 butir 29: legenda baris CONTOH ditulis ulang. Kalimat sibling ("sudah dikosongkan") tidak dipakai karena di workbook ini baris contoh memang tidak pernah ada. Kotak A26 tetap biru (alat tidak mengubah warna di luar clear_rows) |
| C31 Uraian perubahan | "Draft awal untuk sertifikasi ISO 9001 dan ISO/IEC 27001" | "Draft awal untuk review dan pengesahan" | revision_desc dari prompt |
| A32 sampai E32 | Baris riwayat kedua: 00, 13 Oktober 2026, "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih", Divisi Operation, Menunggu | Dikosongkan | Dua baris Revisi 00 bertanggal sama; RTO dan target pulih tidak ada di workbook ini (pencarian semua sel: nol kemunculan). USULAN 2 |
| B36, B37, B38 | "Head of Operation", "ISO/ISMS Coordinator", "COO, Amirull Yusuf Zulkarnain" | "Erik Dwi Yanto / Technical/Operation Engineer L1", "Fani Fatullah / VP Tech Operation and Services", "Samuel Kristanto Utomo / President Director" | Approval persis dari prompt dan defaults.json. USULAN 1 |
| Narasi Bulanan A9 | "Status risiko keamanan informasi (perubahan level, RTP terlambat)" | "Status risiko keamanan informasi (perubahan level, Risk Treatment Plan terlambat)" | Singkatan RTP tidak dijabarkan di workbook. Di salinan audit SNX-ISMS-REG-03 baris Rencana Penanganan bernomor RTP-001 dan seterusnya, dan diagram REG-03 berjudul "Alur Information Security Risk Treatment Plan". USULAN 10 |
| B4, B5, B9, B10, B12, B14 | sudah sama dengan nilai yang diminta | Ditulis ulang dengan nilai yang sama | Supaya spec memuat seluruh medan Kontrol Dokumen yang diminta prompt; tidak mengubah isi sel. B10 mengikuti "Pemilik dokumen" sumber, jabatan tanpa nama |
| Tidak diubah | | | Tanda tangan dan tanggal (C36 sampai D38) kosong; tanggal efektif tetap "Ditetapkan saat pengesahan"; B7 dan B31 (13 Oktober 2026) tanggal tim; rumus S, T, U, U24 dan format kondisional; nama KPI, arah, target, sumber; gambar Alur Proses |

Pemeriksaan atas out.xlsx: pola FORBIDDEN dan STYLE dari tools/lint_doc.py atas 172 sel teks: nol temuan. Tidak ada em-dash atau en-dash (pencarian karakter). Konversi PDF lewat soffice berhasil (7 halaman); halaman 1 dilihat: B21 dua baris, B26 satu baris, riwayat revisi satu baris terisi, tiga nama di Pengesahan terbaca. Hitung ulang LibreOffice: 17 sel "Belum diukur" dan baris "KPI tercapai (bulan terakhir)" ada.

## 3. Penanganan cacat context/audit (bagian 5 Catatan kualitas dan celah, fileId 1rSuMH8wK5BTGUHLm8KjGig1LZOKWcECO)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, pengesahan kosong, tahun 2027, nilai bulanan kosong | Tiga penanda tangan diisi dari defaults.json; tanda tangan dan tanggal dibiarkan kosong (batas keras 3). Nilai bulanan kosong memang keadaan template, tidak diubah. B3 = 2027 tidak diubah (open item 6) |
| 2 | Tidak ada kolom definisi, rumus indikator (numerator dan denominator), frekuensi, pemilik per KPI | Tidak diperbaiki: alat tidak menambah kolom atau sheet, dan mengarang rumus tanpa sumber melanggar batas keras 4. Frekuensi bulanan sudah tertulis di Cara pakai butir 2. USULAN 4 |
| 3 | Target tidak berlabel USULAN; Cara pakai butir 5 saja yang menyebut target awal | Butir 5 dipertahankan (kalimat tim jelas, T1). Sel target numerik tidak diberi label. Pengesahan target dicatat sebagai USULAN 3 |
| 4 | Acuan ISO/IEC 27001 "Annex A 9.1" tidak ada di Annex A edisi 2022 | Diperbaiki: B13 menjadi "Klausul 9.1" |
| 5 | KPI 6 "Change tanpa rollback darurat" memakai kolom FRM-04 yang rumusnya berlaku untuk semua jenis change | Tidak diubah: mengganti nama KPI atau rumus FRM-04 adalah keputusan substansi. USULAN 5 |
| 6 | Data KPI 14 (RCA dalam 2 hari kerja) tidak bisa dihitung dari FRM-08 | Tidak ada perubahan di workbook ini. Kolom tanggal kirim RCA sudah menjadi USULAN 8 di notes/OPS-FRM-08.md. Open item 3 |
| 7 | "Shift Log", "Tiket vulnerability", dan "SIEM" tanpa nomor dokumen | Tidak diubah: nomor dokumen baru tidak boleh dikarang. Open item 2 |
| 8 | KPI 10 (arah ≤, target 0, hitungan) dirata-rata dengan rumus persentase | Rumus tidak diubah (legenda sumber: sel rumus jangan diubah; sumber tidak jelas salah). USULAN 6 |
| 9 | KPI 15 triwulanan di kolom bulanan tanpa aturan bulan tanpa kegiatan; status memakai bulan terisi terakhir | Tidak diubah: aturan pengisian baru tidak ada di sumber. USULAN 7 |
| 10 | Tidak ada KPI untuk pemulihan tiket, UAT atau kualitas, dan response SLA selain Ack P1 dan P2 | Tidak ditambah: baris KPI baru butuh target dari tim. USULAN 8 |
| 11 | "SD dan PM" tidak dijabarkan | Tidak diubah: sumber tidak memberi penjabaran, dan HR-ORG-01 memakai singkatan yang sama. USULAN 9 |
| 12 | Tidak ada kredensial atau data pribadi | Dikonfirmasi ulang atas out.xlsx: nama orang hanya di blok Disetujui oleh dan Pengesahan dari defaults.json; pola kredensial lint: nol temuan |

Cacat tambahan di luar bagian 5 audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | Narasi Bulanan A9 memakai "RTP" tanpa penjabaran | Dijabarkan menjadi "Risk Treatment Plan" (lihat bagian 2). USULAN 10 |
| B | Legenda B26 menyuruh menghapus baris CONTOH yang tidak ada | Ditulis ulang |
| C | Riwayat revisi punya dua baris Revisi 00 bertanggal sama; baris kedua menyebut RTO yang tidak ada di workbook | Baris kedua dikosongkan; teks asli dicatat di bagian 2. USULAN 2 |
| D | Gambar Alur Proses menulis "FRM-01 sampai FRM-09, register" sebagai sumber data, sedangkan KPI 14 bersumber SNX-OPS-FRM-10 | Gambar tidak bisa diubah lewat xlsx_patch. Open item 1 |
| E | Sebutan COO di B21 | "Direktur (COO)" pada sebutan pertama |

## USULAN

Label (USULAN) tidak ditulis di sel xlsx karena sel yang berubah tidak memuat angka atau fakta baru; semua butir di bawah berada di notes ini.

| # | USULAN | Di mana | Pemutus yang disarankan |
|---|---|---|---|
| 1 | Tiga penanda tangan (Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo) menggantikan Head of Operation, ISO/ISMS Coordinator, COO di sumber. Semua baris penanda tangan USULAN di Master List menurut defaults.json; pembalik: form operasional disetujui COO bila owner memutus. Diterapkan | Kontrol Dokumen B11, B36 sampai B38 | Owner (Samuel untuk persetujuannya sendiri) |
| 2 | Baris riwayat revisi kedua dikosongkan; Revisi 00 cukup satu baris. Diterapkan | Kontrol Dokumen A32 sampai E32 | Owner |
| 3 | Target 17 KPI diperlakukan sebagai usulan awal sampai disahkan. Salinan audit mencatat butir 2 di Keputusan dan Gap SNX-OPS-ML-00 ("Sahkan target berlabel USULAN") tanpa menyebut target KPI. Belum diterapkan | KPI E6:E22, Cara pakai butir 5 | Fani |
| 4 | Definisi operasional per KPI (rumus numerator dan denominator, frekuensi, pemilik KPI) sebagai kolom atau sheet baru. Kolom "Rumus indikator" di salinan audit adalah inferensi, bukan isi sumber. Belum diterapkan | KPI sheet atau sheet baru | Fani |
| 5 | KPI 6: samakan nama KPI dengan rumus kolom "Tanpa rollback darurat" di SNX-OPS-FRM-04 (berlaku untuk semua jenis change), atau jadikan rumus itu khusus change darurat. Belum diterapkan | KPI C11, SNX-OPS-FRM-04 Ringkasan | Fani |
| 6 | KPI 10: Rata-rata YTD diganti jumlah kejadian, atau dikecualikan dari rata-rata, karena KPI ini hitungan bertarget 0. Belum diterapkan | KPI S15 | Fani |
| 7 | KPI 15: aturan pengisian bulan tanpa kegiatan untuk KPI triwulanan, misalnya kolom bulan review saja yang diisi. Belum diterapkan | KPI baris 20, Cara pakai butir 2 | Fani |
| 8 | KPI tambahan untuk pemulihan tiket (kolom "Pulih sesuai target" di SNX-OPS-FRM-08), UAT atau kualitas (SNX-OPS-FRM-05), dan response SLA. Target baru tidak diusulkan. Belum diterapkan | KPI baris baru | Fani |
| 9 | Jabarkan "SD dan PM" dengan nama peran yang sudah ada di Struktur Organisasi (Service Delivery Manager, Project Manager), misalnya "Service Delivery dan Project Management". Belum diterapkan | KPI B16 sampai B19 | Fani |
| 10 | "RTP" dijabarkan "Risk Treatment Plan" sesuai SNX-ISMS-REG-03. Diterapkan; konfirmasi bahwa maksud tim sama | Narasi Bulanan A9 | Fani |

## Open items

| # | Open item | Untuk |
|---|---|---|
| 1 | Gambar Alur Proses tidak bisa diubah lewat xlsx_patch. Kotak pertama menulis "FRM-01 sampai FRM-09, register", sedangkan KPI 14 bersumber SNX-OPS-FRM-10 dan KPI 3, 4, 7, 9, 10 bersumber SNX-ISMS-FRM-01 dan SNX-ISMS-FRM-02. Gambar juga memakai "COO" saja tanpa "Direktur (COO)" | Orkestrator, Fani |
| 2 | Tiga sumber KPI tanpa nomor dokumen: "Shift Log" (F22), "Tiket vulnerability" (F13), dan "SIEM" (F12). Sumber tidak menyebut sistem tiket untuk "Tiket vulnerability"; aturan tiket Zammad untuk Ops belum bisa diterapkan tanpa memastikan lingkupnya, jadi tidak ada sistem yang ditambahkan | Fani |
| 3 | KPI 14 butuh tanggal kirim RCA; register SNX-OPS-FRM-08 tidak punya kolomnya (USULAN 8 di notes/OPS-FRM-08.md) | Fani |
| 4 | Pemilik dokumen "Head of Operation" (B10) tidak sama dengan pemeriksa Fani Fatullah (VP Tech Operation and Services). HR-ORG-01 K-09 mencatat hubungan kedua jabatan belum ditetapkan, dan belum ada pemegang bernama untuk Head of Operation. Narasi Bulanan A16 tetap "Diperiksa oleh COO dan tanggal" menurut sumber, berbeda dari penyetuju dokumen di B11 | Fani, owner |
| 5 | Format xlsx tidak punya bagian Scope, Dokumen terkait, atau tabel rekaman (lokasi, pemilik). Sumber tidak menyebut yang dikecualikan dari laporan, lokasi simpan, maupun pemilik rekaman; masa simpan 3 tahun dari sumber. Kode yang dirujuk di kolom Sumber: SNX-OPS-FRM-01, FRM-04, FRM-07, FRM-08, FRM-09, FRM-10, SNX-ISMS-FRM-01, FRM-02, REG-03, REG-04 (semua ada di config/worklist.json) | Orkestrator, Fani |
| 6 | KPI B3 = 2027 berasal dari tim, sedangkan tanggal draft 13 Oktober 2026. Tidak diubah; perlu konfirmasi bahwa 2027 adalah tahun pelaporan pertama | Fani |
| 7 | Tanggal draft 13 Oktober 2026 (B7 dan B31) berasal dari tim dan lebih awal dari revisi ini; tidak diganti. Tanggal efektif tetap "Ditetapkan saat pengesahan" | Owner |
| 8 | Keterbatasan alat: nilai rumus belum tersimpan di out.xlsx (openpyxl), Excel dan LibreOffice menghitung ulang saat dibuka; kotak legenda A26 tetap biru. HUMAN-VERDICT: buka di Excel dan lihat apakah B21 dua baris tidak terpotong dan format kondisional bulan merah tetap muncul saat nilai diisi. Di render LibreOffice B21 terbaca utuh | Orkestrator, owner |
| 9 | Kalimat perintah di sumber ditujukan ke pengguna form, bukan ke penyusun: Cara pakai butir 1 sampai 5, "Sel rumus: jangan diubah", "Baris CONTOH: hapus atau timpa saat dipakai". Tidak dijalankan sebagai instruksi; legenda B26 ditulis ulang karena prompt memerintahkannya | Orkestrator |
| 10 | Cara pakai butir 3 dan B20 menyebut "sel bulan merah berarti di bawah target". Format kondisional di sheet KPI memang mewarnai merah bila di bawah target (arah ≥) atau di atas target (arah ≤), dan hijau untuk sel terisi lainnya. Tidak ada celah di sini; dicatat supaya verifikator tidak mencarinya | Verifikator |

## Asumsi dan tafsir

- "Approval persis" dari prompt mengalahkan sumber di blok Disetujui oleh dan Pengesahan, mengikuti defaults.json.
- Sheet "Kontrol Dokumen" tidak punya baris Status atau Klasifikasi PRO-01 terpisah; B6 "00 (Draft)" dan B9 sudah memuatnya, jadi tidak ada baris yang ditambah.
- Sheet Narasi Bulanan A1 dan A16 menyebut "COO" sebagai penerima dan pemeriksa narasi bulanan. Itu fakta sumber tentang laporan bulanan, jadi tidak diganti dengan penyetuju dokumen.
- Tidak ada rujukan internal AI (daftar RUNBOOK §0 butir 6) di sumber maupun di patch; dicek dengan pola lint_doc atas semua sel teks out.xlsx.
- Fakta tentang FRM-04, FRM-08, REG-03, dan HR-ORG-01 diambil dari repo kerja dan salinan audit, tidak dibuka di Drive.
- Zammad, GLPI, vault, dan PPN tidak ada di sumber dan tidak ditambahkan.
- Satu-satunya kalimat baru yang berisi isi adalah penjabaran "Risk Treatment Plan" di A9 dan teks legenda B26. Keduanya bukan proses baru.

## Dua pertanyaan penutup

**Apa yang membuat teks ini terdengar buatan AI?** Pemeriksaan atas entri `set` yang mengubah teks dan atas notes ini:

| Temuan | Perbaikan |
|---|---|
| Draf awal B26 berbunyi "Biru muda: warna baris contoh, sudah dikosongkan dan tidak dipakai" (kalimat sibling). Di workbook ini tidak pernah ada baris yang dikosongkan, jadi kalimat itu terdengar rapi tetapi menyatakan hal yang tidak terjadi | Diganti "Biru muda: tidak dipakai, tidak ada baris contoh" |
| Penjabaran "Risk Treatment Plan" di A9 bisa terbaca sebagai hiasan | Dipertahankan: menutup singkatan yang tidak dijabarkan, satu fakta, tanpa kata tambahan |
| "Direktur (COO)" di B21 terbaca kaku | Dipertahankan: aturan data_conflicts, hanya satu kali di badan dokumen |
| Tabel notes memakai kalimat "Tidak diubah" berulang | Dipertahankan: tiap baris menyebut alasan berbeda |
| Em-dash, en-dash, tebal, huruf kapital penekanan, kata kosong (holistik, sinergi, robust), penutup positif | Tidak ada di nilai patch (pencarian karakter dan lint). Notes ini tidak memakai em-dash atau en-dash |

**Adakah fakta, angka, nama, atau tanggal tanpa sumber?**

| Butir | Sumber |
|---|---|
| Erik Dwi Yanto, Fani Fatullah, Samuel Kristanto Utomo beserta jabatannya | config/defaults.json prepared_reviewed.OPS dan approved_by; sama dengan prompt |
| "Draft awal untuk review dan pengesahan", "00", "Draft" | revision_desc, revision, status di prompt dan defaults.json |
| "Klausul 9.1" dan "Klausul 9.1, 9.3.2" | Prompt (acuan klausul baris ini); B12 dan B13 sumber |
| "Direktur (COO)" | config/defaults.json data_conflicts, butir sebutan Amirull Yusuf Zulkarnain |
| "Risk Treatment Plan" | Salinan audit SNX-ISMS-REG-03 (judul diagram "Alur Information Security Risk Treatment Plan", ID RTP-001 dan seterusnya); bukan dari workbook ini, jadi dilabeli USULAN 10 |
| "Biru muda: tidak dipakai, tidak ada baris contoh" | Pemeriksaan sel sumber: tidak ada baris contoh; warna E7EEF7 dari sel A26 |
| "3 tahun", "RESTRICTED (Internal)", "Head of Operation", "13 Oktober 2026", "2027", 17 KPI | Sumber RPT-01, tidak diubah |
| Rujukan FRM-04, FRM-05, FRM-08, ML-00 butir 2, HR-ORG-01 K-09 di notes | Repo kerja dan salinan audit; hanya di notes, tidak di sel |
Tidak ada angka, nama, atau tanggal lain yang saya tambahkan.
