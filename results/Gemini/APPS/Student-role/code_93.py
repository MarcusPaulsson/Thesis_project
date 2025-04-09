def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        print("NO")
        return

    if k == 1 and d > 1:
        print("NO")
        return
    
    if k == 1 and d == 1 and n > 2:
        print("NO")
        return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))

    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    next_node = d + 2
    
    # Add nodes to the diameter path
    for i in range(1, d + 2):
        while degrees[i] < k and next_node <= n:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            next_node += 1

    if next_node <= n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()