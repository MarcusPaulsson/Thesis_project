from collections import defaultdict, deque

def bfs(start, graph, n):
    visited = [-1] * (n + 1)
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

def find_max_edges_and_vertices(n, edges):
    graph = defaultdict(list)
    
    # Build the graph
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_node_from_start, _ = bfs(1, graph, n)

    # Step 2: Find the farthest node from the previously found farthest node
    farthest_node, distances = bfs(farthest_node_from_start, graph, n)

    # Step 3: Find the second farthest node from the farthest node found
    second_farthest_node, distances_from_second = bfs(farthest_node, graph, n)

    # The maximum number of edges is the distance between these two farthest nodes
    max_edges = distances[second_farthest_node]

    # Collect the path nodes
    path_nodes = []
    current = second_farthest_node
    while current != farthest_node:
        path_nodes.append(current)
        for neighbor in graph[current]:
            if distances[neighbor] == distances[current] - 1:
                current = neighbor
                break
    path_nodes.append(farthest_node)

    # Choose any three distinct vertices from the path
    a, b, c = path_nodes[0], path_nodes[1], path_nodes[2]

    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Get the result
result = find_max_edges_and_vertices(n, edges)

# Output the result
print(result[0])
print(result[1], result[2], result[3])