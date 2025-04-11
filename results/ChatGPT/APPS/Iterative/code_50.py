import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:n]]

# Build the tree
tree = defaultdict(list)
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

def bfs(start):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = start
    max_distance = 0

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor

    return farthest_node, max_distance

# Step 1: Find the farthest node from an arbitrary node (1)
farthest_from_start, _ = bfs(1)

# Step 2: Find the farthest node from the farthest node found in step 1
farthest_from_farthest, diameter_length = bfs(farthest_from_start)

# Step 3: Collect the path from farthest_from_start to farthest_from_farthest
def find_path(start, end):
    parent = [-1] * (n + 1)
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)

    path = []
    while end != -1:
        path.append(end)
        end = parent[end]
    return path[::-1]

path = find_path(farthest_from_start, farthest_from_farthest)

# Step 4: Choose three vertices from the path
a = path[0]
b = path[-1]
c = path[len(path) // 2]  # Choose a middle point

# Step 5: Calculate the number of edges in the union of paths
# The maximum number of edges in the union of paths is:
max_edges = len(path) - 1 + (n - len(path))

print(max_edges)
print(a, b, c)