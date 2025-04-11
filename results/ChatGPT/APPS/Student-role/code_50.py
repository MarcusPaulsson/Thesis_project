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

def find_max_edges(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_from_start, _ = bfs(1, graph)

    # Step 2: Find the farthest node from the farthest node found in step 1
    farthest_from_a, _ = bfs(farthest_from_start, graph)

    # Step 3: Find the farthest node from the second farthest node
    farthest_from_b, _ = bfs(farthest_from_a, graph)

    # The maximum number of edges is the distance between these two farthest nodes
    max_edges = (len(graph) - 1)  # since it's a tree, max edges is n-1

    # We can return the two endpoints of the longest path and any third node
    return max_edges, farthest_from_start, farthest_from_b

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
result = find_max_edges(n, edges)
print(result[0])
print(result[1], result[2], (set(range(1, n + 1)) - {result[1], result[2]}).pop())