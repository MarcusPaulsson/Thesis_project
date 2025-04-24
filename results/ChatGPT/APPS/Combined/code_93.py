def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > k + 1 and d == 1):
        print("NO")
        return

    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d edges, and we need to connect the remaining vertices
    current_vertex = d + 2
    for i in range(1, d + 1):
        while len([e for e in edges if i in e]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
            
    if current_vertex <= n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)