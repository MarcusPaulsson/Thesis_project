def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        return "NO"

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if len(graph[1]) < D:
        return "NO"

    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree_count = 0

    queue = deque([1])
    
    while queue and degree_count < D:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                spanning_tree_edges.append((current, neighbor))
                queue.append(neighbor)
                degree_count += 1
                if degree_count == D:
                    break

    if degree_count < D:
        return "NO"

    for u in range(1, n + 1):
        if not visited[u]:
            for v in graph[u]:
                if visited[v]:
                    spanning_tree_edges.append((u, v))
                    visited[u] = True
                    break

    if len(spanning_tree_edges) != n - 1:
        return "NO"

    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree_edges)
    return "\n".join(result)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = find_spanning_tree(n, m, D, edges)
print(result)