"""
Exercise 3: Binary Tree Inorder Traversal

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
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree iteratively.
    
    Inorder traversal visits nodes in the order: Left -> Root -> Right
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        List[int]: Inorder traversal of node values
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to the leftmost node
        if current:
            stack.append(current)
            current = current.left
        else:
            # Backtrack from empty subtree
            current = stack.pop()
            result.append(current.val)
            # Visit right subtree
            current = current.right
    
    return result

def inorder_traversal_recursive(root):
    """
    Perform inorder traversal of a binary tree recursively.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        List[int]: Inorder traversal of node values
    
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    """
    result = []
    
    def inorder_helper(node):
        if node:
            # Traverse left subtree
            inorder_helper(node.left)
            # Visit root
            result.append(node.val)
            # Traverse right subtree
            inorder_helper(node.right)
    
    inorder_helper(root)
    return result

# Helper function for testing
def create_tree_from_list(nodes):
    """
    Create a binary tree from a list representation.
    None represents a null node.
    """
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        # Add left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nodes1 = [1, None, 2, 3]
    root1 = create_tree_from_list(nodes1)
    result1 = inorder_traversal(root1)
    expected1 = [1, 3, 2]
    print(f"Test 1: {nodes1} => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    nodes2 = []
    root2 = create_tree_from_list(nodes2)
    result2 = inorder_traversal(root2)
    expected2 = []
    print(f"Test 2: {nodes2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    nodes3 = [1]
    root3 = create_tree_from_list(nodes3)
    result3 = inorder_traversal(root3)
    expected3 = [1]
    print(f"Test 3: {nodes3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("All tests passed!")