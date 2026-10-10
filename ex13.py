
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

# Reset the index
index = np.array(list(range(0, len(df))))
df.set_index(index, inplace=True)

# Drop the duplicate Age_Group column
df.drop(['Age_Group.1'], axis=1, inplace=True)

# Replace inappropriate negative values with NaN
df.loc[df.CustomerID < 0, 'CustomerID'] = np.nan
df.loc[df.Bill < 0, 'Bill'] = np.nan
df.loc[df.EstimatedSalary < 0, 'EstimatedSalary'] = np.nan

# Replace inappropriate NoOfPax values with NaN
df.loc[(df['NoOfPax'] < 1) | (df['NoOfPax'] > 20), 'NoOfPax'] = np.nan

# Check unique values
df.Age_Group.unique()
df.Hotel.unique()

# Correct inconsistent hotel names
df.Hotel.replace(['Ibys'], 'Ibis', inplace=True)

# Standardize food preferences
df.FoodPreference.replace(['Vegetarian', 'veg'], 'Veg', inplace=True)
df.FoodPreference.replace(['non-Veg'], 'Non-Veg', inplace=True)

# Fill missing numerical values
df.EstimatedSalary.fillna(round(df.EstimatedSalary.mean()), inplace=True)
df.NoOfPax.fillna(round(df.NoOfPax.median()), inplace=True)
df['Rating(1-5)'].fillna(round(df['Rating(1-5)'].median()), inplace=True)
df.Bill.fillna(round(df.Bill.mean()), inplace=True)

# Display the cleaned dataset
df
