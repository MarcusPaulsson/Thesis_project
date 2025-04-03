import math
import sys

def angle_between(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
    return math.acos(dot_product / (magnitude_v1 * magnitude_v2))

def main():
    n = int(sys.stdin.readline().strip())
    vectors = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    angles = []
    
    for i in range(n):
        angle = math.atan2(vectors[i][1], vectors[i][0])
        angles.append((angle, i + 1))  # Store angle and its index

    angles.sort()  # Sort by angle

    min_angle = float('inf')
    pair = (0, 0)

    # Compare each angle with the next one in the sorted list
    for i in range(n):
        v1 = angles[i]
        v2 = angles[(i + 1) % n]  # Wrap around to compare with the first one
        current_angle = angle_between(vectors[v1[1] - 1], vectors[v2[1] - 1])
        
        if current_angle < min_angle:
            min_angle = current_angle
            pair = (v1[1], v2[1])

    print(pair[0], pair[1])

if __name__ == "__main__":
    main()