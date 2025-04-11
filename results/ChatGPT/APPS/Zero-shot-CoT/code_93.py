def construct_tree(n, d, k):
    if d > 2 * (k - 1) + 1:
        print("NO")
        return
    
    if d == 1 and n > 1:
        print("NO")
        return
    
    if n == 1:
        print("YES")
        return
    
    edges = []
    
    # Create the main path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Now we have d + 1 vertices in the path
    current_vertex = d + 2
    
    # Attach remaining vertices to the first vertex in the path
    for i in range(current_vertex, n + 1):
        edges.append((1, i))
    
    # Check if any vertex exceeds degree k
    degree_count = [0] * (n + 1)
    for u, v in edges:
        degree_count[u] += 1
        degree_count[v] += 1
    
    if any(degree > k for degree in degree_count[1:]):
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        print(u, v)

# Read input
n, d, k = map(int, input().split())
construct_tree(n, d, k)