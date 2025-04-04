def construct_tree(n, d, k):
    if d > 2 * k or (d == 1 and n > 2) or (n > k + 1 and d == 1):
        return "NO"
    
    edges = []
    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))
    
    # Number of vertices already used
    used = d + 1
    
    # Now, attach remaining vertices to the first vertex of the path
    # if we can still add more vertices without exceeding the degree limit
    if used < n:
        for i in range(used, n):
            if len([v for u, v in edges if u == 1]) < k:
                edges.append((1, i + 1))
            else:
                # Find a vertex that can accommodate more connections
                for j in range(1, used):
                    if len([v for u, v in edges if u == j]) < k:
                        edges.append((j, i + 1))
                        break
            used += 1
    
    result = ["YES"]
    for u, v in edges:
        result.append(f"{u} {v}")
    
    return "\n".join(result)

# Read input
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))