\"\"\"
Exercise 7: Merge Two Sorted Lists

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

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
\"\"\"

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists_iterative(list1, list2):
    \"\"\"
    Merge two sorted linked lists iteratively.
    
    Args:
        list1 (ListNode): Head of first sorted linked list
        list2 (ListNode): Head of second sorted linked list
    
    Returns:
        ListNode: Head of merged sorted linked list
        
    Time Complexity: O(m + n) where m and n are lengths of the lists
    Space Complexity: O(1)
    \"\"\"
    # Create a dummy node to simplify the code
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
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # Return the head of merged list (skip dummy node)
    return dummy.next

def merge_two_lists_recursive(list1, list2):
    \"\"\"
    Merge two sorted linked lists recursively.
    
    Args:
        list1 (ListNode): Head of first sorted linked list
        list2 (ListNode): Head of second sorted linked list
    
    Returns:
        ListNode: Head of merged sorted linked list
        
    Time Complexity: O(m + n) where m and n are lengths of the lists
    Space Complexity: O(m + n) due to recursion stack
    \"\"\"
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case: choose the smaller node and recursively merge the rest
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

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
    list1_vals1 = [1, 2, 4]
    list2_vals1 = [1, 3, 4]
    list1_1 = create_linked_list(list1_vals1)
    list2_1 = create_linked_list(list2_vals1)
    merged_head1 = merge_two_lists_iterative(list1_1, list2_1)
    result1 = linked_list_to_array(merged_head1)
    expected1 = [1, 1, 2, 3, 4, 4]
    print(f\"Test 1:\")
    print(f\"list1 = {list1_vals1}, list2 = {list2_vals1}\")
    print(f\"Expected: {expected1}, Got: {result1}\")
    assert result1 == expected1
    
    # Test case 2
    list1_vals2 = []
    list2_vals2 = []
    list1_2 = create_linked_list(list1_vals2)
    list2_2 = create_linked_list(list2_vals2)
    merged_head2 = merge_two_lists_iterative(list1_2, list2_2)
    result2 = linked_list_to_array(merged_head2)
    expected2 = []
    print(f\"\\nTest 2:\")
    print(f\"list1 = {list1_vals2}, list2 = {list2_vals2}\")
    print(f\"Expected: {expected2}, Got: {result2}\")
    assert result2 == expected2
    
    # Test case 3
    list1_vals3 = []
    list2_vals3 = [0]
    list1_3 = create_linked_list(list1_vals3)
    list2_3 = create_linked_list(list2_vals3)
    merged_head3 = merge_two_lists_iterative(list1_3, list2_3)
    result3 = linked_list_to_array(merged_head3)
    expected3 = [0]
    print(f\"\\nTest 3:\")
    print(f\"list1 = {list1_vals3}, list2 = {list2_vals3}\")
    print(f\"Expected: {expected3}, Got: {result3}\")
    assert result3 == expected3
    
    # Test recursive approach
    list1_vals4 = [1, 2, 4]
    list2_vals4 = [1, 3, 4]
    list1_4 = create_linked_list(list1_vals4)
    list2_4 = create_linked_list(list2_vals4)
    merged_head4 = merge_two_lists_recursive(list1_4, list2_4)
    result4 = linked_list_to_array(merged_head4)
    expected4 = [1, 1, 2, 3, 4, 4]
    print(f\"\\nRecursive Test:\")
    print(f\"list1 = {list1_vals4}, list2 = {list2_vals4}\")
    print(f\"Expected: {expected4}, Got: {result4}\")
    assert result4 == expected4
    
    print(\"\\nAll tests passed!\")