from collections import defaultdict, deque

def bfs(start, graph):
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
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_node, _ = bfs(1, graph)

    # Step 2: Find the farthest node from the previously found farthest node
    other_end, distances = bfs(farthest_node, graph)

    # Step 3: Find the farthest node from the other end to get the diameter
    diameter_length = distances[other_end]
    
    # Step 4: Find the path from farthest_node to other_end
    path = []
    current = other_end
    while current != farthest_node:
        path.append(current)
        for neighbor in graph[current]:
            if distances[neighbor] == distances[current] - 1:
                current = neighbor
                break
    path.append(farthest_node)
    path.reverse()

    # Step 5: Choose three distinct vertices
    if len(path) >= 3:
        a, b, c = path[0], path[len(path) // 2], path[-1]
    else:
        a, b, c = path[0], path[1], path[2]

    return diameter_length + 1, a, b, c

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
res, a, b, c = find_max_edges(n, edges)
print(res)
print(a, b, c)