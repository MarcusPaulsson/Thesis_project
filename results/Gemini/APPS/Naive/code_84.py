def solve():
  n = int(input())
  s = input()

  for i in range(1 << n):
    coloring = ""
    for j in range(n):
      if (i >> j) & 1:
        coloring += '1'
      else:
        coloring += '0'
    
    group0 = ""
    group1 = ""
    for j in range(n):
      if coloring[j] == '0':
        group0 += s[j]
      else:
        group1 += s[j]
    
    group0 = "".join(sorted(group0))
    group1 = "".join(sorted(group1))
    
    merged = ""
    idx0 = 0
    idx1 = 0
    for j in range(n):
      if idx0 < len(group0) and (idx1 == len(group1) or group0[idx0] <= group1[idx1]):
        merged += group0[idx0]
        idx0 += 1
      else:
        merged += group1[idx1]
        idx1 += 1
    
    if merged == "".join(sorted(s)):
      print("YES")
      print(coloring)
      return

  print("NO")

solve()