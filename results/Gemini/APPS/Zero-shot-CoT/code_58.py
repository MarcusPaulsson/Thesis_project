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
    
    for val in indices:
        for idx in indices[val]:
            colors[idx] = color_idx
            color_idx = (color_idx % k) + 1
            
    print("YES")
    print(*colors)

solve()