import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters).")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        return "Strong password 💪"
    else:
        return f"Weak password. Suggestions: {', '.join(feedback)}"

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = check_password_strength(pwd)
    print(result)
