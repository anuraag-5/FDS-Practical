import numpy as np

points = np.array([
    [1, 2],
    [4, 6],
    [7, 3]
])

n = len(points)

print("Manhattan distance between all pairs:")

for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]
        dist = np.abs(p2 - p1).sum()
        print(f"{p1} <-> {p2} = {dist}")