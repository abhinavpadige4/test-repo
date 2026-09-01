"""
Exercise 12: Number of Islands (Medium)
Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

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
    Count the number of islands using DFS (Depth-First Search) to explore connected components.
    
    Args:
        grid (List[List[str]]): 2D grid of '1's (land) and '0's (water)
    
    Returns:
        int: Number of islands in the grid
        
    Time Complexity: O(m * n) where m is rows and n is columns
    Space Complexity: O(m * n) in worst case for recursion stack
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        """
        Helper function to perform DFS and mark visited land cells.
        """
        # Check boundaries and if cell is water or already visited
        if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
            return
        
        # Mark current cell as visited by changing '1' to '0'
        grid[r][c] = '0'
        
        # Explore all 4 directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell, it's a new island
            if grid[r][c] == '1':
                count += 1
                # Use DFS to mark all connected land cells as visited
                dfs(r, c)
    
    return count

# Alternative approach using BFS (Breadth-First Search)
from collections import deque

def num_islands_bfs(grid):
    """
    Count the number of islands using BFS to explore connected components.
    
    Args:
        grid (List[List[str]]): 2D grid of '1's (land) and '0's (water)
    
    Returns:
        int: Number of islands in the grid
        
    Time Complexity: O(m * n) where m is rows and n is columns
    Space Complexity: O(min(m, n)) for the queue
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    # Directions for exploring neighbors (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                # Mark current cell as visited
                grid[r][c] = '0'
                
                # BFS to mark all connected land cells
                queue = deque([(r, c)])
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    # Check all 4 directions
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # Check boundaries and if it's unvisited land
                        if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'):
                            grid[nr][nc] = '0'  # Mark as visited
                            queue.append((nr, nc))
    
    return count

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
    print("Test 1 - Grid:")
    for row in grid1:
        print(row)
    print(f"Output: {result1}")
    print(f"Expected: 1")
    print(f"Pass: {result1 == 1}\\n")
    
    # Test Case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    # Make a copy for testing since the original gets modified
    grid2_copy = [row[:] for row in grid2]
    result2 = num_islands_bfs(grid2_copy)
    print("Test 2 - Grid:")
    for row in grid2:
        print(row)
    print(f"Output: {result2}")
    print(f"Expected: 3")
    print(f"Pass: {result2 == 3}\\n")
    
    # Test Case 3 - Single island
    grid3 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    result3 = num_islands([row[:] for row in grid3])
    print("Test 3 - Grid:")
    for row in grid3:
        print(row)
    print(f"Output: {result3}")
    print(f"Expected: 1")
    print(f"Pass: {result3 == 1}\\n")
    
    # Test Case 4 - No islands
    grid4 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    result4 = num_islands([row[:] for row in grid4])
    print("Test 4 - Grid:")
    for row in grid4:
        print(row)
    print(f"Output: {result4}")
    print(f"Expected: 0")
    print(f"Pass: {result4 == 0}\\n")