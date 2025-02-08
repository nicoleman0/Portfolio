import socket
import threading
import concurrent.futures

print_lock = threading.Lock()

ip = input("Enter the IP address to scan: ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
           print(f"Port {port} is open.")
    except:
        pass


start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan, ip, port)

print("Scanning completed. Have a good day.")