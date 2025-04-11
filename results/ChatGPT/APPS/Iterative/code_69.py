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
    
    # First, connect D edges from vertex 1
    for neighbor in graph[1]:
        if degree < D:
            spanning_tree_edges.append((1, neighbor))
            visited[neighbor] = True
            degree += 1
        else:
            break
    
    # If we couldn't connect D edges, return NO
    if degree < D:
        print("NO")
        return
    
    # Use BFS or DFS to add the remaining edges
    queue = deque()
    for neighbor in graph[1]:
        if visited[neighbor]:
            continue
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

# Example usage:
# n, m, D = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
# find_spanning_tree(n, m, D, edges)