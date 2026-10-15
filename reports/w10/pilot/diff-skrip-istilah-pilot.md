# Diff skrip istilah W10, 5 dokumen pilot

Skrip: reports/orch/w10.py terms (peta STYLE-v23 §1.5: rekaman > record, tiket > ticket, formulir > form, tinjauan/peninjauan > review, tindakan korektif > corrective action, akar masalah > root cause; diksi §2.5: lewat > melalui, sesudah > setelah). Dijalankan sekali, sebelum penyusun bahasa bekerja. Heading, meta, nama peran, kolom PIC, dan id diagram tidak disentuh (heading dibekukan G-4). Basis bed1bb6.

```diff
# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), OPS-FRM-02: 0 teks berubah. Basis bed1bb6.
```

```diff
# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), OPS-FRM-10: 17 teks berubah. Basis bed1bb6.

@@ .sections[0].blocks[5].p
- Tiket tetap dicatat di SNX-OPS-FRM-08 dan change request di SNX-OPS-FRM-04; form ini hanya memuat nomornya. Insiden keamanan informasi dicatat juga di SNX-ISMS-FRM-02.
+ Ticket tetap dicatat di SNX-OPS-FRM-08 dan change request di SNX-OPS-FRM-04; form ini hanya memuat nomornya. Insiden keamanan informasi dicatat juga di SNX-ISMS-FRM-02.

@@ .sections[1].blocks[0].table.rows[0][1]
- Root cause analysis: analisis untuk menemukan akar masalah suatu kejadian, dicatat di form ini.
+ Root cause analysis: analisis untuk menemukan root cause suatu kejadian, dicatat di form ini.

@@ .sections[1].blocks[0].table.rows[1][0]
- Akar masalah
+ Root cause

@@ .sections[1].blocks[0].table.rows[10][1]
- Tindakan menghilangkan akar masalah.
+ Tindakan menghilangkan root cause.

@@ .sections[1].blocks[0].table.rows[13][1]
- Metode analisis yang mengelompokkan penyebab ke enam kategori di bagian Analisis akar masalah.
+ Metode analisis yang mengelompokkan penyebab ke enam kategori di bagian Analisis root cause.

@@ .sections[2].blocks[0].table.rows[1][1]
- Pemilik dokumen. Menyetujui dan mengirim RCA. Menutup RCA sesudah verifikasi (USULAN).
+ Pemilik dokumen. Menyetujui dan mengirim RCA. Menutup RCA setelah verifikasi (USULAN).

@@ .sections[3].blocks[5].p
- 6. Lead NOC atau Lead SOC menjawab tiap tingkat 5 Why dengan bukti, misalnya tiket, log, atau change request.
+ 6. Lead NOC atau Lead SOC menjawab tiap tingkat 5 Why dengan bukti, misalnya ticket, log, atau change request.

@@ .sections[3].blocks[11].p
- 12. Bila hasilnya Belum efektif, Lead NOC atau Lead SOC mengulang analisis di bagian Analisis akar masalah.
+ 12. Bila hasilnya Belum efektif, Lead NOC atau Lead SOC mengulang analisis di bagian Analisis root cause.

@@ .sections[3].blocks[13].p
- Pengiriman RCA ke pelanggan terjadi sebelum verifikasi efektivitas. RCA ditutup hanya sesudah tindakan terbukti efektif.
+ Pengiriman RCA ke pelanggan terjadi sebelum verifikasi efektivitas. RCA ditutup hanya setelah tindakan terbukti efektif.

@@ .sections[4].blocks[0].flow.nodes.b
- Kumpulkan kronologi dan bukti / tiket, log, change request
+ Kumpulkan kronologi dan bukti / ticket, log, change request

@@ .sections[4].blocks[0].flow.nodes.c
- Analisis akar masalah / 5 Why, Fishbone, atau metode lain
+ Analisis root cause / 5 Why, Fishbone, atau metode lain

@@ .sections[4].blocks[0].flow.nodes.f
- Laksanakan tindakan / lewat SNX-OPS-SOP-02 / bila mengubah production
+ Laksanakan tindakan / melalui SNX-OPS-SOP-02 / bila mengubah production

@@ .sections[4].blocks[0].flow.caption
- Gambar 1. Alur RCA dan tindakan korektif. Garis putus-putus kembali ke analisis.
+ Gambar 1. Alur RCA dan corrective action. Garis putus-putus kembali ke analisis.

@@ .sections[5].blocks[1].table.rows[2][1]
- [nomor tiket Zammad di SNX-OPS-FRM-08, nomor CR di SNX-OPS-FRM-04, atau nomor ketidaksesuaian audit]
+ [nomor ticket Zammad di SNX-OPS-FRM-08, nomor CR di SNX-OPS-FRM-04, atau nomor ketidaksesuaian audit]

@@ .sections[5].blocks[14].table.rows[0][0]
- Akar masalah
+ Root cause

@@ .sections[6].blocks[0].table.rows[3][1]
- Technical Ticket / Incident Register. Sumber nomor tiket; kolom No RCA memuat nomor RCA.
+ Technical Ticket / Incident Register. Sumber nomor ticket; kolom No RCA memuat nomor RCA.

@@ .sections[7].blocks[1].table.header[0]
- Rekaman
+ Record
```

