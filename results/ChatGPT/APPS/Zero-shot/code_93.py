def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1:  # Check the maximum diameter possible with given degree
        return "NO"
    
    if d == 1 and n > 2:      # If diameter is 1, we can only have a 2-vertex tree
        return "NO"
    
    edges = []
    
    # Create a linear path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
        
    # The last vertex added in the path
    last_vertex = d + 1
    
    # Now we need to connect the remaining vertices
    for i in range(last_vertex + 1, n + 1):
        # Connect each new vertex to the first vertex in the path
        edges.append((1, i))
    
    # Check if any vertex exceeds the degree k
    degree_count = [0] * (n + 1)
    
    for u, v in edges:
        degree_count[u] += 1
        degree_count[v] += 1
    
    for i in range(1, n + 1):
        if degree_count[i] > k:
            return "NO"
    
    result = ["YES"]
    for u, v in edges:
        result.append(f"{u} {v}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
# Output result
print(construct_tree(n, d, k))