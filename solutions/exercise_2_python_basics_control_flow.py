\"\"\"
Exercise 2: Python Basics - Control Flow and Functions
Difficulty: Medium
Topic: Python Fundamentals

Problem Statement:
Write a Python script that:
1. Defines a function to calculate the factorial of a number using iteration
2. Defines a function to check if a number is prime
3. Uses a loop to print the first 10 Fibonacci numbers
4. Demonstrates conditional statements (if-elif-else) for grading scores

Expected Output:
Factorial of 5: 120
Is 17 prime? True
First 10 Fibonacci numbers: 0 1 1 2 3 5 8 13 21 34
Score: 85 -> Grade: B
\"\"\"

def factorial(n):
    """
    Calculate factorial of a number iteratively.
    Args:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(num):
    """
    Check if a number is prime.
    Args:
        num (int): Integer to check
    Returns:
        bool: True if prime, False otherwise
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    """
    Generate first n Fibonacci numbers.
    Args:
        n (int): Number of Fibonacci numbers to generate
    Returns:
        list: List containing first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[:n]

def get_grade(score):
    """
    Convert numeric score to letter grade.
    Args:
        score (float): Score between 0 and 100
    Returns:
        str: Letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main execution
if __name__ == "__main__":
    # Test factorial
    fact_5 = factorial(5)
    print(f"Factorial of 5: {fact_5}")
    
    # Test prime check
    num = 17
    prime_check = is_prime(num)
    print(f"Is {num} prime? {prime_check}")
    
    # Test Fibonacci
    fib_numbers = fibonacci(10)
    print("First 10 Fibonacci numbers:", " ".join(map(str, fib_numbers)))
    
    # Test grading
    score = 85
    grade = get_grade(score)
    print(f"Score: {score} -> Grade: {grade}")
    
    # Test cases
    assert factorial(5) == 120, "Factorial test failed"
    assert is_prime(17) == True, "Prime test failed"
    assert is_prime(18) == False, "Prime test failed"
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "Fibonacci test failed"
    assert get_grade(85) == "B", "Grade test failed"
    assert get_grade(92) == "A", "Grade test failed"
    assert get_grade(59) == "F", "Grade test failed"
    
    print("\nAll tests passed!")