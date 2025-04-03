from collections import defaultdict, deque

def bfs(start, n, graph):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest_node = start
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:  # Not visited
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, dist

def main():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Find the farthest point from an arbitrary starting point (1)
    farthest_node_from_start, _ = bfs(1, n, graph)
    
    # Find the farthest point from the previously found farthest node
    opposite_node, dist_from_opposite = bfs(farthest_node_from_start, n, graph)

    # Get the farthest node from the opposite node
    farthest_node_from_opposite, dist_from_farthest = bfs(opposite_node, n, graph)

    # Now we have the diameter ends: farthest_node_from_start and farthest_node_from_opposite
    # Let's find the third node that maximizes the edge count
    # We can take the farthest node from the first node we started with (or any node in the tree)
    
    # Collect nodes with maximum distance from either endpoint
    max_distance = -1
    third_node = -1
    for i in range(1, n + 1):
        if dist_from_opposite[i] > max_distance:
            max_distance = dist_from_opposite[i]
            third_node = i
            
    # The three nodes are:
    a = farthest_node_from_start
    b = opposite_node
    c = third_node
    
    # Output the result
    print(len(set([a, b, c])) + 2)  # The edges involved are the distinct edges in the paths
    print(a, b, c)

if __name__ == "__main__":
    main()