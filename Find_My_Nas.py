import webbrowser
import socket 
from PIL import Image
def find_NAS_server():
    # Remplacez "truenas" par le nom d'hôte réel de votre serveur TrueNAS
    hostname = "truenas"
    port = 80  # Vous pouvez également changer le port si nécessaire (par exemple, 443 pour HTTPS)

    try:
        # Obtenez l'adresse IP associée au nom d'hôte
        server_ip = socket.gethostbyname(hostname)
        return server_ip
    except socket.gaierror:
        return None

server_ip = find_NAS_server()

if server_ip:
    print(f"Le serveur TrueNAS a été trouvé. Adresse IP : {server_ip}")
    webbrowser.open(f"http://{server_ip}")  # Ouvre la page avec l'adresse IP trouvée
else:
    print("Serveur TrueNAS introuvable sur le réseau local.")
    
  
    img = Image.open("img/7vriy6.jpg")  # Remplacez par le chemin complet de votre image
    img.show()  # Affiche l'image localement










