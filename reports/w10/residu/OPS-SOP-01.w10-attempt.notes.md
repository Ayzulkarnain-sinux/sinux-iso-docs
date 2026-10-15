# Catatan penyusun OPS-SOP-01: SOP Project Management & Delivery

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-SOP-01.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-SOP-01 (nomor lama dipertahankan), department Operation, klasifikasi RESTRICTED (Internal) mengikuti label sumber (worklist null), audit_class C1. Process owner = "Service Delivery Manager" (jabatan tanpa nama, ikut "Pemilik dokumen" di sumber). Approval persis defaults: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revisi 00, tanggal efektif kosong, revision_desc "Draft awal untuk review dan pengesahan".

Uji terakhir (sesudah putaran perbaikan istilah, lihat bagian terakhir):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-SOP-01.json /tmp/pen-OPS-SOP-01/OPS-SOP-01.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-OPS-SOP-01/OPS-SOP-01.docx sop` memberi `"pass": true`, `"fails": []`, satu warn: "10 butir (USULAN) menunggu ACC" (10 kemunculan teks, 7 butir berbeda, lihat bagian USULAN). Warn PIC SLA nol.
- Validator OOXML skill docx (`validate.py`, dijalankan dari foldernya): "All validations PASSED!".
- Diagram PNG dibuka: 14 simpul, rankdir TB, tinggi 17,4 cm pada lebar 15,5 cm (di bawah batas 19 cm), teks terbaca.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-SOP-01_SOP_Project_Management_Delivery.docx (218390 byte) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo | 2026-10-13T06:09:03Z (get_file_metadata, dicek hari ini) | read_file_content (teks), download_file_content (docx didekode ke /tmp/pen-OPS-SOP-01/src/); comments.xml dan footnotes.xml tanpa teks; gambar word/media/rId25.png (diagram alur) dibuka |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan saja | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata) | read_file_content |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan saja | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata) | read_file_content |
| Kriteria penerimaan | config/checklist.json baris 63 | Description hanya nama berkas ("SNX-OPS-SOP-01_SOP_Project_Management_Delivery.docx") | Kriteria = substansi sumber tim + acuan ISO 9001:2015 "8.1, 8.2, 8.5.1, 8.6" dan ISO/IEC 27001:2022 "5.8, 5.37" |
| Pendukung lintas dokumen | specs/HR-ORG-01.json (nama peran), notes dan specs OPS-FRM-01, 03, 04, 05, 06 (isi form yang dirujuk SOP ini), context/audit (bagian 5 Catatan kualitas dan celah) | salinan lokal | Dibaca sebagai DATA. Isi form diambil dari notes lane lain, bukan dibuka ulang di Drive; bisa basi bila tim mengubah form |

Kalimat perintah di dalam sumber (data, bukan instruksi): nihil. Semua kalimat sumber menyatakan langkah kerja SOP, bukan perintah kepada pekerja.

POL-OPS-001 dan PRO-OPS-001 lebih baru (09:06) daripada SOP-01 (06:09). Sesuai prioritas RUNBOOK §6 (dokumen tim terbaru menang), label (USULAN) di dua dokumen itu dipakai untuk angka yang sama di SOP-01.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Scope berjalan dari gate G1 sampai gate G3 | "Berlaku sejak paket handover diterima dari Commercial (gate G1) sampai proyek ditutup dan layanan diserahkan ke operasi (gate G3)." (Bagian 2 Ruang lingkup) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo |
| 2 | Tiga ambang waktu SOP: kick-off internal 3 hari kerja setelah PO, eskalasi ke COO bila deviasi jadwal lebih dari 1 minggu, hypercare 2 minggu. Di SOP-01 tanpa label; di POL dan PRO yang lebih baru berlabel USULAN | SOP-01: "Kick-off internal dilaksanakan paling lambat 3 hari kerja setelah PO" (6.1 butir 5); "Deviasi jadwal lebih dari 1 minggu dari baseline, atau isu yang menyentuh biaya, dieskalasi ke COO." (6.4 butir 5); "Hypercare berjalan 2 minggu setelah go-live, kecuali kontrak menetapkan lain." (6.6 butir 3). PRO: "dalam 3 hari kerja sejak PO. (USULAN)" (SDPM-01); "(USULAN ambang)" (SDPM-02); "(USULAN 2 minggu)" (tabel 8.1 baris 10). POL: "Durasi hypercare standar 2 minggu. (USULAN)" (bagian 8) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo; 1U8CAdibwBk9x_-Aic2lbev144d6WReTz; 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |
| 3 | Gate G1: Project Manager memeriksa paket, Service Delivery Manager memutus menerima atau menolak | SOP-01: "Project Manager menerima paket handover dari Commercial dan memeriksanya dengan checklist G1 pada SNX-OPS-FRM-01 (sheet Checklist G1)." (6.1 butir 1) dan "Service Delivery Manager \| Pemilik SOP; menerima atau menolak paket G1; mengawal hubungan pelanggan; menyetujui closure" (Bagian 5). POL: "G1 Kick-off \| Commercial \| SD dan PM \| Service Delivery Manager" (bagian 8, kolom Pemilik gate) | 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo; 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv |

## 2. Fakta pendukung dan kutipan

| # | Fakta di dokumen | Kutipan verbatim | Posisi di spec |
|---|---|---|---|
| 1 | Tujuan | "SOP ini menetapkan cara SINUX merencanakan, melaksanakan, mengendalikan, dan menutup proyek implementasi dan migrasi pelanggan, sehingga hasilnya sesuai scope, jadwal, mutu, dan persyaratan keamanan informasi yang disepakati." | Purpose (kalimat tim utuh) |
| 2 | Jenis proyek dalam scope | "onboarding layanan Nusagrid, migrasi ke cloud, implementasi managed services, backup dan DR, observability, security, serta proyek gabungan bersama partner" | Scope paragraf 1 |
| 3 | Pemilik dokumen dan klasifikasi | "Pemilik dokumen \| Service Delivery Manager"; "Klasifikasi \| RESTRICTED (Internal)" | meta.process_owner, meta.classification |
| 4 | Pekerjaan production lewat change request dan go-gate | "Semua pekerjaan pada environment production pelanggan dijalankan melalui change request sesuai SNX-OPS-SOP-02, dengan go-gate: approval, backup, rollback satu perintah, satu langkah satu waktu, terdokumentasi." (6.3 butir 1) | Definisi Go-gate, butir 4.3, 6.3 butir 1 |
| 5 | Akses dan kredensial | "Akses ke sistem pelanggan hanya melalui Jumphost dan akun yang terdaftar di SNX-ISMS-REG-04. Kredensial disimpan di password manager, tidak di chat, tiket, atau dokumen." (6.3 butir 2) | Butir 4.4 |
| 6 | Baseline disetujui sebelum eksekusi | "Baseline rencana disetujui Service Delivery Manager sebelum eksekusi." (6.2 butir 7) | Butir 4.2, 6.2 butir 8 |
| 7 | Keamanan informasi di perencanaan | "Tentukan persyaratan keamanan informasi proyek: klasifikasi data sesuai SNX-ISMS-PRO-01, kebutuhan akses sesuai SNX-ISMS-SOP-02, dan backup sebelum migrasi sesuai SNX-ISMS-SOP-03." (6.2 butir 5) | Butir 4.5, 6.2 butir 5 |
| 8 | Pelanggan pemerintah | "Untuk pelanggan pemerintah melalui main contractor, BAST dibuat atas nama SINUX, versi original disimpan di Drive, dan periode ditetapkan main contractor. Dokumen teknis tanpa harga, diskon, tier, maupun roadmap komersil." (6.5 butir 5) | Bagian 9 baris 4 ("komersil" jadi "komersial") |
| 9 | Checklist G3 belum lengkap | "Checklist belum lengkap berarti layanan tetap hypercare dengan pemilik SD dan PM." (6.6 butir 2) | Butir 4.7, Bagian 9 baris 2 |
| 10 | Lessons learned dan arsip | "Lessons learned disetor ke knowledge base SINUX melalui jalur staging; dokumen proyek diarsip sesuai masa simpan." (6.6 butir 5) | 6.6 butir 6 dan 7 (frasa "jalur staging" dibuang) |
| 11 | Retensi rekaman | "Project plan, scope, timeline, checklist G1 \| SNX-OPS-FRM-01 \| Drive proyek \| Durasi kontrak + 3 tahun"; "Change request log \| SNX-OPS-FRM-04 \| Service Hub, Drive \| 3 tahun"; "BAST, checklist G3, closure report \| SNX-OPS-FRM-06 \| Drive proyek (original bertanda tangan) \| Durasi kontrak + 5 tahun" | Bagian 11 tabel Rekaman |
| 12 | Target kinerja | "Proyek selesai sesuai jadwal baseline \| 80% \| SNX-OPS-FRM-01"; "Onboarding live sesuai tanggal kontrak \| 90% \| SNX-OPS-FRM-01"; "Laporan progres terkirim tepat waktu \| 100% \| SNX-OPS-FRM-03"; "Proyek ditutup dengan BAST dan closure report lengkap \| 100% \| SNX-OPS-FRM-06"; "Target di atas adalah target awal dan dikalibrasi setelah 3 bulan data." | Bagian 8 (baris 7 sampai 10), Kesimpulan |
| 13 | Pemilik rekaman | FRM-01, 02, 03, 05: "Pemilik dokumen \| Project Manager"; FRM-04: "Pemilik dokumen \| Head of Operation"; FRM-06: "Pemilik dokumen \| Service Delivery Manager" (dari notes OPS-FRM-01 sampai 06, bukan dibuka ulang di Drive) | Bagian 11 kolom Lokasi dan pemilik |
| 14 | Penandatangan UAT | "Penguji SINUX (Project Manager)", "Perwakilan pelanggan", "Service Delivery Manager" (blok tanda tangan FRM-05, dari notes OPS-FRM-05) | 6.5 butir 1 dan 6 |
| 15 | Keputusan G1 di FRM-01 | "Pemilik gate: Service Delivery Manager. Gate LOLOS bila tidak ada butir berstatus Belum." (Checklist G1!A2) dan rumus C14 `=IF(COUNTIF(C5:C12,"Belum")=0,"LOLOS","TAHAN")` (dari notes OPS-FRM-01) | Butir 4.1, 6.1 butir 2 |
| 16 | Head of Operation menolak G3 | POL: "Operation berhak menolak serah terima G3 secara tertulis bila checklist belum lengkap." (bagian 8); "Wewenang: ... menolak serah terima G3." (9.1) | Peran Head of Operation, Bagian 9 baris 2 |
| 17 | Gate G2 dan G3 dimiliki Project Manager dan Head of Operation | SOP-01 Bagian 5: "pemilik G2"; "Pemilik gate G3; eskalasi isu lintas sub divisi" | Peran |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Bagian 11 (acuan) | Tercermin di bagian 4 | Prosedur |
|---|---|---|---|
| ISO 9001:2015 8.1 | Ya | 4.2 (baseline sebelum eksekusi) | 6.2 butir 8 |
| ISO 9001:2015 8.2 (sumber tim juga menyebut 8.2.2 dan 8.2.3, dipertahankan sebagai "termasuk") | Ya | 4.1 (paket G1), 4.6 (perubahan) | 6.1 butir 1 sampai 2, 6.2 butir 6, 6.4 butir 6 |
| ISO 9001:2015 8.5.1 | Ya | 4.3 (pekerjaan production lewat change request dan go-gate) | 6.3 |
| ISO 9001:2015 8.6 | Ya | 4.7 (BAST sesudah UAT, serah terima sesudah checklist G3) | 6.5, 6.6 |
| ISO/IEC 27001:2022 Annex A 5.8 | Ya | 4.4 (akses dan kredensial), 4.5 (keamanan informasi proyek) | 6.1 butir 4, 6.2 butir 5, 6.3 butir 2 |
| ISO/IEC 27001:2022 Annex A 5.37 | Ya | 4.3 dan 4.8 (prosedur dan rekaman terdokumentasi) | seluruh bagian 6 |

Pemetaan 4.8 dan 5.37 adalah tafsir penyusun terhadap kriteria baris; sumber tim hanya menyebut 5.8 di Referensi dan "8.1, 8.2, 8.5.1, 8.6" di atribut. Nama klausul (Operational planning and control dan seterusnya) adalah judul baku standar dalam bahasa aslinya, bukan dari dokumen tim.

## 4. Keputusan data dan nama

| Butir | Keputusan | Dasar |
|---|---|---|
| Approval | Persis defaults. Sumber menulis "Disusun oleh Service Delivery Manager", "Diperiksa oleh ISO/ISMS Coordinator", "Disetujui oleh COO, Amirull Yusuf Zulkarnain"; tidak dibawa | config/defaults.json prepared_reviewed.OPS dan approved_by (D2) |
| Sebutan COO | Pertama kali muncul di baris Definisi "Direktur (COO)" (Bagian 3), sesudahnya "COO" (11 kali). Nama orangnya tidak ditulis | data_conflicts, butir "Sebutan Amirull Yusuf Zulkarnain"; HR-ORG-01 (JA-02 Direktur, definisi "Direktur (COO)") |
| Direktur Utama | Tidak muncul di badan dokumen; hanya "President Director" di blok Approved By | data_conflicts, butir "Sebutan Samuel Kristanto Utomo" |
| Sistem tiket | Satu-satunya tempat tiket muncul: kolom Lokasi rekaman Change request log. Sumber menulis "Service Hub"; diganti "tiket change request di Zammad (USULAN)" dengan preseden OPS-FRM-04 (B18) dan OPS-FRM-03. GLPI tidak disebut karena tidak ada proses generalist di SOP ini | defaults.ticketing ("sistem tiket zammad untuk ops, glpi untuk generalist") |
| Vault | Sumber hanya menulis "password manager". Definisi memakai rumusan preseden ISMS-SOP-02: "Penyimpanan kredensial internal SINUX (vault). Status operasional: menunggu konfirmasi Ops." | data_conflicts; RUNBOOK §6 |
| PPN | Tidak ada di SOP ini | |
| Department | "Operation" | defaults.department_labels.OPS |
| Klasifikasi | "RESTRICTED (Internal)" mengikuti label sumber; footer berlabel otomatis | defaults.classification.rule |

### Pemetaan peran sumber ke nama peran HR-ORG-01

| Peran di sumber | Peran di dokumen | Catatan |
|---|---|---|
| Service Delivery Manager, Project Manager, Head of Operation | sama | Ada di HR-ORG-01 "Struktur Divisi Operation", berstatus USULAN tanpa pemegang (K-10) |
| NOC dan SOC | NOC Engineer, SOC Analyst (provisioning, konfigurasi, aset, defect); Lead NOC, Lead SOC (menerima layanan di G3) | Sumber memakai satu baris "NOC dan SOC" untuk dua kegiatan. Pemisahan mengikuti 6.6 butir 2 ("Lead NOC dan Lead SOC") dan blok tanda tangan G3 di FRM-06 ("Menerima (Lead NOC)", "Menerima (Lead SOC...)") |
| Tech dan Product | Manager of Product Tech | JA-05, jabatan terdekat. Sumber menunjuk tim, HR-ORG-01 menunjuk satu jabatan; lihat open item 9 |
| Commercial (peran) | VP Commercial | JA-03. Kata "Commercial" dipertahankan untuk unit (definisi Commercial) |
| COO | COO (setelah "Direktur (COO)") | JA-02 |
| ISO/ISMS Coordinator | Tidak dipakai di badan | Hanya ada di blok Pengesahan sumber, yang diganti defaults. HR-ORG-01 K-13: belum ditetapkan |
| SD dan PM (sub divisi) | Didefinisikan sebagai sub divisi; peran bernama (Service Delivery Manager dan Project Manager) dipakai di PIC | HR-ORG-01 "Struktur Divisi Operation" |

## 5. Penanganan cacat context/audit (bagian 5, fileId 1lv4ALJnqGG9s9cHnzz38yOTJC57pmPgo, plus POL dan PRO yang relevan)

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Status DRAFT, persetujuan "Menunggu", tanda tangan dan tanggal kosong, dua baris riwayat revisi bernomor sama | Teratasi template: satu baris Revision 00 dengan revision_desc dari prompt, Effective Date kosong, kolom Signature kosong |
| 2 | "keselarasan RTO dan target pulih" di baris riwayat kedua tanpa padanan di isi | Tidak dibawa. SOP ini tidak membahas RTO atau target pulih; frasa itu hanya ada di riwayat revisi sumber (open item 15) |
| 3 | Hypercare 2 minggu tanpa label USULAN; POL dan PRO menulisnya USULAN; pemilik hypercare berbeda (SOP-01 dan POL bagian 8: SD dan PM; PRO tabel 8.1 baris 10 dan POL 9.2: Lead NOC); PRO menaruh hypercare sesudah G3, SOP-01 sesudah pemeriksaan checklist G3 | Diberi label (USULAN) di 6.6 butir 3, Bagian 8, dan diagram. Pemilik tetap Service Delivery Manager dan Project Manager (kalimat SOP-01), dengan baris pengecualian "Kontrak menetapkan durasi hypercare selain 2 minggu". Konflik pemilik dan urutan tidak diputus diam-diam: open item 3 dan 4 |
| 4 | Kick-off internal 3 hari kerja dan ambang eskalasi 1 minggu tanpa label USULAN | Diberi label (USULAN) di 6.1 butir 5, 6.4 butir 8, dan Bagian 8 (dasar: PRO SDPM-01 dan SDPM-02, lihat Fakta kunci 2) |
| 5 | Gate G1: Bagian 5 menulis SDM menerima atau menolak, langkah 6.1 menulis PM menerima dan memeriksa; pembagian tidak eksplisit | Dipertegas: PM menerima dan memeriksa (6.1 butir 1), SDM memutus (6.1 butir 2, butir 4.1, peran SDM sebagai pemilik gate G1), SDM mengembalikan paket yang ditolak (Bagian 9 baris 1). Dasar: POL bagian 8 dan 9.4, PRO SDPM-01, FRM-01 Checklist G1!A2. Open item 8 |
| 6 | Rujukan sheet FRM-01 dan bagian FRM-06 cocok dengan sumber form | Dipertahankan ("Checklist G1", "WBS dan Timeline"; sheet "Milestone" ditambah di 6.2 butir 2 karena ada di FRM-01 menurut notes OPS-FRM-01). Nomor butir SOP-01 yang dirujuk FRM-01 (Bagian 6.4), FRM-03 (6.2 butir 3, 6.4), FRM-06 (6.5, 6.6) tetap cocok karena penomoran 6.1 sampai 6.6 dan urutan butir tidak diubah |
| 7 | Sumber data dua KPI: SOP-01 menulis SNX-OPS-FRM-01, POL bagian 11 menulis "Register proyek" dan "Service Hub" | SOP-01 dipertahankan (FRM-01 sebagai sumber data); open item 7 |
| 8 | SOP tidak merujuk POL-OPS-001 dan PRO-OPS-001 | POL-OPS-001 dirujuk di definisi sub divisi dan masuk Dokumen terkait; PRO-OPS-001 masuk Dokumen terkait dengan SDPM-01, SDPM-02, SVC-01. Keduanya diberi catatan "DRAFT v0.1, penomoran masih USULAN" |
| 9 | "Lessons learned disetor ke knowledge base SINUX melalui jalur staging" | Frasa "jalur staging" dibuang (RUNBOOK §0 butir 6). Langkah menjadi "Masukkan lessons learned proyek ke knowledge base SINUX". Cara memasukkan tidak dijelaskan sumber; open item 5 |
| POL 4 | Baseline KPI belum ada; target awal | Kalimat tim "target awal ... dikalibrasi setelah 3 bulan data" dipertahankan di Kesimpulan; kolom Timing memakai "Target awal". Angka 80% dan 90% berlabel (USULAN) mengikuti POL bagian 11 |
| POL 6 | P-08 GLPI lawan Zammad di dokumen lain | Zammad (USULAN) untuk tiket change request, lihat bagian 4 |
| POL 7, PRO 8 | Rujukan internal AI (DOCTRINE, DEC, HANDOVER, SKILL_, SINUX_SERVICE_HUB, CLAIM_CLASS_POLICY) | Tidak dibawa; SOP-01 tidak memuatnya. Lint lulus |
| PRO 2, 9 | USULAN SDPM dan tidak ada klausul ISO atau retensi | Label USULAN dibawa untuk angka yang sama (butir 3 dan 4 di atas). Klausul ISO dari kriteria baris; retensi dari tabel Record SOP-01 |

Cacat tambahan yang saya temukan di luar daftar audit:

| # | Temuan | Penanganan |
|---|---|---|
| A | Definisi Project charter memuat "risiko awal", padahal 6.1 butir 3 mendaftar isi charter tanpa risiko dan memindahkan risiko awal ke FRM-02 (butir 4). Di PRO SDPM-02 charter memuat risiko awal | Definisi disamakan dengan butir 3 sumber (tanpa risiko awal); risiko awal tetap di FRM-02 |
| B | Diagram sumber menulis "Kick-off internal dan pelanggan, maksimal 3 hari kerja sejak PO". Teks: 3 hari hanya untuk kick-off internal; kick-off pelanggan ada di 6.2 | Diagram baru memisahkan: kick-off internal di simpul charter (tanpa angka, angka ada di Bagian 8), kick-off pelanggan di simpul perencanaan |
| C | Diagram sumber: "Perbaiki defect" dan "Kembalikan ke Commercial" tanpa panah kembali; teks 6.5 butir 2 menyebut uji ulang | "Uji ulang" digambar kembali ke "UAT lolos?" (sesuai 6.5). Paket yang dikembalikan menjadi simpul akhir sesuai teks "proyek belum dimulai" |
| D | Legenda gambar sumber (kotak biru dan oranye) tidak berlaku: renderer tidak mewarnai simpul | Legenda tidak dibawa. Garis putus-putus dari Change request proyek ke "Pantau dan lapor mingguan" dipertahankan |
| E | Diagram sumber berhenti di "Hypercare lalu closure"; sumber punya cabang "checklist belum lengkap" di teks | Cabang ditambah di diagram (simpul "Checklist G3 lengkap?" dengan jalan kembali berlabel "Setelah dilengkapi"), mengikuti 6.6 butir 2 |
| F | Definisi gabungan "Gate G1, G2, G3" | Dipecah tiga baris |
| G | "komersil" | Ditulis "komersial" |
| H | Atribut sumber "Masa simpan record: Berlaku sampai digantikan" bertentangan dengan tabel Record (3 tahun, 5 tahun) | Template tidak punya medan itu. Hanya tabel Rekaman Bagian 11 yang berlaku |
| I | Sumber memakai "paket handover" dan "paket G1" bergantian, "closure" dan "closure report" bergantian | Disatukan jadi "paket G1" (didefinisikan) dan "closure report" |
| J | Bagian Referensi sumber tidak punya padanan di template | Klausul ISO ke Bagian 11 (Acuan standar), dokumen SNX ke Dokumen terkait |

## 6. Asumsi dan tafsir (tidak tertulis eksplisit di sumber)

1. Kalimat pasif sumber diberi pelaku dari tabel peran, dengan rujukan bila ada: Project Manager menyusun laporan progres, mengirimnya, meninjau risiko, mengajukan change request proyek, dan mengeskalasi ke COO (PRO SDPM-02; POL 9.4); Project Manager menjalankan uji, mencatat defect, uji ulang, dan UAT (blok "Penguji SINUX (Project Manager)" di FRM-05); NOC Engineer dan SOC Analyst menjalankan perubahan production, mencatat aset, menyerahkan pekerjaan app-level, dan memperbaiki defect (sumber: "NOC dan SOC: Melaksanakan provisioning dan konfigurasi"; PRO NOC-02 dan SOC-02 untuk handoff app-level); Service Delivery Manager mengembalikan paket G1 yang ditolak (pemilik gate G1). Pelaku perbaikan defect dan pencatat aset adalah tafsir paling lemah.
2. Kolom Authority tabel peran tidak ada di sumber. Isinya diturunkan dari kalimat sumber ("pemilik G2", "pemilik gate G3", "memutus perubahan harga dan scope komersial", "Keputusan atas deviasi biaya, scope besar, dan change Major", "reviewer teknis") dan dari POL 9.1 (menolak serah terima G3).
3. Head of Operation sebagai pelaku "memeriksa checklist G3" dan Lead NOC dan Lead SOC sebagai penerima mengikuti 6.6 butir 2 dan blok tanda tangan G3 di FRM-06.
4. "Service Delivery Manager meninjau SOP ini setiap tahun" berasal dari review_period YEARLY (defaults) dan pemilik SOP (sumber); sumber tidak punya kalimat tentang peninjau. "Service Delivery Manager memantau kepatuhan lewat empat indikator" dan "melakukan kalibrasi" adalah tafsir dari "dikalibrasi setelah 3 bulan data" (pasif di sumber).
5. PIC empat KPI = Project Manager, karena pemilik rekaman sumber data (FRM-01, FRM-03; FRM-06 bagian penutupan disusun Project Manager). Sumber KPI tidak menyebut PIC.
6. Pengecualian scope (pekerjaan app-level, keputusan harga dan komersial, tahap sebelum G1, layanan BAU sesudah G3) diturunkan dari 6.3 butir 4, 6.4 butir 4, dan batas scope G1 sampai G3. Sumber SOP-01 tidak punya daftar pengecualian (RUNBOOK butir "Scope menyebut yang dikecualikan"). POL bagian 2 menulis daftar yang lebih luas (termasuk SOC POLRI); open item 12.
7. Definisi umum (Go-live, PIC, PO, DR, UAT, BAST, BAU, Jumphost, Main contractor, Network Operations Center dan Security Operations Center) adalah penjelasan penyusun dari pemakaian di sumber dan di PRO, bukan kalimat tim. Tidak memuat angka, nama, atau tanggal.
8. Frasa "Putuskan perubahan harga dan scope komersial" oleh VP Commercial: sumber menulis "Commercial" (unit); VP Commercial adalah jabatan terdekat di HR-ORG-01.
9. Label (USULAN) tidak diberikan pada nama jabatan Divisi Operation di tiap baris. Satu label di definisi "NOC, SOC, SD dan PM" mewakili status USULAN delapan jabatan di POL-OPS-001 (HR-ORG-01 K-10).
10. Keluaran langkah yang sumbernya tidak menyebut lokasi rekaman ditulis sebagai hasil kerja saja ("Kick-off internal terlaksana", "Rencana komunikasi proyek", "Baseline rencana disetujui", "Eskalasi ke COO"), tanpa mengarang lokasi.

## USULAN

Sepuluh kemunculan label (USULAN) di teks dokumen, tujuh butir berbeda. Tiap butir punya pemutus yang disarankan. Diagram juga memuat label (USULAN) pada simpul hypercare; itu butir U3.

| # | Butir USULAN | Lokasi di spec | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Kick-off internal paling lambat 3 hari kerja setelah PO | 6.1 butir 5; Bagian 8 baris 1 | Angka dari SOP-01; berlabel USULAN di PRO SDPM-01 yang lebih baru | Fani |
| U2 | Eskalasi ke COO bila deviasi jadwal lebih dari 1 minggu dari baseline | 6.4 butir 8; Bagian 8 baris 5 | Angka dari SOP-01; PRO SDPM-02 "(USULAN ambang)" | Fani |
| U3 | Hypercare 2 minggu setelah go-live, kecuali kontrak menetapkan lain | 6.6 butir 3; Bagian 8 baris 6; diagram simpul akhir | Angka dari SOP-01; POL bagian 8 dan PRO tabel 8.1 menulis USULAN | Fani |
| U4 | Target awal 80% proyek selesai sesuai jadwal baseline | Bagian 8 baris 7 | POL bagian 11: "target awal di bawah adalah USULAN" | Fani |
| U5 | Target awal 90% onboarding live sesuai tanggal kontrak | Bagian 8 baris 8 | Sama dengan U4 | Fani |
| U6 | Tiket change request di Zammad, menggantikan "Service Hub" di sumber | Bagian 11 tabel Rekaman, baris Change request log | Kata owner 14 Okt untuk Ops; penerapan ke change request adalah tafsir; preseden OPS-FRM-04 | Owner, dengan Fani |
| U7 | Nama jabatan Divisi Operation (Head of Operation, Lead NOC, NOC Engineer, Lead SOC, SOC Analyst, Service Delivery Manager, Project Manager) berstatus USULAN di POL-OPS-001 | Bagian 3, definisi "NOC, SOC, SD dan PM" | POL bagian 9 dan HR-ORG-01 K-10: nama jabatan, jenjang, headcount adalah USULAN yang disahkan COO | Owner, dengan Fani |

Target 100% (laporan progres tepat waktu, penutupan lengkap) tidak diberi label karena hanya ada di SOP-01 dan tidak dilawan dokumen lain; tetap berstatus "target awal".

## Open items

| # | Open item | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults.approved_by mengunci Samuel Kristanto Utomo / President Director (pembalik: form operasional disetujui COO bila owner memutus). Spec memakai defaults | Owner atau Samuel |
| 2 | Penyusun dan pemeriksa di sumber (Service Delivery Manager dan ISO/ISMS Coordinator) diganti Erik dan Fani menurut defaults. Peran ISMS Coordinator belum ditetapkan (HR-ORG-01 K-13) | Owner |
| 3 | Pemilik hypercare: SOP-01 dan POL bagian 8 menulis SD dan PM; PRO tabel 8.1 baris 10 dan POL 9.2 menulis Lead NOC. Dokumen mengikuti SOP-01 | Fani |
| 4 | Urutan hypercare dan G3: SOP-01 menaruh hypercare sesudah pemeriksaan checklist G3 (6.6 butir 2 dan 3); definisi tim menaruhnya sebelum layanan dinyatakan BAU; PRO tabel 8.1 menaruhnya sesudah G3. Spec mempertahankan urutan SOP-01 | Fani |
| 5 | Cara memasukkan lessons learned ke knowledge base SINUX tidak ada dokumennya; jalur internal di sumber dibuang dari dokumen. Pemilik langkah (Project Manager, dari POL 9.4) belum dikonfirmasi | Owner, dengan Fani |
| 6 | Batas "generalist" lawan Ops untuk sistem tiket belum dirinci owner. SOP ini hanya memakai Zammad untuk tiket change request (U6); SNX-OPS-FRM-04 di sumber menyebut Service Hub | Owner |
| 7 | Sumber data KPI "Proyek selesai sesuai jadwal baseline" dan "Onboarding live sesuai tanggal kontrak": SOP-01 FRM-01, POL bagian 11 "Register proyek" dan "Service Hub" | Fani |
| 8 | Pembagian gate G1 (Project Manager memeriksa, Service Delivery Manager memutus) adalah penegasan penyusun dari tiga lokasi sumber. Checklist G1 di FRM-01 berisi 8 butir, di PRO bagian 8.2 berisi 7 butir (menurut notes OPS-FRM-01); SOP ini merujuk FRM-01 | Fani |
| 9 | Pemetaan peran: Tech dan Product (tim) ke Manager of Product Tech, Commercial ke VP Commercial, NOC dan SOC ke NOC Engineer, SOC Analyst, Lead NOC, Lead SOC. Pelaksana serah paket G1 dari Commercial belum ditunjuk jabatannya | Owner, dengan Fani |
| 10 | Pelaku yang sumbernya pasif (asumsi 1): terutama perbaikan defect, pencatatan aset, dan penolakan G3 secara tertulis oleh Head of Operation (dari POL, bukan SOP-01) | Fani |
| 11 | Kick-off internal tidak punya rekaman di sumber; notulen hanya disebut untuk kick-off pelanggan. POL 9.4 menaruh notulen pada Project Coordinator (opsional), yang tidak disebut SOP-01 dan tidak ditambahkan | Fani |
| 12 | Daftar pengecualian scope diturunkan penyusun (asumsi 6); POL bagian 2 menulis daftar lebih luas | Fani |
| 13 | "Change Major" dan "scope besar" di peran COO merujuk SNX-OPS-SOP-02 yang belum dirender di lane ini; cek ulang istilah setelah SOP-02 selesai | Orkestrator |
| 14 | Isi form yang dirujuk (FRM-01 sampai FRM-06) dibaca dari notes lane lain, bukan dari Drive; bila tim mengubah form, rujukan sheet dan pemilik rekaman perlu dicek ulang | Orkestrator |
| 15 | Frasa riwayat revisi sumber "keselarasan RTO dan target pulih" tidak dibawa karena tidak punya padanan di isi SOP; riwayat revisi di template memakai satu baris | Fani |
| 16 | Status password manager (vault) di definisi: "menunggu konfirmasi Ops" | Ops |
| 17 | Judul klausul ISO di Bagian 11 memakai judul baku bahasa aslinya, dan pemetaan Annex A 5.37 ke butir 4.3 dan 4.8 adalah tafsir penyusun | Konsultan ISO |

## Jawaban dua pertanyaan akhir

### Apa yang membuat teks ini terdengar buatan AI

Saya membaca ulang spec dan menemukan enam hal, lalu memperbaikinya:

| Temuan | Perbaikan |
|---|---|
| Definisi BAU di draf pertama berbunyi "layanan berjalan rutin sesudah gate G3 lolos", yang bertentangan dengan langkah hypercare dan menaruh urutan yang tidak ada di sumber. Terdengar rapi tetapi menyatakan lebih dari sumber | Diganti "layanan berjalan rutin di bawah NOC dan SOC"; keluaran hypercare menjadi "Layanan dipantau ketat selama hypercare" |
| Frasa "sumber tim juga merujuk 8.2.2 dan 8.2.3" di acuan standar menyebut proses penyusunan, bukan isi dokumen | Diganti "termasuk 8.2.2 dan 8.2.3" |
| Butir 4.1 sampai 4.8 berpola sama ("Topik (klausul): aturan") dan 4.1, 4.2, 4.7 sama-sama memakai "hanya sesudah" | Pola dipertahankan karena kriteria baris menuntut klausul tercermin di bagian 4. 4.2 diubah menjadi "tidak dimulai sebelum" agar tidak berulang |
| Dua istilah untuk satu hal: "paket handover" dan "paket G1", "closure" dan "closure report", "production pelanggan" dan "environment production pelanggan" | Disatukan: "paket G1" didefinisikan, "closure report", "environment production pelanggan"; baris definisi Change request menyebut "change request proyek" sebagai bagian dari istilah yang sama |
| Kesimpulan bisa dibaca sebagai penutup umum | Isinya hanya dua kalimat berpelaku: pemantauan lewat empat indikator, kalibrasi sesudah 3 bulan data, peninjauan tiap tahun. Tanpa pujian |
| Daftar tiga yang tampak dipaksakan | Dicek: isi project charter (7 unsur), checklist, dan daftar jenis proyek mengikuti daftar sumber. Daftar "klasifikasi data, kebutuhan akses, backup" di 6.2 butir 5 adalah tiga rujukan dokumen yang nyata di sumber. Tidak ada tebal, huruf kapital, atau tanda kutip untuk penekanan, tidak ada em-dash atau en-dash, tidak ada atribusi kabur, tidak ada ekor penegas |

Kalimat tim dipertahankan apa adanya: Tujuan, kalimat jenis proyek di Scope, definisi Baseline, WBS, dan Hypercare, aturan akses dan kredensial (butir 4.4), langkah 6.1 butir 3 dan 4, 6.2 butir 1 sampai 4, 6.4 butir 1 dan 3, daftar isi charter, daftar teknis go-gate.

### Adakah fakta, angka, nama, atau tanggal tanpa sumber

Hasil pemeriksaan butir per butir terhadap spec:

| Butir di spec | Sumber |
|---|---|
| Nama dan jabatan di halaman approval | config/defaults.json (prepared_reviewed.OPS, approved_by); bukan dari sumber SOP |
| 3 hari kerja, 1 minggu, 2 minggu, 80%, 90%, 100%, 3 bulan, "Durasi kontrak + 3 tahun", "3 tahun", "Durasi kontrak + 5 tahun" | SOP-01 (6.1, 6.4, 6.6, Bagian 7 dan 8) |
| Kode SNX-OPS-FRM-01 sampai FRM-06, SNX-OPS-SOP-02, SNX-OPS-PRC-01, SNX-ISMS-PRO-01, SNX-ISMS-SOP-02, SNX-ISMS-SOP-03, SNX-ISMS-REG-01, SNX-ISMS-REG-04 | SOP-01 (Referensi, langkah, Record) |
| SNX-HR-ORG-01, POL-OPS-001, PRO-OPS-001 | specs/HR-ORG-01.json (nomor) dan dua berkas Drive bahan saja; penomoran POL dan PRO ditulis "masih USULAN" sesuai sumbernya |
| Judul dokumen terkait (mis. "Project Risk Register") | config/checklist.json dan notes lane lain (judul form), salinan audit (judul SOP-02, PRC-01, ISMS) |
| "Network Operations Center", "Security Operations Center" | Judul bagian 4 dan 5 PRO-OPS-001 |
| "LOLOS atau TAHAN", "butir berstatus Belum" | Formula dan petunjuk FRM-01 menurut notes OPS-FRM-01 (bukan dari SOP-01); bisa basi bila form berubah |
| Pemilik rekaman (Project Manager, Head of Operation, Service Delivery Manager) | "Pemilik dokumen" tiap form menurut notes OPS-FRM-01 sampai 06 |
| Head of Operation menolak serah terima G3 secara tertulis | POL bagian 8 dan 9.1, bukan SOP-01 |
| Pelaku langkah yang sumbernya pasif, pemetaan peran, pengecualian scope, definisi umum | Tafsir penyusun (bagian 6); hanya sebagian berlabel USULAN, sisanya open item 9 sampai 12 |
| Judul klausul ISO | Judul baku standar (bukan sumber tim); open item 17 |
| Tanggal | Tidak ada tanggal di spec. Tanggal efektif kosong; "13 Oktober 2026" (tanggal draft sumber) tidak dibawa |

Tidak ditemukan angka, nama, atau tanggal tanpa sumber yang tidak berlabel. Temuan dari pemeriksaan: definisi BAU (diperbaiki), dan pelaku langkah yang sumbernya pasif (dicatat sebagai asumsi dan open item, tidak diberi label karena bukan angka).

## Putaran perbaikan

Satu putaran penyusun, tanpa putaran lint. Render dan lint pertama sudah "pass": true. Perubahan sesudahnya hanya wording: BAU, "sumber tim", "hanya sesudah" di 4.2, penyatuan istilah (paket G1, closure report, environment production pelanggan), dan pengurutan baris definisi. Render, lint, dan validator OOXML dijalankan ulang sesudah perubahan terakhir dan semuanya lulus.

## W10 (bahasa, ISO-W10)
### W10 label dihapus
nihil. Definisi NOC, SOC, SD dan PM, asli: "Nama jabatan di dalamnya berstatus (USULAN) sampai POL-OPS-001 disahkan." Label dipindah ke akhir sel, status tetap usulan.

### W10 kalimat dihapus atau dipindah
- Scope: "(Bagian 6.3 butir 4)" dan "(Bagian 6.4 butir 7)" (rujukan beruntun).
- 4.5: "(Bagian 6.1 dan 6.2)".
- 4.7: "Checklist G3 yang belum lengkap ditangani sesuai Bagian 9." diganti faktanya dari bagian 9 (serah terima ditolak tertulis, layanan tetap hypercare).
- 6.1 langkah 2: "paket yang ditolak mengikuti Bagian 9." diganti faktanya (paket dikembalikan ke Commercial secara tertulis).
- 6.3 langkah 1: "(butir 4.3)"; langkah 2: "hanya sesuai butir 4.4" diganti faktanya (Jumphost, akun terdaftar di SNX-ISMS-REG-04).
- Bagian 9: "(butir 4.1)" dan "(butir 4.7)"; baris main contractor: pengulangan pelaku "Project Manager membuat dokumen teknis" disatukan ke kalimat pertama.
- Definisi Direktur (COO): "Selanjutnya ditulis COO." (pengulangan).
- Dokumen terkait SNX-HR-ORG-01: "di Bagian 5" menjadi "di SOP ini".

### W10 selisih angka
- 6.1 dan 6.2: hilang karena rujukan "(Bagian 6.1 dan 6.2)" di butir 4.5 dihapus; prosedur 6.1 dan 6.2 tetap ada.
- 6.3 dan 6.4: hilang karena rujukan "(Bagian 6.3 butir 4)" dan "(Bagian 6.4 butir 7)" di Scope dihapus; prosedur 6.3 dan 6.4 tetap ada.

### W10 catatan
- Pihak luar: "pelanggan" (dokumen induk OPS).
- "bila" diganti "jika"; "melakukan kalibrasi target setelah 3 bulan data" menjadi "mengalibrasi target setelah ada data 3 bulan".

### W10 putaran perbaikan 1 (qa/OPS-SOP-01.w10.r1.json)
- 4.7: fakta pengganti rujukan Bagian 9 dilengkapi: "dengan pemilik Service Delivery Manager dan Project Manager sampai checklist G3 lengkap".
- 6.3 langkah 2: fakta pengganti "hanya sesuai butir 4.4" dilengkapi dengan aturan kredensial butir 4.4: simpan kredensial hanya di password manager, tidak di chat, ticket, atau dokumen.
- 6.1 langkah 2: rujukan asli "paket yang ditolak mengikuti Bagian 9." dikembalikan, karena pengganti tidak memuat akibat "proyek belum dimulai" (penggantian di bagian kalimat dihapus di atas dibatalkan).
- Pointer lain yang dihapus (Scope, 4.5, 6.3 langkah 1, bagian 9) hanya rujukan dalam kurung tanpa fakta pengganti; isi kalimatnya tetap lengkap.
