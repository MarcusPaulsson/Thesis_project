from collections import defaultdict, deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    farthest_node = start
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor
                    
    return farthest_node, dist

def main():
    n = int(input().strip())
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Find the farthest node from an arbitrary start node (node 1)
    farthest_from_start, _ = bfs(1, graph, n)
    # Find the farthest node from the previous farthest node
    farthest_from_far, dist_from_far = bfs(farthest_from_start, graph, n)
    
    # Get the farthest distance and nodes involved
    max_distance_node = farthest_from_far
    diameter_length = dist_from_far[max_distance_node]

    # To find three vertices a, b, c, we can use the two endpoints of the diameter
    # and one other node that maximizes the edges in the paths
    # We can choose the middle point of the diameter path or any leaf
    
    # Let's get the diameter path
    path = []
    current = max_distance_node
    while current != farthest_from_start:
        path.append(current)
        for neighbor in graph[current]:
            if dist_from_far[neighbor] == dist_from_far[current] - 1:
                current = neighbor
                break
    path.append(farthest_from_start)
    path.reverse()
    
    # Choosing a, b from the diameter ends, and c as a leaf or any node not in the path
    a = path[0]
    b = path[-1]
    c = -1
    
    for node in range(1, n + 1):
        if node not in path:
            c = node
            break

    # The maximum number of edges in the union of paths
    max_edges = diameter_length + 1 + (len(graph[a]) - 1) + (len(graph[b]) - 1)
    print(max_edges)
    print(a, b, c)

if __name__ == "__main__":
    main()