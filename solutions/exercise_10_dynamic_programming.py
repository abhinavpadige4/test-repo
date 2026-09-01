"""
Exercise 10: Climbing Stairs (Medium)
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
    Calculate the number of distinct ways to climb to the top of stairs using dynamic programming.
    
    This is essentially finding the (n+1)th Fibonacci number.
    
    Args:
        n (int): Number of steps to reach the top
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Base cases
    if n <= 2:
        return n
    
    # Use only two variables to store previous results (space optimization)
    prev2 = 1  # Ways to reach step 1
    prev1 = 2  # Ways to reach step 2
    
    # Calculate for steps 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Recursive approach with memoization
def climb_stairs_memo(n, memo={}):
    """
    Calculate the number of distinct ways using recursion with memoization.
    
    Args:
        n (int): Number of steps to reach the top
        memo (dict): Memoization dictionary to store computed results
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Base cases
    if n <= 2:
        return n
    
    # Compute and store result
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]

# Tabulation approach
def climb_stairs_tabulation(n):
    """
    Calculate the number of distinct ways using tabulation (bottom-up DP).
    
    Args:
        n (int): Number of steps to reach the top
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return n
    
    # Create dp array to store number of ways to reach each step
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1
    dp[2] = 2  # Two ways to reach step 2
    
    # Fill dp array bottom-up
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    result1 = climb_stairs(n1)
    print(f"Test 1 - Input: n = {n1}")
    print(f"Output: {result1}")
    print(f"Expected: 2")
    print(f"Pass: {result1 == 2}\\n")
    
    # Test Case 2
    n2 = 3
    result2 = climb_stairs(n2)
    print(f"Test 2 - Input: n = {n2}")
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print(f"Pass: {result2 == 3}\\n")
    
    # Test Case 3
    n3 = 5
    result3 = climb_stairs(n3)
    print(f"Test 3 - Input: n = {n3}")
    print(f"Output: {result3}")
    print(f"Expected: 8")
    print(f"Pass: {result3 == 8}\\n")
    
    # Test Case 4
    n4 = 10
    result4 = climb_stairs(n4)
    print(f"Test 4 - Input: n = {n4}")
    print(f"Output: {result4}")
    print(f"Expected: 89")
    print(f"Pass: {result4 == 89}\\n")
    
    # Test memoization approach
    n5 = 7
    result5 = climb_stairs_memo(n5)
    print(f"Memoization Test - Input: n = {n5}")
    print(f"Output: {result5}")
    print(f"Expected: 21")
    print(f"Pass: {result5 == 21}\\n")