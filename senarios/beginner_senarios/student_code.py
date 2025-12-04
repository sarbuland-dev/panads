import pandas as pd
def main():
    df=pd.read_csv("beginner_senarios/student.csv")
    print("your menu is::: \n")
    print("Total students count")
    print("Average marks of each subject")
    print("Student with highest science marks")
    print("Add new column: Total Marks")
    print("Average total marks\n")
    choice=int(input("enter your choice::  "))
    if choice==1:
        total_student=df["name"].count()
        print(f"total student is {total_student}")
    elif choice==2:
        df["average"] = df[["math", "science", "english"]].mean(axis=1)
        print(f"averge marks are {df[["name","average"]]}")
    elif choice==3:
        df["total_marks"] = df[["math", "science", "english"]].sum(axis=1)
        toper=df["science"].idxmax()
        print(f"Congratulations !!!{df.loc[toper,"name"]} you top the class with Marks {df.loc[toper,"science"]}")
    elif choice==4:
        df["total_marks"] = df[["math", "science", "english"]].sum(axis=1)
        print(df[["name","total_marks"]])
        df.to_csv("beginner_senarios/student.csv", index=False)
        print("\nTotal marks column successfully saved to CSV!")
    elif choice==5:
        df["total_marks"] = df[["math", "science", "english"]].sum(axis=1)
        
        av=df["total_marks"].mean()
        print(av)
    else:
        print("Wrong inputs  ")

print(main())
        
        
        
        
        
    







