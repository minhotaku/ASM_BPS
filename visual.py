import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
customers = pd.read_csv('customers.csv')
sales = pd.read_csv('sales.csv')
product_details = pd.read_csv('product_details.csv')
product_groups = pd.read_csv('product_groups.csv')

# Merge DataFrames
df = sales.merge(customers[['customer_id', 'city']], on='customer_id', how='left')
df = df.merge(product_details[['product_id', 'product_name', 'product_group_id']], on='product_id', how='left')  # Include product_group_id here
df = df.merge(product_groups[['product_group_id', 'product_group_name']], on='product_group_id', how='left')

# Convert 'sale_date' to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Filter data for 2023 (or your desired year)
df_2023 = df[df['sale_date'].dt.year == 2023]

# Plot sales trend by month
df_2023_agg = df_2023.groupby(pd.Grouper(key='sale_date', freq='M'))['total_amount'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(df_2023_agg['sale_date'], df_2023_agg['total_amount'])
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.title('Sales Trend by Month in 2023', fontsize=14)
plt.grid(axis='y')
plt.show()

# Find and plot top 10 selling products
top_products = df_2023.groupby('product_name')['quantity'].sum().nlargest(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar')
plt.xlabel('Product', fontsize=12)
plt.ylabel('Quantity Sold', fontsize=12)
plt.title('Top 10 Selling Products in 2023', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotate and align labels for readability
plt.show()


sales_by_product_group = df_2023.groupby('product_group_name')['total_amount'].sum()
plt.figure(figsize=(12, 6))
sales_by_product_group.plot(kind='bar')
plt.xlabel('Product Group', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.title('Sales Distribution by Product Group in 2023', fontsize=14)
plt.xticks(rotation=45)
plt.show()

