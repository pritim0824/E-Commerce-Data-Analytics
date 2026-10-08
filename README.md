# E-Commerce Data Analytics 📊

## 📌 Project Overview

This project performs data analysis on an e-commerce dataset using Python.

The objective of this project is to understand sales performance, customer ordering patterns, product distribution, payment methods, order status, referral sources, and order value trends.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- OpenPyXL
- VS Code
- Git & GitHub

## 📂 Dataset

The dataset contains 1,200 e-commerce orders and 14 columns.

### Dataset Columns

- OrderID
- Date
- CustomerID
- Product
- Quantity
- UnitPrice
- ShippingAddress
- PaymentMethod
- OrderStatus
- TrackingNumber
- ItemsInCart
- CouponCode
- ReferralSource
- TotalPrice

The original Excel dataset is not included in this public repository for privacy/data-sharing reasons.

## 🔍 Data Cleaning

The following data preparation steps were performed:

- Checked dataset structure and data types
- Checked missing values
- Filled missing `CouponCode` values with `No Coupon`
- Checked duplicate records
- Converted the `Date` column into datetime format
- Verified numerical columns for analysis

## 📊 Analysis Performed

### 1. Product Analysis

Analyzed the distribution of orders across different products using a bar chart.

### 2. Payment Method Analysis

Compared the number of orders using different payment methods such as:

- Online
- Cash
- Credit Card
- Debit Card
- Gift Card

The payment methods were relatively balanced, with Online being the highest and Gift Card being the lowest.

### 3. Order Status Analysis

Analyzed the distribution of different order statuses to understand the overall order situation.

### 4. Referral Source Analysis

Analyzed customer referral sources.

The major referral sources included:

- Instagram
- Email
- Google
- Facebook
- Referral

Instagram had the highest number of orders, while Referral had the lowest.

### 5. Date-wise Order Trend

Analyzed daily order activity using a line chart.

The number of daily orders varied, with most days having around 1–3 orders. There was no clear continuous upward or downward trend.

## 💰 Sales KPIs

| KPI | Value |
|---|---:|
| Total Sales | 1,264,761.96 |
| Average Order Value | 1,053.97 |
| Maximum Order Value | 3,456.40 |
| Minimum Order Value | 11.39 |

## 📈 Statistical Analysis

Descriptive statistics were calculated for important numerical columns.

| Metric | Mean | Median |
|---|---:|---:|
| Quantity | 2.95 | 3.00 |
| Unit Price | 356.41 | 364.21 |
| Items in Cart | 5.49 | 5.00 |
| Total Price | 1,053.97 | 823.62 |

## 🚨 Outlier Analysis

The Interquartile Range (IQR) method was used to identify potential outliers in `TotalPrice`.

- Q1: 410.52
- Q3: 1,578.48
- IQR: 1,167.96
- Upper Bound: 3,330.41
- Potential Outliers: 8

These high-value orders were identified as potential outliers but were not automatically removed because they may represent genuine high-value purchases.

## 📌 Key Insights

- Total sales generated were approximately 1.26 million.
- The average order value was approximately 1,053.97.
- The highest order value was 3,456.40.
- Payment methods showed a relatively balanced distribution.
- Instagram was the leading referral source.
- Daily order volume did not show a consistent increasing or decreasing trend.
- 8 potential high-value outliers were identified using the IQR method.

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/pritim0824/E-Commerce-Data-Analytics.git

### 2. Install the required libraries

```bash
python -m pip install -r requirements.txt
