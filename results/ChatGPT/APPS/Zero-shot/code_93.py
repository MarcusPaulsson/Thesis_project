def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1:
        return "NO"
    
    if d == 1 and n > 2:
        return "NO"
    
    if d == 1:
        if n == 2:
            return "YES\n1 2"
        else:
            return "NO"
    
    if n <= k + 1 and d > 1:
        return "NO"
    
    edges = []
    
    # Create the main path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the path
    current_vertex = d + 2
    
    # We can add branches to the vertices in the path
    for i in range(1, d + 1):
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
            if current_vertex > n:
                break
    
    if current_vertex <= n:
        return "NO"
    
    result = "YES\n" + "\n".join(f"{u} {v}" for u, v in edges)
    return result

n, d, k = map(int, input().split())
print(construct_tree(n, d, k))