import pandas as pd

df = pd.read_csv("Amazon.csv")

india_df = df[df["Country"] == "India"]

print(india_df)