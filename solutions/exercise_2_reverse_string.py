"""
Exercise 2: Reverse a String
Topic: String Manipulation
Difficulty: Easy

Problem Statement:
Write a function that takes a string as input and returns the string reversed.
Do not use Python's built-in reversed() or slicing with [::-1] for the main logic.
Instead, implement the reversal manually.

Solution:
We can reverse a string by iterating from the end to the beginning and building a new string.
Alternatively, we can convert to a list, swap characters in-place, and convert back.
"""

def reverse_string(s):
    """
    Reverse a string manually.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
        >>> reverse_string("a")
        'a'
    """
    # Convert string to list for in-place modification (if we want to avoid extra space for string building)
    # But since strings are immutable, we'll build a new string
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    return ''.join(reversed_chars)

# Alternative implementation using two-pointer technique on a list
def reverse_string_inplace(s):
    """
    Reverse a string by converting to list, swapping in-place, and converting back.
    This demonstrates the two-pointer technique.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    if len(s) <= 1:
        return s
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return ''.join(s_list)

# Test cases
if __name__ == "__main__":
    # Test case 1: Normal string
    test1 = reverse_string("hello")
    print(f"Test 1 - reverse_string('hello'): '{test1}' (Expected: 'olleh')")
    
    # Test case 2: Empty string
    test2 = reverse_string("")
    print(f"Test 2 - reverse_string(''): '{test2}' (Expected: '')")
    
    # Test case 3: Single character
    test3 = reverse_string("a")
    print(f"Test 3 - reverse_string('a'): '{test3}' (Expected: 'a')")
    
    # Test case 4: Palindrome
    test4 = reverse_string("racecar")
    print(f"Test 4 - reverse_string('racecar'): '{test4}' (Expected: 'racecar')")
    
    # Test case 5: String with spaces
    test5 = reverse_string("hello world")
    print(f"Test 5 - reverse_string('hello world'): '{test5}' (Expected: 'dlrow olleh')")
    
    # Verify with alternative implementation
    print("\nVerifying with in-place method:")
    print(f"reverse_string_inplace('hello'): '{reverse_string_inplace('hello')}'")

"""
Time Complexity: O(n) - We iterate through the string once.
Space Complexity: O(n) - We build a new string of length n.
(The in-place version uses O(n) for the list conversion, but O(1) extra space if we consider the list as mutable input - 
 however, in Python strings are immutable so we cannot truly do in-place without conversion.)
"""