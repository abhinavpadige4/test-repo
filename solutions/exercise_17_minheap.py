\"\"\"
Exercise 17: Min Heap Implementation
Topic: Heap Data Structure
Difficulty: Hard

Problem Statement:
Implement a Min Heap with the following operations:
- insert(item): Insert a new item into the heap
- extract_min(): Remove and return the minimum item
- get_min(): Return the minimum item without removing it
- size(): Return the number of items in the heap

Solution:
\"\"\"
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, i):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def _heapify_down(self, i):
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self._swap(i, smallest)
            self._heapify_down(smallest)

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def get_min(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

def main():
    # Example usage
    heap = MinHeap()
    elements = [5, 3, 8, 1, 2, 7, 9]
    for el in elements:
        heap.insert(el)
        print(f"After inserting {el}: {heap.heap}")

    print("\\nExtracting min elements:")
    while heap.size() > 0:
        print(f"Extracted: {heap.extract_min()}, Remaining: {heap.heap}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Insert and get_min
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    assert heap.get_min() == 3, "Test 1 failed"
    print("Test Case 1 Passed: get_min after inserts")
    
    # Test Case 2: Extract min
    assert heap.extract_min() == 3, "Test 2 failed: first extract"
    assert heap.extract_min() == 5, "Test 2 failed: second extract"
    assert heap.extract_min() == 8, "Test 2 failed: third extract"
    assert heap.extract_min() is None, "Test 2 failed: extract from empty"
    print("Test Case 2 Passed: extract_min")
    
    # Test Case 3: Size
    heap.insert(10)
    heap.insert(20)
    assert heap.size() == 2, "Test 3 failed: size"
    print("Test Case 3 Passed: size")
    
    # Test Case 4: Insert descending order
    heap2 = MinHeap()
    for i in range(5, 0, -1):
        heap2.insert(i)
    # Extract should give 1,2,3,4,5
    for expected in range(1, 6):
        assert heap2.extract_min() == expected, f"Test 4 failed: expected {expected}"
    print("Test Case 4 Passed: descending order")
    
    # Test Case 5: Duplicate values
    heap3 = MinHeap()
    heap3.insert(5)
    heap3.insert(5)
    heap3.insert(1)
    assert heap3.extract_min() == 1, "Test 5 failed: duplicate min"
    assert heap3.extract_min() == 5, "Test 5 failed: duplicate 5"
    assert heap3.extract_min() == 5, "Test 5 failed: second duplicate 5"
    print("Test Case 5 Passed: duplicates")
    
    print("\\nAll tests passed!")