import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y, i + 1))

    angles = []
    for x, y, index in vectors:
        angle = math.atan2(y, x)
        angles.append((angle, index))

    angles.sort()

    min_angle_diff = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        j = (i + 1) % n
        angle_diff = abs(angles[i][0] - angles[j][0])
        angle_diff = min(angle_diff, 2 * math.pi - angle_diff)

        if angle_diff < min_angle_diff:
            min_angle_diff = angle_diff
            best_pair = (angles[i][1], angles[j][1])

    print(best_pair[0], best_pair[1])

solve()