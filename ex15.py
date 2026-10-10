import numpy as np
import pandas as pd

df = pd.read_csv("/content/pre-process_datasample.csv")
df
df.info()
df.head()
df.Country.fillna(df.Country.mode()[0], inplace=True)

df.Age.fillna(df.Age.median(), inplace=True)

df.Salary.fillna(round(df.Salary.mean()), inplace=True)

df
updated_dataset = pd.get_dummies(
    df, columns=["Country"], dtype=int
)

updated_dataset["Purchased"].replace(
    ["No", "Yes"], [0, 1], inplace=True
)

updated_dataset
