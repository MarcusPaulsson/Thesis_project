import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    angles = []
    for i in range(n):
        angles.append((math.atan2(vectors[i][1], vectors[i][0]), i + 1))

    angles.sort()

    min_diff = float('inf')
    best_pair = None

    for i in range(n):
        j = (i + 1) % n
        diff = abs(angles[j][0] - angles[i][0])
        diff = min(diff, 2 * math.pi - diff)

        if diff < min_diff:
            min_diff = diff
            best_pair = (angles[i][1], angles[j][1])

    print(best_pair[0], best_pair[1])

solve()