from collections import defaultdict, deque
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
edges = [tuple(map(int, line.split())) for line in data[1:]]

# Build the tree
tree = defaultdict(list)
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

# Function to perform BFS and return the farthest node and its distance
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    farthest_node = start
    max_distance = 0

    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                if distance[node] + 1 > max_distance:
                    max_distance = distance[node] + 1
                    farthest_node = neighbor

    return farthest_node, max_distance

# Find one endpoint of the diameter
first_end, _ = bfs(1)

# Find the other endpoint of the diameter
second_end, diameter_length = bfs(first_end)

# To find the nodes on the diameter path
def find_path(start, end):
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                stack.append(neighbor)
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]

# Get the diameter path
diameter_path = find_path(first_end, second_end)

# Choose vertices a, b, c from the diameter path
a = diameter_path[0]
b = diameter_path[len(diameter_path) // 2]  # Middle point
c = diameter_path[-1]

# The maximum number of edges covered by paths between the three vertices
max_edges = len(set(find_path(a, b) + find_path(b, c) + find_path(a, c))) - 1

print(max_edges)
print(a, b, c)