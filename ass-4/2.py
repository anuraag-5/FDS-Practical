import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1, 100, 50)

# Adding two extreme outliers
data = np.append(data, [300, 350])

plt.boxplot(data)
plt.title("Box Plot with Outliers")
plt.show()