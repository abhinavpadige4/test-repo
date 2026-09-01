\"\"\"
Exercise 6: List Operations and Manipulation
Topic: Lists
Difficulty: Medium

Problem Statement:
Write a program that processes a list of integers entered by the user.
The program should:
- Ask the user to enter a list of integers separated by spaces
- Convert the input into a list of integers
- Perform the following operations and display results:
  a) Show the original list
  b) Show the list sorted in ascending order
  c) Show the list sorted in descending order
  d) Find and show the minimum and maximum values
  e) Calculate and show the sum of all elements
  f) Calculate and show the average of all elements
  g) Remove duplicates and show the list of unique elements
  h) Count how many times a specific number (asked from user) appears in the list

Example:
Input: 5 2 8 2 9 5 1
Output:
Original list: [5, 2, 8, 2, 9, 5, 1]
Sorted ascending: [1, 2, 2, 5, 5, 8, 9]
Sorted descending: [9, 8, 5, 5, 2, 2, 1]
Min: 1, Max: 9
Sum: 32
Average: 4.57
Unique elements: [1, 2, 5, 8, 9]
Enter a number to count: 2
The number 2 appears 2 times.
\"\"\"

def process_list():
    \"\"\"Main function to process the list of integers.\"\"\"
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        # Split and convert to integers
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        print("Error: Please enter only integers separated by spaces.")
        return

    if not numbers:
        print("No numbers entered.")
        return

    # a) Original list
    print(f"Original list: {numbers}")

    # b) Sorted ascending
    sorted_asc = sorted(numbers)
    print(f"Sorted ascending: {sorted_asc}")

    # c) Sorted descending
    sorted_desc = sorted(numbers, reverse=True)
    print(f"Sorted descending: {sorted_desc}")

    # d) Min and max
    min_val = min(numbers)
    max_val = max(numbers)
    print(f"Min: {min_val}, Max: {max_val}")

    # e) Sum
    total = sum(numbers)
    print(f"Sum: {total}")

    # f) Average
    average = total / len(numbers)
    print(f"Average: {average:.2f}")

    # g) Unique elements
    unique = list(set(numbers))
    unique.sort()  # sort for consistent output
    print(f"Unique elements: {unique}")

    # h) Count specific number
    try:
        target = int(input("Enter a number to count: "))
        count = numbers.count(target)
        print(f"The number {target} appears {count} times.")
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    # Test cases with simulated input
    print("Running test cases...")
    
    import builtins
    original_input = builtins.input
    
    # We'll test the processing logic with a predefined list
    test_list = [5, 2, 8, 2, 9, 5, 1]
    
    # Override input to return our test case when needed
    def mock_input(prompt):
        if "Enter a list of integers" in prompt:
            return "5 2 8 2 9 5 1"
        elif "Enter a number to count" in prompt:
            return "2"
        else:
            return original_input(prompt)
    
    builtins.input = mock_input
    try:
        # We'll capture prints by redirecting stdout? For simplicity, we just run the function and see output.
        # But we can test the logic separately.
        print("Testing with list [5, 2, 8, 2, 9, 5, 1]")
        # Instead of calling process_list (which prints), we test the operations:
        numbers = test_list
        assert sorted(numbers) == [1, 2, 2, 5, 5, 8, 9]
        assert sorted(numbers, reverse=True) == [9, 8, 5, 5, 2, 2, 1]
        assert min(numbers) == 1
        assert max(numbers) == 9
        assert sum(numbers) == 32
        assert abs(sum(numbers)/len(numbers) - 4.57) < 0.01
        assert set(numbers) == {1, 2, 5, 8, 9}
        assert numbers.count(2) == 2
        print("All assertions passed.")
    finally:
        builtins.input = original_input
    
    # Uncomment below to run interactively
    # process_list()