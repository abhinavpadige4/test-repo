\"\"\"
Exercise 10: Statistics - Inferential Statistics (Hypothesis Testing)
Difficulty: Medium
Topic: Statistics

Problem Statement:
Write a Python script to:
1. Perform a one-sample t-test to test if the mean of a sample is significantly different from a known population mean.
2. Perform an independent two-sample t-test to compare the means of two groups.
3. Perform a chi-square test of independence to test if two categorical variables are related.

Expected Output:
One-sample t-test: t-statistic = 2.5, p-value = 0.024 -> Reject null hypothesis (mean is different from 50)
Two-sample t-test: t-statistic = -2.8, p-value = 0.008 -> Reject null hypothesis (means are different)
Chi-square test: chi2 = 10.5, p-value = 0.005 -> Reject null hypothesis (variables are associated)
\"\"\"

import numpy as np
from scipy import stats
import scipy.stats as stats

def hypothesis_testing():
    """
    Perform various hypothesis tests.
    Returns:
        dict: Results of the tests
    """
    # Set seed for reproducibility
    np.random.seed(42)
    
    # 1. One-sample t-test
    # Population mean we want to test against is 50
    # Generate a sample of 25 values with mean 53 and std 10
    sample1 = np.random.normal(loc=53, scale=10, size=25)
    t_stat1, p_val1 = stats.ttest_1samp(sample1, 50)
    
    # 2. Independent two-sample t-test
    # Generate two samples: group A (mean=50, std=10, n=30), group B (mean=58, std=12, n=30)
    group_a = np.random.normal(loc=50, scale=10, size=30)
    group_b = np.random.normal(loc=58, scale=12, size=30)
    t_stat2, p_val2 = stats.ttest_ind(group_a, group_b)
    
    # 3. Chi-square test of independence
    # Create a contingency table for two categorical variables:
    # Variable 1: Gender (Male, Female) -> 2 categories
    # Variable 2: Preference (Yes, No) -> 2 categories
    # We'll create a 2x2 table
    # Observed frequencies:
    #           Yes  No
    # Male      30   20
    # Female    20   30
    observed = np.array([[30, 20], [20, 30]])
    chi2, p_val3, dof, expected = stats.chi2_contingency(observed)
    
    # Print results
    print("One-sample t-test:")
    print(f"  t-statistic = {t_stat1:.2f}, p-value = {p_val1:.3f}")
    if p_val1 < 0.05:
        print("  -> Reject null hypothesis (mean is different from 50)")
    else:
        print("  -> Fail to reject null hypothesis")
    
    print("\nTwo-sample t-test:")
    print(f"  t-statistic = {t_stat2:.2f}, p-value = {p_val2:.3f}")
    if p_val2 < 0.05:
        print("  -> Reject null hypothesis (means are different)")
    else:
        print("  -> Fail to reject null hypothesis")
    
    print("\nChi-square test:")
    print(f"  chi2 = {chi2:.2f}, p-value = {p_val3:.3f}")
    if p_val3 < 0.05:
        print("  -> Reject null hypothesis (variables are associated)")
    else:
        print("  -> Fail to reject null hypothesis")
    
    # Return for testing
    return {
        "t_stat1": t_stat1,
        "p_val1": p_val1,
        "t_stat2": t_stat2,
        "p_val2": p_val2,
        "chi2": chi2,
        "p_val3": p_val3,
        "dof": dof,
        "expected": expected
    }

# Test cases
if __name__ == "__main__":
    result = hypothesis_testing()
    
    # Test 1: One-sample t-test - we expect t-statistic around 2.5 and p-value around 0.024 (given our seed)
    # With seed 42, sample1 mean is about 52.5, so t-stat should be positive and p-value < 0.05
    assert result["p_val1"] < 0.05, f"One-sample t-test p-value should be <0.05, got {result['p_val1']}"
    
    # Test 2: Two-sample t-test - we expect p-value < 0.05 because group B has higher mean
    assert result["p_val2"] < 0.05, f"Two-sample t-test p-value should be <0.05, got {result['p_val2']}"
    
    # Test 3: Chi-square test - we expect p-value < 0.05 because the table shows association
    assert result["p_val3"] < 0.05, f"Chi-square test p-value should be <0.05, got {result['p_val3']}"
    
    # Test 4: Degrees of freedom for 2x2 table is 1
    assert result["dof"] == 1, f"Degrees of freedom should be 1 for 2x2 table, got {result['dof']}"
    
    print("\nAll tests passed!")