def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    # Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check for degree constraints
    if len(graph[1]) < D:
        return "NO"

    # Use BFS or DFS to find a spanning tree
    visited = [False] * (n + 1)
    spanning_tree_edges = []

    # Start with vertex 1
    visited[1] = True
    queue = deque([1])
    degree_count = 0

    # First, let's add D edges from vertex 1
    for neighbor in graph[1]:
        if degree_count < D:
            spanning_tree_edges.append((1, neighbor))
            visited[neighbor] = True
            degree_count += 1
        else:
            break

    # Now we need to perform BFS/DFS to cover the rest of the graph
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
        return "YES", spanning_tree_edges
    else:
        return "NO"

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = find_spanning_tree(n, m, D, edges)

if result == "NO":
    print(result)
else:
    print(result[0])
    for u, v in result[1]:
        print(u, v)