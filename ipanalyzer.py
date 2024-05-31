import socket

def ip_analyzer(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(f"L'adresse IP {ip_address} correspond à l'hôte {host_name[0]}")
    except socket.herror:
        print(f"Impossible de trouver l'hôte correspondant à l'adresse IP {ip_address}")

def test_ip():
    try:
        # Get host name corresponding to the IP address
        host_name = socket.gethostbyaddr(ip_address)
        print(f"The IP address {ip_address} corresponds to the host {host_name[0]}")
    except socket.herror:
        print(f"Unable to find the host corresponding to the IP address {ip_address}")


ip_analyzer("8.8.8.8")
