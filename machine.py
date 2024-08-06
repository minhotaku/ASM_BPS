import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the sales data
sales_df = pd.read_csv('sales.csv')

# Convert 'sale_date' to datetime
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'])

# Extract features and target variable
# For simplicity, let's assume we want to predict total sales amount based on the quantity sold and the month of the sale
sales_df['month'] = sales_df['sale_date'].dt.month
X = sales_df[['quantity', 'month']]
y = sales_df['total_amount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the mean squared error (MSE) and the coefficient of determination (R^2 score)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Plot the actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted Sales Amount')
plt.show()

# Predict future sales
future_quantity = 50
future_month = 8
future_sales = model.predict(np.array([[future_quantity, future_month]]))

print(f'Predicted Sales Amount for Quantity {future_quantity} in Month {future_month}: {future_sales[0]}')