```diff
# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), LEG-FRM-01: 31 teks berubah. Basis bed1bb6.

@@ .sections[0].blocks[1].p
- Formulir ini memuat daftar periksa yang dipakai Departemen Legal untuk menelaah kontrak yang diajukan pelanggan sebelum kontrak ditandatangani oleh Pejabat Berwenang. Dengan formulir ini Departemen Legal mengidentifikasi risiko hukum serta risiko komersial, dan memastikan hak dan kewajiban para pihak jelas.
+ Form ini memuat daftar periksa yang dipakai Departemen Legal untuk menelaah kontrak yang diajukan pelanggan sebelum kontrak ditandatangani oleh Pejabat Berwenang. Dengan form ini Departemen Legal mengidentifikasi risiko hukum serta risiko komersial, dan memastikan hak dan kewajiban para pihak jelas.

@@ .sections[0].blocks[4].p
- Departemen Legal memakai formulir ini untuk menelaah kontrak antara SINUX dan pelanggan, termasuk perjanjian layanan teknologi informasi, layanan komputasi awan, penjualan perangkat keras, layanan implementasi, layanan pemeliharaan, dan bentuk kerja sama komersial lainnya. Staff Legal menyesuaikan penelaahan dengan jenis layanan, karakteristik transaksi, dan risiko tiap kontrak.
+ Departemen Legal memakai form ini untuk menelaah kontrak antara SINUX dan pelanggan, termasuk perjanjian layanan teknologi informasi, layanan komputasi awan, penjualan perangkat keras, layanan implementasi, layanan pemeliharaan, dan bentuk kerja sama komersial lainnya. Staff Legal menyesuaikan penelaahan dengan jenis layanan, karakteristik transaksi, dan risiko tiap kontrak.

@@ .sections[0].blocks[5].p
- Butir berikut dikecualikan dari formulir ini.
+ Butir berikut dikecualikan dari form ini.

@@ .sections[0].blocks[6].table.rows[0][1]
- Departemen Legal tidak menelaahnya dengan formulir ini. Kontrak vendor dan pemasok memakai SNX-LEG-FRM-02 (USULAN).
+ Departemen Legal tidak menelaahnya dengan form ini. Kontrak vendor dan pemasok memakai SNX-LEG-FRM-02 (USULAN).

@@ .sections[0].blocks[6].table.rows[1][1]
- Tetap milik Pejabat Berwenang dan Unit Kerja Terkait sesuai bidangnya. Formulir ini hanya memuat catatan risikonya (SNX-LEG-SOP-02).
+ Tetap milik Pejabat Berwenang dan Unit Kerja Terkait sesuai bidangnya. Form ini hanya memuat catatan risikonya (SNX-LEG-SOP-02).

@@ .sections[0].blocks[6].table.rows[2][1]
- Diatur di SNX-LEG-SOP-02. Formulir ini hanya memuat hasil penelaahan.
+ Diatur di SNX-LEG-SOP-02. Form ini hanya memuat hasil penelaahan.

@@ .sections[0].blocks[6].table.rows[3][0]
- Tinjauan kepatuhan pelindungan data pribadi dan kerahasiaan yang menyeluruh
+ Review kepatuhan pelindungan data pribadi dan kerahasiaan yang menyeluruh

@@ .sections[0].blocks[6].table.rows[3][1]
- Memakai SNX-LEG-FRM-03 (USULAN). Formulir ini hanya memuat pemeriksaan ketentuan kontraknya (aspek C5.1 dan C5.2).
+ Memakai SNX-LEG-FRM-03 (USULAN). Form ini hanya memuat pemeriksaan ketentuan kontraknya (aspek C5.1 dan C5.2).

@@ .sections[1].blocks[1].table.rows[8][1]
- Pemeriksaan satu kontrak pelanggan dengan formulir ini, dari pengisian Informasi Kontrak sampai Rekomendasi.
+ Pemeriksaan satu kontrak pelanggan dengan form ini, dari pengisian Informasi Kontrak sampai Rekomendasi.

@@ .sections[2].blocks[0].p
- 1. Staff Legal memakai satu formulir untuk satu kontrak pelanggan dan mengisinya sesudah Unit Kerja Pemohon menyerahkan permintaan penelaahan secara lengkap (SNX-LEG-SOP-02 butir 6.1). Kewajiban memakai formulir ini untuk setiap kontrak pelanggan belum diputus (USULAN: Line Manager Legal memutuskan).
+ 1. Staff Legal memakai satu form untuk satu kontrak pelanggan dan mengisinya setelah Unit Kerja Pemohon menyerahkan permintaan penelaahan secara lengkap (SNX-LEG-SOP-02 butir 6.1). Kewajiban memakai form ini untuk setiap kontrak pelanggan belum diputus (USULAN: Line Manager Legal memutuskan).

@@ .sections[2].blocks[4].p
- 5. Staff Legal mencentang Hasil Penelaahan dan satu Rekomendasi (cara mencentang di Petunjuk Pengisian butir 5), dan menulis dasar rekomendasi. Hasil Penelaahan boleh lebih dari satu pilihan, kecuali pilihan Tidak terdapat temuan (USULAN). Rekomendasi hanya satu pilihan (USULAN). Line Manager Legal memeriksa formulir terisi.
+ 5. Staff Legal mencentang Hasil Penelaahan dan satu Rekomendasi (cara mencentang di Petunjuk Pengisian butir 5), dan menulis dasar rekomendasi. Hasil Penelaahan boleh lebih dari satu pilihan, kecuali pilihan Tidak terdapat temuan (USULAN). Rekomendasi hanya satu pilihan (USULAN). Line Manager Legal memeriksa form terisi.

@@ .sections[2].blocks[5].p
- 6. Rekomendasi pada formulir ini bukan Persetujuan Legal. Line Manager Legal memberi Persetujuan Legal menurut SNX-LEG-SOP-02, dan Persetujuan Legal bukan pengganti persetujuan Pejabat Berwenang (SNX-LEG-SOP-02 butir 4.2).
+ 6. Rekomendasi pada form ini bukan Persetujuan Legal. Line Manager Legal memberi Persetujuan Legal menurut SNX-LEG-SOP-02, dan Persetujuan Legal bukan pengganti persetujuan Pejabat Berwenang (SNX-LEG-SOP-02 butir 4.2).

@@ .sections[2].blocks[6].p
- 7. Staff Legal menelaah ulang kontrak yang berubah material sesudah Persetujuan Legal (SNX-LEG-SOP-02 butir 4.14), dan mengisi formulir baru untuk telaah ulang itu (USULAN).
+ 7. Staff Legal menelaah ulang kontrak yang berubah material setelah Persetujuan Legal (SNX-LEG-SOP-02 butir 4.14), dan mengisi form baru untuk telaah ulang itu (USULAN).

@@ .sections[2].blocks[7].p
- 8. Staff Legal menyimpan formulir terisi bersama berkas kontrak di folder Google Drive Departemen Legal (USULAN, SNX-LEG-SOP-01 butir 4.24 dan SNX-LEG-SOP-03 butir 4.8) dan menulis lokasinya pada tabel Lokasi Penyimpanan Dokumen. Formulir terisi berisi nama pelanggan dan nilai kontrak, sehingga Staff Legal memberinya tingkat RESTRICTED (Internal) menurut SNX-ISMS-PRO-01.
+ 8. Staff Legal menyimpan form terisi bersama berkas kontrak di folder Google Drive Departemen Legal (USULAN, SNX-LEG-SOP-01 butir 4.24 dan SNX-LEG-SOP-03 butir 4.8) dan menulis lokasinya pada tabel Lokasi Penyimpanan Dokumen. Form terisi berisi nama pelanggan dan nilai kontrak, sehingga Staff Legal memberinya tingkat RESTRICTED (Internal) menurut SNX-ISMS-PRO-01.

@@ .sections[3].blocks[0].table.header[1]
- Tugas pada formulir ini
+ Tugas pada form ini

@@ .sections[3].blocks[0].table.rows[0][1]
- Mengisi formulir, menelaah kontrak, mencatat temuan dan rekomendasi, dan menyimpan formulir terisi sebagai pencatat rekaman (Ketentuan butir 1 sampai 5, 7, dan 8). Peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01.
+ Mengisi form, menelaah kontrak, mencatat temuan dan rekomendasi, dan menyimpan form terisi sebagai pencatat record (Ketentuan butir 1 sampai 5, 7, dan 8). Peran ini dipetakan ke jabatan Legal & Compliance (JA-09) di SNX-HR-ORG-01.

@@ .sections[3].blocks[0].table.rows[1][1]
- Pemilik formulir ini dan formulir terisi (USULAN, SNX-LEG-SOP-02 butir 4.19 dan SNX-LEG-SOP-03). Menetapkan Target Penyelesaian, memeriksa formulir terisi, dan memberi Persetujuan Legal (Ketentuan butir 1, 2, 4, 5, dan 6). Peran ini dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01.
+ Pemilik form ini dan form terisi (USULAN, SNX-LEG-SOP-02 butir 4.19 dan SNX-LEG-SOP-03). Menetapkan Target Penyelesaian, memeriksa form terisi, dan memberi Persetujuan Legal (Ketentuan butir 1, 2, 4, 5, dan 6). Peran ini dipetakan ke jabatan Legal & Compliance (JA-08) di SNX-HR-ORG-01.

@@ .sections[3].blocks[0].table.rows[2][1]
- Menyerahkan kontrak pelanggan dan data permintaan lewat PIC Internal (Ketentuan butir 1 dan 2).
+ Menyerahkan kontrak pelanggan dan data permintaan melalui PIC Internal (Ketentuan butir 1 dan 2).

@@ .sections[3].blocks[1].p
- Pembuat, pemeriksa, dan penyetuju formulir ini tercantum di blok Approval pada halaman depan.
+ Pembuat, pemeriksa, dan penyetuju form ini tercantum di blok Approval pada halaman depan.

@@ .sections[6].blocks[0].table.rows[0][1]
- Legal Operational. Butir 4.21 memuat tinjauan pelindungan data pribadi pada kontrak, dan butir 4.24 memuat usulan repositori dokumen legal (USULAN).
+ Legal Operational. Butir 4.21 memuat review pelindungan data pribadi pada kontrak, dan butir 4.24 memuat usulan repositori dokumen legal (USULAN).

@@ .sections[6].blocks[0].table.rows[1][1]
- Contract Review & Legal Approval. Prosedur penerimaan permintaan, penelaahan, persetujuan, dan penandatanganan kontrak. Formulir ini tercantum di prosedur itu sebagai SNX-LEG-FRM-01, checklist review untuk kontrak pelanggan (USULAN).
+ Contract Review & Legal Approval. Prosedur penerimaan permintaan, penelaahan, persetujuan, dan penandatanganan kontrak. Form ini tercantum di prosedur itu sebagai SNX-LEG-FRM-01, checklist review untuk kontrak pelanggan (USULAN).

@@ .sections[6].blocks[0].table.rows[2][1]
- Legal Document Control & Retention. Memuat tujuh kategori dokumen legal dan usulan periode retensinya. Formulir terisi masuk Kategori 4, dan kontrak beserta korespondensi masuk Kategori 1 (USULAN).
+ Legal Document Control & Retention. Memuat tujuh kategori dokumen legal dan usulan periode retensinya. Form terisi masuk Kategori 4, dan kontrak beserta korespondensi masuk Kategori 1 (USULAN).

@@ .sections[6].blocks[0].table.rows[4][1]
- Data Protection & Confidentiality Compliance Review. Tinjauan kepatuhan pelindungan data pribadi dan kerahasiaan yang lebih luas dari aspek C5.1 dan C5.2 (USULAN).
+ Data Protection & Confidentiality Compliance Review. Review kepatuhan pelindungan data pribadi dan kerahasiaan yang lebih luas dari aspek C5.1 dan C5.2 (USULAN).

@@ .sections[7].blocks[1].table.header[0]
- Rekaman
+ Record

@@ .sections[7].blocks[1].table.rows[0][0]
- Formulir terisi per kontrak pelanggan
+ Form terisi per kontrak pelanggan

@@ .sections[7].blocks[4].table.header[2]
- Hubungan dengan formulir ini
+ Hubungan dengan form ini

@@ .sections[7].blocks[4].table.rows[0][1]
- 8.2.3 Peninjauan persyaratan produk dan jasa
+ 8.2.3 Review persyaratan produk dan jasa

@@ .sections[7].blocks[4].table.rows[1][2]
- Staff Legal menelaah ulang kontrak yang berubah material dengan formulir baru (Ketentuan butir 7).
+ Staff Legal menelaah ulang kontrak yang berubah material dengan form baru (Ketentuan butir 7).

@@ .sections[7].blocks[4].table.rows[2][2]
- Staff Legal menyimpan formulir terisi dan mencatat lokasi, pemilik, dan klasifikasinya.
+ Staff Legal menyimpan form terisi dan mencatat lokasi, pemilik, dan klasifikasinya.

@@ .sections[7].blocks[4].table.rows[3][2]
- Staff Legal menelaah kesesuaian ketentuan kontrak dengan hukum yang berlaku dan persyaratan kontraktual lewat tabel Daftar Periksa.
+ Staff Legal menelaah kesesuaian ketentuan kontrak dengan hukum yang berlaku dan persyaratan kontraktual melalui tabel Daftar Periksa.

@@ .sections[8].blocks[0].p
- Formulir ini berstatus Draft dan baru berlaku sesudah Direktur Utama menandatangani blok Approval. Line Manager Legal meninjau formulir ini setiap tahun.
+ Form ini berstatus Draft dan baru berlaku setelah Direktur Utama menandatangani blok Approval. Line Manager Legal meninjau form ini setiap tahun.
```

