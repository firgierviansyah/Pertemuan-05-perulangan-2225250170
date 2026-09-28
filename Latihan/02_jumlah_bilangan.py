# Latihan 2 - Jumlah 1 sampai n
# Input   : satu bilangan bulat positif n
# Proses  : menjumlahkan bilangan dari 1 sampai n dengan for
# Berhenti: setelah perulangan mencapai n
# Output  : hasil penjumlahan 1 + 2 + ... + n

print("=" * 34)
print("      PENJUMLAHAN 1 SAMPAI n")
print("=" * 34)

n = int(input("Masukkan nilai n: "))

total = 0

for i in range(1, n + 1):
    total += i

print("-" * 34)
print(f"Jumlah bilangan 1 sampai {n} = {total}")
print("-" * 34)
print("Perhitungan selesai.")