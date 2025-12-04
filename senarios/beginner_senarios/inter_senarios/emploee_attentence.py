import pandas as pd
df=pd.read_csv("inter_senarios/emploee_attentence.csv")

pre=df[df["status"]=="Present"]
g=pre.groupby("name")["status"]
print(g.count())


# pre=df[df["status"]=="Present"]
# g=pre.groupby("name")["status"].count()
# df["attentence_pre"]=df["name"].map((g/30)*100)
# print(df[["name","attentence_pre"]])

# pre = df[df["status"] == "Present"]

# present_count = pre.groupby("name")["status"].count()

# attendance_percent = (present_count / 30) * 100

# print(attendance_percent)


absent_names = df[df["status"] == "Absent"]["name"]


present_only = df[~df["name"].isin(absent_names)]


print(present_only["name"].unique())




