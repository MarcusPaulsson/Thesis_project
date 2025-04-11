def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if we can have degree D for vertex 1
    if len(graph[1]) < D:
        print("NO")
        return
    
    # Start building the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    
    # First, connect vertex 1 to D neighbors
    degree_count = 0
    for neighbor in graph[1]:
        if degree_count < D:
            spanning_tree_edges.append((1, neighbor))
            visited[neighbor] = True
            degree_count += 1
        else:
            break
    
    # Now, we need to add the rest of the edges to form a spanning tree
    for neighbor in graph[1]:
        if degree_count >= D:
            break
        if not visited[neighbor]:
            spanning_tree_edges.append((1, neighbor))
            visited[neighbor] = True
            degree_count += 1
    
    # BFS to add remaining edges to the spanning tree
    for start in range(2, n + 1):
        if not visited[start]:
            queue.append(start)
            visited[start] = True
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        spanning_tree_edges.append((current, neighbor))
                        queue.append(neighbor)
                        if len(spanning_tree_edges) == n - 1:
                            break
                if len(spanning_tree_edges) == n - 1:
                    break
    
    # Check if we have a valid spanning tree
    if len(spanning_tree_edges) == n - 1:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Find and print the spanning tree
find_spanning_tree(n, m, D, edges)