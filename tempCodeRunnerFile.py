proprof=df5.groupby("product_id")["profitmargin"].sum().reset_index()
propof.rename(columns={"profitmargin":"propof"},inplace=True)

propof.sort_values("propof",ascending=False)
print(propof.head(10))