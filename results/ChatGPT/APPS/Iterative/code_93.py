def construct_tree(n, d, k):
    # Check for impossible configurations
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > 1 and d == 0):
        print("NO")
        return

    print("YES")
    
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Number of used vertices including the path
    used_vertices = d + 1
    
    # Create branches from the path
    for i in range(1, d + 1):
        if used_vertices >= n:
            break
        for _ in range(k - 1):  # Add at most `k - 1` branches to each node
            if used_vertices >= n:
                break
            edges.append((i, used_vertices + 1))
            used_vertices += 1
    
    # Verify if we have exactly n - 1 edges
    if len(edges) != n - 1:
        print("NO")
    else:
        for u, v in edges:
            print(u, v)

# Input reading
n, d, k = map(int, input().split())
construct_tree(n, d, k)