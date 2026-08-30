\"\"\"
Exercise 4: Data Visualization with Matplotlib (Medium)
Problem Statement:
Write a function `plot_histogram(data, bins=10, title='Histogram', xlabel='Value', ylabel='Frequency', save_path=None)` that:
- Takes a list of numerical data.
- Plots a histogram using matplotlib.
- Optionally saves the figure to save_path if provided.
- Returns the matplotlib Figure object (for testing).

Use the 'Agg' backend to avoid GUI issues.

Test Cases:
1. plot_histogram([1,2,2,3,3,3,4,4,5], bins=5) -> returns a Figure object.
2. plot_histogram([], bins=10) -> handles empty data gracefully.
3. plot_histogram([1,1,1,1], bins=1, save_path='test_hist.png') -> saves file and returns Figure.
\"\"\"
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import os

def plot_histogram(data, bins=10, title='Histogram', xlabel='Value', ylabel='Frequency', save_path=None):
    """
    Create and optionally save a histogram.
    
    Args:
        data (list): List of numerical values.
        bins (int): Number of bins.
        title (str): Plot title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        save_path (str): If provided, save figure to this path.
    
    Returns:
        matplotlib.figure.Figure: The figure object.
    """
    fig, ax = plt.subplots()
    if len(data) > 0:
        ax.hist(data, bins=bins, edgecolor='black')
    else:
        # For empty data, just show empty histogram
        ax.hist([], bins=bins, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if save_path:
        fig.savefig(save_path, bbox_inches='tight')
        # Optionally verify file exists
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Failed to save figure to {save_path}")
    return fig

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    # Test 1
    fig1 = plot_histogram([1,2,2,3,3,3,4,4,5], bins=5, title='Test 1')
    assert fig1 is not None, "Test 1 failed: Figure not created"
    print("Test 1 passed: Histogram created with data")
    
    # Test 2
    fig2 = plot_histogram([], bins=10, title='Empty Data')
    assert fig2 is not None, "Test 2 failed: Figure not created for empty data"
    print("Test 2 passed: Empty data handled")
    
    # Test 3
    test_path = 'test_hist.png'
    fig3 = plot_histogram([1,1,1,1], bins=1, title='Test 3', save_path=test_path)
    assert os.path.exists(test_path), f"Test 3 failed: File {test_path} not saved"
    print(f"Test 3 passed: Histogram saved to {test_path}")
    # Clean up
    if os.path.exists(test_path):
        os.remove(test_path)
    
    print("All visualization tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n) where n is length of data (for computing histogram).
    # Space Complexity: O(1) additional space (not counting the figure).
\"\"\"