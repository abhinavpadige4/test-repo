\"\"\"
Exercise 7: Fibonacci Sequence
Topic: Loops and Recursion
Difficulty: Medium

Problem Statement:
Write a program that prints the Fibonacci sequence up to a given number of terms.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

Requirements:
- Ask the user to enter the number of terms (n) they want in the Fibonacci sequence
- Validate that n is a positive integer
- Generate and display the Fibonacci sequence up to n terms
- Handle edge cases: n = 0, n = 1, n = 2

Example:
Input: 7
Output: Fibonacci sequence up to 7 terms: 0, 1, 1, 2, 3, 5, 8

Input: 1
Output: Fibonacci sequence up to 1 term: 0
\"\"\"

def fibonacci_iterative(n):
    \"\"\"Return a list containing the Fibonacci sequence up to n terms (iterative approach).\"\"\"
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_term)
    return fib_sequence

def fibonacci_recursive(n):
    \"\"\"Return the nth Fibonacci number (recursive approach).\"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def main():
    try:
        n = int(input("Enter the number of terms: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    fib_sequence = fibonacci_iterative(n)
    if not fib_sequence:
        print("Fibonacci sequence up to 0 terms: ")
    else:
        print(f"Fibonacci sequence up to {n} terms: {', '.join(map(str, fib_sequence))}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Test iterative function
    assert fibonacci_iterative(0) == []
    assert fibonacci_iterative(1) == [0]
    assert fibonacci_iterative(2) == [0, 1]
    assert fibonacci_iterative(5) == [0, 1, 1, 2, 3]
    assert fibonacci_iterative(7) == [0, 1, 1, 2, 3, 5, 8]
    
    # Test recursive function for individual terms
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2
    assert fibonacci_recursive(4) == 3
    assert fibonacci_recursive(5) == 5
    assert fibonacci_recursive(6) == 8
    
    print("All unit tests passed!")
    
    # Uncomment below to run interactively
    # main()