import sys
import math

def find_min_angle_pair(n, vectors):
    angles = []

    # Calculate angles and store with their original indices
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)  # Angle in radians
        angles.append((angle, i + 1))  # Store angle and 1-based index

    # Sort angles
    angles.sort()

    # Initialize minimum angle and pair of indices
    min_angle = float('inf')
    min_pair = (0, 0)

    # Check adjacent angles in the sorted list
    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[(i + 1) % n]  # Wrap around to first element
        
        # Calculate the non-oriented angle
        angle_diff = angle2 - angle1
        if angle_diff < 0:
            angle_diff += 2 * math.pi
        
        # Update minimum angle and pair if found a smaller angle
        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (index1, index2)

    return min_pair

# Read input
n = int(sys.stdin.readline().strip())
vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Find and print the result
result = find_min_angle_pair(n, vectors)
print(result[0], result[1])