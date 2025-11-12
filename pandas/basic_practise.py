#  Read CSV file
import pandas as pd
df=pd.read_csv("CSV_Files/pandas_practice.csv")
print(df)
print()
# # Read Excel file
df=pd.read_excel("Excel_file/pandas_practice.xlsx")
print(df)
print()
# # Read Jason file
df=pd.read_json("jason file/pandas_practice.json")
print(df)

# create file
data={
    "Name":["ali","ahmad","kamal"],
    "Age":[23,21,22],
    "City":["lahore","karachi","Talwandi"]
}
df=pd.DataFrame(data)
df.to_csv("output.csv",index=False)
print(df)
print()
df2=pd.read_csv("output.csv")
print(df2)
# Asy hi ya excel may bi ho sakta ha or jason may bi

# now head() and tail() concept
df=pd.read_csv("CSV_Files/large_practice_data (1).csv")
print("print 10 row first")
print(df.head(10))
print()
print("print 10 row last")
print(df.tail(10))

# info() ap ko bata ha ky kon sa cloumn kis data type ka ha kitny column kiyny rows ak compltete summary bana kar dyta ha
df=pd.read_csv("CSV_Files/large_practice_data (1).csv")
print("show complete summary \n ")

print(df.info())
print()

print()
print(df.describe())
print()
print(df.shape)
print(df.columns)
data={
    "Name":["ali","ahmad","kamal","talwar khan","azad khan"],
    "Age":[23,21,22,21,22],
    "City":["lahore","karachi","Talwandi","kasur","islamabad"],
    "salary":[2000,23000,56000,45000,10000]
}
df=pd.DataFrame(data)
print(df)
print()
# sigle column ko access karna ha ab
print(df["Name"])
# now multiple 
print()
col=df[["Name","Age"]]
print(col)

# now we filter the rows
col=df[df["salary"]>5000]
print(col)
print()
col=df[(df["salary"]>10000) | (df["Age"]>20)]
print(col)
print()
col=df[(df["salary"]>10000) & (df["Age"]>20)]
print(col)