> Salinan dari Project claude/iso-sinux-context-pack-v19.md (disalin LEAD ISO-A, 15 Okt 2026) dengan tiga penyesuaian: baris default §8 ditandai DIKUNCI, nama roster satu kaki di §7 dihapus, baris pemilihan model di §9 dihapus (diatur RUNBOOK §5). Untuk worker: langkah §0 di bawah diganti RUNBOOK §1a; angka di berkas ini snapshot 14 Okt, ukur ulang live di W0.

# ISO SINUX: Context Pack v19 (pintu masuk tunggal sesi generate)

As-of: 14 Okt 2026 sekitar 08:10Z. KB serving 703fd42363a01ff3d60ab74cc1910770381f70dc. Status: NON-KANONIK, bahan kerja COS. Pasangan staging: iso-study-20261014-close-v19.
Mengungguli: rekomendasi format di #1929 (wrapper template konsultan) DIGANTI oleh SOP TEMPLATE internal SINUX (instruksi owner 14 Okt). Isi audit #1929 tetap berlaku.

## 0. Cara pakai (sesi berikut)
1. kb_anchor manifest; relay_get iso-study-20261014-close-v19.
2. Baca berkas ini utuh. Lalu ukur ulang LIVE: checklist (fileId di §11) dan isi folder Dep.* (tim masih menyunting saat paket ini ditulis: checklist 08:07Z, SOP Billing berganti nama 08:06Z, SOP Contract Review 08:09Z).
3. Baru generate. Angka di berkas ini = snapshot, bukan kontrak.

## 1. Goal dan premis owner (verbatim)
- "konteks saat ini : murni untuk create document yang diminta tim consultant kami (SOP, Struktur organisasi, Jobdesc) sisanya, kita tuangkan SOP yang sudah ada. konsultant akan bantu proses."
- "kemungkinan SOA bukan kita yang isi"
- "ada updated data dari tim, yang sudah ada dan di checklist dan belum ada. dibutuhkan, refrence link juga dilampirkan. ada di Drive ISO sinux"
- "dilampirkan juga Template SOP internal sinux nanti untuk kebutuhan standarisasi semuanya"
- Go-gate berikut: "COS membuat SOP dengan format template dan instruksi yang diberikan nanti, baik itu create new, improve existing supaya sesuai tanpa ada gap dan kelebihan scope, atau samakan dengan formating yang dibuat Aziz. or membantu sisa proses ISO sampai selesai"
- Premis tetap: audit perdana ISO 9001:2015 + ISO/IEC 27001:2022; tiket "zammad untuk ops, glpi untuk generalist"; Fani = VP Tech Operation and Services.

## 2. Kontrak scope
- Checklist tim "Checklist ISO SINUX - 2026" (88 baris) = daftar permintaan. Kolom Description tiap baris = kriteria penerimaan isi ("tanpa gap"). Di luar 88 baris hanya bila konsultan meminta ("tanpa kelebihan scope").
- Ops: kolom H dan I berisi acuan klausul ISO 9001 dan 27001, wajib terbawa ke dokumen.
- Lane konsultan: SoA (SNX-ISMS-SOA-01 diserahkan sebagai bahan), dokumen sistem manajemen (Manual M-SMT-01, kebijakan, sasaran, audit internal, tinjauan manajemen) kecuali konsultan meminta bantuan.
- Daftar 112 dokumen dan paket minimum 22 dari sesi lama = pembanding saja, bukan scope.

