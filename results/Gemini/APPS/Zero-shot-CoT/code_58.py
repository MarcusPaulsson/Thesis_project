def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    positions = {}
    for i in range(n):
        if a[i] not in positions:
            positions[a[i]] = []
        positions[a[i]].append(i)
    
    count = 0
    for key in positions:
        count += len(positions[key])
        if len(positions[key]) > k:
            print("NO")
            return
    
    
    coloring = [0] * n
    color = 1
    assigned = 0
    
    sorted_positions = sorted([(a[i], i) for i in range(n)])
    
    
    possible = True
    
    
    
    for val, idx in sorted_positions:
        coloring[idx] = color
        color = (color % k) + 1
        assigned += 1
    
    
    
    
    counts = [0] * (k + 1)
    for c in coloring:
        counts[c] += 1
    
    for i in range(1, k+1):
      if counts[i] == 0:
        possible = False
        break
    
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*coloring)


solve()