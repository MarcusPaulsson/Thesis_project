def construct_tree(n, d, k):
    # Check for impossible conditions
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > k * (k - 1) + 1):
        print("NO")
        return

    edges = []
    
    # Create the main path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the main path
    current_vertex = d + 2
    
    # Connect remaining vertices
    for i in range(1, d + 2):
        while len([e for e in edges if i in e]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
            if current_vertex > n:
                break
    
    # Check if we used all vertices
    if current_vertex <= n:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            print(u, v)

# Example usage:
# n, d, k = map(int, input().split())
# construct_tree(n, d, k)