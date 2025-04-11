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
    farthest_from_a, diameter_length = bfs(farthest_from_start, graph)
    
    # Step 3: Get the path from farthest_from_start to farthest_from_a
    path = []
    def get_path(node, parent):
        path.append(node)
        if node == farthest_from_a:
            return True
        for neighbor in graph[node]:
            if neighbor != parent and get_path(neighbor, node):
                return True
        path.pop()
        return False
    
    get_path(farthest_from_start, -1)
    
    # Step 4: Choose the three vertices
    a = path[0]
    b = path[len(path) // 2]
    c = path[-1]
    
    # The maximum number of edges in the union of paths
    max_edges = diameter_length + 1
    
    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Get the result
result = find_max_edges(n, edges)

# Output the result
print(result[0])
print(result[1], result[2], result[3])