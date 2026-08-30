\"\"\"
Exercise 3: Data Visualization with Matplotlib and Seaborn (Medium)
Problem Statement:
Given a dataset of iris flowers, create the following visualizations:
1. Pair plot showing relationships between all features
2. Box plot of petal length per species
3. Histogram of sepal width
4. Scatter plot of petal length vs petal width colored by species

Expected Output:
- Display or save the plots (we'll save to files for testing)
- Print summary statistics used in visualizations

Solution:
\"\"\"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_iris_data():
    """Load iris dataset from seaborn or create sample if not available."""
    try:
        df = sns.load_dataset('iris')
    except:
        # Create sample iris-like data
        np.random.seed(42)
        data = {
            'sepal_length': np.random.normal(5.8, 0.8, 150),
            'sepal_width': np.random.normal(3.1, 0.4, 150),
            'petal_length': np.random.normal(3.8, 1.7, 150),
            'petal_width': np.random.normal(1.2, 0.7, 150),
            'species': np.random.choice(['setosa', 'versicolor', 'virginica'], 150)
        }
        df = pd.DataFrame(data)
    return df

def create_visualizations(df, output_dir='plots'):
    """Create and save visualizations."""
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Set style
    sns.set_style("whitegrid")
    
    # 1. Pair plot
    plt.figure(figsize=(10, 8))
    pairplot = sns.pairplot(df, hue='species', diag_kind='kde')
    pairplot.fig.suptitle('Iris Dataset Pair Plot', y=1.02)
    pairplot.savefig(os.path.join(output_dir, 'pairplot.png'), bbox_inches='tight')
    plt.close()
    
    # 2. Box plot of petal length per species
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='species', y='petal_length', data=df)
    plt.title('Petal Length Distribution by Species')
    plt.savefig(os.path.join(output_dir, 'petal_length_boxplot.png'), bbox_inches='tight')
    plt.close()
    
    # 3. Histogram of sepal width
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal_width'], kde=True, bins=20)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.savefig(os.path.join(output_dir, 'sepal_width_histogram.png'), bbox_inches='tight')
    plt.close()
    
    # 4. Scatter plot of petal length vs petal width
    plt.figure(figsize=(8, 6))
    scatter = sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df, s=100)
    plt.title('Petal Length vs Petal Width')
    plt.savefig(os.path.join(output_dir, 'petal_scatter.png'), bbox_inches='tight')
    plt.close()
    
    # Return summary statistics
    summary = df.groupby('species').agg({
        'sepal_length': ['mean', 'std'],
        'sepal_width': ['mean', 'std'],
        'petal_length': ['mean', 'std'],
        'petal_width': ['mean', 'std']
    }).round(2)
    
    return summary

if __name__ == "__main__":
    # Load data
    df = load_iris_data()
    print("Iris Dataset Info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nSpecies distribution:")
    print(df['species'].value_counts())
    
    # Create visualizations
    summary = create_visualizations(df)
    print("\nSummary Statistics (by species):")
    print(summary)
    print("\nPlots saved to 'plots/' directory")
    
    # Simple test: check that plots directory exists and has files
    import os
    assert os.path.exists('plots'), "Plots directory was not created"
    plot_files = os.listdir('plots')
    assert len(plot_files) >= 4, f"Expected at least 4 plot files, got {len(plot_files)}"
    print(f"\nGenerated {len(plot_files)} plot files: {plot_files}")
    print("\nAll tests passed!")

\"\"\"
Time Complexity: O(n) for plotting operations where n is number of data points.
Space Complexity: O(n) for storing the DataFrame and plot objects.
\"\"\"