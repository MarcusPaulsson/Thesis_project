from collections import defaultdict, deque

def bfs(start, graph):
    visited = {start}
    q = deque([start])
    farthest_node = start
    distance = 0
    
    while q:
        next_q = deque()
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_q.append(neighbor)
                    farthest_node = neighbor
        q = next_q
        distance += 1
        
    return farthest_node, distance - 1

def find_max_edges_in_paths(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Step 1: Find one endpoint of the longest path in the tree
    endpoint1 = bfs(1, graph)[0]
    
    # Step 2: Find the farthest node from endpoint1, which gives us the diameter endpoint
    endpoint2, diameter_length = bfs(endpoint1, graph)
    
    # Step 3: We find the path from endpoint1 to endpoint2 to determine the path vertices
    def find_path(start, end):
        parent = {start: None}
        q = deque([start])
        while q:
            node = q.popleft()
            if node == end:
                break
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    q.append(neighbor)

        path = []
        while end is not None:
            path.append(end)
            end = parent[end]
        return path[::-1]

    path = find_path(endpoint1, endpoint2)
    
    # The middle of the path can be a good candidate for the third vertex
    mid_index = len(path) // 2
    third_vertex = path[mid_index]
    
    # We can use the two endpoints and the middle vertex as our three distinct vertices
    a, b, c = path[0], path[-1], third_vertex
    
    return diameter_length + 1, a, b, c

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

result, a, b, c = find_max_edges_in_paths(n, edges)
print(result)
print(a, b, c)