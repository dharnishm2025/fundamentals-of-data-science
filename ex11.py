
import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("Hotel_Dataset.csv")
df

# Identify duplicate rows
df.duplicated()

# Display dataset information
df.info()

# Remove duplicate rows
df.drop_duplicates(inplace=True)
df

# Count the rows
len(df)

# Reset the index
index = np.array(list(range(0, len(df))))
df.set_index(index, inplace=True)
index
df

# Remove the unnecessary column
df.drop(['Age_Group.1'], axis=1, inplace=True)
df

# Replace invalid negative values with NaN
df.loc[df.CustomerID < 0, 'CustomerID'] = np.nan
df.loc[df.Bill < 0, 'Bill'] = np.nan
df.loc[df.EstimatedSalary < 0, 'EstimatedSalary'] = np.nan

# Replace invalid number of passengers with NaN
df.loc[(df['NoOfPax'] < 1) | (df['NoOfPax'] > 20), 'NoOfPax'] = np.nan

# Display unique values
df.Age_Group.unique()
df.Hotel.unique()

# Correct hotel names
df.Hotel.replace(['Ibys'], 'Ibis', inplace=True)

# Display food preference values
df.FoodPreference.unique()

# Standardize food preference values
df.FoodPreference.replace(
    ['Vegetarian', 'veg'], 'Veg', inplace=True
)
df.FoodPreference.replace(
    ['non-Veg'], 'Non-Veg', inplace=True
)

# Fill missing values using mean or median
df.EstimatedSalary.fillna(
    round(df.EstimatedSalary.mean()), inplace=True
)
df.NoOfPax.fillna(
    round(df.NoOfPax.median()), inplace=True
)
df['Rating(1-5)'].fillna(
    round(df['Rating(1-5)'].median()), inplace=True
)
df.Bill.fillna(
    round(df.Bill.mean()), inplace=True
)

# Display the cleaned dataset
df
