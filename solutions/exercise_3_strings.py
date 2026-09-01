"""
Exercise 3: Valid Parentheses
=============================

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Approach:
Use a stack to track opening brackets:
- When encountering an opening bracket, push it to stack
- When encountering a closing bracket:
  * Check if stack is empty (invalid)
  * Check if top of stack matches the closing bracket (pop if match)
- After processing, stack should be empty for valid string

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    """
    Check if string of parentheses is valid.
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Map of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        # If opening bracket, push to stack
        if char in "({[":
            stack.append(char)
        # If closing bracket
        elif char in ")}]":
            # Check if stack is empty or brackets don't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            # Pop matching opening bracket
            stack.pop()
    
    # Valid if stack is empty
    return len(stack) == 0

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid parentheses
    s1 = "()"
    print(f"Test 1: '{s1}' is valid: {is_valid(s1)}")  # Expected: True
    
    # Test Case 2: Valid nested parentheses
    s2 = "()[]{}"
    print(f"Test 2: '{s2}' is valid: {is_valid(s2)}")  # Expected: True
    
    # Test Case 3: Invalid order
    s3 = "([)]"
    print(f"Test 3: '{s3}' is valid: {is_valid(s3)}")  # Expected: False
    
    # Test Case 4: Valid nested
    s4 = "{[()]}"
    print(f"Test 4: '{s4}' is valid: {is_valid(s4)}")  # Expected: True
    
    # Test Case 5: Unmatched opening
    s5 = "((("
    print(f"Test 5: '{s5}' is valid: {is_valid(s5)}")  # Expected: False