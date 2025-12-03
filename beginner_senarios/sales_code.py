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
        df["total_revenue"]=df["price"]*df["quantity"]
        df.to_csv("beginner_senarios/sales.csv")
        print(df["total_revenue"])
    elif choice==2:
        hightest=df["total_revenue"].idxmax()
        print(f"your hightest producting itme is {df.loc[hightest,"item"]} with price {df.loc[hightest,"price"]} and revenue {df.loc[hightest,"total_revenue"]}")
    elif choice==3:
        df["averge_price"]=df["price"].mean()
        print(f"the averge price of items is {df[["item","averge_price"]]}")
    elif choice==4:
        df["sold"]=100-df["quantity"]
        df.to_csv("beginner_senarios/sales.csv")
        print(df["sold"])
        
        

print(main())

