import sys
import math

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
vectors = []

for i in range(1, n + 1):
    x, y = map(int, data[i].split())
    angle = math.atan2(y, x)
    vectors.append((angle, i))

# Sort vectors based on the angle
vectors.sort()

min_angle = float('inf')
index_pair = (0, 0)

# Find the minimum angle between consecutive vectors
for i in range(n):
    angle1, index1 = vectors[i]
    angle2, index2 = vectors[(i + 1) % n]  # Wrap around using modulo
    angle_diff = angle2 - angle1
    
    # Ensure the angle is non-negative
    if angle_diff < 0:
        angle_diff += 2 * math.pi
    
    # Calculate the non-oriented angle
    non_oriented_angle = min(angle_diff, 2 * math.pi - angle_diff)

    if non_oriented_angle < min_angle:
        min_angle = non_oriented_angle
        index_pair = (index1, index2)

print(index_pair[0], index_pair[1])