def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if len(graph[1]) < D:
        print("NO")
        return

    # Start building the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree = 0

    # Use BFS or DFS to construct the spanning tree
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if degree < D and node == 1:
                    spanning_tree_edges.append((node, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)
                    degree += 1
                elif node != 1:
                    spanning_tree_edges.append((node, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)

                if degree == D and node == 1:
                    break
        if degree == D and node == 1:
            break

    # If we reached the required degree for vertex 1
    if degree < D:
        print("NO")
        return

    # Now we need to ensure we have n-1 edges in the spanning tree
    while len(spanning_tree_edges) < n - 1:
        for u in range(1, n + 1):
            if visited[u]:
                for v in graph[u]:
                    if not visited[v]:
                        spanning_tree_edges.append((u, v))
                        visited[v] = True
                        if len(spanning_tree_edges) == n - 1:
                            break
            if len(spanning_tree_edges) == n - 1:
                break

    if len(spanning_tree_edges) != n - 1:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)