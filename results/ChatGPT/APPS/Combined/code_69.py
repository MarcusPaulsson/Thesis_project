def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        print("NO")
        return

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if len(graph[1]) < D:
        print("NO")
        return

    spanning_tree_edges = []
    visited = set()
    visited.add(1)

    # Connect vertex 1 to D neighbors
    degree_count = 0
    for neighbor in graph[1]:
        if degree_count < D:
            spanning_tree_edges.append((1, neighbor))
            visited.add(neighbor)
            degree_count += 1
        else:
            break

    # Use BFS to add remaining edges to form a spanning tree
    queue = deque([1])
    while queue and len(spanning_tree_edges) < n - 1:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                spanning_tree_edges.append((current, neighbor))
                queue.append(neighbor)
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