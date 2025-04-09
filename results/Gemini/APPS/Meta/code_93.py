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
    
    if k == 1 and n > 2:
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    used = d + 1
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Add remaining nodes to the path
    for i in range(1, d + 2):
        while degrees[i] < k and used <= n:
            edges.append((i, used))
            degrees[i] += 1
            degrees[used] += 1
            used += 1

    if used <= n:
        print("NO")
        return
    
    if len(edges) != n - 1:
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        print(u, v)

solve()