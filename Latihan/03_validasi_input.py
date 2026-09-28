# =====================================
# Latihan 3 - Validasi Input Nilai
# Input  : Nilai ujian (0 - 100)
# Proses : Validasi menggunakan while
# Output : Nilai yang telah valid
# =====================================

print("=" * 45)
print("      VALIDASI NILAI UJIAN")
print("=" * 45)

nilai = float(input("Masukkan nilai (0 - 100): "))

while nilai < 0 or nilai > 100:
    print("❌ Nilai tidak valid!")
    print("   Nilai harus berada pada rentang 0 sampai 100.\n")
    
    nilai = float(input("Masukkan kembali nilai: "))

print("\n✅ Nilai diterima.")
print(f"Nilai yang dimasukkan: {nilai}")
print("=" * 45)