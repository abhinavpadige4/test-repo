\"\"\"
Exercise 13: Recursion (Factorial)
Topic: Recursion
Difficulty: Medium

Problem Statement:
Write a program that calculates the factorial of a number using both iterative and recursive methods.
The program should:
- Ask the user to enter a non-negative integer
- Calculate the factorial using an iterative approach (loop)
- Calculate the factorial using a recursive approach
- Display both results and compare
- Handle invalid inputs (negative numbers, non-integers)

Example:
Input: 5
Iterative factorial: 120
Recursive factorial: 120
\"\"\"

def factorial_iterative(n):
    \"\"\"Calculate factorial using iteration.\"\"\"
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    \"\"\"Calculate factorial using recursion.\"\"\"
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

def main():
    while True:
        user_input = input("Enter a non-negative integer: ").strip()
        try:
            n = int(user_input)
            if n < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    try:
        iter_result = factorial_iterative(n)
        recur_result = factorial_recursive(n)
        print(f"Iterative factorial of {n}: {iter_result}")
        print(f"Recursive factorial of {n}: {recur_result}")
        if iter_result == recur_result:
            print("Both methods match!")
        else:
            print("Error: Results do not match!")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Test iterative
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(5) == 120
    assert factorial_iterative(7) == 5040
    
    # Test recursive
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(7) == 5040
    
    # Test error handling
    try:
        factorial_iterative(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    try:
        factorial_recursive(-1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("All unit tests passed!")
    
    # Uncomment below to run interactively
    # main()