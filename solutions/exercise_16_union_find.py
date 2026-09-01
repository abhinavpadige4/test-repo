"""
Exercise 16: Number of Connected Components in Graph
====================================================

Problem Statement:
Given a graph with n nodes and a list of edges, return the number of connected components.

Example:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Approach:
Use Union-Find (Disjoint Set Union) data structure:
1. Initially, each node is its own parent (n separate components)
2. For each edge, union the two nodes
3. Count the number of distinct parents (connected components)

Optimizations:
- Path compression: Make nodes point directly to root during find
- Union by rank: Attach smaller tree under root of larger tree

Time Complexity: O(E * α(n)) where α is inverse Ackermann function (practically constant)
Space Complexity: O(n)
"""

class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find data structure.
        
        Args:
            n (int): Number of nodes
        """
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [0] * n           # Rank for union by rank optimization
        self.components = n           # Initially n separate components
    
    def find(self, x):
        """
        Find root/parent of node x with path compression.
        
        Args:
            x (int): Node to find parent for
            
        Returns:
            int: Root/parent of node x
        """
        # Path compression: make nodes point directly to root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union two nodes x and y.
        
        Args:
            x (int): First node
            y (int): Second node
            
        Returns:
            bool: True if union performed, False if already in same component
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # Already in same component
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller tree under root of larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        # Decrease component count
        self.components -= 1
        return True

def count_components(n, edges):
    """
    Count number of connected components in graph.
    
    Args:
        n (int): Number of nodes
        edges (List[List[int]]): List of edges [node1, node2]
        
    Returns:
        int: Number of connected components
    """
    uf = UnionFind(n)
    
    # Process each edge
    for edge in edges:
        uf.union(edge[0], edge[1])
    
    return uf.components

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Two separate components
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    result1 = count_components(n1, edges1)
    print(f"Test 1: n={n1}, edges={edges1} -> {result1} components")  # Expected: 2
    
    # Test Case 2: One component (connected graph)
    n2 = 4
    edges2 = [[0, 1], [1, 2], [2, 3]]
    result2 = count_components(n2, edges2)
    print(f"Test 2: n={n2}, edges={edges2} -> {result2} components")  # Expected: 1
    
    # Test Case 3: All isolated nodes
    n3 = 3
    edges3 = []
    result3 = count_components(n3, edges3)
    print(f"Test 3: n={n3}, edges={edges3} -> {result3} components")  # Expected: 3
    
    # Test Case 4: Complex graph
    n4 = 6
    edges4 = [[0, 1], [1, 2], [3, 4], [4, 5]]
    result4 = count_components(n4, edges4)
    print(f"Test 4: n={n4}, edges={edges4} -> {result4} components")  # Expected: 2