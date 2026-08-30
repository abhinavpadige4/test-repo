\"\"\"
Exercise 7: Data Visualization - Matplotlib Basic Plots
Difficulty: Easy
Topic: Matplotlib

Problem Statement:
Write a Python script using Matplotlib to:
1. Create a simple line plot of y = x^2 for x from 0 to 10
2. Create a bar chart showing the number of students in different grades
3. Create a histogram of normally distributed random data
4. Create a scatter plot of two variables with a positive correlation

Expected Output:
Four plots will be displayed (or saved if running in a non-interactive environment).
Since we cannot display plots in this environment, we will save them to files and print confirmation.

Note: In a real environment, you would see the plots. For testing, we check that the files are created.
\"\"\"

import matplotlib.pyplot as plt
import numpy as np
import os

def matplotlib_basic_plots():
    """
    Create basic plots using Matplotlib and save them to files.
    Returns:
        list: List of filenames created
    """
    # Create a directory for plots if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    filenames = []
    
    # 1. Line plot: y = x^2
    x = np.linspace(0, 10, 100)
    y = x ** 2
    plt.figure()
    plt.plot(x, y)
    plt.title('Line Plot: y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    filename1 = 'plots/line_plot.png'
    plt.savefig(filename1)
    plt.close()
    filenames.append(filename1)
    
    # 2. Bar chart: number of students in different grades
    grades = ['A', 'B', 'C', 'D', 'F']
    student_counts = [23, 45, 56, 12, 8]
    plt.figure()
    plt.bar(grades, student_counts)
    plt.title('Bar Chart: Student Counts by Grade')
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    filename2 = 'plots/bar_chart.png'
    plt.savefig(filename2)
    plt.close()
    filenames.append(filename2)
    
    # 3. Histogram: normally distributed random data
    np.random.seed(42)  # for reproducibility
    data = np.random.normal(loc=0, scale=1, size=1000)
    plt.figure()
    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Histogram: Normally Distributed Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    filename3 = 'plots/histogram.png'
    plt.savefig(filename3)
    plt.close()
    filenames.append(filename3)
    
    # 4. Scatter plot: two variables with positive correlation
    x = np.random.rand(50) * 10
    y = x + np.random.randn(50) * 2  # adding some noise
    plt.figure()
    plt.scatter(x, y)
    plt.title('Scatter Plot: Positive Correlation')
    plt.xlabel('X Variable')
    plt.ylabel('Y Variable')
    filename4 = 'plots/scatter_plot.png'
    plt.savefig(filename4)
    plt.close()
    filenames.append(filename4)
    
    # Print confirmation
    for fname in filenames:
        print(f"Plot saved: {fname}")
    
    return filenames

# Test cases
if __name__ == "__main__":
    created_files = matplotlib_basic_plots()
    
    # Check that all four files were created
    assert len(created_files) == 4, f"Expected 4 files, got {len(created_files)}"
    for fname in created_files:
        assert os.path.exists(fname), f"File not found: {fname}"
    
    print("\nAll tests passed!")