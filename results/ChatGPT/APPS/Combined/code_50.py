from collections import defaultdict, deque

def bfs(start, graph):
    visited = [-1] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = start

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, visited

def find_max_edges(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # First BFS to find the farthest node from an arbitrary node (e.g., node 1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Second BFS to find the farthest node from the previously found farthest node
    farthest_from_a, distances = bfs(farthest_from_start, graph)
    
    # The diameter length of the tree
    diameter_length = distances[farthest_from_a]

    # Reconstruct the path from farthest_from_start to farthest_from_a
    path = []
    current = farthest_from_a
    queue = deque([farthest_from_start])
    parents = {farthest_from_start: None}
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)

    # Backtrack to get the path
    while current is not None:
        path.append(current)
        current = parents[current]

    # Selecting nodes A, B, and C
    A = path[0]
    B = path[-1]
    C = path[len(path) // 2]  # Picking a middle node in the path

    return diameter_length + 1, (A, B, C)

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Find maximum edges and the vertices
result, vertices = find_max_edges(n, edges)

# Output the results
print(result)
print(*vertices)