\"\"\"
Exercise 12: Merge Intervals
Topic: Array / Sorting
Difficulty: Medium

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Solution:
\"\"\"
def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Args:
        intervals (List[List[int]]): List of intervals [start, end]
    
    Returns:
        List[List[int]]: List of merged intervals
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping intervals
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged

# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic overlapping
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Test Case 1: merge_intervals({intervals1}) = {merge_intervals(intervals1)}")  # Expected: [[1,6],[8,10],[15,18]]
    
    # Test Case 2: No overlap
    intervals2 = [[1,2],[3,4],[5,6]]
    print(f"Test Case 2: merge_intervals({intervals2}) = {merge_intervals(intervals2)}")  # Expected: [[1,2],[3,4],[5,6]]
    
    # Test Case 3: Fully contained
    intervals3 = [[1,4],[4,5]]
    print(f"Test Case 3: merge_intervals({intervals3}) = {merge_intervals(intervals3)}")  # Expected: [[1,5]]
    
    # Test Case 4: Empty list
    print(f"Test Case 4: merge_intervals([]) = {merge_intervals([])}")  # Expected: []

# Complexity Analysis:
# Time Complexity: O(n log n) - due to sorting
# Space Complexity: O(n) - for the output list (or O(1) if we modify in-place)