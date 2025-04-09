import math
import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])

vectors = []
for i in range(1, n + 1):
    x, y = map(int, data[i].split())
    angle = math.atan2(y, x)
    vectors.append((angle, i))

# Sort the vectors by angle
vectors.sort()

# To handle the circular nature, add the first vector to the end
vectors.append((vectors[0][0] + 2 * math.pi, vectors[0][1]))

min_angle = float('inf')
best_pair = (0, 0)

# Find the minimum angle between consecutive vectors
for i in range(n):
    angle1, index1 = vectors[i]
    angle2, index2 = vectors[i + 1]
    angle_diff = angle2 - angle1
    if angle_diff < min_angle:
        min_angle = angle_diff
        best_pair = (index1, index2)

print(best_pair[0], best_pair[1])