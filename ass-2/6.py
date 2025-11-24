import pandas as pd

# Student data
data = {
    "name": ["Amit", "Riya", "Sahil", "Neha", "Kunal"],
    "graduation_percentage": [78, 82, 69, 91, 74],
    "age": [21, 22, 20, 23, 21]
}

df = pd.DataFrame(data)

print("Student DataFrame:\n")
print(df)

# Average age
avg_age = df["age"].mean()
print("\nAverage age of students:", avg_age)

# Average graduation percentage
avg_grad = df["graduation_percentage"].mean()
print("Average graduation percentage:", avg_grad)

# Describe all basic statistics
print("\nBasic Statistics of Data:\n")
print(df.describe())
