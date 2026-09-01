"""
Exercise 2: Word Frequency Counter (Medium)

Problem Statement:
Write a function that counts the frequency of each word in a given text.
Return a dictionary where keys are words (lowercase) and values are their counts.

Requirements:
- Convert all words to lowercase
- Ignore punctuation
- Return the dictionary sorted by frequency (descending), then alphabetically

Example:
Input: "the cat and the dog"
Output: {'the': 2, 'and': 1, 'cat': 1, 'dog': 1}
"""

from collections import Counter
import re


def word_frequency(text: str) -> dict:
    """
    Count word frequencies in a text.
    
    Args:
        text: Input text string
        
    Returns:
        Dictionary of word frequencies sorted by count (desc) then alphabetically
    """
    # Extract words (lowercase, ignore punctuation)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count frequencies
    freq = Counter(words)
    
    # Sort by frequency (descending) then alphabetically
    sorted_freq = dict(sorted(freq.items(), key=lambda x: (-x[1], x[0])))
    
    return sorted_freq


# Test Cases
def test_word_frequency():
    """Test cases for word_frequency function"""
    
    # Test 1: Basic counting
    result1 = word_frequency("the cat and the dog")
    assert result1 == {'the': 2, 'and': 1, 'cat': 1, 'dog': 1}, f"Test 1 failed: {result1}"
    print("✓ Test 1 passed: Basic word counting")
    
    # Test 2: Case insensitivity
    result2 = word_frequency("Hello hello HELLO")
    assert result2 == {'hello': 3}, f"Test 2 failed: {result2}"
    print("✓ Test 2 passed: Case insensitivity")
    
    # Test 3: Punctuation handling
    result3 = word_frequency("Hello, world! Hello... world?")
    assert result3 == {'hello': 2, 'world': 2}, f"Test 3 failed: {result3}"
    print("✓ Test 3 passed: Punctuation handling")
    
    # Test 4: Empty string
    result4 = word_frequency("")
    assert result4 == {}, f"Test 4 failed: {result4}"
    print("✓ Test 4 passed: Empty string")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    print("Running Word Frequency Counter Tests...\n")
    test_word_frequency()