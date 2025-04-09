def construct_tree(n, d, k):
    if d >= n or d * k < n - 1:
        print("NO")
        return

    print("YES")
    edges = []
    
    # Create a path of length d
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    # Current vertex where we can attach new vertices
    current_vertex = d + 1
    
    # Degree counts
    degree = [0] * (n + 1)
    
    # Attach remaining vertices
    for i in range(1, d + 2):
        while degree[i] < k and current_vertex <= n:
            edges.append((i, current_vertex))
            degree[i] += 1
            degree[current_vertex] += 1
            current_vertex += 1
    
    if current_vertex <= n:
        print("NO")
        return
    
    for u, v in edges:
        print(u, v)

# Input reading
n, d, k = map(int, input().split())
construct_tree(n, d, k)