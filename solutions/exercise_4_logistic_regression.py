\"\"\"
Exercise 4: Logistic Regression (Medium-Hard)
Problem Statement:
Given a dataset of customer churn with features: monthly_charges, total_charges, tenure,
and contract_type (encoded as 0 for month-to-month, 1 for one_year, 2 for two_year),
implement a logistic regression model to predict whether a customer will churn (1) or not (0).

Steps:
1. Load the dataset (provided as CSV string for self-containment).
2. Preprocess: encode contract_type as numeric (already done in sample).
3. Split into train and test sets (80-20).
4. Train a logistic regression model.
5. Evaluate using accuracy, precision, recall, and F1-score.
6. Print the model coefficients and evaluation metrics.

Assume the CSV has columns: monthly_charges, total_charges, tenure, contract_type, churn.
\"\"\"
import pandas as pd
import numpy as np
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_and_prepare_data(csv_data: str):
    """
    Load CSV data and prepare features and target.
    
    Args:
        csv_data: CSV content as string.
    
    Returns:
        X: feature array
        y: target array (churn)
    """
    df = pd.read_csv(io.StringIO(csv_data))
    # Features: monthly_charges, total_charges, tenure, contract_type
    X = df[['monthly_charges', 'total_charges', 'tenure', 'contract_type']].values
    y = df['churn'].values
    return X, y

def train_logistic_regression(X, y, test_size=0.2, random_state=42):
    """
    Train logistic regression model and evaluate.
    
    Args:
        X: feature array
        y: target array
        test_size: proportion for test set
        random_state: seed for reproducibility
    
    Returns:
        model: trained LogisticRegression object
        X_train, X_test, y_train, y_test: split data
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    model = LogisticRegression(random_state=random_state)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Metrics
    train_acc = accuracy_score(y_train, y_pred_train)
    test_acc = accuracy_score(y_test, y_pred_test)
    train_prec = precision_score(y_train, y_pred_train)
    test_prec = precision_score(y_test, y_pred_test)
    train_rec = recall_score(y_train, y_pred_train)
    test_rec = recall_score(y_test, y_pred_test)
    train_f1 = f1_score(y_train, y_pred_train)
    test_f1 = f1_score(y_test, y_pred_test)
    
    print(f"Model Coefficients: {model.coef_}")
    print(f"Model Intercept: {model.intercept_}")
    print(f"Training Accuracy: {train_acc:.4f}, Precision: {train_prec:.4f}, Recall: {train_rec:.4f}, F1: {train_f1:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}, Precision: {test_prec:.4f}, Recall: {test_rec:.4f}, F1: {test_f1:.4f}")
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred_test)
    print(f"Confusion Matrix:\\n{cm}")
    
    return model, X_train, X_test, y_train, y_test

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Sample customer churn data
    sample_csv = """monthly_charges,total_charges,tenure,contract_type,churn
29.85,29.85,1,0,1
56.95,188.95,34,0,0
53.85,108.15,2,0,1
42.30,1840.75,72,2,0
70.70,151.65,9,0,1
99.65,820.5,15,1,0
89.10,1349.4,23,1,0
29.75,59.5,2,0,1
49.15,195.6,4,0,0
59.50,292.5,5,0,0
"""
    
    X, y = load_and_prepare_data(sample_csv)
    print(f"Data shape: X={X.shape}, y={y.shape}")
    print(f"Churn rate: {y.mean():.2%}")
    
    model, X_train, X_test, y_train, y_test = train_logistic_regression(X, y)
    
    # Additional test: predict for a new customer
    new_customer = np.array([[65.0, 300.0, 12, 1]])  # monthly_charges, total_charges, tenure, contract_type
    predicted_prob = model.predict_proba(new_customer)[0][1]
    predicted_class = model.predict(new_customer)[0]
    print(f"\nNew customer: monthly_charges=65, total_charges=300, tenure=12, contract_type=1")
    print(f"Predicted probability of churn: {predicted_prob:.4f}")
    print(f"Predicted class: {predicted_class} (1=churn, 0=no churn)")
    
    # Verify model is trained
    assert model.coef_.shape == (1, 4), "Expected 4 features"
    print("\nAll tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(n * iterations) for training (n samples, iterations until convergence)
    # Space Complexity: O(features) for model coefficients plus O(n) for data storage