def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d > n - 1) or (k == 1 and n > 1) or (d == 0 and n > 1):
        print("NO")
        return

    edges = []
    
    # Build the main path to achieve the diameter d
    for i in range(1, d + 1):
        edges.append((i, i + 1))

    # Now we have d + 1 vertices in the main path
    current_vertex = d + 2

    # Connect remaining vertices
    for i in range(1, d + 2):
        if current_vertex > n:
            break
        # For each vertex in the path, we can add more vertices until we reach degree k
        for _ in range(k - 1):  # We already have one connection in the path
            if current_vertex > n:
                break
            edges.append((i, current_vertex))
            current_vertex += 1

    if current_vertex <= n:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            print(u, v)

# Read input
n, d, k = map(int, input().strip().split())
construct_tree(n, d, k)