# Catatan penyusun OPS-SOP-03: SOP Preventive & Corrective Maintenance

Status: DRAFTED (spec + notes ada). Spec: specs/OPS-SOP-03.json. Mode sop, aksi T1, wave W2, nomor SNX-OPS-SOP-03 (nomor lama dipertahankan), department Operation, classification "RESTRICTED (Internal)" mengikuti label sumber (worklist null), audit_class C1. Process owner "Lead NOC" (jabatan tanpa nama, dari "Pemilik dokumen | Lead NOC" di sumber). Approval persis dari config/defaults.json: prepared Erik Dwi Yanto / Technical/Operation Engineer L1, reviewed Fani Fatullah / VP Tech Operation and Services, approved Samuel Kristanto Utomo / President Director. Status Draft, revision 00, effective_date kosong, review_period YEARLY, revision_desc "Draft awal untuk review dan pengesahan".

Hasil uji terakhir (bukti mentah: /tmp/pen-OPS-SOP-03/lint.out.txt):
- `python3 -I tools/render_sop.py template/SOP_TEMPLATE.docx specs/OPS-SOP-03.json /tmp/pen-OPS-SOP-03/OPS-SOP-03.docx` selesai tanpa galat.
- `python3 -I tools/lint_doc.py /tmp/pen-OPS-SOP-03/OPS-SOP-03.docx sop` memberi `"pass": true`, `"fails": []`, satu warn "1 butir (USULAN) menunggu ACC". Warn PIC SLA nol.
- Pemeriksaan tambahan atas spec: semua PIC di langkah dan tabel SLA ada di tabel peran bagian 5; semua kode dokumen yang dirujuk ada di tabel Dokumen terkait; tiap kalimat langkah paling banyak 24 kata; pemindaian frasa terlarang dari prompt (em-dash, en-dash, ekor penegas, frasa pengisi, lindung nilai bertumpuk) nol temuan.
- Konversi soffice ke PDF: 15 halaman; halaman 11 (Process Flow) dilihat, diagram muat satu halaman. tools/selftest.sh tidak dijalankan (menulis ke direktori bersama penyusun paralel); tools dan template tidak diubah.

## 1. Sumber

| Sumber | fileId | modifiedTime | Cara baca |
|---|---|---|---|
| SNX-OPS-SOP-03_SOP_Preventive_Corrective_Maintenance.docx (174745 byte) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc | 2026-10-13T06:09:04Z (get_file_metadata hari ini, sama dengan prompt) | read_file_content (teks); download_file_content didekode ke /tmp/pen-OPS-SOP-03/src/src.docx dengan python3 -I; comments.xml dan footnotes.xml kosong; gambar word/media/rId25.png dibuka dan cocok dengan mermaid di salinan audit |
| POL-OPS-001_Kebijakan_Divisi_Operation_SINUX.docx (111296 byte), bahan | 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv | 2026-10-13T09:06:27.051Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| PRO-OPS-001_Prosedur_Operasional_Divisi_Operation_SINUX.docx (183366 byte), bahan | 1U8CAdibwBk9x_-Aic2lbev144d6WReTz | 2026-10-13T09:06:40.151Z (get_file_metadata, sama dengan prompt) | read_file_content (teks penuh) |
| Pembanding PIC aktivitas PM: SNX-OPS-FRM-07 (di luar daftar sumber prompt, dibaca saja) | 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB | tidak diukur ulang di sesi ini; notes/OPS-FRM-07.md mencatat 2026-10-13T06:09:21Z | read_file_content (teks); kolom PIC sheet Jadwal PM dan Cara pakai dikutip di bawah |
| Kriteria penerimaan | config/checklist.json baris 65 | Description hanya nama berkas | Kriteria = substansi sumber tim + ISO 9001:2015 "7.1.3, 8.5.1, 10.2" dan ISO/IEC 27001:2022 "7.13, 8.6" |
| Catatan cacat | context/audit/iso-sinux-supdocs-ops-2026-10-14.md: bagian SNX-OPS-SOP-03 (baris 4020 sampai 4225, bagian 5 mulai baris 4211), POL-OPS-001 (bagian 5 mulai baris 317), PRO-OPS-001 (bagian 5 mulai baris 720) | salinan audit 13 sampai 14 Okt | DATA, dicocokkan ulang ke teks Drive |
| Peran | specs/HR-ORG-01.json (status DONE), config/defaults.json | repo kerja | Nama peran: Lead NOC, NOC Engineer, Lead SOC, Service Delivery Manager, Head of Operation |

