"""
Exercise 8: Generate Parentheses
=================================

Problem Statement:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

Approach:
Use backtracking recursion:
1. Keep track of open and close parentheses counts
2. Add open parenthesis if count < n
3. Add close parenthesis if count < open count
4. When both counts reach n, we have a valid combination

Time Complexity: O(4^n / sqrt(n)) - Catalan number
Space Complexity: O(4^n / sqrt(n)) for output + O(n) for recursion stack
"""

def generate_parenthesis(n):
    """
    Generate all combinations of well-formed parentheses.
    
    Args:
        n (int): Number of pairs of parentheses
        
    Returns:
        List[str]: All valid combinations of parentheses
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        """
        Recursive helper to build valid parentheses combinations.
        
        Args:
            current (str): Current combination being built
            open_count (int): Number of open parentheses used
            close_count (int): Number of close parentheses used
        """
        # Base case: we've used all n pairs
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add open parenthesis if we haven't used all n
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # Add close parenthesis if it won't make string invalid
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

# Test cases
def test_generate_parenthesis():
    # Test case 1: n = 3
    n1 = 3
    expected1 = ["((()))","(()())","(())()","()(())","()()()"]
    result1 = generate_parenthesis(n1)
    assert set(result1) == set(expected1), f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: n = 1
    n2 = 1
    expected2 = ["()"]
    result2 = generate_parenthesis(n2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: n = 2
    n3 = 2
    expected3 = ["(())", "()()"]
    result3 = generate_parenthesis(n3)
    assert set(result3) == set(expected3), f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_generate_parenthesis()