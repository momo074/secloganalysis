import re

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def analyze_logs(self):
        with open(self.log_file, 'r') as file:
            logs = file.readlines()

        suspicious_logs = []
        for log in logs:
            if self.detect_attack(log):
                suspicious_logs.append(log)

        return suspicious_logs

    def detect_attack(self, log):
        # Example attack detection: searching for suspicious strings
        suspicious_patterns = [
            r'\b(?:SQL injection|XSS attack)\b',
            r'\b(?:bruteforce|ddos)\b',
            r'\b(?:malware|trojan)\b'
        ]

        for pattern in suspicious_patterns:
            if re.search(pattern, log, re.IGNORECASE):
                return True

        return False

if __name__ == "__main__":
    log_file = "logfile.txt"  # Replace with the path to your log file
    analyzer = LogAnalyzer(log_file)
    suspicious_logs = analyzer.analyze_logs()

    if suspicious_logs:
        print("Suspicious logs detected:")
        for log in suspicious_logs:
            print(log)
    else:
        print("No suspicious logs detected.")
