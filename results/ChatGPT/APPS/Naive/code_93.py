def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or d >= n:
        return "NO"
    
    edges = []
    
    # Create a path of length d
    for i in range(1, d + 1):
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
    
    if current_vertex <= n:
        return "NO"
    
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(result)

# Input reading
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))