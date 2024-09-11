import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('datanalys/sort.csv')
print(data)
print("\n\nSorting the csv file on the basis of age (Ascending)\n\n")
sorted_data = data.sort_values(by='Age',ascending=True)
print(sorted_data)
print("\n\nMaking these changes permanent in the csv file\n\n")
sorted_data.to_csv('datanalys/sort.csv', index=False)