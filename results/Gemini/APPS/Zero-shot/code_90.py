def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = n - total_length

    arr = [0] * n
    
    pos = 0
    for i in range(m):
        empty_before = min(min_empty, d - 1)
        
        pos += empty_before
        min_empty -= empty_before
        
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1
            
    if pos + d <= n + 1 :
        
        curr_pos = 0
        can_reach = True
        
        while curr_pos < n + 1:
          
            next_pos = -1
            
            for k in range(min(d, n + 1 - curr_pos)):
                if curr_pos + k + 1 == n + 1:
                    next_pos = curr_pos + k + 1
                    break
                
                if curr_pos + k + 1 <= n and arr[curr_pos + k ] != 0 :
                    next_pos = curr_pos + k + 1

            if next_pos == -1:
                can_reach = False
                break

            curr_pos = next_pos
        
        if can_reach:
            print("YES")
            print(*arr)
            return
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    print("NO")

solve()