\"\"\"
Exercise 3: Even or Odd Checker
Topic: Control Flow
Difficulty: Easy

Problem Statement:
Write a program that asks the user to enter an integer and then determines whether the number is even or odd.

Requirements:
- Prompt the user to enter an integer
- Check if the number is even or odd using modulo operator (%)
- Print an appropriate message: "[number] is even." or "[number] is odd."
- Handle non-integer inputs by displaying an error message

Example:
Input: 4
Output: 4 is even.

Input: 7
Output: 7 is odd.

Input: abc
Output: Error: Please enter a valid integer!
\"\"\"

def check_even_odd():
    \"\"\"Ask for an integer and determine if it's even or odd.\"\"\"
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            return f"{num} is even."
        else:
            return f"{num} is odd."
    except ValueError:
        return "Error: Please enter a valid integer!"

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # We'll simulate input for testing
    import builtins
    original_input = builtins.input
    
    test_cases = [
        (4, "4 is even."),
        (7, "7 is odd."),
        (0, "0 is even."),
        (-3, "-3 is odd."),
        ("abc", "Error: Please enter a valid integer!"),
        ("12.5", "Error: Please enter a valid integer!")  # float string
    ]
    
    for test_input, expected in test_cases:
        builtins.input = lambda _: test_input
        try:
            result = check_even_odd()
            if result == expected:
                print(f"PASS: Input '{test_input}' -> '{result}'")
            else:
                print(f"FAIL: Input '{test_input}' -> Expected: '{expected}', Got: '{result}'")
        finally:
            builtins.input = original_input
    
    # Uncomment below to run interactively
    # print(check_even_odd())