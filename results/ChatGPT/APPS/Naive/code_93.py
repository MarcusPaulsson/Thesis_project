def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1:
        return "NO"
    
    if d == 1 and n > 2:
        return "NO"
    
    if n == 1:
        return "YES\n"
    
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Create a list of nodes that are part of the main path
    last_node = d + 1
    
    # For each node in the main path, add remaining nodes
    for i in range(1, d + 1):
        if last_node >= n:
            break
        while len([x for x, y in edges if x == i]) < k - 1 and last_node < n:
            edges.append((i, last_node))
            last_node += 1
    
    # If there are still nodes left, we need to attach them
    if last_node <= n:
        return "NO"
    
    result = "YES\n" + "\n".join(f"{u} {v}" for u, v in edges)
    return result


# Read input
n, d, k = map(int, input().split())

# Construct tree and print the result
print(construct_tree(n, d, k))