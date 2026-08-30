"""
Main script for house price prediction pipeline.

This script demonstrates a complete data science workflow:
1. Data loading and exploration
2. Data preprocessing
3. Model training and evaluation
4. Model persistence
5. Prediction example
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Configuration
DATA_PATH = 'data/house_prices.csv'
MODEL_PATH = 'models/best_model.joblib'
RANDOM_STATE = 42

def load_data():
    """
    Load house price dataset. If file doesn't exist, generate sample data.
    """
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        print(f"Loaded data from {DATA_PATH}")
    else:
        # Generate sample data for demonstration
        print("Data file not found. Generating sample data...")
        np.random.seed(RANDOM_STATE)
        n_samples = 500
        
        # Generate features
        size = np.random.normal(2000, 500, n_samples).clip(500, 5000)
        bedrooms = np.random.randint(1, 6, n_samples)
        age = np.random.randint(0, 50, n_samples)
        # Create price with some relationship to features plus noise
        price = (size * 100 + bedrooms * 10000 - age * 500 + 
                 np.random.normal(0, 50000, n_samples)).clip(50000, 1000000)
        
        # Add some categorical features
        neighborhood = np.choice(['A', 'B', 'C', 'D'], n_samples, p=[0.4, 0.3, 0.2, 0.1])
        school_rating = np.random.randint(1, 11, n_samples)
        
        df = pd.DataFrame({
            'size': size,
            'bedrooms': bedrooms,
            'age': age,
            'neighborhood': neighborhood,
            'school_rating': school_rating,
            'price': price
        })
        
        # Create data directory and save sample data
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
        print(f"Generated sample data and saved to {DATA_PATH}")
    
    return df

def explore_data(df):
    """
    Perform basic exploratory data analysis.
    """
    print("\n=== Data Exploration ===")
    print(f"Dataset shape: {df.shape}")
    print("\nColumn types:")
    print(df.dtypes)
    print("\nSummary statistics:")
    print(df.describe())
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Visualizations
    os.makedirs('outputs', exist_ok=True)
    
    # Distribution of target variable
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], kde=True)
    plt.title('Distribution of House Prices')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    plt.savefig('outputs/price_distribution.png')
    plt.close()
    
    # Correlation matrix (numeric columns only)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.savefig('outputs/correlation_matrix.png')
    plt.close()
    
    print("Exploratory visualizations saved to outputs/")

def preprocess_data(df):
    """
    Preprocess data: separate features and target, identify column types.
    """
    # Separate features and target
    X = df.drop('price', axis=1)
    y = df['price']
    
    # Identify numeric and categorical columns
    numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X.select_dtypes(include=['object']).columns.tolist()
    
    print(f"\nNumeric features: {numeric_features}")
    print(f"Categorical features: {categorical_features}")
    
    # Create preprocessing pipelines
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    return X, y, preprocessor, numeric_features, categorical_features

def train_and_evaluate_models(X, y, preprocessor):
    """
    Train multiple regression models and evaluate them.
    """
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )
    
    # Define models
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=RANDOM_STATE),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=RANDOM_STATE)
    }
    
    results = {}
    best_model_name = None
    best_score = -np.inf  # We'll use R-squared for selection
    
    for name, model in models.items():
        # Create pipeline
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', model)
        ])
        
        # Train
        pipeline.fit(X_train, y_train)
        
        # Predict
        y_pred_train = pipeline.predict(X_train)
        y_pred_test = pipeline.predict(X_test)
        
        # Evaluate
        train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
        test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
        train_r2 = r2_score(y_train, y_pred_train)
        test_r2 = r2_score(y_test, y_pred_test)
        
        results[name] = {
            'pipeline': pipeline,
            'train_rmse': train_rmse,
            'test_rmse': test_rmse,
            'train_r2': train_r2,
            'test_r2': test_r2
        }
        
        print(f"\n{name}:")
        print(f"  Train RMSE: {train_rmse:.2f}, R-squared: {train_r2:.4f}")
        print(f"  Test RMSE:  {test_rmse:.2f}, R-squared: {test_r2:.4f}")
        
        # Update best model
        if test_r2 > best_score:
            best_score = test_r2
            best_model_name = name
    
    print(f"\nBest model: {best_model_name} (Test R-squared: {best_score:.4f})")
    
    # Save the best model
    best_pipeline = results[best_model_name]['pipeline']
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(best_pipeline, MODEL_PATH)
    print(f"Best model saved to {MODEL_PATH}")
    
    return results, best_model_name

def make_prediction_example(best_model_name):
    """
    Example of making a prediction with the saved model.
    """
    # Load the saved model
    pipeline = joblib.load(MODEL_PATH)
    
    # Create example data (matching the features used in training)
    # We'll use the same structure as the sample data generated
    example_data = pd.DataFrame({
        'size': [2500],
        'bedrooms': [4],
        'age': [10],
        'neighborhood': ['B'],
        'school_rating': [8]
    })
    
    # Make prediction
    predicted_price = pipeline.predict(example_data)[0]
    
    print(f"\n=== Prediction Example ===")
    print(f"Input features:")
    for col in example_data.columns:
        print(f"  {col}: {example_data[col].iloc[0]}")
    print(f"Predicted house price: ${predicted_price:,.2f}")

def main():
    """
    Main function to run the entire pipeline.
    """
    print("=== House Price Prediction Pipeline ===")
    
    # Step 1: Load data
    df = load_data()
    
    # Step 2: Explore data
    explore_data(df)
    
    # Step 3: Preprocess data
    X, y, preprocessor, numeric_features, categorical_features = preprocess_data(df)
    
    # Step 4: Train and evaluate models
    results, best_model_name = train_and_evaluate_models(X, y, preprocessor)
    
    # Step 5: Make a prediction example
    make_prediction_example(best_model_name)
    
    print("\n=== Pipeline completed successfully! ===")

if __name__ == "__main__":
    main()