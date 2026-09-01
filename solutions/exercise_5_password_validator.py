\"\"\"
Exercise 5: Simple Password Validator
Topic: String Manipulation and Conditionals
Difficulty: Easy

Problem Statement:
Write a program that validates a password based on the following criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character from !@#$%^&*

The program should:
- Prompt the user to enter a password
- Check the password against the criteria
- Print whether the password is valid or not, and if not, list which criteria failed

Example:
Input: Password123!
Output: Valid password!

Input: pass
Output: Invalid password! Reasons:
        - Must be at least 8 characters long
        - Must contain at least one uppercase letter
        - Must contain at least one digit
        - Must contain at least one special character from !@#$%^&*
\"\"\"

def validate_password(password):
    \"\"\"Validate the password and return a list of error messages (empty if valid).\"\"\"
    errors = []
    if len(password) < 8:
        errors.append("Must be at least 8 characters long")
    if not any(c.isupper() for c in password):
        errors.append("Must contain at least one uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("Must contain at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Must contain at least one digit")
    special_chars = set("!@#$%^&*")
    if not any(c in special_chars for c in password):
        errors.append("Must contain at least one special character from !@#$%^&*")
    return errors

def main():
    password = input("Enter a password: ")
    errors = validate_password(password)
    if not errors:
        print("Valid password!")
    else:
        print("Invalid password! Reasons:")
        for error in errors:
            print(f"  - {error}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    test_cases = [
        ("Password123!", []),
        ("pass", [
            "Must be at least 8 characters long",
            "Must contain at least one uppercase letter",
            "Must contain at least one digit",
            "Must contain at least one special character from !@#$%^&*"
        ]),
        ("PASSWORD123!", [
            "Must contain at least one lowercase letter"
        ]),
        ("password123!", [
            "Must contain at least one uppercase letter"
        ]),
        ("Password!", [
            "Must contain at least one digit"
        ]),
        ("Password123", [
            "Must contain at least one special character from !@#$%^&*"
        ]),
    ]
    
    for pwd, expected_errors in test_cases:
        result = validate_password(pwd)
        if result == expected_errors:
            print(f"PASS: Password '{pwd}' -> errors: {result}")
        else:
            print(f"FAIL: Password '{pwd}' -> Expected: {expected_errors}, Got: {result}")
    
    # Uncomment below to run interactively
    # main()