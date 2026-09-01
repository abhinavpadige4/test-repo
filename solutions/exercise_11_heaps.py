"""
Exercise 11: Kth Largest Element in an Array
============================================

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Examples:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach:
Use a min-heap of size k:
1. Keep only k largest elements in the heap
2. For each element, if heap size < k, push it
3. Otherwise, if element > heap top, pop smallest and push current element
4. The root of heap will be kth largest element

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

def find_kth_largest(nums, k):
    """
    Find the kth largest element in an array using a min-heap.
    
    Args:
        nums (List[int]): Array of integers
        k (int): Position of largest element to find
        
    Returns:
        int: Kth largest element in the array
    """
    if not nums or k > len(nums):
        return None
    
    # Initialize min-heap
    min_heap = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    
    # Root of min-heap of size k is kth largest element
    return min_heap[0]

# Test cases
def test_find_kth_largest():
    # Test case 1: Normal case
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = find_kth_largest(nums1, k1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Array with duplicates
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    result2 = find_kth_largest(nums2, k2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: k equals array length
    nums3 = [1, 2, 3, 4, 5]
    k3 = 5
    expected3 = 1
    result3 = find_kth_largest(nums3, k3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_kth_largest()