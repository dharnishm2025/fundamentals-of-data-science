import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

# Load the dataset
tips = sns.load_dataset('tips')

# Display the first five rows
tips.head()

# Quantitative analysis: distribution of total bill
sns.displot(tips.total_bill, kde=True)

sns.displot(tips.total_bill, kde=False)

# Relationship between tip and total bill
sns.jointplot(x=tips.tip, y=tips.total_bill)

sns.jointplot(x=tips.tip, y=tips.total_bill, kind="reg")
