
import numpy as np
import pandas as pd

df = pd.read_csv('Iris.csv')
df.info()

df.variety.value_counts()
df.head()

features = df.iloc[:, :-1].values
label = df.iloc[:, 4].values

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=0
)

model = KNeighborsClassifier()
model.fit(x_train, y_train)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

# Predict the variety of a flower
print(model.predict(x_test))