Kalimat perintah di sumber yang ditujukan ke penyusun: tidak ada. Kalimat imperatif di POL dan PRO adalah langkah prosedur dan diperlakukan sebagai isi.

## Fakta kunci

| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Lead NOC menyusun jadwal PM tahunan di SNX-OPS-FRM-07, paling lambat Desember | "Lead NOC menyusun jadwal PM tahunan pada SNX-OPS-FRM-07 (sheet Jadwal PM) paling lambat Desember untuk tahun berikutnya." (Bagian 6.1 butir 1) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |
| 2 | PM yang mengubah sistem berjalan sebagai change Standar atau Normal di window maintenance | "PM yang mengubah sistem (patch, restart, perubahan konfigurasi) dijalankan sebagai change Standar atau Normal sesuai SNX-OPS-SOP-02, di window maintenance." (Bagian 6.2 butir 2) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |
| 3 | Dua target kinerja: kepatuhan jadwal PM 95% dan uji restore bulanan 100% | "Kepatuhan jadwal PM (realisasi dibanding rencana) \| 95%" dan "Uji restore bulanan terlaksana per pelanggan backup \| 100%" (Bagian 9) | 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc |

## 2. Fakta pendukung dan kutipan

| # | Fakta | Kutipan verbatim | Posisi di dokumen |
|---|---|---|---|
| 1 | Tujuan | "SOP ini memastikan infrastruktur dan layanan yang dikelola SINUX dirawat secara terencana (preventive maintenance) dan diperbaiki secara terkendali saat terjadi kerusakan atau penurunan kinerja (corrective maintenance), sehingga availability layanan terjaga dan kejadian berulang dapat dicegah." (sumber Bagian 1) | Bagian 1, kalimat tim utuh |
| 2 | Scope | "Berlaku untuk perangkat, platform, dan layanan yang dikelola SINUX: VM dan platform Nusagrid, server WHM dan cPanel, network device, WAF dan proxy, sistem monitoring, sistem backup, serta sistem internal pendukung operasi (tiket, Jumphost, password manager). Perawatan fisik di data center dijalankan bersama penyedia DC sesuai kontraknya." | Bagian 2 |
| 3 | Pemilik dan masa simpan | "Pemilik dokumen \| Lead NOC"; "Masa simpan record \| Berlaku sampai digantikan"; tabel Bagian 8 "Jadwal PM dan service report \| SNX-OPS-FRM-07 \| 3 tahun" | meta.process_owner; bagian 11 |
| 4 | Window maintenance | "Window maintenance \| Jadwal yang disepakati untuk pekerjaan yang berdampak ke layanan, umumnya Shift 3 (23:00 sampai 07:00 WIB)" | Bagian 3 |
| 5 | Peran Lead SOC | "Lead SOC \| Menyetujui PM yang menyentuh kontrol keamanan; menyuplai daftar patch keamanan" | Bagian 4 dan 5, langkah 6.2 |
| 6 | Sembilan aktivitas PM dan frekuensi minimal | "Jadwal mencakup minimal aktivitas berikut:" lalu tabel 6.1 (health check tiap awal shift sampai uji pemulihan minimal tahunan) | Bagian 8, sembilan baris pertama setelah penyusunan jadwal |
| 7 | Service report dan tiket CM | "Engineer mengisi service report pada SNX-OPS-FRM-07 (sheet Service Report): aktivitas, temuan, tindakan, status, dan bukti." dan "Kerusakan atau penurunan kinerja dicatat sebagai tiket di SNX-OPS-FRM-08 dengan severity sesuai SNX-OPS-SOP-04." | 6.2 butir 3 (cakupan disesuaikan, lihat asumsi 6); 6.4 butir 1 dan 2 |
| 8 | Temuan berulang | "Temuan berulang pada aset yang sama dievaluasi sebagai masalah (problem) dan dapat memicu RCA sesuai SNX-OPS-FRM-10." | Bagian 4, 6.3 |
| 9 | Pengajuan change Normal 3 hari kerja (PRO-OPS-001 NOC-06, fileId 1U8CAdibwBk9x_-Aic2lbev144d6WReTz) | "Ajukan minimal 3 hari kerja sebelumnya lewat change request (CHG-01), kecuali emergency." (Pemicu NOC-06: "change Normal atau Major terjadwal") | 6.2 butir 3, baris SLA |
| 10 | Pelanggan tanpa backup (PRO-OPS-001 NOC-04) | "Jangan klaim bisa restore untuk pelanggan tanpa layanan backup." | Bagian 9 |
| 11 | Wewenang NOC Engineer (POL-OPS-001 9.2, fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv) | "Wewenang: blok ukur read-only kapan saja; blok ubah hanya dengan ACC tercatat." | Bagian 5, kolom Authority (istilah blok diganti) |
| 12 | Batas app-level pelanggan (POL-OPS-001 Bagian 2 dan P-05) | "Di luar ruang lingkup: app-level pelanggan (isi WordPress, plugin, DB aplikasi, kode pelanggan), keputusan harga dan komersial, serta SOC POLRI (tanggung jawab POLRI)." dan "Batas MSP: app-level (isi WordPress, plugin, DB aplikasi, kode pelanggan) = handoff ke developer atau PIC pelanggan, bukan pekerjaan SINUX." | Bagian 2 (pengecualian), bagian 9 |
| 13 | PIC aktivitas PM (SNX-OPS-FRM-07 Jadwal PM, fileId 1jrnarc0yyoZhx2MLACZePMNEe0-jb3ZB) | "Health check layanan kritis,Tiap awal shift,NOC Engineer"; "Review rule dan akun tidak terpakai,Triwulanan,Lead SOC"; "Uji pemulihan SNX-ISMS-PLN-01,Tahunan,Head of Operation" | Bagian 8, kolom PIC |
| 14 | Cakupan service report di form (SNX-OPS-FRM-07 Cara pakai) | "Setiap pelaksanaan PM atau CM yang mengubah sistem dicatat di Service Report beserta nomor tiket atau CR." dan "Lead NOC meninjau kepatuhan bulanan dan menandatangani kolom verifikasi." dan "R = rencana, S = selesai, T = tertunda." | 6.2 butir 7 dan 8; 6.3 butir 1 dan 2 |
| 15 | Tiket Ops di Zammad | config/defaults.json ticketing: kata owner 14 Okt "sistem tiket zammad untuk ops, glpi untuk generalist" | Scope, definisi, 6.4 butir 1 dan 8 |
| 16 | Ambang insiden berulang di SOP-04 (dari salinan audit, bukan dibuka di Drive) | "Insiden berulang (3 kali atau lebih pada layanan yang sama dalam 30 hari) diperlakukan sebagai problem dan wajib RCA." (ringkasan SNX-OPS-SOP-04 di context/audit) | USULAN 1 |
| 17 | Riwayat revisi sumber | Baris kedua: "Review bahasa dan konsistensi: istilah teknologi dalam bahasa Inggris, bahasa Indonesia formal, label klasifikasi, keselarasan RTO dan target pulih" | Tidak dibawa (cacat 2) |
| 18 | Penanda tangan sumber | "Disusun oleh \| Lead NOC", "Diperiksa oleh \| ISO/ISMS Coordinator", "Disetujui oleh \| COO, Amirull Yusuf Zulkarnain" | Diganti defaults (D2); badan dokumen tidak menyebut COO atau Direktur Utama, jadi aturan sebutan "Direktur (COO)" tidak terpakai |

