def construct_tree(n, d, k):
    if d >= n or (k == 1 and d > 0) or (d > 2 * (k - 1)):
        print("NO")
        return

    edges = []
    
    # Create a path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # The last vertex in the path is d + 1
    # Start branching from the first vertex
    current_vertex = 1
    for i in range(d + 1, n + 1):
        edges.append((current_vertex, i))
        # If current_vertex has reached its degree limit, move to the next vertex in the path
        if edges.count((current_vertex, i)) >= k:
            current_vertex += 1
    
    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)