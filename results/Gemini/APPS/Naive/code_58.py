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

    coloring = [0] * n
    color_assignments = {}
    color_index = 1

    for i in range(n):
        if a[i] not in color_assignments:
            color_assignments[a[i]] = []
        
        if len(color_assignments[a[i]]) < k:
            coloring[i] = color_index
            color_assignments[a[i]].append(color_index)
            color_index = (color_index % k) + 1
        else:
            coloring[i] = -1

    color_counts = [0] * (k + 1)
    for c in coloring:
        if c != -1:
            color_counts[c] += 1

    missing_colors = []
    for i in range(1, k + 1):
        if color_counts[i] == 0:
            missing_colors.append(i)

    if missing_colors:
        missing_index = 0
        for i in range(n):
            if coloring[i] == -1:
                coloring[i] = missing_colors[missing_index]
                missing_index = (missing_index + 1) % len(missing_colors)
                
    print("YES")
    print(*coloring)
solve()