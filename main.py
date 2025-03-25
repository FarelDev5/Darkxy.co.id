import os
import time
import random
import subprocess
import requests
import socket
import webbrowser
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from datetime import datetime
import pyfiglet
import re

console = Console()

# Author Information

def author_info():
    print(Panel(
        "[bold white]➥ Makasih ya udh pake tools ini, smoga kalian sehat selalu.[/bold white]\n"
        ))
    print(Panel(
        "[bold yellow]Author : farel alfareza[/bold yellow]\n"
        "[bold cyan]Email : farel.alfareza.dev@gmail.com[/bold cyan]\n"
        "[bold yellow]Tiktok&Instagram : farel.project_5[/bold yellow]",
        title="[bold magenta]About[/bold magenta]", expand=False
        ))
def discalimer():
    print(Panel(
        "[bold green]WELCOME TO DARXY TOOLS[/bold green]\n"
        "[bold cyan]Tools Ini Di buat untuk belajar, saya tidak akan bertanggung jawab atas tindakan anda, menggunakan tools ini.[/bold cyan]\n"
        "[bold yellow]Harap Gunakan Tools Ini Dengan Bijak[/bold yellow]",
        title="[bold magenta]⚠ DISSCLAIMER ⚠[/bold magenta]", expand=False
    ))

# Function to display DARXY logo with gradient effect
def show_logo():
    logo_text = pyfiglet.figlet_format("DARXY TOOL", font="standard")
    gradient_logo = ""
    colors = ["#8A2BE2", "#9370DB", "#BA55D3", "#DA70D6", "#FF69B4"]

    for line in logo_text.splitlines():
        color = colors[0]
        colors = colors[1:] + [colors[0]]  # Rotate colors
        gradient_logo += f"[{color}]{line}[/]\n"

    console.print(Panel(gradient_logo, title="[bold magenta]DARXY[/bold magenta]", expand=False))

# Function to display device information
def device_info():
    device_name = os.popen("getprop ro.product.model").read().strip() or "Unknown Device"
    os_version = os.popen("getprop ro.build.version.release").read().strip() or "Unknown OS"
    termux_version = os.popen("pkg list-installed | grep termux").read().strip() or "Unknown Termux Version"

    table = Table(title="Device Information", title_style="bold magenta")
    table.add_column("Property", style="bold cyan")
    table.add_column("Details", style="bold yellow")
    table.add_row("Device Model", device_name)
    table.add_row("OS Version", os_version)
    table.add_row("Termux Version", termux_version)

    console.print(table)

# Function to ping a website
def ping_website():
    website = input("~ darkxy get #site: ")
    
    try:
        result = subprocess.run(["ping", "-c", "4", website], capture_output=True, text=True, check=True)
        print(Panel(
            f"[bold cyan]Ping Output:[/bold cyan]\n{result.stdout}",
            title="[bold magenta]Ping Website[/bold magenta]", expand=False
        ))
    except subprocess.CalledProcessError as e:
        print(f"[bold red]Error pinging website: {e.stderr}[/bold red]")

# Function to open location in Google Maps
def open_in_maps(lat, lon):
    maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lon}"
    webbrowser.open(maps_url)
    print(f"[bold green]Opening location in Google Maps: {maps_url}[/bold green]")
    
# Function to track IP and open location in Google Maps

