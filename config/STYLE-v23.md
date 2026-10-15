# STYLE v23: bahasa semi-bilingual SINUX dan form rapi

Ditulis LEAD ISO, 15 Okt 2026, atas masukan owner sesudah review tim: "Masih slop, AI sekali. Bahasa Indonya aneh. Better mix, istilah dll tetap in English. Semi bilingual. Hasilnya hanya kurang di bahasa, dan di frm/form kurang rapih dan bahasa kurang bagus."
Berkas ini menggantikan RUNBOOK §6a butir 1 dan 9 serta tiga butir prompt_addendum (lihat LEAD-GUIDE G-4). Butir §6a lain tetap berlaku.

Acuan suara: cara tim menulis dokumennya sendiri, misalnya "SOP Billing and Invoicing" tim FAT dan dokumen Operation Fani. Bahasa Indonesia bisnis yang baku, dengan istilah kerja tetap English. Pembaca: tim SINUX yang menjalankan prosedur, dan auditor ISO.

## 1. Kapan memakai English
1. Istilah kerja, ISO, IT, dan keuangan yang dipakai tim ditulis dalam English apa adanya (glossary di §5). Tidak diterjemahkan dan tidak dimiringkan.
2. Padanan dalam kurung hanya sekali, pada kemunculan pertama, bila pembaca awam mungkin tidak paham: "Term of Payment (TOP)". Setelah itu pakai satu bentuk saja.
3. Kata kerja, kata sambung, dan susunan kalimat tetap Bahasa Indonesia. Kata kerja Indonesia yang sudah ada (meninjau, memeriksa, menyetujui) tidak diganti.
4. Sebutan pihak luar (klien, customer, pelanggan) mengikuti istilah yang paling sering dipakai di sumber tim untuk dokumen itu. Dokumen T2 mengikuti SOP induknya. Satu dokumen memakai satu istilah saja.
5. Peta istilah wajib, diterapkan mekanis melalui satu skrip yang diff-nya di-review, di teks badan dan judul dari spec di 70 dokumen:
   - rekaman menjadi record
   - tiket menjadi ticket
   - formulir menjadi form
   - tinjauan dan peninjauan (kata benda) menjadi review
   - tindakan korektif menjadi corrective action
   - akar masalah menjadi root cause
   Ikuti kapitalisasi asal. Tidak disentuh: label yang ditulis langsung oleh tools/render_sop.py, baris header kolom xlsx, nama peran, judul dokumen, nama berkas tim yang dikutip, dan istilah yang didefinisikan di tabel Istilah sebagai nama proses resmi (misalnya Persetujuan Legal). Istilah lain dibiarkan, termasuk insiden, persetujuan, dan ketidaksesuaian.

## 2. Kalimat
1. Kalimat pasif "di-" boleh dipakai di bagian Definisi, Policy, Rekaman, dan Ketentuan Penggunaan form bila pelakunya jelas dari tabel Roles: "Invoice dikirim sebagai PDF terkunci."
2. Langkah prosedur di bagian 6 dan tabel penanganan di bagian 9 tetap menyebut satu pelaku per langkah. Pelaku disebut sekali di awal langkah; kalimat lanjutan dalam langkah yang sama tidak mengulangnya.
3. Dilarang memakai pola "yang <pelaku> <kata kerja dasar>", misalnya "yang SINUX terbitkan" atau "yang klien potong". Tulis "yang diterbitkan SINUX" atau "yang dipotong klien".
4. Butir di bagian Petunjuk Pengisian, Cara Mengisi, Ketentuan Pengisian, dan Cara pakai (xlsx) memakai kalimat perintah untuk pengisi utama: "Isi kolom Severity hanya untuk RCA insiden." Pengisi utama cukup disebut sekali di bagian Peran. Bila langkah dilakukan peran lain, peran itu tetap disebut, di tengah kalimat atau di akhir: "Setelah terisi, form diperiksa Line Manager Legal." 
5. Pilihan kata: "melalui" atau "via" (bukan "lewat"); "setelah" (bukan "sesudah"); "jika" atau "apabila" (bukan "bila" yang diulang di awal kalimat).
6. Panjang kalimat bervariasi, paling panjang sekitar 30 kata. Kalimat yang memuat lebih dari dua klausa "dan" dipecah.
7. Definisi diawali huruf kapital, satu kalimat, tanpa mengulang istilahnya. Istilah yang artinya jelas bagi karyawan (misalnya Klien, Invoice) tidak perlu didefinisikan, kecuali tim mendefinisikannya di sumber.