## 3. Keluarga dokumen dan lokasi
| Keluarga | Lokasi | Catatan |
|---|---|---|
| Supporting Documents (tim) | folder 1JA0Gl0-C7Pj304cmCoJ_Mr8TowewtN1_ | subfolder Dep. HR 1o3tZgAiGtUf631zBhOR9KKWmJVebRG6i, Dep. FAT 1U4BP2va0dvAez_GhvMutaEf2EuLcyxrj, Dep. Legal 1MaM7FNPv_LdPejBd3P2gqUDph9i2KhFA, Dep. Commercial 1cx8p5BZ1Hobfc6AWf5VGVA1ZekUdZZyN, Dep. Ops 1YCD2HweNAXF54IAcMQM2CGGf1ovvboWK (kosong, satu kaki), Management 1nIjrbsJxU3G_B_-R8h4CVkFQ1baEXKcg (kosong, satu kaki), Sample old - Eranyacloud |
| Ops/ISMS seri SNX (Fani) | folder 1bM4YuiCpQb_70d1f7ZnVMx6XyWOXlaDF (A_Project_Service_Operations 1HJe8WE2BqIwoyDNG58l7ICj0euZPyp8m, B_Information_Security_ISO27001 11V6YWsv0NSM3tVPt7SBZ6WlLuj8yNZsO) | 32 baris Ops checklist menunjuk berkas di sini lewat nama berkas (kolom F), bukan hyperlink |
| Paket konsultan 10 Okt | shared drive 0AFjhfqXaRZJ_Uk9PVA | 165 berkas; template dengan residu perusahaan lain; Lampiran 2 Struktur 1FaPdUww5zNl0O9ZyYg2_Z2nCoU7QMsEg KOSONG |
| Eranyacloud MN-001/MN-002 | folder MN di 1bM4YuiCpQb_70d1f7ZnVMx6XyWOXlaDF | pembanding saja |

## 4. SOP TEMPLATE internal SINUX (fileId 1n6iPAh7yXLadDkY-bwnuDz9D3fNhBodQ)
Dua kaki (teks + parse docx). Metadata: lastModifiedBy "Sita Work", creator kosong, dibuat 07:09Z, rev 3. Premis owner: format dibuat Aziz. Catatan tim di checklist H22: "*SOP Template : Draft Template untuk Semua SOP Sinux dan Versioning Document".

Kerangka berurutan:
1. Sampul center: "STANDARD OPERATIONAL PROCEDURE" / "DEPARTMENT [NAMA]" / "[NAMA SOP]" (bold 16 pt), "No : [NOMOR SURAT]", "Diterbitkan oleh" / "PT STRATEGI INTEGRASI NUSANTARA".
2. "Identity Document" + disclaimer kepemilikan + tabel Information | Detail: Company Name (PT Strategi Integrasi Nusantara (SINUX)), Document Title ([DEPTARTEMEN] - SOP [NAMA SOP]), Document Number ([NOMOR SURAT]), Department, Effective Date ([DD MM YYYY]), Revision Number (Rev. 00), Document Status (Active), Classification ([Internal / Confidential]), Process Owner, Review Period ([MONTHLY / QUARTERLY / YEARLY]).
3. "Revision History": Revision No. | Effective Date | Description of Changes.
4. "Dokument Approval": No | Role | Name / Title | Signature; Prepared By, Reviewed By, Approved By = "Samuel Kristanto Utomo / President Director".
5. Table of Contents statis (berisi instruksi per bagian).
6. Badan 11 Heading 1 bernomor: 1 PURPOSE, 2 SCOPE, 3 DEFINITION & ABBREVIATIONS (tabel Term | Definition), 4 POLICY & GENERAL PRINCIPLES, 5 ROLES, RESPONSIBILITIES & AUTHORITIES (tabel Role | Responsibilities | Authority), 6 STANDARD OPERATING PROCEDURE (6.1 Process Detail), 7 PROCESS FLOW (flowchart atau swimlane, kosong di template), 8 SERVICE LEVEL AGREEMENT (SLA) (tabel Activity | PIC | SLA / Timing), 9 EXCEPTION MANAGEMENT (tabel 2 kolom tanpa header), 10 CONCLUSION, 11 RELATED DOCUMENTS & ATTACHMENTS.
Gaya: A4 portrait, margin atas/kiri 2,2 cm, kanan/bawah 2,0 cm; Arial; heading bold 12 pt hitam; header banner logo SINUX (business@sinux.co.id, sinux.co.id); footer banner alamat Midpoint Place + "Page/ Halaman - N"; penomoran multilevel 1., 6.1.
Ukuran 1,78 MB karena font Calibri dan Cambria tertanam (tidak dipakai badan); media hanya sekitar 94 KB.

