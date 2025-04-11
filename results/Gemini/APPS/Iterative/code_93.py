def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1:
        if n > 2 and k <= 1:
            print("NO")
            return
        if n == 2 and k < 1:
            print("NO")
            return
        if n == 2 and k == 1:
            print("NO")
            return
    
    if d > 1 and k == 1:
        print("NO")
        return

    if d > n - 1:
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    remaining_nodes = n - d - 1
    
    if remaining_nodes < 0:
        print("NO")
        return

    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    next_node = d + 2
    
    for i in range(1, d + 2):
        if degrees[i] >= k:
            continue
        while remaining_nodes > 0 and degrees[i] < k:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            next_node += 1
            remaining_nodes -= 1

    if remaining_nodes > 0:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()