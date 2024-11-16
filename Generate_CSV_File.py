import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Some random comments

# Number of rows to generate
n_rows = 10000

# Create data dictionary
data = {
    'ID': range(1, n_rows + 1),
    'Date': [(datetime(2023, 1, 1) + timedelta(days=x)).strftime('%Y-%m-%d') 
             for x in range(n_rows)],
    'Value': np.random.randint(1000, 10000, n_rows),
    'Category': np.random.choice(['A', 'B', 'C', 'D'], n_rows),
    'Score': np.random.uniform(0, 100, n_rows).round(2),
    'Status': np.random.choice(['Active', 'Pending', 'Closed'], n_rows),
    'Quantity': np.random.randint(1, 1000, n_rows),
    'Price': np.random.uniform(10, 1000, n_rows).round(2),
    'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_rows),
    'Priority': np.random.choice(['High', 'Medium', 'Low'], n_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv('large_dataset.csv', index=False)

# Print first 5 rows as preview
print(df.head())
