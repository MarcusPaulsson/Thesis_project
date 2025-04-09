def solve():
  n, d, k = map(int, input().split())

  if d >= n:
    print("NO")
    return

  if d == 1 and n > 2:
    if k <= 1:
      print("NO")
      return
  
  if d > 1 and k == 1:
      print("NO")
      return

  if d > 1 and n > 2 and k ==1:
      print("NO")
      return

  if d > n -1:
      print("NO")
      return
  
  edges = []
  nodes = list(range(1, n + 1))
  
  # Create the diameter path
  for i in range(d):
    edges.append((i + 1, i + 2))

  remaining_nodes = nodes[d+1:]
  
  
  if k == 1 and d > 1 and n > 2:
      print("NO")
      return

  if len(remaining_nodes) > 0:
    if k == 1:
      print("NO")
      return
    
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        
    
    for node in remaining_nodes:
      
      found_parent = False
      for i in range(1,d+2):
        if degree[i] < k:
          edges.append((node, i))
          degree[node] += 1
          degree[i] += 1
          found_parent = True
          break
      
      if not found_parent:
          print("NO")
          return
    
    
  
  degrees_valid = True
  degree = [0] * (n + 1)
  for u, v in edges:
      degree[u] += 1
      degree[v] += 1
  
  for i in range(1, n+1):
      if degree[i] > k:
          degrees_valid = False
          break

  if len(edges) != n - 1:
    print("NO")
    return


  if degrees_valid:
      print("YES")
      for u, v in edges:
          print(u, v)
  else:
      print("NO")
solve()