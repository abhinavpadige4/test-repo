"""
Exercise 4: Binary Tree Level Order Traversal
============================================

Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level)

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Approach:
Use BFS (Breadth-First Search) with a queue:
- Process nodes level by level
- For each level, track the number of nodes to process
- Add children of current level nodes to queue for next level

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(w) where w is maximum width of tree
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    """
    Perform level order traversal of binary tree.
    
    Args:
        root (TreeNode): Root of binary tree
        
    Returns:
        List[List[int]]: Level order traversal result
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Normal tree
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    result1 = level_order(root1)
    print(f"Test 1: Level order = {result1}")  # Expected: [[3], [9, 20], [15, 7]]
    
    # Test Case 2: Single node
    root2 = TreeNode(1)
    result2 = level_order(root2)
    print(f"Test 2: Level order = {result2}")  # Expected: [[1]]
    
    # Test Case 3: Empty tree
    result3 = level_order(None)
    print(f"Test 3: Level order = {result3}")  # Expected: []