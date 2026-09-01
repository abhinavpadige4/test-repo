\"\"\"
Exercise 16: LRU Cache
Topic: Design / Hash Table + Doubly Linked List
Difficulty: Hard

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Solution:
\"\"\"
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache.
        
        Args:
            capacity (int): Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # Map key to node
        # Dummy head and tail for the doubly linked list
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Add node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Return the value of the key if exists, otherwise -1.
        Also move the accessed node to the head (most recently used).
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Update the value if key exists, else insert.
        If cache exceeds capacity, remove the least recently used item (before tail).
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            if len(self.cache) > self.capacity:
                # Remove the node before tail (LRU)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

# Test cases
if __name__ == "__main__":
    # Test Case 1: Basic operations
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"Test Case 1: cache.get(1) = {cache.get(1)}")  # Expected: 1
    cache.put(3, 3)  # Evicts key 2
    print(f"Test Case 2: cache.get(2) = {cache.get(2)}")  # Expected: -1
    cache.put(4, 4)  # Evicts key 1
    print(f"Test Case 3: cache.get(1) = {cache.get(1)}")  # Expected: -1
    print(f"Test Case 4: cache.get(3) = {cache.get(3)}")  # Expected: 3
    print(f"Test Case 5: cache.get(4) = {cache.get(4)}")  # Expected: 4

# Complexity Analysis:
# Time Complexity: O(1) for both get and put operations
# Space Complexity: O(capacity) - the cache stores at most capacity items