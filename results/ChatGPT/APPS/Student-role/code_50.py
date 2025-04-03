from collections import defaultdict, deque

def bfs(start, graph, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    farthest_node = start

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # not visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
                if distances[neighbor] > distances[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, distances

def find_max_edges_in_paths(n, edges):
    # Create adjacency list for the tree
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary starting point (1)
    farthest_from_start, _ = bfs(1, graph, n)
    
    # Step 2: Find the farthest node from that farthest node (this gives us one end of the diameter)
    opposite_end, distances_from_first = bfs(farthest_from_start, graph, n)
    
    # Step 3: Find the farthest node from the opposite end (this gives us the other end of the diameter)
    _, distances_from_second = bfs(opposite_end, graph, n)
    
    # Step 4: Find the two nodes which are the farthest from the diameter ends
    max_distance = 0
    a, b = -1, -1
    for i in range(1, n + 1):
        if distances_from_first[i] + distances_from_second[i] > max_distance:
            max_distance = distances_from_first[i] + distances_from_second[i]
            a = farthest_from_start
            b = opposite_end
    
    # Step 5: Find the third vertex to maximize edges
    # The third vertex should be chosen from the farthest points from the two endpoints
    candidates = []
    for i in range(1, n + 1):
        if i != a and i != b:
            candidates.append(i)
    
    # Find the candidate which maximizes the distance to both a and b
    c = candidates[0]
    max_additional_distance = 0
    
    for candidate in candidates:
        additional_distance = min(distances_from_first[candidate], distances_from_second[candidate])
        if additional_distance > max_additional_distance:
            max_additional_distance = additional_distance
            c = candidate

    # The final result is the max number of edges in the paths
    res = max_distance + 1  # +1 because edges are one less than the number of vertices

    return res, a, b, c

# Input Reading
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Function Call
result, a, b, c = find_max_edges_in_paths(n, edges)

# Output Result
print(result)
print(a, b, c)