def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_platform_length = sum(c)
    min_empty_space = m - 1
    
    if n + 1 - (total_platform_length + min_empty_space + 1) > (d - 1) * (m + 1):
        print("NO")
        return
    
    arr = [0] * n
    
    pos = 0
    for i in range(m):
        
        needed_jump = 0
        if i == 0:
          needed_jump = 1
        else:
          needed_jump = 1

        while pos < n and (n + 1 - pos - c[i]) > (d - 1) * (m - i):
            pos += 1
            
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1
    
    print("YES")
    print(*arr)

solve()