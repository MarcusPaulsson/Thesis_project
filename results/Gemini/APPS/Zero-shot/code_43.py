import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    def angle(v):
        x, y = v
        return math.atan2(y, x)

    angles = []
    for i in range(n):
        angles.append((angle(vectors[i]), i + 1))

    angles.sort()

    min_angle = float('inf')
    best_pair = None

    for i in range(n - 1):
        diff = angles[i+1][0] - angles[i][0]
        if diff < min_angle:
            min_angle = diff
            best_pair = (angles[i][1], angles[i+1][1])

    diff = angles[0][0] + (2 * math.pi - angles[-1][0])
    if diff < min_angle:
        min_angle = diff
        best_pair = (angles[0][1], angles[-1][1])

    print(best_pair[0], best_pair[1])

solve()