## 3. Pemetaan klausul ISO (kriteria baris)

| Klausul | Di bagian 11 | Tercermin di bagian 4 (paragraf ke-n) | Prosedur dan SLA |
|---|---|---|---|
| ISO 9001:2015 7.1.3 | Ya, "7.1.3 (Infrastruktur)" | Paragraf 1: perawatan menurut jadwal PM tahunan | 6.1, baris SLA aktivitas PM |
| ISO 9001:2015 8.5.1 | Ya | Paragraf 3 dan 5: PM dan perbaikan yang mengubah sistem berjalan sebagai change | 6.2 butir 3 sampai 6; 6.4 butir 4 |
| ISO 9001:2015 10.2 | Ya | Paragraf 6 dan 7: kerusakan ditangani sebagai CM; temuan berulang dievaluasi sebagai problem dan dapat memicu RCA | 6.3 butir 3 dan 4; 6.4 |
| ISO/IEC 27001:2022 Annex A 7.13 | Ya, "7.13 (Equipment maintenance)" | Paragraf 1 | 6.1; scope (perawatan fisik DC bersama penyedia) |
| ISO/IEC 27001:2022 Annex A 8.6 | Ya, "8.6 (Capacity management)" | Paragraf 2: pemeriksaan kapasitas dan tren | Baris SLA kapasitas (mingguan) |

