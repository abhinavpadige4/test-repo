"""
Exercise 6: Climbing Stairs
===========================

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Approach:
This is a classic dynamic programming problem that follows the Fibonacci sequence.
For step i, the number of ways to reach it is equal to:
ways(i) = ways(i-1) + ways(i-2)

We can solve this using bottom-up DP with optimized space complexity.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n):
    """
    Calculate the number of distinct ways to climb to the top of n steps.
    
    Args:
        n (int): Number of steps
        
    Returns:
        int: Number of distinct ways to climb to the top
    """
    if n <= 2:
        return n
    
    # prev2 represents ways to reach step i-2
    # prev1 represents ways to reach step i-1
    prev2, prev1 = 1, 2
    
    # Calculate for steps 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

# Test cases
def test_climb_stairs():
    # Test case 1: n = 2
    n1 = 2
    expected1 = 2
    result1 = climb_stairs(n1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: n = 3
    n2 = 3
    expected2 = 3
    result2 = climb_stairs(n2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: n = 5
    n3 = 5
    expected3 = 8
    result3 = climb_stairs(n3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_climb_stairs()