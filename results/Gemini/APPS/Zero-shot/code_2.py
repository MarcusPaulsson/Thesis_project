def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    p = [0] * n
    
    p[0] = a[0]
    
    for i in range(1, n):
        if a[i] != p[i-1]:
            p[i] = a[i]
        elif b[i] != p[i-1]:
            p[i] = b[i]
        else:
            p[i] = c[i]
            
    if p[n-1] == p[0]:
        if a[n-1] != p[n-2] and a[n-1] != p[0]:
            p[n-1] = a[n-1]
        elif b[n-1] != p[n-2] and b[n-1] != p[0]:
           p[n-1] = b[n-1]
        else:
            p[n-1] = c[n-1]

    print(*p)

t = int(input())
for _ in range(t):
    solve()