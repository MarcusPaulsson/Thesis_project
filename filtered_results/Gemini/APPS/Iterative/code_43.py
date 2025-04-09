import math

def solve():
    n = int(input())
    vectors = []
    for i in range(n):
        x, y = map(int, input().split())
        vectors.append((x, y, i + 1))
    
    angles_with_indices = []
    for x, y, index in vectors:
        angle = math.atan2(y, x)
        angles_with_indices.append((angle, index))
    
    angles_with_indices.sort()
    
    min_angle_diff = float('inf')
    best_pair = None
    
    for i in range(n):
        angle1, index1 = angles_with_indices[i]
        angle2, index2 = angles_with_indices[(i + 1) % n]
        
        diff = abs(angle1 - angle2)
        diff = min(diff, 2 * math.pi - diff)
        
        if diff < min_angle_diff:
            min_angle_diff = diff
            best_pair = (index1, index2)
    
    print(best_pair[0], best_pair[1])

solve()