Cacat template (akan terwarisi bila tidak diputus): "Dokument Approval"; "[DEPTARTEMEN]"; TOC "Responsibilities,&"; sampul "OPERATIONAL" vs badan "Operating"; disclaimer bergaya Heading 1 dan satu Heading 1 kosong (masuk TOC bila di-update); TOC statis memuat 6.2 yang tidak ada; page break di dalam Heading 2; tabel Exception tanpa header; bahasa en-GB; ejaan "Kristanto" (template, Billing) vs "Kristianto" (Job Analysis).

Jebakan rekaman: default "Document Status: Active" dan Effective Date. Draf WAJIB berstatus Draft, Effective Date dan Signature kosong sampai penyetuju menandatangani pada harinya (larangan tanggal mundur).

Celah ISO di template dan aturan pemetaan TANPA mengubah struktur:
- Acuan klausul ISO (kolom H/I checklist) -> bagian 11.
- Daftar rekaman (kode form, lokasi simpan, pemilik, retensi) -> bagian 11, tabel.
- Kontrol keamanan/risiko terkait -> bagian 4.
- RACI/peran -> bagian 5, nama peran mengikuti Struktur Organisasi dan Job Analysis.
- Target waktu -> bagian 8. Pengecualian -> bagian 9 (beri label kolom: Kondisi | Penanganan, usulan).
- Distribusi, nomor di header/footer: tidak ditambahkan (bukan permintaan).
- Klasifikasi Internal/Confidential: selaraskan dengan skema SNX-ISMS-PRO-01 (belum dicek, UNMEASURED).

Uji format 25 butir (lulus/gagal) untuk tiap SOP:
A1 sampul tiga baris bold 16 pt; A2 "No :" terisi dan identik Document Number; A3 "Diterbitkan oleh" + nama PT + page break; A4 header banner SINUX; A5 footer banner alamat + Page/Halaman; A6 A4 dan margin; A7 hanya Arial, heading bold 12 pt hitam.
B8 Identity + disclaimer verbatim; B9 10 label berurutan; B10 isian valid; B11 Revision History baris 00 terisi deskripsi; B12 Approval 3 baris; B13 nama dan jabatan terisi (Signature dan tanggal kosong sampai sah); B14 TOC cocok heading.
C15 11 heading urutan baku; C16 bagian 1, 2, 4, 10 tidak kosong; C17 tabel definisi minimal 1 baris; C18 tabel peran lengkap tiga kolom; C19 6.x berisi langkah; C20 bagian 7 berisi diagram; C21 tabel SLA terisi, PIC cocok bagian 5; C22 tabel pengecualian terisi; C23 bagian 11 berisi dokumen terkait, rekaman, acuan klausul.
D24 nol placeholder dan nol teks instruksi; D25 status, revisi, nomor konsisten di semua tempat.

## 5. Peta kerja per baris checklist (snapshot 07:48Z; 88 baris)
Kode aksi: T1 = konversi berkas yang ada ke template + perbaikan; T2 = tulis baru; T3 = tim menandai TRUE tetapi berkas tak terlihat (tanpa link, link 404, atau "on review"), minta berkas dulu; K = konsultan.
Arti TRUE dari tim = "sudah ada" (kata owner). 49 dari 63 TRUE belum bertaut ke berkas yang terverifikasi.

| Dept | T1 | T2 | T3 | Lain |
|---|---|---|---|---|
| HR (20) | Job Analysis (HR-JA-001), SOP Company Leaves (sumber PP Cuti BAB VI, link FALSE) | Competency Matrix, Annual Training Plan & Matrix, Training Attendance & Evaluation, SOP Promotion, Demotion, Rotation, Mutation, Struktur Organisasi | SOP Recruitment, Onboarding, Training & Development, Performance Appraisal, Offboarding, Personnel File Checklist, NDA Acknowledgement Records, SOP Company Asset, SOP Payroll | SOP Template (rujukan) |
| FAT (12) | SOP Billing & Invoicing, SOP Tax | SOP Financial Document Control & Retention, Financial Transaction Approval Records, FAT Nonconformity & Corrective Action | "on review": SOP AR & Collection, SOP Payment & Disbursement Approval, SOP Accounting & Financial Report, Billing & Collection Monitoring Register (berkas baru muncul 07:39Z, 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ), Financial Document Register, Financial Information Access Authorization Records, FAT KPI Report | |
| Legal (13) | SOP Legal Operational (link 404, berkas terbaca 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb), SOP Contract Review & Legal Approval (draf tim sedang ditulis 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE, bagian Prosedur kosong), Company Licenses & Permits Register, Customer CL, Vendor CL, Data Protection Review, Legal Risk Register, Legal CMCA | Legal & Regulatory Requirements Register, Legal Compliance Evaluation Report, SOP Legal Document Control & Retention, Company Legal Documents Register | NDA Template (link 404, tidak ditemukan 3 kaki) | |
| Commercial (7) | SOP Sales Process (Sales SOP pdf 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0) | SOP Proposal, Quotation & Pricing Control (sumber bagian Sales SOP), Customer Requirement & Order Review Record, Project Handover Record, Customer Feedback & Complaint Register | SOP Sales Incentive (link 404; sensitif, keputusan owner), Sales Pipeline Register (link 404) | |
| Marketing (4) | | Planning & Performance Review, Content/Material & Claims Approval Register, Campaign & Activity Register, Lead & Campaign Outcome Register | | |
| Ops (32) | 31 berkas SNX-OPS/SNX-ISMS | | | SOA-01 = K |
| Total 88 | 44 | 23 | 19 | 2 |

