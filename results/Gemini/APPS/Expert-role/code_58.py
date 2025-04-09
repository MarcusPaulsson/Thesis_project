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

    positions = {}
    for i in range(n):
        if a[i] not in positions:
            positions[a[i]] = []
        positions[a[i]].append(i)

    colors = [0] * n
    color_idx = 1
    
    colored_count = 0
    
    sorted_indices = sorted(range(n), key=lambda i: a[i])
    
    for i in sorted_indices:
        if color_idx > k:
            break
        colors[i] = color_idx
        color_idx += 1
        colored_count += 1
        
    if colored_count < k:
        print("NO")
        return

    
    remaining_indices = []
    for i in range(n):
        if colors[i] == 0:
            remaining_indices.append(i)
            
    current_color = 1
    for i in remaining_indices:
        colors[i] = current_color
        current_color = (current_color % k) + 1
    

    print("YES")
    print(*colors)

solve()