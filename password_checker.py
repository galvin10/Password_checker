def main():
    strength_labels = {
        0: "Weak", 1: "Weak",
        2: "Moderate", 3: "Moderate",
        4: "Strong", 5: "Strong"
    }

    common_list = load_common_passwords("common_passwords.txt")

    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ")

        if password.lower() == "quit":
            print("Goodbye.")
            break

        if len(password) == 0:
            print("Password cannot be empty. Try again.")
            continue

        score, feedback = check_password(password, common_list)
        label = strength_labels.get(score, "Unknown")

        print(f"\nStrength: {label} ({score}/5)")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  - {tip}")

        # Log the result (mask the actual password with asterisks)
        with open("password_log.txt", "a") as log:
            log.write(f"Password: {'*' * len(password)} | Strength: {label} ({score}/5)\n")

main()
