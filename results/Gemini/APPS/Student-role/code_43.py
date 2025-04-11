import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))

    def angle(v):
        return math.atan2(v[1], v[0])

    angles = []
    for i in range(n):
        angles.append((angle(vectors[i]), i + 1))

    angles.sort()

    min_angle = float('inf')
    best_pair = None

    for i in range(n):
        j = (i + 1) % n
        angle_diff = angles[j][0] - angles[i][0]
        if angle_diff < 0:
            angle_diff += 2 * math.pi
        angle_diff = min(angle_diff, 2 * math.pi - angle_diff)
        
        if angle_diff < min_angle:
            min_angle = angle_diff
            best_pair = (angles[i][1], angles[j][1])

    print(best_pair[0], best_pair[1])

solve()