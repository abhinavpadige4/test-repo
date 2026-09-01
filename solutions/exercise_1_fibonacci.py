"""
Exercise 1: Fibonacci Sequence
Difficulty: Easy
Topic: Recursion and Dynamic Programming

Problem Statement:
Write a function to calculate the nth Fibonacci number.
The Fibonacci sequence is defined as:
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1

Solution:
We'll implement three approaches:
1. Recursive (naive)
2. Memoized recursive
3. Iterative (optimal)

Time Complexity:
- Recursive: O(2^n)
- Memoized: O(n)
- Iterative: O(n)

Space Complexity:
- Recursive: O(n) for call stack
- Memoized: O(n) for memoization table
- Iterative: O(1)
"""


def fibonacci_recursive(n: int) -> int:
    """Calculate nth Fibonacci number using naive recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n: int, memo: dict = None) -> int:
    """Calculate nth Fibonacci number using memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n: int) -> int:
    """Calculate nth Fibonacci number using iteration (optimal)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# Test cases
def test_fibonacci():
    """Test cases for Fibonacci implementations."""
    # Test case 1: Basic cases
    assert fibonacci_iterative(0) == 0
    assert fibonacci_iterative(1) == 1
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(3) == 2
    assert fibonacci_iterative(4) == 3
    assert fibonacci_iterative(5) == 5
    assert fibonacci_iterative(10) == 55

    # Test case 2: Larger values
    assert fibonacci_iterative(20) == 6765
    assert fibonacci_iterative(30) == 832040

    # Test case 3: Verify all implementations give same results
    for i in range(20):
        assert fibonacci_recursive(i) == fibonacci_iterative(i)
        assert fibonacci_memoized(i) == fibonacci_iterative(i)

    print("All test cases passed!")


if __name__ == "__main__":
    test_fibonacci()
    print(f"Fibonacci(10) = {fibonacci_iterative(10)}")
    print(f"Fibonacci(20) = {fibonacci_iterative(20)}")