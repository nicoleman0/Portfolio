import nmap

# This is based on HackerSploit's Nmap Automation Tool. 

scanner = nmap.PortScanner()

print("Welcome! This is a simple Nmap automation tool.")
print("You must be using root priveleges to run this tool.")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input(
    """
    \nPlease enter the type of scan you  want to run:
    1) SYN ACK Scan - sS
    2) UDP Scan - sU
    3) Comprehensive Scan - sS -sV -sC -A -O
    \n""")
print("You have selected Option: ", resp)

if resp == '1': 
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS') 
    print(scanner.scaninfo()) 
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp not in ['1', '2', '3']:
    print("Please enter a valid option.")