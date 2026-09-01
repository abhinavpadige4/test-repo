"""
Exercise 18: Course Schedule II
===============================

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
you must take course bi first if you want to take course ai.

Return the ordering of courses you should take to finish all courses.
If it is impossible to finish all courses, return an empty array.

Approach:
Use Topological Sorting with Kahn's Algorithm:
1. Build adjacency list representation of graph
2. Calculate in-degree for each node
3. Add all nodes with in-degree 0 to queue
4. While queue is not empty:
   - Remove node and add to result
   - Reduce in-degree of its neighbors
   - Add neighbors with in-degree 0 to queue
5. If result length < numCourses, there's a cycle (impossible to finish)

Time Complexity: O(V + E) where V is vertices (courses) and E is edges (prerequisites)
Space Complexity: O(V + E) for adjacency list and in-degree array
"""

from collections import defaultdict, deque

def find_order(numCourses, prerequisites):
    """
    Find order to take courses to finish all without conflicts.
    
    Args:
        numCourses (int): Number of courses
        prerequisites (List[List[int]]): Prerequisites list [course, prerequisite]
        
    Returns:
        List[int]: Valid course order, empty list if impossible
    """
    # Build adjacency list and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    # Populate graph and in-degrees
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Initialize queue with courses having no prerequisites
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    
    # Process courses in topological order
    while queue:
        # Take course with no prerequisites
        current_course = queue.popleft()
        result.append(current_course)
        
        # Update in-degrees of dependent courses
        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1
            # If no more prerequisites, add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we couldn't take all courses, there's a cycle
    return result if len(result) == numCourses else []

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Possible to finish all courses
    numCourses1 = 4
    prerequisites1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result1 = find_order(numCourses1, prerequisites1)
    print(f"Test 1: numCourses={numCourses1}, prerequisites={prerequisites1}")
    print(f"Course order: {result1}")  # Expected: [0, 1, 2, 3] or [0, 2, 1, 3]
    
    # Test Case 2: Impossible to finish (cycle)
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    result2 = find_order(numCourses2, prerequisites2)
    print(f"\nTest 2: numCourses={numCourses2}, prerequisites={prerequisites2}")
    print(f"Course order: {result2}")  # Expected: [] (empty)
    
    # Test Case 3: No prerequisites
    numCourses3 = 3
    prerequisites3 = []
    result3 = find_order(numCourses3, prerequisites3)
    print(f"\nTest 3: numCourses={numCourses3}, prerequisites={prerequisites3}")
    print(f"Course order: {result3}")  # Expected: [0, 1, 2] (any order)
    
    # Test Case 4: Linear dependency
    numCourses4 = 5
    prerequisites4 = [[1, 0], [2, 1], [3, 2], [4, 3]]
    result4 = find_order(numCourses4, prerequisites4)
    print(f"\nTest 4: numCourses={numCourses4}, prerequisites={prerequisites4}")
    print(f"Course order: {result4}")  # Expected: [0, 1, 2, 3, 4]