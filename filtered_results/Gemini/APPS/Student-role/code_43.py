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

    min_angle = float('inf')
    best_pair = (-1, -1)
    
    for i in range(n):
        for j in range(i + 1, n):
            angle1 = angles[i]
            angle2 = angles[j]
            
            diff = abs(angle1 - angle2)
            angle = min(diff, 2 * math.pi - diff)
            
            if angle < min_angle:
                min_angle = angle
                best_pair = (i + 1, j + 1)

    print(best_pair[0], best_pair[1])

solve()