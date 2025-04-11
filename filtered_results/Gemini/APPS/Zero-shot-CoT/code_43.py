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
        angles.append(angle)

    min_angle_diff = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        for j in range(i + 1, n):
            angle_diff = abs(angles[i] - angles[j])
            angle_diff = min(angle_diff, 2 * math.pi - angle_diff)
            
            if angle_diff < min_angle_diff:
                min_angle_diff = angle_diff
                best_pair = (i + 1, j + 1)

    print(best_pair[0], best_pair[1])

solve()