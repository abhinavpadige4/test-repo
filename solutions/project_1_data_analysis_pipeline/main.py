\"\"\"
Main script for the data analysis pipeline.
This script loads a CSV file, performs basic cleaning, exploratory analysis,
and generates visualizations.
\"\"\"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

def load_data(filepath):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        print(f"Loaded data with shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def clean_data(df):
    """Perform basic data cleaning steps."""
    # Make a copy to avoid warnings
    df_clean = df.copy()
    
    # 1. Remove duplicate rows
    initial_rows = df_clean.shape[0]
    df_clean.drop_duplicates(inplace=True)
    removed_duplicates = initial_rows - df_clean.shape[0]
    if removed_duplicates > 0:
        print(f"Removed {removed_duplicates} duplicate rows.")
    
    # 2. Handle missing values
    # For numeric columns, fill with median
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        missing_count = df_clean[col].isnull().sum()
        if missing_count > 0:
            median_val = df_clean[col].median()
            df_clean[col].fillna(median_val, inplace=True)
            print(f"Filled {missing_count} missing values in '{col}' with median: {median_val:.2f}")
    
    # For categorical columns, fill with mode
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        missing_count = df_clean[col].isnull().sum()
        if missing_count > 0:
            mode_val = df_clean[col].mode()[0] if not df_clean[col].mode().empty else 'Unknown'
            df_clean[col].fillna(mode_val, inplace=True)
            print(f"Filled {missing_count} missing values in '{col}' with mode: '{mode_val}'")
    
    return df_clean

def exploratory_analysis(df):
    """Perform exploratory data analysis and print summary."""
    print("\n" + "="*50)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe(include='all'))
    
    # Check for unique values in categorical columns (if any)
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        print("\nCategorical Columns Summary:")
        for col in categorical_cols:
            unique_count = df[col].nunique()
            top_value = df[col].mode()[0] if not df[col].mode().empty else None
            print(f"  {col}: {unique_count} unique values, top: '{top_value}'")

def create_visualizations(df, output_dir='outputs/plots'):
    """Create and save visualizations."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Set style
    sns.set_style("whitegrid")
    
    # 1. Histograms for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        n_cols = min(3, len(numeric_cols))  # max 3 per row
        n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
        plt.figure(figsize=(5*n_cols, 4*n_rows))
        for i, col in enumerate(numeric_cols, 1):
            plt.subplot(n_rows, n_cols, i)
            sns.histplot(df[col], kde=True)
            plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'numeric_distributions.png'), dpi=150)
        plt.close()
        print(f"Saved histogram plot to {output_dir}/numeric_distributions.png")
    
    # 2. Box plots for numeric columns (to spot outliers)
    if len(numeric_cols) > 0:
        plt.figure(figsize=(5*n_cols, 4*n_rows))
        for i, col in enumerate(numeric_cols, 1):
            plt.subplot(n_rows, n_cols, i)
            sns.boxplot(y=df[col])
            plt.title(f'Box Plot of {col}')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'numeric_boxplots.png'), dpi=150)
        plt.close()
        print(f"Saved box plot to {output_dir}/numeric_boxplots.png")
    
    # 3. Correlation heatmap (if at least 2 numeric columns)
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(8, 6))
        corr_matrix = df[numeric_cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), dpi=150)
        plt.close()
        print(f"Saved correlation heatmap to {output_dir}/correlation_heatmap.png")

def save_cleaned_data(df, output_dir='outputs/data'):
    """Save the cleaned DataFrame to CSV."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'cleaned_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

def main():
    """Main function to run the data analysis pipeline."""
    # Define paths
    data_dir = 'data'
    output_dir = 'outputs'
    
    # Create directories if they don't exist
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # Ask user for the CSV file name (or use a default)
    csv_file = input("Enter the CSV file name (located in the 'data' directory): ").strip()
    if not csv_file:
        csv_file = 'data.csv'  # default
    
    filepath = os.path.join(data_dir, csv_file)
    
    # Load data
    df = load_data(filepath)
    
    # Clean data
    df_clean = clean_data(df)
    
    # Exploratory analysis
    exploratory_analysis(df_clean)
    
    # Create visualizations
    create_visualizations(df_clean, os.path.join(output_dir, 'plots'))
    
    # Save cleaned data
    save_cleaned_data(df_clean, os.path.join(output_dir, 'data'))
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE!")
    print("="*50)
    print(f"Check the '{output_dir}' directory for results.")

if __name__ == "__main__":
    main()