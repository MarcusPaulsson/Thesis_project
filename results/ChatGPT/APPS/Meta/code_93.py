def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > k + 1 and d == 1):
        print("NO")
        return
    
    edges = []
    
    # Create the main path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the main path
    current_vertex = d + 2
    
    # Attach remaining vertices to the first vertex in the path
    for i in range(1, n - (d + 1) + 1):
        if i <= k - 1:
            edges.append((1, current_vertex))
            current_vertex += 1
        else:
            edges.append((2, current_vertex))
            current_vertex += 1
    
    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)