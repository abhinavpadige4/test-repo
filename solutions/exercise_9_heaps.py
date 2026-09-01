"""
Exercise 9: Kth Largest Element
===============================

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Approach:
Multiple approaches possible:
1. Sort array and return nums[n-k] - O(n log n)
2. Use min-heap of size k - O(n log k)
3. Quickselect algorithm - O(n) average case

We'll implement the min-heap approach:
- Maintain a heap of size k with smallest k elements
- The root of heap will be the kth largest element

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

def find_kth_largest(nums, k):
    """
    Find the kth largest element in array.
    
    Args:
        nums (List[int]): Input array
        k (int): Position of element to find (1-indexed from largest)
        
    Returns:
        int: Kth largest element
    """
    # Min-heap to store k largest elements
    heap = []
    
    for num in nums:
        if len(heap) < k:
            # Heap not full, push element
            heapq.heappush(heap, num)
        elif num > heap[0]:
            # Current element is larger than smallest in heap
            # Remove smallest and add current
            heapq.heapreplace(heap, num)
    
    # Root of min-heap is kth largest element
    return heap[0]

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = find_kth_largest(nums1, k1)
    print(f"Test 1: {nums1}, k={k1} -> {result1}")  # Expected: 5
    
    # Test Case 2: With duplicates
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = find_kth_largest(nums2, k2)
    print(f"Test 2: {nums2}, k={k2} -> {result2}")  # Expected: 4
    
    # Test Case 3: k = 1 (largest element)
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    result3 = find_kth_largest(nums3, k3)
    print(f"Test 3: {nums3}, k={k3} -> {result3}")  # Expected: 5