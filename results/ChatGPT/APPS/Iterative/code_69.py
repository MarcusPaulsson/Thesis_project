def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    if len(graph[1]) < D:
        print("NO")
        return

    # Start building the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    visited[1] = True
    degree = 0

    # Use a queue for BFS
    queue = deque([1])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                if degree < D and current == 1:
                    # Connect this neighbor to vertex 1
                    spanning_tree_edges.append((1, neighbor))
                    degree += 1
                else:
                    # Connect this neighbor to the current node
                    spanning_tree_edges.append((current, neighbor))
                
                visited[neighbor] = True
                queue.append(neighbor)

                # Stop if we already have enough edges
                if len(spanning_tree_edges) == n - 1:
                    break
        if len(spanning_tree_edges) == n - 1:
            break

    if degree != D or len(spanning_tree_edges) != n - 1:
        print("NO")
    else:
        print("YES")
        for v, u in spanning_tree_edges:
            print(v, u)

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)