```diff
# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), FAT-SOP-01: 18 teks berubah. Basis bed1bb6.

@@ .scope[3]
- Di luar scope SOP ini: invoice yang SINUX terima dari vendor beserta pembayarannya; pelaporan dan penyetoran pajak (SNX-FAT-SOP-05); tindak lanjut invoice yang melewati jatuh tempo (SOP Account Receivable & Collection, sedang dalam peninjauan).
+ Di luar scope SOP ini: invoice yang SINUX terima dari vendor beserta pembayarannya; pelaporan dan penyetoran pajak (SNX-FAT-SOP-05); tindak lanjut invoice yang melewati jatuh tempo (SOP Account Receivable & Collection, sedang dalam review).

@@ .definitions[4][1]
- Dokumen yang mencatat pemusnahan arsip sesudah masa retensi berakhir.
+ Dokumen yang mencatat pemusnahan arsip setelah masa retensi berakhir.

@@ .definitions[10][1]
- Faktur Pajak Keluaran elektronik, bukti pemungutan PPN yang SINUX terbitkan lewat CoreTax DJP.
+ Faktur Pajak Keluaran elektronik, bukti pemungutan PPN yang SINUX terbitkan melalui CoreTax DJP.

@@ .definitions[14][1]
- Formulir yang klien isi untuk menyerahkan data master klien.
+ Form yang klien isi untuk menyerahkan data master klien.

@@ .definitions[17][1]
- Badan usaha yang memesan jasa SINUX lewat PKS atau PO dan menerima invoice dari SINUX (customer).
+ Badan usaha yang memesan jasa SINUX melalui PKS atau PO dan menerima invoice dari SINUX (customer).

@@ .policy[4]
- 4.5 Penyerahan Jasa Kena Pajak (JKP) dikenai PPN 12% (USULAN). Finance Staff menerbitkan e-Faktur Pajak secara elektronik lewat CoreTax DJP dalam proses penerbitan invoice, dengan urutan di butir 6.2.
+ 4.5 Penyerahan Jasa Kena Pajak (JKP) dikenai PPN 12% (USULAN). Finance Staff menerbitkan e-Faktur Pajak secara elektronik melalui CoreTax DJP dalam proses penerbitan invoice, dengan urutan di butir 6.2.

@@ .policy[6]
- 4.7 Finance Staff mengirim berkas penagihan lewat email resmi ke PIC Finance/AP klien dan PIC Proyek klien sebagai PDF terkunci (non-editable). Finance Staff mengirim hard copy, yaitu cetakan bertanda tangan dan berstempel, lewat kurir hanya bila PKS mensyaratkannya.
+ 4.7 Finance Staff mengirim berkas penagihan melalui email resmi ke PIC Finance/AP klien dan PIC Proyek klien sebagai PDF terkunci (non-editable). Finance Staff mengirim hard copy, yaitu cetakan bertanda tangan dan berstempel, melalui kurir hanya bila PKS mensyaratkannya.

@@ .policy[14]
- 4.15 Penetapan pelaku pada butir 4.3, 4.9, 4.11, 4.12, 4.14, dan 4.16, pemantauan Overdue di bagian 9, serta Finance Lead sebagai pemilik rekaman di bagian 11, berstatus (USULAN).
+ 4.15 Penetapan pelaku pada butir 4.3, 4.9, 4.11, 4.12, 4.14, dan 4.16, pemantauan Overdue di bagian 9, serta Finance Lead sebagai pemilik record di bagian 11, berstatus (USULAN).

@@ .policy[15]
- 4.16 Finance Staff mencatat pemusnahan arsip sesudah masa retensi berakhir dalam Berita Acara Pemusnahan Dokumen. Finance Lead dan Direktur Utama menyetujui pemusnahan itu.
+ 4.16 Finance Staff mencatat pemusnahan arsip setelah masa retensi berakhir dalam Berita Acara Pemusnahan Dokumen. Finance Lead dan Direktur Utama menyetujui pemusnahan itu.

@@ .procedures[3].steps[3][0]
- Kirim berkas cetak ke alamat penagihan klien lewat kurir.
+ Kirim berkas cetak ke alamat penagihan klien melalui kurir.

@@ .procedures[4].steps[1][0]
- Pantau kas masuk dari klien setiap hari lewat KlikBCA Bisnis.
+ Pantau kas masuk dari klien setiap hari melalui KlikBCA Bisnis.

@@ .flow.nodes.n
- Finance Staff mengirim invoice ke klien / (PDF lewat email; cetak bila PKS mensyaratkan)
+ Finance Staff mengirim invoice ke klien / (PDF melalui email; cetak bila PKS mensyaratkan)

@@ .sla[0][0]
- Pemantauan kas masuk lewat KlikBCA Bisnis
+ Pemantauan kas masuk melalui KlikBCA Bisnis

@@ .exceptions[1][1]
- Finance Staff menerbitkan Surat Pembatalan atau Revisi Invoice dan Faktur Pajak Pengganti lewat CoreTax DJP setelah Finance Lead menyetujui, lalu mencatat alasan dan bukti persetujuan (butir 4.9) serta riwayatnya di log ketidaksesuaian (butir 4.14).
+ Finance Staff menerbitkan Surat Pembatalan atau Revisi Invoice dan Faktur Pajak Pengganti melalui CoreTax DJP setelah Finance Lead menyetujui, lalu mencatat alasan dan bukti persetujuan (butir 4.9) serta riwayatnya di log ketidaksesuaian (butir 4.14).

@@ .exceptions[3][1]
- Finance Staff meneruskan pemantauan sesuai SOP Account Receivable & Collection. SOP itu sedang dalam peninjauan dan berada di luar scope SOP ini.
+ Finance Staff meneruskan pemantauan sesuai SOP Account Receivable & Collection. SOP itu sedang dalam review dan berada di luar scope SOP ini.

@@ .conclusion[0]
- Finance Lead, pemilik SOP ini, memantau kepatuhan terhadap SOP ini lewat Register Penagihan dan Penjualan dan log ketidaksesuaian.
+ Finance Lead, pemilik SOP ini, memantau kepatuhan terhadap SOP ini melalui Register Penagihan dan Penjualan dan log ketidaksesuaian.

@@ .related_documents[3][1]
- SOP Account Receivable & Collection; sedang dalam peninjauan; mengatur penagihan invoice kepada klien dan pendataan piutang, termasuk tindak lanjut Overdue.
+ SOP Account Receivable & Collection; sedang dalam review; mengatur penagihan invoice kepada klien dan pendataan piutang, termasuk tindak lanjut Overdue.

@@ .iso_refs.ISO/IEC 27001:2022
- Annex A 5.12 (Klasifikasi informasi), untuk butir 4.10; Annex A 5.15 (Kontrol akses), untuk pembatasan akses di butir 4.10; Annex A 5.33 (Perlindungan rekaman), untuk butir 4.10 dan 4.12; Annex A 8.5 (Autentikasi aman), untuk 2FA di butir 4.11.
+ Annex A 5.12 (Klasifikasi informasi), untuk butir 4.10; Annex A 5.15 (Kontrol akses), untuk pembatasan akses di butir 4.10; Annex A 5.33 (Perlindungan record), untuk butir 4.10 dan 4.12; Annex A 8.5 (Autentikasi aman), untuk 2FA di butir 4.11.
```

