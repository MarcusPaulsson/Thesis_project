def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check if we can satisfy the degree condition for vertex 1
    if len(graph[1]) < D:
        return "NO"

    # Start building the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree_count = 0

    # Use a queue for BFS
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        
        # If we are at vertex 1, we need to limit the degree to D
        if current == 1:
            for neighbor in graph[current]:
                if degree_count < D:
                    spanning_tree_edges.append((current, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)
                    degree_count += 1
                else:
                    break
        else:
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    spanning_tree_edges.append((current, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)

    # Check if we have n-1 edges in the spanning tree
    if len(spanning_tree_edges) != n - 1:
        return "NO"

    # Return the result
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree_edges)
    return "\n".join(result)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result and print it
result = find_spanning_tree(n, m, D, edges)
print(result)