"""
Exercise 12: Implement Trie (Prefix Tree)
=========================================

Problem Statement:
Implement a trie (prefix tree) data structure with the following methods:
- insert(word): Insert a word into the trie
- search(word): Return True if word exists in trie
- startsWith(prefix): Return True if there's a word with given prefix

Example:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]

Approach:
Trie node structure:
- Each node contains a dictionary of child nodes
- Boolean flag to mark end of word
- For insertion, traverse/create nodes for each character
- For search, traverse nodes and check end flag
- For prefix, just check if path exists

Time Complexity:
- Insert: O(m) where m is word length
- Search: O(m) where m is word length
- StartsWith: O(m) where m is prefix length

Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words, M is average word length
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """Initialize empty trie with root node."""
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insert word into trie.
        
        Args:
            word (str): Word to insert
        """
        node = self.root
        
        # Traverse/create nodes for each character
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        # Mark end of word
        node.is_end_of_word = True
    
    def search(self, word):
        """
        Search for complete word in trie.
        
        Args:
            word (str): Word to search for
            
        Returns:
            bool: True if word exists, False otherwise
        """
        node = self.root
        
        # Traverse nodes for each character
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Word exists only if end flag is set
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if any word in trie starts with given prefix.
        
        Args:
            prefix (str): Prefix to check
            
        Returns:
            bool: True if prefix exists, False otherwise
        """
        node = self.root
        
        # Traverse nodes for each character in prefix
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Prefix exists if path is valid
        return True

# Test Cases
if __name__ == "__main__":
    # Initialize trie
    trie = Trie()
    
    # Test Case 1: Insert words
    trie.insert("apple")
    print("Inserted 'apple'")
    
    # Test Case 2: Search existing word
    result1 = trie.search("apple")
    print(f"Search 'apple': {result1}")  # Expected: True
    
    # Test Case 3: Search non-existing word
    result2 = trie.search("app")
    print(f"Search 'app': {result2}")  # Expected: False
    
    # Test Case 4: Check prefix
    result3 = trie.starts_with("app")
    print(f"Starts with 'app': {result3}")  # Expected: True
    
    # Test Case 5: Insert another word
    trie.insert("app")
    print("Inserted 'app'")
    
    # Test Case 6: Search newly inserted word
    result4 = trie.search("app")
    print(f"Search 'app': {result4}")  # Expected: True