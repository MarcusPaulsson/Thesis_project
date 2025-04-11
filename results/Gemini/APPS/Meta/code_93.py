def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k < 2:
            print("NO")
            return
    
    if k == 1 and d > 1:
        print("NO")
        return
    
    if k == 1 and d == 1 and n > 2:
        print("NO")
        return

    edges = []
    nodes_used = 0

    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    nodes_used = d + 1

    if n == 1 and d == 0:
        print("YES")
        return
    
    if n == 1 and d > 0:
        print("NO")
        return

    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Add remaining nodes
    next_node = d + 2
    
    for i in range(1, d + 2):
        while degrees[i] < k and nodes_used < n:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            nodes_used += 1
            next_node += 1

    if nodes_used < n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()