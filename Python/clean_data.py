import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('customers.csv')

print("Missing values in each column:")
print(df.isnull().sum())

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Option 1: Remove rows with missing values
df_cleaned = df.dropna()
print("After removing rows with missing values:")
print(df_cleaned.isnull().sum())

# Option 2: Fill missing values with a specific value (e.g., 'Unknown' for strings, 0 for numbers)
df_filled = df.fillna({'email': 'Unknown', 'phone': '0000000000'})
print("After filling missing values with specific values:")
print(df_filled.isnull().sum())

# Option 3: Fill missing values with the mean of the column (for numerical data)
df['zip_code'] = df['zip_code'].fillna(df['zip_code'].mean())
print("After filling missing values with the mean:")
# print(df.isnull().sum())


# Remove rows where 'zip_code' is not a valid number
df = df[pd.to_numeric(df['zip_code'], errors='coerce').notnull()]

# Convert 'created_at' and 'updated_at' columns to datetime
df['created_at'] = pd.to_datetime(df['created_at'])
df['updated_at'] = pd.to_datetime(df['updated_at'])

# Validate and correct phone numbers (example: ensure they are 10 digits long)
df['phone'] = df['phone'].apply(lambda x: x if len(str(x)) == 10 else '0000000000')

print("After handling erroneous data:")
print(df.head())


# Save the cleaned DataFrame to a new CSV file
df.to_csv('customers_cleaned.csv', index=False)
