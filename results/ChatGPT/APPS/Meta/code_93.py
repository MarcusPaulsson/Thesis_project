def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 1) or (n > k + 1 and d == 1):
        print("NO")
        return

    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d edges, and we need to connect the remaining vertices
    current_vertex = d + 2
    for i in range(1, d + 1):
        if current_vertex > n:
            break
        # Connect remaining vertices to the path
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1

    # If we still have vertices left, we can connect them to any of the previous vertices
    while current_vertex <= n:
        edges.append((1, current_vertex))
        current_vertex += 1

    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)