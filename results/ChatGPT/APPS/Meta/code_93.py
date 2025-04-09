def construct_tree(n, d, k):
    # Check for impossibility conditions
    if d > 2 * (k - 1) + 1:
        return "NO"
    if d == 1 and n > 2:
        return "NO"
    if n > (k * (d + 1)) // 2 + (k - 1):
        return "NO"

    edges = []
    
    # Create the main path for the diameter d
    for i in range(1, d + 1):
        edges.append((i, i + 1))

    # Now we have d + 1 vertices in the main path
    current_vertex = d + 2

    # Add additional vertices
    for i in range(1, d + 2):
        # While we can add more edges from the current vertex
        while len([e for e in edges if e[0] == i or e[1] == i]) < k and current_vertex <= n:
            edges.append((i, current_vertex))
            current_vertex += 1
            if current_vertex > n:
                break

    # Check if we used all vertices
    if current_vertex <= n:
        return "NO"

    result = ["YES"] + [f"{u} {v}" for u, v in edges]
    return "\n".join(result)

# Input reading
n, d, k = map(int, input().split())
print(construct_tree(n, d, k))