import sys
import math

def minimal_angle_pair(n, vectors):
    angles = []
    
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and 1-based index

    # Sort angles
    angles.sort()

    # To handle the circular nature, we append the first angle + 2π
    angles.append((angles[0][0] + 2 * math.pi, angles[0][1]))

    min_angle = float('inf')
    best_pair = (0, 0)

    # Find the minimal angle between consecutive angles
    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[i + 1]
        angle_diff = angle2 - angle1

        if angle_diff < min_angle:
            min_angle = angle_diff
            best_pair = (index1, index2)

    return best_pair

# Input reading
n = int(sys.stdin.readline().strip())
vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Get the result
result = minimal_angle_pair(n, vectors)

# Output the result
print(result[0], result[1])