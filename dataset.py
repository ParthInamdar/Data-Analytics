import pandas as pd

df = pd.read_csv("Amazon.csv")

print(df.info())
print(df.head(2))