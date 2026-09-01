\"\"\"
Exercise 8: Merge Two Sorted Lists
Topic: Linked List
Difficulty: Medium

Problem Statement:
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Solution:
\"\"\"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    """
    Merge two sorted linked lists.
    
    Args:
        l1 (ListNode): Head of first sorted linked list
        l2 (ListNode): Head of second sorted linked list
    
    Returns:
        ListNode: Head of the merged sorted linked list
    """
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach the remaining elements
    current.next = l1 if l1 else l2
    
    return dummy.next

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values and return head."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    # Test Case 1: Both lists non-empty
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])
    merged = merge_two_lists(l1, l2)
    print(f"Test Case 1: {linked_list_to_list(merged)}")  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test Case 2: One list empty
    l3 = create_linked_list([])
    l4 = create_linked_list([0])
    merged2 = merge_two_lists(l3, l4)
    print(f"Test Case 2: {linked_list_to_list(merged2)}")  # Expected: [0]
    
    # Test Case 3: Both lists empty
    l5 = create_linked_list([])
    l6 = create_linked_list([])
    merged3 = merge_two_lists(l5, l6)
    print(f"Test Case 3: {linked_list_to_list(merged3)}")  # Expected: []
    
    # Test Case 4: Different lengths
    l7 = create_linked_list([1, 2, 3, 4, 5])
    l8 = create_linked_list([6, 7, 8])
    merged4 = merge_two_lists(l7, l8)
    print(f"Test Case 4: {linked_list_to_list(merged4)}")  # Expected: [1, 2, 3, 4, 5, 6, 7, 8]

# Complexity Analysis:
# Time Complexity: O(n + m) - where n and m are the lengths of the two lists
# Space Complexity: O(1) - constant extra space (excluding the output list)