import sys
import math

def angle_between(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cos_angle = dot_product / (magnitude_v1 * magnitude_v2)
    return math.acos(cos_angle)

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1))

    vectors.sort()

    min_angle = float('inf')
    idx_pair = (0, 0)

    for i in range(n):
        v1 = vectors[i]
        v2 = vectors[(i + 1) % n]
        current_angle = angle_between((math.cos(v1[0]), math.sin(v1[0])), (math.cos(v2[0]), math.sin(v2[0])))

        if current_angle < min_angle:
            min_angle = current_angle
            idx_pair = (v1[1], v2[1])

    print(idx_pair[0], idx_pair[1])

if __name__ == "__main__":
    main()