\"\"\"
Exercise 14: Exception Handling
Topic: Error Handling
Difficulty: Medium

Problem Statement:
Write a function that safely divides two numbers and handles various exceptions.
The function should handle:
- Division by zero
- Invalid input types (non-numeric)
- Any other unexpected errors

Solution:
\"\"\"
def safe_divide(a, b):
    """
    Safely divide two numbers and handle exceptions.
    
    Args:
        a: Dividend (should be numeric)
        b: Divisor (should be numeric)
        
    Returns:
        Result of division or None if an error occurs
    """
    try:
        # Attempt to convert to float (handles int, float, and string representations)
        num1 = float(a)
        num2 = float(b)
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except (ValueError, TypeError) as e:
        print(f"Error: Invalid input - {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    # Test the function with various inputs
    test_cases = [
        (10, 2),
        (5, 0),
        ("10", "2"),
        ("abc", 2),
        (10, "def"),
        (None, 5)
    ]
    
    for a, b in test_cases:
        result = safe_divide(a, b)
        print(f"safe_divide({a}, {b}) = {result}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Normal division
    assert safe_divide(10, 2) == 5.0, "Test 1 failed"
    print("Test Case 1 Passed: 10/2 = 5.0")
    
    # Test Case 2: Division by zero
    assert safe_divide(5, 0) is None, "Test 2 failed"
    print("Test Case 2 Passed: Division by zero returns None")
    
    # Test Case 3: String numbers
    assert safe_divide("10", "2") == 5.0, "Test 3 failed"
    print("Test Case 3 Passed: '10'/'2' = 5.0")
    
    # Test Case 4: Invalid string
    assert safe_divide("abc", 2) is None, "Test 4 failed"
    print("Test Case 4 Passed: 'abc'/2 returns None")
    
    # Test Case 5: None input
    assert safe_divide(None, 5) is None, "Test 5 failed"
    print("Test Case 5 Passed: None/5 returns None")
    
    # Test Case 6: Both invalid
    assert safe_divide("x", "y") is None, "Test 6 failed"
    print("Test Case 6 Passed: 'x'/'y' returns None")
    
    print("\\nAll tests passed!")