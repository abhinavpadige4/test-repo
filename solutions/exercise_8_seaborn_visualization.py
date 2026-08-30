\"\"\"
Exercise 8: Data Visualization - Seaborn
Difficulty: Medium
Topic: Seaborn

Problem Statement:
Write a Python script using Seaborn to:
1. Load the built-in 'iris' dataset
2. Create a pairplot to show relationships between all variables
3. Create a boxplot to show the distribution of sepal length per species
4. Create a violin plot to show the distribution of petal width per species
5. Create a heatmap of the correlation matrix

Expected Output:
Plots will be saved to the 'plots' directory.
Since we cannot display plots in this environment, we will save them to files and print confirmation.

Note: In a real environment, you would see the plots. For testing, we check that the files are created.
\"\"\"

import seaborn as sns
import matplotlib.pyplot as plt
import os

def seaborn_visualization():
    """
    Create visualizations using Seaborn and save them to files.
    Returns:
        list: List of filenames created
    """
    # Create a directory for plots if it doesn't exist
    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    filenames = []
    
    # Load the iris dataset
    iris = sns.load_dataset('iris')
    
    # 1. Pairplot
    plt.figure()
    sns.pairplot(iris, hue='species')
    plt.suptitle('Pairplot of Iris Dataset', y=1.02)
    filename1 = 'plots/iris_pairplot.png'
    plt.savefig(filename1, bbox_inches='tight')
    plt.close()
    filenames.append(filename1)
    
    # 2. Boxplot: sepal length per species
    plt.figure()
    sns.boxplot(x='species', y='sepal_length', data=iris)
    plt.title('Boxplot of Sepal Length by Species')
    filename2 = 'plots/iris_boxplot.png'
    plt.savefig(filename2, bbox_inches='tight')
    plt.close()
    filenames.append(filename2)
    
    # 3. Violin plot: petal width per species
    plt.figure()
    sns.violinplot(x='species', y='petal_width', data=iris)
    plt.title('Violin Plot of Petal Width by Species')
    filename3 = 'plots/iris_violinplot.png'
    plt.savefig(filename3, bbox_inches='tight')
    plt.close()
    filenames.append(filename3)
    
    # 4. Heatmap of the correlation matrix
    plt.figure()
    corr = iris.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Heatmap of Iris Correlation Matrix')
    filename4 = 'plots/iris_heatmap.png'
    plt.savefig(filename4, bbox_inches='tight')
    plt.close()
    filenames.append(filename4)
    
    # Print confirmation
    for fname in filenames:
        print(f"Plot saved: {fname}")
    
    return filenames

# Test cases
if __name__ == "__main__":
    created_files = seaborn_visualization()
    
    # Check that all four files were created
    assert len(created_files) == 4, f"Expected 4 files, got {len(created_files)}"
    for fname in created_files:
        assert os.path.exists(fname), f"File not found: {fname}"
    
    print("\nAll tests passed!")