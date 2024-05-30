import re
import math
import socket
import random  # Added import for random module
import datetime  # Added import for datetime module

# Function to analyze IP address
def ip_analyzer(ip_address):
    try:
        # Get host name corresponding to the IP address
        host_name = socket.gethostbyaddr(ip_address)
        print(f"The IP address {ip_address} corresponds to the host {host_name[0]}")
    except socket.herror:
        print(f"Unable to find the host corresponding to the IP address {ip_address}")


# Function to generate intrusion incidents
def intrusion_inc(type):
    intrusion_list = []
    for i in range(1, 101):
        intrusion = {
            "id": i,
            "type": type,
            "severity": random.choice(["low", "medium", "high"]),
            "destination_ip": f"10.0.0.{random.randint(1, 255)}",  # Added destination IP
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Added timestamp
            "description": f"Cyberlympics{go0D_0Ld_m4Ur!Ce!}/Suspicious {type} activity detected"
        }
        intrusion_list.append(intrusion)

    return intrusion_list

if __name__ == "__main__":
    # Test the ip_analyzer function with a sample IP address
    ip_analyzer("8.8.8.8")

    import sys
    # Check if log file path is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python seclog_analyzer.py /path/to/logs")  # Updated print statement for usage
    else:
        main(sys.argv[1])
