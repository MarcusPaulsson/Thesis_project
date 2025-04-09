def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        print("NO")
        return

    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    if len(graph[1]) < D:
        print("NO")
        return

    tree_edges = []
    visited = set()
    visited.add(1)

    # Start by connecting vertex 1 to D neighbors
    for neighbor in graph[1][:D]:
        tree_edges.append((1, neighbor))
        visited.add(neighbor)

    # Use a queue to perform BFS/DFS for the rest of the vertices
    queue = deque()
    for neighbor in graph[1][:D]:
        queue.append(neighbor)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                tree_edges.append((current, neighbor))
                queue.append(neighbor)
                if len(tree_edges) == n - 1:
                    break
        if len(tree_edges) == n - 1:
            break

    if len(tree_edges) == n - 1:
        print("YES")
        for v, u in tree_edges:
            print(v, u)
    else:
        print("NO")

# Example usage
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)