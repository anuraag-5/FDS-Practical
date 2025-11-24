import numpy as np

# Two points (x1, y1) and (x2, y2)
p1 = np.array([1, 2])
p2 = np.array([4, 6])

# Euclidean Distance
distance = np.linalg.norm(p2 - p1)

print("Point 1:", p1)
print("Point 2:", p2)
print("Euclidean Distance: ", distance)