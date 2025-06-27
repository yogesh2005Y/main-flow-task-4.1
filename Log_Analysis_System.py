from collections import defaultdict
import re

def parse_log_line(line):
    """
    Extract IP, URL, and response code from a typical log line.
    Assumes Common Log Format or Combined Log Format.
    """
    match = re.match(r'(\S+) \S+ \S+ \[.*?\] "\S+ (\S+) \S+" (\d+)', line)
    if match:
        ip = match.group(1)
        url = match.group(2)
        response_code = match.group(3)
        return ip, url, response_code
    return None, None, None

def analyze_log(file_path):
    ip_counts = defaultdict(int)
    url_counts = defaultdict(int)
    response_counts = defaultdict(int)

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                ip, url, response = parse_log_line(line)
                if ip and url and response:
                    ip_counts[ip] += 1
                    url_counts[url] += 1
                    response_counts[response] += 1
    except FileNotFoundError:
        print(f"[Error] File not found: {file_path}")
        return

    print("\n📊 Top 5 IP Addresses:")
    for ip, count in sorted(ip_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"{ip} => {count} requests")

    print("\n🌐 Top 5 Requested URLs:")
    for url, count in sorted(url_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"{url} => {count} hits")

    print("\n📬 HTTP Response Codes:")
    for code, count in sorted(response_counts.items()):
        print(f"{code} => {count} responses")

if __name__ == "__main__":
    # Replace with your actual log file path
    log_path = "access.log"
    analyze_log(log_path)
