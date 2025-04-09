import sys
import math

def angle_between(v1, v2):
    # Calculate the angle using the cross and dot product
    cross_product = v1[0] * v2[1] - v1[1] * v2[0]
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    return math.atan2(abs(cross_product), dot_product)

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []
    
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        vectors.append((x, y, i + 1))  # Store vector and its index
    
    # Sort vectors by angle
    vectors.sort(key=lambda v: math.atan2(v[1], v[0]))
    
    min_angle = float('inf')
    result = (0, 0)
    
    for i in range(n):
        v1 = vectors[i][:2]
        v2 = vectors[(i + 1) % n][:2]  # next vector, wrap around
        angle = angle_between(v1, v2)
        
        if angle < min_angle:
            min_angle = angle
            result = (vectors[i][2], vectors[(i + 1) % n][2])
    
    print(result[0], result[1])

if __name__ == "__main__":
    main()