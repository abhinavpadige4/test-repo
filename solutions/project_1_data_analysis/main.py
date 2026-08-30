import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def load_data(filepath):
    """Load data from CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform basic data cleaning: fill numeric missing values with mean, drop rows with non-numeric missing if any."""
    # Make a copy to avoid SettingWithCopyWarning
    df_clean = df.copy()
    # Identify numeric columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    # Fill missing numeric values with column mean
    for col in numeric_cols:
        df_clean[col].fillna(df_clean[col].mean(), inplace=True)
    # For non-numeric columns, fill missing with mode (or drop if preferred)
    non_numeric_cols = df_clean.select_dtypes(exclude=[np.number]).columns
    for col in non_numeric_cols:
        df_clean[col].fillna(df_clean[col].mode()[0] if not df_clean[col].mode().empty else '', inplace=True)
    return df_clean

def compute_statistics(df):
    """Compute descriptive statistics for numeric columns."""
    numeric_df = df.select_dtypes(include=[np.number])
    stats = numeric_df.describe().transpose()
    stats['median'] = numeric_df.median()
    stats['mode'] = numeric_df.mode().iloc[0]  # first mode if multiple
    return stats

def plot_histogram(df, column, output_path='histogram.png'):
    """Plot histogram for a specified column and save."""
    plt.figure()
    df[column].hist(edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def main():
    input_file = 'sample_data.csv'
    output_file = 'cleaned_data.csv'
    stats_file = 'statistics.csv'
    histogram_file = 'histogram.png'
    
    # Check if sample data exists, if not create a simple dataset for demonstration
    if not os.path.exists(input_file):
        print(f"Sample data not found at {input_file}. Creating a sample dataset.")
        # Create a simple dataset
        data = {
            'age': [25, 30, 35, 40, np.nan, 50, 55, 60],
            'salary': [50000, 54000, 58000, 62000, 66000, np.nan, 74000, 78000],
            'department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT']
        }
        df = pd.DataFrame(data)
        df.to_csv(input_file, index=False)
        print(f"Sample data saved to {input_file}")
    
    # Load data
    df = load_data(input_file)
    print("Original data shape:", df.shape)
    print("Original data:\n", df.head())
    
    # Clean data
    df_clean = clean_data(df)
    print("\nCleaned data shape:", df_clean.shape)
    print("Cleaned data:\n", df_clean.head())
    
    # Save cleaned data
    df_clean.to_csv(output_file, index=False)
    print(f"\nCleaned data saved to {output_file}")
    
    # Compute statistics
    stats = compute_statistics(df_clean)
    print("\nDescriptive statistics:\n", stats)
    stats.to_csv(stats_file)
    print(f"Statistics saved to {stats_file}")
    
    # Plot histogram for first numeric column
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        plot_histogram(df_clean, numeric_cols[0], histogram_file)
        print(f"Histogram saved to {histogram_file}")
    else:
        print("No numeric columns for histogram.")
    
    print("\nProject completed successfully!")

if __name__ == "__main__":
    main()