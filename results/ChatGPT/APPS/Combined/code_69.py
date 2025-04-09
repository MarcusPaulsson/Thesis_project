def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict

    if D >= n:
        return "NO"

    # Create an adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Degree of the first vertex
    degree_1 = len(graph[1])

    # Check if it's possible to have degree D for vertex 1
    if D > degree_1:
        return "NO"

    # Start constructing the spanning tree
    visited = [False] * (n + 1)
    spanning_tree_edges = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if (node == 1 and degree_1 > D) or (node != 1):
                    spanning_tree_edges.append((node, neighbor))
                    dfs(neighbor)
                    if len(spanning_tree_edges) == n - 1:
                        return True
                elif node == 1 and degree_1 == D:
                    # For vertex 1, keep track of degree
                    if len(spanning_tree_edges) < D:
                        spanning_tree_edges.append((node, neighbor))
                        degree_1 -= 1
                        dfs(neighbor)
                        if len(spanning_tree_edges) == n - 1:
                            return True
        return False

    dfs(1)

    if len(spanning_tree_edges) != n - 1 or degree_1 != 0:
        return "NO"

    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree_edges)
    return "\n".join(result)

# Input reading
n, m, D = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(m)]

# Find the spanning tree
output = find_spanning_tree(n, m, D, edges)
print(output)