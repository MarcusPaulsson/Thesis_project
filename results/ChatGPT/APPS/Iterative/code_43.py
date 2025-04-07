import math
import sys

def angle_between(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magnitude_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
    return math.acos(max(-1.0, min(1.0, cos_angle)))  # Clamping to avoid domain errors

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)  # Get the angle of the vector
        vectors.append((angle, i + 1, (x, y)))  # Store angle, index, and vector

    # Sort by angle
    vectors.sort()

    min_angle = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        v1 = vectors[i][2]
        v2 = vectors[(i + 1) % n][2]  # Wrap around to compare with the first vector
        
        current_angle = angle_between(v1, v2)
        
        if current_angle < min_angle:
            min_angle = current_angle
            best_pair = (vectors[i][1], vectors[(i + 1) % n][1])

    print(best_pair[0], best_pair[1])

if __name__ == "__main__":
    main()