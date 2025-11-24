import pandas as pd

df = pd.read_csv("Data.csv")
print("\nOrignal DataSet")
print(df)

print(df.describe(include="all"))
print("Shape of Dataset\n")
print(df.shape)
print("First 3 rows\n")
print(df.head())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\n\n=== After Filling Missing Values in Age and Salary ===")
print(df)

country_dummies = pd.get_dummies(df["Country"], prefix="Country")
df = pd.concat([country_dummies, df.drop(columns=["Country"])], axis=1)
df["Purchased"] = df["Purchased"].map({"No": 0, "Yes": 1})

print("\n=== Final Data After Preprocessing ===")
print(df)