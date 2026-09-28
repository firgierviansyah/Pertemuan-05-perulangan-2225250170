# =====================================
# Latihan 4 - Menghitung Bilangan Genap
# Input  : Bilangan bulat positif n
# Proses : Menghitung banyak bilangan genap
# Output : Jumlah bilangan genap dari 1 sampai n
# =====================================

print("=" * 45)
print("     PENGHITUNG BILANGAN GENAP")
print("=" * 45)

n = int(input("Masukkan nilai n: "))

jumlah_genap = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print("-" * 45)
print(f"Banyak bilangan genap dari 1 sampai {n}")
print(f"= {jumlah_genap}")
print("=" * 45)