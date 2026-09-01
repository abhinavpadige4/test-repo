\"\"\"
Exercise 11: Dictionary - Word Count
Topic: Dictionaries
Difficulty: Medium

Problem Statement:
Write a function that takes a string and returns a dictionary with the frequency of each word.
Ignore punctuation and consider words case-insensitive.

Solution:
\"\"\"
import re
from collections import defaultdict

def word_count(text):
    """
    Count the frequency of each word in the given text.
    
    Args:
        text: Input string
        
    Returns:
        Dictionary mapping words to their counts
    """
    # Convert to lowercase and split by non-alphanumeric characters
    words = re.findall(r'\\b[\\w]+\\b', text.lower())
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1
    return dict(freq)

def main():
    # Example usage
    sample = "Hello world! Hello everyone. This is a test. Test, test, test!"
    result = word_count(sample)
    print("Word frequencies:")
    for word, count in sorted(result.items()):
        print(f"  {word}: {count}")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple sentence
    assert word_count("Hello hello world") == {"hello": 2, "world": 1}, "Test 1 failed"
    print("Test Case 1 Passed: 'Hello hello world'")
    
    # Test Case 2: With punctuation
    assert word_count("Hello, world! World is great.") == {"hello": 1, "world": 2, "is": 1, "great": 1}, "Test 2 failed"
    print("Test Case 2 Passed: With punctuation")
    
    # Test Case 3: Empty string
    assert word_count("") == {}, "Test 3 failed"
    print("Test Case 3 Passed: Empty string")
    
    # Test Case 4: Single word repeated
    assert word_count("test test test test") == {"test": 4}, "Test 4 failed"
    print("Test Case 4 Passed: Single word repeated")
    
    # Test Case 5: Mixed case and numbers
    assert word_count("Python3 is great. python3 is fun.") == {"python3": 2, "is": 2, "great": 1, "fun": 1}, "Test 5 failed"
    print("Test Case 5 Passed: Mixed case and numbers")
    
    print("\\nAll tests passed!")