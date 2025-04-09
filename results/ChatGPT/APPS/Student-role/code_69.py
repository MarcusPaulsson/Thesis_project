def find_spanning_tree(n, m, D, edges):
    if D >= n:
        print("NO")
        return

    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    degree = {i: 0 for i in range(1, n + 1)}
    spanning_tree_edges = []
    visited = set()
    queue = deque([1])
    visited.add(1)

    while queue:
        node = queue.popleft()
        if degree[node] < D:
            for neighbor in graph[node]:
                if neighbor not in visited and degree[node] < D:
                    degree[node] += 1
                    degree[neighbor] += 1
                    spanning_tree_edges.append((node, neighbor))
                    visited.add(neighbor)
                    queue.append(neighbor)

                if degree[node] == D:
                    break

    if degree[1] != D:
        print("NO")
        return

    # Add remaining edges to complete the spanning tree
    for u, v in edges:
        if (u, v) not in spanning_tree_edges and (v, u) not in spanning_tree_edges:
            if len(spanning_tree_edges) < n - 1:
                spanning_tree_edges.append((u, v))

    if len(spanning_tree_edges) == n - 1:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")


# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)