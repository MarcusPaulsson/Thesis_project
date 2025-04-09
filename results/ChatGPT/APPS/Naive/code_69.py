def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Build the adjacency list
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    # Check if the degree of vertex 1 can be exactly D
    if D > len(graph[1]):
        return "NO"

    # BFS to find a spanning tree with the desired degree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    degree = 0

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                spanning_tree_edges.append((node, neighbor))
                queue.append(neighbor)

                # Count the degree for the first vertex
                if node == 1:
                    degree += 1

                # If we have reached the desired degree for vertex 1
                if node == 1 and degree == D:
                    break

        # If we reached the desired degree, we can stop
        if degree == D:
            break

    # If we have not reached the desired degree of vertex 1
    if degree < D:
        return "NO"

    # Now we need to add more edges if we have less than n-1 edges in the spanning tree
    if len(spanning_tree_edges) < n - 1:
        for v, u in edges:
            if len(spanning_tree_edges) >= n - 1:
                break
            if (v, u) not in spanning_tree_edges and (u, v) not in spanning_tree_edges:
                if visited[v] and visited[u]:
                    continue
                spanning_tree_edges.append((v, u))
                visited[v] = True
                visited[u] = True

    # Check if we have exactly n-1 edges
    if len(spanning_tree_edges) != n - 1:
        return "NO"

    result = ["YES"]
    result.extend(f"{v} {u}" for v, u in spanning_tree_edges)
    return "\n".join(result)

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = find_spanning_tree(n, m, D, edges)
print(result)