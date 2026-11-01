import socket
print("=== Ethical Port Scanner ===")
target = input("Enter IP to scan (use 127.0.0.1 to scan yourself): ")
print(f"\nScanning {target}... This is legal only on YOUR devices!\n")

common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
for port in common_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} : OPEN - Might be vulnerable")
    else:
        print(f"Port {port} : closed")
    s.close()

print("\nScan done. OPEN ports are entry points hackers check.")
