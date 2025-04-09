def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    zero_indices = [i for i, x in enumerate(a) if x == 0]
    
    distances = []
    for i in range(n):
        min_dist = float('inf')
        for j in zero_indices:
            dist = abs(i - j)
            min_dist = min(min_dist, dist)
        distances.append(min_dist)
    
    print(*distances)

solve()