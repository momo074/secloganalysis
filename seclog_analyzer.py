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
    
    for log in logs:
        if detect_intrusion(log):
            print(f"Suspicious activity detected: {log}")

def intrusion_inc(type):
    list = []
    for i in range (0,100):
        list.append(i) 


if __name__ == "__main__":
    # Test de la fonction
ip_analyzer("8.8.8.8")
    import sys
    if len(sys.argv) < 2:
        print("Not in the loop : seclog_analyzer.py /chemin/vers/les/logs")
    else:
        main(sys.argv[1])
