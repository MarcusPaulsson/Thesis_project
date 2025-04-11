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
    
    # Step 1: Find the farthest node from an arbitrary node (let's say node 1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the previously found farthest node
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, _ = bfs(farthest_from_a, graph)
    
    # Now we have the two endpoints of the longest path in the tree
    # We can take any two nodes from the longest path and one more node
    # that is not on that path to maximize the edges used.
    
    # To find the path from farthest_from_start to farthest_from_a
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
    
    longest_path = find_path(farthest_from_start, farthest_from_a)
    
    # Choose the two endpoints of the longest path
    a = longest_path[0]
    b = longest_path[-1]
    
    # Choose a third node that is not on the longest path
    path_set = set(longest_path)
    c = next(node for node in range(1, n + 1) if node not in path_set)
    
    # The maximum number of edges in the union of the paths
    max_edges = len(longest_path) - 1 + len(graph[a]) + len(graph[b]) + len(graph[c]) - 3
    
    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Finding the result
max_edges, a, b, c = find_max_edges_in_paths(n, edges)

# Output the result
print(max_edges)
print(a, b, c)