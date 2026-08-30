\"\"\"
Exercise 9: Statistics - Descriptive Statistics and Probability
Difficulty: Easy
Topic: Statistics

Problem Statement:
Write a Python script to:
1. Calculate measures of central tendency (mean, median, mode) for a given list of numbers
2. Calculate measures of dispersion (variance, standard deviation, range)
3. Calculate basic probability: probability of drawing a red card from a standard deck of 52 cards
4. Calculate the probability of rolling a sum of 7 with two six-sided dice

Expected Output:
Data: [1, 2, 2, 3, 4, 7, 9, 9, 9, 10]
Mean: 5.6
Median: 5.5
Mode: 9
Variance: 10.84
Standard Deviation: 3.29
Range: 9
Probability of drawing a red card: 0.5
Probability of rolling a sum of 7 with two dice: 0.16666666666666666
\"\"\"

import statistics
from collections import Counter

def descriptive_statistics_and_probability():
    """
    Calculate descriptive statistics and basic probabilities.
    Returns:
        dict: Results for testing
    """
    # Data set
    data = [1, 2, 2, 3, 4, 7, 9, 9, 9, 10]
    
    # 1. Measures of central tendency
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    # Mode: handle multiple modes by taking the first one if multiple
    mode_val = statistics.mode(data)  # This will raise an error if multiple modes, but we have a single mode (9)
    
    # 2. Measures of dispersion
    variance_val = statistics.variance(data)
    stdev_val = statistics.stdev(data)
    data_range = max(data) - min(data)
    
    # 3. Probability: red card from a standard deck
    # Standard deck: 52 cards, 26 red (hearts and diamonds)
    prob_red_card = 26 / 52
    
    # 4. Probability: sum of 7 with two six-sided dice
    # Total outcomes: 6 * 6 = 36
    # Favorable outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) -> 6
    prob_sum_7 = 6 / 36
    
    # Print results
    print(f"Data: {data}")
    print(f"Mean: {mean_val}")
    print(f"Median: {median_val}")
    print(f"Mode: {mode_val}")
    print(f"Variance: {variance_val:.2f}")
    print(f"Standard Deviation: {stdev_val:.2f}")
    print(f"Range: {data_range}")
    print(f"Probability of drawing a red card: {prob_red_card}")
    print(f"Probability of rolling a sum of 7 with two dice: {prob_sum_7}")
    
    # Return for testing
    return {
        "data": data,
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "variance": variance_val,
        "stdev": stdev_val,
        "range": data_range,
        "prob_red_card": prob_red_card,
        "prob_sum_7": prob_sum_7
    }

# Test cases
if __name__ == "__main__":
    result = descriptive_statistics_and_probability()
    
    # Test 1: Mean
    assert abs(result["mean"] - 5.6) < 0.001, f"Mean failed: {result['mean']}"
    
    # Test 2: Median
    assert abs(result["median"] - 5.5) < 0.001, f"Median failed: {result['median']}"
    
    # Test 3: Mode
    assert result["mode"] == 9, f"Mode failed: {result['mode']}"
    
    # Test 4: Variance
    assert abs(result["variance"] - 10.84) < 0.01, f"Variance failed: {result['variance']}"
    
    # Test 5: Standard Deviation
    assert abs(result["stdev"] - 3.29) < 0.01, f"Standard deviation failed: {result['stdev']}"
    
    # Test 6: Range
    assert result["range"] == 9, f"Range failed: {result['range']}"
    
    # Test 7: Probability of red card
    assert abs(result["prob_red_card"] - 0.5) < 0.001, f"Red card probability failed: {result['prob_red_card']}"
    
    # Test 8: Probability of sum 7
    assert abs(result["prob_sum_7"] - (6/36)) < 0.001, f"Sum of 7 probability failed: {result['prob_sum_7']}"
    
    print("\nAll tests passed!")