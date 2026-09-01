"""
Exercise 15: LRU Cache
=======================

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
  If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Examples:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Approach:
Use a combination of hash map and doubly linked list:
1. Hash map for O(1) access to nodes
2. Doubly linked list to maintain usage order
3. Most recently used at head, least recently used at tail
4. On get/put, move accessed node to head
5. When capacity exceeded, remove tail node

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity)
"""

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        Initialize the LRU cache with given capacity.
        
        Args:
            capacity (int): Maximum number of entries the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        
        # Dummy head and tail nodes
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """
        Add node right after head (most recently used).
        """
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """
        Move certain node in between to the head (mark as most recently used).
        """
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """
        Pop the current tail (least recently used).
        """
        res = self.tail.prev
        self._remove_node(res)
        return res
    
    def get(self, key):
        """
        Get the value of the key if it exists, otherwise return -1.
        
        Args:
            key (int): Key to look up
            
        Returns:
            int: Value of the key if exists, otherwise -1
        """
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        # Move the accessed node to the head
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
        """
        Insert or update the value of the key.
        
        Args:
            key (int): Key to insert or update
            value (int): Value to associate with the key
        """
        node = self.cache.get(key)
        
        if not node:
            # Create a new node
            new_node = ListNode(key, value)
            
            self.cache[key] = new_node
            self._add_node(new_node)
            
            if len(self.cache) > self.capacity:
                # Evict the least recently used node
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            # Update the value and move to head
            node.value = value
            self._move_to_head(node)

# Test cases
def test_lru_cache():
    # Test case 1: Basic operations
    lru = LRUCache(2)
    
    # Put 1,1
    lru.put(1, 1)
    
    # Put 2,2
    lru.put(2, 2)
    
    # Get 1 - should return 1
    result1 = lru.get(1)
    assert result1 == 1, f"Test 1 failed: expected 1, got {result1}"
    
    # Put 3,3 - should evict key 2
    lru.put(3, 3)
    
    # Get 2 - should return -1 (not found)
    result2 = lru.get(2)
    assert result2 == -1, f"Test 2 failed: expected -1, got {result2}"
    
    # Put 4,4 - should evict key 1
    lru.put(4, 4)
    
    # Get 1 - should return -1 (not found)
    result3 = lru.get(1)
    assert result3 == -1, f"Test 3 failed: expected -1, got {result3}"
    
    # Get 3 - should return 3
    result4 = lru.get(3)
    assert result4 == 3, f"Test 4 failed: expected 3, got {result4}"
    
    # Get 4 - should return 4
    result5 = lru.get(4)
    assert result5 == 4, f"Test 5 failed: expected 4, got {result5}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_lru_cache()