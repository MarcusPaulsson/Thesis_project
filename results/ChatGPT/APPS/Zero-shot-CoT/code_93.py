def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 1) or (d == 0 and n > 1):
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the path
    current_vertex = d + 2
    
    # We can attach additional vertices to the first vertex in the path
    for i in range(1, n - (d + 1) + 1):
        if len(edges) < n - 1:
            edges.append((1, current_vertex))
            current_vertex += 1
    
    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)