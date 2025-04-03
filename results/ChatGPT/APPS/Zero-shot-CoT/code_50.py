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

    # Step 1: Find the farthest node from an arbitrary node (let's choose 1)
    farthest_node_from_1, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the farthest_node_from_1
    farthest_node_from_A, distances_A = bfs(farthest_node_from_1, graph)
    
    # Step 3: Find the farthest node from the farthest_node_from_A
    farthest_node_from_B, distances_B = bfs(farthest_node_from_A, graph)

    # The maximum distance between the two farthest nodes gives us the diameter
    # Now we can pick the two nodes and find a third node
    max_distance = distances_B[farthest_node_from_B]
    
    # Find a third node which is not one of the endpoints of the diameter
    a = farthest_node_from_A
    b = farthest_node_from_B
    c = None

    for i in range(1, n + 1):
        if i != a and i != b:
            c = i
            break

    # The maximum number of edges in the union of the three paths
    # The number of edges in the tree is n - 1, we need to calculate the edges used in the paths
    max_edges = max_distance + 1

    return max_edges, a, b, c

# Input reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Solve the problem
max_edges, a, b, c = find_max_edges(n, edges)

# Output the result
print(max_edges)
print(a, b, c)