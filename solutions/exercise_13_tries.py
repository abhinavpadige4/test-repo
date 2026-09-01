"""
Exercise 13: Implement Trie (Prefix Tree)
=========================================

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
Implement the Trie class with the following methods:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string with the given prefix.

Examples:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Approach:
Use a tree structure where each node represents a character.
Each node has:
1. A dictionary of children nodes
2. A flag indicating if node represents end of a word

Time Complexity:
- Insert: O(m) where m is length of word
- Search: O(m) where m is length of word
- StartsWith: O(m) where m is length of prefix

Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words and M is average length
"""

class TrieNode:
    def __init__(self):
        """
        Initialize a Trie node.
        """
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize the trie with a root node.
        """
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insert a word into the trie.
        
        Args:
            word (str): Word to insert
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word):
        """
        Search if a word exists in the trie.
        
        Args:
            word (str): Word to search
            
        Returns:
            bool: True if word exists, False otherwise
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """
        Check if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix (str): Prefix to check
            
        Returns:
            bool: True if prefix exists, False otherwise
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True

# Test cases
def test_trie():
    # Test case 1: Basic operations
    trie = Trie()
    
    # Insert "apple"
    trie.insert("apple")
    
    # Search "apple" - should return True
    result1 = trie.search("apple")
    assert result1 == True, f"Test 1 failed: expected True, got {result1}"
    
    # Search "app" - should return False (not complete word)
    result2 = trie.search("app")
    assert result2 == False, f"Test 2 failed: expected False, got {result2}"
    
    # startsWith "app" - should return True
    result3 = trie.starts_with("app")
    assert result3 == True, f"Test 3 failed: expected True, got {result3}"
    
    # Insert "app"
    trie.insert("app")
    
    # Search "app" - should return True now
    result4 = trie.search("app")
    assert result4 == True, f"Test 4 failed: expected True, got {result4}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_trie()