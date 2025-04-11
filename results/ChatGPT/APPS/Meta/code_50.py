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
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)

    # Step 2: Find the farthest node from the farthest node found
    farthest_from_a, distances_from_a = bfs(farthest_from_start, graph)

    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, distances_from_b = bfs(farthest_from_a, graph)

    # The diameter of the tree is the distance between farthest_from_a and farthest_from_b
    diameter_length = distances_from_a[farthest_from_b]

    # Step 4: Find the nodes on the diameter path
    path = []
    current = farthest_from_b
    while current != farthest_from_start:
        path.append(current)
        for neighbor in graph[current]:
            if distances_from_a[neighbor] == distances_from_a[current] - 1:
                current = neighbor
                break
    path.append(farthest_from_start)
    path.reverse()

    # Step 5: Choose three distinct vertices from the diameter path
    if len(path) >= 3:
        a, b, c = path[0], path[1], path[2]
    else:
        a, b, c = path[0], path[1], path[1]  # fallback, should not happen in valid input

    # The maximum number of edges in the union of the paths
    max_edges = diameter_length + 1

    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Solve the problem
max_edges, a, b, c = find_max_edges(n, edges)

# Output the result
print(max_edges)
print(a, b, c)