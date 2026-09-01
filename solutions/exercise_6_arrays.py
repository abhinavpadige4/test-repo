"""
Exercise 6: Container With Most Water (Medium)
Problem Statement:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

def max_area(height):
    """
    Find the maximum area between two vertical lines using two pointers approach.
    
    Args:
        height (List[int]): Array representing heights of vertical lines
    
    Returns:
        int: Maximum area that can be contained
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize two pointers at both ends
    left = 0
    right = len(height) - 1
    max_water = 0
    
    # Move pointers inward based on which side is shorter
    while left < right:
        # Calculate current area
        current_area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Brute force approach for comparison (not recommended for large inputs)
def max_area_brute_force(height):
    """
    Brute force approach to find maximum area - O(n^2) time complexity.
    
    Args:
        height (List[int]): Array representing heights of vertical lines
    
    Returns:
        int: Maximum area that can be contained
        
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            current_area = min(height[i], height[j]) * (j - i)
            max_water = max(max_water, current_area)
    
    return max_water

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    result1 = max_area(height1)
    print(f"Test 1 - Input: {height1}")
    print(f"Output: {result1}")
    print(f"Expected: 49")
    print(f"Pass: {result1 == 49}\\n")
    
    # Test Case 2
    height2 = [1,1]
    result2 = max_area(height2)
    print(f"Test 2 - Input: {height2}")
    print(f"Output: {result2}")
    print(f"Expected: 1")
    print(f"Pass: {result2 == 1}\\n")
    
    # Test Case 3
    height3 = [4,3,2,1,4]
    result3 = max_area(height3)
    print(f"Test 3 - Input: {height3}")
    print(f"Output: {result3}")
    print(f"Expected: 16")
    print(f"Pass: {result3 == 16}\\n")
    
    # Test Case 4
    height4 = [1,2,1]
    result4 = max_area(height4)
    print(f"Test 4 - Input: {height4}")
    print(f"Output: {result4}")
    print(f"Expected: 2")
    print(f"Pass: {result4 == 2}\\n")