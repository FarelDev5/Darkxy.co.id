domain="$1" # Mengambil domain sebagai argumen dari baris perintah

# Memeriksa apakah domain diberikan
if [ -z "$domain" ]; then
  echo "Harap berikan domain sebagai argumen."
  exit 1
fi

# Memeriksa koneksi internet (opsional, tetapi direkomendasikan)
if ! ping -c 1 "$domain" > /dev/null 2>&1; then
  echo "Tidak dapat menghubungi domain: $domain"
  exit 1
fi

# Menjalankan nmap dengan script dns-brute
nmap -p 80 --script dns-brute.nse "$domain"

# Menjalankan wget dengan opsi verbose
wget -S "$domain"

echo "Pemindaian dan pengunduhan selesai."