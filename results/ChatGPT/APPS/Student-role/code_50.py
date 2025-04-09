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

def find_farthest_nodes(graph):
    # Start from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)
    # Find the farthest node from that node
    farthest_node, distances = bfs(farthest_from_start, graph)
    return farthest_from_start, farthest_node, distances

def get_paths(a, b, c, distances):
    # The total number of distinct edges in paths a-b, b-c, and a-c
    return len(set(distances[a]) | set(distances[b]) | set(distances[c]))

n = int(input().strip())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# Find two farthest nodes in the tree
u, v, distances_u = find_farthest_nodes(graph)
# Get distances from u
_, distances_v = bfs(v, graph)

# Find the maximum number of distinct edges
max_edges = 0
best_triplet = (1, 2, 3)

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if a != b:
            for c in range(b + 1, n + 1):
                if a != c and b != c:
                    edges_count = get_paths(a, b, c, distances_u)
                    if edges_count > max_edges:
                        max_edges = edges_count
                        best_triplet = (a, b, c)

print(max_edges)
print(*best_triplet)