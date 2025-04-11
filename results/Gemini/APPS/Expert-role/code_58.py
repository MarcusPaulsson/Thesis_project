def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    possible = True
    for x in counts:
        if counts[x] > k:
            possible = False
            break

    if not possible:
        print("NO")
        return

    print("YES")

    colors = [0] * n
    color_map = {}
    color_idx = 1

    for i in range(n):
        num = a[i]
        if num not in color_map:
            color_map[num] = []
        
        if len(color_map[num]) < k:
            color_map[num].append(i)
        

    assigned = 0
    color_assignment = {}
    
    for num in color_map:
        indices = color_map[num]
        for idx in indices:
            colors[idx] = (assigned % k) + 1
            assigned += 1

    print(*colors)

solve()