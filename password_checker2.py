import math
import re

# Load common passwords
with open("common_passwords.txt") as f:
    COMMON_PASSWORDS = set([line.strip() for line in f])

def calculate_entropy(password):
    """
    Estimate password entropy in bits
    """
    charset_size = 0
    if re.search(r"[a-z]", password):
        charset_size += 26
    if re.search(r"[A-Z]", password):
        charset_size += 26
    if re.search(r"[0-9]", password):
        charset_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset_size += 32 # symbols approximation

    return len(password) * math.log2(charset_size) if charset_size else 0

def check_password(password):
    print(f"Checking password: {password}")

    # Dictionary check
    if password.lower() in COMMON_PASSWORDS:
        print("! This password is very common!")

    # Entropy check
    entropy = calculate_entropy(password)
    print(f"Entropy: {entropy:.2f} bits")
    if entropy < 50:
        print("!! Password entropy is low; consider making it longer or more complex.")

    # Pattern detection
    if re.search(r"(.)\1{2,}", password):
        print("!!! Password has repeated characters!")
    if re.search(r"(0123|1234|abcd|qwerty)", password.lower()):
        print("!! Password contains a common pattern!")

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password(pwd)