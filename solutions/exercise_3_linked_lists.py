"""
Exercise 3: Merge Two Sorted Lists (Easy)
Problem Statement:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    """
    Merge two sorted linked lists into one sorted linked list.
    
    Args:
        list1 (ListNode): Head of the first sorted linked list
        list2 (ListNode): Head of the second sorted linked list
    
    Returns:
        ListNode: Head of the merged sorted linked list
        
    Time Complexity: O(m + n) where m and n are lengths of the lists
    Space Complexity: O(1)
    """
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists and connect nodes in sorted order
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Connect remaining nodes (if any)
    current.next = list1 or list2
    
    # Return the head of merged list (skip dummy node)
    return dummy.next

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
    list1_1 = create_linked_list([1, 2, 4])
    list2_1 = create_linked_list([1, 3, 4])
    merged1 = merge_two_lists(list1_1, list2_1)
    result1 = linked_list_to_array(merged1)
    print(f"Test 1 - List1: [1,2,4], List2: [1,3,4]")
    print(f"Output: {result1}")
    print(f"Expected: [1,1,2,3,4,4]")
    print(f"Pass: {result1 == [1,1,2,3,4,4]}\\n")
    
    # Test Case 2
    list1_2 = create_linked_list([])
    list2_2 = create_linked_list([])
    merged2 = merge_two_lists(list1_2, list2_2)
    result2 = linked_list_to_array(merged2)
    print(f"Test 2 - List1: [], List2: []")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print(f"Pass: {result2 == []}\\n")
    
    # Test Case 3
    list1_3 = create_linked_list([])
    list2_3 = create_linked_list([0])
    merged3 = merge_two_lists(list1_3, list2_3)
    result3 = linked_list_to_array(merged3)
    print(f"Test 3 - List1: [], List2: [0]")
    print(f"Output: {result3}")
    print(f"Expected: [0]")
    print(f"Pass: {result3 == [0]}\\n")