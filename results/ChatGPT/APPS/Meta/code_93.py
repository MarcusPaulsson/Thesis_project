def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 1) or (n > k * (k - 1) + 1 and d > 1):
        print("NO")
        return
    
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have a path 1-2-3-...-(d+1) making the diameter d
    current_vertex = d + 2
    
    # Attach extra vertices to the path
    for i in range(1, d + 1):
        if current_vertex > n:
            break
        # Attach vertices to vertex i
        for _ in range(k - 1):
            if current_vertex > n:
                break
            edges.append((i, current_vertex))
            current_vertex += 1
            
    # If we still have vertices left, we need to attach them
    while current_vertex <= n:
        if current_vertex > n:
            break
        edges.append((1, current_vertex))  # Attach to the root (or any node)
        current_vertex += 1
    
    # Print the result
    print("YES")
    for u, v in edges:
        print(u, v)

# Example input
n, d, k = map(int, input().split())
construct_tree(n, d, k)