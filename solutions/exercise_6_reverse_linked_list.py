\"\"\"
Exercise 6: Reverse a Linked List
Topic: Linked List
Difficulty: Medium

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Solution:
\"\"\"
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        ListNode: New head of the reversed linked list
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

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
    # Test Case 1: Empty list
    head1 = create_linked_list([])
    reversed1 = reverse_linked_list(head1)
    print(f"Test Case 1: {linked_list_to_list(reversed1)}")  # Expected: []
    
    # Test Case 2: Single element
    head2 = create_linked_list([1])
    reversed2 = reverse_linked_list(head2)
    print(f"Test Case 2: {linked_list_to_list(reversed2)}")  # Expected: [1]
    
    # Test Case 3: Multiple elements
    head3 = create_linked_list([1, 2, 3, 4, 5])
    reversed3 = reverse_linked_list(head3)
    print(f"Test Case 3: {linked_list_to_list(reversed3)}")  # Expected: [5, 4, 3, 2, 1]
    
    # Test Case 4: Two elements
    head4 = create_linked_list([10, 20])
    reversed4 = reverse_linked_list(head4)
    print(f"Test Case 4: {linked_list_to_list(reversed4)}")  # Expected: [20, 10]

# Complexity Analysis:
# Time Complexity: O(n) - where n is the number of nodes in the list
# Space Complexity: O(1) - constant extra space