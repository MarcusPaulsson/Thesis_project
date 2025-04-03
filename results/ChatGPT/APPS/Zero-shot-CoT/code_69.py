def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    # Check if we can form a valid spanning tree
    if D >= n or len(graph[1]) < D:
        print("NO")
        return

    # Start building the spanning tree
    tree_edges = []
    visited = set()
    visited.add(1)
    degree_1 = 0

    # Choose D edges from vertex 1
    for neighbor in graph[1]:
        if degree_1 < D:
            tree_edges.append((1, neighbor))
            visited.add(neighbor)
            degree_1 += 1
        else:
            break

    # BFS/DFS to add the remaining edges
    queue = deque()
    for neighbor in graph[1]:
        if degree_1 < D:
            continue
        if neighbor not in visited:
            queue.append(neighbor)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                tree_edges.append((current, neighbor))
                visited.add(neighbor)
                queue.append(neighbor)
                if len(tree_edges) == n - 1:
                    break
        if len(tree_edges) == n - 1:
            break

    # If we have exactly n-1 edges, we have a spanning tree
    if len(tree_edges) == n - 1:
        print("YES")
        for v, u in tree_edges:
            print(v, u)
    else:
        print("NO")

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find a spanning tree
find_spanning_tree(n, m, D, edges)