def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    
    if d > n + 1:
        print("YES")
        result = [0] * n
        last_index = n - c[0]
        for i in range(c[0]):
            result[last_index + i] = 1
        print(*result)
        return

    min_empty = (m + 1) * (d - 1)
    if total_length + min_empty > n:
        print("NO")
        return

    print("YES")
    result = [0] * n
    
    current_pos = 0
    platform_positions = []
    
    for i in range(m):
        
        needed_space = d - 1 if i == 0 else d - 1
        
        while current_pos + c[i] <= n and current_pos < needed_space:
            current_pos += 1
        
        platform_positions.append(current_pos)
        
        for j in range(c[i]):
            result[current_pos + j] = i + 1
        
        current_pos += c[i]
    
    print(*result)

solve()