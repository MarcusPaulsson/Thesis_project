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

def find_max_edges_in_paths(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the previously found node
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, max_distance = bfs(farthest_from_a, graph)
    
    # To find a third distinct vertex not in the path from farthest_from_a to farthest_from_b
    path = []
    parent = {}
    
    def find_path(node):
        while node in parent:
            path.append(node)
            node = parent[node]
        path.append(node)
    
    def bfs_with_parent(start):
        queue = deque([start])
        visited = {start}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
    
    bfs_with_parent(farthest_from_a)
    find_path(farthest_from_b)
    
    path_set = set(path)
    third_vertex = next((v for v in range(1, n + 1) if v not in path_set), None)
    
    return max_distance + 1, farthest_from_a, farthest_from_b, third_vertex

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
max_edges, a, b, c = find_max_edges_in_paths(n, edges)
print(max_edges)
print(a, b, c)