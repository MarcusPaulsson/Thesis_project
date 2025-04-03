def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k < 2:
            print("NO")
            return

    if d > 1 and k == 1:
        print("NO")
        return

    if d > 1 and n > d + 1 and k == 2:
        print("NO")
        return

    edges = []
    nodes = list(range(1, n + 1))

    # Create the main path of length d
    for i in range(d):
        edges.append((nodes[i], nodes[i+1]))

    # Add remaining nodes to the path
    curr_node_idx = 0
    node_idx = d + 1
    
    degrees = [0] * n
    
    for i in range(d):
        degrees[i] += 1
    degrees[d] += 1

    while node_idx < n:
        
        added = False
        for i in range(d+1):
            if degrees[i] < k:
                edges.append((nodes[i], nodes[node_idx]))
                degrees[i] += 1
                degrees[node_idx] = 1
                node_idx += 1
                added = True
                break
        if not added:
            print("NO")
            return
                
    print("YES")
    for u, v in edges:
        print(u, v)

solve()