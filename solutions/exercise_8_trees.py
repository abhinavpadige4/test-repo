\"\"\"
Exercise 8: Maximum Depth of Binary Tree

Problem Statement:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
\"\"\"

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_recursive(root):
    \"\"\"
    Calculate the maximum depth of a binary tree recursively.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        int: Maximum depth of the tree
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (recursion stack)
    \"\"\"
    # Base case: empty tree has depth 0
    if not root:
        return 0
    
    # Recursive case: depth is 1 (current node) + max depth of subtrees
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return max(left_depth, right_depth) + 1

def max_depth_iterative_dfs(root):
    \"\"\"
    Calculate the maximum depth of a binary tree using iterative DFS.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        int: Maximum depth of the tree
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (stack space)
    \"\"\"
    if not root:
        return 0
    
    # Stack stores (node, depth) pairs
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        
        if node:
            max_depth = max(max_depth, depth)
            # Add children to stack with incremented depth
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    
    return max_depth

def max_depth_iterative_bfs(root):
    \"\"\"
    Calculate the maximum depth of a binary tree using iterative BFS (level-order traversal).
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        int: Maximum depth of the tree
        
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(w) where w is the maximum width of the tree (queue space)
    \"\"\"
    if not root:
        return 0
    
    from collections import deque
    queue = deque([root])
    depth = 0
    
    while queue:
        # Process all nodes at current level
        level_size = len(queue)
        depth += 1
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth

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
    nodes1 = [3, 9, 20, None, None, 15, 7]
    root1 = create_tree_from_list(nodes1)
    result1_recursive = max_depth_recursive(root1)
    result1_dfs = max_depth_iterative_dfs(root1)
    result1_bfs = max_depth_iterative_bfs(root1)
    expected1 = 3
    print(f\"Test 1: Tree = {nodes1}\")
    print(f\"Expected: {expected1}\")
    print(f\"Recursive result: {result1_recursive}\")
    print(f\"DFS result: {result1_dfs}\")
    print(f\"BFS result: {result1_bfs}\")
    assert result1_recursive == expected1
    assert result1_dfs == expected1
    assert result1_bfs == expected1
    
    # Test case 2
    nodes2 = [1, None, 2]
    root2 = create_tree_from_list(nodes2)
    result2_recursive = max_depth_recursive(root2)
    result2_dfs = max_depth_iterative_dfs(root2)
    result2_bfs = max_depth_iterative_bfs(root2)
    expected2 = 2
    print(f\"\\nTest 2: Tree = {nodes2}\")
    print(f\"Expected: {expected2}\")
    print(f\"Recursive result: {result2_recursive}\")
    print(f\"DFS result: {result2_dfs}\")
    print(f\"BFS result: {result2_bfs}\")
    assert result2_recursive == expected2
    assert result2_dfs == expected2
    assert result2_bfs == expected2
    
    # Test case 3
    nodes3 = []
    root3 = create_tree_from_list(nodes3)
    result3_recursive = max_depth_recursive(root3)
    result3_dfs = max_depth_iterative_dfs(root3)
    result3_bfs = max_depth_iterative_bfs(root3)
    expected3 = 0
    print(f\"\\nTest 3: Tree = {nodes3}\")
    print(f\"Expected: {expected3}\")
    print(f\"Recursive result: {result3_recursive}\")
    print(f\"DFS result: {result3_dfs}\")
    print(f\"BFS result: {result3_bfs}\")
    assert result3_recursive == expected3
    assert result3_dfs == expected3
    assert result3_bfs == expected3
    
    # Test case 4
    nodes4 = [1, 2, 3, 4, 5, 6, 7, 8]
    root4 = create_tree_from_list(nodes4)
    result4_recursive = max_depth_recursive(root4)
    result4_dfs = max_depth_iterative_dfs(root4)
    result4_bfs = max_depth_iterative_bfs(root4)
    expected4 = 4
    print(f\"\\nTest 4: Tree = {nodes4}\")
    print(f\"Expected: {expected4}\")
    print(f\"Recursive result: {result4_recursive}\")
    print(f\"DFS result: {result4_dfs}\")
    print(f\"BFS result: {result4_bfs}\")
    assert result4_recursive == expected4
    assert result4_dfs == expected4
    assert result4_bfs == expected4
    
    print(\"\\nAll tests passed!\")