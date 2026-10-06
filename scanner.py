import socket
import sys
from datetime import datetime

def scan(target, start=1, end=1024):
    print(f"Scanning {target} (ports {start}-{end})")
    print(f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}\n")
    try:
        ip = socket.gethostbyname(target)
        for port in range(start, end + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"
                print(f"[OPEN] {port}/tcp  ({service})")
            s.close()
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        sys.exit()
    print("\nScan complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scanner.py <target>")
        sys.exit(1)
    scan(sys.argv[1])
