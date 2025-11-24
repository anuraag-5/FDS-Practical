import pandas as pd

# Load CSV into dataframe
df = pd.read_csv("SOCR-HeightWeight.csv")

# Print first 20 rows
print("First 20 rows:\n")
print(df.head(20))
print("First 20 rows:\n")
print(df.tail(20))

# Basic statistical details
print("\nStatistical summary:\n")
print(df.describe())

# Add BMI column
# Height in inches → convert to meters → inches * 0.0254
# Weight in pounds → convert to kg → pounds * 0.453592
df["Height(Inches)"] = df["Height(Inches)"] * 0.0254
df["Weight(Pounds)"] = df["Weight(Pounds)"] * 0.453592
df["BMI"] = df["Weight(Pounds)"] / (df["Height(Inches)"] ** 2)

print("\nDataFrame with BMI column:\n")
print(df.head())
