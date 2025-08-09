import socket

def check_dns(hostname: str) -> bool:
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False
    
def load_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and convert to lowercase
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()

blocklist_domains = load_domains("./Lists/BLACKLIST.txt")
for domain in blocklist_domains:
    if not check_dns(domain):
        print(f"DNS resolution failed for {domain}")
        exit(1)
    else:
        print(f"DNS resolution successful for {domain}")