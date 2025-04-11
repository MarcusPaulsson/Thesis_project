import sys
import math

def minimal_angle_pair(n, vectors):
    angles = []
    
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))  # Store angle and index (1-based)

    angles.sort()  # Sort by angle

    min_angle = float('inf')
    min_pair = (0, 0)

    for i in range(n):
        a1, idx1 = angles[i]
        a2, idx2 = angles[(i + 1) % n]  # Wrap around to the first element
        angle_diff = abs(a2 - a1)
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (idx1, idx2)

    return min_pair

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    result = minimal_angle_pair(n, vectors)
    print(result[0], result[1])