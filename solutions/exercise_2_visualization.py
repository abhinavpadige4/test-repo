\"\"\"
Exercise 2: Data Visualization with Matplotlib and Seaborn
Topic: Data Visualization
Difficulty: Easy

Problem Statement:
Write a Python script that:
1. Loads the iris dataset (from sklearn.datasets or via seaborn).
2. Creates a pair plot showing relationships between all features, colored by species.
3. Creates a box plot for each feature grouped by species.
4. Creates a histogram for sepal length with a KDE overlay.
5. Saves each plot to a PNG file.

Provide test cases to verify the plots are created.

\"\"\"
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from sklearn.datasets import load_iris

def create_visualizations(save_dir='plots'):
    """
    Load iris dataset and create various visualizations.
    
    Parameters:
    save_dir (str): Directory to save plots.
    """
    # Create save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Load iris dataset
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # 1. Pair plot
    plt.figure(figsize=(10, 8))
    pair_plot = sns.pairplot(df, hue='species')
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', y=1.02)
    pair_plot.savefig(os.path.join(save_dir, 'iris_pairplot.png'))
    plt.close()
    
    # 2. Box plot for each feature
    plt.figure(figsize=(12, 8))
    df_melted = pd.melt(df, id_vars='species', value_vars=iris.feature_names)
    sns.boxplot(x='variable', y='value', hue='species', data=df_melted)
    plt.title('Feature Distribution by Species')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, 'iris_boxplot.png'))
    plt.close()
    
    # 3. Histogram with KDE for sepal length
    plt.figure(figsize=(8, 6))
    sns.histplot(df['sepal length (cm)'], kde=True, hue='species', multiple='stack')
    plt.title('Sepal Length Distribution with KDE')
    plt.xlabel('Sepal Length (cm)')
    plt.savefig(os.path.join(save_dir, 'iris_sepal_length_hist.png'))
    plt.close()
    
    print(f"All plots saved to {save_dir}/")
    
    # Verify files exist
    expected_files = [
        'iris_pairplot.png',
        'iris_boxplot.png',
        'iris_sepal_length_hist.png'
    ]
    for f in expected_files:
        path = os.path.join(save_dir, f)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Plot not saved: {path}")
    
    return True

# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    print("=== Running Exercise 2 Tests ===")
    try:
        create_visualizations('test_plots')
        print("All visualization tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")
        raise
    
    # Cleanup
    import shutil
    if os.path.exists('test_plots'):
        shutil.rmtree('test_plots')