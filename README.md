# Darkxy Tool

## Deskripsi
**Darkxy** adalah tools untuk mengubah tampilan Termux agar menyerupai terminal Linux, dilengkapi dengan berbagai fitur tambahan. Darkxy tidak hanya memodifikasi tampilan, tetapi juga menyediakan fitur khusus seperti informasi IP, koneksi DNS, dan lainnya, yang membantu pengguna dalam aktivitas terminal di Termux.

## Fitur Utama
- **Kustomisasi Tampilan**: Menyesuaikan tampilan Termux agar lebih mirip terminal Linux.
- **Informasi Jaringan**: Menampilkan informasi IP dan koneksi DNS.
- **Kompatibilitas Perintah**: Mendukung perintah-perintah dasar Termux dan Linux.
- **Penginstalan Paket**: Mudah menginstal berbagai paket yang diperlukan untuk pengoperasian Termux.
- **Fitur Tambahan**: Fitur tambahan yang dirancang untuk meningkatkan pengalaman pengguna di Termux.

## Persyaratan
Pastikan Anda memiliki **Python 3** yang sudah terinstal di Termux.

## Instalasi
Ikuti langkah-langkah berikut untuk menginstal **Darkxy** beserta semua bahan yang dibutuhkan:

1. **Perbarui Paket dan Install Git**
   ```bash
   pkg update && pkg upgrade
   pkg install git -y
   ```

2. **Clone Repository Darkxy**
   Clone repositori Darkxy dari GitHub:
   ```bash
   git clone https://github.com/FarelDev5/Darkxy
   ```

3. **Masuk ke Direktori Darkxy**
   Pindah ke direktori `Darkxy`:
   ```bash
   cd Darkxy
   ```

4. **Instal Semua Bahan yang Dibutuhkan**
   Tools Darkxy mungkin memerlukan beberapa paket tambahan agar berfungsi dengan baik. Instal semua bahan yang diperlukan dengan menjalankan:
   ```bash
   bash install.sh
   ```
   
   ```bash
   pip install requests
   ```

5. **Jalankan Script**
   Setelah semua bahan terpasang, Anda dapat menjalankan tools dengan perintah:
   ```bash
   python3 main.py
   ```

## Cara Penggunaan
Setelah `main.py` dijalankan, Anda bisa mulai menggunakan perintah-perintah di tools ini dengan format:
```
Darkxy/cmd: <perintah_anda>
```

Contoh:
```bash
Darkxy/cmd: ls
```

Anda juga dapat mengakses fitur tambahan yang telah disediakan oleh Darkxy untuk menampilkan informasi jaringan atau menjalankan perintah lainnya.

## Catatan
- **Darkxy** dirancang untuk bekerja optimal di Termux dengan tampilan menyerupai terminal Linux.
- Pastikan semua paket terpasang dengan benar untuk menghindari error.

## Kontribusi
Jika Anda ingin berkontribusi, silakan buat *pull request* atau buka *issue* di [GitHub Repository](https://github.com/FarelDev5)

---

Dikembangkan oleh Farel Alfareza.

## ⚠ DISCLAIMER ⚠

Gunakan dengan bijak.
tools ini di gunakan untuk belajar
saya tidak bertanggung jawab jika di salah gunakan
semua tergantung dari bagaimana cara kamu menggunakan tools ini
