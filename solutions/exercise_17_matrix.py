"""
Exercise 17: Set Matrix Zeroes
==============================

Problem Statement:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Examples:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

Approach:
Use the first row and first column as markers:
1. First check if first row or first column has zeros
2. Iterate through matrix (excluding first row/column) and mark zeros in first row/col
3. Nullify rows and columns based on markers
4. Nullify first row/column if needed

Time Complexity: O(m * n)
Space Complexity: O(1)
"""

def set_zeroes(matrix):
    """
    Set entire row and column to 0 if an element is 0, in-place.
    
    Args:
        matrix (List[List[int]]): Input matrix to modify
    """
    if not matrix or not matrix[0]:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Check if first row has zero
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    
    # Check if first column has zero
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # Use first row and column as markers
    # Iterate through matrix starting from index (1,1)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row
                matrix[0][j] = 0  # Mark column
    
    # Nullify rows based on markers in first column
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0
    
    # Nullify columns based on markers in first row
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0
    
    # Nullify first row if needed
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Nullify first column if needed
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Test cases
def test_set_zeroes():
    # Test case 1: Normal case
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    set_zeroes(matrix1)
    assert matrix1 == expected1, f"Test 1 failed: expected {expected1}, got {matrix1}"
    
    # Test case 2: Multiple zeros
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected2 = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    set_zeroes(matrix2)
    assert matrix2 == expected2, f"Test 2 failed: expected {expected2}, got {matrix2}"
    
    # Test case 3: Single element
    matrix3 = [[1]]
    expected3 = [[1]]
    set_zeroes(matrix3)
    assert matrix3 == expected3, f"Test 3 failed: expected {expected3}, got {matrix3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_set_zeroes()