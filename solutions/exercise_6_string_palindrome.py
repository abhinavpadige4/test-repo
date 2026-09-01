\"\"\"
Exercise 6: String Palindrome Check
Topic: String Manipulation
Difficulty: Medium

Problem Statement:
Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
Ignore spaces, punctuation, and capitalization.

Solution:
\"\"\"
import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]

def main():
    # Test the function with examples
    test_strings = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        ""
    ]
    for s in test_strings:
        print(f"'{s}' -> {is_palindrome(s)}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Classic palindrome with punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test 1 failed"
    print("Test Case 1 Passed: 'A man, a plan, a canal: Panama'")
    
    # Test Case 2: Simple palindrome
    assert is_palindrome("racecar") == True, "Test 2 failed"
    print("Test Case 2 Passed: 'racecar'")
    
    # Test Case 3: Not a palindrome
    assert is_palindrome("hello") == False, "Test 3 failed"
    print("Test Case 3 Passed: 'hello'")
    
    # Test Case 4: Another complex palindrome
    assert is_palindrome("Was it a car or a cat I saw?") == True, "Test 4 failed"
    print("Test Case 4 Passed: 'Was it a car or a cat I saw?'")
    
    # Test Case 5: Empty string
    assert is_palindrome("") == True, "Test 5 failed"
    print("Test Case 5 Passed: Empty string")
    
    # Test Case 6: Single character
    assert is_palindrome("a") == True, "Test 6 failed"
    print("Test Case 6 Passed: Single character")
    
    print("\\nAll tests passed!")