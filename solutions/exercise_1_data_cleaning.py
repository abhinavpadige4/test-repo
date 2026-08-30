\"\"\"
Exercise 1: Data Cleaning (Easy)
Problem Statement:
Write a function `clean_data(data)` that takes a list of numbers (may contain None or NaN values) and returns a tuple:
- cleaned list with all None/NaN removed
- count of removed elements

Use math.isnan to detect NaN (note: None cannot be passed to isnan, handle separately).

Test Cases:
1. clean_data([1, 2, None, 4, float('nan'), 6]) -> ([1, 2, 4, 6], 2)
2. clean_data([None, None, None]) -> ([], 3)
3. clean_data([1.0, 2.0, 3.0]) -> ([1.0, 2.0, 3.0], 0)
\"\"\"
import math

def clean_data(data):
    """
    Remove None and NaN values from a list.
    
    Args:
        data (list): List of numbers possibly containing None or float('nan').
    
    Returns:
        tuple: (cleaned_list, removed_count)
    """
    cleaned = []
    removed = 0
    for item in data:
        if item is None:
            removed += 1
        elif isinstance(item, float) and math.isnan(item):
            removed += 1
        else:
            cleaned.append(item)
    return cleaned, removed

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, None, 4, float('nan'), 6], ([1, 2, 4, 6], 2)),
        ([None, None, None], ([], 3)),
        ([1.0, 2.0, 3.0], ([1.0, 2.0, 3.0], 0)),
    ]
    
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = clean_data(input_data)
        assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"
        print(f"Test case {i} passed: clean_data({input_data}) = {result}")
    
    print("All tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n) where n is length of data list (single pass).
    # Space Complexity: O(n) for cleaned list (worst case no removals).
\"\"\"