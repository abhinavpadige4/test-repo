"""
Exercise 1: String Palindrome Checker (Easy)

Problem Statement:
Write a function that checks if a given string is a palindrome.
A palindrome reads the same forwards and backwards (ignoring case and spaces).

Example:
- "racecar" → True
- "A man a plan a canal Panama" → True
- "hello" → False

Requirements:
- Ignore case sensitivity
- Ignore spaces and special characters
- Return a boolean value
"""

def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text: Input string to check
        
    Returns:
        True if palindrome, False otherwise
    """
    # Clean the string: lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


# Test Cases
def test_palindrome():
    """Test cases for is_palindrome function"""
    
    # Test 1: Simple palindrome
    assert is_palindrome("racecar") == True, "Test 1 failed"
    print("✓ Test 1 passed: 'racecar' is a palindrome")
    
    # Test 2: Non-palindrome
    assert is_palindrome("hello") == False, "Test 2 failed"
    print("✓ Test 2 passed: 'hello' is not a palindrome")
    
    # Test 3: Palindrome with spaces and mixed case
    assert is_palindrome("A man a plan a canal Panama") == True, "Test 3 failed"
    print("✓ Test 3 passed: 'A man a plan a canal Panama' is a palindrome")
    
    # Test 4: Empty string
    assert is_palindrome("") == True, "Test 4 failed"
    print("✓ Test 4 passed: Empty string is a palindrome")
    
    # Test 5: Single character
    assert is_palindrome("a") == True, "Test 5 failed"
    print("✓ Test 5 passed: Single character is a palindrome")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    print("Running Palindrome Checker Tests...\n")
    test_palindrome()