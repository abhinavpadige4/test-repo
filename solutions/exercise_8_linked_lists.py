"""
Exercise 8: Remove Nth Node From End of List (Medium)
Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow up: Could you do this in one pass?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of the linked list in one pass using two pointers.
    
    Args:
        head (ListNode): Head of the linked list
        n (int): Position from the end to remove (1-indexed)
    
    Returns:
        ListNode: Head of the modified linked list
        
    Time Complexity: O(L) where L is the length of the list
    Space Complexity: O(1)
    """
    # Create a dummy node to handle edge cases (like removing the head)
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers
    first = dummy
    second = dummy
    
    # Advance first pointer by n+1 steps
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from end
    second.next = second.next.next
    
    # Return the head of modified list
    return dummy.next

# Alternative approach using two passes
def remove_nth_from_end_two_pass(head, n):
    """
    Two-pass approach to remove the nth node from the end.
    
    Args:
        head (ListNode): Head of the linked list
        n (int): Position from the end to remove (1-indexed)
    
    Returns:
        ListNode: Head of the modified linked list
        
    Time Complexity: O(L) where L is the length of the list
    Space Complexity: O(1)
    """
    # First pass: count the total number of nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    # Calculate position from beginning
    position_from_start = count - n
    
    # Special case: removing the first node
    if position_from_start == 0:
        return head.next
    
    # Second pass: traverse to the node before the target and remove it
    current = head
    for _ in range(position_from_start - 1):
        current = current.next
    
    current.next = current.next.next
    return head

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
    """Convert a linked list to an array."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = remove_nth_from_end(head1, 2)
    output1 = linked_list_to_array(result1)
    print(f"Test 1 - Input: [1,2,3,4,5], n = 2")
    print(f"Output: {output1}")
    print(f"Expected: [1,2,3,5]")
    print(f"Pass: {output1 == [1,2,3,5]}\\n")
    
    # Test Case 2
    head2 = create_linked_list([1])
    result2 = remove_nth_from_end(head2, 1)
    output2 = linked_list_to_array(result2)
    print(f"Test 2 - Input: [1], n = 1")
    print(f"Output: {output2}")
    print(f"Expected: []")
    print(f"Pass: {output2 == []}\\n")
    
    # Test Case 3
    head3 = create_linked_list([1, 2])
    result3 = remove_nth_from_end(head3, 1)
    output3 = linked_list_to_array(result3)
    print(f"Test 3 - Input: [1,2], n = 1")
    print(f"Output: {output3}")
    print(f"Expected: [1]")
    print(f"Pass: {output3 == [1]}\\n")
    
    # Test Case 4
    head4 = create_linked_list([1, 2, 3])
    result4 = remove_nth_from_end(head4, 3)
    output4 = linked_list_to_array(result4)
    print(f"Test 4 - Input: [1,2,3], n = 3")
    print(f"Output: {output4}")
    print(f"Expected: [2,3]")
    print(f"Pass: {output4 == [2,3]}\\n")