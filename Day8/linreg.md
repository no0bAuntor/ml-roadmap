# 📈 Linear Regression

## 📘 Theory

Linear Regression is a **supervised learning algorithm** used to predict **continuous numeric values**. It models the relationship between one or more independent variables (features) and a dependent variable (target) by fitting a **straight line** through the data.

The general equation is:
$$
y = mx + b
$$

Where:
- `y` = predicted output  
- `x` = input feature  
- `m` = slope (how much y changes with x)  
- `b` = intercept (value of y when x = 0)

Linear regression aims to find the best-fit line by minimizing the **Mean Squared Error (MSE)** between predicted and actual values.

---

## 💡 Real-World Example

Imagine a scenario where you're predicting **student marks** based on the number of **hours studied**. As study hours increase, marks generally increase too.

You collect data like:
- 3 hours → 30 marks  
- 5 hours → 50 marks  
- 7 hours → 70 marks  

Linear regression will fit a straight line to this pattern and allow you to predict, say, what a student might score after 6.5 hours of study.

---

## ⚙️ Applications in Machine Learning

Linear Regression is commonly used in:

- 🏠 **Housing**: Predicting prices based on area, location, bedrooms
- 💰 **Finance**: Forecasting stock prices or sales trends
- 🎓 **Education**: Predicting student performance
- 🚗 **Energy**: Estimating fuel efficiency from engine size
- 📈 **Marketing**: Predicting ad campaign impact or sales revenue

It also serves as a **baseline model** for more complex regression algorithms in real-world ML systems.

---
