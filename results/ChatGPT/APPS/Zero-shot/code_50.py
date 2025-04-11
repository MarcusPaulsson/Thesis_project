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
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the previously found farthest node
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, _ = bfs(farthest_from_a, graph)
    
    # The diameter endpoints are farthest_from_start and farthest_from_a
    # We can take any two nodes from the diameter path and one more node
    # to maximize the edges covered.
    
    # Collect the path from farthest_from_start to farthest_from_a
    def collect_path(start, end):
        parent = {start: None}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == end:
                break
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        path = []
        while end is not None:
            path.append(end)
            end = parent[end]
        return path[::-1]
    
    path = collect_path(farthest_from_start, farthest_from_a)
    
    # Choose the endpoints of the diameter and one more node
    a = path[0]
    b = path[-1]
    c = path[len(path) // 2]  # Choose a middle node as c
    
    # Calculate the number of edges in the union of paths
    max_edges = len(path) - 1 + (len(graph[a]) - 1) + (len(graph[b]) - 1) - 1
    
    return max_edges, a, b, c

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
max_edges, a, b, c = find_max_edges(n, edges)
print(max_edges)
print(a, b, c)