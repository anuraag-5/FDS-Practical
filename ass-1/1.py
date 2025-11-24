import pandas as pd

# 1) Create data for 10 students
data = {
    "name": ["Amit", "Riya", "Sahil", "Neha", "Kunal",
             "Pooja", "Vivek", "Sara", "Isha", "Rohan"],
    "age": [18, 19, 18, 20, 19, 18, 21, 20, 19, 18],
    "percentage": [78.5, 82.0, 69.5, 91.0, 74.0,
                   88.0, 65.5, 79.0, 85.0, 72.5]
}

# Create dataframe
df = pd.DataFrame(data)

# View the dataframe
print("DataFrame:\n", df, "\n")

# Shape (rows, columns)
print("Shape (rows, columns):", df.shape)

# Number of rows and columns
print("Number of rows:", df.shape[1])
print("Number of columns:", df.shape[0], "\n")

# Data types
print("Data types:\n", df.dtypes, "\n")

# Feature (column) names
print("Column names:", df.columns.tolist(), "\n")

# Description / basic statistics
print("Statistical description:\n", df.describe())   # only numeric columns
