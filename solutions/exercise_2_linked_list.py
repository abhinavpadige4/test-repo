"""
Exercise 2: Linked List Cycle Detection
=======================================

Problem Statement:
Given head of a linked list, determine if the linked list has a cycle in it.
A cycle exists if there is some node that can be reached again by following the next pointer.

Approach:
Use Floyd's Cycle Detection Algorithm (Tortoise and Hare):
- Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
- If there's a cycle, they will eventually meet
- If fast reaches null, there's no cycle

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Detect if a linked list has a cycle.
    
    Args:
        head (ListNode): Head of the linked list
        
    Returns:
        bool: True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    # Move slow one step and fast two steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    # If fast reaches end, no cycle
    return False

# Test Cases
if __name__ == "__main__":
    # Test Case 1: No cycle
    # 1 -> 2 -> 3 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    
    print(f"Test 1 - Has cycle: {has_cycle(node1)}")  # Expected: False
    
    # Test Case 2: Cycle exists
    # 1 -> 2 -> 3 -> 4
    #      ^         |
    #      |_________|
    node4 = ListNode(1)
    node5 = ListNode(2)
    node6 = ListNode(3)
    node7 = ListNode(4)
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node5  # Creates cycle
    
    print(f"Test 2 - Has cycle: {has_cycle(node4)}")  # Expected: True
    
    # Test Case 3: Single node with cycle
    node8 = ListNode(1)
    node8.next = node8  # Points to itself
    
    print(f"Test 3 - Has cycle: {has_cycle(node8)}")  # Expected: True