Nama klausul 8.5.1 dan 10.2 berasal dari standar ISO 9001:2015, bukan dari dokumen tim. "7.1.3 (infrastruktur)", "7.13 (equipment maintenance)", dan "8.6 (capacity management)" ada di sumber Bagian 3.

## 4. Penanganan cacat context/audit

Bagian 5 SNX-OPS-SOP-03 (fileId 10odQYr4B2cyaAX9Z98EKxv4HUjgwIoYc):

| # | Cacat tercatat | Penanganan |
|---|---|---|
| 1 | Draft rev 00, persetujuan Menunggu, tanda tangan kosong, dua baris riwayat revisi bernomor sama | Teratasi template: satu baris Revision 00 "Draft awal untuk review dan pengesahan", Effective Date kosong, Signature kosong. Tidak ada tanda tangan atau tanggal yang diisi |
| 2 | Kalimat riwayat "keselarasan RTO dan target pulih" tanpa padanan | Kalimat tidak dibawa. SOP ini tidak memuat RTO, RPO, atau target pulih; uji pemulihan hanya dirujuk ke SNX-ISMS-PLN-01 (baris SLA, PIC Head of Operation) |
| 3 | Severity tidak didefinisikan di SOP ini | Diperbaiki sebagian: definisi Severity (P1 sampai P4 menurut SNX-OPS-SOP-04) dan baris SLA "Respons, update ke pelanggan, dan target pulih tiket CM | Sesuai severity di SNX-OPS-SOP-04". Matriks tidak disalin (satu tempat: SOP-04). Open item 7 |
| 4 | Dua lokasi matriks eskalasi (SOP-04 dan POL-OPS-001 Bagian 6) | Tidak diperbaiki dari dokumen ini: SOP-03 merujuk SOP-04 seperti sumber. Open item 7 |
| 5 | Window maintenance: "Ajukan minimal 3 hari kerja sebelumnya" ada di PRO-OPS-001 NOC-06, tidak di SOP-03 | Diperbaiki: 6.2 butir 3 dan baris SLA memuat 3 hari kerja untuk change Normal PM. Dipakai pada lingkup NOC-06 (change Normal). Standar tidak tercakup NOC-06, Major tidak ada di SOP-03. Satuan lawan notifikasi pelanggan H-2 di open item 8 |
| 6 | Uji restore bulanan 100% tanpa label USULAN, padahal PRO-OPS-001 NOC-04 memberi label | Kalimat tim dipertahankan tanpa label (T1, SOP-03 sumber utama). Status keputusan berbeda masuk open item 5 |
| 7 | Cek rutin konsisten dengan PRO-OPS-001 NOC-04 dan NOC-05 | Tidak ada tindakan. Sembilan baris frekuensi dipakai persis di tabel SLA |
| 8 | KPI 95% dan 100% tidak ada di tabel KPI POL-OPS-001; POL memuat "Backup job sukses 98%" yang tidak ada di SOP-03 | Dua target SOP-03 dipertahankan di tabel SLA. 98% tidak dibawa (bukan butir sumber SOP-03). Open item 6 |
| 9 | Pemilik Lead NOC; Diperiksa oleh "ISO/ISMS Coordinator" tanpa nama | process_owner "Lead NOC"; pemeriksa Fani Fatullah dari defaults. "ISMS Coordinator" tidak dipakai di badan dokumen (HR-ORG-01 K-13: belum ditetapkan) |
| 10 | Gambar: titik kembali garis putus-putus hanya ada di gambar | Diagram baru digambar ulang di spec dengan garis putus-putus yang sama (change request ke Jalankan PM, CM ke Tinjau kepatuhan bulanan, RCA ke Rangkum ke laporan bulanan), dan keterangan gambar menyebut ketiga titik kembali itu. Simpul "Kerusakan atau penurunan kinerja di luar PM" ditambahkan karena Bagian 7 sumber berlaku juga tanpa PM. "SD dan PM" di gambar sumber diganti Service Delivery Manager |

Cacat tambahan yang saya temukan:

