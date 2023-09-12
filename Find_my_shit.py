import scapy.all as scapy
import time

def discover_nas():
    # L'adresse IP de départ pour le scan (exemple: 192.168.1.1)
    ip_range = "192.168.1.1/24"

    # Crée un paquet ARP pour le scan
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    # Envoie le paquet ARP et reçoit les réponses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    thing_list = []

    for element in answered_list:
        all_your_shit = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        thing_list.append(all_your_shit)

    return thing_list

def main():
    print("Recherche de trucs sur le réseau...")
    nas_list = discover_nas()

    if len(nas_list) == 0:
        print("Euhh rien trouvé sur le réseau LOL")
    else:
        print("Oh y'a du monde sur le réseau :")
        for i in nas_list:
            print(f"IP: {i['ip']}, MAC: {i['mac']}")

main()