## 3. Rujukan, label, dan catatan internal
1. Rujuk butir lain hanya bila pembaca harus membukanya untuk menjalankan langkah. Paling banyak satu rujukan per paragraf atau per sel tabel.
2. Hapus kalimat penunjuk seperti "Lama dan titik awal hitungannya ada di butir 4.8" atau "Masa simpannya ada di bagian 11". Bila faktanya perlu, tulis faktanya.
3. Rujukan ke dokumen lain cukup "sesuai SNX-LEG-SOP-02". Nomor butir ditambahkan hanya bila butirnya spesifik.
4. Rujukan ke butir dokumen sendiri yang ditulis di baris tabel milik dokumen lain diberi penanda: "butir 4.8 SOP ini" atau "butir 3 form ini".
5. Label (USULAN) hanya untuk nilai atau aturan yang belum bersumber dari tim: angka, batas waktu, kontrol baru, dan pemetaan jabatan baru. Satu label per butir, diletakkan di akhir butir.
6. Label (USULAN) yang sudah ada dipertahankan, kecuali pada instruksi pengisian mekanis (cara mencentang, menambah baris, format tanggal). Setiap label yang dihapus dicatat di notes/<KEY>.md di bawah judul "W10 label dihapus", lengkap dengan kalimat aslinya. USULAN-OPEN dan Master List dibangun ulang setelahnya.
7. Butir meta yang mendaftar butir lain berstatus USULAN tidak dihapus, karena menghapusnya menggeser nomor butir yang dirujuk dokumen lain. Butir itu ditulis ulang dalam satu kalimat wajar, nomornya tetap. Contoh SNX-FAT-SOP-01 butir 4.15: "Pembagian tugas pada butir 4.3, 4.9, 4.11, 4.12, 4.14, dan 4.16, pemantauan Overdue di bagian 9, serta Finance Lead sebagai pemilik record di bagian 11 masih menunggu keputusan FAT (USULAN)."
8. Catatan penyusunan atau pemetaan tidak ditulis di badan dokumen. Contoh: "Jabatan Divisi Operation yang belum punya pemegang menurut SNX-HR-ORG-01" di tabel Roles. Catatan seperti itu dipindah ke notes/<KEY>.md.
9. Penomoran butir dan heading tidak berubah di W10. Tidak ada butir, bagian, atau tabel yang dihapus, dipindah, atau digabung.

## 4. Form rapi (docx dan xlsx)
1. Docx form: bagian sebelum isi form dipadatkan dengan kalimat yang lebih pendek dan wajar, tanpa menghapus butir atau memindahkan bagian. Jumlah halaman dan halaman awal bagian ISI diukur sebelum dan sesudah, lalu dilaporkan.
2. Tabel di semua dokumen:
   - Teks sel rata kiri, tidak rata kiri-kanan.
   - Baris judul berulang di tiap halaman, dan baris tidak terbelah antarhalaman.
   - Lebar kolom proporsional: No atau Kode sekitar 1,2 cm, Status sekitar 2,2 cm, dan kolom teks utama paling lebar. Total lebar 16 cm.
3. Xlsx:
   - Baris judul kolom dibekukan (freeze panes).
   - Wrap text di kolom teks, dan lebar kolom sesuai isi.
   - Page setup landscape, fit to 1 page wide, dan baris judul dicetak berulang (print titles).
   - Di sheet Kontrol Dokumen, semua sel panjang di-wrap.
   - Daftar sheet data beserta baris header-nya ditulis worker di reports/w10/xlsx_sheets.json sebelum diubah. Sheet berisi gambar alur tidak diubah.

## 5. Glossary
Ditulis dalam English (kata benda kerja; peta wajib di §1.5, sisanya dipakai saat menulis ulang kalimat): record, review, reviewer, checker, maker, requester, PIC, owner, process owner, invoice, Term of Payment (TOP), Accounts Receivable (AR), Accounts Payable (AP), audit trail, soft copy, hard copy, milestone, deliverable, handover, ticket, incident, escalation, SLA, breach, downtime, RCA, root cause, corrective action, preventive action, change request, UAT, go-live, backup, restore, access review, user access, privileged access, patch, vulnerability, asset register, risk register, risk owner, risk treatment, likelihood, impact, severity, priority, compliance, NDA, DoA, KPI, campaign, lead, content, claim, checklist, form, register, report, template, folder.
Tetap Bahasa Indonesia: Berita Acara Serah Terima (BAST), Perjanjian Kerja Sama (PKS), Surat Perintah Kerja (SPK), Faktur Pajak, e-Faktur, PPN, PPh, NPWP, persetujuan, insiden, ketidaksesuaian, pemusnahan, masa simpan, Direktur Utama, Direktur, Departemen, serta nama jabatan dan unit di SNX-HR-ORG-01.
Nama peran yang sudah ada di tabel Peran atau Roles tidak diganti di W10, termasuk Pemeriksa, Pencatat, Penanggap alternatif, dan Pemverifikasi. Kalimat baru tidak membuat nama peran baru.

