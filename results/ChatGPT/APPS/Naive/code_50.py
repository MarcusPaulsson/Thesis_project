import sys
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
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (1)
    farthest_node_from_start, _ = bfs(1, graph)
    
    # Step 2: Find the farthest node from the farthest node found in step 1
    farthest_node, distances = bfs(farthest_node_from_start, graph)
    
    # Step 3: Find the farthest node from the second farthest node
    other_end_node, distances_from_other_end = bfs(farthest_node, graph)

    # Step 4: Find the maximum distance and the nodes at that distance
    max_distance = max(distances)
    max_distance_nodes = [i for i in range(1, n + 1) if distances[i] == max_distance]

    # Step 5: Choose three distinct nodes
    a = farthest_node_from_start
    b = max_distance_nodes[0]
    c = max_distance_nodes[1] if len(max_distance_nodes) > 1 else (b % n + 1)

    # The number of edges in the union of paths is the number of edges in the tree
    # minus the edges in the path between a and b
    return len(edges), a, b, c

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    edges = [tuple(map(int, line.split())) for line in data[1:n]]
    
    result = find_max_edges(n, edges)
    print(result[0])
    print(result[1], result[2], result[3])