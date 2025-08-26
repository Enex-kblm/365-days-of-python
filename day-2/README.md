# GitHub Repository Storyteller 📖

Program Python yang mengubah riwayat commit repository GitHub menjadi cerita naratif yang indah dan bermakna.

## Deskripsi

Repository Storyteller adalah tool unik yang menganalisis commit history dari repository GitHub dan menyajikannya dalam bentuk cerita yang menarik. Program ini menggunakan GitHub API untuk mengambil data commit dan mengubahnya menjadi narasi yang menggambarkan perjalanan development sebuah project.

## Fitur Utama

### 🎨 ASCII Art Banner
- Menggunakan `pyfiglet` untuk membuat banner ASCII yang menarik
- Memberikan sentuhan visual yang memukau pada output

### 📊 Analisis Commit History
- Mengambil hingga 100 commit terakhir dari repository
- Menganalisis tanggal commit pertama dan terakhir
- Menghitung kontribusi setiap developer
- Mengidentifikasi kontributor paling aktif

### 📝 Storytelling Naratif
- Mengubah data teknis menjadi cerita yang mudah dipahami
- Menggunakan bahasa Indonesia yang puitis dan bermakna
- Menyajikan timeline development dalam format yang engaging

### 💾 Export ke File
- Menyimpan cerita dalam file `repo_story.txt`
- Format UTF-8 untuk mendukung karakter Indonesia

## Requirements

```bash
pip install requests pyfiglet
```

## Cara Penggunaan

1. Jalankan program:
```bash
python repo_storyteller.py
```

2. Masukkan URL repository GitHub ketika diminta:
```
Masukkan URL repo GitHub: https://github.com/username/repository-name
```

3. Program akan menampilkan cerita dan menyimpan ke file `repo_story.txt`

## Format URL yang Didukung

Program mendukung berbagai format URL GitHub:

- `https://github.com/owner/repo`
- `https://github.com/owner/repo/`
- `https://github.com/owner/repo.git`

## Contoh Output
```
 ____                    ____  _                   _       _ _           
|  _ \ ___ _ __   ___   / ___|| |_ ___  _ __ _   _| |_ ___| | | ___ _ __ 
| |_) / _ \ '_ \ / _ \  \___ \| __/ _ \| '__| | | | __/ _ \ | |/ _ \ '__|
|  _ <  __/ |_) | (_) |  ___) | || (_) | |  | |_| | ||  __/ | |  __/ |   
|_| \_\___| .__/ \___/  |____/ \__\___/|_|   \__, |\__\___|_|_|\___|_|   
          |_|                                |___/                       

📖 Sebuah Perjalanan: Enex-kblm/365-days-of-python

🌱 Pada 26 August 2025, lahirlah sebuah gagasan.
   Enex-kblm menorehkan baris kode pertama,
   seperti seorang penulis yang menulis kata pembuka dalam sebuah buku.
   Dari sinilah cerita repository ini dimulai.

⏳ Waktu berjalan, commit demi commit hadir.
   Setiap perubahan adalah sebuah bab baru,
   penuh dengan ide, perbaikan, dan semangat untuk tumbuh.

⚡ Hingga akhirnya pada 26 August 2025,
   tercatat sebuah commit terbaru yang berbicara lantang:
   → "Create repo_storyteller.py"
   Seolah menjadi tanda bahwa perjalanan ini belum berakhir,
   melainkan sedang menuju ke arah yang lebih besar.

👑 Dari semua tokoh yang hadir dalam kisah ini,
   sosok paling gigih adalah Enex-kblm,
   dengan 5 kontribusi berharga
   dari total 5 jejak langkah terakhir.

🚀 Maka, repository ini bukan hanya sekumpulan kode.
   Ia adalah saksi perjalanan, wujud ide yang hidup,
   dan bukti bahwa setiap developer meninggalkan cerita
   melalui baris demi baris yang mereka tuliskan.

✨ Dan seperti semua kisah hebat,
   365-days-of-python masih terus menulis bab berikutnya...
```

## Struktur Kode

### Fungsi `get_repo_story(repo_url: str)`
Fungsi utama yang menganalisis repository dan menghasilkan cerita:

**Input**: URL repository GitHub
**Output**: String berisi cerita naratif

**Proses:**
1. **Parsing URL**: Mengekstrak owner dan nama repository
2. **API Call**: Mengambil data commit dari GitHub API
3. **Data Analysis**: Menganalisis commit history dan kontributor
4. **Story Generation**: Mengubah data menjadi narasi yang menarik

### Komponen Cerita

1. **Banner ASCII**: Header visual menggunakan pyfiglet
2. **Pembukaan**: Informasi commit pertama dan pencetus ide
3. **Perjalanan**: Deskripsi proses development
4. **Commit Terbaru**: Highlight commit terakhir
5. **Top Contributor**: Penghargaan untuk kontributor paling aktif
6. **Penutup**: Refleksi filosofis tentang makna repository

## Penanganan Error

Program menangani berbagai kondisi error:

1. **Repository tidak ditemukan**:
   ```
   ❌ Gagal ambil data repo: Not Found
   ```

2. **Repository kosong**:
   ```
   ❌ Tidak ada commit ditemukan.
   ```

3. **API Rate Limit**: Program akan menampilkan pesan error dari GitHub API

## Contoh Penggunaan

```python
# Contoh manual call
story = get_repo_story("https://github.com/microsoft/vscode")
print(story)

# Output akan disimpan ke repo_story.txt
```

## Batasan

- Mengambil maksimal 100 commit terakhir (limitasi GitHub API)
- Memerlukan koneksi internet untuk mengakses GitHub API
- Repository private memerlukan authentication token

## Pengembangan Lebih Lanjut

Ide untuk pengembangan:
- [ ] Support untuk GitHub authentication token
- [ ] Analisis lebih mendalam (file changes, lines of code)
- [ ] Multiple output format (HTML, Markdown)
- [ ] Visualisasi timeline dengan grafik
- [ ] Support untuk GitLab dan Bitbucket
- [ ] Template cerita yang dapat dikustomisasi

## Inspirasi

Program ini terinspirasi dari ide bahwa setiap repository memiliki cerita unik di balik kode-kodenya. Setiap commit adalah jejak perjalanan developer, dan setiap repository adalah bukti dedikasi dan kreativitas dalam dunia programming.

## Kontribusi

Kontribusi selalu diterima! Silakan:
1. Fork repository ini
2. Buat branch untuk fitur baru
3. Commit perubahan Anda
4. Push ke branch
5. Buat Pull Request

## Lisensi

Program ini bersifat open source dan dapat digunakan secara bebas untuk tujuan edukasi dan pengembangan.

---

*"Setiap baris kode adalah sebuah cerita, setiap commit adalah sebuah bab, dan setiap repository adalah sebuah buku yang menunggu untuk dibaca."*
