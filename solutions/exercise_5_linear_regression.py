\"\"\"
Exercise 5: Simple Linear Regression from Scratch (Hard)
Problem Statement:
Implement a simple linear regression model using only NumPy.
Steps:
1. Generate synthetic data for house prices based on size.
2. Implement the model: y = mx + b.
3. Define loss function (Mean Squared Error).
4. Implement gradient descent to learn m and b.
5. Train the model and plot the results.
6. Make predictions and evaluate.

Expected Output:
- Print learned parameters (m, b).
- Print final loss.
- Show a plot of data and regression line (saved to file).
- Test that the learned parameters are close to the true values.

Solution:
\"\"\"
import numpy as np
import matplotlib.pyplot as plt
import os

def generate_data(n_samples=100, true_m=2.5, true_b=10, noise=5.0):
    """Generate synthetic linear data."""
    np.random.seed(42)
    X = np.random.rand(n_samples) * 10  # house size from 0 to 10
    y = true_m * X + true_b + np.random.randn(n_samples) * noise
    return X, y

def predict(X, m, b):
    """Make predictions."""
    return m * X + b

def compute_loss(y_true, y_pred):
    """Mean Squared Error."""
    return np.mean((y_true - y_pred) ** 2)

def gradient_descent(X, y, m_init=0, b_init=0, learning_rate=0.01, n_iterations=1000):
    """Perform gradient descent."""
    m = m_init
    b = b_init
    n = len(X)
    loss_history = []
    
    for i in range(n_iterations):
        y_pred = predict(X, m, b)
        loss = compute_loss(y, y_pred)
        loss_history.append(loss)
        
        # Gradients
        dm = -(2/n) * np.sum(X * (y - y_pred))
        db = -(2/n) * np.sum(y - y_pred)
        
        # Update
        m = m - learning_rate * dm
        b = b - learning_rate * db
        
        # Optional: print progress
        if i % 100 == 0:
            print(f"Iteration {i}: Loss = {loss:.4f}, m = {m:.4f}, b = {b:.4f}")
    
    return m, b, loss_history

def plot_results(X, y, m, b, save_path='plots/regression_plot.png'):
    """Plot data and regression line."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.scatter(X, y, alpha=0.7, label='Data')
    x_line = np.linspace(X.min(), X.max(), 100)
    y_line = predict(x_line, m, b)
    plt.plot(x_line, y_line, 'r-', linewidth=2, label=f'Regression Line (y={m:.2f}x+{b:.2f})')
    plt.xlabel('House Size')
    plt.ylabel('Price')
    plt.title('Linear Regression: House Price vs Size')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Plot saved to {save_path}")

if __name__ == "__main__":
    # 1. Generate data
    X, y = generate_data()
    print(f"Generated {len(X)} samples")
    print(f"First 5 X: {X[:5]}")
    print(f"First 5 y: {y[:5]}")
    
    # 2. Train model
    print("\nTraining model with gradient descent...")
    m_learned, b_learned, loss_history = gradient_descent(X, y, learning_rate=0.01, n_iterations=500)
    
    # 3. Evaluate
    y_pred = predict(X, m_learned, b_learned)
    final_loss = compute_loss(y, y_pred)
    print(f"\nFinal Loss (MSE): {final_loss:.4f}")
    print(f"Learned parameters: m = {m_learned:.4f}, b = {b_learned:.4f}")
    print(f"True parameters: m = 2.5, b = 10.0")
    
    # 4. Plot
    plot_results(X, y, m_learned, b_learned)
    
    # 5. Test: parameters should be close to true values (within tolerance)
    assert abs(m_learned - 2.5) < 0.5, f"Slope m is not close enough: {m_learned}"
    assert abs(b_learned - 10.0) < 2.0, f"Intercept b is not close enough: {b_learned}"
    assert final_loss < 30.0, f"Loss is too high: {final_loss}"
    print("\nAll tests passed!")

\"\"\"
Time Complexity: O(n * iterations) for gradient descent where n is number of samples.
Space Complexity: O(n) for storing data and predictions.
\"\"\"