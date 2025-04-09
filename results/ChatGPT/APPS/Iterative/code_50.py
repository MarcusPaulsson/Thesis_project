from collections import defaultdict, deque
import sys

def bfs(start):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = start
    max_distance = 0
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_node = neighbor
                    
    return farthest_node, max_distance

def find_three_nodes():
    # Step 1: Find a farthest node from an arbitrary node (node 1)
    farthest_from_start, _ = bfs(1)
    
    # Step 2: Find the farthest node from that farthest node (this gives us one endpoint of the diameter)
    farthest_from_a, diameter_length = bfs(farthest_from_start)
    
    # Step 3: The other endpoint of the diameter
    farthest_from_b, _ = bfs(farthest_from_a)
    
    # Now we need to find the third node that maximizes the edges
    # We can use BFS from one of the endpoints to get the nodes along the diameter path
    path_nodes = []
    queue = deque([farthest_from_start])
    parent = {farthest_from_start: None}
    
    while queue:
        node = queue.popleft()
        path_nodes.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    
    # Reconstruct the path from farthest_from_start to farthest_from_b
    diameter_path = []
    current = farthest_from_b
    while current is not None:
        diameter_path.append(current)
        current = parent[current]
    
    diameter_path.reverse()
    
    # Choose three nodes: two endpoints of the diameter and one additional node
    if len(diameter_path) > 2:
        third_node = diameter_path[len(diameter_path) // 2]
    else:
        third_node = diameter_path[0]  # In case of very small diameter
    
    return diameter_length + 1, farthest_from_start, third_node, farthest_from_b

n = int(sys.stdin.readline().strip())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

max_edges, a, b, c = find_three_nodes()
print(max_edges)
print(a, b, c)