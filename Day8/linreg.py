from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([[5], [3], [4], [6], [7], [8]])  # study hours
y = np.array([54, 22, 48, 70, 76, 95])        # marks

# Model
model = LinearRegression()
model.fit(x, y)

# Prediction
x_pred = np.array([[6.3]])
y_pred = model.predict(x_pred)

print(f"Predicted score: {y_pred[0]}")
print(f"Slope: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Plotting
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, model.predict(x), color='green', label='Regression Line')
plt.scatter(x_pred, y_pred, color='red', label='Predicted (6.3 hrs)')

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression - Study Hours vs Marks")
plt.legend()
plt.grid(True)
plt.show()
