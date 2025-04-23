def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        print("NO")
        return

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    degree = {i: 0 for i in range(1, n + 1)}
    spanning_tree_edges = []
    visited = set()

    # BFS to construct the spanning tree
    def bfs(start):
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited and degree[node] < D:
                    spanning_tree_edges.append((node, neighbor))
                    degree[node] += 1
                    degree[neighbor] += 1
                    visited.add(neighbor)
                    queue.append(neighbor)
                    if degree[node] == D:
                        break

    bfs(1)

    if degree[1] != D:
        print("NO")
        return

    # Add remaining edges to complete the spanning tree
    for u in range(1, n + 1):
        for v in graph[u]:
            if degree[u] < 1 and degree[v] < 1 and (u, v) not in spanning_tree_edges and (v, u) not in spanning_tree_edges:
                spanning_tree_edges.append((u, v))
                degree[u] += 1
                degree[v] += 1
                if len(spanning_tree_edges) == n - 1:
                    break

    if len(spanning_tree_edges) == n - 1:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")

# Example usage:
# n, m, D = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
# find_spanning_tree(n, m, D, edges)