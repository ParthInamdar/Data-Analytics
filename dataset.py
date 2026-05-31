import pandas as pd

df = pd.read_csv("Amazon.csv")

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
