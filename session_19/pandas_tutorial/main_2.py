import pandas as pd

df = pd.read_excel("dummy_data.xlsx", 0)
print("Dataframe Loaded:\n", df.head())
print("Dataframe Info:\n", df.info())
df.dropna(inplace=True)
print("Dataframe Info:\n", df.info())
print("Dataframe Details:\n", df.describe())