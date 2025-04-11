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

    colors = [0] * n
    color_map = {}
    color_idx = 1
    
    indices = list(range(n))
    indices.sort(key=lambda i: a[i])

    for i in indices:
        val = a[i]
        if val not in color_map:
            color_map[val] = []
        
        if len(color_map[val]) < k:
            colors[i] = color_idx
            color_map[val].append(color_idx)
            color_idx = (color_idx % k) + 1
        else:
            colors[i] = 0

    
    color_counts = [0] * (k + 1)
    for color in colors:
        if 1 <= color <= k:
            color_counts[color] += 1

    
    for i in range(1, k + 1):
        if color_counts[i] == 0:
            
            uncolored_indices = [idx for idx in range(n) if colors[idx] == 0]
            if not uncolored_indices:
                print("NO")
                return
            
            colors[uncolored_indices[0]] = i
            
            color_counts = [0] * (k + 1)
            for color in colors:
                if 1 <= color <= k:
                    color_counts[color] += 1
            
            all_colored = True
            for j in range(1, k + 1):
                if color_counts[j] == 0:
                    all_colored = False
                    break
            
            if not all_colored:
                print("NO")
                return
            
            break
    
    color_counts = [0] * (k + 1)
    for color in colors:
        if 1 <= color <= k:
            color_counts[color] += 1
    
    all_colored = True
    for i in range(1, k + 1):
        if color_counts[i] == 0:
            all_colored = False
            break
    
    if not all_colored:
        print("NO")
        return

    print("YES")
    print(*colors)

solve()