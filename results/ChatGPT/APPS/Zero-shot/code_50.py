from collections import defaultdict, deque

def bfs(start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest_node = start
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor
    return farthest_node, dist

n = int(input())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Find the farthest node from an arbitrary node (1)
farthest_from_start, _ = bfs(1, n)
# Find the farthest node from that farthest node (this gives one endpoint of the diameter)
farthest_node, dist_from_first = bfs(farthest_from_start, n)
# Now find distances from the second farthest node (this gives the other endpoint of the diameter)
_, dist_from_second = bfs(farthest_node, n)

# The maximum number of edges used in paths among three distinct vertices is the diameter length
max_edges = dist_from_first[farthest_node]

# Now we need to choose three vertices a, b, c
# We can take the two endpoints of the diameter and one more node
a, b = farthest_from_start, farthest_node

# Choose the third vertex with the maximum distance from either of the endpoints
third_vertex = -1
if dist_from_first[b] > dist_from_second[b]:
    # Take the third vertex from the first distances
    for i in range(1, n + 1):
        if i != a and i != b and (third_vertex == -1 or dist_from_first[i] > dist_from_first[third_vertex]):
            third_vertex = i
else:
    # Take the third vertex from the second distances
    for i in range(1, n + 1):
        if i != a and i != b and (third_vertex == -1 or dist_from_second[i] > dist_from_second[third_vertex]):
            third_vertex = i

print(max_edges)
print(a, b, third_vertex)