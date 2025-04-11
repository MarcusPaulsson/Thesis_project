def solve():
    n = int(input())
    stats = []
    for _ in range(n):
        p, c = map(int, input().split())
        stats.append((p, c))
    
    for i in range(1, n):
        if stats[i][0] < stats[i-1][0] or stats[i][1] < stats[i-1][1]:
            print("NO")
            return
        if stats[i][1] - stats[i-1][1] > stats[i][0] - stats[i-1][0]:
            print("NO")
            return
    
    print("YES")

t = int(input())
for _ in range(t):
    solve()