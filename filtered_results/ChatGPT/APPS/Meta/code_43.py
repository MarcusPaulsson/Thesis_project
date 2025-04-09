import sys
import math

def minimal_angle_pair(n, vectors):
    angles = []
    
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and original index
    
    # Sort angles
    angles.sort()
    
    min_angle = float('inf')
    min_pair = (0, 0)
    
    # Check the angle between consecutive sorted angles and also the wrap around
    for i in range(n):
        angle1, idx1 = angles[i]
        angle2, idx2 = angles[(i + 1) % n]  # Wrap around to first element
        
        # Calculate the non-oriented angle between the two angles
        angle_diff = abs(angle1 - angle2)
        non_oriented_angle = min(angle_diff, 2 * math.pi - angle_diff)
        
        if non_oriented_angle < min_angle:
            min_angle = non_oriented_angle
            min_pair = (idx1, idx2)
    
    return min_pair

# Read input
n = int(input().strip())
vectors = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Get the pair of indices with minimal non-oriented angle
result = minimal_angle_pair(n, vectors)

# Print the result
print(result[0], result[1])