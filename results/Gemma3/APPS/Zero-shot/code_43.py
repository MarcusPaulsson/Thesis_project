import math

def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def magnitude(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def angle(v1, v2):
    dot = dot_product(v1, v2)
    mag1 = magnitude(v1)
    mag2 = magnitude(v2)
    return math.acos(dot / (mag1 * mag2))

def solve():
    n = int(input())
    vectors = []
    for _ in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))
    
    min_angle = float('inf')
    best_pair = (0, 0)
    
    for i in range(n):
        for j in range(i + 1, n):
            ang = angle(vectors[i], vectors[j])
            if ang < min_angle:
                min_angle = ang
                best_pair = (i + 1, j + 1)
    
    print(best_pair[0], best_pair[1])

solve()