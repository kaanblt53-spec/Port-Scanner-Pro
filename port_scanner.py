import socket
import threading
import os
from datetime import datetime

PORT_BILGILERI = {
    21: "FTP (Dosya Aktarımı)",
    22: "SSH (Güvenli Bağlantı)",
    23: "Telnet",
    25: "SMTP (E-posta)",
    53: "DNS",
    80: "HTTP (Web)",
    135: "RPC (Windows)",
    139: "NetBIOS (Windows)",
    443: "HTTPS (Güvenli Web)",
    445: "SMB (Dosya Paylaşımı)",
    3306: "MySQL Veritabanı",
    3389: "RDP (Uzak Masaüstü)"
}

sonuclar = []

def port_scanner(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            servis_adi = PORT_BILGILERI.get(port, "Bilinmeyen Servis")
            try:
                banner = s.recv(1024).decode().strip()
                if banner:
                    bilgi = f"[+] Port {port} AÇIK  --> Banner: {banner} ({servis_adi})"
                else:
                    bilgi = f"[+] Port {port} AÇIK  --> Servis: {servis_adi} (Banner boş)"
            except:
                bilgi = f"[+] Port {port} AÇIK  --> Servis: {servis_adi} (Banner alınamadı)"
            
            print(bilgi)
            sonuclar.append(bilgi)
        
        s.close()
    except:
        pass

target = input("Taramak istediğiniz IP veya Domain: ")
target_ip = socket.gethostbyname(target)

print("-" * 50)
print(f"Tarama başlatıldı: {target_ip}")
print("-" * 50)

threads = []
for port in range(1, 1024):
    thread = threading.Thread(target=port_scanner, args=(target_ip, port))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open("bulunanlar.txt", "w", encoding="utf-8") as f:
    f.write(f"Hedef: {target_ip}\nTarih: {datetime.now()}\n")
    f.write("-" * 30 + "\n")
    for satir in sonuclar:
        f.write(satir + "\n")

print("-" * 50)
print(f"Tarama bitti. Dosya: {os.path.abspath('bulunanlar.txt')}")
