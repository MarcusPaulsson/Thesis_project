def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_length = sum(c)
    
    if d > n + 1:
        arr = [0] * n
        pos = n - c[0]
        for i in range(c[0]):
            arr[pos + i] = 1
        print("YES")
        print(*arr)
        return

    min_space = (m - 1) * (d - 1) + m
    if total_length + (m - 1) * (d - 1) > n:
        print("NO")
        return
    
    arr = [0] * n
    
    curr_pos = 0
    start_pos = 0
    
    for i in range(m):
        
        needed_space = n - (total_length - sum(c[:i]) + (m-1 - i) * (d-1))
        start_pos = n- needed_space
        
        
        for j in range(c[i]):
            arr[start_pos + j] = i + 1
            
        n = start_pos
        

    print("YES")
    print(*arr)
solve()