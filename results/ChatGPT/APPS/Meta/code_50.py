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
    
    # Step 2: Find the farthest node from the previously found node
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, diameter_length = bfs(farthest_from_a, graph)
    
    # The maximum number of edges in the union of paths is the diameter length + 1
    max_edges = diameter_length + 1
    
    # To find the three vertices, we can use the path from farthest_from_start to farthest_from_b
    # We can use BFS to find the actual path
    def find_path(start, end):
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
    
    path = find_path(farthest_from_start, farthest_from_b)
    
    # Choose the first, last, and one more node from the path
    a = path[0]
    b = path[-1]
    c = path[len(path) // 2]  # Choose a middle node
    
    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Finding the result
result = find_max_edges(n, edges)
print(result[0])
print(result[1], result[2], result[3])