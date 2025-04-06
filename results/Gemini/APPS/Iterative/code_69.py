def solve():
  n, m, d = map(int, input().split())
  edges = []
  for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

  def check_degree(tree_edges):
    degree = 0
    for u, v in tree_edges:
      if u == 1 or v == 1:
        degree += 1
    return degree

  def is_connected(tree_edges):
    if not tree_edges:
      return False 
    
    adj = {}
    for i in range(1, n + 1):
      adj[i] = []
    
    for u, v in tree_edges:
      adj[u].append(v)
      adj[v].append(u)
    
    visited = [False] * (n + 1)
    q = [1]
    visited[1] = True
    
    while q:
      u = q.pop(0)
      for v in adj[u]:
        if not visited[v]:
          visited[v] = True
          q.append(v)
    
    for i in range(1, n + 1):
      if not visited[i]:
        return False
    return True

  import itertools
  
  for i in range(1 << m):
    tree_edges = []
    for j in range(m):
      if (i >> j) & 1:
        tree_edges.append(edges[j])
    
    if len(tree_edges) == n - 1:
      if is_connected(tree_edges) and check_degree(tree_edges) == d:
        print("YES")
        for u, v in tree_edges:
          print(u, v)
        return

  print("NO")

solve()