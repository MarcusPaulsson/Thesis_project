def construct_tree(n, d, k):
    # Check for impossible conditions
    if d > 2 * k or (d == 1 and n > 2) or (d == 0 and n > 1):
        return "NO"

    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 2):
        edges.append((i, i + 1))
    
    # We have d + 1 nodes in the main path
    current_node = d + 2

    for i in range(1, d + 2):
        # Add branches if we have remaining nodes
        for _ in range(1, k):
            if current_node > n:
                break
            edges.append((i, current_node))
            current_node += 1

    if current_node <= n:
        return "NO"
    
    result = ["YES"]
    result.extend(f"{a} {b}" for a, b in edges)
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
result = construct_tree(n, d, k)
print(result)