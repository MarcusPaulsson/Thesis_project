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

def find_max_edges(n, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph, n)

    # Step 2: Find the farthest node from that farthest node (this gives one endpoint of the diameter)
    farthest_node, dist_from_first = bfs(farthest_from_start, graph, n)

    # Step 3: Find the farthest node from the other endpoint (this gives the other endpoint of the diameter)
    other_end_node, dist_from_second = bfs(farthest_node, graph, n)

    # The diameter endpoints are farthest_from_start and farthest_node
    # The maximum number of edges is the distance between these two endpoints
    max_edges = dist_from_second[farthest_node]

    # To find three distinct vertices, we can use the two endpoints and one more vertex
    # We can simply take any vertex that is not one of the two endpoints
    third_vertex = 1 if farthest_from_start != 1 else 2

    return max_edges + 1, (farthest_from_start, farthest_node, third_vertex)

# Reading input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Getting the result
max_edges, (a, b, c) = find_max_edges(n, edges)

# Outputting the result
print(max_edges)
print(a, b, c)