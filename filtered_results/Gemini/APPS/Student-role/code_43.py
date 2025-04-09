import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y))
    
    angles = []
    for x, y in vectors:
        angle = math.atan2(y, x)
        angles.append(angle)
    
    min_angle_diff = float('inf')
    best_pair = (-1, -1)
    
    for i in range(n):
        for j in range(i + 1, n):
            angle1 = angles[i]
            angle2 = angles[j]
            
            diff = abs(angle1 - angle2)
            diff = min(diff, 2 * math.pi - diff)
            
            if diff < min_angle_diff:
                min_angle_diff = diff
                best_pair = (i + 1, j + 1)
    
    print(best_pair[0], best_pair[1])

solve()