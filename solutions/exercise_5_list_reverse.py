\"\"\"
Exercise 5: List Manipulation - Reverse a List
Topic: Lists
Difficulty: Easy

Problem Statement:
Write a function that takes a list and returns a new list with the elements in reverse order.
Do not use the built-in reverse() or slicing [::-1] for this exercise; use a loop.

Solution:
\"\"\"
def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)  # Insert at the beginning
    return reversed_lst

def main():
    # Example usage
    original = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(original)
    print(f"Original list: {original}")
    print(f"Reversed list: {reversed_list}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Normal list
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "Test 1 failed"
    print("Test Case 1 Passed: [1,2,3,4,5] -> [5,4,3,2,1]")
    
    # Test Case 2: Empty list
    assert reverse_list([]) == [], "Test 2 failed"
    print("Test Case 2 Passed: [] -> []")
    
    # Test Case 3: Single element
    assert reverse_list([42]) == [42], "Test 3 failed"
    print("Test Case 3 Passed: [42] -> [42]")
    
    # Test Case 4: List with strings
    assert reverse_list(['a', 'b', 'c']) == ['c', 'b', 'a'], "Test 4 failed"
    print("Test Case 4 Passed: ['a','b','c'] -> ['c','b','a']")
    
    # Test Case 5: List with mixed types
    assert reverse_list([1, 'hello', 3.14]) == [3.14, 'hello', 1], "Test 5 failed"
    print("Test Case 5 Passed: [1,'hello',3.14] -> [3.14,'hello',1]")
    
    print("\\nAll tests passed!")