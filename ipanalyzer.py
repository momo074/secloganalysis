import socket

def ip_analyzer(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(f"L'adresse IP {ip_address} correspond à l'hôte {host_name[0]}")
    except socket.herror:
        print(f"Impossible de trouver l'hôte correspondant à l'adresse IP {ip_address}")

# Test de la fonction
ip_analyzer("8.8.8.8")
