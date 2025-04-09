def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or d > n - 1:
        return "NO"
    
    edges = []
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d edges, and we need to connect the remaining vertices
    # We have n - (d + 1) vertices left to connect
    remaining_vertices = n - (d + 1)
    
    # If we have remaining vertices, we can attach them to the last vertex in the path
    if remaining_vertices > 0:
        last_vertex = d + 1
        for i in range(remaining_vertices):
            if len(edges) < n - 1 and edges.count((last_vertex, last_vertex + 1)) < k:
                edges.append((last_vertex, last_vertex + 1))
                last_vertex += 1
    
    # Check if we exceeded the degree
    degree_count = {}
    for u, v in edges:
        if u in degree_count:
            degree_count[u] += 1
        else:
            degree_count[u] = 1
        if v in degree_count:
            degree_count[v] += 1
        else:
            degree_count[v] = 1
        
    for count in degree_count.values():
        if count > k:
            return "NO"
    
    result = ["YES"]
    for u, v in edges:
        result.append(f"{u} {v}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))