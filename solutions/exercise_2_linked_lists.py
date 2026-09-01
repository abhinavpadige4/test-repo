"""
Exercise 2: Reverse Linked List

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        ListNode: New head of the reversed linked list
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    current = head
    
    while current:
        # Store next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    # prev is now the new head
    return prev

def reverse_list_recursive(head):
    """
    Reverse a singly linked list recursively.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        ListNode: New head of the reversed linked list
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    # Base case
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head

# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array."""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy comparison."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(arr1)
    reversed_head1 = reverse_list(head1)
    result1 = linked_list_to_array(reversed_head1)
    expected1 = [5, 4, 3, 2, 1]
    print(f"Test 1: {arr1} => {result1}")
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test Case 2
    arr2 = [1, 2]
    head2 = create_linked_list(arr2)
    reversed_head2 = reverse_list(head2)
    result2 = linked_list_to_array(reversed_head2)
    expected2 = [2, 1]
    print(f"Test 2: {arr2} => {result2}")
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test Case 3
    arr3 = []
    head3 = create_linked_list(arr3)
    reversed_head3 = reverse_list(head3)
    result3 = linked_list_to_array(reversed_head3)
    expected3 = []
    print(f"Test 3: {arr3} => {result3}")
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("All tests passed!")