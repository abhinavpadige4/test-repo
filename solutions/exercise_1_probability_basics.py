\"\"\"
Exercise 1: Probability Basics
Topic: Probability theory
Difficulty: Easy

Problem Statement:
Given a fair six-sided die, calculate the probability of rolling an even number.

Solution:
Define sample space S = {1,2,3,4,5,6}. Even numbers = {2,4,6}. Probability = |even|/|S| = 3/6 = 0.5.

Write a function that returns this probability.
\"\"\"

def probability_even_die():
    \"\"\"Return probability of rolling an even number on a fair six-sided die.\"\"\"
    return 3 / 6

# Test cases
if __name__ == \"__main__\":
    # Test 1
    result = probability_even_die()
    expected = 0.5
    print(f\"Test 1 - Probability of even: {result} (expected {expected})\")
    assert abs(result - expected) < 1e-9, \"Test 1 failed\"
    print(\"Test 1 passed\")
    
    # Additional sanity: probability of odd
    def probability_odd_die():
        return 3 / 6
    assert probability_odd_die() == 0.5
    print(\"Sanity check passed\")
    
    print(\"All tests passed.\")
\"\"\"