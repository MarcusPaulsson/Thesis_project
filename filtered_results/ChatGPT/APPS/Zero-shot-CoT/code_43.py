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
    best_pair = (0, 0)

    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[(i + 1) % n]  # Wrap around to the first element
        angle_diff = angle2 - angle1
        
        if angle_diff < 0:
            angle_diff += 2 * math.pi
        
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            best_pair = (index1, index2)

    return best_pair

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    vectors = [tuple(map(int, line.split())) for line in data[1:n + 1]]
    
    result = minimal_angle_pair(n, vectors)
    print(result[0], result[1])