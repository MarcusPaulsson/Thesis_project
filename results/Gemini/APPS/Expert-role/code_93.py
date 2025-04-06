def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k <= 1:
            print("NO")
            return
    
    if k == 1 and d > 1:
        print("NO")
        return
    
    if n == 1 and d > 0:
        print("NO")
        return
        
    if n == 1 and d == 0:
        print("YES")
        return
    
    if n == 2 and d > 1:
        print("NO")
        return
    
    if n == 2 and d == 1 and k < 1:
        print("NO")
        return

    edges = []
    
    # Create the path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))

    if k < 2 and d > 1:
        print("NO")
        return

    if k < 1 and d == 1 and n > 1:
        print("NO")
        return

    remaining_nodes = n - d - 1
    
    if remaining_nodes < 0:
      print("NO")
      return

    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    if any(deg > k for deg in degree[1:]):
        print("NO")
        return

    curr_node = d + 2

    q = list(range(1, d + 2))

    while remaining_nodes > 0 and q:
        u = q.pop(0)
        
        if degree[u] < k:
            edges.append((u, curr_node))
            degree[u] += 1
            degree[curr_node] += 1
            q.append(curr_node)
            curr_node += 1
            remaining_nodes -= 1
        
        if any(deg > k for deg in degree[1:]):
            print("NO")
            return

    if remaining_nodes > 0:
        print("NO")
        return
    
    if any(deg > k for deg in degree[1:]):
        print("NO")
        return

    if len(edges) != n - 1:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()