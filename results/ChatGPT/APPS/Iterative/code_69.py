def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check if the first vertex has enough neighbors to satisfy degree D
    if len(graph[1]) < D:
        print("NO")
        return
    
    spanning_tree = []
    degree = {i: 0 for i in range(1, n + 1)}
    
    # Start with vertex 1 and take D edges
    for neighbor in graph[1][:D]:
        spanning_tree.append((1, neighbor))
        degree[1] += 1
        degree[neighbor] += 1
    
    # Use a queue for BFS to complete the spanning tree
    queue = deque([1])
    visited = {1}
    
    while queue and len(spanning_tree) < n - 1:
        current = queue.popleft()
        for neighbor in graph[current]:
            if degree[current] > 1 and degree[neighbor] < 1:  # Ensure we can add this edge
                spanning_tree.append((current, neighbor))
                degree[current] += 1
                degree[neighbor] += 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Validate spanning tree
    if len(spanning_tree) != n - 1 or degree[1] != D:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)

# Input handling
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)