from collections import defaultdict, deque

def bfs(start, graph):
    visited = {start: 0}
    queue = deque([start])
    farthest_node = start
    max_distance = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor
                    
    return farthest_node, max_distance

def find_max_edges(n, edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 1: Find the farthest node from an arbitrary node (node 1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the previously found farthest node
    farthest_from_a, diameter_length = bfs(farthest_from_start, graph)
    
    # Step 3: Find the path from farthest_from_start to farthest_from_a
    path = []
    parent = {farthest_from_start: None}
    queue = deque([farthest_from_start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    
    # Reconstruct the path
    current = farthest_from_a
    while current is not None:
        path.append(current)
        current = parent[current]
    
    path_length = len(path)
    
    # Step 4: Choose three distinct vertices
    if path_length >= 3:
        a, b, c = path[0], path[path_length // 2], path[-1]
    else:
        a, b, c = path[0], path[1], path[2]
    
    return diameter_length + 1, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Get the result
result = find_max_edges(n, edges)

# Output the result
print(result[0])
print(result[1], result[2], result[3])