
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Mall_Customers.csv')

df.info()
df.head()

# Visualize relationships between columns
sns.pairplot(df)

# Select Annual Income and Spending Score
features = df.iloc[:, [3, 4]].values

# Apply K-Means clustering
from sklearn.cluster import KMeans

model = KMeans(n_clusters=5, random_state=0, n_init=10)
model.fit(features)

# Add cluster labels to the dataset
Final = df.iloc[:, [3, 4]].copy()
Final['label'] = model.predict(features)

Final.head()

# Plot the clusters
plt.scatter(
    features[:, 0],
    features[:, 1],
    c=model.labels_
)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-Means Clustering of Mall Customers')
plt.show()
