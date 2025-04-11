def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        print("NO")
        return
    
    if k == 1 and n > 2:
        print("NO")
        return

    if k == 1 and d > 1:
        print("NO")
        return
    
    if k == 1 and d == 1 and n == 2:
        print("YES")
        print("1 2")
        return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))

    if len(edges) > n - 1:
        print("NO")
        return

    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    next_node = d + 2
    
    q = list(range(1, d + 2))
    
    while q and next_node <= n:
        u = q.pop(0)
        
        while degrees[u] < k and next_node <= n:
            edges.append((u, next_node))
            degrees[u] += 1
            degrees[next_node] += 1
            q.append(next_node)
            next_node += 1

    if any(degree > k for degree in degrees[1:]):
        print("NO")
        return

    if len(edges) != n - 1:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()