"""
Exercise 9: Validate Binary Search Tree (Medium)
Problem Statement:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Examples:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    """
    Validate if a binary tree is a valid binary search tree using recursive bounds checking.
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        bool: True if the tree is a valid BST, False otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    """
    def validate(node, low=float('-inf'), high=float('inf')):
        # Empty trees are valid BSTs
        if not node:
            return True
        
        # Current node's value must be between low and high
        if node.val <= low or node.val >= high:
            return False
        
        # Left subtree must be valid with upper bound as current node's value
        # Right subtree must be valid with lower bound as current node's value
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
    
    return validate(root)

# Alternative approach using in-order traversal
def is_valid_bst_inorder(root):
    """
    Validate BST using in-order traversal property (should be strictly increasing).
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        bool: True if the tree is a valid BST, False otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    """
    def inorder(node, values):
        if not node:
            return
        
        inorder(node.left, values)
        values.append(node.val)
        inorder(node.right, values)
    
    values = []
    inorder(root, values)
    
    # Check if the in-order traversal is strictly increasing
    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False
    
    return True

# Iterative approach using stack
def is_valid_bst_iterative(root):
    """
    Validate BST using iterative in-order traversal with stack.
    
    Args:
        root (TreeNode): Root node of the binary tree
    
    Returns:
        bool: True if the tree is a valid BST, False otherwise
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    """
    if not root:
        return True
    
    stack = []
    prev = None
    current = root
    
    while stack or current:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        
        # Check if current value is greater than previous value
        if prev is not None and current.val <= prev:
            return False
        
        prev = current.val
        current = current.right
    
    return True

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid BST [2,1,3]
    #     2
    #    / \\
    #   1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    result1 = is_valid_bst(root1)
    print(f"Test 1 - Tree: [2,1,3]")
    print(f"Output: {result1}")
    print(f"Expected: True")
    print(f"Pass: {result1 == True}\\n")
    
    # Test Case 2: Invalid BST [5,1,4,null,null,3,6]
    #       5
    #      / \\
    #     1   4
    #        / \\
    #       3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    result2 = is_valid_bst(root2)
    print(f"Test 2 - Tree: [5,1,4,null,null,3,6]")
    print(f"Output: {result2}")
    print(f"Expected: False")
    print(f"Pass: {result2 == False}\\n")
    
    # Test Case 3: Single node
    root3 = TreeNode(1)
    result3 = is_valid_bst(root3)
    print(f"Test 3 - Tree: [1]")
    print(f"Output: {result3}")
    print(f"Expected: True")
    print(f"Pass: {result3 == True}\\n")
    
    # Test Case 4: Valid BST with duplicate values not allowed
    #     5
    #    / \\
    #   3   6
    #  / \\   \\
    # 2   4   7
    root4 = TreeNode(5)
    root4.left = TreeNode(3)
    root4.right = TreeNode(6)
    root4.left.left = TreeNode(2)
    root4.left.right = TreeNode(4)
    root4.right.right = TreeNode(7)
    result4 = is_valid_bst(root4)
    print(f"Test 4 - Valid BST")
    print(f"Output: {result4}")
    print(f"Expected: True")
    print(f"Pass: {result4 == True}\\n")