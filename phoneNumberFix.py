import pandas as pd

df1 = pd.read_csv("/Users/matthewuytioco/PycharmProjects/practicum_final_merge/final_merge.csv")

df1["phone"] = df1["phone"].str.replace(r'[()-]', '', regex=True)

print(df1)

df1.to_csv('data_cleaned.csv', index=False)