| # | Temuan | Penanganan |
|---|---|---|
| A | Definisi sumber PM menyebut "pembersihan kapasitas" dan "renewal sertifikat", sedangkan tabel 6.1 hanya memuat "Kapasitas disk, CPU, memori, dan tren pertumbuhan" dan "Masa berlaku sertifikat SSL (30 hari ke depan)"; tabel juga memuat review rule dan uji pemulihan yang tidak ada di definisi | Definisi PM dipendekkan menjadi arti dan merujuk tabel di bagian 8. Dua frasa itu tidak dibawa. Open item 9 |
| B | 6.2 butir 3 sumber meminta service report untuk tiap PM; SNX-OPS-FRM-07 Cara pakai 3 membatasi pada PM yang mengubah sistem dan CM, dan pemeriksaan harian dan mingguan hanya tercatat per bulan di Jadwal PM | Dokumen mengikuti form: service report untuk PM yang mengubah sistem dan untuk CM; realisasi PM lain ditandai S atau T di Jadwal PM. Open item 4 |
| C | Kalimat pasif tanpa pelaku (6.1 butir 3, 6.2 butir 4, 6.3 butir 2, Bagian 7 semua butir) | Diberi pelaku dari tabel peran; lihat asumsi 1 |
| D | "blok ukur read-only" dan "blok ubah" adalah istilah dari skill internal (PRO audit butir 8, tidak bisa diverifikasi) | Diganti "pemeriksaan read-only" dan "approval change yang tercatat" |
| E | Header "Masa simpan record: Berlaku sampai digantikan" bertentangan dengan tabel Bagian 8 "3 tahun" | Template tidak punya field itu; hanya tabel rekaman bagian 11 yang berlaku |
| F | "Temuan berulang" tanpa kriteria | USULAN 1 |
| G | Kapasitas (Annex A 8.6) hanya diperiksa dan dilihat trennya; tidak ada ambang atau tindakan selain tiket CM | Tidak ditambah (bukan butir sumber). Open item 10 |
| H | Approver change Standar dan Normal: SOP-03 dan POL 9.2 menulis Lead NOC; RACI POL Bagian 10 menaruh Head of Operation sebagai A untuk change Standar dan Normal, dan 9.1 memberi Head of Operation wewenang change Normal lintas sub divisi (POL audit butir 11) | Dokumen mengikuti SOP-03 dan POL 9.2: Lead NOC. Open item 11 |

Bagian 5 POL-OPS-001 (fileId 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv) dan PRO-OPS-001 (fileId 1U8CAdibwBk9x_-Aic2lbev144d6WReTz), butir yang menyentuh dokumen ini:

| # | Cacat tercatat | Penanganan |
|---|---|---|
| POL 6 | P-08 menetapkan semua tiket di GLPI; Bagian 13 butir 6 menunda GLPI sebagai sistem resmi | Dokumen memakai Zammad untuk tiket CM (premis owner). GLPI tidak disebut karena SOP ini tidak butuh batas "generalist". Open item 3 |
| POL 7, PRO 8 | Rujukan internal (DOCTRINE, DEC, HANDOVER, CORE, SKILL_, SINUX_SERVICE_HUB, "packet setor", "jalur staging", "blok ukur", "blok ubah") | Tidak ada yang dibawa; lint lolos |
| POL 11, 13 | RACI change Standar dan Normal; target pulih tidak ada di POL | Lihat H dan cacat 3 |
| POL 4 | Baseline KPI belum diukur | Target 95% dan 100% SOP-03 juga belum punya baseline; open item 6 |
| PRO 2 | Langkah berlabel USULAN termasuk uji restore NOC-04 | Lihat cacat 6 |
| PRO 7 | 3 hari kerja pengajuan lawan notifikasi H-2 dan H-5 | Lihat cacat 5; open item 8 |
| PRO 9 | Tidak ada klausul ISO dan masa simpan record | Dilengkapi di bagian 11 SOP-03 |
| PRO 11 | Tiket dalam 10 menit sejak alert terkonfirmasi (NOC-01) tidak ada di POL | Tidak dibawa: itu aturan penanganan insiden (lane SNX-OPS-SOP-04), bukan PM atau CM |

## 5. Asumsi dan tafsir (tidak tertulis eksplisit di sumber SOP-03)

