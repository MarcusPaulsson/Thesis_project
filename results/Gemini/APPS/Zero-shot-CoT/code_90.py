def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_length = sum(c)
    empty_space = n - total_length
    
    a = [0] * n
    
    pos = 0
    start = 0
    for i in range(m):
        
        needed_space = min(empty_space, d - 1)
        
        start += needed_space
        empty_space -= needed_space
        
        for j in range(c[i]):
            a[start + j] = i + 1
        
        start += c[i]
    
    
    
    
    
    reachable = [False] * (n + 2)
    reachable[0] = True
    
    
    
    for i in range(n + 1):
        if reachable[i]:
            for j in range(i + 1, min(i + d + 1, n + 2)):
                if j == n + 1 or (j <= n and a[j-1] != 0):
                    reachable[j] = True
    
    if reachable[n+1]:
        print("YES")
        print(*a)
    else:
        print("NO")
solve()