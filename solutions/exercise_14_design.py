"""
Exercise 14: LRU Cache
======================

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
- int get(int key): Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value): Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache.
  If the number of keys exceeds the capacity, evict the least recently used key.

Approach:
Combine hash map (dictionary) for O(1) lookup and doubly linked list for O(1) reordering:
- Hash map stores key -> Node mapping
- Doubly linked list maintains usage order (most recent at head, least at tail)
- On get/put, move accessed node to head
- When capacity exceeded, remove tail node

Time Complexity:
- get: O(1)
- put: O(1)

Space Complexity: O(capacity)
"""

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        Initialize LRU Cache with given capacity.
        
        Args:
            capacity (int): Maximum number of entries cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # key -> Node
        
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        """Remove node from doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node):
        """Add node right after head (mark as most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_head(self, node):
        """Move existing node to head (mark as recently used)."""
        self._remove_node(node)
        self._add_to_head(node)
    
    def _pop_tail(self):
        """Remove and return the least recently used node (tail)."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
    
    def get(self, key):
        """
        Get value for key if exists, otherwise return -1.
        
        Args:
            key (int): Key to look up
            
        Returns:
            int: Value if key exists, -1 otherwise
        """
        node = self.cache.get(key)
        
        if not node:
            return -1
        
        # Move accessed node to head
        self._move_to_head(node)
        return node.value
    
    def put(self, key, value):
        """
        Insert or update key-value pair in cache.
        
        Args:
            key (int): Key to insert/update
            value (int): Value to insert/update
        """
        node = self.cache.get(key)
        
        if not node:
            # Create new node
            new_node = Node(key, value)
            
            # Add to cache
            self.cache[key] = new_node
            
            # Add to head
            self._add_to_head(new_node)
            
            # Evict LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                # Remove tail node
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
        else:
            # Update existing node
            node.value = value
            self._move_to_head(node)

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic operations
    lru_cache = LRUCache(2)
    
    lru_cache.put(1, 1)  # cache is {1=1}
    print("Put (1, 1)")
    
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}
    print("Put (2, 2)")
    
    result1 = lru_cache.get(1)  # return 1
    print(f"Get 1: {result1}")
    
    lru_cache.put(3, 3)  # LRU key 2 is evicted, cache is {1=1, 3=3}
    print("Put (3, 3) - evicts key 2")
    
    result2 = lru_cache.get(2)  # returns -1 (not found)
    print(f"Get 2: {result2}")
    
    lru_cache.put(4, 4)  # LRU key 1 is evicted, cache is {4=4, 3=3}
    print("Put (4, 4) - evicts key 1")
    
    result3 = lru_cache.get(1)  # return -1 (not found)
    print(f"Get 1: {result3}")
    
    result4 = lru_cache.get(3)  # return 3
    print(f"Get 3: {result4}")
    
    result5 = lru_cache.get(4)  # return 4
    print(f"Get 4: {result5}")