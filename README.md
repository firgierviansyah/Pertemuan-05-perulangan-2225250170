# Pertemuan 05 - Perulangan Python

## Identitas Mahasiswa

- Nama : FIRGI ERVIANSYAH
- NIM : 2225250170
- Kelas : 3B

---

## Tujuan

Mempelajari dan menerapkan penggunaan perulangan `for` dan `while` dalam Python untuk menyelesaikan masalah iteratif, melakukan validasi input, menghitung akumulasi data, serta mengelola hasil pekerjaan menggunakan Git dan GitHub. [1]

---

## Struktur Proyek

```text
pertemuan-05-perulangan-NIM/
│
├── README.md
├── .gitignore
├── kuis.docx
│
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│
└── kuis/
    └── kuis2_deret_aritmetika.py
```

---

## Cara Menjalankan Program

### Latihan 1

```bash
python latihan/01_tabel_perkalian.py
```

### Latihan 2

```bash
python latihan/02_jumlah_bilangan.py
```

### Latihan 3

```bash
python latihan/03_validasi_input.py
```

### Latihan 4

```bash
python latihan/04_hitung_genap.py
```

### Kuis 2

```bash
python kuis/kuis2_deret_aritmetika.py
```

---

## Algoritma Kuis 2 (Deret Aritmetika)

1. Meminta input suku pertama (`a`).
2. Meminta input beda (`d`).
3. Meminta input banyak suku (`n`).
4. Melakukan validasi menggunakan `while` hingga nilai `n` lebih dari 0.
5. Membuat variabel `total` dengan nilai awal 0.
6. Menggunakan perulangan `for` sebanyak `n` kali.
7. Menghitung nilai setiap suku dengan rumus:

   ```
   suku = a + (i × d)
   ```

8. Menampilkan setiap suku yang dihasilkan.
9. Menambahkan nilai suku ke variabel `total`.
10. Setelah perulangan selesai, menampilkan jumlah seluruh suku. 

---

## Hasil Pengujian

### Test Case 1

Input:

```text
a = 2
d = 3
n = 5
```

Output yang Diharapkan:

```text
2, 5, 8, 11, 14
Jumlah = 40
```

Output Aktual:

```text
2.00, 5.00, 8.00, 11.00, 14.00
Jumlah = 40.00
```

Status:

✅ Berhasil

---

### Test Case 2

Input:

```text
a = 10
d = -2
n = 4
```

Output yang Diharapkan:

```text
10, 8, 6, 4
Jumlah = 28
```

Output Aktual:

```text
10.00, 8.00, 6.00, 4.00
Jumlah = 28.00
```

Status:

✅ Berhasil

---

### Test Case 3

Input:

```text
a = 1.5
d = 0.5
n = 3
```

Output yang Diharapkan:

```text
1.5, 2.0, 2.5
Jumlah = 6.0
```

Output Aktual:

```text
1.50, 2.00, 2.50
Jumlah = 6.00
```

Status:

✅ Berhasil

---

## Refleksi

Pada pertemuan ini saya mempelajari perbedaan penggunaan perulangan `for` dan `while`. Saya memahami bahwa `for` lebih cocok digunakan ketika jumlah iterasi sudah diketahui, sedangkan `while` digunakan ketika perulangan bergantung pada suatu kondisi. 

Kesalahan yang sempat ditemukan adalah penggunaan batas perulangan yang kurang tepat sehingga jumlah iterasi tidak sesuai dengan yang diharapkan. Kesalahan tersebut diperbaiki dengan memeriksa kembali nilai awal, kondisi berhenti, dan perubahan variabel pada setiap iterasi. 

Melalui latihan dan kuis, saya menjadi lebih memahami konsep validasi input, akumulasi data, serta pentingnya melakukan pengujian menggunakan beberapa test case sebelum program diunggah ke GitHub.