def track_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(Panel(
                f"[bold cyan]IP: {ip}[/bold cyan]\n"
                f"[bold green]Location: {data['city']}, {data['regionName']}, {data['country']}[/bold green]\n"
                f"[bold yellow]ISP: {data['isp']}[/bold yellow]\n"
                f"[bold red]Latitude: {data['lat']} | Longitude: {data['lon']}[/bold red]",
                title="[bold magenta]IP Tracker[/bold magenta]", expand=False
            ))
            open_in_maps(data['lat'], data['lon'])  # Directly open in Google Maps
        else:
            print("[bold red]IP tracking failed. Please check the IP address.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# GeoIP Lookup Feature
def geoip_lookup(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        print(Panel(
            f"[bold cyan]IP: {data.get('ip', 'N/A')}[/bold cyan]\n"
            f"[bold green]City: {data.get('city', 'N/A')}[/bold green]\n"
            f"[bold green]Region: {data.get('region', 'N/A')}[/bold green]\n"
            f"[bold green]Country: {data.get('country', 'N/A')}[/bold green]\n"
            f"[bold yellow]Organization: {data.get('org', 'N/A')}[/bold yellow]\n"
            f"[bold red]Location: {data.get('loc', 'N/A')}[/bold red]",
            title="[bold magenta]GeoIP Information[/bold magenta]", expand=False
        ))
    except Exception as e:
        print(f"[bold red]Error retrieving GeoIP data: {e}[/bold red]")

# Port Scanner Feature
def port_scanner(ip):
    print(f"[bold green]Scanning open ports on {ip}...[/bold green]")
    open_ports = []
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((ip, port)) == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            print(Panel(
                f"[bold cyan]Open Ports:[/bold cyan] {', '.join(map(str, open_ports))}",
                title="[bold magenta]Port Scanner[/bold magenta]", expand=False
            ))
        else:
            print("[bold red]No open ports found.[/bold red]")
    except Exception as e:
        print(f"[bold red]Error: {e}[/bold red]")

# Function to display current date and time
def date_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(Panel(
        f"[bold cyan]Current Date and Time: {current_time}[/bold cyan]",
        title="[bold magenta]Date & Time[/bold magenta]", expand=False
    ))

# Function to display available commands
def show_commands():
    
    commands = [
        "track <ip> - Melacak alamat IP yang diberikan dan membuka lokasinya di Google Maps.",
        "date - Menampilkan tanggal dan waktu saat ini.",
        "geoip <ip> - Melakukan pencarian GeoIP untuk alamat IP yang diberikan.",
        "port <ip> - Memindai port terbuka untuk alamat IP yang diberikan.",
        "ascii - Mengubah teks menjadi kode ASCII.",
        "ping <website> - Melakukan ping ke situs web.",
        "edit <filename> - Mengedit file Python yang ditentukan.",
        "help - Menampilkan daftar perintah ini.",
        "clear - Membersihkan layar tetapi mempertahankan tampilan utama.",
        "exit - Keluar dari program.",
        "rquote - Menampilkan kutipan acak.",
        "cmatrix - Menampilkan animasi matriks.",
        "sl - Menampilkan animasi kereta.",
        "ls - Menampilkan daftar direktori.",
        "about - Menampilkan informasi tentang program.",
        "Any shell command - Menginstal, menjalankan, atau mengelola paket.",
        # Perintah Termux tambahan
        "pkg install <paket> - Menginstal paket perangkat lunak.",
        "pkg uninstall <paket> - Menghapus instalasi paket perangkat lunak.",
        "pkg update - Memperbarui daftar paket yang tersedia.",
        "pkg upgrade - Meningkatkan paket yang diinstal ke versi terbaru.",
        "pkg search <paket> - Mencari paket.",
        "pkg list-installed - Melisting paket yang terinstall.",
        "termux-setup-storage - Memberikan akses penyimpanan ke Termux.",
        "cd <direktori> - Mengubah direktori kerja saat ini.",
        "mkdir <direktori> - Membuat direktori baru.",
        "rm <file/direktori> - Menghapus file atau direktori.",
        "cp <sumber> <tujuan> - Menyalin file atau direktori.",
        "mv <sumber> <tujuan> - Memindahkan atau mengganti nama file atau direktori.",
        "cat <file> - Menampilkan isi file.",
        "grep <pola> <file> - Mencari pola dalam file.",
        "find <direktori> -nama <pola> - Mencari file berdasarkan nama.",
        "chmod +x <file> - Memberikan izin eksekusi pada file.",
        "nano <file> - Editor teks sederhana.",
        "vim <file> - Editor teks yang lebih canggih.",
        "ping <host> - Menguji konektivitas jaringan.",
        "ifconfig - Menampilkan konfigurasi antarmuka jaringan.",
        "ip addr - Menampilkan alamat IP dan konfigurasi jaringan.",
        "ssh <pengguna>@<host> - Menghubungkan ke server SSH.",
        "wget <url> - Mengunduh file dari URL.",
        "curl <url> - Mengunduh atau mengirim data dari/ke URL.",
        "netstat - Menampilkan koneksi jaringan.",
        "traceroute <host> - Menampilkan rute paket jaringan.",
        "top - Menampilkan proses yang sedang berjalan dan penggunaan sumber daya.",
        "ps - Menampilkan daftar proses yang sedang berjalan.",
        "kill <PID> - Menghentikan proses dengan ID proses (PID) tertentu.",
        "date - Menampilkan tanggal dan waktu.",
        "clear - Membersihkan layar terminal.",
        "exit - Keluar dari Termux.",
        "whoami - Menampilkan pengguna yang sedang login.",
        "termux-change-repo - Mengubah repositori Termux.",
        "termux-change-mirror - Mengubah mirror unduhan paket termux.",
        "proot-distro install <distro> - Menginstal distribusi Linux di dalam Termux.",
        "proot-distro login <distro> - Masuk ke distribusi Linux yang diinstal di dalam Termux.",
        "apt update - Memperbarui daftar paket (untuk sistem berbasis Debian/Ubuntu).",
        "apt install <paket> - Menginstal paket (untuk sistem berbasis Debian/Ubuntu).",
    ]
    print(Panel(
        "\n".join(commands),
        title="[bold magenta]Available Commands[/bold magenta]", expand=False
    ))

# Validate IP Address
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None

# ASCII Code Conversion Feature
def text_to_ascii():
    text = input("~ darkxy get #ascii :")
    ascii_codes = [(char, ord(char)) for char in text]
    result = "\n".join([f"[bold yellow]'{char}': {code}[/bold yellow]" for char, code in ascii_codes])
    print(Panel(
        f"[bold cyan]ASCII Codes and Interpretations:[/bold cyan]\n{result}",
        title="[bold magenta]ASCII Conversion[/bold magenta]", expand=False
    ))

# Function to edit a Python file
def edit_file(filename):
    try:
        # Open the specified file in nano or create it if it doesn't exist
        subprocess.run(["nano", filename])
        print(f"[bold green]Editing {filename}...[/bold green]")
        # After editing, run the Python file
        run_python_file(filename)
    except Exception as e:
        print(f"[bold red]Error editing file: {e}[/bold red]")

# Function to run a Python file
def run_python_file(filename):
    try:
        subprocess.run(["python3", filename])
    except Exception as e:
        print(f"[bold red]Error running file: {e}[/bold red]")
        
def quoterun():
  kata = [
      "Sholat itu sampai tua bukan nunggu tua.",
      "Ibadah itu sampai mati bukan nunggu mati.",
     "Sholatlah sebelum di sholati",
     "Biarkan dia pergi karena dunia ini juga hanya titipan.",
     "Dunia ini berputar, pantesan saya pusing",
     "Tanpa saya, warga Indonesia kurang satu",
     "Kesempatan tidak datang 2 kali kecuali remedial",
     "Masa depanmu tidak secerah hp bapakku",
     "Di setiap kelebihan pasti ada kembalian",
     "Tetaplah membalas budi, walau budi nggak salah",
     "Hidup cuma sekali kalo dua kali namanya hidup-hidup",
     "Dunia punya cerita yg cerita bukan saya",
     "Jangan menunda-nunda pekerjaan, kecuali menunda jatuh cinta.",
     "Cinta itu buta, tapi kenapa kalo nyari pacar pada melek?",
     "Kegagalan adalah keberhasilan yang tertunda, tapi kalo kebanyakan ya gagal juga.",
     "Jangan pernah menyerah, sebelum mencoba lagi.",
     "Hidup itu seperti roda, kadang di atas kadang di bawah, tapi yang penting rodanya nggak kempes.",
     "Jika kamu merasa sendiri, ingatlah ada aku di sini, menemanimu dalam kesendirianmu.",
     "Jangan bersedih jika hidupmu tidak sesuai harapan, mungkin saja harapanmu yang terlalu tinggi.",
     "Jadilah dirimu sendiri, jangan meniru orang lain, karena setiap orang punya keunikan masing-masing."
  ]
  kata_random = random.choice(kata)
  print(Panel(f"[bold yellow]{kata_random}[/bold yellow]"))

# Main Command Loop
def main():
    show_logo()
    discalimer()
    device_info()

    while True:
        command = input("~ darkxy get #: ").strip().lower()
        
        if command.startswith("track"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                track_ip(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command == "date":
            date_time()
        
        elif command.startswith("geoip"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                geoip_lookup(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command.startswith("port"):
            _, ip = command.split(maxsplit=1)
            if is_valid_ip(ip):
                port_scanner(ip)
            else:
                print("[bold red]Invalid IP address.[/bold red]")
        
        elif command.startswith("ascii"):
            text_to_ascii()
        
        elif command.startswith("ping"):
            _, website = command.split(maxsplit=1)
            ping_website()
        
          
        elif command.startswith("rquote"):
          quoterun()
        
        elif command.startswith("edit"):
            _, filename = command.split(maxsplit=1)
            edit_file(filename)
            
        elif command == 'about':
            author_info()
        
        elif command == "help":
            show_commands()
        
        elif command == "clear":
            os.system('clear')
            show_logo()
            discalimer()
            device_info()
            

        elif command == "exit":
            print("[bold red]Exiting program...[/bold red]")
            break
          
        else:
            os.system(command)

if __name__ == "__main__":
    main()