1. Pelaku kalimat pasif: pemberitahuan jadwal ke pelanggan oleh Service Delivery Manager (peran sumber "Mengkomunikasikan jadwal maintenance ke pelanggan"); "Engineer" di sumber dibaca NOC Engineer (satu-satunya peran engineer di Bagian 5 sumber); pembuatan tiket CM, penetapan severity, eskalasi ke penyedia, penutupan tiket, penghapusan data aman oleh NOC Engineer; evaluasi problem, keputusan dan penyusunan RCA, serta tinjauan insiden bulanan oleh Lead NOC (POL 9.2: Lead NOC "menyusun RCA P1 dan P2 bersama engineer").
2. PIC sembilan aktivitas PM dibaca dari Jadwal PM SNX-OPS-FRM-07 (NOC Engineer untuk tujuh aktivitas, Lead SOC untuk review rule dan akun, Head of Operation untuk uji pemulihan). Sumber SOP-03 tidak memberi PIC per aktivitas.
3. Kolom Authority tidak ada di sumber. Isinya diturunkan dari kalimat sumber dan POL 9.2. Paling tipis: Head of Operation dan Penyedia DC dan upstream.
4. Langkah menandai kode S atau T di Jadwal PM adalah tafsir dari FRM-07 (kode R, S, T) agar tinjauan "rencana lawan realisasi" punya masukan; pelakunya NOC Engineer tidak disebut di FRM-07.
5. Definisi NOC dan SOC disamakan dengan HR-ORG-01; Jumphost dengan SOP-02 akses pilot; Overseer dari PRO-OPS-001 NOC-01 dan NOC-05 ("dashboard aktif", "cek perangkat internal di Overseer"). Definisi Problem dan RCA adalah penjelasan penyusun.
6. Cakupan service report mengikuti FRM-07 (cacat B), bukan kalimat 6.2 butir 3 sumber.
7. Lokasi "Google Drive" dan pemilik rekaman di bagian 11 diambil dari "Pemilik dokumen" tiap form (FRM-07 dan ISMS-FRM-01 Lead NOC; FRM-04, FRM-10, RPT-01 Head of Operation, sesuai notes sibling). Sumber SOP-03 hanya memberi nomor dan masa simpan. Baris RCA (5 tahun, dari FRM-10) dan laporan bulanan (3 tahun, dari RPT-01) ditambahkan karena dirujuk di badan dokumen.
8. Tiket CM: tiket dibuat di Zammad (premis owner), SNX-OPS-FRM-08 dipakai sebagai catatan rekap. Sumber menulis "dicatat sebagai tiket di SNX-OPS-FRM-08".
9. Baris pengecualian "Kerusakan di app-level pelanggan" dan "Pelanggan tanpa layanan backup" berasal dari POL-OPS-001 dan PRO-OPS-001 (kutipan 11, 12, 10). "Patch kritis" dari tabel 6.1 sumber ("atau segera untuk patch kritis"); "sebagai change" adalah kesimpulan dari 6.2 butir 2.
10. Vault: kata "password manager" ada di scope sumber. Definisi memuat "Status operasional: menunggu konfirmasi Ops" sesuai aturan data_conflicts. Tidak ada klaim aktif atau belum live.
11. Nama peran sesuai HR-ORG-01. "Penyedia DC dan upstream" adalah pihak luar dari sumber, bukan jabatan SINUX, sehingga tidak ada di HR-ORG-01. Head of Operation ada di HR-ORG-01 sebagai (USULAN), tanpa pemegang (K-10).

## USULAN

Lint menghitung 1 butir berlabel di dokumen.

| # | Butir | Letak | Alasan | Pemutus yang disarankan |
|---|---|---|---|---|
| U1 | Temuan dihitung berulang bila terjadi tiga kali atau lebih pada aset yang sama dalam 30 hari | Bagian 4, paragraf ke-7 | Sumber memakai "temuan berulang" tanpa kriteria. Angka diambil dari ambang insiden berulang SNX-OPS-SOP-04 dan diperluas ke temuan PM, jadi diberi label | Fani |

Butir tanpa label yang memerlukan penegasan pemutus (bukan angka tanpa sumber, tetapi status keputusannya belum final di dokumen sumber): uji restore bulanan 100% (PRO NOC-04 memberi label USULAN) dan pengajuan change Normal 3 hari kerja (PRO-OPS-001 masih DRAFT). Keduanya di open items 5 dan 8.

## Open items

