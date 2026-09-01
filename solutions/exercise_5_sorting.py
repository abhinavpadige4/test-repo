"""
Exercise 5: Merge Intervals
===========================

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return an array of the non-overlapping intervals.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Approach:
1. Sort intervals by start time
2. Iterate through sorted intervals
3. If current interval overlaps with last merged interval, merge them
4. Otherwise, add current interval to result

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for result array
"""

def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Args:
        intervals (List[List[int]]): List of intervals [start, end]
        
    Returns:
        List[List[int]]: Merged non-overlapping intervals
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # If current interval overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge by extending end time of last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add current interval to result
            merged.append(current)
    
    return merged

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Overlapping intervals
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    result1 = merge_intervals(intervals1)
    print(f"Test 1: {intervals1} -> {result1}")  # Expected: [[1,6],[8,10],[15,18]]
    
    # Test Case 2: No overlapping
    intervals2 = [[1,4],[5,6]]
    result2 = merge_intervals(intervals2)
    print(f"Test 2: {intervals2} -> {result2}")  # Expected: [[1,4],[5,6]]
    
    # Test Case 3: All overlapping
    intervals3 = [[1,4],[4,5]]
    result3 = merge_intervals(intervals3)
    print(f"Test 3: {intervals3} -> {result3}")  # Expected: [[1,5]]