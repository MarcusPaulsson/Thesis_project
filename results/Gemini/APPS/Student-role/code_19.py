def solve():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))

    ans = float('inf')
    for i in range(n - d + 1):
        sub_array = a[i:i+d]
        
        unique_shows = len(set(sub_array))
        ans = min(ans, unique_shows)
    
    print(ans)


t = int(input())
for _ in range(t):
    solve()