import sys
import math

def minimal_angle_pair(n, vectors):
    angles = []
    
    # Calculate angles and sort them
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x) # angle in radians
        angles.append((angle, i + 1)) # store angle and index (1-based)

    # Sort by angle
    angles.sort()

    min_angle = float('inf')
    best_pair = (0, 0)

    # Check adjacent angles in the sorted list and also wrap around
    for i in range(n):
        angle1, idx1 = angles[i]
        angle2, idx2 = angles[(i + 1) % n]
        
        # Calculate the angle difference
        diff = angle2 - angle1
        if diff < 0:
            diff += 2 * math.pi
        
        # Non-oriented angle
        non_oriented_angle = min(diff, 2 * math.pi - diff)

        if non_oriented_angle < min_angle:
            min_angle = non_oriented_angle
            best_pair = (idx1, idx2)

    return best_pair

# Input reading
n = int(sys.stdin.readline().strip())
vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Get the result
result = minimal_angle_pair(n, vectors)

# Output the result
print(result[0], result[1])