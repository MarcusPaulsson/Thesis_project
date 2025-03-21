def solve():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    
    for k in range(1, 1025):
        new_s = sorted([x ^ k for x in s])
        if new_s == s:
            print(k)
            return
    
    print(-1)

t = int(input())
for _ in range(t):
    solve()