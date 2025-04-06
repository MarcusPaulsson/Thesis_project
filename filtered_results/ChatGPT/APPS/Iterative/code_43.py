import math
import sys

def angle_between(v1, v2):
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    det = v1[0] * v2[1] - v1[1] * v2[0]
    return math.atan2(det, dot)

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1))

    # Sort by angle
    vectors.sort()

    # To find the minimal angle, we also need to consider the wrap-around case
    min_angle = float('inf')
    pair_indices = (0, 0)

    for i in range(n):
        v1 = vectors[i]
        v2 = vectors[(i + 1) % n]  # Wrap around to compare with the first vector
        angle_diff = abs(v1[0] - v2[0])
        
        # Ensure we take the non-oriented angle
        if angle_diff > math.pi:
            angle_diff = 2 * math.pi - angle_diff
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            pair_indices = (v1[1], v2[1])

    print(pair_indices[0], pair_indices[1])

if __name__ == "__main__":
    main()