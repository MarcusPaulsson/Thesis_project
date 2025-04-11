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

def find_max_edges_and_vertices(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the farthest node found
    farthest_from_farthest, max_distance = bfs(farthest_from_start, graph)
    
    # Step 3: Get the path from farthest_from_start to farthest_from_farthest
    def get_path(start, end):
        parent = {}
        queue = deque([start])
        visited = {start}
        
        while queue:
            node = queue.popleft()
            if node == end:
                break
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        path = []
        while end in parent:
            path.append(end)
            end = parent[end]
        path.append(start)
        return path[::-1]
    
    longest_path = get_path(farthest_from_start, farthest_from_farthest)
    
    # Step 4: Select three vertices from the longest path
    a = longest_path[0]
    b = longest_path[len(longest_path) // 2]
    c = longest_path[-1]
    
    # The maximum number of edges in the union of paths
    max_edges = 3 * (len(longest_path) - 1)
    
    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Get the result
max_edges, a, b, c = find_max_edges_and_vertices(n, edges)

# Output the result
print(max_edges)
print(a, b, c)