```diff
# Diff skrip istilah W10 (STYLE-v23 §1.5 dan §2.5), HR-SOP-13: 19 teks berubah. Basis bed1bb6.

@@ .purpose[1]
- Hasil yang dijaga: setiap mutasi punya kebutuhan organisasi yang tertulis dan baru berlaku sesudah keputusan tertulis.
+ Hasil yang dijaga: setiap mutasi punya kebutuhan organisasi yang tertulis dan baru berlaku setelah keputusan tertulis.

@@ .scope[2]
- Batas rotasi dan mutasi: perpindahan sementara untuk penyegaran atau pengembangan keterampilan, dalam unit kerja dan tingkatan jabatan yang sama, dengan karyawan kembali ke tugas semula sesudah masa rotasi, adalah rotasi (SNX-HR-SOP-12). Perpindahan menetap karena kebutuhan organisasi ke unit kerja, sub divisi Operation (NOC, SOC, serta SD dan PM), atau lokasi operasional lain adalah mutasi (SNX-HR-SOP-13) (USULAN).
+ Batas rotasi dan mutasi: perpindahan sementara untuk penyegaran atau pengembangan keterampilan, dalam unit kerja dan tingkatan jabatan yang sama, dengan karyawan kembali ke tugas semula setelah masa rotasi, adalah rotasi (SNX-HR-SOP-12). Perpindahan menetap karena kebutuhan organisasi ke unit kerja, sub divisi Operation (NOC, SOC, serta SD dan PM), atau lokasi operasional lain adalah mutasi (SNX-HR-SOP-13) (USULAN).

@@ .definitions[8][1]
- Jabatan di SNX-HR-ORG-01 yang dipegang karyawan sesudah mutasi.
+ Jabatan di SNX-HR-ORG-01 yang dipegang karyawan setelah mutasi.

@@ .policy[2]
- 4.3 Pemisahan peran (ISO 9001:2015 5.3): jabatan yang mengusulkan, menanggapi, menyimpulkan kualifikasi, menetapkan keputusan, dan mencatat mutasi berbeda satu sama lain; pembagiannya ada di bagian 5. Bila Atasan Langsung Tujuan dan Atasan Langsung Asal adalah jabatan yang sama, Penanggap alternatif menanggapi usulan menurut bagian 9 (USULAN). Pengecualian: bila Direktur Utama adalah Atasan Langsung Tujuan, Direktur Utama mengusulkan sekaligus memutuskan, dan bila ia juga Atasan Langsung Asal, ia menanggapi sendiri. Pemeriksa yang terpisah dari Direktur Utama adalah HR Lead, lewat kesimpulan kualifikasi dan rekomendasi di butir 6.2 dan 6.3 (USULAN).
+ 4.3 Pemisahan peran (ISO 9001:2015 5.3): jabatan yang mengusulkan, menanggapi, menyimpulkan kualifikasi, menetapkan keputusan, dan mencatat mutasi berbeda satu sama lain; pembagiannya ada di bagian 5. Bila Atasan Langsung Tujuan dan Atasan Langsung Asal adalah jabatan yang sama, Penanggap alternatif menanggapi usulan menurut bagian 9 (USULAN). Pengecualian: bila Direktur Utama adalah Atasan Langsung Tujuan, Direktur Utama mengusulkan sekaligus memutuskan, dan bila ia juga Atasan Langsung Asal, ia menanggapi sendiri. Pemeriksa yang terpisah dari Direktur Utama adalah HR Lead, melalui kesimpulan kualifikasi dan rekomendasi di butir 6.2 dan 6.3 (USULAN).

@@ .policy[3]
- 4.4 Kualifikasi (ISO 9001:2015 7.2): HR Lead menyimpulkan kualifikasi karyawan terhadap persyaratan jabatan tujuan di SNX-HR-JA-01 dan mencatat kesenjangan kompetensi beserta tindakannya. SNX-HR-JA-01 butir 4.7 menyatakan masa pengalaman minimum ditentukan sesudah job evaluation. Sampai masa itu ditetapkan, HR Lead menyimpulkan pengalaman dari persyaratan pendidikan dan pengalaman jabatan tujuan dan menulis alasannya (USULAN).
+ 4.4 Kualifikasi (ISO 9001:2015 7.2): HR Lead menyimpulkan kualifikasi karyawan terhadap persyaratan jabatan tujuan di SNX-HR-JA-01 dan mencatat kesenjangan kompetensi beserta tindakannya. SNX-HR-JA-01 butir 4.7 menyatakan masa pengalaman minimum ditentukan setelah job evaluation. Sampai masa itu ditetapkan, HR Lead menyimpulkan pengalaman dari persyaratan pendidikan dan pengalaman jabatan tujuan dan menulis alasannya (USULAN).

@@ .policy[5]
- 4.6 Persetujuan tertulis (ISO 9001:2015 5.3): SNX-HR-JA-01 butir 4.5 menyatakan keputusan pengangkatan atau pemutusan hubungan kerja mengikuti delegasi dan persetujuan tertulis yang berlaku. Mutasi mengikuti ketentuan yang sama: berlaku hanya sesudah keputusan tertulis Direktur Utama (USULAN).
+ 4.6 Persetujuan tertulis (ISO 9001:2015 5.3): SNX-HR-JA-01 butir 4.5 menyatakan keputusan pengangkatan atau pemutusan hubungan kerja mengikuti delegasi dan persetujuan tertulis yang berlaku. Mutasi mengikuti ketentuan yang sama: berlaku hanya setelah keputusan tertulis Direktur Utama (USULAN).

@@ .policy[8]
- 4.9 Hak akses (ISO/IEC 27001:2022 Annex A 5.18 dan 6.5): SNX-ISMS-SOP-02 mengatur perubahan akses saat mutasi, yaitu perpindahan peran seseorang: pencabutan hak akses lama yang tidak relevan paling lambat 5 hari kerja sesudah mutasi, dan pengajuan hak akses baru. Mutasi dalam SOP ini termasuk di dalamnya, dan Atasan Langsung Tujuan mengajukan hak akses baru (butir 6.4).
+ 4.9 Hak akses (ISO/IEC 27001:2022 Annex A 5.18 dan 6.5): SNX-ISMS-SOP-02 mengatur perubahan akses saat mutasi, yaitu perpindahan peran seseorang: pencabutan hak akses lama yang tidak relevan paling lambat 5 hari kerja setelah mutasi, dan pengajuan hak akses baru. Mutasi dalam SOP ini termasuk di dalamnya, dan Atasan Langsung Tujuan mengajukan hak akses baru (butir 6.4).

@@ .policy[9]
- 4.10 Garis lapor dan dokumen organisasi (ISO 9001:2015 5.3): SNX-HR-JA-01 butir 4.3 menyatakan garis lapor berlabel menunggu konfirmasi belum resmi. Bila jabatan atau garis lapor karyawan berubah, HR Lead memperbarui SNX-HR-ORG-01 dan SNX-HR-JA-01 lewat revisi (butir 6.4).
+ 4.10 Garis lapor dan dokumen organisasi (ISO 9001:2015 5.3): SNX-HR-JA-01 butir 4.3 menyatakan garis lapor berlabel menunggu konfirmasi belum resmi. Bila jabatan atau garis lapor karyawan berubah, HR Lead memperbarui SNX-HR-ORG-01 dan SNX-HR-JA-01 melalui revisi (butir 6.4).

@@ .policy[10]
- 4.11 Rekaman dan klasifikasi (ISO 9001:2015 7.5.3): HRGA Officer mengarsipkan rekaman mutasi di personal file karyawan (butir 6.4). Rekaman itu berisi data karyawan dan berklasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 (USULAN). Lokasi, pemilik, dan retensi ada di tabel bagian 11.
+ 4.11 Record dan klasifikasi (ISO 9001:2015 7.5.3): HRGA Officer mengarsipkan record mutasi di personal file karyawan (butir 6.4). Record itu berisi data karyawan dan berklasifikasi RESTRICTED (Internal) menurut SNX-ISMS-PRO-01 (USULAN). Lokasi, pemilik, dan retensi ada di tabel bagian 11.

@@ .roles[1][1]
- Memeriksa kelengkapan usulan, meneruskannya ke Atasan Langsung Asal, memberikan informasi jabatan baru kepada karyawan, memperbarui data kepegawaian, mengarsipkan rekaman di personal file, dan memberi tahu Atasan Langsung Tujuan tentang mutasi (butir 6.2 dan 6.4).
+ Memeriksa kelengkapan usulan, meneruskannya ke Atasan Langsung Asal, memberikan informasi jabatan baru kepada karyawan, memperbarui data kepegawaian, mengarsipkan record di personal file, dan memberi tahu Atasan Langsung Tujuan tentang mutasi (butir 6.2 dan 6.4).

@@ .procedures[3].intro[0]
- Langkah berikut berjalan sesudah keputusan menyetujui. Untuk keputusan menolak, lihat bagian 9.
+ Langkah berikut berjalan setelah keputusan menyetujui. Untuk keputusan menolak, lihat bagian 9.

@@ .procedures[3].steps[6][2]
- Tiket perubahan akses di Service Hub (GLPI)
+ Ticket perubahan akses di Service Hub (GLPI)

@@ .procedures[3].steps[7][0]
- Perbarui pemegang jabatan dan garis lapor di SNX-HR-ORG-01 dan SNX-HR-JA-01 lewat revisi kedua dokumen, bila jabatan atau garis lapor berubah.
+ Perbarui pemegang jabatan dan garis lapor di SNX-HR-ORG-01 dan SNX-HR-JA-01 melalui revisi kedua dokumen, bila jabatan atau garis lapor berubah.

@@ .sla[8][2]
- 1 hari kerja sesudah pemberitahuan mutasi diterima, agar batas pencabutan 5 hari kerja di SNX-ISMS-SOP-02 tercapai (USULAN)
+ 1 hari kerja setelah pemberitahuan mutasi diterima, agar batas pencabutan 5 hari kerja di SNX-ISMS-SOP-02 tercapai (USULAN)

@@ .exceptions[1][1]
- HR Lead menambahkan jabatan itu lewat revisi kedua dokumen (USULAN). HRGA Officer melanjutkan proses usulan setelah Direktur Utama mengesahkan revisi itu (USULAN).
+ HR Lead menambahkan jabatan itu melalui revisi kedua dokumen (USULAN). HRGA Officer melanjutkan proses usulan setelah Direktur Utama mengesahkan revisi itu (USULAN).

@@ .exceptions[7][1]
- HR Lead mencatat tindakan pemenuhan syarat dan melapor ke Direktur Utama saat syarat terpenuhi (USULAN). HRGA Officer memperbarui data kepegawaian sesudah laporan itu (USULAN).
+ HR Lead mencatat tindakan pemenuhan syarat dan melapor ke Direktur Utama saat syarat terpenuhi (USULAN). HRGA Officer memperbarui data kepegawaian setelah laporan itu (USULAN).

@@ .conclusion[0]
- HR Lead selaku pemilik SOP memeriksa kepatuhan terhadap SOP ini dengan membandingkan rekaman di bagian 11 dengan langkah di bagian 6 dan batas waktu di bagian 8 (USULAN).
+ HR Lead selaku pemilik SOP memeriksa kepatuhan terhadap SOP ini dengan membandingkan record di bagian 11 dengan langkah di bagian 6 dan batas waktu di bagian 8 (USULAN).

@@ .related_documents[6][1]
- Information Classification & Handling Procedure: tingkat klasifikasi rekaman mutasi (butir 4.11).
+ Information Classification & Handling Procedure: tingkat klasifikasi record mutasi (butir 4.11).

@@ .records[4][0]
- Tiket perubahan akses karena mutasi
+ Ticket perubahan akses karena mutasi
```

