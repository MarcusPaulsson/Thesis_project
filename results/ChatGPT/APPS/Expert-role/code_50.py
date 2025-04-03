from collections import defaultdict, deque

def bfs(start, graph):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque([start])
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

n = int(input().strip())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# Step 1: Find the farthest node from an arbitrary node (node 1)
farthest_node, _ = bfs(1, graph)

# Step 2: Find the farthest node from the farthest node found
other_farthest_node, dist_from_first = bfs(farthest_node, graph)

# Step 3: Use the path from farthest_node to other_farthest_node to find the maximum
path = []
current = other_farthest_node
while current != farthest_node:
    path.append(current)
    for neighbor in graph[current]:
        if dist_from_first[neighbor] == dist_from_first[current] - 1:
            current = neighbor
            break
path.append(farthest_node)
path.reverse()

# Step 4: Choose three distinct vertices a, b, c from the path
a = path[0]
b = path[len(path) // 2]  # Middle of the path
c = path[-1]

# Step 5: The number of edges in the union of paths is |E| = |V| - 1 + |V| - 1 + |V| - 1 - 3 = 3*len(path) - 3
res = len(path) - 1 + len(path) - 1 + len(path) - 1 - 3

print(res)
print(a, b, c)