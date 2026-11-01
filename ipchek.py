import socket
print("=== Ethical IP Info Tool V2 ===")
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"Device: {hostname}")
print(f"Local IP (your phone to itself): {local_ip}")

try:
    import urllib.request, json
    print("\nChecking public IP (what Google sees)...")
    data = urllib.request.urlopen('https://api.ipify.org?format=json', timeout=5).read()
    public_ip = json.loads(data)['ip']
    print(f"Your PUBLIC IP: {public_ip}")
    print("White hats hide this with VPN!")
except:
    print("No internet - connect data to see public IP")
