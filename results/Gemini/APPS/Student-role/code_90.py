def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    min_empty = m - 1
    max_empty = n - total_length
    
    if d * (m + 1) <= n + 1:
        print("NO")
        return

    arr = [0] * n
    
    current_pos = 0
    
    for i in range(m):
        
        needed_space = min(d - 1, n - current_pos - sum(c[i:]))
        
        current_pos += needed_space
        
        for j in range(c[i]):
            arr[current_pos] = i + 1
            current_pos += 1
            
    print("YES")
    print(*arr)

solve()