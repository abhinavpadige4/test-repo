"""
Exercise 3: Binary Tree Inorder Traversal
=========================================

Problem Statement:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Examples:
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Approach:
Implement iterative inorder traversal using a stack.
Inorder traversal follows the pattern: Left -> Root -> Right

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree iteratively.
    
    Args:
        root (TreeNode): Root of the binary tree
        
    Returns:
        List[int]: Inorder traversal of node values
    """
    if not root:
        return []
    
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None here, so we backtrack
        current = stack.pop()
        result.append(current.val)
        
        # Visit right subtree
        current = current.right
    
    return result

# Test cases
def test_inorder_traversal():
    # Test case 1: Normal tree
    #     1
    #      \
    #       2
    #      /
    #     3
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    
    expected1 = [1, 3, 2]
    result1 = inorder_traversal(root1)
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2: Empty tree
    root2 = None
    expected2 = []
    result2 = inorder_traversal(root2)
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3: Single node
    root3 = TreeNode(1)
    expected3 = [1]
    result3 = inorder_traversal(root3)
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_inorder_traversal()