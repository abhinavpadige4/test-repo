"""
Exercise 4: Maximum Depth of Binary Tree (Easy)
Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Calculate the maximum depth of a binary tree using recursion.
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        int: Maximum depth of the binary tree
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    # Base case: if node is None, depth is 0
    if not root:
        return 0
    
    # Recursively calculate depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return 1 (current node) + max depth of subtrees
    return 1 + max(left_depth, right_depth)

# Alternative iterative solution using BFS
def max_depth_iterative(root):
    """
    Calculate the maximum depth of a binary tree using iteration (BFS).
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        int: Maximum depth of the binary tree
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree
    """
    if not root:
        return 0
    
    from collections import deque
    queue = deque([(root, 1)])  # (node, depth)
    max_depth_val = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth_val = max(max_depth_val, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth_val

# Test Cases
if __name__ == "__main__":
    # Test Case 1: [3,9,20,null,null,15,7]
    #       3
    #      / \\
    #     9   20
    #        /  \\
    #       15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    result1_recursive = max_depth(root1)
    result1_iterative = max_depth_iterative(root1)
    print(f"Test 1 - Tree: [3,9,20,null,null,15,7]")
    print(f"Recursive Output: {result1_recursive}")
    print(f"Iterative Output: {result1_iterative}")
    print(f"Expected: 3")
    print(f"Recursive Pass: {result1_recursive == 3}")
    print(f"Iterative Pass: {result1_iterative == 3}\\n")
    
    # Test Case 2: [1,null,2]
    #     1
    #      \\
    #       2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    
    result2_recursive = max_depth(root2)
    result2_iterative = max_depth_iterative(root2)
    print(f"Test 2 - Tree: [1,null,2]")
    print(f"Recursive Output: {result2_recursive}")
    print(f"Iterative Output: {result2_iterative}")
    print(f"Expected: 2")
    print(f"Recursive Pass: {result2_recursive == 2}")
    print(f"Iterative Pass: {result2_iterative == 2}\\n")
    
    # Test Case 3: Empty tree
    root3 = None
    result3_recursive = max_depth(root3)
    result3_iterative = max_depth_iterative(root3)
    print(f"Test 3 - Tree: []")
    print(f"Recursive Output: {result3_recursive}")
    print(f"Iterative Output: {result3_iterative}")
    print(f"Expected: 0")
    print(f"Recursive Pass: {result3_recursive == 0}")
    print(f"Iterative Pass: {result3_iterative == 0}\\n")