
import numpy as np
import pandas as pd

df = pd.read_csv('Social_Network_Ads.csv')
df.head()

# Select input features and target
features = df.iloc[:, [2, 3]].values
label = df.iloc[:, 4].values

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=0
)

model = LogisticRegression()
model.fit(x_train, y_train)

# Check model accuracy
print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

# Predict purchases
print(model.predict(x_test))

from sklearn.metrics import classification_report
print(classification_report(label, model.predict(features)))
