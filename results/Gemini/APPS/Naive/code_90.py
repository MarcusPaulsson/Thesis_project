def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    
    total_platform_length = sum(c)
    remaining_space = n - total_platform_length
    
    arr = [0] * n
    
    current_pos = 0
    platform_index = 0
    
    while platform_index < m:
        
        needed_space = min(remaining_space, d - 1)
        
        for i in range(needed_space):
            arr[current_pos] = 0
            current_pos += 1
            remaining_space -= 1
            
        for i in range(c[platform_index]):
            arr[current_pos] = platform_index + 1
            current_pos += 1
            
        platform_index += 1
            
    print("YES")
    print(*arr)

solve()