def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    if d > n + 1:
        arr = [0] * n
        arr[n - c[0]: ] = [1] * c[0]
        print("YES")
        print(*arr)
        return

    min_empty = m - 1
    if total_length + min_empty > n:
        print("NO")
        return

    arr = [0] * n
    
    current_pos = 0
    platform_positions = []
    
    for i in range(m):
        
        best_start = -1
        
        for j in range(current_pos, n - c[i] + 1):
            
            can_reach = False
            if i == 0:
                if j <= d - 1:
                    can_reach = True
            else:
                if j - (platform_positions[i-1] + c[i-1]) <= d - 1:
                    can_reach = True
            
            if can_reach:
                best_start = j
                break
        
        if best_start == -1:
            print("NO")
            return
        
        platform_positions.append(best_start)
        
        for k in range(best_start, best_start + c[i]):
            arr[k] = i + 1
        
        current_pos = best_start + c[i]
    
    
    last_platform_end = platform_positions[-1] + c[-1]
    
    if n + 1 - last_platform_end > d:
        print("NO")
        return
    
    print("YES")
    print(*arr)

solve()