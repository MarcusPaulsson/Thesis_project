def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1 or (d == 1 and n > 2) or (n > 1 and d == 0):
        print("NO")
        return

    edges = []
    
    # Create the main path for the diameter
    for i in range(1, d + 2):
        edges.append((i, i + 1))
    
    current_vertex = d + 2
    # Add branches to the path
    for i in range(1, d + 2):
        for _ in range(k - 1):
            if current_vertex <= n:
                edges.append((i, current_vertex))
                current_vertex += 1
            else:
                break
        if current_vertex > n:
            break
    
    if current_vertex <= n:
        print("NO")
    else:
        print("YES")
        for u, v in edges:
            print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)