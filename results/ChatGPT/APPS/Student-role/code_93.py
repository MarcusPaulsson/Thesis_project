def construct_tree(n, d, k):
    # Check impossible conditions
    if d > 2 * (k - 1) + 1:
        return "NO"
    
    # Check if k is too low to create any valid tree with the required diameter
    if k == 1 and n > 1:
        return "NO"
    
    # Build the tree
    edges = []
    
    # Create a base path for the diameter
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    # Now we need to connect the remaining vertices
    current_vertex = d + 2
    
    # List of available vertices to connect to the main path
    available_vertices = list(range(1, d + 2))
    
    for vertex in available_vertices:
        # Connect up to k-1 new vertices to this vertex
        for _ in range(k - 1):
            if current_vertex <= n:
                edges.append((vertex, current_vertex))
                current_vertex += 1
            else:
                break

    # Check if we used all vertices
    if current_vertex - 1 < n:
        return "NO"
    
    # If we have a valid configuration, return the edges
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
output = construct_tree(n, d, k)
print(output)