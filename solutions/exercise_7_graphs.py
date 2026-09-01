"""
Exercise 7: Number of Islands
=============================

Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Approach:
Use BFS or DFS to traverse each island:
1. Iterate through each cell in the grid
2. When encountering a '1', increment island count and perform DFS/BFS
3. In DFS/BFS, mark visited land cells as '0' to avoid counting again

Time Complexity: O(m * n)
Space Complexity: O(m * n) in worst case for recursion stack
"""

def num_islands(grid):
    """
    Count number of islands in a binary grid.
    
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
        """Depth-first search to mark all connected land cells as visited."""
        # Check bounds and if cell is water or already visited
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
            return
        
        # Mark current cell as visited by changing '1' to '0'
        grid[r][c] = '0'
        
        # Visit all 4 adjacent cells
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Iterate through each cell
    for r in range(rows):
        for c in range(cols):
            # If land cell found, it's a new island
            if grid[r][c] == '1':
                count += 1
                # Mark all connected land cells as visited
                dfs(r, c)
    
    return count

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Multiple islands
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    result1 = num_islands([row[:] for row in grid1])  # Copy to avoid modifying original
    print(f"Test 1: Number of islands = {result1}")  # Expected: 1
    
    # Test Case 2: Multiple separate islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result2 = num_islands([row[:] for row in grid2])
    print(f"Test 2: Number of islands = {result2}")  # Expected: 3
    
    # Test Case 3: All water
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    result3 = num_islands([row[:] for row in grid3])
    print(f"Test 3: Number of islands = {result3}")  # Expected: 0