"""
Exercise 13: Coin Change (Medium)
Problem Statement:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Examples:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

def coin_change(coins, amount):
    """
    Find the minimum number of coins needed to make up the given amount using dynamic programming.
    
    Args:
        coins (List[int]): Denominations of available coins
        amount (int): Target amount to make up
    
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # dp[i] will store the minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0
    
    # For each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value is less than or equal to current amount
            if coin <= i:
                # Update dp[i] with minimum of current value and 1 + dp[i - coin]
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return the result or -1 if impossible
    return dp[amount] if dp[amount] != float('inf') else -1

# Recursive approach with memoization
def coin_change_memo(coins, amount):
    """
    Find minimum coins using recursion with memoization.
    
    Args:
        coins (List[int]): Denominations of available coins
        amount (int): Target amount to make up
    
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
    """
    memo = {}
    
    def helper(amt):
        if amt in memo:
            return memo[amt]
        
        if amt == 0:
            return 0
        
        if amt < 0:
            return -1
        
        min_coins = float('inf')
        
        for coin in coins:
            result = helper(amt - coin)
            if result != -1:
                min_coins = min(min_coins, result + 1)
        
        memo[amt] = min_coins if min_coins != float('inf') else -1
        return memo[amt]
    
    return helper(amount)

# BFS approach
from collections import deque

def coin_change_bfs(coins, amount):
    """
    Find minimum coins using BFS approach.
    
    Args:
        coins (List[int]): Denominations of available coins
        amount (int): Target amount to make up
    
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
        
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    if amount == 0:
        return 0
    
    # Queue stores (current_amount, number_of_coins_used)
    queue = deque([(0, 0)])
    # Visited set to avoid processing same amount multiple times
    visited = set([0])
    
    while queue:
        current_amount, num_coins = queue.popleft()
        
        # Try each coin denomination
        for coin in coins:
            new_amount = current_amount + coin
            
            # If we've reached the target amount
            if new_amount == amount:
                return num_coins + 1
            
            # If new amount is valid and not visited
            if new_amount < amount and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))
    
    return -1

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = coin_change(coins1, amount1)
    print(f"Test 1 - Coins: {coins1}, Amount: {amount1}")
    print(f"Output: {result1}")
    print(f"Expected: 3")
    print(f"Pass: {result1 == 3}\\n")
    
    # Test Case 2
    coins2 = [2]
    amount2 = 3
    result2 = coin_change(coins2, amount2)
    print(f"Test 2 - Coins: {coins2}, Amount: {amount2}")
    print(f"Output: {result2}")
    print(f"Expected: -1")
    print(f"Pass: {result2 == -1}\\n")
    
    # Test Case 3
    coins3 = [1]
    amount3 = 0
    result3 = coin_change(coins3, amount3)
    print(f"Test 3 - Coins: {coins3}, Amount: {amount3}")
    print(f"Output: {result3}")
    print(f"Expected: 0")
    print(f"Pass: {result3 == 0}\\n")
    
    # Test Case 4
    coins4 = [1, 2, 5]
    amount4 = 7
    result4 = coin_change(coins4, amount4)
    print(f"Test 4 - Coins: {coins4}, Amount: {amount4}")
    print(f"Output: {result4}")
    print(f"Expected: 2")  # 5 + 2 = 7
    print(f"Pass: {result4 == 2}\\n")
    
    # Test Case 5
    coins5 = [2, 5, 10, 1]
    amount5 = 27
    result5 = coin_change_memo(coins5, amount5)
    print(f"Test 5 - Coins: {coins5}, Amount: {amount5}")
    print(f"Output: {result5}")
    print(f"Expected: 4")  # 10 + 10 + 5 + 2 = 27
    print(f"Pass: {result5 == 4}\\n")