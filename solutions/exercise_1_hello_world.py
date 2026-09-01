\"\"\"
Exercise 1: Hello World with User Input
Topic: Basics
Difficulty: Easy

Problem Statement:
Write a program that asks the user for their name and then greets them with a personalized message.

Requirements:
- Prompt the user to enter their name
- Read the input from the user
- Print a greeting message: "Hello, [name]! Welcome to Python programming!"
- Handle empty input by assigning a default name "Guest"

Example:
Input: Alice
Output: Hello, Alice! Welcome to Python programming!

Input: (empty)
Output: Hello, Guest! Welcome to Python programming!
\"\"\"

def greet_user():
    \"\"\"Ask for user name and return a personalized greeting.\"\"\"
    name = input("Enter your name: ").strip()
    if not name:
        name = "Guest"
    return f"Hello, {name}! Welcome to Python programming!"

if __name__ == "__main__":
    # Test cases
    print("Test Case 1: Normal input")
    # Simulate input for testing - in real scenario, use actual input
    # We'll demonstrate with predefined values for test purposes
    test_names = ["Alice", "", "Bob"]
    for test_name in test_names:
        # Temporarily replace input function for testing
        import builtins
        original_input = builtins.input
        builtins.input = lambda _: test_name
        try:
            result = greet_user()
            print(f"Input: '{test_name}' -> Output: {result}")
        finally:
            builtins.input = original_input
    
    # Actual interactive run (uncomment below to run interactively)
    # print(greet_user())
\"\"\"