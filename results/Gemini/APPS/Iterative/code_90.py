def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_length = sum(c)
    arr = [0] * n
    
    pos = 0
    remaining = n
    
    for i in range(m):
        needed = min(remaining - total_length, d - 1)
        pos += needed
        remaining -= needed
        
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1
        remaining -= c[i]
        total_length -= c[i]
        
    if remaining < 0:
        print("NO")
        return

    if total_length > 0:
        print("NO")
        return
    
    
    
    
    reachable = False
    
    def check_reachable(arrangement):
        
        curr_pos = 0
        
        
        while curr_pos < n:
            
            next_pos = -1
            for i in range(curr_pos + 1, min(curr_pos + d + 1, n + 1)):
                if i == n:
                    
                    return True
                
                if arrangement[i-1] != 0:
                    next_pos = i
                    
            if next_pos == -1:
                return False
            
            curr_pos = next_pos
        
        return True

    if check_reachable(arr):
        print("YES")
        print(*arr)
    else:
        print("NO")

solve()