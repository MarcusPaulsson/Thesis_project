def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if D > len(graph[1]) or D >= n:
        print("NO")
        return

    # Start building the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree_count = 0

    # First, connect vertex 1 to D neighbors
    for neighbor in graph[1]:
        if degree_count < D:
            spanning_tree_edges.append((1, neighbor))
            visited[neighbor] = True
            degree_count += 1
        else:
            break

    # BFS to connect the rest of the vertices
    queue = deque()
    for neighbor in graph[1]:
        if visited[neighbor]:
            queue.append(neighbor)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                spanning_tree_edges.append((current, neighbor))
                queue.append(neighbor)
                if len(spanning_tree_edges) == n - 1:
                    break
        if len(spanning_tree_edges) == n - 1:
            break

    if len(spanning_tree_edges) == n - 1:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")

# Example usage
# n, m, D = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
# find_spanning_tree(n, m, D, edges)