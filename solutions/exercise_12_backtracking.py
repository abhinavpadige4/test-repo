"""
Exercise 12: N-Queens Problem
=============================

Problem Statement:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration where 'Q' indicates a queen and '.' indicates an empty space.

Examples:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

Approach:
Use backtracking:
1. Place queens row by row
2. For each row, try placing queen in each column
3. Check if position is valid (no conflicts with previously placed queens)
4. If valid, recursively try next row
5. If we reach last row, we found a solution

Time Complexity: O(N!)
Space Complexity: O(N^2) for board + O(N) for recursion stack
"""

def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all valid configurations.
    
    Args:
        n (int): Size of chessboard and number of queens
        
    Returns:
        List[List[str]]: All valid board configurations
    """
    def is_safe(board, row, col):
        """
        Check if placing queen at (row, col) is safe.
        """
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(board, row):
        """
        Recursive backtracking function to place queens.
        """
        if row == n:
            # Found a valid solution
            result.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                # Place queen
                board[row][col] = 'Q'
                # Recurse to next row
                backtrack(board, row + 1)
                # Backtrack
                board[row][col] = '.'
    
    result = []
    # Initialize empty board
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result

# Test cases
def test_solve_n_queens():
    # Test case 1: n = 4
    n1 = 4
    result1 = solve_n_queens(n1)
    expected_count1 = 2  # There are 2 solutions for n=4
    assert len(result1) == expected_count1, f"Test 1 failed: expected {expected_count1} solutions, got {len(result1)}"
    
    # Test case 2: n = 1
    n2 = 1
    result2 = solve_n_queens(n2)
    expected2 = [["Q"]]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solve_n_queens()