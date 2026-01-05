import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score == 5:
        strength = "STRONG 💪"
    elif score >= 3:
        strength = "MEDIUM ⚠️"
    else:
        strength = "WEAK ❌"

    return strength, feedback


print("🔐 Password Complexity Checker 🔐")
password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve your password:")
    for tip in feedback:
        print("-", tip)
else:
    print("✅ Your password meets all security requirements!")
