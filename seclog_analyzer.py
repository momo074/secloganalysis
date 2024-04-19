import re

def main(log_path):
    with open(log_path, 'r') as file:
        logs = file.readlines()
    
    for log in logs:
        if detect_intrusion(log):
            print(f"Suspicious activity detected: {log}")

def detect_intrusion(log):
    # Exemple d'expression régulière pour détecter une tentative d'injection SQL
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
        print("Usage: python seclog_analyzer.py /chemin/vers/les/logs")
    else:
        main(sys.argv[1])
