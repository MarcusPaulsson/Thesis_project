def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_platform_length = sum(c)
    min_empty_space = n - total_platform_length

    arr = [0] * n
    current_pos = 0
    
    for i in range(m):
        
        empty_space = min(d - 1, min_empty_space)
        
        start_pos = current_pos + empty_space
        
        for j in range(c[i]):
            if start_pos + j < n:
                arr[start_pos + j] = i + 1
        
        current_pos = start_pos + c[i]
        min_empty_space -= empty_space
        
    
    reachable = False
    
    q = [0]
    visited = {0}
    
    while q:
        curr = q.pop(0)
        
        if curr == n + 1:
            reachable = True
            break
        
        for next_node in range(curr + 1, min(curr + d + 1, n + 2)):
            
            if next_node == n + 1:
                q.append(next_node)
                
            elif 1 <= next_node <= n and arr[next_node - 1] != 0 and next_node not in visited:
                q.append(next_node)
                visited.add(next_node)
    
    if reachable:
        print("YES")
        print(*arr)
    else:
        print("NO")

solve()