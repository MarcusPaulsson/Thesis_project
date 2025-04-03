def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict
    
    # Build the graph
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)
    
    # Check if vertex 1 has enough neighbors
    if len(graph[1]) < D:
        print("NO")
        return
    
    # Prepare to collect the spanning tree edges
    spanning_tree_edges = []
    visited = set()
    
    # Start with vertex 1
    visited.add(1)
    
    # Add edges from vertex 1 to its D neighbors
    for i in range(D):
        neighbor = graph[1][i]
        spanning_tree_edges.append((1, neighbor))
        visited.add(neighbor)

    # Now we need to add edges from other vertices
    # Use DFS or BFS to add edges to the spanning tree
    def dfs(v):
        for u in graph[v]:
            if u not in visited:
                visited.add(u)
                spanning_tree_edges.append((v, u))
                dfs(u)
    
    # Start DFS from one of the neighbors of 1
    dfs(graph[1][0])
    
    # Check if we have exactly n-1 edges
    if len(spanning_tree_edges) == n - 1:
        print("YES")
        for v, u in spanning_tree_edges:
            print(v, u)
    else:
        print("NO")

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)