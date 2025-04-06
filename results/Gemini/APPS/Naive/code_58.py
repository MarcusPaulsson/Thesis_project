def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    for x in counts:
        if counts[x] > k:
            print("NO")
            return

    print("YES")
    colors = [0] * n
    color_map = {}
    color_index = 1
    
    for i in range(n):
        if a[i] not in color_map:
            color_map[a[i]] = []
        color_map[a[i]].append(i)
        
    
    assigned_count = 0
    
    for num in color_map:
        indices = color_map[num]
        for index in indices:
            colors[index] = color_index
            color_index = (color_index % k) + 1
            assigned_count += 1
            

    print(*colors)

solve()