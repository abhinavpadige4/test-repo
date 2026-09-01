\"\"\"
Exercise 18: Dijkstra's Shortest Path Algorithm
Topic: Graph Algorithms
Difficulty: Hard

Problem Statement:
Implement Dijkstra's algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

Solution:
\"\"\"
import heapq
from typing import Dict, List, Tuple, Any

def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], source: Any) -> Dict[Any, float]:
    """
    Compute shortest paths from source to all vertices in a weighted graph.
    
    Args:
        graph: Adjacency list representation {node: [(neighbor, weight), ...]}
        source: Starting vertex
        
    Returns:
        Dictionary mapping each vertex to its shortest distance from source
    """
    # Initialize distances with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    # Priority queue: (distance, vertex)
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # If we've already found a better path, skip
        if current_distance > distances[current_vertex]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # If found shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def main():
    # Example graph (undirected for simplicity, but algorithm works for directed too)
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
        'E': [('C', 10), ('D', 2), ('F', 3)],
        'F': [('D', 6), ('E', 3)]
    }
    
    source = 'A'
    distances = dijkstra(graph, source)
    
    print(f"Shortest distances from {source}:")
    for vertex, dist in sorted(distances.items()):
        print(f"  {vertex}: {dist}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple graph
    graph1 = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }
    dist1 = dijkstra(graph1, 'A')
    expected1 = {'A': 0, 'B': 1, 'C': 3, 'D': 6}
    assert dist1 == expected1, f"Test 1 failed. Expected {expected1}, got {dist1}"
    print("Test Case 1 Passed: Simple graph")
    
    # Test Case 2: Disconnected graph (some vertices unreachable)
    graph2 = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 1)],
        'D': [('C', 1)]
    }
    dist2 = dijkstra(graph2, 'A')
    # A and B reachable, C and D should be infinity
    assert dist2['A'] == 0, "Test 2 failed: A distance"
    assert dist2['B'] == 1, "Test 2 failed: B distance"
    assert dist2['C'] == float('infinity'), "Test 2 failed: C should be unreachable"
    assert dist2['D'] == float('infinity'), "Test 2 failed: D should be unreachable"
    print("Test Case 2 Passed: Disconnected graph")
    
    # Test Case 3: Single vertex
    graph3 = {'A': []}
    dist3 = dijkstra(graph3, 'A')
    assert dist3 == {'A': 0}, f"Test 3 failed. Expected {{'A': 0}}, got {dist3}"
    print("Test Case 3 Passed: Single vertex")
    
    # Test Case 4: Graph with zero weight edge
    graph4 = {
        'A': [('B', 0), ('C', 5)],
        'B': [('A', 0), ('C', 1)],
        'C': [('A', 5), ('B', 1)]
    }
    dist4 = dijkstra(graph4, 'A')
    expected4 = {'A': 0, 'B': 0, 'C': 1}
    assert dist4 == expected4, f"Test 4 failed. Expected {expected4}, got {dist4}"
    print("Test Case 4 Passed: Zero weight edge")
    
    print("\\nAll tests passed!")