\"\"\"
Exercise 6: Container With Most Water

Problem Statement:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Examples:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
\"\"\"

def max_area_brute_force(height):
    \"\"\"
    Find the maximum area between two lines using brute force approach.
    
    Args:
        height (List[int]): Array representing heights of vertical lines
    
    Returns:
        int: Maximum area of water that can be stored
        
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    \"\"\"
    max_area = 0
    n = len(height)
    
    # Check all possible pairs of lines
    for i in range(n):
        for j in range(i + 1, n):
            # Area is width * height (minimum of the two lines)
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    
    return max_area

def max_area_two_pointers(height):
    \"\"\"
    Find the maximum area between two lines using two pointers approach.
    
    The key insight is that we start with the widest possible container and move
    the pointer pointing to the shorter line inward, since moving the taller
    line inward would only decrease the area.
    
    Args:
        height (List[int]): Array representing heights of vertical lines
    
    Returns:
        int: Maximum area of water that can be stored
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    \"\"\"
    left = 0
    right = len(height) - 1
    max_area = 0
    
    # Move pointers toward each other
    while left < right:
        # Calculate area with current pointers
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line
        # because moving the taller line won't help increase area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test cases
if __name__ == \"__main__\": 
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = max_area_two_pointers(height1)
    print(f\"Test 1: height = {height1}\")
    print(f\"Expected: 49, Got: {result1}\")
    assert result1 == 49
    
    # Test case 2
    height2 = [1, 1]
    result2 = max_area_two_pointers(height2)
    print(f\"\\nTest 2: height = {height2}\")
    print(f\"Expected: 1, Got: {result2}\")
    assert result2 == 1
    
    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    result3 = max_area_two_pointers(height3)
    print(f\"\\nTest 3: height = {height3}\")
    print(f\"Expected: 16, Got: {result3}\")
    assert result3 == 16
    
    # Test case 4
    height4 = [1, 2, 1]
    result4 = max_area_two_pointers(height4)
    print(f\"\\nTest 4: height = {height4}\")
    print(f\"Expected: 2, Got: {result4}\")
    assert result4 == 2
    
    # Compare approaches for a smaller example
    height5 = [1, 8, 6, 2, 5]
    brute_result = max_area_brute_force(height5)
    optimal_result = max_area_two_pointers(height5)
    
    print(f\"\\nComparison for height = {height5}:\")
    print(f\"Brute Force Result: {brute_result}\")
    print(f\"Two Pointers Result: {optimal_result}\")
    assert brute_result == optimal_result
    
    print(\"\\nAll tests passed!\")