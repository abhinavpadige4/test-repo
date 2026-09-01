"""
Exercise 17: Range Sum Query - Mutable
======================================

Problem Statement:
Given an integer array nums, handle multiple queries of the following types:
1. Update the value of an element in nums.
2. Calculate the sum of the elements of nums between indices left and right inclusive.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive.

Approach:
Use a Segment Tree data structure:
- Build a binary tree where each node represents sum of a range
- Leaf nodes represent individual array elements
- Internal nodes represent sum of their children's ranges
- Supports both updates and range queries in O(log n) time

Time Complexity:
- Build: O(n)
- Update: O(log n)
- Sum Range: O(log n)

Space Complexity: O(n)
"""

class SegmentTree:
    def __init__(self, nums):
        """
        Initialize segment tree with given array.
        
        Args:
            nums (List[int]): Input array
        """
        self.n = len(nums)
        # Tree array size is 4*n to ensure enough space
        self.tree = [0] * (4 * self.n)
        self.nums = nums
        if self.n > 0:
            self.build_tree(0, 0, self.n - 1)
    
    def build_tree(self, node, start, end):
        """
        Build segment tree recursively.
        
        Args:
            node (int): Current tree node index
            start (int): Start index of current range
            end (int): End index of current range
        """
        if start == end:
            # Leaf node
            self.tree[node] = self.nums[start]
        else:
            # Internal node
            mid = (start + end) // 2
            # Build left and right subtrees
            self.build_tree(2 * node + 1, start, mid)
            self.build_tree(2 * node + 2, mid + 1, end)
            # Current node value is sum of children
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def update(self, node, start, end, idx, val):
        """
        Update value at index idx to val.
        
        Args:
            node (int): Current tree node index
            start (int): Start index of current range
            end (int): End index of current range
            idx (int): Index to update
            val (int): New value
        """
        if start == end:
            # Leaf node, update value
            self.nums[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                # Update left subtree
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                # Update right subtree
                self.update(2 * node + 2, mid + 1, end, idx, val)
            # Update current node value
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, left, right):
        """
        Query sum in range [left, right].
        
        Args:
            node (int): Current tree node index
            start (int): Start index of current range
            end (int): End index of current range
            left (int): Query range start
            right (int): Query range end
            
        Returns:
            int: Sum in range [left, right]
        """
        if right < start or end < left:
            # No overlap
            return 0
        if left <= start and end <= right:
            # Complete overlap
            return self.tree[node]
        
        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, left, right)
        right_sum = self.query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum

class NumArray:
    def __init__(self, nums):
        """
        Initialize NumArray with given array.
        
        Args:
            nums (List[int]): Initial array
        """
        self.segment_tree = SegmentTree(nums)
    
    def update(self, index, val):
        """
        Update value at given index.
        
        Args:
            index (int): Index to update
            val (int): New value
        """
        self.segment_tree.update(0, 0, self.segment_tree.n - 1, index, val)
    
    def sumRange(self, left, right):
        """
        Calculate sum of elements between indices left and right inclusive.
        
        Args:
            left (int): Left index (inclusive)
            right (int): Right index (inclusive)
            
        Returns:
            int: Sum of elements in range [left, right]
        """
        return self.segment_tree.query(0, 0, self.segment_tree.n - 1, left, right)

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic operations
    nums1 = [1, 3, 5]
    numArray = NumArray(nums1)
    print(f"Initialized with array: {nums1}")
    
    result1 = numArray.sumRange(0, 2)
    print(f"Sum range [0, 2]: {result1}")  # Expected: 9
    
    numArray.update(1, 2)
    print("Updated index 1 to 2")
    
    result2 = numArray.sumRange(0, 2)
    print(f"Sum range [0, 2] after update: {result2}")  # Expected: 8
    
    # Test Case 2: Larger array
    nums2 = [1, 2, 3, 4, 5]
    numArray2 = NumArray(nums2)
    print(f"\nInitialized with array: {nums2}")
    
    result3 = numArray2.sumRange(1, 3)
    print(f"Sum range [1, 3]: {result3}")  # Expected: 9
    
    numArray2.update(2, 10)
    print("Updated index 2 to 10")
    
    result4 = numArray2.sumRange(1, 3)
    print(f"Sum range [1, 3] after update: {result4}")  # Expected: 16