def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    if D > len(graph[1]):
        return "NO"

    # Start constructing the spanning tree
    spanning_tree_edges = []
    degree_count = {i: 0 for i in range(1, n + 1)}
    visited = set()
    
    # BFS/DFS to construct spanning tree
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited and degree_count[node] < D:
                spanning_tree_edges.append((node, neighbor))
                degree_count[node] += 1
                degree_count[neighbor] += 1
                dfs(neighbor)

    # Start DFS from vertex 1
    dfs(1)

    # Check if we reached the required degree for vertex 1
    if degree_count[1] != D:
        return "NO"

    # Ensure we have n-1 edges in the spanning tree
    # We can add remaining edges if needed
    for v in range(1, n + 1):
        for neighbor in graph[v]:
            if degree_count[v] < (n - 1):
                if degree_count[neighbor] < (n - 1) and (v, neighbor) not in spanning_tree_edges and (neighbor, v) not in spanning_tree_edges:
                    spanning_tree_edges.append((v, neighbor))
                    degree_count[v] += 1
                    degree_count[neighbor] += 1
                    if len(spanning_tree_edges) == n - 1:
                        break

    if len(spanning_tree_edges) != n - 1:
        return "NO"

    result = ["YES"]
    for edge in spanning_tree_edges:
        result.append(f"{edge[0]} {edge[1]}")
    
    return "\n".join(result)

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output result
result = find_spanning_tree(n, m, D, edges)
print(result)