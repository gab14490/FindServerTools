import socket
import webbrowser
import customtkinter as ctkr

def find_NAS_server(hostname, port):
    try:
        server_ip = socket.gethostbyname(hostname)
        return server_ip
    except socket.gaierror:
        return None

def find_server_and_open_browser():
    hostname = hostname_entry.get()
    port = port_entry.get()  # Récupère la valeur du champ d'entrée du port
    if not port:
        for p in [80, 443]:  # Listes des ports à essayer
            server_ip = find_NAS_server(hostname, p)
            if server_ip:
                break
    else:
        server_ip = find_NAS_server(hostname, port)

    if server_ip:
        result_label.configure(text=f"Le serveur {hostname} a été trouvé. Adresse IP : {server_ip}")
        if check_var.get() == "on":
            webbrowser.open(f"http://{server_ip}")
    else:
        result_label.configure(text=f"Serveur {hostname} introuvable sur le réseau local.")

def change_appearance():
    if theme_switch_var.get():
        app._set_appearance_mode("light")
    else:
        app._set_appearance_mode("dark")

# Création de la fenêtre principale avec customtkinter
app = ctkr.CTk()
app.geometry("400x350")  # Définition de la taille de la fenêtre

# Création des widgets avec customtkinter
instruction_label = ctkr.CTkLabel(app, text="Entrez le nom d'hôte du serveur :")
instruction_label.pack(side="top", anchor="nw", padx=10, pady=10)

label_input_hostname = ctkr.CTkLabel(app, text="Hostname : ")
label_input_hostname.pack(side="top", anchor="nw", padx=10)

hostname_entry = ctkr.CTkEntry(app)
hostname_entry.pack(side="top", anchor="nw", padx=10)

# Champ d'entrée pour spécifier le port
port_label = ctkr.CTkLabel(app, text="Port : ")
port_label.pack(side="top", anchor="nw", padx=10)

port_entry = ctkr.CTkEntry(app)
port_entry.pack(side="top", anchor="nw", padx=10)

check_var = ctkr.StringVar(value="on")
checkbox = ctkr.CTkCheckBox(app, text="Ouvrir interface web", variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(side="top", anchor="w", padx=10)

find_button = ctkr.CTkButton(app, text="Rechercher le serveur", command=find_server_and_open_browser)
find_button.pack(side="top", pady=20)

result_label = ctkr.CTkLabel(app, text="")
result_label.pack(pady=10)

# Ajout d'un commutateur pour changer l'apparence
theme_switch_var = ctkr.BooleanVar(value=False)
theme_switch = ctkr.CTkSwitch(app, text="Thème clair", variable=theme_switch_var, command=change_appearance)
theme_switch.pack(side="top", anchor="ne", padx=10, pady=10)  # Met le switch en haut à droite

# Exécution de la boucle principale
app.mainloop()










