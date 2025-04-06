def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    min_empty = m - 1
    max_empty = n - total_length
    
    if max_empty + min_empty >= d - 1:
        
        arr = [0] * n
        
        current_pos = 0
        
        for i in range(m):
            
            needed_empty = min(d - 1, n - total_length)
            
            for j in range(needed_empty):
                arr[current_pos] = 0
                current_pos += 1
                
            for j in range(c[i]):
                arr[current_pos] = i + 1
                current_pos += 1
            
            n -= needed_empty
            
            n -= c[i]
            
            d -= needed_empty
        
        
        
        for i in range(len(arr) -1, -1, -1):
            if arr[i] == 0 and n > 0:
                n -= 1
            else:
                break
        
        print("YES")
        print(*arr)
    else:
        print("NO")
    
solve()