def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_spaces = m - 1
    max_spaces = (m + 1) * (d - 1)

    remaining_space = n - total_length
    
    if remaining_space > max_spaces:
        print("NO")
        return

    arr = [0] * n
    
    curr_pos = 0
    
    for i in range(m):
        
        
        space_needed = min(remaining_space, d - 1)
        
        
        for j in range(space_needed):
            arr[curr_pos] = 0
            curr_pos += 1
        remaining_space -= space_needed

        for j in range(c[i]):
            arr[curr_pos] = i + 1
            curr_pos += 1

    
    for i in range(remaining_space):
        arr[curr_pos] = 0
        curr_pos += 1

    
    print("YES")
    print(*arr)

solve()