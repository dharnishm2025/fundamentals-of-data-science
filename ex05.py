
import pandas as pd

# Load the dataset
diabetes_df = pd.read_csv("diabetes.csv")

# Display the first few rows
print(diabetes_df.head())

# Dataset structure and summary statistics
print(db.info())
print(db.describe())

# Visualize the distribution of each feature
import matplotlib.pyplot as plt
import seaborn as sns

db.hist(bins=50, figsize=(20, 15))
plt.show()

# Pairplot to visualize relationships
sns.pairplot(db)
plt.show()
