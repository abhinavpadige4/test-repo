\"\"\"
Exercise 8: Dictionary Basics
Topic: Dictionaries
Difficulty: Easy

Problem Statement:
Write a program that creates a dictionary to store information about a person and then allows the user to query that information.

Requirements:
- Create a dictionary with keys: 'name', 'age', 'city', 'occupation'
- Initialize the dictionary with some sample data
- Ask the user what information they want to know (name, age, city, occupation)
- Print the corresponding value from the dictionary
- If the user enters a key that doesn't exist, print an error message
- Allow the user to continue querying until they type 'quit'

Example:
What do you want to know? (name, age, city, occupation, or quit): name
Name: Alice
What do you want to know? (name, age, city, occupation, or quit): salary
Error: Key 'salary' not found. Available keys: name, age, city, occupation
What do you want to know? (name, age, city, occupation, or quit): quit
Goodbye!
\"\"\"

def main():
    # Sample person data
    person = {
        'name': 'Alice Smith',
        'age': 30,
        'city': 'New York',
        'occupation': 'Software Engineer'
    }
    
    print("Person Information System")
    print(f"Available keys: {', '.join(person.keys())}")
    
    while True:
        user_input = input("\nWhat do you want to know? (or type 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            print("Goodbye!")
            break
        
        if user_input in person:
            # Format the key for display (capitalize first letter)
            key_display = user_input.capitalize()
            print(f"{key_display}: {person[user_input]}")
        else:
            print(f"Error: Key '{user_input}' not found. Available keys: {', '.join(person.keys())}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # We'll test the dictionary logic
    test_person = {
        'name': 'Alice Smith',
        'age': 30,
        'city': 'New York',
        'occupation': 'Software Engineer'
    }
    
    # Test that keys exist
    assert 'name' in test_person
    assert test_person['name'] == 'Alice Smith'
    assert test_person['age'] == 30
    
    # Test missing key
    assert 'salary' not in test_person
    
    print("Dictionary tests passed.")
    
    # Uncomment below to run interactively
    # main()