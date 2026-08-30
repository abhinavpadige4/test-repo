\"\"\"
Exercise 4: NumPy Array Operations (Easy)
Problem Statement:
Perform the following operations using NumPy:
1. Create a 1D array of numbers from 0 to 9.
2. Create a 2D array (3x3) with values from 1 to 9.
3. Perform element-wise addition, multiplication, and matrix multiplication.
4. Compute mean, median, std, and sum along axes.
5. Reshape and flatten arrays.

Expected Output:
- Print results of each operation.

Solution:
\"\"\"
import numpy as np

def numpy_operations():
    # 1. Create 1D array
    arr1d = np.arange(10)
    print("1D array (0-9):", arr1d)
    
    # 2. Create 2D array 3x3
    arr2d = np.arange(1, 10).reshape(3, 3)
    print("\n2D array (3x3):")
    print(arr2d)
    
    # 3. Element-wise operations
    arr1d_slice = arr1d[:9]  # first 9 elements to match shape
    add_result = arr1d_slice + arr2d.flatten()
    mul_result = arr1d_slice * arr2d.flatten()
    print("\nElement-wise addition (1D slice + flattened 2D):", add_result)
    print("Element-wise multiplication:", mul_result)
    
    # Matrix multiplication (2D @ 2D.T)
    mat_mul = arr2d @ arr2d.T
    print("\nMatrix multiplication (arr2d @ arr2d.T):")
    print(mat_mul)
    
    # 4. Statistical operations
    print("\nStatistics for arr2d:")
    print(f"Mean: {np.mean(arr2d):.2f}")
    print(f"Median: {np.median(arr2d):.2f}")
    print(f"Std: {np.std(arr2d):.2f}")
    print(f"Sum: {np.sum(arr2d)}")
    print(f"Mean per column: {np.mean(arr2d, axis=0)}")
    print(f"Sum per row: {np.sum(arr2d, axis=1)}")
    
    # 5. Reshape and flatten
    arr_reshaped = arr2d.reshape(9, 1)
    arr_flattened = arr2d.flatten()
    print("\nReshaped to (9,1):")
    print(arr_reshaped)
    print("Flattened:", arr_flattened)
    
    # Test cases
    assert arr1d.shape == (10,), "1D array shape incorrect"
    assert arr2d.shape == (3, 3), "2D array shape incorrect"
    assert np.sum(arr2d) == 45, "Sum of 2D array should be 45"
    assert np.mean(arr2d) == 5.0, "Mean of 2D array should be 5.0"
    print("\nAll tests passed!")

if __name__ == "__main__":
    numpy_operations()
\"\"\"
Time Complexity: Most operations are O(n) where n is number of elements.
Space Complexity: O(n) for storing arrays.
\"\"\"