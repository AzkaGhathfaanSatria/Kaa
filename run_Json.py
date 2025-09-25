import pandas as pd
import json

# Nama file JSON yang kamu punya
file_json = "Azka Ghathfaan Satria_V3925021_Kelas B.json"
# Nama file Excel hasil
file_excel = "output_tabel.xlsx"

# Baca file JSON
with open(file_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Ambil root objek
aplikasi = data["aplikasi_pemantau_pemerintahan"]

# Ubah setiap bagian menjadi DataFrame
df_anggota = pd.DataFrame(aplikasi["Anggota_DPR_Situs_Resmi_DPR"])
df_pengeluaran = pd.DataFrame(aplikasi["Pengeluaran_Projek_Portal_Data_Indonesia"])
df_jadwal = pd.DataFrame(aplikasi["Jadwal_Rapat_Situs_Resmi_DPR_RI"])
df_pemilu = pd.DataFrame(aplikasi["Data_Pemilu_KPU"])

# ====== Tampilkan di Terminal ======
print("=== Anggota DPR ===")
print(df_anggota.to_string(index=False))
print("\n=== Pengeluaran Projek ===")
print(df_pengeluaran.to_string(index=False))
print("\n=== Jadwal Rapat ===")
print(df_jadwal.to_string(index=False))
print("\n=== Data Pemilu ===")
print(df_pemilu.to_string(index=False))

# ====== Simpan ke Excel ======
with pd.ExcelWriter(file_excel) as writer:
    df_anggota.to_excel(writer, sheet_name="Anggota DPR", index=False)
    df_pengeluaran.to_excel(writer, sheet_name="Pengeluaran Projek", index=False)
    df_jadwal.to_excel(writer, sheet_name="Jadwal Rapat", index=False)
    df_pemilu.to_excel(writer, sheet_name="Data Pemilu", index=False)

print(f"\n✅ Data berhasil disimpan ke file: {file_excel}")
