\"\"\"
Exercise 3: Simple Calculator
Topic: Functions and User Input
Difficulty: Easy

Problem Statement:
Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

Solution:
\"\"\"
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            
            next_calculation = input("Do another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    import io
    import sys
    
    # We'll test the functions directly
    # Test Case 1: Addition
    assert add(5, 3) == 8, "Addition failed"
    print("Test Case 1 Passed: Addition")
    
    # Test Case 2: Subtraction
    assert subtract(5, 3) == 2, "Subtraction failed"
    print("Test Case 2 Passed: Subtraction")
    
    # Test Case 3: Multiplication
    assert multiply(5, 3) == 15, "Multiplication failed"
    print("Test Case 3 Passed: Multiplication")
    
    # Test Case 4: Division
    assert divide(6, 3) == 2.0, "Division failed"
    print("Test Case 4 Passed: Division")
    
    # Test Case 5: Division by zero
    assert divide(5, 0) == "Error! Division by zero.", "Division by zero handling failed"
    print("Test Case 5 Passed: Division by zero")
    
    print("\\nAll unit tests passed!")
    # Note: The interactive part is not tested in unit tests for simplicity.
    print("To test the interactive calculator, run the program and follow the prompts.")