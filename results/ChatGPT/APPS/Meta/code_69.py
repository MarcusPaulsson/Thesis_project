def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    if D >= n:
        print("NO")
        return

    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    degree = {i: 0 for i in range(1, n + 1)}
    spanning_tree_edges = []
    visited = set()
    
    # Start BFS/DFS from vertex 1
    queue = deque([1])
    visited.add(1)

    while queue:
        node = queue.popleft()
        if degree[node] < D and node == 1:
            # Try to connect to more nodes if we are at node 1
            for neighbor in graph[node]:
                if neighbor not in visited and degree[node] < D:
                    spanning_tree_edges.append((node, neighbor))
                    degree[node] += 1
                    degree[neighbor] += 1
                    visited.add(neighbor)
                    queue.append(neighbor)
        else:
            # Connect to unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    spanning_tree_edges.append((node, neighbor))
                    degree[node] += 1
                    degree[neighbor] += 1
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Check if we have a valid spanning tree
    if degree[1] != D or len(spanning_tree_edges) != n - 1:
        print("NO")
    else:
        print("YES")
        for v, u in spanning_tree_edges:
            print(v, u)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

find_spanning_tree(n, m, D, edges)