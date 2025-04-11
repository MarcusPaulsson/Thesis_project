def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (d == 0 and n > 1):
        print("NO")
        return

    print("YES")
    edges = []
    
    # Create a path of length d
    for i in range(1, d + 2):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the path
    current_vertex = d + 2
    
    # Connect remaining vertices
    for i in range(1, d + 2):
        if current_vertex > n:
            break
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
    
    # If we still have vertices left, we can connect them to any of the existing vertices
    while current_vertex <= n:
        edges.append((1, current_vertex))
        current_vertex += 1
    
    # Output the edges
    for u, v in edges:
        print(u, v)

n, d, k = map(int, input().split())
construct_tree(n, d, k)