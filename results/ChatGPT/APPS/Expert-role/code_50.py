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
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the farthest node found in step 1
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Step 3: Find the farthest node from the farthest node found in step 2
    farthest_from_b, _ = bfs(farthest_from_a, graph)
    
    # The diameter of the tree is the distance between farthest_from_start and farthest_from_b
    diameter_length = _

    # To maximize the number of edges in the paths, we can choose the endpoints of the diameter
    # and one more vertex that is not on the path between them.
    
    # We can use BFS again to find the path from farthest_from_start to farthest_from_b
    def find_path(start, end):
        parent = {start: None}
        queue = deque([start])
        path = []
        
        while queue:
            node = queue.popleft()
            if node == end:
                break
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        # Reconstruct the path
        while end is not None:
            path.append(end)
            end = parent[end]
        
        return path[::-1]
    
    path = find_path(farthest_from_start, farthest_from_b)
    
    # Choose the two endpoints of the diameter
    a = farthest_from_start
    b = farthest_from_b
    
    # Choose a third vertex that is not on the path
    path_set = set(path)
    c = None
    for node in range(1, n + 1):
        if node not in path_set and node != a and node != b:
            c = node
            break
    
    return diameter_length + 1, a, b, c

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
res, a, b, c = find_max_edges_and_vertices(n, edges)
print(res)
print(a, b, c)