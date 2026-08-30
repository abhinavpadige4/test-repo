\"\"\"
Exercise 3: Linear Regression with scikit-learn (Medium)
Problem Statement:
Given a dataset of house sizes (in square feet) and their corresponding prices (in thousands of dollars),
perform a simple linear regression to predict house price based on size.
Steps:
1. Import necessary libraries (numpy, pandas, sklearn, matplotlib).
2. Generate a synthetic dataset for house sizes and prices (or use a provided small dataset).
3. Split the data into training and testing sets (80% train, 20% test).
4. Train a linear regression model.
5. Make predictions on the test set.
6. Evaluate the model using Mean Squared Error (MSE) and R-squared.
7. Plot the regression line and the data points.

Expected Output:
- Printed MSE and R-squared values.
- A scatter plot with the regression line.

Time Complexity: O(n) for training (using normal equation or gradient descent, but sklearn's LinearRegression uses O(n_features^2 * n_samples) for normal equation, which is efficient for small n_features).
Space Complexity: O(n_features^2) for the normal equation approach.
\"\"\"
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def generate_house_data(n_samples=100):
    """
    Generate synthetic house size and price data.
    Price = 50 + 5 * size + noise
    """
    np.random.seed(42)
    size = np.random.randint(500, 4000, n_samples)  # square feet
    price = 50 + 5 * size + np.random.normal(0, 5000, n_samples)  # price in thousands
    return pd.DataFrame({'size': size, 'price': price})

def linear_regression_exercise(data=None):
    """
    Perform linear regression on house size vs price data.

    Parameters:
    data (pd.DataFrame): DataFrame with 'size' and 'price' columns. If None, generate synthetic data.

    Returns:
    tuple: (model, mse, r2, X_test, y_test, y_pred)
    """
    if data is None:
        data = generate_house_data()

    # Features and target
    X = data[['size']]
    y = data['price']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Actual data')
    plt.scatter(X_test, y_pred, color='red', alpha=0.7, label='Predictions')
    # Plot the regression line
    X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(X_line)
    plt.plot(X_line, y_line, color='green', linewidth=2, label='Regression line')
    plt.xlabel('House Size (sq ft)')
    plt.ylabel('Price (thousands $)')
    plt.title('House Price vs Size: Linear Regression')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    return model, mse, r2, X_test, y_test, y_pred

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Test case 1: Using synthetic data
    model, mse, r2, X_test, y_test, y_pred = linear_regression_exercise()
    print(f"Model Coefficient (slope): {model.coef_[0]:.2f}")
    print(f"Model Intercept: {model.intercept_:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

    # Assertions for sanity check
    assert model.coef_[0] > 0, "Slope should be positive"
    assert 0 <= r2 <= 1, "R-squared should be between 0 and 1"
    assert mse >= 0, "MSE should be non-negative"

    # Test case 2: Using a small custom dataset
    small_data = pd.DataFrame({
        'size': [1000, 1500, 2000, 2500, 3000],
        'price': [150, 200, 250, 300, 350]  # Perfect linear relationship: price = 50 + 0.1*size? Actually: 1000->150, 1500->200 => slope=0.1, intercept=50
    })
    model2, mse2, r2_2, _, _, _ = linear_regression_exercise(small_data)
    print("\nSmall dataset results:")
    print(f"Slope: {model2.coef_[0]:.2f}, Intercept: {model2.intercept_:.2f}")
    print(f"MSE: {mse2:.2f}, R-squared: {r2_2:.2f}")
    # For perfect linear data, we expect high R-squared and low MSE
    assert r2_2 > 0.99, "R-squared should be very high for perfect linear data"
    assert mse2 < 1e-10, "MSE should be near zero for perfect linear data"

    print("\nAll tests passed!")