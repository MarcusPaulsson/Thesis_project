def construct_tree(n, d, k):
    # Check if it's possible to construct the tree
    if d > 2 * k or (d == 1 and n > 2) or (n > k + 1 and d == 1):
        print("NO")
        return

    # Start constructing the tree
    edges = []
    
    # Create a chain of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices used (1 to d + 1)
    used_vertices = d + 1
    
    # Now we need to connect the remaining vertices
    # We can connect them to the first vertex (1) or other vertices in the chain
    for i in range(used_vertices + 1, n + 1):
        if len(edges) < n - 1:
            # Try to connect to the first vertex
            if edges.count((1, i)) == 0 and edges.count((i, 1)) == 0:
                edges.append((1, i))
            else:
                # Connect to vertex 2 if possible
                if edges.count((2, i)) == 0 and edges.count((i, 2)) == 0:
                    edges.append((2, i))
                else:
                    # Connect to the next in the chain
                    edges.append((3, i))
    
    if len(edges) != n - 1:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)