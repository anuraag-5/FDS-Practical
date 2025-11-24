import numpy as np

nums = np.array([0.5, 0.7, 1.1, 2.1, 3.2])
bins = np.array([0, 1, 2, 3])

hist, bin_edges = np.histogram(nums, bins=bins)

print("Histogram result: ", hist)
print("Bins: ", bin_edges)