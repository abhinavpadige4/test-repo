"""
Exercise 8: Kth Largest Element in an Array

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
"""

import heapq

def find_kth_largest_heap(nums, k):
    """
    Find the kth largest element using a min-heap of size k.
    
    Approach:
    1. Maintain a min-heap of size k
    2. For each element in the array:
       - If heap size < k, push the element
       - If element > heap top, pop the smallest and push the new element
    3. The root of the heap will be the kth largest element
    
    Args:
        nums (List[int]): Array of integers
        k (int): Position of largest element to find
    
    Returns:
        int: The kth largest element
    
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    # Initialize a min-heap
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    # The root of the heap is the kth largest element
    return heap[0]

def find_kth_largest_sorting(nums, k):
    """
    Find the kth largest element by sorting the array.
    
    Args:
        nums (List[int]): Array of integers
        k (int): Position of largest element to find
    
    Returns:
        int: The kth largest element
    
    Time Complexity: O(n log n)
    Space Complexity: O(1) if sorting in place, O(n) otherwise
    """
    # Sort the array in descending order
    nums_sorted = sorted(nums, reverse=True)
    # Return the (k-1)th element (0-indexed)
    return nums_sorted[k - 1]

def find_kth_largest_quickselect(nums, k):
    """
    Find the kth largest element using the QuickSelect algorithm.
    
    This is based on the quicksort partitioning approach.
    
    Args:
        nums (List[int]): Array of integers
        k (int): Position of largest element to find
    
    Returns:
        int: The kth largest element
    
    Time Complexity: O(n) average case, O(n^2) worst case
    Space Complexity: O(1)
    """
    def partition(left, right, pivot_index):
        """
        Partition the array around a pivot element.
        """
        pivot = nums[pivot_index]
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        # Move all elements smaller than pivot to the left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to its final place
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    def select(left, right, k_smallest):
        """
        Returns the k-th smallest element in the list within left..right.
        """
        if left == right:
            return nums[left]
        
        # Choose a random pivot
        import random
        pivot_index = random.randint(left, right)
        
        # Find the pivot position and compare with k
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
    
    # kth largest is (n-k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    original1 = nums1.copy()
    result1 = find_kth_largest_heap(nums1, k1)
    expected1 = 5
    print(f"Test 1: nums={original1}, k={k1} => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    original2 = nums2.copy()
    result2 = find_kth_largest_heap(nums2, k2)
    expected2 = 4
    print(f"Test 2: nums={original2}, k={k2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    nums3 = [1]
    k3 = 1
    original3 = nums3.copy()
    result3 = find_kth_largest_heap(nums3, k3)
    expected3 = 1
    print(f"Test 3: nums={original3}, k={k3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Verify all three approaches give the same result for test case 1
    nums1_copy1 = original1.copy()
    nums1_copy2 = original1.copy()
    result1_sort = find_kth_largest_sorting(nums1_copy1, k1)
    result1_quick = find_kth_largest_quickselect(nums1_copy2, k1)
    print(f"Verification for test 1 - Heap: {result1}, Sorting: {result1_sort}, QuickSelect: {result1_quick}")
    assert result1 == result1_sort == result1_quick, "All methods should give the same result"
    
    print("All tests passed!")