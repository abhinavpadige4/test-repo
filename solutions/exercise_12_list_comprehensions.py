\"\"\"
Exercise 12: List Comprehensions
Topic: Lists and Comprehensions
Difficulty: Medium

Problem Statement:
Write a program that demonstrates the power of list comprehensions by solving several common tasks.

The program should:
1. Create a list of squares of numbers from 1 to 10 using list comprehension.
2. Create a list of even numbers from a given list using list comprehension.
3. Create a list of lengths of strings in a given list using list comprehension.
4. Create a list of tuples (number, square) for numbers from 1 to 5 using list comprehension.
5. Flatten a list of lists using list comprehension.

Example:
Input for task 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [2, 4, 6, 8, 10]

Input for task 3: ['apple', 'banana', 'cherry']
Output: [5, 6, 6]

\"\"\"

def task1_squares(n):
    \"\"\"Return a list of squares from 1 to n using list comprehension.\"\"\"
    return [x**2 for x in range(1, n+1)]

def task2_evens(numbers):
    \"\"\"Return a list of even numbers from the input list using list comprehension.\"\"\"
    return [x for x in numbers if x % 2 == 0]

def task3_string_lengths(strings):
    \"\"\"Return a list of lengths of strings in the input list using list comprehension.\"\"\"
    return [len(s) for s in strings]

def task4_number_square_tuples(n):
    \"\"\"Return a list of tuples (number, square) for numbers from 1 to n using list comprehension.\"\"\"
    return [(x, x**2) for x in range(1, n+1)]

def task5_flatten(list_of_lists):
    \"\"\"Flatten a list of lists using list comprehension.\"\"\"
    return [item for sublist in list_of_lists for item in sublist]

def main():
    print("List Comprehensions Demo")
    print("=" * 30)
    
    # Task 1
    squares = task1_squares(10)
    print(f"1. Squares from 1 to 10: {squares}")
    
    # Task 2
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = task2_evens(numbers)
    print(f"2. Even numbers from {numbers}: {evens}")
    
    # Task 3
    strings = ['apple', 'banana', 'cherry']
    lengths = task3_string_lengths(strings)
    print(f"3. Lengths of {strings}: {lengths}")
    
    # Task 4
    tuples = task4_number_square_tuples(5)
    print(f"4. Number-square tuples up to 5: {tuples}")
    
    # Task 5
    nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    flattened = task5_flatten(nested)
    print(f"5. Flattened {nested}: {flattened}")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Task 1
    assert task1_squares(5) == [1, 4, 9, 16, 25]
    # Task 2
    assert task2_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    # Task 3
    assert task3_string_lengths(['a', 'ab', 'abc']) == [1, 2, 3]
    # Task 4
    assert task4_number_square_tuples(3) == [(1, 1), (2, 4), (3, 9)]
    # Task 5
    assert task5_flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    
    print("All unit tests passed!")
    
    # Uncomment below to run the demo
    # main()