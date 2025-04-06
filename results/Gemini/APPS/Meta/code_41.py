def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    distances = [0] * n
    
    for i in range(n):
        min_dist = float('inf')
        for j in range(n):
            if a[j] == 0:
                dist = abs(i - j)
                min_dist = min(min_dist, dist)
        distances[i] = min_dist
    
    print(*distances)

solve()