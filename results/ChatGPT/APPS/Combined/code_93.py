def construct_tree(n, d, k):
    # Check if the parameters make it impossible to construct such a tree
    if d > 2 * (k - 1) or (d == 1 and n > 2) or (d == 0 and n > 1) or (n == 1 and d > 0):
        print("NO")
        return

    edges = []
    
    # Create the main path for diameter d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    current_vertex = d + 2  # The next available vertex after creating the diameter path

    # Attach remaining vertices to ensure degree constraints
    degree = [0] * (d + 2)  # Track the degree of vertices from 1 to d + 1

    for i in range(1, d + 1):
        while degree[i] < k and current_vertex <= n:
            edges.append((i, current_vertex))
            degree[i] += 1
            current_vertex += 1
            
            # If we have filled all vertices, we can stop early
            if current_vertex > n:
                break

    # If there are still vertices left, attach them to the last vertex in the diameter path
    last_vertex = d + 1
    while current_vertex <= n:
        if degree[last_vertex] < k:
            edges.append((last_vertex, current_vertex))
            degree[last_vertex] += 1
            current_vertex += 1
        else:
            # Find a new vertex to attach current_vertex to
            for i in range(1, d + 1):
                if degree[i] < k:
                    edges.append((i, current_vertex))
                    degree[i] += 1
                    current_vertex += 1
                    break

    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)