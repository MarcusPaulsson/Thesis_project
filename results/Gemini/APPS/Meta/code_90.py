def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = n - total_length
    
    arr = [0] * n
    
    current_pos = 0
    for i in range(m):
        
        empty_before = min(min_empty,d-1)
        
        for j in range(empty_before):
          arr[current_pos] = 0
          current_pos +=1
        min_empty -= empty_before
        
        for j in range(c[i]):
            arr[current_pos] = i + 1
            current_pos += 1

    for j in range(n-current_pos):
        arr[current_pos] = 0
        current_pos+=1
    
    
    curr = 0
    possible = False
    
    q = [0]
    visited = [False] * (n+2)
    visited[0] = True
    
    while len(q) > 0:
        u = q.pop(0)
        if u == n+1:
            possible = True
            break
        
        for v in range(u+1, min(u+d+1, n+2)):
            if not visited[v]:
                if v == n+1 or arr[v-1] != 0:
                    q.append(v)
                    visited[v] = True
    
    if possible:
        print("YES")
        print(*arr)
    else:
        print("NO")

solve()