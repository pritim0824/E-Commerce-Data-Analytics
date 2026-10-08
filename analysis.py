import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Excel file load
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# Missing CouponCode ko "No Coupon" se replace karna
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

print("\n--- Descriptive Statistics ---")

print("\nQuantity:")
print("Mean:", df['Quantity'].mean())
print("Median:", df['Quantity'].median())
print("Count:", df['Quantity'].count())

print("\nUnit Price:")
print("Mean:", df['UnitPrice'].mean())
print("Median:", df['UnitPrice'].median())
print("Count:", df['UnitPrice'].count())

print("\nItems in Cart:")
print("Mean:", df['ItemsInCart'].mean())
print("Median:", df['ItemsInCart'].median())
print("Count:", df['ItemsInCart'].count())

print("\nTotal Price:")
print("Mean:", df['TotalPrice'].mean())
print("Median:", df['TotalPrice'].median())
print("Count:", df['TotalPrice'].count())

print("\n--- Product-wise Order Count ---")

product_counts = df['Product'].value_counts()

print(product_counts)

# Product-wise Bar Chart

plt.figure(figsize=(10, 6))

product_counts.plot(kind='bar')

plt.title('Number of Orders by Product')
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("\n--- Orders by Payment Method ---")

payment_counts = df['PaymentMethod'].value_counts()

print(payment_counts)

# Payment Method Bar Chart

plt.figure(figsize=(8, 5))

payment_counts.plot(kind='bar')

plt.title('Orders by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

print("\n--- Orders by Order Status ---")

status_counts = df['OrderStatus'].value_counts()

print(status_counts)

# Order Status Bar Chart

plt.figure(figsize=(8, 5))

status_counts.plot(kind='bar')

plt.title('Orders by Order Status')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# Total Price Distribution

plt.figure(figsize=(10, 5))

plt.hist(df['TotalPrice'], bins=20)

plt.title('Distribution of Total Order Price')
plt.xlabel('Total Price')
plt.ylabel('Number of Orders')

plt.tight_layout()
plt.show()

# Total Price Box Plot

plt.figure(figsize=(10, 5))

sns.boxplot(x=df['TotalPrice'])

plt.title('Box Plot of Total Price')
plt.xlabel('Total Price')

plt.tight_layout()
plt.show()

# Outlier Calculation using IQR

Q1 = df['TotalPrice'].quantile(0.25)
Q3 = df['TotalPrice'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df['TotalPrice'] < lower_bound) |
    (df['TotalPrice'] > upper_bound)
]

print("\n--- Total Price Outlier Analysis ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Outliers:", len(outliers))

print("\n--- Orders by Referral Source ---")

referral_counts = df['ReferralSource'].value_counts()

print(referral_counts)

plt.figure(figsize=(10, 5))

referral_counts.plot(kind='bar')

plt.title('Orders by Referral Source')
plt.xlabel('Referral Source')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Date-wise Order Trend

df['Date'] = pd.to_datetime(df['Date'])

daily_orders = df.groupby('Date').size()

print("\n--- Date-wise Orders ---")
print(daily_orders)

plt.figure(figsize=(12, 5))

daily_orders.plot(kind='line')

plt.title('Order Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Orders')

plt.tight_layout()
plt.show()

# Total Sales Analysis

total_sales = df['TotalPrice'].sum()
average_order_value = df['TotalPrice'].mean()
maximum_order_value = df['TotalPrice'].max()
minimum_order_value = df['TotalPrice'].min()

print("\n--- Sales Analysis ---")
print("Total Sales:", total_sales)
print("Average Order Value:", average_order_value)
print("Maximum Order Value:", maximum_order_value)
print("Minimum Order Value:", minimum_order_value)