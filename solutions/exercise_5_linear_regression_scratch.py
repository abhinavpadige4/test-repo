\"\"\"
Exercise 5: Simple Linear Regression from Scratch
Topic: Machine Learning Algorithms
Difficulty: Medium

Problem Statement:
Implement simple linear regression from scratch using gradient descent.
Given a dataset of (x, y) points, find the best fit line y = mx + b.

Requirements:
- Implement gradient descent to minimize mean squared error (MSE)
- Function should take learning rate, number of iterations, and return slope (m) and intercept (b)
- Include a function to predict y values given x
- Handle edge cases like empty dataset
- Return the final m, b, and cost history

Example:
Input: x = [1, 2, 3, 4, 5], y = [2, 4, 5, 4, 5]
Output: m ≈ 0.6, b ≈ 2.2 (approximate values)
\"\"\"

import numpy as np
from typing import List, Tuple, Optional

def linear_regression_gradient_descent(
    x: List[float], 
    y: List[float], 
    learning_rate: float = 0.01, 
    n_iterations: int = 1000
) -> Tuple[float, float, List[float]]:
    """
    Perform simple linear regression using gradient descent.
    
    Args:
        x: List of independent variable values
        y: List of dependent variable values
        learning_rate: Step size for gradient descent (default 0.01)
        n_iterations: Number of iterations to run gradient descent (default 1000)
        
    Returns:
        Tuple of (slope, intercept, cost_history)
        cost_history: List of MSE values at each iteration
    """
    # Convert to numpy arrays for easier computation
    x_arr = np.array(x, dtype=float)
    y_arr = np.array(y, dtype=float)
    
    # Handle edge cases
    if len(x_arr) == 0 or len(y_arr) == 0:
        return 0.0, 0.0, []
    if len(x_arr) != len(y_arr):
        raise ValueError("x and y must have the same length")
    
    # Initialize parameters
    m = 0.0  # slope
    b = 0.0  # intercept
    n = len(x_arr)
    
    # To store cost history
    cost_history = []
    
    # Gradient descent
    for i in range(n_iterations):
        # Predictions
        y_pred = m * x_arr + b
        
        # Calculate error
        error = y_pred - y_arr
        
        # Mean Squared Error
        mse = np.mean(error ** 2)
        cost_history.append(mse)
        
        # Gradients
        dm = (2 / n) * np.dot(error, x_arr)
        db = (2 / n) * np.sum(error)
        
        # Update parameters
        m -= learning_rate * dm
        b -= learning_rate * db
    
    return m, b, cost_history

def predict(x: List[float], m: float, b: float) -> List[float]:
    """
    Make predictions using the linear regression model.
    
    Args:
        x: List of input values
        m: Slope
        b: Intercept
        
    Returns:
        List of predicted y values
    """
    return [m * xi + b for xi in x]

# Test cases
if __name__ == "__main__":
    # Test case 1: Simple linear data
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, 4, 5, 4, 5]
    m1, b1, cost1 = linear_regression_gradient_descent(x1, y1, learning_rate=0.01, n_iterations=1000)
    print("Test 1 - Simple linear data:")
    print(f"Slope (m): {m1:.4f}")
    print(f"Intercept (b): {b1:.4f}")
    print(f"Final cost (MSE): {cost1[-1]:.6f}")
    # Expected: m around 0.6, b around 2.2
    assert 0.5 <= m1 <= 0.7, f"Expected m between 0.5 and 0.7, got {m1}"
    assert 2.0 <= b1 <= 2.5, f"Expected b between 2.0 and 2.5, got {b1}"
    print("✓ Test 1 passed\\n")
    
    # Test case 2: Perfect linear relationship
    x2 = [1, 2, 3, 4, 5]
    y2 = [3, 5, 7, 9, 11]  # y = 2x + 1
    m2, b2, cost2 = linear_regression_gradient_descent(x2, y2, learning_rate=0.01, n_iterations=1000)
    print("Test 2 - Perfect linear relationship (y = 2x + 1):")
    print(f"Slope (m): {m2:.4f}")
    print(f"Intercept (b): {b2:.4f}")
    print(f"Final cost (MSE): {cost2[-1]:.6f}")
    assert abs(m2 - 2.0) < 0.01, f"Expected m close to 2.0, got {m2}"
    assert abs(b2 - 1.0) < 0.01, f"Expected b close to 1.0, got {b2}"
    assert cost2[-1] < 0.0001, f"Expected very low cost, got {cost2[-1]}"
    print("✓ Test 2 passed\\n")
    
    # Test case 3: Prediction
    x_test = [6, 7, 8]
    predictions = predict(x_test, m2, b2)
    print("Test 3 - Prediction for x=[6,7,8] using model from Test 2:")
    print(f"Predictions: {predictions}")
    expected = [2*6+1, 2*7+1, 2*8+1]  # [13, 15, 17]
    for i, (pred, exp) in enumerate(zip(predictions, expected)):
        assert abs(pred - exp) < 0.1, f"Prediction {pred} not close to expected {exp}"
    print("✓ Test 3 passed\\n")
    
    # Test case 4: Empty lists
    try:
        m4, b4, cost4 = linear_regression_gradient_descent([], [])
        print("Test 4 - Empty lists:")
        print(f"m: {m4}, b: {b4}, cost_history length: {len(cost4)}")
        assert m4 == 0.0 and b4 == 0.0 and cost4 == []
        print("✓ Test 4 passed\\n")
    except Exception as e:
        print(f"Test 4 failed with exception: {e}")
        raise
    
    print("All tests passed!")

# Complexity Analysis:
# Time Complexity: O(n * iterations) where n is number of data points
# Space Complexity: O(iterations) for storing cost history