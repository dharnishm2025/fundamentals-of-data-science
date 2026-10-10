
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline

data = pd.read_csv('/content/Iris_Dataset.csv')

data

data.info()

data.describe()

# Visualize the data
sns.pairplot(data, hue='variety')

plt.show()
