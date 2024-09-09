import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("datanalys/Book1.csv",header = 0)
print(data.head())
missing_values = data.isnull().sum()
print("Missing values :")
print(missing_values)