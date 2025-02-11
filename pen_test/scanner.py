import socket
import threading
import concurrent.futures

print_lock = threading.Lock()

ip = input("Enter the IP address to scan: ")

def scan(scanner, ip, port):
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        with print_lock:
           print(f"Port {port} is open.")
    except:
        print(f"Port {port} is open.")
    finally:
        scanner.close()


start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        executor.submit(scan, scanner, ip, port)

print("Scanning completed. Have a good day.")