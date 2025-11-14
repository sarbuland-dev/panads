import pandas as pd
data={
    "Name":["ali","ahmad","kamal","talwar khan","azad khan"],
    "Age":[23,21,22,21,22],
    "City":["lahore","karachi","Talwandi","kasur","islamabad"],
    "salary":[2000,23000,56000,45000,10000]
}

df=pd.DataFrame(data)
print(df)
df.insert(0,"id",["A1","A2","A3","A4","A5"])
print("\n with index to chosse loction\n",df)

# this is called straight forword method used when you are not inserting in that where your column be create :
df["bounce"]=df["salary"] * 0.1
print("\n with no location\n",df)
print()

# now we update the value,,,,where 2 is row index or os column ka name kis ki row ka index ha = new value jo ky 24 ha
df.loc[2,"Age"]=24
print(df)

# now to remove :::
df.drop(columns=["id"],inplace=True)
print(df)
print()
# now remove multiple columns:
df.insert(0,"id",["A1","A2","A3","A4","A5"])     #firsty we create id column again phe error ni ay ga
df.drop(columns=["id","bounce"],inplace=True)
print(df)


# now we want to check missing values then use isnull()for checking values and isnull().sum() to check how much values :
data={
    "Name":["ali",None,"kamal","talwar khan","azad khan"],
    "Age":[23,21,22,None,22],
    "City":["lahore",None,"Talwandi","kasur",None],
    "salary":[None,23000,56000,45000,10000]
}

df=pd.DataFrame(data)
print(df.isnull())
print()
print(df.isnull().sum())

print(df.dropna(axis=0,inplace=False))

print()

print(df.dropna(axis=1,inplace=False))
print()

print(df.dropna(inplace=False))
print()
print(df.fillna("not define",inplace=True))
print(df)
# ab kisi specfic cloumn ko access karna ha
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

# kisi bi column may none value ki jaga koi asstimeted value ko put karna
df["Age"]=df["Age"].interpolate(method="linear",axis=0)
print(df)
# grouping:::::
data={
    "Name":["ali","ahmad","kamal","ahmad","azad khan"],
    "Age":[23,21,22,21,22],
    "City":["lahore","karachi","Talwandi","kasur","islamabad"],
    "salary":[2000,23000,56000,45000,10000]
}
df=pd.DataFrame(data)
print(df.groupby("Age")["salary"].sum())
print()
print(df.groupby("Age")["salary"].min())
print(df.min())
print()
print(df.groupby("Age")["Name"].min())
# with multiple conditions ::::
print(df.groupby(["Age","Name"])["salary"].sum())

data={
    "id":[1,2,3,4],
    "name":["ahmad","ali","khan","jawad"]
}
df_1=pd.DataFrame(data)

data={
    "id":[1,2,4,5],
    "order":[234,56,78,1200]
}
df_2=pd.DataFrame(data)
df=pd.merge(df_1,df_2,on="id",how="inner")
print("with inner",df)
print()
df=pd.merge(df_1,df_2,on="id",how="outer")
print("with outer",df)
print()
df=pd.merge(df_1,df_2,on="id",how="left")
print("with left",df)
print()
df=pd.merge(df_1,df_2,on="id",how="right")
print("with right",df)
print()
# is may column ni dyt ku ky wo saab ko merge kart dyta ha::::::::
df=pd.merge(df_1,df_2,how="cross")
print("with cross",df)



