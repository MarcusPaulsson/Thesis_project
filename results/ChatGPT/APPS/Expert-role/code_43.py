import sys
import math

def angle_between(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    return math.acos(dot_product / (magnitude_v1 * magnitude_v2))

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1, (x, y)))
    
    vectors.sort()  # Sort by angle

    min_angle = float('inf')
    result = (0, 0)
    
    for i in range(n):
        v1 = vectors[i][2]
        v2 = vectors[(i + 1) % n][2]
        angle = angle_between(v1, v2)
        
        if angle < min_angle:
            min_angle = angle
            result = (vectors[i][1], vectors[(i + 1) % n][1])
    
    print(result[0], result[1])

if __name__ == "__main__":
    main()