"""
Exercise 20: Burst Balloons
===========================

Problem Statement:
You are given n balloons, indexed from 0 to n - 1. Each balloon has a number painted on it.
If you burst the ith balloon, you get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds, treat it as a balloon with value 1.

Return the maximum coins you can collect by bursting all the balloons optimally.

Example:
Input: nums = [3,1,5,8]
Output: 167

Approach:
Dynamic Programming with interval DP:
- Instead of thinking which balloon to burst first, think which balloon to burst last
- For subarray from i to j, try each k as the last balloon to burst
- When k is last to burst, we get nums[i-1] * nums[k] * nums[j+1] plus coins from left and right parts
- dp[i][j] = max(dp[i][k-1] + nums[i-1] * nums[k] * nums[j+1] + dp[k+1][j]) for all k in [i,j]

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

def max_coins(nums):
    """
    Calculate maximum coins obtainable by bursting balloons optimally.
    
    Args:
        nums (List[int]): Array of balloon values
        
    Returns:
        int: Maximum coins possible
    """
    # Add boundary 1s to handle edge cases
    nums = [1] + nums + [1]
    n = len(nums)
    
    # dp[i][j] represents max coins for balloons in range i to j (exclusive of boundaries)
    dp = [[0] * n for _ in range(n)]
    
    # Length of subarray (excluding boundaries)
    for length in range(1, n - 1):
        # Start index
        for i in range(1, n - length):
            # End index
            j = i + length - 1
            
            # Try each balloon k as the last to burst in range i to j
            for k in range(i, j + 1):
                # Coins from bursting balloon k last in range i to j
                # nums[i-1] * nums[k] * nums[j+1] + coins from left + coins from right
                coins = (dp[i][k - 1] + 
                        nums[i - 1] * nums[k] * nums[j + 1] + 
                        dp[k + 1][j])
                dp[i][j] = max(dp[i][j], coins)
    
    # Return max coins for entire array (excluding boundary 1s)
    return dp[1][n - 2]

# Recursive + Memoization approach (alternative implementation)
def max_coins_memo(nums):
    """
    Calculate maximum coins using recursive approach with memoization.
    
    Args:
        nums (List[int]): Array of balloon values
        
    Returns:
        int: Maximum coins possible
    """
    # Add boundary 1s
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Memoization table
    memo = [[0] * n for _ in range(n)]
    
    def burst(left, right):
        """
        Calculate max coins for range (left, right) exclusive.
        
        Args:
            left (int): Left boundary (exclusive)
            right (int): Right boundary (exclusive)
            
        Returns:
            int: Max coins for range
        """
        # Base case
        if left + 1 == right:
            return 0
        
        # Check memo
        if memo[left][right] > 0:
            return memo[left][right]
        
        # Try each balloon as last to burst
        max_coins = 0
        for i in range(left + 1, right):
            # Coins from bursting balloon i last
            coins = (burst(left, i) + 
                    nums[left] * nums[i] * nums[right] + 
                    burst(i, right))
            max_coins = max(max_coins, coins)
        
        memo[left][right] = max_coins
        return max_coins
    
    return burst(0, n - 1)

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Example case
    nums1 = [3, 1, 5, 8]
    result1 = max_coins(nums1)
    print(f"Test 1: {nums1} -> Max coins: {result1}")  # Expected: 167
    
    # Test Case 2: Two balloons
    nums2 = [1, 5]
    result2 = max_coins(nums2)
    print(f"Test 2: {nums2} -> Max coins: {result2}")  # Expected: 10
    
    # Test Case 3: Single balloon
    nums3 = [3]
    result3 = max_coins(nums3)
    print(f"Test 3: {nums3} -> Max coins: {result3}")  # Expected: 3
    
    # Test Case 4: Increasing sequence
    nums4 = [1, 2, 3]
    result4 = max_coins(nums4)
    print(f"Test 4: {nums4} -> Max coins: {result4}")  # Expected: 12
    
    # Test Case 5: Using memoization approach
    nums5 = [3, 1, 5, 8]
    result5 = max_coins_memo(nums5)
    print(f"Test 5: {nums5} -> Max coins (memo): {result5}")  # Expected: 167