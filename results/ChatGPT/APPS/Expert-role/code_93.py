def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (d == 0 and n > 1):
        print("NO")
        return

    print("YES")
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d edges, which means we have d + 1 vertices in the main path
    current_vertex = d + 2
    
    # We will attach the remaining vertices to the first vertex of the path
    for i in range(1, n - (d + 1) + 1):
        if i <= k - 1:
            edges.append((1, current_vertex))
            current_vertex += 1
        else:
            # If we exceed the degree limit, we need to attach to the next available vertex
            edges.append((2, current_vertex))
            current_vertex += 1

    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)