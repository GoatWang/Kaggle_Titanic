import pandas as pd

df = pd.read_csv('train.csv')
print("columns", df.columns)
print("length", len(df))
print(df)