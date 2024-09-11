import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer

data = pd.read_csv('datanalys/dup.csv')
print(data)
print("Here in this code we will remove all the duplicate values ")
duplicate = data.duplicated()
print(duplicate)
print("We can also filter and check which is duplicate\n\n\n")
print(data[duplicate])
print("Now we drop the duplicated values from the data\n\n\n")
data.drop_duplicates(inplace=True)#Here inplace true will make the changes in the real data
data.to_csv('datanalys/dup.csv', index=False)
print("Changes have been saved permanently to 'datanalys/dup.csv'.")
print(data)