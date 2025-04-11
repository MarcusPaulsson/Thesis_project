def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k < 2:
            print("NO")
            return
        if n > k:
            print("NO")
            return
    
    if d > 1 and k == 1:
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    available_nodes = list(range(1, n + 1))
    
    q = list(range(1, d + 2))
    
    idx = 0
    while idx < len(q):
        u = q[idx]
        idx += 1
        
        for v in range(1, n + 1):
            if len(edges) == n - 1:
                break
            if v not in available_nodes:
                continue
            if v in q:
                continue
            if degrees[u] < k:
                edges.append((u, v))
                degrees[u] += 1
                degrees[v] += 1
                q.append(v)
                available_nodes.remove(v)
    
    if len(edges) == n - 1:
        print("YES")
        for u, v in edges:
            print(u, v)
    else:
        print("NO")

solve()