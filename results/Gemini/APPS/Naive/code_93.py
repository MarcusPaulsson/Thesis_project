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

    if k == 1 and n == 2 and d == 1:
        print("YES")
        print("1 2")
        return

    edges = []
    
    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    remaining_nodes = n - d - 1
    
    if k == 1 and d != 1:
        print("NO")
        return

    
    if d > 1 and k == 1:
        print("NO")
        return
    
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    next_node = d + 2
    
    def add_node(parent):
        nonlocal next_node, remaining_nodes
        if next_node > n:
            return False
        
        if degrees[parent] < k:
            edges.append((parent, next_node))
            degrees[parent] += 1
            degrees[next_node] += 1
            next_node += 1
            remaining_nodes -= 1
            return True
        return False

    
    for i in range(1, d + 2):
        while degrees[i] < k and remaining_nodes > 0:
            if not add_node(i):
                break
    
    if remaining_nodes > 0:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            print(u, v)

solve()