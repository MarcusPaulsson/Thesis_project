def solve():
  n, d, k = map(int, input().split())

  if d >= n:
    print("NO")
    return

  if d == 1 and n > 2:
    if k < 2:
      print("NO")
      return
  elif k == 1 and d > 1:
    print("NO")
    return
  
  if k == 1 and d != 1:
    print("NO")
    return
  
  if n == 1 and d > 0:
    print("NO")
    return
  
  if n == 1 and d == 0:
      print("YES")
      return

  edges = []
  
  # Create a path of length d
  for i in range(d):
    edges.append((i + 1, i + 2))
  
  remaining_nodes = n - d - 1
  
  if remaining_nodes < 0:
    print("NO")
    return
  
  degrees = [0] * (n + 1)
  for u, v in edges:
    degrees[u] += 1
    degrees[v] += 1

  current_node = d + 2
  
  
  for i in range(1, d + 2):
    while degrees[i] < k and remaining_nodes > 0:
      edges.append((i, current_node))
      degrees[i] += 1
      degrees[current_node] += 1
      current_node += 1
      remaining_nodes -= 1

  if remaining_nodes > 0:
      print("NO")
      return

  if len(edges) != n - 1:
    print("NO")
    return
  
  print("YES")
  for u, v in edges:
    print(u, v)

solve()