def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    distances = [0] * n
    
    for i in range(n):
        min_dist = float('inf')
        for j in range(n):
            if a[j] == 0:
                min_dist = min(min_dist, abs(i - j))
        distances[i] = min_dist
    
    print(*distances)

solve()