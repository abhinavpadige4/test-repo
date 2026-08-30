\"\"\"
Exercise 1: NumPy Arrays Basics
Problem Statement:
Write a function `analyze_array` that takes a list of numbers and returns a dictionary containing:
- The NumPy array version of the list.
- The mean, median, and standard deviation of the array.
Use NumPy for calculations.

Requirements:
- Import numpy as np.
- Handle empty list by returning an empty array and None for statistics.
- Round statistical values to 2 decimal places.

Test Cases:
1. Input: [1, 2, 3, 4, 5]
   Expected Output: {'array': array([1, 2, 3, 4, 5]), 'mean': 3.0, 'median': 3.0, 'std': 1.41}
2. Input: [10, 20, 30]
   Expected Output: {'array': array([10, 20, 30]), 'mean': 20.0, 'median': 20.0, 'std': 8.16}
3. Input: []
   Expected Output: {'array': array([]), 'mean': None, 'median': None, 'std': None}

Complexity Analysis:
Time Complexity: O(n) where n is the length of the input list (due to array conversion and reductions).
Space Complexity: O(n) for storing the NumPy array.
\"\"\"

import numpy as np

def analyze_array(data):
    \"\"\"Convert list to NumPy array and compute basic statistics.
    
    Args:
        data (list of float/int): Input numeric data.
        
    Returns:
        dict: Contains 'array' (np.ndarray), 'mean', 'median', 'std'.
              Statistics are None for empty input.
    \"\"\"
    if not data:
        arr = np.array([])
        return {'array': arr, 'mean': None, 'median': None, 'std': None}
    
    arr = np.array(data)
    mean_val = round(float(np.mean(arr)), 2)
    median_val = round(float(np.median(arr)), 2)
    std_val = round(float(np.std(arr)), 2)
    
    return {
        'array': arr,
        'mean': mean_val,
        'median': median_val,
        'std': std_val
    }


# Test cases
if __name__ == \"__main__\":
    # Test 1
    result1 = analyze_array([1, 2, 3, 4, 5])
    print(\"Test 1:\", result1)
    # Expected: array([1,2,3,4,5]), mean 3.0, median 3.0, std 1.41
    
    # Test 2
    result2 = analyze_array([10, 20, 30])
    print(\"Test 2:\", result2)
    # Expected: array([10,20,30]), mean 20.0, median 20.0, std 8.16
    
    # Test 3
    result3 = analyze_array([])
    print(\"Test 3:\", result3)
    # Expected: array([]), mean None, median None, std None