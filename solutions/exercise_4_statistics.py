\"\"\"
Exercise 4: Statistics Basics
Problem Statement:
Write a function `compute_statistics` that takes a list of numbers and returns a dictionary containing:
- Mean, median, standard deviation, variance
- Min, max, range
- 25th, 50th (median), 75th percentiles
- Skewness and kurtosis (using scipy.stats)
Use NumPy for calculations where possible, and SciPy for skewness and kurtosis.

Requirements:
- Import numpy as np and scipy.stats as stats.
- Handle empty list by returning None for all statistics.
- Round numerical values to 2 decimal places.

Test Cases:
1. Input: [1, 2, 3, 4, 5]
   Expected Output: 
        mean: 3.0, median: 3.0, std: 1.41, var: 2.0,
        min: 1, max: 5, range: 4,
        25th: 2.0, 50th: 3.0, 75th: 4.0,
        skewness: 0.0, kurtosis: -1.3
2. Input: [10, 20, 30, 40, 50, 60]
   Expected Output: 
        mean: 35.0, median: 35.0, std: 17.08, var: 291.67,
        min: 10, max: 60, range: 50,
        25th: 20.0, 50th: 35.0, 75th: 50.0,
        skewness: 0.0, kurtosis: -1.2
3. Input: []
   Expected Output: All statistics None.

Complexity Analysis:
Time Complexity: O(n log n) due to sorting for percentiles (NumPy uses quickselect which is O(n) on average, but we'll consider O(n log n) for simplicity).
Space Complexity: O(n) for storing the array.
\"\"\"

import numpy as np
from scipy import stats

def compute_statistics(data):
    \"\"\"Compute descriptive statistics for a list of numbers.
    
    Args:
        data (list of float/int): Input numeric data.
        
    Returns:
        dict: Contains statistics as float values rounded to 2 decimal places.
              Returns None for all values if input is empty.
    \"\"\"
    if not data:
        return {
            'mean': None, 'median': None, 'std': None, 'var': None,
            'min': None, 'max': None, 'range': None,
            '25th': None, '50th': None, '75th': None,
            'skewness': None, 'kurtosis': None
        }
    
    arr = np.array(data)
    mean_val = round(float(np.mean(arr)), 2)
    median_val = round(float(np.median(arr)), 2)
    std_val = round(float(np.std(arr)), 2)
    var_val = round(float(np.var(arr)), 2)
    min_val = round(float(np.min(arr)), 2)
    max_val = round(float(np.max(arr)), 2)
    range_val = round(max_val - min_val, 2)
    p25, p50, p75 = np.percentile(arr, [25, 50, 75])
    p25 = round(float(p25), 2)
    p50 = round(float(p50), 2)
    p75 = round(float(p75), 2)
    skew_val = round(float(stats.skew(arr)), 2)
    kurt_val = round(float(stats.kurtosis(arr)), 2)  # Fisher's kurtosis (excess kurtosis)
    
    return {
        'mean': mean_val,
        'median': median_val,
        'std': std_val,
        'var': var_val,
        'min': min_val,
        'max': max_val,
        'range': range_val,
        '25th': p25,
        '50th': p50,
        '75th': p75,
        'skewness': skew_val,
        'kurtosis': kurt_val
    }


# Test cases
if __name__ == \"__main__\":
    # Test 1
    result1 = compute_statistics([1, 2, 3, 4, 5])
    print(\"Test 1:\")
    for k, v in result1.items():
        print(f\"  {k}: {v}\")
    expected1 = {
        'mean': 3.0, 'median': 3.0, 'std': 1.41, 'var': 2.0,
        'min': 1.0, 'max': 5.0, 'range': 4.0,
        '25th': 2.0, '50th': 3.0, '75th': 4.0,
        'skewness': 0.0, 'kurtosis': -1.3
    }
    assert result1 == expected1, f\"Test 1 failed. Got {result1}\"
    print(\"  PASSED\\n\")
    
    # Test 2
    result2 = compute_statistics([10, 20, 30, 40, 50, 60])
    print(\"Test 2:\")
    for k, v in result2.items():
        print(f\"  {k}: {v}\")
    expected2 = {
        'mean': 35.0, 'median': 35.0, 'std': 17.08, 'var': 291.67,
        'min': 10.0, 'max': 60.0, 'range': 50.0,
        '25th': 20.0, '50th': 35.0, '75th': 50.0,
        'skewness': 0.0, 'kurtosis': -1.2
    }
    assert result2 == expected2, f\"Test 2 failed. Got {result2}\"
    print(\"  PASSED\\n\")
    
    # Test 3
    result3 = compute_statistics([])
    print(\"Test 3:\")
    for k, v in result3.items():
        print(f\"  {k}: {v}\")
    assert all(v is None for v in result3.values()), f\"Test 3 failed. Got {result3}\"
    print(\"  PASSED\\n\")
    
    print(\"All tests passed!\")