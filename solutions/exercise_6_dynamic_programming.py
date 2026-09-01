"""
Exercise 6: Climbing Stairs

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
"""

def climb_stairs(n):
    """
    Calculate the number of distinct ways to climb n stairs.
    
    This is a classic dynamic programming problem that follows the Fibonacci sequence.
    For each step i, the number of ways to reach it is the sum of ways to reach (i-1) and (i-2).
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Base cases
    if n <= 2:
        return n
    
    # We only need to keep track of the last two values
    prev2 = 1  # Ways to reach step 1
    prev1 = 2  # Ways to reach step 2
    
    # Calculate for steps 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

def climb_stairs_dp_array(n):
    """
    Calculate the number of distinct ways to climb n stairs using DP array.
    
    Alternative implementation that uses an array to store all intermediate results.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n
    
    # Initialize DP array
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1
    dp[2] = 2  # Two ways to reach step 2
    
    # Fill the DP array
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def climb_stairs_recursive_memo(n):
    """
    Calculate the number of distinct ways to climb n stairs using recursion with memoization.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    memo = {}
    
    def helper(steps):
        if steps in memo:
            return memo[steps]
        
        if steps <= 2:
            return steps
        
        memo[steps] = helper(steps - 1) + helper(steps - 2)
        return memo[steps]
    
    return helper(n)

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    result1 = climb_stairs(n1)
    expected1 = 2
    print(f"Test 1: n={n1} => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    n2 = 3
    result2 = climb_stairs(n2)
    expected2 = 3
    print(f"Test 2: n={n2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    n3 = 5
    result3 = climb_stairs(n3)
    expected3 = 8
    print(f"Test 3: n={n3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Verify all three implementations give the same result for n=10
    n4 = 10
    result4a = climb_stairs(n4)
    result4b = climb_stairs_dp_array(n4)
    result4c = climb_stairs_recursive_memo(n4)
    print(f"Test 4: n={n4} => Method1: {result4a}, Method2: {result4b}, Method3: {result4c}")
    assert result4a == result4b == result4c, "All methods should give the same result"
    
    print("All tests passed!")