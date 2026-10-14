# Uji regresi pola lint: kalimat sah harus lolos, kalimat terlarang harus ditembak. Dipanggil selftest baris 6.
import importlib.util, re, sys
spec = importlib.util.spec_from_file_location('lint', sys.argv[1]); L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
def hits(t):
    out = []
    for pat, why in L.FORBIDDEN:
        if re.search(pat, t, flags=re.I if 'password' in pat else 0): out.append(why)
    for pat, why in L.STYLE:
        if re.search(pat, t, flags=re.I): out.append(why)
    if re.search(L.DUMMY, t, flags=re.I): out.append('dummy')
    return out
lolos = ["Perubahan diuji di lingkungan staging sebelum ke production.", "Kebijakan password: minimal 12 karakter, unik per sistem.",
 "Tingkat SECRET: hanya Direksi dan pemilik informasi.", "Berita Acara Handover ditandatangani kedua pihak.", "SOP SALES-TO-OPERATIONS HANDOVER",
 "☐ Ya ☐ Tidak ☑ Selesai ✓", "Kolom Nama Penyusun diisi pemohon.", "Token API disimpan di vault, bukan di dokumen.", "Server staging dipisah dari production.",
 "Klasifikasi SECRET: SNX-ISMS-PRO-01 bagian 4.", "Langkah 1 \u2794 Langkah 2", "Acuan ISO 9001:2015 klausul 7.5 dan ISO \u00a7 tidak dipakai.", "Tiket Ops dicatat di Zammad, tiket umum di GLPI (SINUX Service Hub)."]
tembak = ["password: P@ssw0rd123", "api_key=AKIA1234ABCD5678", "Dokumen disusun dengan bantuan Claude.", "Selesai ✅", "submit_to_staging packet", "Lihat HANDOVER_W2.md",
 "Nama Penyusun / Jabatan", "Proses ini sangat penting untuk tim.",
 "Lihat (HANDOVER \u00a72).", "Sesuai CORE \u00a713.", "Acuan baseline SINUX_SERVICE_HUB.", "Patuhi CLAIM_CLASS_POLICY.", "Lessons learned disetor melalui jalur staging.", "Packet staging dikirim.", "dibantu claude", "Kata sandi awal: Sinux@2026", "Password admin: Sinux2026!", "Analisa resiko dilakukan.", "Rujuk DEC-2026-123.", "Lihat SKILL_ir-report."]
bad = 0
for t in lolos:
    h = hits(t); print('LOLOS ' if not h else 'SALAH-TEMBAK', repr(t[:50]), h); bad += bool(h)
for t in tembak:
    h = hits(t); print('TEMBAK' if h else 'SALAH-LOLOS ', repr(t[:50]), h); bad += (not h)
print('GAGAL', bad); sys.exit(1 if bad else 0)
