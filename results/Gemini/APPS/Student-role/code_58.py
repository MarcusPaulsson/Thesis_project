def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    if any(count > k for count in counts.values()):
        print("NO")
        return

    colors = [0] * n
    color_map = {}
    color_index = 1

    for i in range(n):
        val = a[i]
        if val not in color_map:
            color_map[val] = []
        color_map[val].append(i)
    
    assignment = {}
    
    for val in color_map:
        indices = color_map[val]
        for index in indices:
            colors[index] = color_index
            color_index = (color_index % k) + 1
            
    
    color_set = set(colors)
    if 0 in color_set:
        print("NO")
        return
    
    if len(set(colors)) < k:
        print("NO")
        return
    
    
    
    color_counts = [0] * (k + 1)
    for color in colors:
        color_counts[color] += 1
        
    if any(count == 0 for count in color_counts[1:]):
        print("NO")
        return
    
    print("YES")
    print(*colors)
    

solve()