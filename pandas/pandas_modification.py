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