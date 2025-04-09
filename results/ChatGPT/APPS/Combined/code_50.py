from collections import defaultdict, deque

def bfs(start, tree, n):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = start

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, visited

def maximum_edges_in_paths(n, edges):
    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Find farthest nodes using BFS
    farthest_from_start, _ = bfs(1, tree, n)
    farthest_from_a, distances_from_a = bfs(farthest_from_start, tree, n)
    farthest_from_b, distances_from_b = bfs(farthest_from_a, tree, n)

    # Maximum edges in paths are calculated as the distance between these two farthest nodes
    max_edges = distances_from_a[farthest_from_b]

    # Collect three distinct vertices a, b, c
    vertex_a = farthest_from_start
    vertex_b = farthest_from_a
    vertex_c = next(i for i in range(1, n + 1) if i != vertex_a and i != vertex_b)

    return max_edges + 1, vertex_a, vertex_b, vertex_c

# Input handling
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

result = maximum_edges_in_paths(n, edges)
print(result[0])
print(result[1], result[2], result[3])