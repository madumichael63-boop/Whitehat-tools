print("=== Password Strength Checker ===")
password = input("Enter a password to test: ")

score = 0
if len(password) >= 8:
    score += 1
else:
    print("- Too short! Use 8+ characters")

if any(c.isupper() for c in password):
    score += 1
else:
    print("- Add UPPERCASE letter")

if any(c.isdigit() for c in password):
    score += 1
else:
    print("- Add a number")

if any(c in "!@#$%^&*" for c in password):
    score += 1
else:
    print("- Add symbol like ! @ #")

print(f"\nScore: {score}/4")
if score == 4:
    print("STRONG - Good job!")
elif score >= 2:
    print("MEDIUM - Can be hacked easily")
else:
    print("WEAK - Hackers will crack this in seconds!")
