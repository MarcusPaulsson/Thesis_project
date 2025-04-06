def solve():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  
  counts = {}
  for x in a:
    counts[x] = counts.get(x, 0) + 1
  
  for x in counts:
    if counts[x] > k:
      print("NO")
      return
  
  print("YES")
  colors = [0] * n
  color_idx = 1
  
  colored_count = 0
  
  for i in range(n):
    if counts[a[i]] > 0:
      colors[i] = color_idx
      counts[a[i]] -= 1
      color_idx = (color_idx % k) + 1
      colored_count += 1
      
      if colored_count == k:
        break
        
  color_idx = 1
  
  for i in range(n):
    if colors[i] == 0:
      colors[i] = color_idx
      color_idx = (color_idx % k) + 1
  
  print(*colors)

solve()