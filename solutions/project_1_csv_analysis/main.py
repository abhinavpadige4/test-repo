\"\"\"
Main script for CSV analysis project.

This script:
1. Loads a CSV file from the 'data' directory.
2. Performs basic data cleaning (handling missing values, converting data types).
3. Conducts exploratory data analysis (EDA) and generates summary statistics.
4. Creates visualizations (histograms, box plots, correlation heatmap) and saves them.
5. Saves the cleaned data to the 'outputs' directory.

Usage:
    python main.py
\"\"\"
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Setup directories
DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
PLOTS_DIR = OUTPUT_DIR / "plots"

# Create directories if they don't exist
OUTPUT_DIR.mkdir(exist_ok=True)
PLOTS_DIR.mkdir(exist_ok=True)

def load_data(file_name: str = "data.csv") -> pd.DataFrame:
    """
    Load CSV file from the data directory.

    Parameters:
    file_name (str): Name of the CSV file.

    Returns:
    pd.DataFrame: Loaded data.
    """
    file_path = DATA_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}. Please place your CSV file in the 'data' directory.")
    df = pd.read_csv(file_path)
    print(f"Loaded data from {file_path} with shape {df.shape}")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic data cleaning.

    Steps:
    - Convert column names to lowercase and replace spaces with underscores.
    - Identify and convert numeric columns (if they are stored as objects).
    - Fill missing numeric values with median.
    - Fill missing categorical values with mode.

    Parameters:
    df (pd.DataFrame): Input data.

    Returns:
    pd.DataFrame: Cleaned data.
    """
    df_clean = df.copy()
    
    # Clean column names
    df_clean.columns = [col.strip().lower().replace(' ', '_') for col in df_clean.columns]
    
    # Identify numeric and categorical columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
    
    # Convert columns that should be numeric but are stored as objects
    for col in df_clean.columns:
        if df_clean[col].dtype == 'object':
            # Try to convert to numeric
            converted = pd.to_numeric(df_clean[col], errors='coerce')
            # If at least 50% of the values are numeric, assume it's a numeric column
            if converted.notna().sum() / len(converted) > 0.5:
                df_clean[col] = converted
                # Update the lists
                if col in categorical_cols:
                    categorical_cols.remove(col)
                if col not in numeric_cols:
                    numeric_cols.append(col)
    
    # Re-identify numeric and categorical columns after conversion
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
    
    # Fill missing numeric values with median
    for col in numeric_cols:
        if df_clean[col].isna().any():
            median_val = df_clean[col].median()
            df_clean[col].fillna(median_val, inplace=True)
            print(f"Filled missing values in {col} with median: {median_val}")
    
    # Fill missing categorical values with mode
    for col in categorical_cols:
        if df_clean[col].isna().any():
            mode_val = df_clean[col].mode()[0] if not df_clean[col].mode().empty else "Unknown"
            df_clean[col].fillna(mode_val, inplace=True)
            print(f"Filled missing values in {col} with mode: {mode_val}")
    
    return df_clean

def exploratory_data_analysis(df: pd.DataFrame):
    """
    Perform exploratory data analysis and generate visualizations.

    Parameters:
    df (pd.DataFrame): Cleaned data.
    """
    # Summary statistics
    print("\n=== Summary Statistics ===")
    print(df.describe(include='all'))
    
    # Save summary statistics to a file
    summary_path = OUTPUT_DIR / "summary_statistics.csv"
    df.describe(include='all').to_csv(summary_path)
    print(f"Summary statistics saved to {summary_path}")
    
    # Visualizations
    # 1. Histograms for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        df[numeric_cols].hist(figsize=(12, 10), bins=20, edgecolor='black')
        plt.suptitle("Histograms of Numeric Columns")
        plt.tight_layout()
        hist_path = PLOTS_DIR / "histograms.png"
        plt.savefig(hist_path)
        plt.close()
        print(f"Histograms saved to {hist_path}")
    
    # 2. Box plots for numeric columns
    if len(numeric_cols) > 0:
        plt.figure(figsize=(12, 6))
        df[numeric_cols].boxplot(rot=45)
        plt.title("Box Plots of Numeric Columns")
        plt.tight_layout()
        box_path = PLOTS_DIR / "boxplots.png"
        plt.savefig(box_path)
        plt.close()
        print(f"Box plots saved to {box_path}")
    
    # 3. Correlation heatmap (if at least 2 numeric columns)
    if len(numeric_cols) >= 2:
        plt.figure(figsize=(10, 8))
        corr_matrix = df[numeric_cols].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        heatmap_path = PLOTS_DIR / "correlation_heatmap.png"
        plt.savefig(heatmap_path)
        plt.close()
        print(f"Correlation heatmap saved to {heatmap_path}")
    
    # 4. Value counts for categorical columns (top 5 categories)
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        df[col].value_counts().head(10).plot(kind='bar')
        plt.title(f"Top 10 Categories in {col}")
        plt.ylabel("Count")
        plt.tight_layout()
        cat_path = PLOTS_DIR / f"value_counts_{col}.png"
        plt.savefig(cat_path)
        plt.close()
        print(f"Value counts plot for {col} saved to {cat_path}")

def main():
    """
    Main function to run the CSV analysis.
    """
    try:
        # Step 1: Load data
        df_raw = load_data()
        
        # Step 2: Clean data
        df_clean = clean_data(df_raw)
        
        # Step 3: Save cleaned data
        cleaned_path = OUTPUT_DIR / "cleaned_data.csv"
        df_clean.to_csv(cleaned_path, index=False)
        print(f"Cleaned data saved to {cleaned_path}")
        
        # Step 4: Exploratory data analysis and visualizations
        exploratory_data_analysis(df_clean)
        
        print("\nAnalysis completed successfully!")
        print(f"Check the '{OUTPUT_DIR}' directory for outputs.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()