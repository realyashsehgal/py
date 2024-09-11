import pandas as pd
import numpy as np
import sklearn.impute as SimpleImputer
data = pd.read_csv('datanalys/filter.csv')
print(data)
print("\nFilterring the data based on the age who is older than 50\n")
filtered = data[data['Age'] > 50]
print(filtered)
filtered.to_csv('datanalys/gggg.csv')
print("\nNow we filter the filterre data by genders\n")
data = pd.read_csv('datanalys/gggg.csv')
filter_data = data[data['Gender'] == "Male"]
print(filter_data)
filter_data.to_csv('datanalys/gggg.csv')