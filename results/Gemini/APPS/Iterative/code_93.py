def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1:
        if n > 2 and k < 2:
            print("NO")
            return
        if k == 1 and n > 2:
            print("NO")
            return
        if n > k:
            print("NO")
            return
    elif d > n -1 :
        print("NO")
        return
    elif d > 1 and k == 1:
        print("NO")
        return
    
    if d > 1 and n == 2:
        print("NO")
        return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    next_node = d + 2
    
    # Add nodes to the diameter path until we reach n nodes
    for i in range(1, d + 2):
        while degree[i] < k and next_node <= n:
            edges.append((i, next_node))
            degree[i] += 1
            degree[next_node] += 1
            next_node += 1
    
    if next_node <= n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()