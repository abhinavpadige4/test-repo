"""
Exercise 19: Max Area of Island
==============================

Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid 
are surrounded by water. The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Examples:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

Approach:
Use Depth-First Search (DFS):
1. For each cell with value 1, perform DFS to calculate area of the island
2. During DFS, mark visited cells as 0 to avoid revisiting
3. Keep track of maximum area found

Time Complexity: O(m * n)
Space Complexity: O(m * n) in worst case due to recursion stack
"""

def max_area_of_island(grid):
    """
    Find the maximum area of an island in a binary matrix.
    
    Args:
        grid (List[List[int]]): Binary matrix representing land (1) and water (0)
        
    Returns:
        int: Maximum area of an island
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    max_area = 0
    
    def dfs(r, c):
        """
        Depth-first search to calculate area of island starting from (r, c).
        
        Args:
            r (int): Row index
            c (int): Column index
            
        Returns:
            int: Area of island starting from (r, c)
        """
        # Check boundaries and if cell is water or already visited
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return 0
        
        # Mark current cell as visited
        grid[r][c] = 0
        
        # Calculate area: 1 (current cell) + area of neighbors
        area = 1
        area += dfs(r + 1, c)  # Down
        area += dfs(r - 1, c)  # Up
        area += dfs(r, c + 1)  # Right
        area += dfs(r, c - 1)  # Left
        
        return area
    
    # Traverse the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found unvisited land
                # Calculate area of current island and update max
                current_area = dfs(i, j)
                max_area = max(max_area, current_area)
    
    return max_area

# Test cases
def test_max_area_of_island():
    # Test case 1: Grid with multiple islands
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    expected1 = 6
    result1 = max_area_of_island(grid1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: All water
    grid2 = [[0,0,0,0,0,0,0,0]]
    expected2 = 0
    result2 = max_area_of_island(grid2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single cell island
    grid3 = [[1]]
    expected3 = 1
    result3 = max_area_of_island(grid3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_area_of_island()