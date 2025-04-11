import sys
import math

def main():
    n = int(sys.stdin.readline().strip())
    vectors = []

    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1))

    vectors.sort()

    min_angle = float('inf')
    min_pair = (0, 0)

    for i in range(n):
        angle1, index1 = vectors[i]
        angle2, index2 = vectors[(i + 1) % n]
        angle_diff = abs(angle2 - angle1)
        angle_diff = min(angle_diff, 2 * math.pi - angle_diff)

        if angle_diff < min_angle:
            min_angle = angle_diff
            min_pair = (index1, index2)

    print(min_pair[0], min_pair[1])

if __name__ == "__main__":
    main()