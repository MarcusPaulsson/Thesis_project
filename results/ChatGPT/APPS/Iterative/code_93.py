def construct_tree(n, d, k):
    if d > 2 * (k - 1) or (d == 1 and n > 2) or (d > 1 and n == 1) or n > 1 + k * (d // 2):
        return "NO"
    
    edges = []
    
    # Create a line with d + 1 vertices to ensure the diameter d
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    # Now we have d + 1 vertices used
    current_vertex = d + 2
    
    # Keep track of the degree of each vertex
    degree = [0] * (n + 1)
    for i in range(1, d + 2):
        degree[i] = 1
    
    # Connect the remaining vertices to ensure degree constraints
    for i in range(current_vertex, n + 1):
        # Find a vertex to connect to that doesn't exceed degree k
        for j in range(1, d + 2):
            if degree[j] < k:
                edges.append((j, i))
                degree[j] += 1
                break
    
    if len(edges) != n - 1:
        return "NO"

    result = ["YES"]
    for edge in edges:
        result.append(f"{edge[0]} {edge[1]}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
result = construct_tree(n, d, k)
print(result)