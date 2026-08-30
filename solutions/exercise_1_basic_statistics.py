\"\"\"
Exercise 1: Basic Statistics Calculation
Topic: Statistics and Probability
Difficulty: Easy

Problem Statement:
Write a Python function that calculates the mean, median, and mode of a given list of numbers.
Handle edge cases such as empty lists and lists with multiple modes.

Requirements:
- Mean: average of all numbers
- Median: middle value when sorted (average of two middle values for even length)
- Mode: most frequent value(s) - return all modes if multiple exist
- Return results as a dictionary with keys 'mean', 'median', 'mode'
- For mode, return a list (even if single mode) or empty list if no mode exists

Example:
Input: [1, 2, 2, 3, 4]
Output: {'mean': 2.4, 'median': 2, 'mode': [2]}
\"\"\"

from collections import Counter
from typing import List, Union, Dict, Any

def calculate_statistics(numbers: List[Union[int, float]]) -> Dict[str, Any]:
    """
    Calculate mean, median, and mode of a list of numbers.
    
    Args:
        numbers: List of integers or floats
        
    Returns:
        Dictionary with keys 'mean', 'median', 'mode'
        Mode is returned as a list (can be empty, single, or multiple values)
    """
    # Handle empty list
    if not numbers:
        return {'mean': None, 'median': None, 'mode': []}
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    
    # Calculate mode
    frequency = Counter(numbers)
    max_count = max(frequency.values())
    
    # If all elements are unique, max_count will be 1
    if max_count == 1 and len(numbers) > 1:
        mode = []  # No mode exists
    else:
        mode = [num for num, count in frequency.items() if count == max_count]
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode
    }

# Test cases
if __name__ == "__main__":
    # Test case 1: Normal case with single mode
    test1 = [1, 2, 2, 3, 4]
    result1 = calculate_statistics(test1)
    print("Test 1 - Input:", test1)
    print("Output:", result1)
    print("Expected: {'mean': 2.4, 'median': 2, 'mode': [2]}")
    assert result1['mean'] == 2.4
    assert result1['median'] == 2
    assert result1['mode'] == [2]
    print("✓ Test 1 passed\\n")
    
    # Test case 2: Multiple modes
    test2 = [1, 1, 2, 2, 3, 4]
    result2 = calculate_statistics(test2)
    print("Test 2 - Input:", test2)
    print("Output:", result2)
    print("Expected: mean=1.5, median=2.0, mode=[1, 2]")
    assert result2['mean'] == 1.5
    assert result2['median'] == 2.0
    assert set(result2['mode']) == {1, 2}
    print("✓ Test 2 passed\\n")
    
    # Test case 3: Empty list
    test3 = []
    result3 = calculate_statistics(test3)
    print("Test 3 - Input:", test3)
    print("Output:", result3)
    print("Expected: {'mean': None, 'median': None, 'mode': []}")
    assert result3['mean'] is None
    assert result3['median'] is None
    assert result3['mode'] == []
    print("✓ Test 3 passed\\n")
    
    # Test case 4: All unique values (no mode)
    test4 = [1, 2, 3, 4, 5]
    result4 = calculate_statistics(test4)
    print("Test 4 - Input:", test4)
    print("Output:", result4)
    print("Expected: mean=3.0, median=3, mode=[]")
    assert result4['mean'] == 3.0
    assert result4['median'] == 3
    assert result4['mode'] == []
    print("✓ Test 4 passed\\n")
    
    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(n log n) due to sorting for median calculation
# Space Complexity: O(n) for storing the sorted list and frequency counter