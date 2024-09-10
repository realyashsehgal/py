import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("datanalys/Book1.csv",header = 0)
print(data.head())
missing_values = data.isnull().sum()
print("Missing values :")
print(missing_values)
imputer = SimpleImputer(strategy='median')
imputer.fit(data[['Age']])
data[['Age']] = imputer.transform(data[['Age']])

print(data.head(10))

print(data.dtypes)

unique_values = data['Height'].unique()
print(unique_values)

# Find unique values in each column
# for column in data.columns:
#     unique_values = data[column].unique()
#     print(f"Unique values in '{column}': {unique_values}")
data = data[data['Height'] != 873734544]
print(data)
