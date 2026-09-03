# Day 1 Exercise: Pandas & NumPy Basics
import pandas as pd
import numpy as np

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", data)
print("Mean:", np.mean(data))

# Create a Pandas DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 92, 78]
})
print("\nDataFrame:")
print(df)
print("\nAverage Score:", df['Score'].mean())