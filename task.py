import pandas as pd

customers = pd.read_csv("Customers.csv")
products = pd.read_csv("Products.csv")
transactions = pd.read_csv("Transactions.csv")

# --- Display shapes ---
print("===== SHAPE OF EACH DATAFRAME =====")
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Transactions:", transactions.shape)
print("\n")