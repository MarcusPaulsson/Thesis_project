def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = m - 1

    if n + 1 - (total_length + min_empty + 1) > d:
        print("NO")
        return
    
    print("YES")
    a = [0] * n
    
    current_pos = 0
    for i in range(m):
        
        
        needed_empty = 0
        if i == m-1:
            needed_empty = n - current_pos - c[i]
        else:
            needed_empty = min(d-1, n - (current_pos + sum(c[i:]) + (m-i-1)))
        
        
        current_pos += needed_empty
        
        for j in range(c[i]):
            a[current_pos] = i + 1
            current_pos += 1

    print(*a)

solve()