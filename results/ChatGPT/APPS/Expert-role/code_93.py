def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d > n - 1) or (n > k * (d // 2 + 1)):
        return "NO"
    
    edges = []
    
    # Create the main path with length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have a path of length d, vertices are from 1 to d + 1
    last_vertex = d + 2
    
    # Now we need to attach the remaining vertices
    for i in range(1, d + 2):
        if last_vertex > n:
            break
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and last_vertex <= n:
            edges.append((i, last_vertex))
            last_vertex += 1
    
    if last_vertex <= n:
        return "NO"
    
    result = ["YES"]
    for u, v in edges:
        result.append(f"{u} {v}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))