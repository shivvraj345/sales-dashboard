import pandas as pd

# Load data
df = pd.read_csv('train.csv')

# Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Fill missing postal codes
df['Postal Code'] = df['Postal Code'].fillna(0)

# Add useful columns
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month

# Save cleaned file
df.to_csv('cleaned_sales.csv', index=False)
print("Done! Cleaned file saved!")
print(df.shape)