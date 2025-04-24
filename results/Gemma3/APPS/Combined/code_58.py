def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k > n:
        print("NO")
        return
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    if any(count > k for count in counts.values()):
        print("NO")
        return
    
    coloring = [0] * n
    color_index = 1
    
    for i in range(n):
        coloring[i] = color_index
        color_index = (color_index % k) + 1
        
    
    color_used = [False] * (k + 1)
    for color in coloring:
        color_used[color] = True
    
    if not all(color_used[1:k+1]):
        print("NO")
        return
    
    print("YES")
    print(*coloring)

solve()