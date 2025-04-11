def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (d == 0 and n > 1):
        print("NO")
        return
    
    print("YES")
    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have a path of length d, which uses d edges and has d + 1 vertices
    current_vertex = d + 2
    
    # We can attach additional vertices to the vertices in the path
    for i in range(1, d + 2):
        if current_vertex > n:
            break
        # Attach vertices to the current vertex if it has not reached the degree limit
        for _ in range(k - 1):
            if current_vertex > n:
                break
            edges.append((i, current_vertex))
            current_vertex += 1
    
    # If we have used up all vertices, print the edges
    if current_vertex - 1 == n:
        for u, v in edges:
            print(u, v)
    else:
        print("NO")

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)