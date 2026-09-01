"""
Exercise 6: Climbing Stairs
===========================

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1

Approach:
This is a classic dynamic programming problem (Fibonacci sequence):
- For n=1, there's 1 way
- For n=2, there are 2 ways
- For n>2, ways(n) = ways(n-1) + ways(n-2)

We can solve this with:
1. Recursion (inefficient)
2. Memoization (top-down)
3. Tabulation (bottom-up) - most efficient
4. Space-optimized version

Time Complexity: O(n)
Space Complexity: O(1)
"""

def climb_stairs(n):
    """
    Calculate number of distinct ways to climb n stairs.
    
    Args:
        n (int): Number of stairs
        
    Returns:
        int: Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    # Space-optimized DP approach
    # We only need the last two values
    prev2 = 1  # ways to climb 1 stair
    prev1 = 2  # ways to climb 2 stairs
    
    # Calculate for stairs 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 2
    n1 = 2
    result1 = climb_stairs(n1)
    print(f"Test 1: {n1} stairs -> {result1} ways")  # Expected: 2
    
    # Test Case 2: n = 3
    n2 = 3
    result2 = climb_stairs(n2)
    print(f"Test 2: {n2} stairs -> {result2} ways")  # Expected: 3
    
    # Test Case 3: n = 5
    n3 = 5
    result3 = climb_stairs(n3)
    print(f"Test 3: {n3} stairs -> {result3} ways")  # Expected: 8