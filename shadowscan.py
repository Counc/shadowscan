import socket
import sys
requests = None
try:
    import requests
except ImportError:
    pass
from datetime import datetime

def banner():
    print("""
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███████╗ ██████╗ ███╗   ██╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝ ████╗  ██║
    ███████╗███████║███████║██║  ██║██║   ██║███████╗██║  ███╗██╔██╗ ██║
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║╚════██║██║   ██║██║╚██╗██║
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝███████║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═══╝
              [ Advanced Recon & Security Scanner ]
              [         Created by Counc          ]
    """)

def check_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("[-] Hata: Hedef çözümlenemedi! Geçerli bir URL veya IP girin.")
        sys.exit()

def port_scanner(ip):
    print(f"\n[+] Port Taraması Başlatılıyor: {ip}")
    common_ports = [21, 22, 80, 443, 8080, 3306]
    for port in common_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"    [OPEN] Port {port} açık")
        s.close()

def http_headers(url):
    print(f"\n[+] HTTP Güvenlik Başlıkları Kontrol Ediliyor...")
    if not url.startswith("http"):
        url = "http://" + url
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        security_headers = ['Content-Security-Policy', 'X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security']
        
        for sh in security_headers:
            if sh in headers:
                print(f"    [+] {sh}: Bulundu (Güvenli)")
            else:
                print(f"    [-] {sh}: Eksik! (Potansiyel Risk)")
    except Exception as e:
        print(f"    [-] Bağlantı hatası: {e}")

if __name__ == "__main__":
    banner()
    target_input = input("Hedef domain veya IP adresi girin (örn: example.com): ")
    target_ip = check_target(target_input)
    
    print(f"[*] Hedef IP: {target_ip}")
    print(f"[*] İşlem Zamanı: {datetime.now()}")
    
    port_scanner(target_ip)
    http_headers(target_input)
    print("\n[+] Tarama Tamamlandı!")
          
