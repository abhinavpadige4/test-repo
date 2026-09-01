\"\"\"
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

Follow up: Recursive solution is trivial, could you do it iteratively?
\"\"\"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_recursive(root):
    \"\"\"
    Perform inorder traversal of a binary tree recursively.
    
    Inorder traversal visits nodes in this order:
    1. Left subtree
    2. Root node
    3. Right subtree
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        List[int]: Inorder traversal of node values
        
    Time Complexity: O(n)
    Space Complexity: O(h) where h is the height of the tree
    \"\"\"
    result = []
    
    def inorder_helper(node):
        if node:
            # Traverse left subtree
            inorder_helper(node.left)
            # Visit root node
            result.append(node.val)
            # Traverse right subtree
            inorder_helper(node.right)
    
    inorder_helper(root)
    return result

def inorder_traversal_iterative(root):
    \"\"\"
    Perform inorder traversal of a binary tree iteratively using a stack.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        List[int]: Inorder traversal of node values
        
    Time Complexity: O(n)
    Space Complexity: O(h) where h is the height of the tree
    \"\"\"
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

# Helper function for testing
def create_tree_from_list(nodes):
    \"\"\"Create a binary tree from a list representation.\"\"\"
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
if __name__ == \"__main__\": 
    # Test case 1
    nodes1 = [1, None, 2, 3]
    root1 = create_tree_from_list(nodes1)
    result1_recursive = inorder_traversal_recursive(root1)
    result1_iterative = inorder_traversal_iterative(root1)
    print(f\"Test 1: Tree = {nodes1}\")
    print(f\"Expected: [1, 3, 2]\")
    print(f\"Recursive result: {result1_recursive}\")
    print(f\"Iterative result: {result1_iterative}\")
    assert result1_recursive == [1, 3, 2]
    assert result1_iterative == [1, 3, 2]
    
    # Test case 2
    nodes2 = []
    root2 = create_tree_from_list(nodes2)
    result2_recursive = inorder_traversal_recursive(root2)
    result2_iterative = inorder_traversal_iterative(root2)
    print(f\"\\nTest 2: Tree = {nodes2}\")
    print(f\"Expected: []\")
    print(f\"Recursive result: {result2_recursive}\")
    print(f\"Iterative result: {result2_iterative}\")
    assert result2_recursive == []
    assert result2_iterative == []
    
    # Test case 3
    nodes3 = [1]
    root3 = create_tree_from_list(nodes3)
    result3_recursive = inorder_traversal_recursive(root3)
    result3_iterative = inorder_traversal_iterative(root3)
    print(f\"\\nTest 3: Tree = {nodes3}\")
    print(f\"Expected: [1]\")
    print(f\"Recursive result: {result3_recursive}\")
    print(f\"Iterative result: {result3_iterative}\")
    assert result3_recursive == [1]
    assert result3_iterative == [1]
    
    print(\"\\nAll tests passed!\")