Prioritas deliverable eksplisit owner: SOP, Struktur Organisasi (HR baris 21), Jobdesc (HR baris 8 Job Analysis).

## 6. Hasil audit 52 dokumen tim (verifikasi buta 12/12 PASS)
| Kelas | Dokumen |
|---|---|
| A aman | Ops FRM-03 |
| B perbaikan mekanis | Ops FRM-01, 02, 05, 06, 09; ISMS PRO-01, SOP-02, 04, 05, REG-04, FRM-01, 02; Legal Licenses & Permits Register, Customer CL, Vendor CL, DP Review |
| C1 ACC COO angka USULAN | Ops SOP-01, 02, 03, 05, FRM-04, 07, 10, RPT-01 |
| C2 data/keputusan | Ops POL-OPS-001, ML-00, PRC-01, SOP-04, FRM-08; ISMS REG-01, 02, 03, SOP-01, 03, FRM-03, PLN-01; FAT Billing, Tax; Legal SOP Divisi Legal v0.1, Legal Risk Register, CMCA, Jobdesk LM Legal, Jobdesk Staff Legal; Commercial Sales SOP, KPI; HR-JA-001, PP Cuti |
| D bahan saja | PRO-OPS-001, Sales Playbook, Commercial Onboarding deck |
| K konsultan | SOA-01 |

Perbaikan lintas dokumen (saat dituangkan):
1. Buang rujukan internal AI: SKILL_, DOCTRINE, DEC-, HANDOVER, staging, "packet setor" (terverifikasi di POL-OPS-001, PRO-OPS-001, SOP-04, ISMS-SOP-01).
2. Buang baris CONTOH (20 di form Ops, 12 di REG-01).
3. Tiket: Zammad untuk Ops, GLPI generalist (POL-OPS-001 P-08 masih "semua tiket di GLPI").
4. Fani = VP Tech Operation and Services (POL-OPS-001 §3 menulis "Komisaris dan Advisor").
5. Prepared/Reviewed/Approved tiga orang berbeda (SOP Billing kini satu orang); template mengunci Approved By = Samuel.
6. Vault: REG-01 "Aktif" vs KB "BELUM LIVE" (upd 8 Okt); kondisi hari ini UNMEASURED.
7. SOP-03: kunci enkripsi backup tersimpan di vault yang ikut di-backup; perlu salinan offline/break-glass.
8. PPN 11% (1.2) vs 12% (10 tempat) di SOP Billing; rumusan diputus FAT.
9. Ejaan nama Direktur Utama satu versi resmi.
10. Jangan salin residu paket konsultan; Eranyacloud pembanding saja.

