# ==========================================
# Kuis 2 - Deret Aritmetika
# Input  : a, d, n
# Proses : Menampilkan n suku deret aritmetika
#          dan menghitung jumlahnya
# Output : Daftar suku dan total deret
# ==========================================

print("=" * 50)
print("           DERET ARITMETIKA")
print("=" * 50)

a = float(input("Suku pertama (a) : "))
d = float(input("Beda (d)         : "))
n = int(input("Banyak suku (n)  : "))

while n <= 0:
    print("❌ n harus bilangan bulat positif!")
    n = int(input("Masukkan kembali n: "))

print("\nDaftar Suku Deret")
print("-" * 50)

total = 0

for i in range(n):
    suku = a + (i * d)
    total += suku

    print(f"Suku ke-{i + 1:>2} = {suku:.2f}")

print("-" * 50)
print(f"Jumlah deret = {total:.2f}")
print("=" * 50)