import subprocess
import time
import socket

def ping(host):
    try:
        subprocess.check_output(["ping", "-c", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def main():
    devices = []
    
    while True:
        print("\n1. Ajouter une adresse IP")
        print("2. Démarrer la surveillance")
        print("3. Quitter")
        choice = input("Choix : ")
        
        if choice == "1":
            ip = input("Adresse IP : ")
            if is_valid_ip(ip):
                devices.append(ip)
                print(f"Adresse IP {ip} ajoutée.")
            else:
                print("Adresse IP non valide.")
        elif choice == "2":
            if not devices:
                print("Aucune adresse IP à surveiller.")
            else:
                while True:
                    for device in devices:
                        status = "en ligne" if ping(device) else "hors ligne"
                        print(f"{device} est {status}.")
                    time.sleep(10)
        elif choice == "3":
            break

main()