## 7. Struktur Organisasi dan Jobdesc
- Sumber tunggal: HR-JA-001 (15 jabatan bernama) + struktur Divisi Operation POL-OPS-001 §9 (8 jabatan USULAN tanpa nama). Hasil juga mengisi Lampiran 2 Manual konsultan yang kosong.
- Uraian Tugas paket konsultan tidak dipakai (residu gudang/impor).
- Jabatan dipisah dari peran: jobdesc hanya jabatan nyata; sekitar 16 peran yang dipakai SOP (Head of Operation, Lead NOC/SOC, NOC Engineer, SOC Analyst, PM, Project Coordinator, ISMS Coordinator, Finance Lead/Staff, Line Manager/Staff Legal, Commercial Manager, Presales, Sales Executive, MR/Ketua Tim ISO) dipetakan ke jabatan lewat matriks peran + SK penunjukan (9001 5.3, 27001 5.3).
- HR-JA-001 sendiri mensyaratkan garis lapor terkonfirmasi sebelum Controlled/Effective.
- Data dibutuhkan (owner + Samuel): sebutan resmi jabatan puncak (template: "President Director"; dokumen lain: Direktur Utama, CEO), garis lapor 15 JA, jabatan Ops nyata vs peran, penunjuk Koordinator SMT/ISMS. HR Lead: roster (KB menyebut nama yang tak ada di HR-JA-001, satu kaki), ejaan nama, KPI/kualifikasi.

## 8. Keputusan
| Status | Butir |
|---|---|
| Diputus owner | Format = SOP TEMPLATE internal SINUX; SoA = konsultan; tiket Zammad Ops/GLPI generalist; audit perdana; Fani VP Tech Ops |
| Dikunci template | Approved By = Samuel Kristanto Utomo / President Director; 11 bagian baku |
| Default COS (DIKUNCI LEAD 15 Okt, lihat config/defaults.json) | Nomor dokumen: SNX-<AREA>-<JENIS>-<NN> datar, nomor lama jadi alias; SOP = template penuh, form/register = sampul + Identity + Revision + Approval lalu badan sendiri (tafsir H22 "Versioning Document"); status Draft sampai sah; Reviewed By = kepala departemen; berkas baru di folder draf COS, berkas tim tidak ditimpa |
| Terbuka | Perbaikan cacat template oleh Aziz; angka USULAN Ops K1-K12 (ACC COO); DoA harga/kontrak/pembayaran; rumusan PPN; SOP Sales Incentive (owner) |

## 9. Model operasi sesi generate
1. Ukur ulang live (checklist + folder) dan sebut delta.
2. Kunci input: skema nomor, data struktur, keputusan cacat template. Yang belum datang: pakai default §8 berlabel.
3. PILOT satu SOP penuh (ISMS SOP-02 User Access Control, kelas B) ke template dengan menyunting SALINAN SOP TEMPLATE.docx (python-docx) agar header, footer, gaya, penomoran utuh; diagram alir dibuat sebagai gambar lalu ditanam. Owner/Aziz menilai format dulu, baru produksi massal.
4. Produksi per departemen: Struktur Organisasi dan Job Analysis lebih dulu (karena bagian 5 tiap SOP bergantung padanya), lalu T1 (Ops/ISMS, Legal, FAT, Commercial, HR), lalu T2, T3 menunggu berkas tim.
5. Tiap dokumen: uji 25 butir format + kriteria Description checklist + perbaikan lintas dokumen; verifikator buta pada sampel.
6. Paket pengesahan: blok tanda tangan dan tanggal kosong, diisi penyetuju sendiri.
Larangan: rekaman bertanggal mundur; mengisi tanda tangan/tanggal atas nama penyetuju; menyalin residu paket konsultan; Eranyacloud selain pembanding; rujukan internal AI di dokumen ISO; menimpa berkas tim; kredensial.

## 10. Risiko (Red Team) dan pembalik
| Risiko | Bukti | Pembalik |
|---|---|---|
| Snapshot basi | tim menyunting 08:06Z sampai 08:09Z | ukur ulang di awal sesi |
| TRUE dianggap selesai | 49 TRUE tanpa berkas terverifikasi | hitung selesai hanya bila berkas terbuka dan lulus uji |
| Cacat template berlipat ganda | 10 cacat terukur | putus sekali sebelum produksi massal |
| Rekaman palsu | default template "Active" + Effective Date | Draft, tanggal kosong |
| Samuel jadi leher botol tanda tangan | Approved By terkunci untuk semua SOP | satu sesi tanda tangan batch |
| Kelebihan scope | dokumen sistem manajemen milik konsultan | hanya 88 baris kecuali konsultan minta |

