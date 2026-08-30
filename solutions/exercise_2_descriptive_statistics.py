\"\"\"
Exercise 2: Descriptive Statistics
Topic: Descriptive statistics
Difficulty: Easy

Problem Statement:
Given a list of numbers, calculate the mean, median, and mode.
Handle the case where there might be multiple modes (return a list).

Solution:
- Mean: sum(values) / len(values)
- Median: middle value when sorted (average of two middle if even)
- Mode: most frequent value(s). If multiple, return all.

Write a function descriptive_stats(data) that returns a dict with keys 'mean', 'median', 'mode'.
\"\"\"

from collections import Counter

def descriptive_stats(data):
    \"\"\"Calculate mean, median, and mode of a list of numbers.\"\"\"
    if not data:
        return {'mean': None, 'median': None, 'mode': []}
    
    # Mean
    mean = sum(data) / len(data)
    
    # Median
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median = sorted_data[n//2]
    else:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    
    # Mode
    freq = Counter(data)
    max_count = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_count]
    
    return {'mean': mean, 'median': median, 'mode': mode}

# Test cases
if __name__ == \"__main__\":
    # Test 1: Simple list
    data1 = [1, 2, 3, 4, 5]
    result1 = descriptive_stats(data1)
    expected1 = {'mean': 3.0, 'median': 3, 'mode': [1, 2, 3, 4, 5]}  # all appear once
    print(f\"Test 1: {result1}\")
    assert result1['mean'] == expected1['mean']
    assert result1['median'] == expected1['median']
    assert set(result1['mode']) == set(expected1['mode'])
    print(\"Test 1 passed\")
    
    # Test 2: Even number of elements
    data2 = [1, 2, 3, 4, 5, 6]
    result2 = descriptive_stats(data2)
    expected2 = {'mean': 3.5, 'median': 3.5, 'mode': [1, 2, 3, 4, 5, 6]}
    print(f\"Test 2: {result2}\")
    assert result2['mean'] == expected2['mean']
    assert result2['median'] == expected2['median']
    assert set(result2['mode']) == set(expected2['mode'])
    print(\"Test 2 passed\")
    
    # Test 3: With a clear mode
    data3 = [1, 2, 2, 3, 4]
    result3 = descriptive_stats(data3)
    expected3 = {'mean': 2.4, 'median': 2, 'mode': [2]}
    print(f\"Test 3: {result3}\")
    assert abs(result3['mean'] - expected3['mean']) < 1e-9
    assert result3['median'] == expected3['median']
    assert result3['mode'] == expected3['mode']
    print(\"Test 3 passed\")
    
    print(\"All tests passed.\")
\"\"\"