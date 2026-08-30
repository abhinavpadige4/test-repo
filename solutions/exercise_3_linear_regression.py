\"\"\"
Exercise 3: Simple Linear Regression with Scikit-learn
Topic: Machine Learning Basics
Difficulty: Easy

Problem Statement:
Write a Python script that:
1. Generates a synthetic dataset for linear regression (with some noise).
2. Splits the data into training and testing sets.
3. Trains a linear regression model.
4. Makes predictions on the test set.
5. Evaluates the model using R-squared and Mean Squared Error.
6. Plots the regression line and the data points.

Provide test cases to verify the model is trained and evaluated.

\"\"\"
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

def linear_regression_exercise(n_samples=100, noise=10, test_size=0.2, random_state=42):
    """
    Generate synthetic data, train linear regression model, evaluate, and plot.
    
    Parameters:
    n_samples (int): Number of samples to generate.
    noise (float): Standard deviation of Gaussian noise added to target.
    test_size (float): Proportion of dataset to include in test split.
    random_state (int): Random seed for reproducibility.
    
    Returns:
    dict: Contains model, metrics, and data splits.
    """
    # 1. Generate synthetic data
    np.random.seed(random_state)
    X = np.random.rand(n_samples, 1) * 10  # Features between 0 and 10
    y = 2.5 * X.ravel() + np.random.normal(0, noise, n_samples)  # y = 2.5*x + noise
    
    # 2. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    # 3. Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 4. Predict
    y_pred = model.predict(X_test)
    
    # 5. Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # 6. Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(X_train, y_train, color='blue', label='Training data', alpha=0.7)
    plt.scatter(X_test, y_test, color='green', label='Test data', alpha=0.7)
    # Plot regression line
    X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = model.predict(X_line)
    plt.plot(X_line, y_line, color='red', linewidth=2, label='Regression line')
    plt.xlabel('Feature X')
    plt.ylabel('Target y')
    plt.title('Linear Regression: Training vs Test Data')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot
    plot_path = 'linear_regression_plot.png'
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")
    
    # Return results
    results = {
        'model': model,
        'X_train': X_train, 'y_train': y_train,
        'X_test': X_test, 'y_test': y_test,
        'y_pred': y_pred,
        'mse': mse,
        'r2': r2,
        'plot_path': plot_path
    }
    
    return results

# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    print("=== Running Exercise 3 Tests ===")
    results = linear_regression_exercise()
    
    # Check that model is trained
    assert hasattr(results['model'], 'coef_'), "Model not trained!"
    assert len(results['model'].coef_) == 1, "Expected single feature model!"
    
    # Check that metrics are computed
    assert results['mse'] >= 0, "MSE should be non-negative!"
    assert 0 <= results['r2'] <= 1, "R-squared should be between 0 and 1!"
    
    # Check that plot file exists
    assert os.path.exists(results['plot_path']), "Plot file not created!"
    
    # Check data splits
    assert len(results['X_train']) + len(results['X_test']) == 100, "Total samples mismatch!"
    
    print(f"Model coefficient: {results['model'].coef_[0]:.2f} (expected ~2.5)")
    print(f"Mean Squared Error: {results['mse']:.2f}")
    print(f"R-squared: {results['r2']:.2f}")
    print("\nAll tests passed!")
    
    # Cleanup plot file
    os.remove(results['plot_path'])