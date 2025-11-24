import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SOCR-HeightWeight.csv")

plt.scatter(df["Height(Inches)"], df["Weight(Pounds)"])
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.title("Scatter Plot: Height vs Weight")
plt.grid(True)
plt.show()
