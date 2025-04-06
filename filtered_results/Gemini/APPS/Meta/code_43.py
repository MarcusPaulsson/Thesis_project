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

    for i in range(n):
        j = (i + 1) % n
        angle1 = angles[i][0]
        angle2 = angles[j][0]
        
        diff = angle2 - angle1
        if diff < 0:
            diff += 2 * math.pi

        non_oriented_angle = min(diff, 2 * math.pi - diff)
        
        if non_oriented_angle < min_angle:
            min_angle = non_oriented_angle
            best_pair = (angles[i][1], angles[j][1])

    print(best_pair[0], best_pair[1])

solve()