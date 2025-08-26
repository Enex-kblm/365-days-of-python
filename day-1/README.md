# SPLDV (Sistem Persamaan Linear Dua Variabel) Solver & Plotter

Program Python untuk menyelesaikan dan memvisualisasikan Sistem Persamaan Linear Dua Variabel (SPLDV) dengan grafik interaktif.

## Deskripsi

Program ini dapat:
- Memparse dan menganalisis dua persamaan linear dengan dua variabel
- Menggambar grafik kedua persamaan pada koordinat kartesius
- Mencari dan menampilkan titik potong (solusi) dari kedua persamaan
- Menyimpan hasil visualisasi sebagai file gambar PNG

## Fitur Utama

### 🔍 Parsing Persamaan Otomatis
- Mendeteksi variabel secara otomatis dari persamaan
- Mendukung berbagai format penulisan persamaan
- Menangani koefisien positif, negatif, dan implisit

### 📊 Visualisasi Grafik
- Plot kedua garis persamaan dengan warna berbeda
- Menampilkan titik potong dengan marker merah
- Grid dan sumbu koordinat untuk kemudahan pembacaan
- Legend untuk identifikasi persamaan

### 💾 Export Hasil
- Menyimpan grafik dalam format PNG resolusi tinggi (300 DPI)
- Nama file default: `spldv.png`

## Requirements

```bash
pip install numpy matplotlib
```

## Cara Penggunaan

1. Jalankan program:
```bash
python grafik.py
```

2. Masukkan persamaan pertama ketika diminta:
```
Masukkan persamaan 1: 2x + 3y = 6
```

3. Masukkan persamaan kedua:
```
Masukkan persamaan 2: x - y = 1
```

4. Program akan menampilkan grafik dan menyimpan sebagai `spldv.png`

## Format Persamaan yang Didukung

Program mendukung berbagai format penulisan persamaan:

- `2x + 3y = 6`
- `x - 2y = 4`
- `-x + y = 3`
- `3x - y = -2`
- `x + y = 0`

**Catatan:** 
- Gunakan variabel huruf (a-z, A-Z)
- Program secara otomatis mendeteksi 2 variabel pertama yang ditemukan
- Spasi akan diabaikan dalam parsing

## Contoh Output

![Contoh Grafik SPLDV](day-1/spldv.png)

Grafik menampilkan:
- **Garis biru**: Persamaan pertama
- **Garis orange**: Persamaan kedua  
- **Titik merah**: Solusi/titik potong dengan koordinat
- **Grid**: Untuk memudahkan pembacaan nilai
- **Legend**: Label untuk setiap persamaan

## Struktur Kode

### Fungsi `parse_equation(eq, var1, var2)`
Memparse string persamaan dan mengekstrak koefisien:
- **Input**: String persamaan dan nama dua variabel
- **Output**: Koefisien a, b, dan konstanta c untuk format ax + by = c

### Fungsi `plot_spldv(eq1, eq2)`
Fungsi utama untuk plotting dan penyelesaian:
- Memparse kedua persamaan
- Membuat plot garis untuk setiap persamaan  
- Menghitung titik potong menggunakan eliminasi matriks
- Menampilkan dan menyimpan grafik

## Penanganan Error

Program menangani berbagai kondisi error:

1. **Variabel tidak cukup**: 
   ```
   Harus ada 2 variabel berbeda!
   ```

2. **Sistem tidak memiliki solusi unik**:
   ```
   Persamaan tidak punya solusi unik (paralel atau sama).
   ```

## Pengembangan Lebih Lanjut

Ide untuk pengembangan:
- [ ] Dukungan sistem dengan lebih dari 2 variabel
- [ ] Mode batch untuk multiple sistem persamaan
- [ ] Export dalam format lain (SVG, PDF)
- [ ] GUI interface
- [ ] Animasi proses penyelesaian

## Kontribusi

Kontribusi selalu diterima! Silakan buat pull request atau laporkan issue yang ditemukan.

## Lisensi

Program ini bersifat open source dan dapat digunakan secara bebas untuk tujuan edukasi dan penelitian.
