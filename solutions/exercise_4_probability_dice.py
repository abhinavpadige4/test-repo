\"\"\"
Exercise 4: Probability Calculation - Dice Roll
Topic: Statistics and Probability
Difficulty: Easy

Problem Statement:
Write a Python function that calculates the probability of getting a sum of 7 when rolling two fair six-sided dice.
The function should also return the number of favorable outcomes and total possible outcomes.

Requirements:
- Return a dictionary with keys: 'probability', 'favorable_outcomes', 'total_outcomes'
- Probability should be a float rounded to 4 decimal places
- List all favorable outcomes as tuples (die1, die2)
- Assume two fair six-sided dice (values 1-6)

Example:
Favorable outcomes for sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) -> 6 outcomes
Total outcomes: 6 * 6 = 36
Probability: 6/36 = 0.1667
\"\"\"

from typing import List, Tuple, Dict, Union

def dice_sum_probability(target_sum: int = 7) -> Dict[str, Union[float, int, List[Tuple[int, int]]]]:
    """
    Calculate the probability of getting a target sum when rolling two six-sided dice.
    
    Args:
        target_sum: The desired sum (default 7)
        
    Returns:
        Dictionary containing:
        - probability: float rounded to 4 decimal places
        - favorable_outcomes: list of tuples (die1, die2) that sum to target
        - total_outcomes: total number of possible outcomes (36)
    """
    favorable = []
    total_outcomes = 6 * 6  # 36
    
    # Generate all possible outcomes
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            if die1 + die2 == target_sum:
                favorable.append((die1, die2))
    
    probability = len(favorable) / total_outcomes
    
    return {
        'probability': round(probability, 4),
        'favorable_outcomes': favorable,
        'total_outcomes': total_outcomes
    }

# Test cases
if __name__ == "__main__":
    # Test case 1: Sum of 7 (default)
    result1 = dice_sum_probability(7)
    print("Test 1 - Probability of sum 7:")
    print(f"Probability: {result1['probability']}")
    print(f"Favorable outcomes: {result1['favorable_outcomes']}")
    print(f"Total outcomes: {result1['total_outcomes']}")
    assert result1['probability'] == 0.1667
    assert len(result1['favorable_outcomes']) == 6
    assert result1['total_outcomes'] == 36
    expected_favorable = [(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)]
    assert set(result1['favorable_outcomes']) == set(expected_favorable)
    print("✓ Test 1 passed\\n")
    
    # Test case 2: Sum of 2 (minimum)
    result2 = dice_sum_probability(2)
    print("Test 2 - Probability of sum 2:")
    print(f"Probability: {result2['probability']}")
    print(f"Favorable outcomes: {result2['favorable_outcomes']}")
    assert result2['probability'] == 0.0278  # 1/36 ≈ 0.0278
    assert result2['favorable_outcomes'] == [(1,1)]
    print("✓ Test 2 passed\\n")
    
    # Test case 3: Sum of 12 (maximum)
    result3 = dice_sum_probability(12)
    print("Test 3 - Probability of sum 12:")
    print(f"Probability: {result3['probability']}")
    print(f"Favorable outcomes: {result3['favorable_outcomes']}")
    assert result3['probability'] == 0.0278  # 1/36 ≈ 0.0278
    assert result3['favorable_outcomes'] == [(6,6)]
    print("✓ Test 3 passed\\n")
    
    # Test case 4: Sum of 13 (impossible)
    result4 = dice_sum_probability(13)
    print("Test 4 - Probability of sum 13 (impossible):")
    print(f"Probability: {result4['probability']}")
    print(f"Favorable outcomes: {result4['favorable_outcomes']}")
    assert result4['probability'] == 0.0
    assert result4['favorable_outcomes'] == []
    print("✓ Test 4 passed\\n")
    
    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(1) - fixed 36 iterations (constant)
# Space Complexity: O(1) - stores at most 6 favorable outcomes