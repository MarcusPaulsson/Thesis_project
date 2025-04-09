def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check if we can satisfy the degree condition for vertex 1
    if len(graph[1]) < D:
        print("NO")
        return

    # Prepare to store the spanning tree edges
    spanning_tree = []
    visited = [False] * (n + 1)
    visited[1] = True

    # Start BFS from vertex 1
    queue = deque([1])
    
    # Add edges from vertex 1 to its neighbors until we reach degree D
    degree_count = 0
    for neighbor in graph[1]:
        if degree_count < D:
            spanning_tree.append((1, neighbor))
            visited[neighbor] = True
            degree_count += 1
            queue.append(neighbor)

    # Now perform BFS/DFS to add remaining edges
    while queue and degree_count < D:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                spanning_tree.append((current, neighbor))
                visited[neighbor] = True
                queue.append(neighbor)
                if len(spanning_tree) == n - 1:  # Stop if we have enough edges
                    break

    # Add additional edges for vertex 1 to ensure its degree is D
    if degree_count < D:
        for neighbor in graph[1]:
            if degree_count < D and visited[neighbor]:
                continue
            if degree_count < D:
                spanning_tree.append((1, neighbor))
                degree_count += 1
                if degree_count == D:
                    break

    # Check if we have formed a spanning tree
    if len(spanning_tree) == n - 1 and degree_count == D:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)