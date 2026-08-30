\"\"\"
Exercise 5: Titanic Survival Prediction with Feature Engineering (Hard)
Problem Statement:
Using the Titanic dataset, build a machine learning pipeline to predict passenger survival.
Steps:
1. Load the Titanic dataset from a CSV file (we'll use a small sample for speed).
2. Perform data cleaning:
   - Handle missing values in Age (median per Pclass), Embarked (mode), Fare (median).
   - Extract titles from Name (Mr, Mrs, Miss, etc.) and map to categories.
   - Convert Sex to numeric (0/1).
   - Create family size feature (SibSp + Parch + 1).
   - Create is_alone feature.
   - Bin Age into categories.
   - Bin Fare into categories.
3. Encode categorical variables (Embarked, Title, Age_bin, Fare_bin) using one-hot encoding.
4. Split data into training and validation sets.
5. Train a Random Forest classifier.
6. Evaluate using accuracy and classification report.
7. Print feature importances.

Expected Output:
- Printed accuracy and classification report.
- Feature importances bar chart (optional).

Time Complexity: O(n * log n) for Random Forest training (approximately).
Space Complexity: O(n * features) for the encoded dataset.
\"\"\"
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

def load_titanic_data(csv_path: str = None) -> pd.DataFrame:
    """
    Load Titanic dataset. If csv_path is None, create a small sample.
    """
    if csv_path is None:
        # Sample data (first few rows from the actual dataset)
        data = {
            'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'Survived': [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
            'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 3, 2],
            'Name': ['Braund, Mr. Owen Harris',
                     'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
                     'Heikkinen, Miss. Laina',
                     'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
                     'Allen, Mr. William Henry',
                     'Moran, Mr. James',
                     'McCarthy, Mr. Timothy J',
                     'Palsson, Master. Gosta Leonard',
                     'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
                     'Nasser, Mrs. Nicholas (Adele Achem)'],
            'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'female'],
            'Age': [22, 38, 26, 35, 35, np.nan, 54, 2, 27, 14],
            'SibSp': [1, 1, 0, 1, 0, 0, 0, 3, 0, 1],
            'Parch': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Ticket': ['A/5 21171', 'PC 17599',
                       'STON/O2. 3101282', '113803', '373450',
                       '330877', '17463', '349909', '347742', '237736'],
            'Fare': [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708],
            'Cabin': [np.nan, 'C85', np.nan, 'C123', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
            'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', 'C']
        }
        df = pd.DataFrame(data)
    else:
        df = pd.read_csv(csv_path)
    return df

def extract_title(name):
    """Extract title from name."""
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    return 'Unknown'

def preprocess_titanic(df):
    """Preprocess the Titanic dataframe."""
    df = df.copy()
    
    # Extract title
    df['Title'] = df['Name'].apply(extract_title)
    # Group rare titles
    title_mapping = {
        'Mr': 'Mr', 'Mrs': 'Mrs', 'Miss': 'Miss', 'Master': 'Master',
        'Dr': 'Officer', 'Rev': 'Officer', 'Col': 'Officer', 'Major': 'Officer',
        'Countess': 'Royalty', 'Jonkheer': 'Royalty', 'Don': 'Royalty',
        'Lady': 'Royalty', 'Sir': 'Royalty', 'the Countess': 'Royalty',
        'Ms': 'Miss', 'Mme': 'Mrs', 'Mlle': 'Miss'
    }
    df['Title'] = df['Title'].map(title_mapping)
    df['Title'] = df['Title'].fillna('Unknown')
    
    # Fill missing Embarked with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Fill missing Fare with median
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    
    # Fill missing Age with median per Pclass
    df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))
    
    # Create family size
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    # Create is_alone
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Bin Age
    df['AgeBin'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100], labels=['Child', 'Teen', 'YoungAdult', 'Adult', 'Senior'])
    # Bin Fare
    df['FareBin'] = pd.qcut(df['Fare'], q=4, labels=['Low', 'Medium', 'High', 'VeryHigh'])
    
    # Encode Sex
    df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})
    
    # Select features for modeling
    feature_cols = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'Title', 'FamilySize', 'IsAlone', 'AgeBin', 'FareBin']
    # Ensure all columns exist
    feature_cols = [c for c in feature_cols if c in df.columns]
    
    # One-hot encode categorical variables
    df_processed = pd.get_dummies(df[feature_cols], columns=['Embarked', 'Title', 'AgeBin', 'FareBin'], drop_first=True)
    
    return df_processed

def train_model(X, y):
    """Train a Random Forest model."""
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    accuracy = accuracy_score(y_val, y_pred)
    report = classification_report(y_val, y_pred)
    return model, accuracy, report, X_val, y_val, y_pred

def plot_feature_importances(model, feature_names):
    """Plot feature importances."""
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure(figsize=(10, 6))
    plt.title("Feature Importances")
    plt.bar(range(len(importances)), importances[indices], align="center")
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
    plt.tight_layout()
    plt.show()

# -------------------------
# Test Cases
# -------------------------
if __name__ == "__main__":
    # Load data
    df = load_titanic_data()
    print("Original data shape:", df.shape)
    print(df.head())
    
    # Preprocess
    X = preprocess_titanic(df)
    y = df['Survived']
    print("\nProcessed features shape:", X.shape)
    print("Feature names:", list(X.columns))
    
    # Train model
    model, accuracy, report, X_val, y_val, y_pred = train_model(X, y)
    print(f"\nValidation Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)
    
    # Assertions
    assert 0 <= accuracy <= 1, "Accuracy should be between 0 and 1"
    assert len(X_val) > 0, "Validation set should not be empty"
    
    # Plot feature importances (optional, comment out if no display)
    # plot_feature_importances(model, list(X.columns))
    
    print("\nAll tests passed!")