| # | Butir | Pemutus |
|---|---|---|
| 1 | Penyetuju: sumber menulis "COO, Amirull Yusuf Zulkarnain"; defaults menetapkan Samuel Kristanto Utomo / President Director. Defaults dipakai | Owner atau Samuel |
| 2 | Lead NOC, NOC Engineer, Lead SOC, Service Delivery Manager, dan Head of Operation belum punya pemegang bernama (HR-ORG-01 K-10); hubungan Head of Operation dengan VP Tech Operation and Services belum ditetapkan (K-09). Pemilik SOP tetap Lead NOC, pemeriksa Fani. "ISO/ISMS Coordinator" di sumber belum ditetapkan (K-13) | Owner, Fani |
| 3 | Sistem tiket: POL-OPS-001 P-08 menulis semua tiket di GLPI, sedangkan premis owner memberi Zammad untuk Ops. SOP ini memakai Zammad. SNX-OPS-FRM-08 adalah register rekap; hubungannya dengan tiket di Zammad perlu ditegaskan, juga di SOP-04 dan FRM-09 | Owner, Fani |
| 4 | Cakupan service report: sumber 6.2 butir 3 (tiap PM) lawan FRM-07 Cara pakai 3 (PM yang mengubah sistem dan CM). Dokumen mengikuti FRM-07. Pemeriksaan read-only harian dan mingguan hanya tercatat per bulan di Jadwal PM | Fani, Lead NOC |
| 5 | Uji restore bulanan 100%: SOP-03 tanpa label, PRO-OPS-001 NOC-04 berlabel USULAN, POL 9.2 hanya "memastikan uji restore bulanan berjalan" | Fani |
| 6 | KPI: POL-OPS-001 Bagian 11 tidak memuat kepatuhan jadwal PM dan uji restore, dan memuat "Backup job sukses 98%" yang tidak ada di SOP-03. Baseline KPI belum diukur (POL 11) | Fani |
| 7 | Dua lokasi matriks severity dan matriks eskalasi (SNX-OPS-SOP-04 dan POL-OPS-001 Bagian 6); target pulih (USULAN di SOP-04) tidak ada di POL. Isi belum dibandingkan baris per baris | Fani (lane SNX-OPS-SOP-04) |
| 8 | Pengajuan change Normal minimal 3 hari kerja (PRO NOC-06) lawan notifikasi pelanggan H-2 untuk Normal (POL Bagian 7); satuan hari kalender atau kerja tidak ditegaskan, dan belum ada aturan pengajuan untuk change Standar | Fani |
| 9 | Definisi PM di sumber memuat "pembersihan kapasitas" dan "renewal sertifikat" tanpa padanan di tabel 6.1; tidak ada jadwal renewal sertifikat. Perlu dipastikan apakah renewal masuk PM | Lead NOC, Fani |
| 10 | Kapasitas (Annex A 8.6): tidak ada ambang dan tidak ada tindakan selain tiket CM bila disk, CPU, atau memori mendekati batas | Fani |
| 11 | Approver change Standar dan Normal: Lead NOC (SOP-03, POL 9.2) lawan Head of Operation sebagai A di RACI POL Bagian 10 | Fani |
| 12 | Sumber tidak menyebut lokasi rekaman untuk: pemberitahuan jadwal ke pelanggan, hasil diagnosis, approval Lead SOC atas PM, keputusan problem dan RCA, serta hasil tinjauan insiden bulanan. Kolom rekaman di bagian 6 memakai nama generik | Lead NOC |
| 13 | Lokasi simpan rekaman terisi (Google Drive, per tahun) dan retensi per rekaman: sumber SOP-03 memberi 3 tahun untuk empat rekaman; RCA 5 tahun dari FRM-10; header sumber "Berlaku sampai digantikan" bertentangan dengan tabel | Fani |
| 14 | Head of Operation sebagai PIC uji pemulihan tahunan dan Lead SOC sebagai PIC review rule dan akun berasal dari FRM-07, tidak dari SOP-03 sumber | Fani |
| 15 | "Laporan bulanan" di SOP-03 diarahkan ke SNX-OPS-RPT-01 (gambar sumber); PRO-OPS-001 SDPM-04 menyebut laporan bulanan pelanggan. Belum jelas apakah keduanya satu dokumen | Fani, Service Delivery Manager |
| 16 | Status password manager (vault): "menunggu konfirmasi Ops" | Ops (Fani) |
| 17 | POL-OPS-001 dan PRO-OPS-001 masih DRAFT dengan penomoran USULAN; kodenya di bagian 11 diganti nomor SNX bila sudah terbit. POL-OPS-001 masih menulis jabatan Fani berbeda dari HR-ORG-01 (K-12) | Fani |
| 18 | Jam Shift 3 "umumnya": sumber tidak menyebut penanganan bila window berdampak ke layanan jatuh di luar Shift 3. Tidak ditambahkan ke bagian 9 karena tidak ada kontrol pengganti di sumber | Fani |

