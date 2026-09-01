\"\"\"
Exercise 5: Climbing Stairs

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
\"\"\"

def climb_stairs_recursive(n):
    \"\"\"
    Calculate the number of distinct ways to climb stairs using recursion.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(2^n)
    Space Complexity: O(n) due to recursion stack
    \"\"\"
    # Base cases
    if n <= 2:
        return n
    
    # Recursive case: ways to reach step n is the sum of ways to reach
    # step n-1 (then take 1 step) and ways to reach step n-2 (then take 2 steps)
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

def climb_stairs_memoization(n):
    \"\"\"
    Calculate the number of distinct ways to climb stairs using memoization.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    \"\"\"
    # Memoization cache
    memo = {}
    
    def helper(steps):
        # Check if already computed
        if steps in memo:
            return memo[steps]
        
        # Base cases
        if steps <= 2:
            return steps
        
        # Compute and store result
        memo[steps] = helper(steps - 1) + helper(steps - 2)
        return memo[steps]
    
    return helper(n)

def climb_stairs_dp(n):
    \"\"\"
    Calculate the number of distinct ways to climb stairs using dynamic programming.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    \"\"\"
    if n <= 2:
        return n
    
    # dp[i] represents number of ways to reach step i
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1
    dp[2] = 2  # Two ways to reach step 2
    
    # Fill the dp array
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climb_stairs_optimized(n):
    \"\"\"
    Calculate the number of distinct ways to climb stairs with optimized space.
    
    Args:
        n (int): Number of steps to climb
    
    Returns:
        int: Number of distinct ways to climb to the top
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    \"\"\"
    if n <= 2:
        return n
    
    # We only need the previous two values
    prev2 = 1  # Ways to reach step 1
    prev1 = 2  # Ways to reach step 2
    
    # Calculate for each step from 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test cases
if __name__ == \"__main__\": 
    # Test case 1
    n1 = 2
    result1 = climb_stairs_dp(n1)
    print(f\"Test 1: n = {n1}\")
    print(f\"Expected: 2, Got: {result1}\")
    assert result1 == 2
    
    # Test case 2
    n2 = 3
    result2 = climb_stairs_dp(n2)
    print(f\"\\nTest 2: n = {n2}\")
    print(f\"Expected: 3, Got: {result2}\")
    assert result2 == 3
    
    # Test case 3
    n3 = 5
    result3 = climb_stairs_dp(n3)
    print(f\"\\nTest 3: n = {n3}\")
    print(f\"Expected: 8, Got: {result3}\")
    assert result3 == 8
    
    # Compare all approaches for small n
    n4 = 10
    recursive_result = climb_stairs_recursive(n4) if n4 <= 10 else \"Too slow for large n\"
    memo_result = climb_stairs_memoization(n4)
    dp_result = climb_stairs_dp(n4)
    opt_result = climb_stairs_optimized(n4)
    
    print(f\"\\nComparison for n = {n4}:\")
    print(f\"Recursive: {recursive_result}\")
    print(f\"Memoization: {memo_result}\")
    print(f\"DP: {dp_result}\")
    print(f\"Optimized: {opt_result}\")
    
    # Verify all methods give the same result
    if isinstance(recursive_result, int):
        assert recursive_result == memo_result == dp_result == opt_result
    else:
        assert memo_result == dp_result == opt_result
    
    print(\"\\nAll tests passed!\")