"""
Exercise 7: Number of Islands

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
"""

def num_islands(grid):
    """
    Count the number of islands in a 2D binary grid using DFS.
    
    Approach:
    1. Iterate through each cell in the grid
    2. When we find a '1', increment island count and perform DFS to mark all connected land as visited
    3. In DFS, mark visited land cells as '0' to avoid counting them again
    
    Args:
        grid (List[List[str]]): 2D grid of '1's (land) and '0's (water)
    
    Returns:
        int: Number of islands
    
    Time Complexity: O(M * N) where M is rows and N is columns
    Space Complexity: O(M * N) in worst case for recursion stack
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        """
        Depth-first search to mark all connected land cells as visited.
        """
        # Check bounds and if cell is water or already visited
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # Mark current cell as visited by changing '1' to '0'
        grid[r][c] = '0'
        
        # Explore all 4 directions (up, down, left, right)
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell, it's a new island
            if grid[r][c] == '1':
                islands += 1
                # Use DFS to mark all connected land cells as visited
                dfs(r, c)
    
    return islands

def num_islands_bfs(grid):
    """
    Count the number of islands using BFS instead of DFS.
    
    Args:
        grid (List[List[str]]): 2D grid of '1's (land) and '0's (water)
    
    Returns:
        int: Number of islands
    
    Time Complexity: O(M * N)
    Space Complexity: O(min(M, N)) for queue in worst case
    """
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def bfs(start_r, start_c):
        """
        Breadth-first search to mark all connected land cells as visited.
        """
        queue = deque([(start_r, start_c)])
        grid[start_r][start_c] = '0'  # Mark as visited
        
        while queue:
            r, c = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # Check bounds and if it's unvisited land
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'  # Mark as visited
                    queue.append((nr, nc))
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell, it's a new island
            if grid[r][c] == '1':
                islands += 1
                # Use BFS to mark all connected land cells as visited
                bfs(r, c)
    
    return islands

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    result1 = num_islands(grid1)
    expected1 = 1
    print(f"Test 1: Grid with 1 island => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    # Make a copy for BFS test since the grid gets modified
    grid2_copy = [row[:] for row in grid2]
    result2 = num_islands(grid2)
    expected2 = 3
    print(f"Test 2: Grid with 3 islands => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test BFS version with the copied grid
    result2_bfs = num_islands_bfs(grid2_copy)
    print(f"Test 2 (BFS): Grid with 3 islands => {result2_bfs}")
    assert result2_bfs == expected2, f"Expected {expected2}, got {result2_bfs}"
    
    # Test Case 3: Empty grid
    grid3 = []
    result3 = num_islands(grid3)
    expected3 = 0
    print(f"Test 3: Empty grid => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("All tests passed!")