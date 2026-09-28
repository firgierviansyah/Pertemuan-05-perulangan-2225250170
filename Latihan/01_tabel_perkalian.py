# Latihan 1 - Tabel Perkalian
# Input   : satu bilangan bulat n
# Proses  : menggunakan for untuk menghitung n x 1 sampai n x 10
# Berhenti: setelah perulangan berjalan 10 kali
# Output  : tabel perkalian dari n x 1 sampai n x 10

print("=" * 30)
print("       TABEL PERKALIAN")
print("=" * 30)

n = int(input("Masukkan bilangan: "))

print(f"\nTabel perkalian {n}")
print("-" * 30)

for i in range(1, 11):
    hasil = n * i
    print(f"{n:>3} x {i:<2} = {hasil}")

print("-" * 30)
print("Perulangan selesai.")