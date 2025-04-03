from collections import defaultdict, deque

def bfs(start, tree, n):
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

def find_max_edges(n, edges):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_node_from_1, _ = bfs(1, tree, n)
    
    # Step 2: Find the farthest node from the previous farthest node
    farthest_node, _ = bfs(farthest_node_from_1, tree, n)
    
    # Step 3: Get the distance and path from farthest_node_from_1 to farthest_node
    path = []
    def get_path(node, parent):
        if node == farthest_node:
            path.append(node)
            return True
        for neighbor in tree[node]:
            if neighbor != parent and get_path(neighbor, node):
                path.append(node)
                return True
        return False

    get_path(farthest_node_from_1, -1)
    
    # The path is now the longest path in the tree
    path.reverse()
    length = len(path)
    
    # Step 4: Choose three nodes to maximize the edges
    if length >= 3:
        a, b, c = path[0], path[length // 2], path[-1]
    else:
        a, b, c = path[0], path[1], path[2]
    
    # Step 5: Count the edges in the union of paths
    edges_count = (length - 1) + (length - 1) + 1  # Paths a-b, b-c, a-c count

    # Resulting output
    return edges_count, (a, b, c)

# Read input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Get the result
res, (a, b, c) = find_max_edges(n, edges)

# Output result
print(res)
print(a, b, c)