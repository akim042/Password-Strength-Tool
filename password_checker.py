import re

def check_password_strength(password):
    """
    Returns a strength score and message for the given password.
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count errors
    errors = [length_error, digit_error, upper_error, lower_error, symbol_error]
    score = 5 - sum(errors)

    # Determine strength message
    if score == 5:
        strength = "Very Strong ✅"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium ⚠️"
    elif score == 2:
        strength = "Weak ❌"
    else:
        strength = "Very Weak ❌"

    return score, strength

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")
    score, strength = check_password_strength(password)
    print(f"Strength Score: {score}/5")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()