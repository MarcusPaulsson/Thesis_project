def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if D > len(graph[1]):
        print("NO")
        return

    # Start building the spanning tree
    spanning_tree_edges = []
    degree_count = {i: 0 for i in range(1, n + 1)}
    degree_count[1] = 0

    # Use a queue for BFS
    queue = deque([1])
    visited = set([1])
    
    # First, connect vertex 1 to D neighbors
    for neighbor in graph[1]:
        if degree_count[1] < D:
            spanning_tree_edges.append((1, neighbor))
            degree_count[1] += 1
            degree_count[neighbor] += 1
            visited.add(neighbor)
            queue.append(neighbor)

    # Now, we need to ensure we can connect the rest of the graph
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                spanning_tree_edges.append((current, neighbor))
                degree_count[current] += 1
                degree_count[neighbor] += 1
                visited.add(neighbor)
                queue.append(neighbor)
                if len(spanning_tree_edges) == n - 1:
                    break
        if len(spanning_tree_edges) == n - 1:
            break

    # Check if we have a valid spanning tree
    if len(spanning_tree_edges) == n - 1 and degree_count[1] == D:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)