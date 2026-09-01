\"\"\"
Exercise 9: Valid Parentheses
Topic: Stack
Difficulty: Medium

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Solution:
\"\"\"
def is_valid_parentheses(s):
    """
    Return True if the input string is valid, False otherwise.
    
    Args:
        s (str): Input string containing only parentheses characters
    
    Returns:
        bool: True if valid, False otherwise
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Top element of stack if not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

# Test cases
if __name__ == "__main__":
    # Test Case 1: Simple valid
    print(f"Test Case 1: is_valid_parentheses('()') = {is_valid_parentheses('()')}")  # Expected: True
    
    # Test Case 2: Multiple types
    print(f"Test Case 2: is_valid_parentheses('()[]{{}}') = {is_valid_parentheses('()[]{{}}')}")  # Expected: True
    
    # Test Case 3: Invalid (wrong order)
    print(f"Test Case 3: is_valid_parentheses('(]') = {is_valid_parentheses('(]')}")  # Expected: False
    
    # Test Case 4: Invalid (mismatched)
    print(f"Test Case 4: is_valid_parentheses('([)]') = {is_valid_parentheses('([)')}")  # Expected: False
    
    # Test Case 5: Empty string
    print(f"Test Case 5: is_valid_parentheses('') = {is_valid_parentheses('')}")  # Expected: True

# Complexity Analysis:
# Time Complexity: O(n) - where n is the length of the string
# Space Complexity: O(n) - for the stack in the worst case