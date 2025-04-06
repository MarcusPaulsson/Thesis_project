def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    distances = []
    for i in range(n):
        min_dist = float('inf')
        for j in range(n):
            if a[j] == 0:
                min_dist = min(min_dist, abs(i - j))
        distances.append(min_dist)
    
    print(*distances)

solve()