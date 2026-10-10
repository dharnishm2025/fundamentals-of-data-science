
import numpy as np
import pandas as pd

df = pd.read_csv("pre-process_datasample.csv")
df

# Fill missing values
df.Country.fillna(df.Country.mode()[0], inplace=True)
df.Age.fillna(df.Age.median(), inplace=True)
df.Salary.fillna(round(df.Salary.mean()), inplace=True)

df

# Convert categorical columns into numeric columns
df = pd.get_dummies(df, columns=['Country', 'Purchased'], dtype=int)

# Create the feature set
final_set = df
final_set

from sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler(feature_range=(0, 1))
mms.fit(final_set)

feat_minmax_scaler = mms.transform(final_set)
feat_minmax_scaler
