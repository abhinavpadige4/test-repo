"""
Exercise: Fibonacci Sequence Generator

Write a function that generates the first n numbers in the Fibonacci sequence.
The Fibonacci sequence starts with 0 and 1, and each subsequent number is the
sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...

Example:
    fibonacci(5) -> [0, 1, 1, 2, 3]
    fibonacci(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
"""

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

# Test cases
if __name__ == "__main__":
    print(fibonacci(5))   # Expected: [0, 1, 1, 2, 3]
    print(fibonacci(8))   # Expected: [0, 1, 1, 2, 3, 5, 8, 13]
    print(fibonacci(1))   # Expected: [0]
    print(fibonacci(0))   # Expected: []