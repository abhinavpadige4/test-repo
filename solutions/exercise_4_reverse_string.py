\"\"\"
Exercise 4: Reverse a String
Topic: Strings and Loops
Difficulty: Easy

Problem Statement:
Write a program that asks the user to enter a string and then prints the reverse of that string.

Requirements:
- Prompt the user to enter a string
- Reverse the string without using built-in reverse() or slicing with [::-1] (for learning purposes)
- Print the reversed string
- Handle empty string input

Example:
Input: hello
Output: olleh

Input: (empty)
Output: (empty line)
\"\"\"

def reverse_string(s):
    \"\"\"Return the reverse of the input string.\"\"\"
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    user_input = input("Enter a string: ")
    reversed_result = reverse_string(user_input)
    print("Reversed string:", reversed_result)

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("", ""),
        ("a", "a"),
        ("12345", "54321"),
    ]
    
    for input_str, expected in test_cases:
        result = reverse_string(input_str)
        if result == expected:
            print(f"PASS: '{input_str}' -> '{result}'")
        else:
            print(f"FAIL: '{input_str}' -> Expected: '{expected}', Got: '{result}'")
    
    # Uncomment below to run interactively
    # main()