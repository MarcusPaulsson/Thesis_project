def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_length = sum(c)
    
    min_empty = m - 1
    
    if n - total_length < min_empty:
        print("NO")
        return
    
    arr = [0] * n
    
    pos = 0
    for i in range(m):
        
        
        best_start = -1
        for j in range(pos, min(n - c[i] + 1, pos + d)):
            
            best_start = j
            break
        
        if best_start == -1:
            print("NO")
            return
        
        for k in range(c[i]):
            arr[best_start + k] = i + 1
        
        pos = best_start + c[i]
    
    
    if pos + d <= n:
       
        print("YES")
        print(*arr)
    else:
        
        print("YES")
        print(*arr)

solve()