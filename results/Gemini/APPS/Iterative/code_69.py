def solve():
  n, m, d = map(int, input().split())
  edges = []
  for _ in range(m):
    edges.append(tuple(map(int, input().split())))

  adj = {i: [] for i in range(1, n + 1)}
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

  def bfs(start_node, degree):
    q = [(start_node, [])]
    visited = {start_node}

    while q:
      curr_node, path = q.pop(0)
      
      neighbors = []
      for u, v in edges:
        if u == curr_node and v not in visited:
          neighbors.append(v)
        elif v == curr_node and u not in visited:
          neighbors.append(u)

      for neighbor in neighbors:
        new_path = path + [(curr_node, neighbor)]
        
        if len(new_path) == n - 1:
          
          tree_adj = {i: [] for i in range(1, n + 1)}
          tree_edges = []
          for u, v in new_path:
            tree_adj[u].append(v)
            tree_adj[v].append(u)
            tree_edges.append((u,v))

          
          visited_nodes = set()
          queue = [1]
          visited_nodes.add(1)
          while queue:
            node = queue.pop(0)
            for neighbor_node in tree_adj[node]:
              if neighbor_node not in visited_nodes:
                visited_nodes.add(neighbor_node)
                queue.append(neighbor_node)
          
          if len(visited_nodes) == n:
            degree_1 = 0
            for u, v in tree_edges:
              if u == 1 or v == 1:
                degree_1 += 1
            if degree_1 == degree:
              return new_path
          
        elif neighbor not in visited:
          visited.add(neighbor)
          q.append((neighbor, new_path))
    return None

  spanning_tree = bfs(1, d)

  if spanning_tree:
    print("YES")
    for u, v in spanning_tree:
      print(u, v)
  else:
    print("NO")

solve()