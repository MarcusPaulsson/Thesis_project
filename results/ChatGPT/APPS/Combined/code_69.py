def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Early exit if the desired degree is not feasible
    if D >= n:
        return "NO"

    # Construct the graph from edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if the first vertex can meet the degree requirement
    if len(graph[1]) < D:
        return "NO"
    
    # Initialize variables for spanning tree construction
    spanning_tree_edges = []
    visited = set([1])
    degree_count = 0
    
    # Use BFS to ensure we can reach the required degree for vertex 1
    queue = deque([1])
    
    while queue and degree_count < D:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                spanning_tree_edges.append((current, neighbor))
                visited.add(neighbor)
                queue.append(neighbor)
                degree_count += 1
                
                if degree_count == D:
                    break
    
    # If we don't have the required degree for vertex 1
    if degree_count < D:
        return "NO"
    
    # Continue to build the spanning tree ensuring connectivity
    for u, v in edges:
        if len(spanning_tree_edges) == n - 1:
            break
        if (u in visited and v not in visited) or (v in visited and u not in visited):
            spanning_tree_edges.append((u, v))
            visited.update([u, v])
    
    # Ensure we have a valid spanning tree
    if len(spanning_tree_edges) != n - 1:
        return "NO"
    
    # Prepare the output
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree_edges)
    
    return "\n".join(result)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result and print
result = find_spanning_tree(n, m, D, edges)
print(result)