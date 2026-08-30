\"\"\"
Exercise 3: NumPy - Arrays and Operations
Difficulty: Easy
Topic: NumPy

Problem Statement:
Write a Python script using NumPy to:
1. Create a 1D array of integers from 0 to 9
2. Create a 2D array (3x3) with values from 1 to 9
3. Perform element-wise addition, multiplication, and power operations
4. Calculate mean, median, and standard deviation of a 1D array
5. Reshape a 1D array of 12 elements into a 3x4 matrix

Expected Output:
1D array: [0 1 2 3 4 5 6 7 8 9]
2D array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Element-wise addition (2D + 10): 
[[11 12 13]
 [14 15 16]
 [17 18 19]]
Element-wise multiplication (2D * 2): 
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
Power operation (2D ** 2): 
[[ 1  4  9]
 [16 25 36]
 [49 64 81]]
Statistics of [1,2,3,4,5,6,7,8,9]: Mean=5.0, Median=5.0, Std=2.58
Reshaped array (12 elements to 3x4):
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
\"\"\"

import numpy as np

def numpy_operations():
    """
    Perform various NumPy operations.
    Returns:
        dict: Results of operations for testing
    """
    # 1. Create 1D array from 0 to 9
    arr_1d = np.arange(10)
    
    # 2. Create 2D array (3x3) with values 1-9
    arr_2d = np.arange(1, 10).reshape(3, 3)
    
    # 3. Element-wise operations
    arr_plus_10 = arr_2d + 10
    arr_times_2 = arr_2d * 2
    arr_power_2 = arr_2d ** 2
    
    # 4. Statistics on 1D array 1-9
    stats_arr = np.arange(1, 10)
    mean_val = np.mean(stats_arr)
    median_val = np.median(stats_arr)
    std_val = np.std(stats_arr)
    
    # 5. Reshape 12 elements to 3x4
    arr_12 = np.arange(1, 13)
    arr_reshaped = arr_12.reshape(3, 4)
    
    # Print results
    print(f"1D array: {arr_1d}")
    print(f"2D array:\n{arr_2d}")
    print(f"Element-wise addition (2D + 10):\n{arr_plus_10}")
    print(f"Element-wise multiplication (2D * 2):\n{arr_times_2}")
    print(f"Power operation (2D ** 2):\n{arr_power_2}")
    print(f"Statistics of {stats_arr}: Mean={mean_val}, Median={median_val}, Std={std_val:.2f}")
    print(f"Reshaped array (12 elements to 3x4):\n{arr_reshaped}")
    
    # Return for testing
    return {
        "arr_1d": arr_1d,
        "arr_2d": arr_2d,
        "arr_plus_10": arr_plus_10,
        "arr_times_2": arr_times_2,
        "arr_power_2": arr_power_2,
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "arr_reshaped": arr_reshaped
    }

# Test cases
if __name__ == "__main__":
    result = numpy_operations()
    
    # Test 1: 1D array
    expected_1d = np.arange(10)
    assert np.array_equal(result["arr_1d"], expected_1d), "1D array creation failed"
    
    # Test 2: 2D array shape and values
    expected_2d = np.arange(1, 10).reshape(3, 3)
    assert np.array_equal(result["arr_2d"], expected_2d), "2D array creation failed"
    
    # Test 3: Addition
    expected_plus = expected_2d + 10
    assert np.array_equal(result["arr_plus_10"], expected_plus), "Addition failed"
    
    # Test 4: Multiplication
    expected_times = expected_2d * 2
    assert np.array_equal(result["arr_times_2"], expected_times), "Multiplication failed"
    
    # Test 5: Power
    expected_power = expected_2d ** 2
    assert np.array_equal(result["arr_power_2"], expected_power), "Power operation failed"
    
    # Test 6: Statistics
    stats_arr = np.arange(1, 10)
    assert abs(result["mean"] - 5.0) < 0.001, "Mean calculation failed"
    assert abs(result["median"] - 5.0) < 0.001, "Median calculation failed"
    assert abs(result["std"] - 2.58) < 0.01, "Std calculation failed"
    
    # Test 7: Reshape
    expected_reshaped = np.arange(1, 13).reshape(3, 4)
    assert np.array_equal(result["arr_reshaped"], expected_reshaped), "Reshape failed"
    
    print("\nAll tests passed!")