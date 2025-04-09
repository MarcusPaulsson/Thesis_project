def solve():
  n, d, k = map(int, input().split())

  if d >= n:
    print("NO")
    return

  if d == 1 and n > 2:
    if k == 1:
      print("NO")
      return
    
  if d > 1 and k == 1:
    print("NO")
    return

  edges = []
  
  # Create the diameter path
  for i in range(d):
    edges.append((i + 1, i + 2))
  
  degree = [0] * (n + 1)
  for u, v in edges:
    degree[u] += 1
    degree[v] += 1
  
  next_node = d + 2
  
  # Add nodes to the diameter path
  for i in range(1, d + 2):
    while degree[i] < k and next_node <= n:
      edges.append((i, next_node))
      degree[i] += 1
      degree[next_node] += 1
      next_node += 1
  
  # Check if we used all nodes
  if next_node <= n:
    print("NO")
    return
  
  # Check if the graph is connected
  if len(edges) != n - 1:
    print("NO")
    return
  
  # Check if the degree is at most k
  for i in range(1, n + 1):
    if degree[i] > k:
      print("NO")
      return
  
  print("YES")
  for u, v in edges:
    print(u, v)

solve()