## 6. Dua pertanyaan wajib

Pertanyaan 1: apa yang membuat teks ini terdengar buatan AI?

Temuan pada draf pertama dan yang saya lakukan:
- Draf pertama kebijakan paragraf ke-3 dan langkah pertama 6.2 memakai "yaitu ..." dua kali dalam satu kalimat. Kalimat sumber memakai tanda kurung ("(pemeriksaan read-only)", "(patch, restart, perubahan konfigurasi)"); saya kembalikan ke bentuk itu.
- Draf pertama langkah evaluasi menulis "pantau tren penurunannya", kata kerja karangan; target di sumber hanya "tren menurun". Diganti "dengan target tren menurun".
- "Tiket corrective maintenance" dan "tiket CM" berganti untuk hal yang sama. Diseragamkan menjadi "tiket CM" setelah CM didefinisikan; teks gambar memakai "Corrective maintenance (CM)" sekali.
- Baris SLA memakai "Ack" tanpa definisi di dokumen ini. Diganti "Respons, update ke pelanggan, dan target pulih".
- "Cantumkan ... minimal aktivitas dan frekuensi" kaku; diganti "aktivitas minimal dan frekuensi minimalnya".
- Label "(ISO 9001 ...; Annex A ...)" muncul di enam paragraf kebijakan dan terdengar mekanis. Tetap dipakai karena kriteria baris menuntut kontrol tercermin di bagian 4; saya batasi pada paragraf yang benar-benar dipetakan dan tidak menempelkannya di paragraf lain.
- Daftar berderet ("aktivitas, temuan, tindakan, status, dan bukti"; "disk, CPU, memori"; "Standar, Normal, dan Emergency") semuanya dari sumber, bukan kelompok tiga yang dipaksakan.
- Kolom output yang berulang ("Baris service report di SNX-OPS-FRM-07") sengaja sama karena menyebut rekaman yang sama.
- Tidak ada em-dash, en-dash, tebal atau huruf kapital untuk penekanan, pembuka generik, ekor penegas, atau penutup positif. Conclusion dua kalimat tentang pemantauan dan peninjauan, tanpa pujian.

Pertanyaan 2: adakah fakta, angka, nama, atau tanggal tanpa sumber?

- Angka tanpa sumber tim hanya satu dan berlabel (USULAN): ambang tiga kali dalam 30 hari (dari SOP-04 lewat salinan audit, diperluas ke temuan PM).
- Angka lain semuanya bersumber: 30 hari (masa berlaku SSL), 95% dan 100% (SOP-03 Bagian 9), 3 hari kerja (PRO NOC-06), 3 tahun (SOP-03 Bagian 8 dan RPT-01), 5 tahun (FRM-10), 23:00 sampai 07:00 WIB (Bagian 4 sumber), P1 sampai P4 (SOP-04 dan POL Bagian 6).
- Nama orang hanya tiga penanda tangan dari defaults. Tidak ada tanggal di dokumen; Effective Date kosong; status Draft.
- Sistem semuanya dari sumber atau premis owner: Nusagrid, WHM, cPanel, Jumphost, Zammad, Overseer, SIEM, EDR, Cloudflare, WAF, WordPress.
- Yang bukan kalimat tim dan sudah dicatat di bagian 5: nama klausul 8.5.1 dan 10.2, definisi Problem, RCA, Overseer, NOC, SOC, kolom Authority, lokasi Google Drive dan pemilik rekaman, PIC dari FRM-07, kalimat "sebagai change" pada patch kritis.
- Yang saya ubah sesudah pemeriksaan ini: kata "Ack" dihapus dari baris SLA (tanpa definisi), istilah tiket diseragamkan, dan kalimat langkah dipendekkan. Kutipan di tabel 2 dicocokkan ulang ke teks Drive yang dibaca hari ini.
