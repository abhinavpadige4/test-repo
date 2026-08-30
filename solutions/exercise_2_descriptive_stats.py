\"\"\"
Exercise 2: Descriptive Statistics (Easy)
Problem Statement:
Write a function `descriptive_stats(data)` that takes a list of numbers and returns a dictionary containing:
- mean
- median
- mode (if multiple modes, return the smallest one; if no mode, return None)
- range (max - min)
- variance (population variance)
- standard deviation (population std dev)

Do not use any libraries (like numpy, statistics) for calculations. Use only built-in Python.

Test Cases:
1. descriptive_stats([1, 2, 3, 4, 5]) -> 
   {'mean': 3.0, 'median': 3, 'mode': None, 'range': 4, 'variance': 2.0, 'std_dev': ~1.414}
2. descriptive_stats([1, 1, 2, 3, 4]) -> 
   {'mean': 2.2, 'median': 2, 'mode': 1, 'range': 3, 'variance': ~1.36, 'std_dev': ~1.166}
3. descriptive_stats([5, 5, 5, 5]) -> 
   {'mean': 5.0, 'median': 5, 'mode': 5, 'range': 0, 'variance': 0.0, 'std_dev': 0.0}
\"\"\"
def descriptive_stats(data):
    """
    Calculate descriptive statistics for a list of numbers.
    
    Args:
        data (list): List of numerical values.
    
    Returns:
        dict: Dictionary with keys 'mean', 'median', 'mode', 'range', 'variance', 'std_dev'.
    """
    if not data:
        return {'mean': None, 'median': None, 'mode': None, 'range': None, 'variance': None, 'std_dev': None}
    
    n = len(data)
    # Mean
    mean = sum(data) / n
    
    # Median
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n//2]
    else:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    
    # Mode
    frequency = {}
    for val in data:
        frequency[val] = frequency.get(val, 0) + 1
    max_freq = max(frequency.values())
    if max_freq == 1:
        mode = None  # No mode
    else:
        # Get all values with max_freq, return the smallest
        modes = [k for k, v in frequency.items() if v == max_freq]
        mode = min(modes)
    
    # Range
    data_range = max(data) - min(data)
    
    # Variance (population variance)
    variance = sum((x - mean) ** 2 for x in data) / n
    
    # Standard deviation
    std_dev = variance ** 0.5
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': data_range,
        'variance': variance,
        'std_dev': std_dev
    }

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 
         {'mean': 3.0, 'median': 3, 'mode': None, 'range': 4, 'variance': 2.0, 'std_dev': 2.0**0.5}),
        ([1, 1, 2, 3, 4], 
         {'mean': 2.2, 'median': 2, 'mode': 1, 'range': 3, 'variance': 1.36, 'std_dev': 1.36**0.5}),
        ([5, 5, 5, 5], 
         {'mean': 5.0, 'median': 5, 'mode': 5, 'range': 0, 'variance': 0.0, 'std_dev': 0.0})
    ]
    
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = descriptive_stats(input_data)
        # Compare with tolerance for floating point
        passed = True
        for key in expected:
            if isinstance(expected[key], float):
                if abs(result[key] - expected[key]) > 1e-9:
                    passed = False
                    break
            else:
                if result[key] != expected[key]:
                    passed = False
                    break
        if passed:
            print(f"Test case {i} passed")
        else:
            print(f"Test case {i} failed: got {result}, expected {expected}")
    
    print("All tests completed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n log n) due to sorting for median. Otherwise O(n) for mean, mode, range, variance.
    # Space Complexity: O(n) for sorted list and frequency dictionary.
\"\"\"