import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    angles = []
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))

    angles.sort()

    min_angle_diff = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        angle1, index1 = angles[i]
        angle2, index2 = angles[(i + 1) % n]
        
        diff = abs(angle1 - angle2)
        diff = min(diff, 2 * math.pi - diff)

        if diff < min_angle_diff:
            min_angle_diff = diff
            best_pair = (index1, index2)

    print(best_pair[0], best_pair[1])

solve()