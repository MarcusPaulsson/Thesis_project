from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def find_spanning_tree(n, m, D, edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    if len(graph[1]) < D:  # First vertex cannot have degree D
        return "NO"
    
    # Start building the spanning tree
    spanning_tree = []
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        degree_count = 0
        
        while queue:
            if degree_count == D:
                break
            current = queue.popleft()
            connections = 0
            
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    if current == 1 and connections < D:
                        spanning_tree.append((current, neighbor))
                        connections += 1
                        visited[neighbor] = True
                        queue.append(neighbor)
                    elif current != 1:
                        spanning_tree.append((current, neighbor))
                        visited[neighbor] = True
                        queue.append(neighbor)

            if current == 1:
                degree_count += connections
        
        return degree_count
    
    if bfs(1) < D:  # If we couldn't satisfy the degree requirement
        return "NO"
    
    # Ensure we have n-1 edges
    if len(spanning_tree) < n - 1:
        remaining_edges = []
        for u in range(1, n + 1):
            for v in graph[u]:
                if u < v and (u, v) not in spanning_tree and (v, u) not in spanning_tree:
                    remaining_edges.append((u, v))
        
        for u, v in remaining_edges:
            if len(spanning_tree) == n - 1:
                break
            spanning_tree.append((u, v))

    if len(spanning_tree) != n - 1:
        return "NO"
    
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree)
    return "\n".join(result)

# Read input
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Output result
print(find_spanning_tree(n, m, D, edges))