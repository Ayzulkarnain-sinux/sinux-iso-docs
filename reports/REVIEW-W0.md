# REVIEW-W0 (2026-10-14T19:35:56Z)

## SNX-ISMS-SOP-02 User Access Control & Authorization
- State: DONE; lint: True; verifikasi: PASS; putaran perbaikan: 1; OOXML: PASSED
- Berkas: out/08_ISMS/SNX-ISMS-SOP-02 User Access Control & Authorization (Rev00 DRAFT).docx
- Sumber: SNX-ISMS-SOP-02_SOP_User_Access_Control_Authorization.docx (1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT, modifiedTime 2026-10-13T06:09:01Z)

### Fakta kunci
| # | Fakta | Kutipan verbatim sumber | fileId |
|---|---|---|---|
| 1 | Pencabutan akses saat pemberhentian paling lambat hari terakhir kerja, mendadak segera | "Saat pemberhentian, semua akses dicabut paling lambat pada hari terakhir kerja; untuk pemberhentian mendadak, segera." (Bagian 7.5) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |
| 2 | Review akses privileged triwulanan, akses biasa semesteran | "akses privileged setiap triwulan, akses biasa setiap semester." (Bagian 7.6) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |
| 3 | Akses privileged ke sistem pelanggan butuh approval Head of Operation, plus persetujuan pelanggan bila kontrak mensyaratkan | "Akses privileged ke sistem pelanggan butuh approval Head of Operation, dan bila kontrak mensyaratkan, persetujuan pelanggan." (Bagian 7.1) | 1JoSiwoMglIxy7Ic3t0EhRfvzJgf5ydzT |

### USULAN
| # | Butir | Letak di dokumen | Pemutus yang disarankan |
|---|---|---|---|
| U1 | Matriks tingkat akses acuan per peran (label USULAN dari sumber) | Bagian 4 | Fani |
| U2 | Keputusan permintaan akses 2 hari kerja sesudah atasan mengonfirmasi | Bagian 8 | Fani |
| U3 | Pembuatan akun 1 hari kerja sesudah approval | Bagian 8 | Fani |
| U4 | Catatan hasil sampling log sesi privileged disimpan di Google Drive, pemilik Lead SOC | Bagian 11 | Fani |
| U5 | Retensi catatan sampling 3 tahun | Bagian 11 | Fani |

Jumlah USULAN berlabel di dokumen: 5 (sama dengan hitungan lint). Putaran perbaikan tidak menambah USULAN.

### Open items
Ringkasan open items sebelumnya (rinci di bagian 8 di atas) dan butir baru dari putaran perbaikan.

| # | Butir | Pemutus yang disarankan |
|---|---|---|
| 1 | Penyetuju dokumen: sumber COO, defaults Samuel (defaults dipakai) | owner, Samuel |
| 2 | Head of Operation belum dipetakan ke jabatan nyata (HR-ORG-01 belum DONE) | owner, Fani |
| 3 | Status password manager (vault) belum terkonfirmasi; SOP mewajibkan password disimpan di sana | Ops (Fani) |
| 4 | Batas Service Hub (GLPI) lawan Zammad untuk permintaan akses | owner |
| 5 | Log Jumphost minimal 90 hari tidak menjamin cakupan sampling triwulanan | Fani |
| 6 | Tenggat 10 hari kerja untuk Ubah atau Cabut hasil review: dasar REG-04, bukan SOP-02 sumber; target 95% hanya untuk temuan | Fani |
| 7 | Pelaku permintaan persetujuan pelanggan tidak disebut sumber | Fani |
| 8 | "approval Lead" restore Acronis: ditulis "Lead NOC atau Lead SOC", tafsir perlu konfirmasi | Fani |
| 9 | SoA SNX-ISMS-SOA-01 memetakan 8.18 dan 8.3 ke "Bagian 7.7" yang kini butir 6.7; kecocokan isi 8.18 belum dinilai | konsultan SoA, Fani |
| 10 | REG-04: istilah Level tidak sama dengan matriks; belum ada matriks per sistem dan peran | Fani |
| 11 | Scope tanpa pengecualian tertulis; pelaku pencabutan akun vendor yang kedaluwarsa tidak disebut | Fani |
| 12 | POL-OPS-001 P-03 membolehkan kredensial lewat japri, SOP-02 melarang chat; POL-OPS-001 masih DRAFT dengan nomor USULAN | Fani |
| 13 | Template tidak punya slot KPI; 4 target sumber dilebur ke bagian 8 | Aziz |
| 14 (baru) | Kontrol pengganti saat sistem internal tidak mendukung akses privileged lewat Jumphost tidak disebut sumber. Baris pengecualian hanya menyatakan akses langsung dengan akun terpisah dari akun harian; tidak ada kontrol karangan | Fani |
| 15 (baru) | Pencatatan pemakaian 
- Nonblocking verifikasi ulang (12) dan pemeriksa PDF (7) ada di qa/ISMS-SOP-02.verify.json dan qa/ISMS-SOP-02.pdfcheck.json untuk review tim; putaran 1 di qa/ISMS-SOP-02.verify.r1.json.
