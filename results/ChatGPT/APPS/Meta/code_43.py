import sys
import math

def minimal_angle_pair(n, vectors):
    angles = []
    
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and index (1-based)
    
    # Sort angles
    angles.sort()
    
    min_angle = float('inf')
    min_pair = (0, 0)
    
    # Check adjacent angles in the sorted list
    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[(i + 1) % n]  # Wrap around for circular comparison
        
        # Calculate the non-oriented angle
        angle_diff = abs(angle2 - angle1)
        angle_diff = min(angle_diff, 2 * math.pi - angle_diff)  # Non-oriented angle
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (index1, index2)
    
    return min_pair

# Read input
n = int(sys.stdin.readline().strip())
vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Get the result
result = minimal_angle_pair(n, vectors)

# Print the result
print(result[0], result[1])