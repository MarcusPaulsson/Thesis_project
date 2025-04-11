def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    if D >= n or D > len(graph[1]):
        return "NO"
    
    # Start building the spanning tree
    spanning_tree = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree = 0
    
    # First, connect vertex 1 to D neighbors if possible
    for neighbor in graph[1]:
        if degree < D:
            spanning_tree.append((1, neighbor))
            visited[neighbor] = True
            degree += 1
    
    # If we couldn't connect D neighbors, return NO
    if degree < D:
        return "NO"
    
    # Now we need to connect the remaining vertices
    queue = deque()
    for neighbor in graph[1]:
        if visited[neighbor]:
            queue.append(neighbor)
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                spanning_tree.append((current, neighbor))
                visited[neighbor] = True
                queue.append(neighbor)
                if len(spanning_tree) == n - 1:
                    break
        if len(spanning_tree) == n - 1:
            break
    
    if len(spanning_tree) == n - 1:
        result = ["YES"]
        result.extend(f"{u} {v}" for u, v in spanning_tree)
        return "\n".join(result)
    else:
        return "NO"

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = find_spanning_tree(n, m, D, edges)
print(result)