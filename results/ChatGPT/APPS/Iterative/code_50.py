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
    farthest_node_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the previously found farthest node
    opposite_node, diameter_length = bfs(farthest_node_from_start, graph)
    
    # Step 3: Get the path from farthest_node_from_start to opposite_node
    path = []
    def get_path(node, parent):
        if node == opposite_node:
            path.append(node)
            return True
        for neighbor in graph[node]:
            if neighbor != parent and get_path(neighbor, node):
                path.append(node)
                return True
        return False
    
    get_path(farthest_node_from_start, -1)
    path.reverse()
    
    # Step 4: Choose three vertices from the path
    if len(path) >= 3:
        a, b, c = path[0], path[len(path) // 2], path[-1]
    else:
        a, b, c = path[0], path[1], path[2]
    
    # The number of edges in the union of paths
    res = diameter_length + 1
    
    return res, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Find the result
result = find_max_edges(n, edges)

# Output the result
print(result[0])
print(result[1], result[2], result[3])