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

    # To handle the circular nature of angles, we can duplicate the list with adjusted angles
    extended_angles = angles + [(angle + 2 * math.pi, idx) for angle, idx in angles]

    min_angle = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        angle1, idx1 = extended_angles[i]
        angle2, idx2 = extended_angles[i + 1]
        angle_diff = angle2 - angle1
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            best_pair = (idx1, idx2)

    return best_pair

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    a, b = minimal_angle_pair(n, vectors)
    print(a, b)