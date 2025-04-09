def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    zeros = [i for i, x in enumerate(a) if x == 0]
    
    distances = []
    for i in range(n):
        min_dist = float('inf')
        for j in zeros:
            dist = abs(i - j)
            min_dist = min(min_dist, dist)
        distances.append(min_dist)
    
    print(*distances)

solve()