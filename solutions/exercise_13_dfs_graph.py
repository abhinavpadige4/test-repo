\"\"\"
Exercise 13: Depth-First Search (DFS) on Graph
Topic: Graph Algorithms
Difficulty: Medium

Problem Statement:
Given a graph represented as an adjacency list and a starting node, perform a depth-first search traversal and return the order of visited nodes.

Solution:
\"\"\"
def dfs(graph, start):
    """
    Perform depth-first search on a graph.
    
    Args:
        graph (dict): Adjacency list representation of the graph
        start: Starting node
    
    Returns:
        List: Nodes in the order they were visited
    """
    visited = set()
    result = []
    
    def dfs_recursive(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result

# Test cases
if __name__ == "__main__":
    # Test Case 1: Simple graph
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(f"Test Case 1: dfs(graph1, 'A') = {dfs(graph1, 'A')}")
    # Expected: ['A', 'B', 'D', 'E', 'F', 'C'] or similar (depending on order)
    
    # Test Case 2: Graph with cycle
    graph2 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    print(f"Test Case 2: dfs(graph2, 0) = {dfs(graph2, 0)}")
    # Expected: [0, 1, 2, 3]
    
    # Test Case 3: Disconnected graph (only connected component from start)
    graph3 = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    print(f"Test Case 3: dfs(graph3, 0) = {dfs(graph3, 0)}")  # Expected: [0, 1]
    
    # Test Case 4: Single node
    graph4 = {'X': []}
    print(f"Test Case 4: dfs(graph4, 'X') = {dfs(graph4, 'X')}")  # Expected: ['X']

# Complexity Analysis:
# Time Complexity: O(V + E) - where V is number of vertices, E is number of edges
# Space Complexity: O(V) - for the visited set and recursion stack