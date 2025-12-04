import pandas as pd
df=pd.read_csv("inter_senarios/online_order.csv")
df["revenue"]=df["quantity"]*df["price"]
grouped=df.groupby("product")["revenue"].sum()
print(grouped)
print("\n")
df["cus_revenue"]=df["quantity"]*df["price"]
grouped=df.groupby("customer_id")["cus_revenue"].sum()
print(grouped)
print("\n")
df["order"]=(df["order_date"]>"2025-11-03") & (df["order_date"]<"2025-11-06")
print(df[["order_id","order"]])
df["order"]=df["quantity"]*df["order_date"]
print(df["order"])
