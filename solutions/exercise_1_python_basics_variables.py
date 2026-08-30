\"\"\"
Exercise 1: Python Basics - Variables and Data Types
Difficulty: Easy
Topic: Python Fundamentals

Problem Statement:
Write a Python script that:
1. Creates variables of different data types (integer, float, string, boolean)
2. Performs basic arithmetic operations
3. Demonstrates string concatenation and formatting
4. Prints the type of each variable

Expected Output:
Integer: 42, Type: <class 'int'>
Float: 3.14, Type: <class 'float'>
String: Hello, World!, Type: <class 'str'>
Boolean: True, Type: <class 'bool'>
Sum of integer and float: 45.14
Concatenated string: Hello, World! Welcome to Data Science
\"\"\"

def variables_and_data_types():
    """
    Demonstrate Python variables and data types.
    Returns:
        dict: A dictionary containing the variables and their types
    """
    # Integer
    integer_var = 42
    
    # Float
    float_var = 3.14
    
    # String
    string_var = "Hello, World!"
    
    # Boolean
    boolean_var = True
    
    # Arithmetic operations
    sum_result = integer_var + float_var
    
    # String concatenation and formatting
    greeting = string_var + " Welcome to Data Science"
    
    # Print results
    print(f"Integer: {integer_var}, Type: {type(integer_var)}")
    print(f"Float: {float_var}, Type: {type(float_var)}")
    print(f"String: {string_var}, Type: {type(string_var)}")
    print(f"Boolean: {boolean_var}, Type: {type(boolean_var)}")
    print(f"Sum of integer and float: {sum_result}")
    print(f"Concatenated string: {greeting}")
    
    # Return for testing
    return {
        "integer": integer_var,
        "float": float_var,
        "string": string_var,
        "boolean": boolean_var,
        "sum": sum_result,
        "greeting": greeting
    }

# Test cases
if __name__ == "__main__":
    result = variables_and_data_types()
    
    # Test 1: Check integer value
    assert result["integer"] == 42, f"Expected integer 42, got {result['integer']}"
    
    # Test 2: Check float value
    assert abs(result["float"] - 3.14) < 0.001, f"Expected float 3.14, got {result['float']}"
    
    # Test 3: Check string value
    assert result["string"] == "Hello, World!", f"Expected string 'Hello, World!', got {result['string']}"
    
    # Test 4: Check boolean value
    assert result["boolean"] == True, f"Expected boolean True, got {result['boolean']}"
    
    # Test 5: Check sum
    assert abs(result["sum"] - 45.14) < 0.001, f"Expected sum 45.14, got {result['sum']}"
    
    # Test 6: Check greeting
    assert result["greeting"] == "Hello, World! Welcome to Data Science", f"Expected greeting 'Hello, World! Welcome to Data Science', got {result['greeting']}"
    
    print("\nAll tests passed!")

\"\"\"
Time Complexity: O(1) - All operations are constant time
Space Complexity: O(1) - Fixed number of variables
\"\"\"