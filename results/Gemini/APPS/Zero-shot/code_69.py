def solve():
  n, m, D = map(int, input().split())
  edges = []
  for _ in range(m):
    edges.append(list(map(int, input().split())))

  def check_degree(tree_edges):
    degree = 0
    for u, v in tree_edges:
      if u == 1 or v == 1:
        degree += 1
    return degree

  def is_connected(tree_edges):
    if not tree_edges:
      return False

    adj = [[] for _ in range(n + 1)]
    for u, v in tree_edges:
      adj[u].append(v)
      adj[v].append(u)

    visited = [False] * (n + 1)
    q = [1]
    visited[1] = True
    count = 0
    while q:
      u = q.pop(0)
      count += 1
      for v in adj[u]:
        if not visited[v]:
          visited[v] = True
          q.append(v)
    return count == n

  def find_spanning_tree(edges, D):
    import itertools
    for i in range(1 << m):
      tree_edges = []
      for j in range(m):
        if (i >> j) & 1:
          tree_edges.append(edges[j])

      if len(tree_edges) == n - 1 and is_connected(tree_edges) and check_degree(tree_edges) == D:
        return tree_edges
    return None

  spanning_tree = find_spanning_tree(edges, D)

  if spanning_tree:
    print("YES")
    for u, v in spanning_tree:
      print(u, v)
  else:
    print("NO")

solve()