"""
Exercise 2: Linked List Cycle Detection
=======================================

Problem Statement:
Given a linked list, determine if it has a cycle in it. Return the node where the cycle begins. If there is no cycle, return None.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

Input: head = [1,2], pos = 0
Output: tail connects to node index 0

Input: head = [1], pos = -1
Output: no cycle

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

Approach:
Use Floyd's Cycle Detection Algorithm (Tortoise and Hare):
1. Use two pointers, slow and fast
2. Move slow one step and fast two steps
3. If they meet, there's a cycle
4. To find the start of cycle, move one pointer to head and advance both one step until they meet

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    """
    Detect if there is a cycle in the linked list and return the start node of cycle.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        ListNode: Start node of cycle if exists, else None
    """
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if cycle exists
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        # No cycle found
        return None
    
    # Phase 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# Test cases
def test_detect_cycle():
    # Test case 1: Cycle exists
    # Create nodes: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle back to node2 (index 1)
    
    result1 = detect_cycle(node1)
    assert result1 == node2, f"Test 1 failed: expected node with value {node2.val}, got {result1.val if result1 else None}"
    
    # Test case 2: No cycle
    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    
    result2 = detect_cycle(node5)
    assert result2 is None, f"Test 2 failed: expected None, got {result2}"
    
    # Test case 3: Single node with cycle
    node7 = ListNode(1)
    node7.next = node7  # Points to itself
    
    result3 = detect_cycle(node7)
    assert result3 == node7, f"Test 3 failed: expected node with value {node7.val}, got {result3.val if result3 else None}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_detect_cycle()