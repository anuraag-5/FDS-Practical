import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.randint(1, 100, 50)

# Line Plot
plt.plot(data, color='blue')
plt.title("Line Plot of Random Data")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# Scatter Plot
plt.scatter(range(50), data, color='red')
plt.title("Scatter Plot of Random Data")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# Histogram
plt.hist(data, bins=10, color='green')
plt.title("Histogram of Random Data")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.boxplot(data)
plt.title("Box Plot of Random Data")
plt.show()