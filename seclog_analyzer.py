import re
import math

import socket

def ip_analyzer(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)
        print(f"L'adresse IP {ip_address} correspond à l'hôte {host_name[0]}")
    except socket.herror:
        print(f"Impossible de trouver l'hôte correspondant à l'adresse IP {ip_address}")

def main(log_path):
    with open(log_path, 'r') as file:
        logs = file.readlines()
    

def intrusion_inc(type):
    intrusion_list = []
    # Simulating intrusion incidents
    for i in range(1, 101):
        intrusion = {
            "id": i,
            "type": type,
            "severity": random.choice(["low", "medium", "high"]),
            "source_ip": f"192.168.1.{random.randint(1, 255)}",
            "description": f"Suspicious {type} activity detected"
        }
        intrusion_list.append(intrusion)
    
    return intrusion_list



if __name__ == "__main__":
    # Test de la fonction
ip_analyzer("8.8.8.8")
    import sys
    if len(sys.argv) < 2:
        print("Not in the loop : seclog_analyzer.py /chemin/vers/les/logs")
    else:
        main(sys.argv[1])
