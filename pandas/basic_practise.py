#  Read CSV file
import pandas as pd
# df=pd.read_csv("CSV_Files/pandas_practice.csv")
# print(df)
# print()
# # Read Excel file
# df=pd.read_excel("Excel_file/pandas_practice.xlsx")
# print(df)
# print()
# # Read Jason file
# df=pd.read_json("jason file/pandas_practice.json")
# print(df)

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
