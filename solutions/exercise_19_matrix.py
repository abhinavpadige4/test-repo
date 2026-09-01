"""
Exercise 19: Spiral Matrix
=========================

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Approach:
Simulate the spiral traversal by maintaining boundaries:
1. Initialize four boundaries: top, bottom, left, right
2. Traverse in four directions in order:
   - Left to right along top boundary
   - Top to bottom along right boundary
   - Right to left along bottom boundary
   - Bottom to top along left boundary
3. After each traversal, adjust the corresponding boundary
4. Continue until all elements are processed

Time Complexity: O(m * n) where m and n are matrix dimensions
Space Complexity: O(1) excluding result array
"""

def spiral_order(matrix):
    """
    Return elements of matrix in spiral order.
    
    Args:
        matrix (List[List[int]]): Input matrix
        
    Returns:
        List[int]: Elements in spiral order
    """
    if not matrix or not matrix[0]:
        return []
    
    result = []
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize boundaries
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while top <= bottom and left <= right:
        # Traverse right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1  # Move top boundary down
        
        # Traverse down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1  # Move right boundary left
        
        # Traverse left along bottom row (if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1  # Move bottom boundary up
        
        # Traverse up along left column (if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1  # Move left boundary right
    
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result1 = spiral_order(matrix1)
    print(f"Test 1: {matrix1}")
    print(f"Spiral order: {result1}")  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    # Test Case 2: 3x4 matrix
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    result2 = spiral_order(matrix2)
    print(f"\nTest 2: {matrix2}")
    print(f"Spiral order: {result2}")  # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    
    # Test Case 3: Single row
    matrix3 = [[1, 2, 3, 4, 5]]
    result3 = spiral_order(matrix3)
    print(f"\nTest 3: {matrix3}")
    print(f"Spiral order: {result3}")  # Expected: [1, 2, 3, 4, 5]
    
    # Test Case 4: Single column
    matrix4 = [[1], [2], [3], [4]]
    result4 = spiral_order(matrix4)
    print(f"\nTest 4: {matrix4}")
    print(f"Spiral order: {result4}")  # Expected: [1, 2, 3, 4]
    
    # Test Case 5: 1x1 matrix
    matrix5 = [[1]]
    result5 = spiral_order(matrix5)
    print(f"\nTest 5: {matrix5}")
    print(f"Spiral order: {result5}")  # Expected: [1]