\"\"\"
Exercise 2: Reverse a Linked List

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

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
\"\"\"

class ListNode:
    \"\"\"Definition for singly-linked list node.\"\"\"
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head):
    \"\"\"
    Reverse a linked list iteratively.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        ListNode: Head of the reversed linked list
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    \"\"\"
    prev = None
    current = head
    
    while current:
        # Store the next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    # prev is now the new head
    return prev

def reverse_list_recursive(head):
    \"\"\"
    Reverse a linked list recursively.
    
    Args:
        head (ListNode): Head of the linked list
    
    Returns:
        ListNode: Head of the reversed linked list
        
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    \"\"\"
    # Base case: empty list or single node
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
    \"\"\"Create a linked list from an array.\"\"\"
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def linked_list_to_array(head):
    \"\"\"Convert a linked list to an array for easy verification.\"\"\"
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == \"__main__\": 
    # Test case 1
    nums1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(nums1)
    reversed_head1 = reverse_list_iterative(head1)
    result1 = linked_list_to_array(reversed_head1)
    print(f\"Test 1: Original = {nums1}\")
    print(f\"Expected: [5, 4, 3, 2, 1], Got: {result1}\")
    assert result1 == [5, 4, 3, 2, 1]
    
    # Test case 2
    nums2 = [1, 2]
    head2 = create_linked_list(nums2)
    reversed_head2 = reverse_list_iterative(head2)
    result2 = linked_list_to_array(reversed_head2)
    print(f\"\\nTest 2: Original = {nums2}\")
    print(f\"Expected: [2, 1], Got: {result2}\")
    assert result2 == [2, 1]
    
    # Test case 3
    nums3 = []
    head3 = create_linked_list(nums3)
    reversed_head3 = reverse_list_iterative(head3)
    result3 = linked_list_to_array(reversed_head3)
    print(f\"\\nTest 3: Original = {nums3}\")
    print(f\"Expected: [], Got: {result3}\")
    assert result3 == []
    
    print(\"\\nAll iterative tests passed!\")
    
    # Test recursive approach
    nums4 = [1, 2, 3, 4, 5]
    head4 = create_linked_list(nums4)
    reversed_head4 = reverse_list_recursive(head4)
    result4 = linked_list_to_array(reversed_head4)
    print(f\"\\nRecursive Test: Original = {nums4}\")
    print(f\"Expected: [5, 4, 3, 2, 1], Got: {result4}\")
    assert result4 == [5, 4, 3, 2, 1]
    
    print(\"\\nRecursive test passed!\")