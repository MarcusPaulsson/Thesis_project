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
    
    min_diff = float('inf')
    best_pair = (0, 0)
    
    for i in range(n):
        j = (i + 1) % n
        diff = angles[j][0] - angles[i][0]
        if diff < 0:
            diff += 2 * math.pi
        
        diff = min(diff, 2 * math.pi - diff)
        
        if diff < min_diff:
            min_diff = diff
            best_pair = (angles[i][1], angles[j][1])
            
    print(best_pair[0], best_pair[1])

solve()