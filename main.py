import re

def check_password_strength(password):
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase letter": bool(re.search(r'[A-Z]', password)),
        "Lowercase letter": bool(re.search(r'[a-z]', password)),
        "Digit": bool(re.search(r'\d', password)),
        "Special character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    score = sum(criteria.values())
    
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    print(f"\nPassword Strength: {strength}")
    for rule, passed in criteria.items():
        print(f"[{'✔' if passed else '✘'}] {rule}")

# Example usage
password = input("Enter a password to test: ")
check_password_strength(password)
