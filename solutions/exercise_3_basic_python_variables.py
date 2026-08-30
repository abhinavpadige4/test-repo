\"\"\"
Exercise 3: Basic Python - Variables and Data Types
Topic: Python syntax, data structures
Difficulty: Easy

Problem Statement:
Write a function that takes in a person's name (string) and age (integer) and returns a formatted string: 
\"Hello, [name]. You are [age] years old.\"

Additionally, demonstrate the use of different data types by creating a list, a tuple, a dictionary, and a set.

Solution:
We'll create a function `greet_person` and then show examples of each data type.
\"\"\"

def greet_person(name: str, age: int) -> str:
    \"\"\"Return a greeting message with the person's name and age.\"\"\"
    return f\"Hello, {name}. You are {age} years old.\"

# Demonstrate data types
if __name__ == \"__main__\":
    # Test the function
    message = greet_person(\"Alice\", 30)
    print(message)
    assert message == \"Hello, Alice. You are 30 years old.\"
    
    # List
    my_list = [1, 2, 3, 4, 5]
    print(f\"List: {my_list}\")
    
    # Tuple
    my_tuple = (1, 2, 3)
    print(f\"Tuple: {my_tuple}\")
    
    # Dictionary
    my_dict = {\"name\": \"Bob\", \"age\": 25}
    print(f\"Dictionary: {my_dict}\")
    
    # Set
    my_set = {1, 2, 3, 4, 5}
    print(f\"Set: {my_set}\")
    
    print(\"All tests passed.\")
\"\"\"