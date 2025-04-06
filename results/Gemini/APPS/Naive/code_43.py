import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    min_angle = float('inf')
    best_pair = (0, 0)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = vectors[i]
            x2, y2 = vectors[j]

            dot_product = x1 * x2 + y1 * y2
            magnitude1 = math.sqrt(x1**2 + y1**2)
            magnitude2 = math.sqrt(x2**2 + y2**2)

            angle = math.acos(dot_product / (magnitude1 * magnitude2))

            if angle < min_angle:
                min_angle = angle
                best_pair = (i + 1, j + 1)

    print(best_pair[0], best_pair[1])

solve()