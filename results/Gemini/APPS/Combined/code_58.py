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
    color_idx = 1
    
    assignments = {}

    for i in range(n):
        num = a[i]
        if num not in assignments:
            assignments[num] = []
        
        if len(assignments[num]) < k:
            coloring[i] = color_idx
            assignments[num].append(color_idx)
            color_idx = (color_idx % k) + 1
            if color_idx == 0:
                color_idx = 1

    color_used = [False] * (k + 1)
    for color in coloring:
        color_used[color] = True
    
    all_colors_used = all(color_used[1:])
    
    if not all_colors_used:
        print("NO")
        return

    print("YES")
    print(*coloring)

solve()