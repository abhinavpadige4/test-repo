"""
Exercise 11: 3Sum (Medium)
Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Examples:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []

Input: nums = [0,0,0]
Output: [[0,0,0]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""

def three_sum(nums):
    """
    Find all unique triplets in the array which gives the sum of zero.
    
    Args:
        nums (List[int]): Array of integers
    
    Returns:
        List[List[int]]: All unique triplets that sum to zero
        
    Time Complexity: O(n^2) where n is the length of the array
    Space Complexity: O(1) ignoring the space used for output
    """
    # Sort the array to enable two-pointer technique and easy duplicate handling
    nums.sort()
    result = []
    
    # Iterate through each element as the first element of triplet
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # If the smallest number is positive, no more triplets possible
        if nums[i] > 0:
            break
        
        # Use two pointers to find the other two elements
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
            elif current_sum < 0:
                # Sum is too small, move left pointer right
                left += 1
            else:
                # Sum is too large, move right pointer left
                right -= 1
    
    return result

# Alternative approach using hash set (less efficient but different perspective)
def three_sum_hash(nums):
    """
    Alternative approach using hash set to find triplets.
    
    Args:
        nums (List[int]): Array of integers
    
    Returns:
        List[List[int]]: All unique triplets that sum to zero
        
    Time Complexity: O(n^2) where n is the length of the array
    Space Complexity: O(n) for the hash set
    """
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Create a set to store visited elements in current iteration
        seen = set()
        target = -nums[i]
        
        for j in range(i + 1, len(nums)):
            complement = target - nums[j]
            
            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                # Skip duplicates for the third element
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            
            seen.add(nums[j])
    
    return result

# Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1,0,1,2,-1,-4]
    result1 = three_sum(nums1)
    print(f"Test 1 - Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[-1,-1,2],[-1,0,1]]")
    print(f"Pass: {sorted(result1) == sorted([[-1,-1,2],[-1,0,1]])}\\n")
    
    # Test Case 2
    nums2 = [0,1,1]
    result2 = three_sum(nums2)
    print(f"Test 2 - Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print(f"Pass: {result2 == []}\\n")
    
    # Test Case 3
    nums3 = [0,0,0]
    result3 = three_sum(nums3)
    print(f"Test 3 - Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [[0,0,0]]")
    print(f"Pass: {result3 == [[0,0,0]]}\\n")
    
    # Test Case 4
    nums4 = [-2,0,1,1,2]
    result4 = three_sum(nums4)
    print(f"Test 4 - Input: {nums4}")
    print(f"Output: {result4}")
    expected4 = [[-2,0,2],[-2,1,1]]
    print(f"Expected: {expected4}")
    print(f"Pass: {sorted(result4) == sorted(expected4)}\\n")