\"\"\"
Exercise 8: Fibonacci Sequence
Topic: Recursion and Iteration
Difficulty: Medium

Problem Statement:
Write a function that returns the nth Fibonacci number. The Fibonacci sequence is defined as:
F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
Implement both recursive and iterative versions.

Solution:
\"\"\"
def fibonacci_recursive(n):
    """Recursive implementation of Fibonacci."""
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """Iterative implementation of Fibonacci."""
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def main():
    # Test both implementations
    test_values = [0, 1, 2, 5, 10]
    for n in test_values:
        rec = fibonacci_recursive(n)
        it = fibonacci_iterative(n)
        print(f"Fibonacci({n}) -> Recursive: {rec}, Iterative: {it}")
        assert rec == it, f"Mismatch at n={n}"

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: n=0
    assert fibonacci_recursive(0) == 0 and fibonacci_iterative(0) == 0, "Test 1 failed"
    print("Test Case 1 Passed: n=0")
    
    # Test Case 2: n=1
    assert fibonacci_recursive(1) == 1 and fibonacci_iterative(1) == 1, "Test 2 failed"
    print("Test Case 2 Passed: n=1")
    
    # Test Case 3: n=5
    assert fibonacci_recursive(5) == 5 and fibonacci_iterative(5) == 5, "Test 3 failed"
    print("Test Case 3 Passed: n=5")
    
    # Test Case 4: n=10
    assert fibonacci_recursive(10) == 55 and fibonacci_iterative(10) == 55, "Test 4 failed"
    print("Test Case 4 Passed: n=10")
    
    # Test Case 5: Negative input
    try:
        fibonacci_recursive(-1)
        assert False, "Test 5 failed: Expected ValueError"
    except ValueError:
        pass
    try:
        fibonacci_iterative(-1)
        assert False, "Test 5 failed: Expected ValueError"
    except ValueError:
        print("Test Case 5 Passed: Negative input raises ValueError")
    
    print("\\nAll tests passed!")