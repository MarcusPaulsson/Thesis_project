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

    indices = {}
    for i in range(n):
        if a[i] not in indices:
            indices[a[i]] = []
        indices[a[i]].append(i)

    colors = [0] * n
    color_idx = 1
    
    assignments = []
    for val in sorted(indices.keys()):
        for idx in indices[val]:
            assignments.append((idx, val))
    
    assignments.sort()

    count = 0
    for idx, val in assignments:
        colors[idx] = color_idx
        color_idx = (color_idx % k) + 1
        count += 1
        
    if len(set(colors)) < k:
        print("NO")
        return

    print("YES")
    print(*colors)

solve()