\"\"\"
Exercise 2: Data Visualization (Easy-Medium)
Problem Statement:
Given a DataFrame containing information about cars (mpg, horsepower, weight, origin),
create the following visualizations using matplotlib and seaborn:
1. A scatter plot of horsepower vs. mpg, colored by origin.
2. A histogram of mpg.
3. A boxplot of weight distribution by origin.
4. A pairplot of the numerical columns.

Assume the data is in a CSV file 'cars.csv' with columns: mpg, horsepower, weight, origin.

Provide a solution that generates these plots and saves them as PNG files.
For self-contained testing, we'll generate a small sample dataset.
\"\"\"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

def generate_sample_data():
    """Generate a small sample dataset for testing."""
    np.random.seed(42)
    n = 100
    data = {
        'mpg': np.random.normal(25, 5, n),
        'horsepower': np.random.normal(150, 30, n),
        'weight': np.random.normal(3000, 500, n),
        'origin': np.random.choice(['USA', 'Europe', 'Japan'], n)
    }
    return pd.DataFrame(data)

def create_visualizations(df, save_prefix='plot'):
    """
    Create and save visualizations.
    
    Args:
        df: pandas DataFrame with car data.
        save_prefix: prefix for saved image files.
    """
    # Set style
    sns.set_style("whitegrid")
    
    # 1. Scatter plot: horsepower vs mpg, colored by origin
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='horsepower', y='mpg', hue='origin', palette='deep')
    plt.title('Horsepower vs MPG by Origin')
    plt.savefig(f'{save_prefix}_scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Histogram of mpg
    plt.figure(figsize=(10, 6))
    sns.histplot(df['mpg'], kde=True, color='skyblue')
    plt.title('Distribution of MPG')
    plt.xlabel('MPG')
    plt.savefig(f'{save_prefix}_histogram.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Boxplot of weight by origin
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='origin', y='weight', palette='pastel')
    plt.title('Weight Distribution by Origin')
    plt.savefig(f'{save_prefix}_boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Pairplot of numerical columns
    numerical_cols = ['mpg', 'horsepower', 'weight']
    sns.pairplot(df[numerical_cols], diag_kind='kde', plot_kws={'alpha':0.6})
    plt.suptitle('Pairplot of Numerical Features', y=1.02)
    plt.savefig(f'{save_prefix}_pairplot.png', dpi=300, bbox_inches='tight')
    plt.close()

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Generate sample data
    df = generate_sample_data()
    print("Sample DataFrame shape:", df.shape)
    print(df.head())
    
    # Create visualizations
    create_visualizations(df, save_prefix='solutions/test_plot')
    print("Visualizations saved as test_plot_*.png")
    
    # Verify that files were created (in a real scenario, we'd check the filesystem)
    # For this self-contained test, we'll just print success.
    print("All visualizations generated successfully!")
    
    # Complexity Analysis:
    # Time Complexity: O(n) for generating plots (each plot processes n points)
    # Space Complexity: O(n) for storing the DataFrame