## 6. Contoh dari out/ commit bed1bb6
| Dokumen | Sebelum | Sesudah |
|---|---|---|
| SNX-FAT-SOP-01, Definisi | Faktur Pajak Keluaran elektronik, bukti pemungutan PPN yang SINUX terbitkan lewat CoreTax DJP. | Faktur Pajak Keluaran elektronik yang diterbitkan SINUX melalui CoreTax DJP sebagai bukti pemungutan PPN. |
| SNX-FAT-SOP-01, 4.1 | Finance Staff memproses permohonan penagihan hanya bila empat dokumen pendukung (bagian 3) sudah lengkap dan tervalidasi. | Permohonan penagihan hanya diproses jika PKS, PO/SPK, BAST, dan NPWP klien sudah lengkap dan tervalidasi. |
| SNX-FAT-SOP-01, Definisi TOP | Jangka waktu klien melunasi invoice sampai tanggal jatuh tempo. Lama dan titik awal hitungannya ada di butir 4.8. | Jangka waktu pelunasan invoice sampai tanggal jatuh tempo. |
| SNX-OPS-FRM-10, Petunjuk 7 | Lead NOC atau Lead SOC menambah baris di tabel Tindakan bila satu jenis tindakan lebih dari satu (USULAN). | Tambah baris di tabel Tindakan jika ada lebih dari satu tindakan sejenis (USULAN). |
| SNX-OPS-FRM-10, Petunjuk 6 | Lead NOC atau Lead SOC menjawab tiap tingkat 5 Why dengan bukti, misalnya tiket, log, atau change request. | Jawab tiap tingkat 5 Why dengan bukti, misalnya ticket, log, atau change request. |
| SNX-LEG-FRM-01, Ketentuan 1 | Staff Legal memakai satu formulir untuk satu kontrak pelanggan dan mengisinya sesudah Unit Kerja Pemohon menyerahkan permintaan penelaahan secara lengkap (SNX-LEG-SOP-02 butir 6.1). Kewajiban memakai formulir ini untuk setiap kontrak pelanggan belum diputus (USULAN: Line Manager Legal memutuskan). | Satu form dipakai untuk satu kontrak pelanggan, dan diisi setelah Unit Kerja Pemohon menyerahkan permintaan penelaahan yang lengkap (SNX-LEG-SOP-02 butir 6.1). Apakah form ini wajib untuk setiap kontrak pelanggan masih menunggu keputusan Line Manager Legal (USULAN). |

## 7. Kutipan suara tim (verbatim, sumber "1. SOP Billing and Invoicing", fileId 1sZfTBx1ZxBIryhzJHf14eOcRR7HuQ1E1Qox3DdwmHKI)
- "Batas Kewenangan Pembuatan: Staff Finance dilarang keras menerbitkan atau mengirimkan invoice kepada klien tanpa persetujuan (approval) tertulis dari Finance Lead."
- "Soft Copy (Digital): Secara standar, seluruh berkas penagihan dikirimkan secara elektronik (PDF) via email resmi ke email PIC AP dan PIC Proyek."
- "Setiap draf invoice wajib melalui proses validasi 3 arah (3-way matching) antara nominal PKS, acuan PO, dan bukti penyerahan BAST sebelum e-Faktur Pajak diterbitkan."
Catatan: ambil register dan campuran istilahnya, bukan struktur bullet atau angka di dalamnya.

## 8. Substansi beku
1. Pass bahasa tidak boleh mengubah hal-hal berikut:
   - angka, batas waktu, dan nama orang;
   - jabatan, peran, dan kode dokumen;
   - isi keputusan G-3 dan status Draft;
   - arti setiap aturan.
2. Yang boleh hilang hanya kalimat penunjuk (§3.2), catatan internal (§3.8), dan label mekanis (§3.6). Setiap penghapusan dicatat di notes/<KEY>.md.
3. Butir dan heading tidak bergeser (§3.9). Kepatuhan dicek dengan tools/w10_langscan.py diff.
