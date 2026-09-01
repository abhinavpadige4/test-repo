"""
Exercise 7: Number of Islands
=============================

Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Examples:
Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1

Input: grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

Approach:
Use Depth-First Search (DFS) to traverse each island.
For every '1' encountered, increment island count and use DFS to mark all connected '1's as visited (by changing them to '0').

Time Complexity: O(m * n)
Space Complexity: O(m * n) in worst case due to recursion stack
"""

def num_islands(grid):
    """
    Count the number of islands in a 2D binary grid.
    
    Args:
        grid (List[List[str]]): 2D grid of '1's (land) and '0's (water)
        
    Returns:
        int: Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        """
        Depth-first search to mark all connected land cells as visited.
        """
        # Check boundaries and if cell is water or already visited
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # Mark current cell as visited by changing '1' to '0'
        grid[r][c] = '0'
        
        # Explore all 4 directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Traverse the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Found unvisited land
                count += 1
                dfs(i, j)  # Mark entire island as visited
    
    return count

# Test cases
def test_num_islands():
    # Test case 1: One large island
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected1 = 1
    result1 = num_islands(grid1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Three separate islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected2 = 3
    result2 = num_islands(grid2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: All water
    grid3 = [
        ["0","0","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected3 = 0
    result3 = num_islands(grid3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_num_islands()