import pandas as pd

# Sample data
df = pd.DataFrame({
    "values": [10, 12, 15, 18, 20, 25, 30]
})

print("DataFrame:\n", df)

# Mean
mean_val = df["values"].mean()

# Range = max - min
range_val = df["values"].max() - df["values"].min()

# IQR = Q3 - Q1
Q1 = df["values"].quantile(0.25)
Q3 = df["values"].quantile(0.75)
IQR = Q3 - Q1

print("\nMean:", mean_val)
print("Range:", range_val)
print("IQR:", IQR)