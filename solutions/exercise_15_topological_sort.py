\"\"\"
Exercise 15: Topological Sort (Kahn's Algorithm)
Topic: Graph Algorithms
Difficulty: Medium

Problem Statement:
Given a directed acyclic graph (DAG), print all vertices in topological order.
Use Kahn's algorithm which uses in-degree of vertices.

Solution:
\"\"\"
from collections import deque, defaultdict

def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph (DAG).
    
    Args:
        graph: Dictionary representing adjacency list {node: [list of neighbors]}
        
    Returns:
        List of vertices in topological order, or empty list if cycle exists
    """
    # Compute in-degree of each vertex
    in_degree = defaultdict(int)
    # Ensure all nodes are in in_degree (even if they have zero in-degree)
    for u in graph:
        in_degree[u]  # initialize if not present
        for v in graph[u]:
            in_degree[v] += 1
    
    # Queue for nodes with zero in-degree
    queue = deque([u for u in graph if in_degree[u] == 0])
    top_order = []
    
    while queue:
        u = queue.popleft()
        top_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # If topological sort includes all vertices, return it
    if len(top_order) == len(graph):
        return top_order
    else:
        # Cycle exists
        return []

def main():
    # Example graph (DAG)
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': []
    }
    
    result = topological_sort(graph)
    print("Topological Order:", result)
    
    # Another example
    graph2 = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        1: [],
        0: []
    }
    result2 = topological_sort(graph2)
    print("Topological Order 2:", result2)

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple DAG
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result1 = topological_sort(graph1)
    # Valid topological orders: ['A','B','C','D'] or ['A','C','B','D']
    assert set(result1) == {'A','B','C','D'}, "Test 1 failed: Missing nodes"
    assert len(result1) == 4, "Test 1 failed: Length mismatch"
    # Check that A comes before B and C, and B and C come before D
    assert result1.index('A') < result1.index('B'), "Test 1 failed: A before B"
    assert result1.index('A') < result1.index('C'), "Test 1 failed: A before C"
    assert result1.index('B') < result1.index('D'), "Test 1 failed: B before D"
    assert result1.index('C') < result1.index('D'), "Test 1 failed: C before D"
    print("Test Case 1 Passed: Simple DAG")
    
    # Test Case 2: Linear graph
    graph2 = {
        '1': ['2'],
        '2': ['3'],
        '3': ['4'],
        '4': []
    }
    result2 = topological_sort(graph2)
    assert result2 == ['1', '2', '3', '4'], "Test 2 failed: Linear graph"
    print("Test Case 2 Passed: Linear graph")
    
    # Test Case 3: Empty graph
    graph3 = {}
    result3 = topological_sort(graph3)
    assert result3 == [], "Test 3 failed: Empty graph"
    print("Test Case 3 Passed: Empty graph")
    
    # Test Case 4: Single node
    graph4 = {'A': []}
    result4 = topological_sort(graph4)
    assert result4 == ['A'], "Test 4 failed: Single node"
    print("Test Case 4 Passed: Single node")
    
    # Test Case 5: Graph with cycle (should return empty list)
    graph5 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']  # Cycle
    }
    result5 = topological_sort(graph5)
    assert result5 == [], "Test 5 failed: Cycle detection"
    print("Test Case 5 Passed: Cycle detection")
    
    print("\\nAll tests passed!")