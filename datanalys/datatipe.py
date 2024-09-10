import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer

data = pd.read_csv('datanalys/datatype.csv')
print(data)

print("In this we will convert data type")
print(data.dtypes)
print("Here by default data type of income is float so we convert it to int\n\n\n")
data['Income'] = data['Income'].astype(int)
print(data.dtypes)
print(data)