import urllib.request

print("=== Ethical Website Security Checker ===")
url = input("Enter website (like https://google.com): ")

if not url.startswith("http"):
    url = "https://" + url

try:
    print(f"\nScanning {url} ...\n")
    req = urllib.request.Request(url, headers={'User-Agent': 'WhiteHat-Checker'})
    with urllib.request.urlopen(req, timeout=10) as response:
        print(f"Status: {response.status} OK")
        print("\n--- Security Headers (what protects site) ---")
        headers = response.headers
        
        # Check important security headers
        security_checks = {
            "Strict-Transport-Security": "Protects from fake sites",
            "Content-Security-Policy": "Blocks XSS hacking",
            "X-Frame-Options": "Blocks clickjacking",
            "X-Content-Type-Options": "Blocks malware injection"
        }
        
        for header, meaning in security_checks.items():
            if header in headers:
                print(f"[GOOD] {header}: Present -> {meaning}")
            else:
                print(f"[MISSING] {header}: Missing -> Site weaker to {meaning}")

        print("\n--- Server Info (what hacker sees) ---")
        for h in ["Server", "X-Powered-By"]:
            if h in headers:
                print(f"{h}: {headers[h]}")

        print("\nScan done. White hats report MISSING headers to get paid!")

except Exception as e:
    print(f"Error: {e}")
    print("Try with https://google.com or https://facebook.com")
