"""
Exercise 8: Generate Parentheses
================================

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Approach:
Use backtracking:
1. Start with empty string and count of open/close parentheses
2. At each step, we can add:
   - Open parenthesis if count < n
   - Close parenthesis if count < open count
3. When length = 2*n, we have a valid combination

Time Complexity: O(4^n / sqrt(n)) - Catalan number
Space Complexity: O(4^n / sqrt(n)) for result + O(n) for recursion stack
"""

def generate_parenthesis(n):
    """
    Generate all combinations of well-formed parentheses.
    
    Args:
        n (int): Number of pairs of parentheses
        
    Returns:
        List[str]: All valid combinations
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        # Base case: reached required length
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add open parenthesis if count < n
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # Add close parenthesis if count < open_count
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    n1 = 1
    result1 = generate_parenthesis(n1)
    print(f"Test 1: n={n1} -> {result1}")  # Expected: ["()"]
    
    # Test Case 2: n = 2
    n2 = 2
    result2 = generate_parenthesis(n2)
    print(f"Test 2: n={n2} -> {result2}")  # Expected: ["(())", "()()"]
    
    # Test Case 3: n = 3
    n3 = 3
    result3 = generate_parenthesis(n3)
    print(f"Test 3: n={n3} -> {result3}")  # Expected: ["((()))","(()())","(())()","()(())","()()()"]