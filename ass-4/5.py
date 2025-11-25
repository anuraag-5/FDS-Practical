import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target

# Count species frequency
freq = df["species"].value_counts()

plt.pie(freq.values, labels=["setosa", "versicolor", "virginica"], autopct="%1.1f%%")
plt.title("Pie Chart - Iris Species Frequency")
plt.show()

plt.hist(df["species"], bins=3, color="teal")
plt.title("Histogram of Iris Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.show()