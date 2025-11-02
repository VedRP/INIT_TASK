import pandas as pd 

df1=pd.read_csv("customers.csv")
df2=pd.read_csv("transactions.csv")
df3=pd.read_csv("products.csv")



for column in df1.columns:
    if df1[column].dtype in ['int64','float64']:
      df1[column].fillna(df1[column].mean(),inplace=True)
    else:
      df1[column].fillna(df1[column].mode()[0], inplace=True)  

for column in df2.columns:
    if df2[column].dtype in ['int64', 'float64']:
        df2[column].fillna(df2[column].median(), inplace=True)
    else:
        df2[column].fillna(df2[column].mode()[0], inplace=True)


for column in df3.columns:
    if df3[column].dtype in ['int64', 'float64']:
        df3[column].fillna(df3[column].median(), inplace=True)
    else:
        df3[column].fillna(df3[column].mode()[0], inplace=True)


print(df1.isnull().sum())  
print(df2.isnull().sum()) 
print(df3.isnull().sum())       

# first we check which column in the data frame is either or int or float then fillna input mean() value of that columns in the null place in that column
# further in else we use same but put mode which is inputs most comman value in that place   
revenue=df2["quantity"] * df2["price"]  
print(revenue)  

df4=pd.merge(df1,df2,on="customer_id",how="right")
#here all fromtrancation would be present but extra from df1 would be none

df5=pd.merge(df4,df3,on="product_id",how="left")

print(df5)

profitmargin=(((df5["price"]-df5["cost_price"]).sum())/((df5["price"].sum())))*100
print(profitmargin)


# task c
df5["revenue"]=df5["quantity"] * df5["price"]
total_revenue = df5.groupby("customer_id")["revenue"].sum().reset_index()
total_revenue.rename(columns={"revenue": "total_revenue"}, inplace=True)
print(total_revenue)

total_transaction=df5.groupby("customer_id")["transaction_id"].count().reset_index()
total_transaction.rename(columns={"transaction_id":"total_transaction"},inplace=True)
print(total_transaction)


avgtran = df5.groupby("customer_id")["revenue"].mean().reset_index()
avgtran.rename(columns={"revenue": "avgtran"}, inplace=True)


print(avgtran)

# frecat = df5.groupby("customer_id")["category"].mode().reset_index() 
# frecat.rename(columns={"category":"frecat"}, inplace=True) 
# print(frecat)
#  problem:-AttributeError: 'SeriesGroupBy' object has no attribute 'mode'


df5["timestamp"] = pd.to_datetime(df5["timestamp"])
df5["months"] = df5["timestamp"].dt.month_name()

monrev=df5.groupby("months")["revenue"].sum().reset_index()
monrev.rename(columns={"revenue": "monrev"},inplace=True)
print(monrev)

monuniq=df5.groupby("months")["customer_id"].nunique().reset_index()
monuniq.rename(columns={"customer_id": "monuniq"},inplace=True)
print(monuniq)


monavg=df5.groupby("months")["revenue"].mean().reset_index()
monavg.rename(columns={"revenue": "monavg"},inplace=True)
print(monavg)


prorev=df5.groupby("product_id")["revenue"].sum().reset_index()
prorev.rename(columns={"revenue": "prorev"},inplace=True)

topprorev=prorev.sort_values("prorev",ascending=False).head(10)
print(topprorev)

proquantity=df5.groupby("product_id")["quantity"].sum().reset_index()
proquantity.rename(columns={"quantity": "proquantity"},inplace=True)
topquantity=proquantity.sort_values("proquantity",ascending=False).head(10)
print(topquantity)

df5["profitmargin"]=((df5["price"]-df5["cost_price"])/df5["price"])*100

proprof=df5.groupby("product_id")["profitmargin"].mean().reset_index()
proprof.rename(columns={"profitmargin":"proprof"},inplace=True)

topprop=proprof.sort_values("proprof",ascending=False)
print(topprop.head(10))


df5["timestamp"]=pd.to_datetime(df5["timestamp"])
df5["Dates"]=df5["timestamp"].dt.date

recency=df5.groupby("customer_id")["Dates"].max().reset_index()
recency.rename(columns={"Dates":"recency"},inplace=False)

print(recency)

monetary = df5.groupby("customer_id")["revenue"].sum().reset_index()
monetary.rename(columns={"revenue": "Monetary"}, inplace=True)
print(monetary)