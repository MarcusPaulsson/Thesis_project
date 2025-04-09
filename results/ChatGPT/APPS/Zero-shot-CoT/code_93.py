def construct_tree(n, d, k):
    if d >= n or k < 1 or (d > 2 * (k - 1) + 1):
        print("NO")
        return
    
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Keep track of the vertices used
    used_vertices = d + 1
    
    # Now we need to connect the remaining vertices
    for i in range(1, d + 1):
        if used_vertices < n:
            # Add a new vertex as a child of the current vertex
            edges.append((i, used_vertices + 1))
            used_vertices += 1
    
    # If we still have more vertices to add, we must add them
    for i in range(1, d + 1):
        while used_vertices < n and edges.count((i, used_vertices + 1)) < k:
            edges.append((i, used_vertices + 1))
            used_vertices += 1
    
    if used_vertices < n:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)