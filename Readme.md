# 🔐 Password Strength Checker

A simple Python-based Password Strength Checker that evaluates the security of a password based on common password security rules and provides suggestions for improvement.

**Author:** Galvin  
**Date:** June 9, 2026  
**Version:** 1.0  


## Features

* Checks password strength on a scale of **0–5**
* Categorizes passwords as:

  * Weak
  * Moderate
  * Strong
* Detects commonly used passwords from a predefined list
* Provides actionable feedback to improve password security
* Logs password strength results to a file without storing the actual password
* Interactive command-line interface

---

## How It Works

The program evaluates passwords based on factors such as:

* Minimum length requirements
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Presence in a common-password database

After evaluation, the program:

1. Assigns a strength score (0–5)
2. Displays a strength label
3. Provides suggestions for improvement
4. Records the result in a log file using masked passwords

---

## Project Structure

```text
password-strength-checker/
│
├── password_checker.py
├── common_passwords.txt
├── password_log.txt
└── README.md
```

---

## Installation

### Prerequisites

* Python 3.8 or later

### Clone the Repository

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

---

## Usage

Run the program:

```bash
python password_checker.py
```

Example:

```text
Enter a password to check (or 'quit' to exit): Password123!

Strength: Strong (5/5)
```

Example with feedback:

```text
Enter a password to check (or 'quit' to exit): pass

Strength: Weak (1/5)

Suggestions:
  - Increase password length.
  - Add uppercase letters.
  - Include numbers.
  - Add special characters.
```

Exit the application:

```text
quit
```

---

## Logging

The application stores password assessment results in:

```text
password_log.txt
```

For security reasons, passwords are **never stored in plain text**.

Example log entry:

```text
Password: *********** | Strength: Strong (5/5)
```

---

## Strength Rating Scale

| Score | Rating   |
| ----- | -------- |
| 0–1   | Weak     |
| 2–3   | Moderate |
| 4–5   | Strong   |

---

## Future Improvements

* Password entropy calculation
* Password breach detection using APIs
* GUI version with Tkinter
* Web-based password checker
* Password generation feature
* Advanced pattern detection

---

## Security Note

This project is intended for educational purposes. While it follows basic password-strength evaluation techniques, it should not be considered a replacement for enterprise-grade security validation systems.

---

## License

This project is licensed under the MIT License.

Feel free to fork, modify, and improve the project.
