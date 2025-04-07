from collections import defaultdict, deque

def bfs(start, n, graph):
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

def find_diameter_path(graph, start, end, dist_from_start):
    path = []
    current = end
    while current != start:
        path.append(current)
        for neighbor in graph[current]:
            if dist_from_start[neighbor] == dist_from_start[current] - 1:
                current = neighbor
                break
    path.append(start)
    return path[::-1]  # Reverse to get the path from start to end

def main():
    n = int(input().strip())
    graph = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    # Step 1: Find the farthest node from an arbitrary node (node 1)
    farthest_node_from_start, _ = bfs(1, n, graph)

    # Step 2: Find the farthest node from that farthest node
    farthest_node, dist_from_one_end = bfs(farthest_node_from_start, n, graph)

    # Step 3: Find the path and distances from the other endpoint
    diameter_path = find_diameter_path(graph, farthest_node_from_start, farthest_node, dist_from_one_end)
    diameter_length = len(diameter_path) - 1  # Number of edges

    # Choosing three distinct vertices: first, middle, last of the diameter path
    a = diameter_path[0]
    c = diameter_path[-1]
    b = diameter_path[len(diameter_path) // 2]  # Middle node

    # The maximum edges covered
    max_edges = diameter_length + 1  # edges are one less than the number of nodes in the path

    print(max_edges)
    print(a, b, c)

if __name__ == "__main__":
    main()