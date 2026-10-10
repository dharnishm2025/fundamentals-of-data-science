
import numpy as np
import pandas as pd

df = pd.read_csv('Salary_data.csv')
df

df.info()
df.dropna(inplace=True)
df.info()
df.describe()

features = df.iloc[:, [0]].values
label = df.iloc[:, [1]].values

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=0
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)

# Check model performance
print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

# Display coefficient and intercept
print(model.coef_)
print(model.intercept_)

# Save the trained model
import pickle
pickle.dump(model, open('SalaryPred.model', 'wb'))

# Load the saved model
model = pickle.load(open('SalaryPred.model', 'rb'))

# Predict salary
yr_of_exp = float(input("Enter Years of Experience: "))
yr_of_exp_NP = np.array([[yr_of_exp]])
Salary = model.predict(yr_of_exp_NP)

print("Estimated Salary for {} years of experience is {}".format(
    yr_of_exp, Salary
))
