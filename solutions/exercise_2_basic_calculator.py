\"\"\"
Exercise 2: Basic Calculator
Topic: Control Flow and Functions
Difficulty: Easy

Problem Statement:
Create a simple calculator that can perform addition, subtraction, multiplication, and division.
The program should:
- Ask the user to enter two numbers
- Ask the user to choose an operation (+, -, *, /)
- Perform the selected operation and display the result
- Handle division by zero by displaying an error message
- Handle invalid operation choices by displaying an error message

Example:
Enter first number: 10
Enter second number: 5
Choose operation (+, -, *, /): *
Result: 10 * 5 = 50
\"\"\"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    \"\"\"Main calculator function.\"\"\"
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return
    
    print("Choose operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    
    operation = input("Enter operation (+, -, *, /): ").strip()
    
    try:
        if operation == '+':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation! Please choose +, -, *, or /")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Test addition
    assert add(2, 3) == 5
    # Test subtraction
    assert subtract(5, 3) == 2
    # Test multiplication
    assert multiply(3, 4) == 12
    # Test division
    assert divide(10, 2) == 5
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("All unit tests passed!")
    print("\nTo run the calculator interactively, uncomment the line below:")
    # calculator()