from collections import defaultdict, deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    farthest_node = start
    max_distance = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if len(visited) > max_distance:
                    max_distance = len(visited)
                    farthest_node = neighbor

    return farthest_node, max_distance

def find_three_nodes(n, edges):
    graph = defaultdict(list)
    
    # Build the tree
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Find the farthest node from an arbitrary starting point (node 1)
    farthest_from_start, _ = bfs(1, graph)
    
    # Find the farthest node from the previously found node
    farthest_from_a, _ = bfs(farthest_from_start, graph)
    
    # Find the farthest node from the second farthest node
    farthest_from_b, max_edges = bfs(farthest_from_a, graph)
    
    return max_edges, farthest_from_start, farthest_from_b

# Input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Find the result
max_edges, a, b = find_three_nodes(n, edges)

# Output
print(max_edges)
print(a, b, (b % n) + 1)  # Just to ensure three distinct vertices