# Catatan penyusun HR-JA-01: Job Analysis dan Uraian Jabatan

Status: DRAFTED (spec + notes ada). Spec: specs/HR-JA-01.json. Mode generic, aksi T1, nomor SNX-HR-JA-01 (nomor SNX lama dipertahankan), department Human Resources, classification RESTRICTED (Internal), audit_class C2, wave W1. Approval persis dari config/defaults.json: prepared Sita Nadia Salsabila Widodo / HRGA Officer, reviewed Aziz Priyo Widakdo / HR Manager, approved Samuel Kristanto Utomo / President Director. process_owner "HR Manager" (jabatan tanpa nama). Draft, revision 00, effective_date kosong, review YEARLY.

Hasil uji terakhir (sesudah semua suntingan):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/HR-JA-01.json /tmp/pen-HR-JA-01/HR-JA-01.docx` sukses.
- `python3 -I tools/lint_doc.py /tmp/pen-HR-JA-01/HR-JA-01.docx generic` menghasilkan `"pass": true`, `fails: []`, satu warn "28 butir (USULAN) menunggu ACC" (putaran perbaikan 1; sebelumnya 12).
- Validator OOXML skill docx: "All validations PASSED!". PDF via soffice 30 halaman (putaran 1: 26 halaman), dilihat sebagai montase halaman pada putaran awal dan teks PDF pada putaran 1.

Putaran perbaikan 1 (verifikator buta: FAIL, 1 blocking, kondisi kerja): baris "Kondisi kerja" tiap jabatan kini berisi pola kerja, lingkungan dan kondisi fisik, serta risiko kerja; garis lapor pindah ke baris "Garis pelaporan". Butir 4.10 baru memuat lokasi, izin keluar area kantor, kerja dari rumah, dan hari libur resmi. Kalimat yang menunda kondisi kerja ke revisi berikutnya dihapus. Rincian sumber di bagian 2b.

## 1. Sumber

| Sumber | fileId | modifiedTime (get_file_metadata, dicek ulang hari ini) | Cara baca |
|---|---|---|---|
| SINUX_Job_Analysis_2026.docx (51426 byte) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 | 2026-10-13T10:34:44.783Z | read_file_content (teks utuh, 15 jabatan) |
| Jobdesk Line Manager Legal – SINUX.docx (12341 byte) | 1Mv6TuLy8QsllpA4YTTjmNg7Hsur4yWiL | 2026-10-13T10:54:32.072Z | read_file_content |
| Jobdesk Staff Legal – SINUX.docx (12252 byte) | 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW | 2026-10-13T10:54:34.881Z | read_file_content |
| Checklist baris 8 (kriteria) | 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY, config/checklist.json | 2026-10-14T17:47:13.611Z | Description: "Dokumen analisis yang memuat rincian tugas, tanggung jawab, kualifikasi, dan kondisi kerja dari suatu posisi." |
| Peraturan Perusahaan BAB VI (berkas PP - Cuti.docx, 30617 byte) | 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z | 2026-10-13T11:34:27.275Z | read_file_content (Pasal 22, 29, 31 dipakai untuk butir 4.10) |
| POL-OPS-001 Kebijakan Divisi Operation SINUX, DRAFT v0.1 (111296 byte) | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z | read_file_content (Bagian 3, 5, 6, 13 untuk pola shift Operation) |
| Footer template SOP (alamat kantor) | template/SOP_TEMPLATE.docx, word/media/image2.png | n/a | gambar dibuka: "Sinux Office / Midpoint Place Lt.10, Jl. H. Fachrudin, Kp. Bali, Tanah Abang, Jakarta Pusat, DKI Jakarta" |
| Catatan cacat (DATA, bukan Drive) | context/audit/iso-sinux-supdocs-hr-2026-10-14.md bagian 5 (HR-JA-001), iso-sinux-supdocs-legal-2026-10-14.md bagian 5 (dua jobdesk) | salinan audit 13 sampai 14 Okt | grep fileId, dibaca utuh |

Catatan W0 (checklist menautkan 1bSxe1PtXbG9p-XFsc0hlcSxYaD2W86yO): `get_file_metadata` pada fileId itu hari ini menjawab "Requested entity was not found". Pencarian `title contains 'Job Analysis'` hanya menemukan SINUX_Job_Analysis_2026.docx dan Jobdesk Staff Legal (halaman berikutnya kosong). Berkas yang ditaut checklist tetap tidak terlihat oleh konektor; sumber worklist dipakai. Minta tim membagikan berkas itu, lalu bandingkan dengan SINUX_Job_Analysis_2026.docx sebelum dokumen ini disahkan.

Tidak ada kalimat di tiga sumber yang menyuruh penyusun atau alat melakukan sesuatu. Kalimat "harus dikonfirmasi oleh manajemen sebelum pengesahan" dan "harus diselesaikan sebelum dokumen diberi status Controlled / Effective" adalah aturan untuk dokumen, bukan perintah ke penyusun; keduanya dimuat di butir 4.3.

## 2. Kriteria penerimaan dan letaknya di dokumen

| Unsur Description | Letak |
|---|---|
| Rincian tugas | Bagian 6, tabel "Tugas dan tanggung jawab" tiap jabatan (7 butir, JA-14 11 butir); bagian 7 untuk dua jabatan Legal |
| Tanggung jawab | Baris "Tujuan jabatan" dan tabel yang sama; bagian 7 "Tanggung jawab utama" Line Manager Legal |
| Kualifikasi | Baris Pendidikan dan pengalaman (kelompok K1 sampai K4, butir 4.9), kompetensi teknis, kompetensi perilaku, persyaratan tambahan (butir 4.7); bagian 7 "Kualifikasi (USULAN)" |
| Kondisi kerja | Butir 4.10 (lokasi, izin keluar area kantor, kerja dari rumah, hari libur resmi, jam kerja); baris "Kondisi kerja" tiap jabatan di bagian 6 (pola kerja, lingkungan dan kondisi fisik, risiko kerja); baris "Garis pelaporan"; hubungan kerja (butir 4.8); batasan wewenang (butir 4.5); bagian 7 "Rutinitas", "Batasan dan eskalasi", "Hubungan kerja" |
| Posisi | Dokumen memakai "jabatan" untuk semua; "posisi" hanya muncul di definisi Jabatan |

## 2b. Sumber kondisi kerja (putaran perbaikan 1)

| Unsur | Isi di dokumen | Sumber dan kutipan verbatim | Status |
|---|---|---|---|
| Lokasi kerja utama | Sinux Office, Midpoint Place Lt.10, Jakarta Pusat (butir 4.10) | Footer template SOP: "Sinux Office" dan "Midpoint Place Lt.10, Jl. H. Fachrudin, Kp. Bali, Tanah Abang, Jakarta Pusat, DKI Jakarta". Alamat kantor, bukan pernyataan HR bahwa semua jabatan bekerja di sana | bersumber; "lokasi kerja utama" tafsir |
| Izin keluar area kantor | butir 4.10 | PP Pasal 29 ayat 1: "Karyawan tidak diperkenankan untuk keluar dari area kantor pada jam kerja tanpa ada izin dan pemberitahuan sebelumnya kepada atasan langsung;" | bersumber |
| Kerja dari rumah | butir 4.10 | PP Pasal 31: "Bekerja dari Rumah dapat diberikan untuk karyawan yang memiliki halangan untuk berangkat ke kantor, tapi bukan karena sakit maupun cuti;" dan "harus tetap dapat dihubungi pada jam kerja melalui saluran komunikasi yang biasa digunakan di Perusahaan;" dan "Karyawan diwajibkan memberikan laporan kepada atasan atas pekerjaan yang dilakukan;" | bersumber |
| Hari libur resmi | butir 4.10 | PP Pasal 22: "Karyawan tidak wajib bekerja pada hari-hari libur resmi;" dan "Perusahaan dapat mempekerjakan karyawan untuk bekerja pada hari-hari libur resmi apabila jenis dan sifat pekerjaan tersebut harus dilaksanakan atau dijalankan secara terus-menerus atau pada keadaan lain berdasarkan kesepakatan antara karyawan dengan Perusahaan;" | bersumber |
| Jam masuk dan jam pulang | "mengikuti Peraturan Perusahaan (USULAN)" | PP BAB VI (Pasal 22 sampai 34) tidak menyebut jam masuk, jam pulang, atau jumlah jam kerja per hari; hanya "jam kerja" tanpa angka. Bab PP lain tidak ada di tangan penyusun | USULAN U10 |
| Pola shift Operation (JA-02, JA-04, JA-13) | JA-02: COO dihubungi di luar jam kerja saat P1; JA-04: layanan Operation 24/7; JA-13: tiga shift 8 jam | POL-OPS-001 Bagian 5: "NOC dan SOC wajib tertutup 24 jam sehari, 7 hari seminggu, dengan tiga shift 8 jam dan overlap 15 menit untuk serah terima. (USULAN, jam dan jumlah regu disahkan COO)" dengan jam "07:00 sampai 15:00", "15:00 sampai 23:00", "23:00 sampai 07:00" (WIB). Bagian 6: P1 "merupakan satu-satunya kelas yang boleh membangunkan COO di luar jam kerja". Bagian 13: "COO: konfirmasi apakah tim Tech Ops yang ada (mis. Erik Dwi Yanto) dipetakan ke NOC." | bersumber, tetapi POL-OPS-001 sendiri berstatus DRAFT dan jam shift berlabel USULAN di sumber; dokumen ini menulisnya sebagai "mengusulkan" dan menggantungkan penempatan JA-13 pada keputusan COO |
| Tugas dan wewenang yang menjadi kondisi kerja | pola kerja dan risiko kerja tiap jabatan | HR-JA-001 dan dua jobdesk Legal: rujukan butir uraian atau wewenang ditulis di tiap sel (mis. JA-15 butir 2 "perpindahan barang ringan", butir 6 "Menggunakan APD bila diwajibkan dan melaporkan potensi bahaya", wewenang 2 "Menghentikan aktivitas yang tidak aman dan melapor"; JA-09 bagian 7.2 "Rutinitas") | bersumber |
| Lingkungan dan kondisi fisik tiap jabatan | "ruang kantor, kerja menetap dengan komputer, bahaya fisik rendah" untuk jabatan kantor; JA-15 "area kantor dan fasilitas, kerja sebagian berdiri dan berpindah tempat, bukan kerja layar"; kekhususan (pertemuan di luar kantor, demo di lokasi pelanggan, event di luar jam) | Tidak ada di sumber mana pun. Versi paling wajar menurut jenis pekerjaan yang tertulis di tugas jabatan | USULAN U3 (15 label, satu per jabatan) |

Tidak ada angka baru. Angka jam shift berasal dari POL-OPS-001.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Cakupan: 15 jabatan aktif, tanpa jabatan kosong dan grading | "15 jabatan aktif. Posisi kosong dan grading tidak dicantumkan." (tabel kontrol dokumen, baris Cakupan) | 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1 |
| 2 | Line Manager Legal perlu persetujuan atasan untuk empat hal | "Perlu persetujuan atasan: strategi litigasi, penyelesaian sengketa,perubahan struktur korporasi, dan penyimpangan dari playbook pada klausul risiko tinggi." (bawah tabel Wewenang; salah ketik tanpa spasi ada di sumber) | 1Mv6TuLy8QsllpA4YTTjmNg7Hsur4yWiL |
| 3 | Staff Legal melapor somasi, klaim, atau surat regulator paling lambat 1 hari kerja | "Melaporkan somasi, klaim, atau surat regulator kepada Line Manager paling lambat 1 hari kerja." (Bagian 5 Batasan dan Eskalasi) | 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW |

## Kutipan sumber lain untuk fakta penting

| Fakta | Kutipan verbatim | Dipakai di | fileId |
|---|---|---|---|
| Wewenang dibatasi Authority Matrix | "Authority dalam dokumen dibatasi oleh persetujuan Authority Matrix, jabatan tidak otomatis memperoleh hak tanda tangan kontrak atau otorisasi keuangan." (Bagian 2) | butir 4.4 | 1m91Wr... |
| KPI tidak ada per jabatan | "KPI dalam dokumen merupakan usulan indikator, target numerik, bobot dan sumber data ditetapkan pada KPI Matrix terpisah." (Bagian 2) | butir 4.6, ruang lingkup | 1m91Wr... |
| Garis usulan belum resmi | "Hubungan atasan-bawahan bertanda “usulan/konfirmasi” tidak boleh diperlakukan sebagai reporting line resmi sampai disahkan." (Bagian 2) | butir 4.3 | 1m91Wr... |
| Syarat sebelum status berlaku | "Catatan pengendalian: semua hubungan pelaporan dan batas otoritas yang belum terkonfirmasi harus diselesaikan sebelum dokumen diberi status Controlled / Effective." (Bagian 4) | butir 4.3 | 1m91Wr... |
| Peninjauan berkala | "Next review \| 12 bulan sejak efektif atau saat ada perubahan signifikan" (Bagian 4) | bagian 9 | 1m91Wr... |
| Pemilik dokumen | "Process Owner \| HR Lead – Aziz Priyo Widakdo" (tabel kontrol) | meta.process_owner "HR Manager" | 1m91Wr... |
| Persyaratan tambahan semua jabatan | "memahami SOP dan kerahasiaan informasi, sertifikasi profesi/vendor hanya diwajibkan bila ditetapkan dalam competency matrix atau kebutuhan kontrak pelanggan. Masa pengalaman minimum ditentukan setelah job evaluation." | butir 4.7 | 1m91Wr... |
| Batasan umum wewenang | "Batasan umum: keputusan keuangan, legal, perubahan kontrak, pengangkatan/pemutusan hubungan kerja, serta perubahan sistem produksi tetap mengikuti delegasi dan persetujuan tertulis yang berlaku." | butir 4.5 | 1m91Wr... |
| Garis lapor JA-14 tidak satu atasan | "Direktur atau Management sesuai struktur yang disahkan" (JA-14, Atasan Langsung) | JA-14, kondisi kerja | 1m91Wr... |
| Pelaporan Product Tech belum pasti | "Hubungan pelaporan Manager of Product Tech perlu dikonfirmasi." (JA-03, Bawahan Langsung) dan JA-05 "Atasan Langsung \| Direktur" | JA-03, JA-05 | 1m91Wr... |
| Line Manager Legal: atasan | "Atasan langsung \| CEO" (Bagian 1) | bagian 7.1 (ditulis Direktur Utama) | 1Mv6Tu... |
| Line Manager Legal: kontradiksi wewenang | "Menahan kontrak berisiko tinggi sampai ada keputusan manajemen" dengan batas "Legal tidak berhak menahan dan hanya memberi opini (kecuali ada keputusan dari manajemen)" (Bagian 4) | bagian 7.1, USULAN U4 | 1Mv6Tu... |
| Line Manager Legal: pengalaman | "Pengalaman minimal 5 tahun di bidang legal korporasi atau komersial." (Bagian 7, berlabel usulan) | bagian 7.1 | 1Mv6Tu... |
| Staff Legal: pengingat jatuh tempo | "Mengirim pengingat jatuh tempo kontrak dan izin kepada PIC bisnis pada 90, 60, dan 30 hari sebelumnya." (Bagian 3) | bagian 7.2 | 1dOku3... |
| Staff Legal: pengalaman | "Pengalaman minimal 1-2 tahun; fresh graduate dapat dipertimbangkan sesuai level jabatan." (Bagian 7, usulan) | bagian 7.2 | 1dOku3... |
| Kalimat terpotong | "...disahkan oleh Management. oleh pemegang fungsi dan Management, bukan fakta yang telah disahkan." (Bagian 1 paragraf 2) | butir 4.1 | 1m91Wr... |
| Klausul ISO di sumber | "ISO 9001:2015 klausul 7.3 dan 7.5: pemahaman karyawan serta pengendalian informasi terdokumentasi." (Bagian 2) | bagian 11 | 1m91Wr... |

## 3. Keputusan data (config/defaults.json v21 mengalahkan sumber)

| Butir | Sumber menulis | Dokumen memakai | Dasar |
|---|---|---|---|
| Ejaan Direktur Utama | Samuel Kristianto Utomo | Samuel Kristanto Utomo; badan dokumen "Direktur Utama"; blok approval "President Director" | data_conflicts |
| CEO (jobdesk Line Manager Legal) | CEO | Direktur Utama | data_conflicts |
| Amirull | Direktur | "Direktur (COO)" di tabel Daftar Jabatan (sebutan pertama di badan), sesudahnya "COO" (judul JA-02, atasan langsung, bawahan JA-01) | data_conflicts |
| Aziz | HR Lead | HR Manager (JA-14, atasan JA-12, process owner) | data_conflicts, premis owner |
| Prepared, reviewed, approved | HR Lead, Pemegang fungsi terkait, Management / Authorized Director | Sita, Aziz, Samuel | prepared_reviewed HR, approved_by |
| Laras | atasan langsung Direktur | "COO (garis pelaporan ke Direktur Utama menunggu konfirmasi)" | data_conflicts, kata owner |
| Aziz, garis ke atas | Direktur atau Management | "COO atau Management (menunggu konfirmasi)" | data_conflicts |
| Nama Legal | JA-08 Ester Febe Utomo, JA-09 Alif Altamziz | dipertahankan | data_conflicts (selesai) |
| Tiket | tidak menyebut sistem | Zammad pada JA-04 butir 3, JA-13 butir 1 dan 6 (peran Operation). GLPI tidak dipakai karena tidak ada jabatan generalist yang menyebut tiket | defaults "ticketing" |
| Tidak dipakai | vault, PPN | tidak relevan untuk dokumen ini | |

## 4. Penanganan cacat context/audit

### 4.1 HR-JA-001 (1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1), bagian 5 audit

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | DRAF, Revision "03 -", Effective "-", nomor usulan | Rev. 00, Draft, effective kosong, nomor SNX-HR-JA-01; HR-JA-001 dicantumkan di Dokumen terkait sebagai sumber |
| 2 | Tidak ada KPI, bagan organisasi, grade; hanya 15 jabatan | Tidak ditambah. Ruang lingkup menyebutnya sebagai pengecualian; KPI di butir 4.6; bagan di SNX-HR-ORG-01 |
| 3 | Kalimat terpotong Bagian 1 | Disambung di butir 4.1: dua potongan digabung ("ditinjau oleh pemegang fungsi dan disahkan oleh Management, bukan fakta yang telah disahkan"). Penggabungan itu tafsir, masuk USULAN U7 |
| 4 | Frasa kompetensi janggal | Dipulihkan, lihat tabel 5. Terbukti dari sumber sendiri: Bagian 2 memakai "pemahaman karyawan" untuk klausul 7.3 (awareness), jadi "Risk pemahaman karyawan" = "Risk awareness". Frasa tunggal huruf kecil yang bermakna ("pembinaan", "pengendalian dokumen", "pemantauan dan log analysis") hanya diberi huruf kapital |
| 5 | Pelaporan Manager of Product Tech tidak konsisten | JA-05 atasan "COO (VP Commercial sebagai atasan langsung menunggu konfirmasi)"; JA-03 bawahan "menunggu konfirmasi". Open item 4 |
| 6 | Atasan JA-06 dan JA-07 "Commercial - Laras Rasmawati" | "VP Commercial (Laras Rasmawati)" |
| 7 | "Management / Direktur" dan "Direktur atau Management" | Tidak memilih satu atasan: "COO atau Management (menunggu konfirmasi)" untuk JA-08, JA-10, JA-11, JA-14. Open item 4 |
| 8 | Nama unit tidak seragam | Operation (JA-04, 05, 13), Human Resources (JA-12, 14, 15), sisanya sesuai sumber. Masuk USULAN U7 |
| 9 | Dua jabatan berjudul sama "Legal & Compliance" | Pembeda "(Line Manager Legal)" dan "(Staff Legal)" di daftar jabatan, berlabel USULAN U2 |
| 10 | Tidak ada Finance Lead dan Finance Staff | Bagian 8 mencatat keduanya "Belum dipetakan"; tidak ada jabatan baru dibuat. Open item 11 |
| 11 | Ejaan Samuel dan sebutan CEO | Lihat tabel 3 |
| 12 | Teks B dan F identik di 15 jabatan, E batasan umum identik, empat varian pendidikan | Satu kali di butir 4.5, 4.7, 4.8, 4.9 (kelompok K1 sampai K4); tiap jabatan merujuk butir itu. Butir wewenang per jabatan tetap utuh |
| 13 | Masa pengalaman minimum dan sertifikasi belum ada | Dipertahankan apa adanya di butir 4.7, tidak diisi angka. Open item 14 |
| 14 | Jumlah tabel 34 lawan 17 | Tidak berlaku untuk dokumen hasil; tidak ditangani |
| 15 | Klausul 7.3 dan 7.5 dibaca satu baris; tidak ada rujukan 27001 | Bagian 11 memisahkan 7.3 Kesadaran dan 7.5 Informasi terdokumentasi, menambah 27001:2022 5.3, 7.2, 7.3, 7.5, Annex A 5.2. Seluruh bagian berlabel "(USULAN, dikonfirmasi konsultan)" |

### 4.2 Jobdesk Line Manager Legal (1Mv6TuLy8QsllpA4YTTjmNg7Hsur4yWiL)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tidak ada kode, revisi, tanggal, pemilik, penyetuju, klasifikasi | Teratasi oleh template dan meta; tanggal tetap kosong |
| 2 | Kontradiksi wewenang "menahan kontrak" | Tidak dipilih diam-diam. Bagian 7.1 menulis "Legal memberi opini; penahanan berlaku hanya atas keputusan Management (USULAN)". Ini bacaan penyusun agar kedua kalimat sumber bisa benar bersamaan; U4 dan open item 7 |
| 3 | Sel batas "Menunjuk notaris, konsultan, atau advokat" kosong | Ditulis "Belum ditetapkan". Open item 8 |
| 4 | Atasan CEO lawan "Management / Direktur" di JA-08 | Ditulis "Direktur Utama menurut Jobdesk Line Manager Legal. Menunggu konfirmasi, karena JA-08 di bagian 6 menulis COO atau Management." Open item 6 |
| 5 | DoA dan "KPI dari CEO" tanpa dokumen | "DoA" dan "matriks otorisasi" dibaca sebagai Authority Matrix (USULAN U1); "KPI dari Direktur Utama". Authority Matrix tercantum di Dokumen terkait tanpa kode |
| 6 | KPI mengacu SLA yang usulan | Indikator "Review kontrak sesuai SLA" dan target "90% tepat waktu" dipertahankan berlabel USULAN. Dokumen tidak menyebut angka SLA, karena SLA ada di SOP Legal yang tidak saya baca. Open item 17 |
| 7 | KPI dan kualifikasi berlabel usulan; tanpa nama | Label dipertahankan lewat "(USULAN)" di header tabel; pemetaan nama USULAN U2 |
| 8 | Titik tengah menggantung di baris judul | Tidak dibawa; judul dokumen diganti |
| 9 | Salah ketik "sengketa,perubahan" | Diperbaiki menjadi "sengketa, perubahan struktur korporasi" |

### 4.3 Jobdesk Staff Legal (1dOku3703JwQCVeC39tl9x6k0FMa4f3nW)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Tidak ada kode, revisi, dan seterusnya | Teratasi oleh template dan meta |
| 2 | Dua KPI tanpa target | Ditulis "Belum ditetapkan"; tidak dibuat angka. Open item 9 |
| 3 | KPI dan kualifikasi usulan | Label (USULAN) di header tabel |
| 4 | Titik tengah menggantung | Tidak dibawa |
| 5 | Tidak ada nama; pemetaan ke JA-09 | Pemetaan tetap USULAN U2; "Alif Altamziz = Supporting PIC Legal" adalah konfirmasi owner 14 Okt (defaults), tetapi pemetaan ke jabatan Staff Legal belum dikonfirmasi |
| 6 | SOP Legal menyebut "Staff Legal (Senior/Junior)", jobdesk satu level | Tidak dibedakan di dokumen. Open item 17 |
| 7 | Pengalaman berbentuk rentang "1-2 tahun" | Ditulis "1 sampai 2 tahun"; tidak dijadikan angka tunggal |

## 5. Pemulihan frasa rusak (teks sumber menjadi teks dokumen)

| Letak | Teks sumber | Teks dokumen |
|---|---|---|
| JA-02 D.5 | pihak terkait management | Stakeholder management |
| JA-04 D.3 | pelanggan communication | Customer communication |
| JA-04 D.4, JA-10 D.3 | Risk pemahaman karyawan | Risk awareness |
| JA-10 D.4 | pihak terkait coordination | Stakeholder coordination |
| JA-11 D.4 | tenggat waktu discipline | Deadline discipline |
| JA-13 D.5 | Escalation pemahaman karyawan | Escalation awareness |
| JA-15 D.4 | Safety pemahaman karyawan | Safety awareness |
| JA-14 D.5 | pihak terkait influence | Stakeholder influence |
| JA-08 C.3 | Legal kepatuhan register | Legal compliance register |
| JA-11 C.2 | Tax kepatuhan Indonesia | Tax compliance Indonesia |
| JA-08 C.1 | Contract drafting/peninjauan | Contract drafting/review |
| JA-03 C.3 | Account management dan contract serah terima | Account management dan serah terima kontrak |
| JA-14 C.2 | rekrutmen assessment dan workforce planning | Asesmen rekrutmen dan workforce planning |
| JA-14 C.5 | Competency mapping, TNA dan pelatihan evaluation | Competency mapping, TNA dan evaluasi pelatihan |
| JA-03 A.3 | pricing peninjauan | peninjauan pricing |
| JA-08 A.1 | legal peninjauan kontrak | peninjauan hukum atas kontrak |
| JA-09 A.6 | bukti audit/legal kepatuhan | bukti audit dan kepatuhan hukum |
| JA-09 E.3 | legal persetujuan final | persetujuan hukum final |
| JA-10 A.1 | cash flow proyeksi | proyeksi cash flow |
| JA-11 A.7 | pendukung schedules | schedule pendukung |
| JA-13 A.3 | pemeriksaan rutin pemantauan, backup status dan alert | pemeriksaan rutin atas pemantauan, status backup dan alert |
| JA-14 E.2 | quality peninjauan | peninjauan mutu |

Penjelasan pola: kata "pemahaman karyawan", "pihak terkait", "kepatuhan", "peninjauan", "pelanggan", "tenggat waktu" tampak menggantikan awareness, stakeholder, compliance, review, customer, deadline dengan urutan kata Inggris yang tertinggal. Pemulihan ini tafsir (USULAN U7), bukan kalimat tim.

## 6. Asumsi dan tafsir

1. Padanan kata lain yang diseragamkan agar satu istilah satu hal: manajemen dan Direksi menjadi Management; Divisi Legal menjadi Legal; HR menjadi Human Resources; GA menjadi general affairs; "Departemen HR" menjadi Human Resources; "Tech Operation and Services" sebagai nama unit menjadi Operation (nama jabatan VP tidak diubah); atasan menjadi atasan langsung; HRGA (JA-14 butir 9) menjadi HRGA Officer; pelindungan menjadi perlindungan; Mengkoordinasikan menjadi Mengoordinasikan; "1-2" menjadi "1 sampai 2". "Divisi Bisnis/Sales" menjadi Commercial (USULAN U7).
2. Kalimat sumber yang dibiarkan walau kurang jelas: "eligible collection SIP" (JA-10 butir 3, singkatan SIP tidak dijelaskan), "Product Tech" (JA-07 butir 4), "tim teknis", "tim komersial", "tim delivery", "engineer senior". Alasannya T1: suara tim dipertahankan; SIP masuk open item 12.
3. Singkatan (SLA, CRM, TCV, BOM/BOQ, PoC, RCA, ITSM, HRIS, TNA, COGS, AR/AP, PSAK, NDA, PKS, OSS, KBLI, NIB) tidak diuraikan karena tidak ada di sumber dan dokumen ini untuk pembaca internal. Satu-satunya yang diuraikan: APD menjadi "alat pelindung diri (APD)".
4. Kelompok pendidikan K1 sampai K4 adalah label penyusun. Isinya kalimat sumber. Daftar jabatan tiap kelompok dicek terhadap teks sumber (JA-01 sampai 04 dan 14 = kepemimpinan; JA-05 sampai 12 = D3/S1; JA-13 = SMK/D3/S1 IT; JA-15 = sesuai kebutuhan operasional).
5. "Management" didefinisikan sebagai unit tempat JA-01 dan JA-02 berada, dari kolom Unit / Departemen sumber (keduanya "Management"). Sumber tidak mendefinisikannya.
6. Pelaku "HR Manager meninjau dokumen ini 12 bulan sejak tanggal efektif" diambil dari process owner; sumber hanya menulis "Next review". Pelaku "Pemegang fungsi meninjau, Management mengesahkan" dan "Management mengonfirmasi" mengikuti kalimat sumber ("oleh pemegang fungsi dan Management", "dikonfirmasi oleh manajemen").
7. Sumber mencatat peran "Reviewed by: Pemegang fungsi terkait / Department Owner". Defaults menetapkan Aziz sebagai reviewer; dokumen mengikuti defaults.
8. Persyaratan, kompetensi, dan wewenang JA-01 sampai JA-15 disalin tanpa mengubah substansi; tidak ada butir ditambah atau dibuang. JA-14 tetap punya 11 tugas, 7 kompetensi teknis, 7 perilaku, 6 wewenang.
9. Tabel Peran ISO hanya memuat peran yang dibahas tiga sumber ini. Peran Operation dan ISMS (Head of Operation dan seterusnya) dirujuk ke SNX-HR-ORG-01; isi SNX-HR-ORG-01 belum ada saat dokumen ini disusun (worklist: W1, QUEUED).
10. Kode SNX-LEG-SOP-01 (SOP Legal Operational), SNX-FAT-SOP-01, SNX-FAT-SOP-05, SNX-HR-FRM-01, SNX-HR-ORG-01 diambil dari config/worklist.json. Isi SOP Legal, SOP FAT, dan HR-FRM-01 tidak saya buka; kebenaran bahwa SOP FAT memakai Finance Lead dan Finance Staff berasal dari bagian 5 audit HR (cacat 10), bukan dari berkas Drive.
11. Klausul ISO dan judulnya berasal dari teks standar yang saya kenal dan dari bagian 2 HR-JA-001; tidak ada saran konsultan di repo. Seluruhnya berlabel.
12. Tabel kompetensi dan wewenang berupa satu sel berisi butir bernomor dan titik koma, karena renderer mengisi satu paragraf per sel.
13. Putaran 1: nama unit "IT/Keamanan" dan "IT" di jobdesk Legal dipertahankan karena bukan nama unit di HR-JA-001 dan tidak ada padanan Operation yang terbukti; sinonim "peninjauan hukum" (JA-08) dan "review" (jobdesk) dipertahankan sebagai kata tim (T1).
14. Putaran 1: frasa "lokasi kerja utama" memakai alamat kantor di footer template. Sumber tim tidak menyebut apakah jabatan tertentu (Commercial, Operation) bekerja di lokasi pelanggan; kekhususan itu berlabel USULAN.
15. Putaran 1: POL-OPS-001 tidak memberi nomor SNX (penomoran usulan di sumber), jadi dicantumkan dengan kode sumbernya di Dokumen terkait.
16. Putaran 1: kalimat butir 4.10 tentang Pasal 22, 29, dan 31 adalah parafrasa dekat dari kutipan di bagian 2b; "atasan" di pasal itu ditulis "atasan langsung" hanya bila pasal menyebut atasan langsung (Pasal 29 ayat 1).

## USULAN

Hitungan sesudah putaran 1: 28 label "(USULAN)" di dokumen (sama dengan warn lint) ditambah 1 label "(USULAN, dikonfirmasi konsultan)" di bagian 11. Total 11 butir. Perubahan putaran 1: U3 diganti isi dan jumlah labelnya (dari 1 menjadi 15), U10 dan U11 baru, butir "HR Manager melengkapi revisi berikutnya" dihapus.

| # | Butir | Letak | Pemutus yang disarankan |
|---|---|---|---|
| U1 | "Matriks otorisasi" (JA-02, JA-14) dan "DoA" (jobdesk Legal) dibaca sebagai Authority Matrix | Definisi | Legal |
| U2 | JA-08 = Line Manager Legal, JA-09 = Staff Legal (3 label: daftar jabatan, dua baris matriks peran) | bagian 5, 8 | Legal |
| U3 | Lingkungan dan kondisi fisik kerja per jabatan, dan kekhususan yang ikut dalam kalimat itu (pertemuan atau demo di lokasi pelanggan, event di luar jam kerja, eskalasi insiden di luar jam kerja, penempatan JA-13 pada shift atau jam kantor menurut keputusan COO); 15 label, satu per jabatan | bagian 6, baris Kondisi kerja | Aziz |
| U10 | Jam masuk dan jam pulang mengikuti Peraturan Perusahaan (jam tidak ada di PP BAB VI) | butir 4.10 | Aziz |
| U11 | Kualifikasi bagian 7 menggantikan kelompok K2 untuk JA-08 dan JA-09, dan masa pengalaman minimum butir 4.7 mengikuti angka bagian 7 | bagian 7, paragraf pengantar | Legal |
| U4 | Batas wewenang "Menahan kontrak berisiko tinggi": Legal memberi opini, penahanan hanya atas keputusan Management | bagian 7.1 | Legal |
| U5 | Indikator dan target KPI Line Manager Legal serta Staff Legal (target dari sumber, berlabel usulan di sumber; 2 label) | bagian 7.1, 7.2 | Legal |
| U6 | Kualifikasi Line Manager Legal dan Staff Legal (berlabel usulan di sumber; 2 label) | bagian 7.1, 7.2 | Legal |
| U7 | Pemulihan frasa rusak, penyambungan kalimat butir 4.1, penyeragaman nama unit, Bisnis/Sales menjadi Commercial | bagian 9, tabel 5 notes | Aziz |
| U8 | SNX-HR-FRM-01 dibaca sebagai Competency Matrix di sumber | Dokumen terkait | Aziz |
| U9 | Seluruh acuan klausul ISO 9001:2015 dan ISO/IEC 27001:2022 (termasuk tambahan 27001 yang tidak ada di sumber) | bagian 11 | owner (konsultan mengonfirmasi) |

## Open items

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Checklist baris 8 menautkan 1bSxe1PtXbG9p-XFsc0hlcSxYaD2W86yO yang tidak terlihat oleh konektor (metadata not found, pencarian judul nihil). Minta tim membagikan berkas itu, lalu bandingkan dengan sumber yang dipakai | owner, Aziz |
| 2 | Konfirmasi pemulihan frasa kompetensi (tabel 5) dan penyambungan kalimat butir 4.1 bersama pemegang fungsi | Aziz |
| 3 | Penyeragaman nama unit: JA-12, JA-14, JA-15 semuanya Human Resources; JA-04, JA-05, JA-13 Operation. Fungsi General Affairs tidak disebut sebagai unit | Aziz |
| 4 | Satu atasan langsung untuk JA-08, JA-10, JA-11, JA-14 (COO atau Management); garis JA-03 ke Direktur Utama; atasan JA-05 (COO atau VP Commercial) | owner, Aziz |
| 5 | Pemetaan JA-08 ke Line Manager Legal dan JA-09 ke Staff Legal; kedua jobdesk tidak menyebut nama | Legal |
| 6 | Atasan Line Manager Legal: Direktur Utama (jobdesk, sumber menulis CEO) atau COO atau Management (JA-08) | owner, Samuel |
| 7 | Kontradiksi wewenang menahan kontrak berisiko tinggi di jobdesk Line Manager Legal; SOP Legal juga memuat "Hentikan proses; eskalasi ke manajemen" pada risiko Tinggi (kutipan dari audit, SOP tidak saya buka) | Legal, Samuel |
| 8 | Batas wewenang menunjuk notaris, konsultan, atau advokat kosong di sumber; SOP Legal merujuk batas itu ke jobdesk ini | Legal |
| 9 | Target KPI Staff Legal untuk "Kesalahan material pada dokumen final" dan "Isu risiko yang terlambat dieskalasi" kosong; KPI semua jabatan menunggu KPI Matrix (tidak ada di korpus) | Aziz |
| 10 | Apakah Authority Matrix, matriks otorisasi, dan DoA satu dokumen; dokumen itu belum ada (SOP Legal menyebut matriks DoA "belum disusun" menurut audit) | Legal, Aziz |
| 11 | Pemetaan Finance Lead dan Finance Staff ke JA-10 dan JA-11 (atau jabatan baru) | owner, FAT |
| 12 | Arti "SIP" pada "eligible collection SIP" (JA-10 butir 3) tidak dijelaskan di sumber | FAT |
| 13 | Jam masuk, jam pulang, dan jumlah jam kerja per hari tidak ada di PP BAB VI (hanya BAB VI yang saya baca). Lingkungan dan kondisi fisik tiap jabatan adalah USULAN U3; Aziz memastikan atau mengganti per jabatan. Bila ada bab PP atau SK jam kerja, kutip angkanya | Aziz |
| 14 | Masa pengalaman minimum menunggu job evaluation; sertifikasi menunggu Competency Matrix. Belum ada keduanya | Aziz |
| 15 | HR-JA-001 bernomor "usulan, validasi Document Control"; dua jobdesk Legal tidak bernomor. Validasi nomor dan arsip HR-JA-001 revisi 03 sesudah SNX-HR-JA-01 disahkan | Aziz |
| 16 | SNX-HR-ORG-01 (matriks peran ISO) belum ada saat dokumen ini disusun; rujukan di bagian 3, 8, 10 bergantung padanya | owner |
| 17 | SOP Legal (SNX-LEG-SOP-01): SLA review kontrak (usulan) dan "Staff Legal (Senior/Junior)" tidak saya periksa; KPI Line Manager Legal dan kualifikasi Staff Legal perlu diselaraskan | Legal |
| 18 | Penyebutan Zammad pada JA-04 butir 3 dan JA-13 butir 1 dan 6 mengikuti kata owner 14 Okt (Zammad untuk Ops). Batas "generalist" belum dirinci | owner |
| 19 | Tanggal efektif, tanda tangan, dan status tetap kosong atau Draft sampai Samuel menandatangani | Samuel |
| 20 | Pola kerja JA-13 (shift atau jam kantor) dan jam shift 07:00, 15:00, 23:00 WIB menunggu keputusan COO atas POL-OPS-001 (DRAFT v0.1; pemetaan JA-13 ke NOC belum dikonfirmasi di sumber). JA-04 dan JA-02 mengikuti pola 24/7 dan P1 dari draf yang sama | owner |
| 21 | specs/HR-ORG-01.json (DONE) menulis atasan JA-03, JA-04, JA-05, JA-08, JA-10, JA-11, JA-14 sebagai "Direktur (JA-02)" dan tidak membedakan JA-08 dan JA-09 di daftar jabatan, sedangkan dokumen ini menulis "COO" dan "COO atau Management (menunggu konfirmasi)". Perlu diselaraskan di salah satu dokumen. Saya tidak boleh menulis di spec itu | owner, Aziz |

## Penanganan temuan nonblocking putaran 1 (qa/HR-JA-01.verify.r1.json)

| Temuan | Penanganan |
|---|---|
| Kualifikasi ganda bagian 6 (K2) lawan bagian 7 tanpa penjelasan | Satu kalimat di pengantar bagian 7: kualifikasi bagian 7 lebih spesifik, bila disahkan berlaku untuk JA-08 dan JA-09, dan masa pengalaman butir 4.7 mengikuti angka di sana (USULAN U11) |
| HR-ORG-01 dan HR-JA-01 berbeda untuk atasan (Direktur lawan COO) dan pembeda JA-08, JA-09 | Tidak diubah: spec HR-ORG-01 bukan milik saya. Open item 21 |
| "SNX-HR-ORG-01 ... (bagian 3 dan 8)" ambigu | Diganti "dirujuk di bagian 3 dan 8 dokumen ini" |
| Sinonim peninjauan hukum, review, reviewer; "IT/Keamanan" dan "IT" | Dipertahankan sebagai kata tim (T1); asumsi 13 |
| Butir 4.9 tanpa pelaku | Diganti "Dokumen ini membagi persyaratan pendidikan dan pengalaman dalam empat kelompok." Butir 4.7 tetap (kalimat sumber) |
| Zammad tidak di HR-JA-001 | Tidak diubah; open item 18 |
| Temuan lain (nama, cacat audit, batas keras, format) | Verifikator menyatakan cocok; tidak ada tindakan |

## Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan perbaikannya:
- Baris tabel Acuan ISO menulis klaim hasil ("ditetapkan, dikomunikasikan, dan dipahami", "sehingga pemegang jabatan mengetahui tugas dan wewenangnya"). Terdengar seperti kalimat standar yang ditempel dan menjanjikan lebih dari yang dikerjakan dokumen. Saya ganti dengan apa yang dokumen lakukan dan menulis bahwa penilaian kompetensi aktual berada di luar dokumen.
- Tabel Definisi mengulang aturan yang sudah ada di butir 4 (garis resmi, sertifikasi, masa pengalaman). Saya pangkas menjadi arti istilah. Satu definisi melingkar (Jabatan memakai pemegang jabatan, pemegang jabatan memakai jabatan) saya putus, dan istilah "Persyaratan jabatan" yang didefinisikan tetapi tidak dipakai saya ganti "Kualifikasi".
- Penyebutan sumber berganti-ganti ("Job Analysis sumber", "Sumber", "HR-JA-001"). Saya seragamkan menjadi HR-JA-001 dan "Sumber dokumen ini". Frasa "usulan (USULAN)" yang ganda saya hapus.
- Yang masih terdengar mekanis dan sengaja dibiarkan: "Kelompok K1, lihat butir 4.9" berulang 15 kali, daftar kompetensi satu sel dengan titik koma, dan baris 27001 5.3 serta 7.2 yang berbunyi "Sama dengan ISO 9001:2015". Ketiganya benar dan menghindari penyalinan kalimat yang sama ke banyak tempat.
- Tidak ada pembuka generik, penutup positif, em-dash, tebal, tanda kutip penekanan, "tidak hanya ... tetapi juga", atau kata kosong. Hedging hanya satu: "paling mungkin" di bagian 9. Kalimat tugas berawalan "Me-" berderet adalah suara tim dan dipertahankan sesuai T1.
- Putaran 1: baris "Kondisi kerja" 13 dari 15 jabatan memakai pembuka sama "ruang kantor, kerja menetap dengan komputer" dan 14 dari 15 memuat "bahaya fisik rendah". Itu terdengar seperti templat, dan memang bukan fakta tim. Saya biarkan karena frasa itu satu-satunya klaim yang berlabel USULAN pada sel tersebut, bagian bersumber (pola kerja dan risiko kerja) berbeda tiap jabatan dengan rujukan butir, dan pembeda nyata (JA-13 shift, JA-15 kerja fisik, pertemuan luar kantor) ditulis spesifik. Aziz sebaiknya mengganti frasa itu per jabatan bila fakta lapangan berbeda.
- Putaran 1: setiap sel Kondisi kerja berformat "Pola kerja ... Lingkungan dan kondisi fisik ... Risiko kerja ..." dan butir 4.10 ditulis tiga paragraf pendek. Struktur kembar ini terbaca mekanis, tetapi memudahkan auditor membandingkan jabatan.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka: 15 jabatan, 12 bulan, 90, 60, dan 30 hari, 1 hari kerja, 2 hari kerja, 90%, 100%, 0, 5 tahun, 1 sampai 2 tahun, semuanya dari tiga sumber. Tidak ada tanggal di dokumen.
- Nama dan jabatan: semuanya dari sumber atau defaults.json. Nama baru tidak ada.
- Tanpa sumber langsung: (a) Zammad di JA-04 dan JA-13, dari kata owner di defaults (open item 18); (b) pelaku HR Manager pada peninjauan tahunan, dari process owner (asumsi 6); (c) label K1 sampai K4; (d) definisi Management, Job evaluation, dan Competency Matrix yang saya tulis dari konteks kalimat sumber; (e) kode SNX pada Dokumen terkait, dari worklist; (f) klausul dan judul ISO, berlabel USULAN; (g) uraian APD; (h) tiga butir yang saya baca dari audit dan tidak dari Drive: pemakaian Finance Lead dan Finance Staff di SOP FAT, SLA SOP Legal, "Staff Legal (Senior/Junior)".
- Sudah saya perbaiki di teks: klaim hasil pada baris ISO (di atas) dan "dikomunikasikan dan dipahami" yang tidak bisa dibuktikan dari dokumen.
- Putaran 1: tanpa sumber langsung sekarang tambahan: (i) lingkungan dan kondisi fisik 15 jabatan (U3, berlabel); (ii) jam masuk dan pulang "mengikuti Peraturan Perusahaan" (U10, berlabel; angka tidak ditulis); (iii) "lokasi kerja utama semua jabatan" dari alamat kantor di footer template (tafsir, asumsi 14); (iv) rujukan ISO 9001:2015 7.1.4 dan ISO/IEC 27001:2022 Annex A 6.7 (berlabel lewat kalimat pembuka bagian 11). Angka baru hanya jam shift 07:00, 15:00, 23:00 WIB dan "tiga shift 8 jam", dari POL-OPS-001 bagian 5 dan ditulis sebagai usulan draf. Tidak ada nama atau tanggal baru.
