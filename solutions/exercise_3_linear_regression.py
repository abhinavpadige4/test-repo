\"\"\"
Exercise 3: Simple Linear Regression from Scratch (Medium)
Problem Statement:
Implement a simple linear regression model (y = mx + b) using gradient descent.
Write a function `linear_regression(X, y, learning_rate=0.01, epochs=1000)` that:
- Takes list of features X (independent variable) and target y (dependent variable)
- Returns tuple (m, b) after training using gradient descent to minimize MSE.
- Also return the final MSE.

Assume X and y are lists of equal length, numeric.

Test Cases:
1. Perfect linear data: X=[1,2,3,4,5], y=[2,4,6,8,10] -> m≈2, b≈0, MSE≈0
2. Noisy data: X=[1,2,3,4,5], y=[2.1,3.9,6.2,8.1,9.8] -> m close to 2, b close to 0
3. Constant y: X=[1,2,3,4,5], y=[5,5,5,5,5] -> m≈0, b≈5
\"\"\"
def linear_regression(X, y, learning_rate=0.01, epochs=1000):
    """
    Perform simple linear regression using gradient descent.
    
    Args:
        X (list): List of feature values.
        y (list): List of target values.
        learning_rate (float): Step size for gradient descent.
        epochs (int): Number of iterations.
    
    Returns:
        tuple: (m, b, final_mse) where m is slope, b is intercept.
    """
    n = len(X)
    if n == 0:
        return 0, 0, 0
    
    # Initialize parameters
    m = 0.0
    b = 0.0
    
    for epoch in range(epochs):
        # Predictions
        y_pred = [m * x + b for x in X]
        # Errors
        errors = [y_pred[i] - y[i] for i in range(n)]
        # Gradients
        dm = (2/n) * sum([errors[i] * X[i] for i in range(n)])
        db = (2/n) * sum(errors)
        # Update parameters
        m -= learning_rate * dm
        b -= learning_rate * db
    
    # Final MSE
    y_pred_final = [m * x + b for x in X]
    mse = sum([(y_pred_final[i] - y[i]) ** 2 for i in range(n)]) / n
    
    return m, b, mse

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1,2,3,4,5], [2,4,6,8,10]),
        ([1,2,3,4,5], [2.1,3.9,6.2,8.1,9.8]),
        ([1,2,3,4,5], [5,5,5,5,5])
    ]
    
    for i, (X, y) in enumerate(test_cases, 1):
        m, b, mse = linear_regression(X, y, learning_rate=0.01, epochs=2000)
        print(f"Test case {i}:")
        print(f"  X = {X}")
        print(f"  y = {y}")
        print(f"  Learned m = {m:.4f}, b = {b:.4f}, MSE = {mse:.6f}")
        # Simple assertions (allow tolerance)
        if i == 1:
            assert abs(m - 2) < 0.01 and abs(b) < 0.01 and mse < 1e-6, "Test 1 failed"
        elif i == 2:
            assert abs(m - 2) < 0.1 and abs(b) < 0.1, "Test 2 failed"
        elif i == 3:
            assert abs(m) < 0.1 and abs(b - 5) < 0.1, "Test 3 failed"
        print("  Passed\n")
    
    print("All tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(epochs * n) where n is number of samples.
    # Space Complexity: O(1) additional space (not counting input/output).
\"\"\"