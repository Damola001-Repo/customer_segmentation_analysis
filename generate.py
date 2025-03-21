import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_rows = 10000

# Customer IDS (unique identifiers)
customer_ids = [f"CUST{1000 + i}" for i in range(n_rows)]

# Demographics
ages = np.random.randint(18, 70, size=n_rows)
genders = np.random.choice(['Male', 'Female'], size=n_rows)
incomes = np.random.randint(30000, 120000, size=n_rows)
locations = np.random.choice(['Agege', 'Ajeromi_ifelodun',
                             'Alimosho', 'Ifako_ijaiye',
                             'Ikeja', 'Isolo', 'Mushin',
                             'Oshodi_isolo', 'Surulere'], size=n_rows)

# Transaction behaviour
transaction_counts = np.random.randint(1, 10, size=n_rows)
avg_transaction_amount = np.random.uniform(20, 500, size=n_rows)
total_spent = transaction_counts * avg_transaction_amount

# Last purchase date
last_purchase_date = [datetime.now() - timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)]

# Product categories
product_categories = np.random.choice(['Electronics', 'Fashion', 'Home Goods', 'Food', 'Books'], size=n_rows)

# Creating DataFrame
df = pd.DataFrame({
    'Customer_ID': customer_ids,
    'Age': ages,
    'Gender': genders,
    'Income': incomes,
    'Location': locations,
    'Transaction_count': transaction_counts,
    'Average_Transaction_Amount': avg_transaction_amount,
    'Total_Spent': total_spent,
    'Last_purchase_date': last_purchase_date,
    'Product_category': product_categories
})

df.to_csv('sales_record.csv')