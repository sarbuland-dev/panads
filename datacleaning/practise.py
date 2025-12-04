import pandas as pd
df=pd.read_csv("datacleaning/practise.csv")
df.fillna({"age":21},inplace=True)
df.fillna({"salary":21000},inplace=True)

print(df.to_string())

df["age"] = df["age"].replace("twenty-nine", 29)
print(df)
df["department"]=df["department"].replace("it","IT")
print(df)
df["age"]=df["age"].replace(30,21)
print(df)