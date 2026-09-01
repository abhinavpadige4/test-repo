"""
Exercise 3: FizzBuzz
Topic: Control Flow & Loops
Difficulty: Easy

Problem Statement:
Write a program that prints the numbers from 1 to n. But for multiples of three print "Fizz" instead of the number, for multiples of five print "Buzz", and for numbers which are multiples of both three and five print "FizzBuzz".

Solution:
Iterate from 1 to n, check divisibility by 3 and 5 using modulo operator.
"""

def fizzbuzz(n):
    """
    Generate FizzBuzz sequence up to n.
    
    Args:
        n (int): The upper limit (inclusive)
        
    Returns:
        list: A list of strings representing the FizzBuzz sequence
        
    Examples:
        >>> fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: n = 5
    test1 = fizzbuzz(5)
    expected1 = ['1', '2', 'Fizz', '4', 'Buzz']
    print(f"Test 1 - fizzbuzz(5): {test1}")
    print(f"Expected: {expected1}")
    print(f"Pass: {test1 == expected1}\n")
    
    # Test case 2: n = 15 (first FizzBuzz at 15)
    test2 = fizzbuzz(15)
    expected2 = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    print(f"Test 2 - fizzbuzz(15): {test2}")
    print(f"Expected: {expected2}")
    print(f"Pass: {test2 == expected2}\n")
    
    # Test case 3: n = 1
    test3 = fizzbuzz(1)
    expected3 = ['1']
    print(f"Test 3 - fizzbuzz(1): {test3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {test3 == expected3}\n")
    
    # Print the sequence for n=20 for visual verification
    print("FizzBuzz sequence for n=20:")
    for item in fizzbuzz(20):
        print(item, end=' ')
    print()

"""
Time Complexity: O(n) - We iterate through n numbers once.
Space Complexity: O(n) - We store n strings in the result list.
"""