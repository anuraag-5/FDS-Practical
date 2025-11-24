import numpy as np
import pandas as pd   # for NaN

data = {
    "name": ["Amit", "Riya", "Sahil", "Neha", "Kunal",
             "Pooja", "Vivek", "Sara", "Isha", "Rohan"],
    "age": [18, 19, 18, 20, 19, 18, 21, 20, 19, 18],
    "percentage": [78.5, 82.0, 69.5, 91.0, 74.0,
                   88.0, 65.5, 79.0, 85.0, 72.5]
}

# Create dataframe
df = pd.DataFrame(data)

# 5 new rows (some duplicate, some with missing values)
new_rows = [
    {"name": "Amit",  "age": 18,   "percentage": 78.5},   # duplicate of 1st
    {"name": "Riya",  "age": 19,   "percentage": None},   # missing percentage
    {"name": None,    "age": 20,   "percentage": 90.0},   # missing name
    {"name": "Kunal", "age": None, "percentage": 74.0},   # missing age
    {"name": "Neha",  "age": 20,   "percentage": 91.0},   # duplicate of Neha
]

# Convert to DataFrame and append
new_df = pd.DataFrame(new_rows)
df = pd.concat([df, new_df], ignore_index=True)

# Add 'remarks' column with empty values
df["remarks"] = ""

# Drop 'remarks' column
df = df.drop(columns=["remarks"])

# Replace empty strings with proper NaN (if any)
df = df.replace("", pd.NA)

# Drop all rows that have ANY null / NaN value
df_clean = df.dropna()

print("Data after dropping 'remarks' and removing null/empty values:\n", df_clean)
