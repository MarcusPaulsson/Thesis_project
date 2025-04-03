def solve():
  n = int(input())
  a = list(map(int, input().split()))

  depth = [0] * n
  parents = [0] * n
  
  q = [a[0]]
  idx = 1
  
  while q:
    curr = q.pop(0)
    children = []
    
    while idx < n:
      children.append(a[idx])
      idx += 1
      if idx < n and any(a[idx] < x for x in children):
        idx -= 1
        children.pop()
        break

    for child in children:
      parents[child - 1] = curr
      depth[child - 1] = depth[curr - 1] + 1
      q.append(child)
  
  print(max(depth))
    

t = int(input())
for _ in range(t):
  solve()