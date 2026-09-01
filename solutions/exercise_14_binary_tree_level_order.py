\"\"\"
Exercise 14: Binary Tree Level Order Traversal
Topic: Tree / BFS
Difficulty: Medium

Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Solution:
\"\"\"
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Return the level order traversal of a binary tree.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        List[List[int]]: List of lists containing node values level by level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    
    return result

# Helper function to build a tree from a list (for testing)
def build_tree(values):
    """
    Build a binary tree from a list representation (like LeetCode).
    None indicates a missing node.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            left = TreeNode(values[i])
            node.left = left
            queue.append(left)
        i += 1
        if i < len(values) and values[i] is not None:
            right = TreeNode(values[i])
            node.right = right
            queue.append(right)
        i += 1
    return root

# Test cases
if __name__ == "__main__":
    # Test Case 1: Typical tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    vals1 = [3, 9, 20, None, None, 15, 7]
    root1 = build_tree(vals1)
    print(f"Test Case 1: level_order = {level_order(root1)}")
    # Expected: [[3], [9, 20], [15, 7]]
    
    # Test Case 2: Single node
    root2 = build_tree([1])
    print(f"Test Case 2: level_order = {level_order(root2)}")  # Expected: [[1]]
    
    # Test Case 3: Empty tree
    root3 = build_tree([])
    print(f"Test Case 3: level_order = {level_order(root3)}")  # Expected: []
    
    # Test Case 4: Left skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    root4 = build_tree([1, 2, None, 3])
    print(f"Test Case 4: level_order = {level_order(root4)}")  # Expected: [[1], [2], [3]]

# Complexity Analysis:
# Time Complexity: O(n) - where n is the number of nodes (each node processed once)
# Space Complexity: O(n) - for the queue and result list