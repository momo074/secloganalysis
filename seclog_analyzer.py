import re
import math

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
        print(list)

def detect_intrusion(log):
    patterns = [
        r"(UNION SELECT|SELECT.*FROM.*WHERE)",
        r"(DROP TABLE|DROP DATABASE)",
        r"(--|;).*"
    ]
    for pattern in patterns:
        if re.search(pattern, log):
            return True
    return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Not in the loop : seclog_analyzer.py /chemin/vers/les/logs")
    else:
        main(sys.argv[1])
