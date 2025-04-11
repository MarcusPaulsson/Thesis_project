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

  coloring = [0] * n
  color_assignment = {}
  color_index = 1
  
  indices_by_value = {}
  for i in range(n):
      if a[i] not in indices_by_value:
          indices_by_value[a[i]] = []
      indices_by_value[a[i]].append(i)

  
  for val in indices_by_value:
      for index in indices_by_value[val]:
          coloring[index] = color_index
          color_index = (color_index % k) + 1
          
  print("YES")
  print(*coloring)

solve()