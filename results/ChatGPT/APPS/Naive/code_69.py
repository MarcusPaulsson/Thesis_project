def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        print("NO")
        return

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    degree = {i: 0 for i in range(1, n + 1)}
    spanning_tree_edges = []
    visited = set()
    
    # BFS to construct the spanning tree
    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            if degree[node] < D and node == 1:
                # Try to connect to D neighbors
                for neighbor in graph[node]:
                    if degree[node] < D and neighbor not in visited:
                        spanning_tree_edges.append((node, neighbor))
                        degree[node] += 1
                        degree[neighbor] += 1
                        visited.add(neighbor)
                        queue.append(neighbor)
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        spanning_tree_edges.append((node, neighbor))
                        degree[node] += 1
                        degree[neighbor] += 1
                        visited.add(neighbor)
                        queue.append(neighbor)

    bfs(1)

    if degree[1] != D or len(spanning_tree_edges) != n - 1:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)

# Example usage:
# n, m, D = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
# find_spanning_tree(n, m, D, edges)