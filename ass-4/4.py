from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

# Count species frequency
freq = df["species"].value_counts()

plt.bar(freq.index, freq.values, color="purple")
plt.title("Frequency of Iris Species")
plt.xlabel("Species (0 = setosa, 1 = versicolor, 2 = virginica)")
plt.ylabel("Count")
plt.show()