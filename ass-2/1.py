import numpy as np

# Original 2D array
arr = np.array([[0, 1],
                [2, 3]])

# Flatten the array
flat_arr = arr.flatten()

print("Original flattened array:", flat_arr)

# Find maximum and minimum
max_val = flat_arr.max()
min_val = flat_arr.min()

print("Maximum value of the above flattened array:", max_val)
print("Minimum value of the above flattened array:", min_val)