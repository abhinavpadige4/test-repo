\"\"\"
Exercise 3: Matplotlib Plots Basics
Problem Statement:
Write a function `create_plot` that takes in two lists (x and y) and generates a line plot.
The function should:
- Create a line plot of y vs x.
- Label the x-axis as 'X-axis' and y-axis as 'Y-axis'.
- Set the title to 'Line Plot'.
- Return the matplotlib figure object.

Requirements:
- Import matplotlib.pyplot as plt.
- Handle empty lists by creating an empty plot with title 'Empty Data'.
- Do not display the plot (we'll manage it in tests).

Test Cases:
1. Input: x = [1, 2, 3, 4], y = [1, 4, 9, 16]
   Expected Output: A figure containing a line that passes through (1,1), (2,4), (3,9), (4,16).
2. Input: x = [0, 1, 2, 3], y = [0, 1, 0, 1]
   Expected Output: A figure containing a line that oscillates.
3. Input: x = [], y = []
   Expected Output: An empty figure with title 'Empty Data'.

Complexity Analysis:
Time Complexity: O(n) where n is the length of the input lists (due to plotting n points).
Space Complexity: O(n) for storing the plot data in the figure.
\"\"\"

import matplotlib.pyplot as plt

def create_plot(x, y):
    \"\"\"Create a line plot from x and y data.
    
    Args:
        x (list): X-axis data.
        y (list): Y-axis data.
        
    Returns:
        matplotlib.figure.Figure: The generated figure.
    \"\"\"
    fig, ax = plt.subplots()
    
    if not x or not y:
        ax.set_title('Empty Data')
    else:
        ax.plot(x, y)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Line Plot')
    
    return fig


# Test cases
if __name__ == \"__main__\":
    # Test 1: Quadratic data
    fig1 = create_plot([1, 2, 3, 4], [1, 4, 9, 16])
    ax1 = fig1.axes[0]
    line1 = ax1.lines[0]
    x_data1, y_data1 = line1.get_xdata(), line1.get_ydata()
    print(\"Test 1 - Quadratic:\")
    print(f\"  X data: {list(x_data1)}\")
    print(f\"  Y data: {list(y_data1)}\")
    assert list(x_data1) == [1, 2, 3, 4]
    assert list(y_data1) == [1, 4, 9, 16]
    plt.close(fig1)
    print(\"  PASSED\\n\")
    
    # Test 2: Oscillating data
    fig2 = create_plot([0, 1, 2, 3], [0, 1, 0, 1])
    ax2 = fig2.axes[0]
    line2 = ax2.lines[0]
    x_data2, y_data2 = line2.get_xdata(), line2.get_ydata()
    print(\"Test 2 - Oscillating:\")
    print(f\"  X data: {list(x_data2)}\")
    print(f\"  Y data: {list(y_data2)}\")
    assert list(x_data2) == [0, 1, 2, 3]
    assert list(y_data2) == [0, 1, 0, 1]
    plt.close(fig2)
    print(\"  PASSED\\n\")
    
    # Test 3: Empty data
    fig3 = create_plot([], [])
    ax3 = fig3.axes[0]
    print(\"Test 3 - Empty data:\")
    print(f\"  Title: {ax3.get_title()}\")
    assert ax3.get_title() == 'Empty Data'
    assert len(ax3.lines) == 0  # No lines plotted
    plt.close(fig3)
    print(\"  PASSED\\n\")
    
    print(\"All tests passed!\")