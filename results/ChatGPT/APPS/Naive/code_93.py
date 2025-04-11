def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1:
        return "NO"
    
    if d == 0 and n > 1:
        return "NO"
    
    if n == 1:
        return "YES\n"
    
    edges = []
    
    # Create the main path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the path
    current_vertex = d + 2
    
    # Attach remaining vertices to the path
    for i in range(1, d + 2):
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
    
    if current_vertex <= n:
        return "NO"
    
    result = ["YES"]
    for u, v in edges:
        result.append(f"{u} {v}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))