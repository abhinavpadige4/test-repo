\"\"\"
Exercise 3: Linear Regression (Medium)
Problem Statement:
Given a dataset of house prices with features: size (sqft), bedrooms, age (years),
and price ($), implement a simple linear regression model to predict house price
using size as the only feature.

Steps:
1. Load the dataset (provided as CSV string for self-containment).
2. Extract 'size' as X and 'price' as y.
3. Split into train and test sets (80-20).
4. Train a linear regression model.
5. Evaluate using RMSE and R-squared.
6. Print the model coefficients and evaluation metrics.

Assume the CSV has columns: size, bedrooms, age, price.
\"\"\"
import pandas as pd
import numpy as np
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_and_prepare_data(csv_data: str):
    """
    Load CSV data and prepare features and target.
    
    Args:
        csv_data: CSV content as string.
    
    Returns:
        X: feature array (size)
        y: target array (price)
    """
    df = pd.read_csv(io.StringIO(csv_data))
    X = df[['size']].values  # Using only size as feature
    y = df['price'].values
    return X, y

def train_linear_regression(X, y, test_size=0.2, random_state=42):
    """
    Train linear regression model and evaluate.
    
    Args:
        X: feature array
        y: target array
        test_size: proportion for test set
        random_state: seed for reproducibility
    
    Returns:
        model: trained LinearRegression object
        X_train, X_test, y_train, y_test: split data
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Metrics
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    print(f"Model Coefficients: slope = {model.coef_[0]:.2f}, intercept = {model.intercept_:.2f}")
    print(f"Training RMSE: {train_rmse:.2f}, R-squared: {train_r2:.4f}")
    print(f"Test RMSE: {test_rmse:.2f}, R-squared: {test_r2:.4f}")
    
    return model, X_train, X_test, y_train, y_test

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Sample house price data
    sample_csv = """size,bedrooms,age,price
1500,3,10,300000
1800,4,5,350000
1200,2,18,200000
2000,4,8,400000
1600,3,12,320000
1900,4,3,380000
1300,2,20,210000
2100,5,2,420000
1400,3,15,250000
1700,3,7,330000
"""
    
    X, y = load_and_prepare_data(sample_csv)
    print(f"Data shape: X={X.shape}, y={y.shape}")
    
    model, X_train, X_test, y_train, y_test = train_linear_regression(X, y)
    
    # Additional test: predict for a new size
    new_size = np.array([[1750]])
    predicted_price = model.predict(new_size)[0]
    print(f"\nPredicted price for 1750 sqft house: ${predicted_price:,.2f}")
    
    # Verify model is trained (coefficients should be reasonable)
    assert model.coef_[0] > 0, "Price should increase with size"
    assert model.intercept_ >= 0, "Intercept should be non-negative"
    print("\nAll tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n) for training (n samples) - linear regression via normal equation is O(n) for univariate
    # Space Complexity: O(1) for model parameters (slope and intercept) plus O(n) for data storage