## 11. Indeks fileId
Checklist 1zlA3Eztm08xkL_V23S5yPhiti-pgOj_T296uUI-stmY; SOP TEMPLATE 1n6iPAh7yXLadDkY-bwnuDz9D3fNhBodQ; HR-JA-001 1m91WrfxiL4BnQSMItHSgF_VP9eUD5Vt1; PP Cuti 1i2JaRaQolbKxKL9HjDao2s4F0bzma9-Z; SOP Billing 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI; SOP Tax 1iMKby6u4X8MYyGlrC5qz73D0y2anOv87; FAT Billing & Collection Register 1Z9PXCiBgb8c13TGx8BG3ajlbxNEDWMg6KaSy0mi7ehQ; SOP Divisi Legal 19peOeN1yA-GwAlfNylE6xQR7rHVKRsZb; SOP Contract Review (draf tim) 1E_8SkaHZo8txljia4JhWjRHakimojRCpwivZzrPyamE; Jobdesk LM Legal 1Mv6TuLy8QsllpA4YTTjmNg7Hsur4yWiL; Jobdesk Staff Legal 1dOku3703JwQCVeC39tl9x6k0FMa4f3nW; Licenses & Permits Register 1a1hDz9zwdRHBAHaU9wALSdg66R4bD8mGD-86TyzJewk; Customer CL 1lsdhtFZrf7bdckagXYtEXxmIyRw3jNw-28iXJpoTeaY; Vendor CL 1xU1pbum660ZzBCuTA5klCyAVK1iWonLCY0NOejqSlHg; DP Review 1m9mIkrMmiIY4TNmbV7j_rRuXKPUnfiK_EP80myS6lN8; Legal Risk Register 1ysIL0ytnspFGsYpSolSnuBpCG_MFE9IoiTJIhWfIIhA; Legal CMCA 1NQvPoHgx4n3SDUmMa5EzJ8QOUg-jb-Bf6fX7x0EarXA; Sales SOP 19Hex8udn1JDG4NKY7hZaODjroHeHwMM0; Commercial Onboarding 16TIN9Tsv_sBXMrL4KHeO8f6Ao0F-KsAS; Sales Playbook 1RVxuhUAFVTqwbtArb9uG4i2paG7Ph35w; KPI Commercial & Marketing 1TNg8MveAYQ26Fkalk7UlL_iu7FC6EUIb; POL-OPS-001 1bn7EHpmUm2DL7ZJVg284KzCLEQrfPBGv; PRO-OPS-001 1U8CAdibwBk9x_-Aic2lbev144d6WReTz; ML-00 11KICKwmsIgl5TEgdX_5AgLa-mfoIBVTH; ISMS REG-01 1mMx6v0UhAWMQU6I6rAfsZz20nsjv-FkP; REG-02 1skCiIY43Vz6qfT71vEKz55EZFGHVCl4Q; REG-03 1NdkQrRWevHXuH9thxmoTPsRIf0wNl-MJ; REG-04 14JtND6eqCuvufrVoPDzKJyrHp4eQsGjT; SOA-01 1g9Yiuv6EDJP2ikgAbpcnRVE0ZVFkLWG2; Lampiran 2 Struktur (konsultan, kosong) 1FaPdUww5zNl0O9ZyYg2_Z2nCoU7QMsEg.
Link 404 di checklist (perlu dibagikan ulang oleh tim): SOP Divisi Legal 1YxX0cPQDjqaJyQsxEdw-uKnP5XUN_8WK, Boilerplate NDA 1GsC8jRj0WeR2_mEbkXpIlSCf3iOKPIvTcX3a2kA55CA, SOP_HR_SalesIncentivePlan 1j6QsEa9a8jHJYBCo2mmX5w9rvUvM6v3h, Sales Pipeline Register 12IGYJDN2bnJ1ohj_m8SG2TERv12SuTcUKvTDgIalUHM.

## 12. UNMEASURED
Daftar permintaan tertulis konsultan (pegangan = checklist + kata owner); perubahan checklist sesudah 07:48Z; isi 19 dokumen T3; kondisi vault hari ini; skema klasifikasi PRO-01 vs template; pembuat template selain metadata; isi folder Dep. Ops dan Management (satu kaki: kosong).
