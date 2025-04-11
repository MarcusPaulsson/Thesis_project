def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    positions = {}
    for i in range(n):
        if a[i] not in positions:
            positions[a[i]] = []
        positions[a[i]].append(i)

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    for x in counts:
        if counts[x] > k:
            print("NO")
            return

    colors = [0] * n
    color_idx = 1
    
    colored_count = 0
    
    for num in sorted(positions.keys()):
        for pos in positions[num]:
            if color_idx <= k:
                colors[pos] = color_idx
                color_idx += 1
                colored_count += 1
            else:
                break
        if color_idx > k:
            break
    
    if colored_count < k:
        print("NO")
        return

    
    color_idx = 1
    for i in range(n):
        if colors[i] == 0:
            colors[i] = color_idx
            color_idx = (color_idx % k) + 1

    print("YES")
    print(*colors)

solve()