import pandas as pd 

df1=pd.read_csv("customers.csv")
df2=pd.read_csv("transactions.csv")
df3=pd.read_csv("products.csv")

# change csv to excel or jason according to file type

print(df1.shape)
print(df2.shape)
print(df3.shape)
#this tell no of rows and columns for in depth use infO() and describe funtions

print(df1.dtypes)
print(df2.dtypes)
print(df3.dtypes)
# this gives each data type of each columns in each df

print(df1.head(3))
print(df2.head(3))
print(df3.head(3))
#this display top 3 data of each files for bottom three use tail

print(df1.isnull().sum())
print(df2.isnull().sum())
print(df3.isnull().sum())
#isnull or not null give boolean for null value in a column and then sum() just add them

duplicates=df2['transaction_id'].duplicated().sum()
print(duplicates)
#duplicated() marks duplicate entity as true 

print(df3.columns)

earlist=df1["signup_date"].min()
print(earlist)
latest=df1["signup_date"].max()
print(latest)

df2["timestamp"]=pd.to_datetime(df2["timestamp"])
print(df2["timestamp"])

hours=df2["timestamp"].dt.hour
print(hours)

months=df2["timestamp"].dt.month_name()
print(months)

day=df2["timestamp"].dt.day_name()
print(day)

#here dt is panad function datetime accessor it let us access date and time