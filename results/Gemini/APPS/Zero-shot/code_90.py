def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = m - 1
    max_empty = n - total_length
    
    if d * (m + 1) <= n + 1:
        if d == 1:
            if sum(c) < n:
                print("NO")
                return
        
    
    
    arr = [0] * n
    
    pos = 0
    for i in range(m):
        
        needed_space = min(d-1, n - pos - sum(c[i:]))
        
        pos += needed_space
        
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1

    print("YES")
    print(*arr)

solve()