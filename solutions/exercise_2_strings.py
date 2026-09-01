"""
Exercise 2: Reverse String (Easy)
Problem Statement:
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Examples:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ascii character
"""

def reverse_string(s):
    """
    Reverses a string in-place using two pointers approach.
    
    Args:
        s (List[str]): Array of characters representing the string
    
    Returns:
        None: Modifies the input list in-place
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    # Swap characters from both ends moving toward center
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = ["h","e","l","l","o"]
    print(f"Test 1 - Input: {s1}")
    reverse_string(s1)
    print(f"Output: {s1}")
    print(f"Expected: ['o','l','l','e','h']")
    print(f"Pass: {s1 == ['o','l','l','e','h']}\\n")
    
    # Test Case 2
    s2 = ["H","a","n","n","a","h"]
    print(f"Test 2 - Input: {s2}")
    reverse_string(s2)
    print(f"Output: {s2}")
    print(f"Expected: ['h','a','n','n','a','H']")
    print(f"Pass: {s2 == ['h','a','n','n','a','H']}\\n")
    
    # Test Case 3
    s3 = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    expected3 = [":","a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]
    print(f"Test 3 - Input: {s3}")
    reverse_string(s3)
    print(f"Output: {s3}")
    print(f"Expected: {expected3}")
    print(f"Pass: {s3 == expected3}\\n")