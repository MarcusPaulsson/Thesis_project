def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 2:
        print(p[1], p[0])
    else:
        print(*p[::-1])

t = int(input())
for _ in range(t):
    solve()