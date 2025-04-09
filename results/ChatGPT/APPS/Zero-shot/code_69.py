def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    if len(graph[1]) < D:
        print("NO")
        return
    
    # Degree of vertex 1 should be D
    tree_edges = []
    visited = set()
    visited.add(1)
    
    # Start with vertex 1
    degree_1 = 0
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if degree_1 < D and node == 1:
                    tree_edges.append((node, neighbor))
                    degree_1 += 1
                elif node != 1:
                    tree_edges.append((node, neighbor))
                
                visited.add(neighbor)
                queue.append(neighbor)
                
                if degree_1 >= D and node == 1:
                    break
        
        if degree_1 >= D:
            break

    if degree_1 < D or len(tree_edges) < n - 1:
        print("NO")
        return
    
    print("YES")
    for u, v in tree_edges:
        print(u, v)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)