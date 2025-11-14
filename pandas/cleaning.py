import pandas as pd
# firstly we read csv file::::::::::
df=pd.read_csv("CSV_Files/practise.csv")
# then we put values in cloumne at exect index:::::::
df.loc[5,"Age"]=24
# then we put in multipul indexs:::::::::
df.loc[[1,3,5],"Age"]=[23,45,67]
df.loc[6,"City"]="Lahore"
df.loc[[4,7],"Salary"]=[23000,12000]
df.loc[[2,8,5],"JoinDate"]=["2021-05-12","2022-03-12","2021-09-5"]
print(df)

# to remove spaces in the end and beginning::::::
cols = ["Name", "Age", "City", "Salary", "JoinDate"]

df[cols] = df[cols].apply(lambda x: x.str.replace(' ', '', regex=False))

df[cols] = df[cols].apply(lambda x: x.str.replace(r'\s+', ' ', regex=True).str.strip().str.upper())   # for upper
df[cols] = df[cols].apply(lambda x: x.str.replace(r'\s+', ' ', regex=True).str.strip().str.lower())     #for lower
df[cols] = df[cols].apply(lambda x: x.str.replace(r'\s+', ' ', regex=True).str.strip().str.title())    #for captilaiztion
print(df)

