import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "name": ["Amit", "Riya", "Sahil", "Neha", "Kunal"],
    "percentage": [78.5, 82.0, 69.5, 91.0, 74.0]
}

df = pd.DataFrame(data)

# Line plot
plt.plot(df["name"], df["percentage"], marker='o')
plt.xlabel("Name")
plt.ylabel("Percentage")
plt.title("Name vs Percentage")
plt.grid(True)
plt.show()
