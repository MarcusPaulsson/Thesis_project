def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    if d * (m + 1) <= n + 1:
        print("NO")
        return

    a = [0] * n
    
    current_pos = 0
    
    for i in range(m):
        
        needed_empty = min(d - 1, n - current_pos - total_length + sum(c[i:]))
        
        start_pos = current_pos + needed_empty
        
        for j in range(c[i]):
            a[start_pos + j] = i + 1
            
        current_pos = start_pos + c[i]
            
    print("YES")
    print(*a)

solve()