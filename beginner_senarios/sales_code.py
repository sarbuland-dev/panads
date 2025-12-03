import pandas as pd
df=pd.read_csv("beginner_senarios/sales.csv")
def main():
    print("your menu is here::::")
    print("Total revenue")
    print("Which item generated the highest revenue?")
    print("Average price of items")
    print("Total number of items sold")
    choice=int(input("Enter your choice ::::::"))
    if choice==1:
        df["total_revenue"]=df[(df["price"])*(df["quantity"])]
        df.to_csv("beginner_senarios/sales.csv")