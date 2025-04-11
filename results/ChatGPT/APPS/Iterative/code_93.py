def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d > 1 and n < d + 1) or (k == 1 and n > 1):
        print("NO")
        return

    print("YES")
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 2):
        edges.append((i, i + 1))
    
    # Now we have a path of length d, which uses d edges and d + 1 vertices
    current_vertex = d + 2
    
    # Attach remaining vertices
    for i in range(1, d + 2):
        while len(edges) < n - 1 and len([e for e in edges if e[0] == i or e[1] == i]) < k:
            if current_vertex > n:
                break
            edges.append((i, current_vertex))
            current_vertex += 1
    
    # If we still have vertices left to connect
    while current_vertex <= n:
        for i in range(1, d + 2):
            if len(edges) >= n - 1:
                break
            if len([e for e in edges if e[0] == i or e[1] == i]) < k:
                edges.append((i, current_vertex))
                current_vertex += 1
        if current_vertex > n:
            break
    
    if len(edges) == n - 1:
        for u, v in edges:
            print(u, v)
    else:
        print("NO")

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)